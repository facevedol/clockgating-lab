"""
Generates the strings for bank distribution:
    reg_groups = [ rand(max_banks_per_size), , ...] ; length = max_regs_per_bank
    ...
    ...
    count times
"""
import random
import argparse


def parse_arguments():
    """
    Parse the input arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--max_regs_per_bank",
                        help="Number of different register bank sizes",
                        type=int)
    parser.add_argument("--max_banks_per_size",
                        help="Maximum number of banks per bank size",
                        type=int)
    parser.add_argument("--count",
                        help="Number of reg_groups to be created",
                        type=int)
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    count = args.count
    max_bank_size = args.max_regs_per_bank
    rand_max = args.max_banks_per_size

    for i in range(count):
        bank_group = []
        for bank_size in range(max_bank_size):
            bank_group.append(random.randrange(0, rand_max))

        gated_factor = random.uniform(0, 2)
        ungated_factor = gated_factor + random.uniform(1, 3)
        cg_factor = random.uniform(2, 4)
        sizing_steps = random.randrange(3, 64)
        print("       Design(name=\"des{:02d}\",".format(i))
        print("              gated_factor={:f},".format(gated_factor))
        print("              ungated_factor={:f},".format(ungated_factor))
        print("              cg_factor={:f},".format(cg_factor))
        print("              sizing_steps={:f},".format(sizing_steps))    
        print("              reg_groups=" + str(bank_group) + "),")
