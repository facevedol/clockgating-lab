"""File with the class that runs the simulation on all designs"""

from src.designs import designs


class Simulator(object):
    """
    Class that will, for each design:
        - setup the designs
        - run the simulation
        - do the report
    """

    def __init__(self, minimum_bitwidth, maximum_fanout, working_dir):
        self.minimum_bitwidth = minimum_bitwidth
        self.maximum_fanout = maximum_fanout
        self.working_dir = working_dir

    def run_designs(self):
        """Run each design with the user settings"""
        for design in designs:
            design.run(self.minimum_bitwidth,
                       self.maximum_fanout)
            design.report(self.working_dir)
