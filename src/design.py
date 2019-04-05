"""File containing the definition of a Design."""
from math import floor, ceil


class Design(object):
    """
    Defines and stores the reference design representation.
    Each design will be defined with:
        - collection of grouped registers.
        - Information of power consumption of:
            * Gated registers
            * Ungated registers
            * Clock gates

    reg_groups:
        index: number of registers per bank
        value: number of banks

    result:
        index: nop
        value:
            regs: number of registers
            cgs: number of clock gates gating regs
    """
    def __init__(self, name, ungated_factor, gated_factor, cg_factor, sizing_steps, reg_groups):
        self.name = name
        self.ungated_factor = ungated_factor
        self.gated_factor = gated_factor
        self.cg_factor = cg_factor
        self.sizing_steps = sizing_steps
        self.reg_groups = reg_groups
        self.results = []

    def run(self, minimum_bitwidth, maximum_fanout):
        """User setup"""
        self.minimum_bitwidth = minimum_bitwidth
        self.maximum_fanout = maximum_fanout
        self.insertClockGating()
        print("Running design: " + self.name)

    def insertClockGating(self):
        """Insert clock gates for each bank group"""
        for i in range(len(self.reg_groups)):
            if i < self.minimum_bitwidth:
                self.results.append({
                    "regs": self.reg_groups[i] * i,
                    "cgs": 0
                })
                continue
            cgs_per_bank = 1
            if i > self.maximum_fanout:
                cgs_per_bank = (floor(i / self.maximum_fanout) - 1) + 2
            self.results.append({
                "regs": self.reg_groups[i] * i,
                "cgs": cgs_per_bank * self.reg_groups[i]
            })

    def report(self, working_dir):
        """Print the report of the current implementation for this design"""
        print("reporting to: " + working_dir + "/" + self.name + ".rpt")
        summary = self.summarize()
        self.print_summary(summary)

    def summarize(self):
        summary = {
            "cgs": 0,
            "gated": 0,
            "ungated": 0,
            "power": 0
        }
        for r in self.results:
            if r["cgs"] == 0:
                summary["power"] += self.ungated_factor * r["regs"]
                summary["ungated"] += r["regs"]
            else:
                max_cgs = floor(r["regs"]/self.maximum_fanout)
                leftover = r["regs"] - (max_cgs * self.maximum_fanout)
                fanout1 = floor(leftover / 2)
                fanout2 = ceil(leftover / 2)
                pwr = max_cgs * self.cg_power(self.maximum_fanout)
                pwr += self.cg_power(fanout1) + self.cg_power(fanout2)
                pwr += (r["regs"] * self.gated_factor)
                summary["power"] += pwr
                summary["gated"] += r["regs"]
                summary["cgs"] += r["cgs"]
        return summary

    def print_summary(self, summary):
        f = open("{:s}.rpt".format(self.name), "w")
        f.write("For design {:s}: \n".format(self.name))
        f.write("  - Number of clock gates: {:d}\n".format(summary["cgs"]))
        f.write("  - Number of gated registers: {:d}\n".format(summary["gated"]))
        f.write("  - Number of ungated registers: {:d}\n".format(summary["ungated"]))
        f.write("  - Power consumed: {:f}\n".format(summary["power"]))
        f.close()

    def cg_power(self, fanout):
        return (floor(fanout/self.sizing_steps) + 1) ** self.cg_factor + self.cg_factor*10
