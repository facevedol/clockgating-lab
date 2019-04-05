import argparse
from src.simulator import Simulator
from time import strftime
import os


def parse_arguments():
    """Parse the input arguments:
        -minimum_bitwith: Minimum bitwidth to insert a clock gate
        -maximum_fanout: Maximum number of register that a clock gate can gate
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--minimum_bitwidth",
                        help="Minimum bitwidth to insert a clock gate",
                        type=int)
    parser.add_argument("--maximum_fanout",
                        help="Maximum number of register that a clock gate "
                             "can gate",
                        type=int)
    return parser.parse_args()


def setup_working_dir():
    if not os.path.exists("reports"):
        os.makedirs("reports")

    os.chdir("reports")
    dir_name = strftime("%Y%m%d_%H%M%S")

    if os.path.exists(dir_name):
        id = 0
        tmp_dir_name = dir_name + "." + id
        while os.path.exists(tmp_dir_name):
            id = id + 1
            tmp_dir_name = dir_name + "." + id
        dir_name = tmp_dir_name

    os.makedirs(dir_name)
    os.chdir(dir_name)

    return dir_name


if __name__ == "__main__":
    args = parse_arguments()
    if (2 * args.minimum_bitwidth) > args.maximum_fanout:
        print("The maximum fanout needs to be smaller than twice the "
              "minimum bitwidth plus one.")
        quit()

    print("Starting ...")
    working_dir = setup_working_dir()
    print("Working directory: " + working_dir)
    sim = Simulator(args.minimum_bitwidth, args.maximum_fanout, working_dir)
    sim.run_designs()
    print("Thank you!")
