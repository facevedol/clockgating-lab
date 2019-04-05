"""File with all designs implementations"""

from src.design import Design


def reset_designs():
    """Reset the designs stored in this file"""
    new_designs = [
       Design(name="des00",
              gated_factor=1.360010,
              ungated_factor=2.666848,
              cg_factor=3.631245,
              sizing_steps=42.000000,
              reg_groups=[7, 9, 27, 6, 14, 19, 22, 8, 9, 7, 11, 26, 8, 31, 4, 23, 12, 29, 11, 11, 11, 9, 23, 14, 20, 14, 12, 10, 0, 24, 15, 22, 3, 21, 31, 21, 19, 9, 19, 6, 29, 8, 20, 12, 22, 4, 20, 29, 29, 8, 8, 0, 13, 30, 2, 15, 26, 14, 7, 17, 30, 7, 29, 5, 10, 14, 10, 13, 19, 8, 19, 21, 0, 23, 28, 11, 1, 18, 22, 31, 30, 12, 10, 7, 7, 18, 31, 11, 23, 15, 8, 10, 15, 8, 3, 19, 23, 7, 12, 7, 11, 7, 28, 27, 28, 15, 9, 28, 26, 20, 23, 9, 26, 30, 26, 16, 22, 16, 21, 30, 31, 3, 2, 13, 13, 22, 17, 6]),
       Design(name="des01",
              gated_factor=0.220550,
              ungated_factor=1.623068,
              cg_factor=3.121163,
              sizing_steps=53.000000,
              reg_groups=[11, 23, 25, 13, 1, 10, 30, 12, 6, 23, 2, 13, 13, 1, 15, 28, 2, 25, 24, 21, 20, 31, 18, 2, 31, 2, 4, 8, 26, 6, 14, 28, 26, 21, 26, 23, 21, 26, 13, 2, 30, 25, 28, 28, 0, 7, 30, 28, 24, 25, 11, 18, 15, 1, 19, 15, 4, 18, 8, 23, 24, 2, 31, 1, 28, 14, 7, 28, 22, 30, 14, 30, 17, 3, 28, 18, 25, 24, 22, 31, 11, 2, 26, 10, 30, 27, 7, 28, 9, 10, 25, 8, 17, 9, 15, 6, 29, 7, 4, 14, 5, 30, 6, 5, 29, 24, 14, 29, 3, 7, 17, 24, 27, 15, 22, 15, 16, 30, 22, 15, 24, 8, 27, 25, 3, 3, 10, 14]),
       Design(name="des02",
              gated_factor=1.762540,
              ungated_factor=3.339404,
              cg_factor=3.625965,
              sizing_steps=27.000000,
              reg_groups=[18, 31, 23, 7, 29, 17, 30, 23, 24, 3, 13, 13, 6, 14, 6, 20, 29, 12, 7, 4, 31, 25, 27, 7, 30, 2, 9, 24, 0, 7, 21, 8, 28, 2, 11, 2, 11, 21, 17, 4, 6, 2, 7, 30, 12, 28, 4, 20, 31, 17, 24, 3, 5, 28, 22, 8, 2, 24, 22, 27, 11, 23, 3, 18, 18, 7, 6, 4, 6, 25, 8, 24, 10, 1, 7, 17, 4, 28, 8, 9, 6, 30, 13, 27, 18, 18, 1, 19, 30, 18, 8, 6, 11, 28, 19, 30, 10, 2, 13, 31, 7, 6, 13, 20, 27, 8, 31, 22, 1, 31, 20, 6, 20, 5, 28, 31, 19, 15, 17, 21, 21, 22, 24, 4, 13, 9, 26, 15]),
       Design(name="des03",
              gated_factor=1.497432,
              ungated_factor=2.570857,
              cg_factor=3.176459,
              sizing_steps=7.000000,
              reg_groups=[27, 3, 8, 10, 19, 20, 10, 9, 9, 18, 5, 6, 24, 21, 17, 21, 30, 31, 4, 4, 0, 26, 17, 18, 0, 9, 19, 15, 24, 13, 3, 26, 24, 26, 0, 25, 21, 18, 29, 11, 1, 17, 9, 9, 18, 17, 30, 18, 28, 14, 19, 16, 18, 22, 0, 12, 31, 22, 17, 15, 24, 3, 6, 13, 19, 8, 22, 23, 21, 16, 0, 12, 10, 31, 24, 16, 7, 25, 8, 10, 16, 17, 0, 5, 25, 25, 12, 24, 1, 7, 8, 24, 2, 29, 16, 18, 31, 9, 10, 2, 19, 7, 30, 18, 22, 8, 18, 6, 18, 14, 29, 0, 14, 8, 22, 2, 24, 14, 7, 24, 12, 6, 22, 26, 1, 24, 3, 10]),
       Design(name="des04",
              gated_factor=0.347816,
              ungated_factor=2.779454,
              cg_factor=2.932682,
              sizing_steps=58.000000,
              reg_groups=[23, 13, 28, 4, 10, 26, 5, 6, 21, 20, 9, 2, 19, 0, 11, 7, 0, 25, 13, 0, 24, 30, 5, 30, 29, 7, 12, 19, 17, 2, 25, 15, 16, 14, 3, 2, 24, 20, 0, 24, 29, 11, 25, 0, 4, 25, 22, 26, 25, 6, 10, 10, 8, 22, 6, 10, 0, 18, 1, 11, 15, 21, 24, 11, 30, 17, 30, 17, 28, 3, 30, 29, 26, 11, 8, 2, 15, 29, 29, 1, 5, 21, 13, 26, 23, 7, 4, 5, 8, 10, 24, 13, 27, 7, 31, 13, 24, 8, 7, 11, 14, 24, 14, 22, 26, 6, 22, 1, 11, 19, 31, 31, 0, 12, 27, 0, 30, 24, 2, 10, 6, 19, 31, 14, 21, 7, 0, 22]),
       Design(name="des05",
              gated_factor=1.619886,
              ungated_factor=2.782570,
              cg_factor=3.865448,
              sizing_steps=59.000000,
              reg_groups=[12, 30, 22, 3, 9, 15, 6, 23, 28, 16, 8, 27, 29, 18, 16, 6, 30, 11, 11, 17, 29, 30, 29, 3, 15, 25, 15, 15, 20, 15, 8, 0, 9, 29, 2, 1, 5, 27, 8, 1, 26, 12, 3, 26, 18, 2, 13, 19, 4, 28, 25, 10, 7, 29, 11, 10, 19, 2, 31, 4, 8, 24, 16, 18, 5, 28, 16, 4, 18, 31, 17, 8, 13, 10, 5, 28, 13, 9, 0, 14, 14, 11, 15, 9, 14, 3, 30, 6, 13, 5, 12, 11, 19, 11, 26, 14, 5, 28, 9, 8, 28, 2, 20, 10, 5, 28, 0, 31, 15, 10, 28, 16, 28, 26, 5, 7, 27, 22, 16, 17, 18, 15, 9, 8, 8, 16, 25, 14]),
       Design(name="des06",
              gated_factor=1.639326,
              ungated_factor=4.039363,
              cg_factor=2.190000,
              sizing_steps=60.000000,
              reg_groups=[2, 2, 10, 2, 18, 15, 8, 23, 29, 21, 0, 30, 8, 19, 12, 7, 6, 16, 3, 4, 29, 21, 20, 1, 10, 10, 9, 19, 7, 29, 21, 8, 17, 20, 10, 19, 29, 14, 5, 8, 12, 5, 18, 1, 30, 8, 5, 0, 27, 11, 29, 17, 14, 8, 9, 16, 4, 5, 21, 28, 18, 3, 21, 25, 29, 17, 7, 27, 17, 31, 9, 15, 23, 17, 18, 3, 31, 13, 13, 0, 30, 15, 5, 19, 21, 27, 15, 18, 20, 3, 11, 28, 31, 19, 26, 21, 7, 14, 17, 19, 13, 26, 12, 4, 5, 21, 23, 17, 2, 19, 23, 4, 0, 25, 23, 19, 11, 27, 15, 21, 28, 29, 8, 9, 19, 31, 7, 19]),
       Design(name="des07",
              gated_factor=0.585947,
              ungated_factor=2.122285,
              cg_factor=3.340014,
              sizing_steps=37.000000,
              reg_groups=[10, 10, 22, 12, 31, 13, 3, 13, 24, 30, 29, 25, 11, 27, 29, 29, 5, 8, 17, 15, 16, 21, 22, 21, 5, 19, 17, 4, 22, 9, 7, 13, 15, 10, 24, 4, 0, 24, 25, 23, 3, 14, 18, 11, 28, 5, 4, 29, 18, 31, 3, 8, 28, 17, 29, 8, 5, 21, 25, 24, 23, 27, 24, 22, 12, 3, 0, 23, 1, 23, 2, 20, 27, 28, 9, 17, 13, 3, 26, 21, 3, 21, 11, 22, 17, 30, 28, 12, 20, 20, 27, 30, 6, 23, 7, 5, 2, 26, 3, 25, 14, 14, 14, 27, 31, 30, 8, 29, 15, 1, 2, 19, 31, 9, 15, 10, 31, 7, 17, 31, 26, 7, 23, 25, 17, 13, 3, 23]),
       Design(name="des08",
              gated_factor=0.138596,
              ungated_factor=2.530831,
              cg_factor=3.371850,
              sizing_steps=19.000000,
              reg_groups=[22, 11, 13, 7, 25, 19, 9, 15, 6, 24, 14, 6, 13, 14, 25, 10, 30, 25, 2, 10, 5, 17, 7, 21, 24, 25, 3, 25, 5, 29, 8, 21, 26, 4, 2, 27, 30, 21, 5, 30, 0, 15, 24, 11, 17, 3, 28, 16, 1, 6, 22, 22, 28, 21, 24, 22, 9, 17, 17, 30, 1, 19, 11, 23, 4, 30, 29, 23, 4, 30, 13, 21, 23, 13, 17, 4, 3, 10, 0, 0, 30, 26, 25, 18, 22, 1, 25, 6, 5, 11, 25, 13, 22, 2, 8, 28, 27, 21, 14, 31, 21, 13, 18, 5, 26, 25, 9, 6, 6, 15, 0, 2, 18, 31, 15, 12, 24, 0, 3, 14, 6, 0, 2, 31, 8, 29, 20, 1]),
       Design(name="des09",
              gated_factor=1.963935,
              ungated_factor=4.895086,
              cg_factor=3.506777,
              sizing_steps=23.000000,
              reg_groups=[5, 12, 8, 23, 24, 0, 7, 14, 7, 7, 27, 15, 9, 23, 6, 14, 8, 3, 17, 7, 4, 23, 20, 7, 25, 9, 7, 27, 19, 11, 27, 13, 18, 12, 10, 20, 12, 5, 8, 31, 15, 0, 17, 19, 13, 4, 23, 16, 29, 24, 2, 10, 11, 1, 15, 8, 19, 0, 28, 25, 28, 16, 14, 4, 23, 15, 21, 8, 15, 1, 9, 12, 2, 11, 27, 18, 7, 25, 7, 13, 1, 27, 3, 24, 20, 2, 19, 20, 14, 3, 25, 26, 26, 18, 29, 0, 28, 15, 27, 12, 0, 16, 24, 26, 29, 2, 26, 23, 14, 2, 2, 23, 26, 21, 0, 25, 30, 18, 31, 16, 28, 10, 8, 26, 7, 3, 23, 9]),
       Design(name="des10",
              gated_factor=1.685550,
              ungated_factor=3.781264,
              cg_factor=2.928142,
              sizing_steps=10.000000,
              reg_groups=[11, 2, 5, 22, 5, 24, 30, 11, 18, 6, 14, 20, 27, 23, 23, 3, 30, 26, 20, 12, 24, 12, 4, 10, 7, 10, 24, 0, 12, 6, 1, 17, 24, 0, 3, 11, 15, 30, 3, 11, 2, 19, 30, 23, 17, 4, 18, 26, 31, 4, 3, 7, 23, 1, 5, 19, 19, 0, 6, 7, 16, 18, 19, 18, 4, 10, 14, 13, 8, 9, 14, 29, 13, 16, 14, 22, 16, 30, 2, 12, 14, 2, 31, 21, 23, 4, 23, 9, 24, 10, 9, 17, 25, 10, 7, 3, 27, 28, 13, 8, 10, 4, 9, 24, 9, 31, 19, 6, 25, 6, 4, 21, 15, 26, 10, 3, 14, 3, 8, 8, 19, 8, 1, 6, 19, 15, 29, 20]),
       Design(name="des11",
              gated_factor=1.902926,
              ungated_factor=3.910357,
              cg_factor=2.860279,
              sizing_steps=13.000000,
              reg_groups=[21, 27, 8, 8, 15, 21, 17, 4, 20, 27, 24, 17, 13, 12, 1, 21, 18, 3, 1, 23, 15, 20, 3, 14, 4, 19, 30, 1, 11, 22, 31, 8, 30, 22, 2, 18, 2, 16, 22, 14, 31, 24, 1, 23, 31, 9, 28, 8, 9, 27, 17, 14, 20, 24, 29, 9, 15, 19, 20, 5, 23, 2, 24, 3, 15, 7, 13, 28, 24, 3, 12, 1, 27, 26, 8, 13, 4, 15, 0, 4, 9, 11, 6, 15, 27, 30, 22, 3, 29, 31, 18, 22, 21, 24, 13, 14, 28, 1, 30, 27, 19, 11, 5, 21, 15, 25, 8, 25, 1, 1, 17, 17, 6, 21, 15, 11, 17, 28, 24, 27, 26, 12, 19, 2, 18, 5, 7, 17]),
       Design(name="des12",
              gated_factor=1.738585,
              ungated_factor=3.176330,
              cg_factor=2.870796,
              sizing_steps=6.000000,
              reg_groups=[11, 27, 14, 19, 18, 6, 28, 25, 12, 6, 22, 19, 23, 10, 21, 7, 28, 31, 5, 26, 1, 25, 7, 24, 17, 9, 11, 18, 23, 0, 25, 11, 25, 6, 29, 7, 11, 26, 8, 24, 13, 0, 4, 20, 27, 10, 15, 4, 28, 3, 9, 28, 11, 29, 16, 30, 22, 14, 23, 24, 8, 30, 25, 1, 29, 21, 11, 9, 18, 0, 1, 25, 17, 16, 3, 10, 19, 10, 1, 30, 25, 17, 1, 23, 25, 21, 14, 25, 19, 4, 4, 25, 16, 30, 11, 12, 11, 14, 25, 25, 16, 4, 5, 18, 3, 15, 19, 15, 26, 6, 30, 7, 6, 1, 16, 7, 6, 22, 26, 28, 0, 6, 29, 22, 5, 24, 3, 28]),
       Design(name="des13",
              gated_factor=1.962990,
              ungated_factor=4.161640,
              cg_factor=3.969921,
              sizing_steps=22.000000,
              reg_groups=[3, 20, 17, 6, 25, 0, 23, 13, 23, 18, 29, 11, 20, 17, 2, 24, 6, 7, 23, 4, 16, 29, 15, 16, 3, 29, 6, 20, 6, 31, 29, 1, 19, 18, 3, 11, 26, 4, 2, 17, 22, 4, 9, 22, 4, 17, 23, 22, 28, 12, 1, 29, 30, 1, 0, 29, 1, 23, 30, 12, 28, 4, 31, 29, 25, 10, 18, 0, 23, 6, 21, 2, 2, 16, 21, 25, 9, 14, 18, 9, 1, 26, 11, 16, 23, 13, 0, 3, 23, 20, 6, 8, 3, 0, 31, 0, 3, 31, 4, 17, 18, 3, 2, 23, 11, 18, 18, 8, 13, 4, 10, 25, 16, 7, 3, 30, 31, 8, 14, 13, 2, 4, 11, 20, 9, 14, 24, 7]),
       Design(name="des14",
              gated_factor=1.455031,
              ungated_factor=2.655144,
              cg_factor=3.476270,
              sizing_steps=9.000000,
              reg_groups=[3, 0, 16, 7, 11, 23, 18, 25, 16, 24, 17, 22, 25, 28, 22, 15, 20, 7, 15, 7, 30, 1, 5, 25, 10, 7, 6, 14, 19, 9, 26, 29, 19, 18, 30, 2, 21, 6, 9, 14, 27, 2, 4, 9, 30, 13, 10, 25, 7, 17, 2, 17, 20, 27, 9, 1, 6, 22, 12, 5, 25, 6, 4, 11, 13, 0, 27, 20, 31, 9, 9, 12, 11, 2, 9, 26, 28, 27, 21, 14, 1, 9, 6, 14, 24, 16, 27, 25, 30, 22, 1, 5, 15, 18, 1, 10, 24, 16, 18, 30, 24, 24, 30, 12, 8, 27, 2, 3, 24, 13, 23, 31, 1, 5, 28, 15, 8, 22, 14, 4, 29, 11, 20, 15, 27, 19, 6, 12]),
       Design(name="des15",
              gated_factor=1.912823,
              ungated_factor=4.055302,
              cg_factor=3.637001,
              sizing_steps=58.000000,
              reg_groups=[16, 28, 5, 6, 19, 12, 19, 23, 18, 14, 23, 30, 7, 8, 16, 11, 27, 27, 6, 6, 22, 21, 5, 12, 28, 31, 18, 19, 26, 26, 28, 16, 10, 4, 8, 1, 7, 1, 21, 20, 10, 29, 0, 6, 16, 13, 5, 1, 24, 31, 30, 13, 25, 9, 14, 28, 24, 23, 5, 29, 9, 28, 0, 11, 13, 31, 2, 23, 23, 21, 21, 23, 25, 29, 31, 11, 11, 7, 27, 4, 19, 14, 15, 1, 18, 7, 24, 29, 22, 13, 29, 20, 22, 8, 2, 23, 31, 17, 12, 11, 10, 13, 5, 10, 18, 18, 19, 27, 13, 29, 15, 15, 6, 5, 31, 2, 27, 3, 16, 22, 3, 11, 11, 6, 28, 4, 17, 23]),
       Design(name="des16",
              gated_factor=0.676354,
              ungated_factor=2.020557,
              cg_factor=3.569391,
              sizing_steps=44.000000,
              reg_groups=[29, 5, 8, 8, 24, 22, 24, 18, 11, 31, 9, 27, 23, 9, 10, 1, 29, 29, 15, 27, 18, 11, 27, 11, 5, 4, 29, 12, 29, 31, 10, 30, 9, 24, 15, 25, 15, 26, 12, 10, 13, 7, 16, 31, 27, 28, 3, 27, 18, 11, 30, 17, 23, 25, 7, 30, 1, 21, 18, 0, 10, 22, 24, 29, 2, 5, 9, 24, 20, 19, 2, 26, 1, 26, 30, 21, 2, 7, 31, 23, 16, 31, 10, 26, 11, 25, 16, 15, 13, 10, 31, 26, 28, 20, 23, 31, 10, 23, 3, 0, 30, 19, 6, 10, 6, 20, 22, 11, 10, 29, 11, 14, 12, 11, 18, 3, 18, 1, 5, 8, 25, 31, 22, 27, 28, 3, 7, 28]),
       Design(name="des17",
              gated_factor=0.728448,
              ungated_factor=2.970643,
              cg_factor=2.864375,
              sizing_steps=43.000000,
              reg_groups=[10, 10, 7, 19, 16, 21, 22, 1, 11, 23, 13, 23, 12, 3, 4, 17, 28, 7, 29, 17, 21, 2, 14, 30, 15, 13, 5, 23, 31, 23, 17, 24, 31, 11, 23, 0, 18, 21, 7, 0, 30, 4, 9, 26, 24, 14, 19, 9, 4, 12, 25, 18, 14, 18, 16, 24, 5, 13, 7, 3, 21, 31, 24, 19, 21, 11, 19, 10, 26, 0, 10, 3, 15, 1, 10, 30, 6, 26, 27, 4, 13, 25, 25, 7, 9, 13, 17, 31, 19, 29, 30, 9, 21, 16, 12, 13, 8, 21, 4, 24, 12, 24, 12, 22, 24, 24, 27, 16, 29, 13, 2, 25, 17, 0, 8, 7, 28, 18, 7, 30, 3, 14, 31, 6, 13, 7, 6, 17]),
       Design(name="des18",
              gated_factor=1.579931,
              ungated_factor=3.964965,
              cg_factor=3.565936,
              sizing_steps=38.000000,
              reg_groups=[3, 20, 14, 20, 4, 28, 16, 26, 6, 28, 2, 26, 8, 9, 1, 6, 29, 16, 19, 23, 1, 30, 0, 28, 5, 19, 0, 5, 7, 16, 12, 29, 4, 28, 13, 17, 9, 12, 10, 11, 1, 6, 17, 23, 29, 8, 27, 15, 24, 8, 11, 26, 14, 28, 24, 13, 15, 28, 23, 29, 31, 20, 9, 30, 27, 28, 30, 15, 17, 17, 31, 24, 23, 21, 10, 21, 7, 1, 16, 3, 27, 9, 30, 23, 13, 24, 12, 28, 6, 29, 1, 4, 7, 7, 21, 22, 4, 29, 21, 3, 15, 19, 15, 13, 29, 10, 19, 21, 9, 19, 25, 20, 14, 12, 20, 5, 7, 18, 12, 27, 3, 8, 17, 14, 20, 24, 9, 19]),
       Design(name="des19",
              gated_factor=1.779085,
              ungated_factor=3.640209,
              cg_factor=3.145636,
              sizing_steps=7.000000,
              reg_groups=[6, 23, 1, 21, 17, 9, 1, 5, 26, 9, 23, 18, 29, 7, 8, 10, 14, 2, 25, 19, 22, 16, 30, 12, 21, 11, 10, 19, 25, 26, 20, 30, 16, 24, 23, 9, 1, 13, 4, 11, 23, 25, 16, 17, 30, 15, 20, 2, 1, 26, 0, 9, 27, 22, 20, 13, 9, 29, 6, 27, 3, 31, 0, 20, 4, 30, 21, 2, 28, 19, 31, 6, 2, 24, 30, 22, 23, 3, 13, 28, 12, 18, 2, 30, 12, 0, 14, 5, 5, 19, 13, 28, 9, 24, 6, 25, 29, 2, 18, 9, 10, 10, 4, 2, 3, 29, 14, 17, 2, 16, 22, 15, 26, 15, 6, 27, 31, 26, 25, 27, 31, 6, 23, 18, 25, 30, 30, 4]),
       Design(name="des20",
              gated_factor=1.543067,
              ungated_factor=2.827150,
              cg_factor=3.633983,
              sizing_steps=45.000000,
              reg_groups=[6, 3, 6, 2, 8, 1, 17, 16, 28, 7, 8, 26, 24, 24, 19, 13, 21, 17, 2, 2, 16, 29, 19, 19, 0, 9, 7, 31, 11, 31, 16, 26, 7, 26, 27, 12, 14, 22, 25, 10, 17, 11, 29, 15, 1, 24, 23, 11, 22, 12, 5, 23, 1, 26, 26, 9, 25, 13, 21, 0, 3, 3, 7, 26, 2, 8, 0, 3, 6, 24, 12, 14, 10, 4, 23, 26, 10, 31, 25, 13, 6, 10, 10, 1, 22, 26, 10, 12, 11, 16, 23, 7, 24, 12, 3, 6, 14, 3, 19, 1, 11, 6, 12, 6, 16, 27, 23, 25, 24, 7, 0, 10, 22, 9, 23, 10, 24, 23, 24, 31, 4, 5, 23, 17, 5, 5, 6, 20]),
       Design(name="des21",
              gated_factor=0.577253,
              ungated_factor=2.889849,
              cg_factor=3.607448,
              sizing_steps=45.000000,
              reg_groups=[5, 29, 24, 14, 5, 23, 6, 27, 21, 26, 31, 31, 20, 4, 28, 25, 1, 13, 29, 16, 31, 3, 16, 24, 12, 21, 10, 25, 30, 19, 16, 20, 19, 8, 24, 30, 24, 7, 0, 25, 13, 8, 1, 28, 4, 31, 5, 23, 21, 22, 28, 5, 19, 6, 20, 16, 4, 17, 28, 3, 2, 10, 9, 24, 15, 13, 19, 23, 24, 2, 24, 18, 7, 7, 8, 24, 17, 24, 28, 0, 27, 21, 5, 15, 30, 3, 11, 31, 16, 29, 29, 12, 16, 31, 23, 24, 11, 28, 9, 25, 31, 31, 28, 9, 24, 15, 17, 15, 1, 9, 18, 20, 7, 5, 27, 19, 14, 22, 1, 10, 16, 24, 22, 14, 9, 3, 2, 10]),
       Design(name="des22",
              gated_factor=1.327807,
              ungated_factor=3.244060,
              cg_factor=3.839113,
              sizing_steps=35.000000,
              reg_groups=[30, 1, 5, 17, 19, 26, 2, 15, 30, 15, 16, 27, 0, 25, 0, 28, 15, 26, 6, 2, 11, 28, 30, 11, 15, 10, 16, 22, 22, 15, 27, 1, 15, 20, 6, 6, 29, 1, 5, 31, 21, 2, 23, 26, 31, 18, 17, 3, 29, 6, 23, 4, 31, 28, 29, 17, 27, 18, 20, 30, 19, 10, 18, 3, 17, 13, 4, 5, 11, 8, 11, 9, 25, 1, 1, 14, 1, 29, 28, 23, 5, 20, 21, 9, 30, 18, 6, 8, 30, 27, 29, 22, 7, 22, 0, 17, 17, 2, 29, 28, 8, 16, 16, 22, 22, 18, 27, 13, 16, 27, 30, 4, 7, 15, 26, 12, 3, 0, 28, 29, 19, 8, 30, 7, 13, 27, 26, 16]),
       Design(name="des23",
              gated_factor=1.614722,
              ungated_factor=4.060107,
              cg_factor=3.828736,
              sizing_steps=52.000000,
              reg_groups=[8, 1, 12, 19, 3, 12, 14, 30, 23, 31, 31, 11, 16, 7, 23, 22, 13, 9, 23, 18, 0, 29, 6, 23, 14, 23, 0, 14, 2, 12, 29, 9, 12, 17, 1, 31, 3, 17, 31, 16, 6, 19, 16, 16, 26, 0, 11, 0, 19, 7, 27, 15, 12, 13, 0, 11, 5, 3, 19, 17, 13, 24, 19, 31, 21, 17, 21, 7, 25, 8, 12, 16, 25, 8, 12, 14, 11, 23, 5, 17, 10, 21, 16, 20, 23, 3, 13, 30, 28, 1, 18, 27, 8, 29, 17, 10, 1, 31, 29, 22, 27, 20, 25, 4, 29, 1, 29, 27, 21, 21, 26, 12, 17, 16, 1, 15, 28, 26, 4, 2, 30, 3, 29, 13, 1, 28, 31, 3]),
       Design(name="des24",
              gated_factor=1.263629,
              ungated_factor=2.462150,
              cg_factor=3.870188,
              sizing_steps=54.000000,
              reg_groups=[4, 25, 25, 0, 14, 12, 5, 18, 26, 0, 17, 7, 9, 9, 12, 9, 13, 14, 8, 10, 12, 28, 3, 30, 19, 13, 11, 5, 18, 29, 11, 29, 31, 31, 9, 28, 27, 11, 21, 16, 19, 14, 9, 1, 15, 11, 9, 24, 29, 14, 31, 9, 31, 28, 19, 31, 19, 19, 12, 13, 20, 5, 2, 18, 5, 24, 19, 10, 5, 23, 17, 16, 21, 12, 20, 24, 0, 11, 12, 1, 1, 9, 21, 13, 23, 28, 1, 26, 5, 18, 3, 9, 6, 8, 31, 9, 0, 11, 7, 1, 13, 25, 16, 0, 8, 3, 1, 6, 6, 20, 20, 7, 2, 15, 12, 0, 19, 30, 27, 30, 23, 3, 26, 15, 25, 20, 17, 8]),
       Design(name="des25",
              gated_factor=1.450399,
              ungated_factor=2.537853,
              cg_factor=3.654372,
              sizing_steps=38.000000,
              reg_groups=[0, 7, 26, 31, 25, 4, 4, 4, 9, 29, 2, 20, 15, 30, 28, 0, 27, 0, 6, 18, 18, 6, 16, 12, 7, 25, 11, 31, 20, 23, 2, 2, 27, 28, 4, 14, 20, 5, 7, 12, 30, 18, 4, 3, 10, 31, 7, 24, 20, 15, 22, 17, 15, 4, 24, 1, 15, 1, 24, 24, 0, 12, 12, 21, 12, 30, 17, 11, 8, 15, 16, 3, 8, 12, 21, 1, 13, 26, 11, 27, 15, 21, 0, 22, 31, 0, 4, 14, 13, 13, 22, 17, 2, 14, 29, 10, 28, 10, 22, 16, 17, 21, 22, 14, 19, 26, 25, 5, 28, 8, 11, 26, 6, 14, 30, 21, 2, 10, 11, 23, 14, 17, 27, 17, 30, 10, 19, 8]),
       Design(name="des26",
              gated_factor=0.946529,
              ungated_factor=2.607676,
              cg_factor=3.485675,
              sizing_steps=59.000000,
              reg_groups=[4, 18, 0, 20, 30, 9, 16, 11, 30, 31, 12, 7, 6, 15, 28, 30, 19, 8, 17, 22, 11, 11, 7, 0, 31, 24, 6, 9, 14, 23, 11, 13, 9, 10, 23, 17, 26, 31, 27, 31, 30, 23, 18, 1, 2, 14, 26, 6, 26, 26, 1, 6, 0, 1, 2, 11, 27, 5, 8, 15, 4, 4, 13, 16, 16, 2, 26, 4, 5, 9, 10, 19, 7, 1, 28, 9, 23, 19, 14, 27, 25, 27, 27, 29, 31, 16, 26, 27, 29, 14, 2, 3, 3, 18, 15, 13, 23, 15, 25, 21, 15, 11, 6, 10, 28, 18, 20, 15, 1, 23, 16, 31, 26, 25, 27, 4, 4, 16, 29, 28, 28, 17, 31, 16, 21, 3, 12, 9]),
       Design(name="des27",
              gated_factor=1.762470,
              ungated_factor=3.802568,
              cg_factor=3.816939,
              sizing_steps=27.000000,
              reg_groups=[0, 13, 25, 4, 7, 8, 10, 7, 23, 28, 18, 1, 21, 19, 7, 27, 30, 8, 31, 14, 3, 30, 11, 27, 20, 25, 26, 1, 7, 26, 9, 7, 4, 21, 8, 26, 4, 12, 23, 19, 5, 21, 3, 29, 7, 19, 12, 16, 6, 13, 2, 24, 0, 30, 22, 21, 22, 21, 10, 17, 22, 2, 6, 3, 0, 8, 18, 28, 8, 21, 18, 13, 20, 16, 0, 31, 11, 10, 22, 7, 15, 25, 0, 19, 6, 3, 13, 15, 25, 9, 11, 8, 28, 28, 31, 3, 29, 16, 29, 5, 25, 11, 8, 1, 2, 29, 22, 13, 10, 18, 23, 23, 21, 13, 14, 17, 31, 9, 13, 17, 10, 9, 5, 18, 11, 8, 2, 19]),
       Design(name="des28",
              gated_factor=0.256635,
              ungated_factor=1.407646,
              cg_factor=3.598414,
              sizing_steps=32.000000,
              reg_groups=[14, 25, 2, 10, 31, 1, 30, 22, 28, 18, 8, 31, 4, 24, 4, 25, 4, 25, 5, 23, 4, 8, 27, 1, 6, 13, 1, 10, 22, 18, 21, 3, 26, 28, 17, 4, 17, 6, 27, 10, 16, 29, 27, 0, 13, 3, 23, 18, 2, 26, 10, 10, 27, 9, 28, 9, 15, 11, 10, 14, 13, 22, 23, 29, 21, 11, 24, 27, 26, 14, 21, 15, 24, 13, 13, 24, 2, 18, 12, 31, 7, 0, 17, 25, 28, 15, 16, 22, 5, 24, 3, 19, 5, 25, 0, 25, 0, 10, 7, 26, 26, 7, 26, 21, 3, 6, 1, 26, 31, 22, 25, 28, 3, 16, 18, 21, 7, 20, 8, 11, 25, 14, 7, 18, 13, 24, 29, 5]),
       Design(name="des29",
              gated_factor=1.473694,
              ungated_factor=2.869445,
              cg_factor=3.111669,
              sizing_steps=4.000000,
              reg_groups=[25, 2, 18, 5, 13, 12, 13, 14, 23, 26, 14, 23, 11, 22, 28, 19, 1, 14, 4, 7, 20, 25, 23, 23, 16, 19, 8, 14, 17, 9, 2, 19, 3, 21, 7, 5, 25, 19, 5, 22, 28, 1, 10, 9, 22, 21, 31, 19, 23, 30, 7, 15, 10, 25, 23, 10, 12, 0, 16, 11, 1, 6, 23, 6, 30, 17, 27, 5, 31, 10, 0, 28, 22, 19, 3, 18, 9, 17, 18, 16, 20, 20, 30, 23, 20, 14, 13, 1, 15, 27, 28, 19, 22, 27, 24, 31, 17, 1, 13, 27, 5, 30, 27, 14, 15, 15, 28, 6, 3, 2, 9, 16, 22, 11, 20, 19, 2, 1, 10, 2, 31, 2, 4, 19, 7, 17, 13, 21]),
       Design(name="des30",
              gated_factor=0.878789,
              ungated_factor=3.877141,
              cg_factor=3.825306,
              sizing_steps=3.000000,
              reg_groups=[3, 26, 13, 12, 13, 1, 23, 29, 19, 29, 17, 19, 30, 22, 14, 29, 31, 29, 10, 13, 29, 3, 18, 6, 5, 15, 8, 30, 31, 7, 28, 31, 2, 12, 10, 1, 18, 6, 12, 22, 20, 29, 31, 2, 13, 0, 13, 21, 14, 12, 1, 31, 9, 9, 22, 11, 29, 7, 13, 31, 20, 14, 13, 4, 1, 22, 11, 3, 25, 5, 5, 4, 21, 22, 2, 3, 3, 20, 28, 0, 7, 11, 7, 22, 10, 5, 7, 0, 24, 7, 20, 29, 21, 13, 25, 5, 5, 8, 1, 18, 18, 4, 6, 15, 15, 1, 4, 3, 14, 31, 8, 24, 19, 15, 15, 4, 25, 9, 18, 5, 29, 10, 6, 0, 15, 26, 24, 15]),
       Design(name="des31",
              gated_factor=0.170228,
              ungated_factor=2.047625,
              cg_factor=3.593002,
              sizing_steps=38.000000,
              reg_groups=[16, 28, 4, 14, 6, 6, 8, 20, 5, 10, 22, 0, 19, 4, 19, 9, 12, 28, 10, 7, 26, 13, 19, 6, 8, 9, 6, 16, 28, 31, 9, 8, 20, 20, 0, 29, 4, 7, 4, 21, 29, 18, 23, 11, 30, 18, 14, 31, 10, 13, 8, 10, 0, 8, 31, 6, 30, 0, 30, 8, 29, 28, 23, 2, 22, 18, 0, 29, 27, 30, 20, 1, 21, 3, 8, 17, 14, 5, 1, 8, 27, 17, 6, 17, 13, 24, 23, 18, 1, 21, 9, 16, 22, 24, 15, 18, 26, 8, 26, 10, 26, 14, 14, 17, 13, 1, 26, 0, 1, 14, 6, 13, 9, 24, 28, 8, 9, 3, 8, 7, 18, 28, 22, 17, 11, 30, 6, 17]),
       Design(name="des32",
              gated_factor=1.229213,
              ungated_factor=3.401004,
              cg_factor=3.956885,
              sizing_steps=46.000000,
              reg_groups=[1, 9, 20, 10, 11, 18, 24, 26, 2, 11, 16, 23, 30, 21, 10, 18, 12, 3, 22, 10, 13, 29, 3, 2, 28, 1, 20, 8, 7, 28, 16, 31, 13, 9, 9, 17, 15, 4, 22, 29, 8, 0, 21, 20, 7, 30, 21, 9, 3, 27, 6, 27, 19, 29, 19, 14, 14, 23, 9, 13, 16, 30, 15, 12, 13, 4, 30, 27, 16, 18, 26, 11, 2, 17, 21, 11, 30, 5, 7, 19, 14, 23, 10, 0, 30, 25, 20, 20, 25, 8, 14, 2, 14, 6, 3, 17, 17, 11, 16, 27, 25, 29, 10, 26, 3, 7, 30, 1, 1, 29, 25, 28, 6, 20, 9, 6, 2, 6, 24, 26, 5, 20, 23, 28, 26, 19, 25, 23]),
       Design(name="des33",
              gated_factor=1.432894,
              ungated_factor=3.410772,
              cg_factor=3.988129,
              sizing_steps=7.000000,
              reg_groups=[7, 17, 1, 17, 26, 31, 16, 29, 20, 1, 10, 22, 4, 25, 20, 13, 15, 13, 13, 18, 3, 9, 0, 1, 23, 15, 1, 27, 27, 25, 14, 2, 22, 23, 0, 12, 26, 13, 8, 25, 19, 7, 10, 12, 1, 12, 13, 31, 18, 24, 16, 0, 8, 3, 1, 15, 1, 0, 23, 23, 20, 13, 19, 19, 18, 6, 29, 24, 26, 23, 5, 6, 10, 8, 28, 8, 24, 11, 28, 10, 9, 17, 31, 20, 30, 9, 21, 0, 30, 16, 19, 18, 2, 17, 31, 25, 2, 8, 30, 30, 21, 12, 15, 0, 24, 0, 23, 3, 0, 5, 23, 30, 30, 11, 3, 14, 31, 30, 25, 9, 14, 6, 5, 8, 5, 27, 26, 9]),
       Design(name="des34",
              gated_factor=1.270807,
              ungated_factor=2.462540,
              cg_factor=3.154253,
              sizing_steps=28.000000,
              reg_groups=[9, 2, 13, 22, 30, 18, 16, 4, 31, 15, 28, 26, 0, 26, 30, 29, 24, 12, 31, 29, 1, 14, 19, 7, 3, 17, 11, 9, 14, 3, 2, 29, 26, 16, 31, 11, 7, 15, 8, 3, 29, 25, 24, 11, 20, 29, 25, 19, 8, 30, 13, 20, 27, 23, 13, 17, 15, 12, 27, 17, 14, 22, 16, 9, 6, 4, 20, 31, 17, 0, 27, 18, 6, 4, 1, 5, 21, 28, 28, 6, 24, 27, 3, 8, 18, 8, 0, 7, 20, 18, 23, 8, 21, 26, 27, 8, 24, 23, 12, 29, 8, 0, 9, 11, 8, 24, 27, 8, 18, 14, 22, 0, 18, 22, 20, 22, 30, 15, 2, 28, 15, 21, 13, 28, 6, 4, 1, 11]),
       Design(name="des35",
              gated_factor=1.198295,
              ungated_factor=3.723607,
              cg_factor=3.654246,
              sizing_steps=44.000000,
              reg_groups=[17, 30, 11, 1, 28, 24, 12, 28, 16, 14, 24, 27, 6, 4, 14, 10, 15, 9, 28, 9, 18, 24, 30, 12, 31, 18, 0, 31, 20, 5, 5, 17, 27, 17, 5, 0, 7, 25, 12, 21, 4, 24, 24, 16, 30, 21, 26, 12, 11, 29, 3, 0, 6, 13, 3, 6, 19, 4, 1, 18, 26, 22, 7, 15, 5, 13, 6, 15, 7, 30, 1, 9, 22, 14, 11, 17, 6, 21, 9, 4, 14, 19, 12, 2, 28, 3, 6, 1, 15, 8, 22, 12, 17, 18, 1, 8, 24, 26, 17, 31, 2, 26, 26, 10, 21, 22, 23, 17, 29, 17, 17, 6, 14, 12, 2, 5, 19, 20, 29, 21, 3, 30, 29, 20, 21, 26, 21, 11]),
       Design(name="des36",
              gated_factor=1.024681,
              ungated_factor=3.080548,
              cg_factor=2.667174,
              sizing_steps=18.000000,
              reg_groups=[25, 9, 31, 5, 26, 1, 18, 22, 27, 16, 20, 1, 19, 29, 12, 14, 3, 23, 21, 1, 10, 27, 14, 30, 31, 2, 24, 11, 9, 31, 20, 21, 19, 9, 11, 26, 11, 7, 16, 5, 20, 2, 22, 5, 22, 9, 29, 18, 9, 7, 28, 30, 4, 20, 19, 6, 28, 10, 7, 30, 22, 2, 7, 28, 3, 29, 5, 17, 9, 9, 17, 0, 31, 3, 12, 22, 22, 21, 7, 5, 12, 10, 3, 2, 28, 22, 5, 17, 12, 26, 15, 9, 6, 8, 19, 28, 11, 12, 11, 19, 28, 27, 29, 21, 19, 19, 12, 15, 12, 24, 1, 9, 29, 17, 30, 2, 5, 9, 26, 24, 5, 13, 22, 23, 16, 2, 1, 14]),
       Design(name="des37",
              gated_factor=0.678411,
              ungated_factor=2.329114,
              cg_factor=2.355890,
              sizing_steps=19.000000,
              reg_groups=[8, 26, 18, 13, 22, 5, 6, 4, 4, 30, 27, 3, 16, 8, 30, 10, 12, 19, 3, 14, 29, 11, 8, 0, 13, 23, 21, 19, 7, 7, 10, 1, 9, 29, 21, 19, 13, 9, 13, 9, 26, 14, 31, 14, 16, 8, 27, 13, 26, 31, 4, 19, 3, 7, 13, 1, 3, 23, 30, 27, 12, 10, 3, 3, 20, 3, 12, 3, 7, 4, 31, 28, 26, 14, 11, 9, 14, 1, 14, 9, 3, 9, 9, 7, 24, 25, 1, 25, 28, 2, 3, 8, 1, 3, 30, 26, 12, 7, 4, 14, 2, 13, 19, 27, 21, 17, 10, 13, 5, 18, 1, 3, 11, 15, 29, 31, 14, 0, 13, 6, 30, 16, 18, 20, 3, 12, 5, 13]),
       Design(name="des38",
              gated_factor=1.335786,
              ungated_factor=4.009737,
              cg_factor=2.390421,
              sizing_steps=29.000000,
              reg_groups=[28, 2, 7, 14, 14, 0, 15, 15, 30, 25, 7, 31, 28, 11, 20, 30, 23, 1, 11, 7, 17, 19, 22, 25, 9, 25, 31, 0, 19, 1, 13, 18, 9, 16, 27, 1, 6, 18, 18, 19, 6, 3, 16, 0, 30, 0, 5, 21, 18, 5, 19, 17, 18, 28, 14, 2, 4, 4, 29, 18, 9, 3, 15, 13, 1, 23, 14, 8, 5, 22, 3, 28, 4, 23, 8, 1, 19, 3, 9, 25, 1, 19, 26, 22, 15, 6, 11, 12, 12, 8, 24, 28, 16, 3, 26, 27, 20, 13, 1, 12, 15, 21, 18, 19, 12, 31, 24, 14, 14, 5, 10, 31, 19, 16, 29, 11, 25, 23, 1, 5, 13, 20, 28, 17, 1, 18, 11, 1]),
       Design(name="des39",
              gated_factor=1.394102,
              ungated_factor=3.964904,
              cg_factor=3.232803,
              sizing_steps=58.000000,
              reg_groups=[13, 5, 15, 5, 16, 22, 9, 12, 18, 8, 5, 26, 12, 16, 20, 16, 20, 9, 22, 13, 1, 24, 25, 8, 21, 30, 23, 4, 18, 20, 12, 9, 21, 10, 23, 0, 8, 4, 27, 14, 24, 9, 18, 13, 12, 27, 12, 25, 8, 18, 16, 11, 21, 18, 2, 14, 14, 5, 24, 5, 20, 28, 16, 20, 2, 4, 22, 2, 12, 15, 21, 31, 6, 2, 2, 29, 16, 13, 22, 27, 11, 30, 30, 11, 14, 14, 19, 1, 1, 26, 20, 2, 11, 29, 27, 7, 1, 18, 13, 25, 4, 9, 24, 8, 29, 17, 19, 2, 5, 8, 24, 17, 8, 5, 7, 17, 31, 0, 5, 12, 3, 4, 30, 3, 19, 29, 16, 15]),
       Design(name="des40",
              gated_factor=1.870060,
              ungated_factor=3.803805,
              cg_factor=2.667635,
              sizing_steps=6.000000,
              reg_groups=[30, 16, 16, 12, 18, 16, 4, 30, 17, 16, 6, 10, 5, 11, 17, 27, 29, 11, 6, 6, 31, 20, 16, 27, 12, 22, 10, 11, 29, 15, 24, 21, 10, 4, 24, 14, 4, 31, 25, 29, 19, 23, 7, 10, 13, 4, 19, 2, 25, 2, 1, 6, 7, 24, 19, 24, 31, 23, 1, 23, 26, 7, 16, 14, 7, 5, 15, 29, 28, 31, 13, 22, 2, 1, 30, 25, 17, 24, 10, 28, 20, 1, 26, 11, 21, 13, 28, 31, 2, 6, 8, 0, 20, 5, 30, 6, 20, 8, 10, 4, 9, 1, 7, 12, 23, 2, 28, 20, 3, 4, 11, 24, 18, 15, 26, 15, 16, 16, 22, 4, 28, 7, 9, 8, 28, 3, 28, 1]),
       Design(name="des41",
              gated_factor=1.100555,
              ungated_factor=4.060953,
              cg_factor=2.404535,
              sizing_steps=47.000000,
              reg_groups=[6, 31, 26, 23, 13, 10, 26, 2, 20, 17, 7, 7, 26, 5, 25, 0, 6, 8, 14, 31, 8, 13, 5, 30, 17, 11, 21, 14, 28, 28, 17, 26, 2, 2, 15, 4, 3, 14, 31, 23, 1, 24, 18, 28, 6, 2, 7, 27, 0, 1, 12, 24, 17, 17, 26, 25, 25, 12, 4, 6, 29, 5, 11, 12, 27, 28, 27, 7, 14, 14, 29, 27, 24, 1, 17, 24, 8, 1, 14, 15, 3, 30, 0, 15, 28, 30, 28, 24, 8, 27, 28, 15, 27, 12, 30, 5, 27, 12, 24, 3, 27, 7, 27, 23, 1, 28, 28, 15, 23, 8, 12, 23, 31, 20, 16, 19, 28, 27, 17, 11, 3, 13, 21, 13, 5, 13, 9, 16]),
       Design(name="des42",
              gated_factor=1.601136,
              ungated_factor=4.463196,
              cg_factor=3.570721,
              sizing_steps=21.000000,
              reg_groups=[4, 10, 14, 23, 16, 27, 13, 27, 3, 30, 6, 5, 1, 27, 6, 1, 18, 19, 29, 8, 5, 4, 28, 12, 30, 7, 13, 17, 9, 12, 19, 15, 12, 18, 17, 18, 16, 23, 30, 21, 19, 3, 2, 21, 18, 29, 9, 15, 2, 13, 20, 27, 25, 23, 28, 29, 14, 5, 28, 13, 1, 12, 23, 3, 27, 20, 11, 0, 20, 0, 13, 28, 22, 13, 13, 5, 31, 2, 8, 2, 3, 9, 1, 28, 15, 7, 12, 0, 3, 5, 23, 17, 15, 18, 16, 8, 26, 29, 11, 18, 15, 10, 23, 21, 23, 2, 2, 6, 7, 30, 27, 19, 22, 14, 26, 19, 22, 29, 1, 27, 27, 7, 21, 25, 24, 16, 29, 1]),
       Design(name="des43",
              gated_factor=1.281383,
              ungated_factor=4.070417,
              cg_factor=2.875465,
              sizing_steps=55.000000,
              reg_groups=[1, 13, 21, 22, 17, 8, 11, 20, 3, 16, 3, 22, 13, 17, 9, 20, 25, 20, 4, 21, 22, 23, 24, 21, 21, 29, 10, 0, 10, 9, 26, 14, 6, 1, 6, 8, 16, 26, 16, 8, 24, 27, 17, 27, 22, 11, 30, 13, 27, 18, 18, 8, 17, 0, 17, 27, 2, 16, 22, 30, 29, 6, 6, 8, 12, 24, 5, 5, 3, 21, 23, 10, 17, 18, 1, 20, 8, 7, 8, 14, 18, 29, 24, 12, 4, 29, 9, 20, 3, 26, 19, 2, 17, 8, 29, 1, 15, 3, 27, 24, 22, 21, 4, 8, 20, 3, 2, 11, 13, 15, 31, 14, 1, 27, 30, 6, 31, 1, 3, 16, 20, 26, 25, 28, 29, 13, 0, 4]),
       Design(name="des44",
              gated_factor=1.081451,
              ungated_factor=3.750302,
              cg_factor=3.340408,
              sizing_steps=62.000000,
              reg_groups=[28, 1, 19, 28, 16, 14, 23, 30, 25, 5, 12, 30, 31, 6, 11, 28, 11, 15, 15, 11, 10, 29, 16, 25, 10, 6, 8, 31, 5, 17, 10, 21, 9, 28, 3, 14, 4, 8, 15, 19, 8, 7, 14, 22, 21, 28, 4, 4, 27, 24, 16, 7, 15, 14, 25, 19, 20, 11, 23, 29, 20, 6, 5, 3, 2, 3, 7, 11, 20, 9, 13, 21, 3, 24, 23, 11, 1, 3, 1, 28, 22, 23, 13, 11, 22, 8, 31, 8, 15, 30, 25, 12, 28, 23, 25, 29, 10, 16, 14, 6, 2, 30, 9, 20, 23, 11, 17, 7, 16, 28, 18, 6, 27, 1, 15, 26, 11, 5, 8, 5, 31, 14, 3, 5, 20, 2, 13, 7]),
       Design(name="des45",
              gated_factor=0.694132,
              ungated_factor=3.473727,
              cg_factor=2.349740,
              sizing_steps=4.000000,
              reg_groups=[24, 29, 26, 21, 21, 13, 13, 14, 7, 7, 16, 1, 0, 20, 24, 8, 1, 18, 11, 31, 21, 5, 21, 18, 7, 18, 23, 15, 14, 16, 2, 26, 8, 19, 31, 27, 29, 10, 23, 31, 5, 2, 19, 24, 21, 11, 11, 8, 24, 20, 18, 11, 19, 10, 17, 27, 2, 0, 1, 24, 14, 16, 16, 23, 22, 19, 25, 17, 12, 27, 3, 10, 31, 4, 17, 14, 22, 27, 25, 8, 12, 16, 3, 25, 20, 0, 8, 17, 19, 6, 4, 10, 12, 15, 5, 26, 11, 13, 23, 2, 29, 25, 18, 22, 29, 11, 8, 2, 2, 25, 14, 1, 2, 11, 29, 8, 17, 31, 31, 28, 10, 22, 14, 27, 20, 22, 14, 27]),
       Design(name="des46",
              gated_factor=1.305357,
              ungated_factor=4.236219,
              cg_factor=2.224518,
              sizing_steps=30.000000,
              reg_groups=[10, 17, 6, 17, 4, 22, 5, 8, 28, 23, 11, 14, 23, 8, 10, 20, 21, 6, 14, 24, 11, 13, 29, 28, 10, 17, 11, 14, 27, 6, 15, 31, 13, 4, 27, 23, 19, 17, 13, 3, 20, 21, 4, 2, 9, 8, 30, 9, 13, 31, 18, 23, 17, 31, 31, 6, 1, 20, 14, 4, 9, 25, 12, 15, 20, 4, 17, 27, 13, 24, 12, 4, 27, 4, 0, 9, 0, 9, 27, 25, 4, 0, 11, 6, 21, 23, 6, 30, 13, 14, 27, 17, 25, 0, 8, 8, 4, 20, 11, 22, 24, 27, 22, 8, 5, 24, 7, 10, 8, 24, 19, 15, 6, 21, 14, 15, 8, 0, 11, 28, 11, 28, 5, 26, 27, 22, 26, 24]),
       Design(name="des47",
              gated_factor=0.537268,
              ungated_factor=2.129427,
              cg_factor=3.682066,
              sizing_steps=5.000000,
              reg_groups=[9, 8, 31, 15, 7, 16, 16, 20, 31, 4, 11, 8, 11, 22, 28, 3, 15, 11, 1, 30, 17, 7, 0, 1, 14, 30, 26, 22, 21, 4, 4, 24, 23, 14, 14, 11, 22, 9, 12, 2, 5, 10, 2, 0, 28, 31, 24, 6, 4, 14, 20, 3, 26, 29, 20, 13, 27, 23, 24, 5, 8, 19, 29, 28, 13, 9, 24, 25, 24, 13, 7, 17, 13, 23, 20, 3, 28, 15, 8, 8, 1, 31, 8, 7, 22, 29, 16, 8, 29, 2, 28, 2, 20, 29, 20, 30, 19, 11, 27, 3, 2, 18, 11, 11, 9, 18, 13, 8, 31, 3, 16, 26, 4, 12, 3, 3, 25, 9, 20, 6, 4, 4, 2, 25, 15, 9, 2, 28]),
       Design(name="des48",
              gated_factor=1.785258,
              ungated_factor=3.450340,
              cg_factor=2.819535,
              sizing_steps=45.000000,
              reg_groups=[20, 12, 21, 31, 29, 19, 30, 8, 17, 20, 16, 12, 16, 5, 14, 10, 20, 8, 6, 22, 27, 15, 14, 14, 22, 28, 13, 16, 23, 28, 27, 16, 16, 30, 17, 18, 26, 18, 30, 15, 22, 3, 2, 12, 9, 25, 19, 29, 21, 13, 20, 18, 13, 21, 22, 7, 28, 3, 6, 7, 27, 10, 28, 12, 10, 2, 24, 8, 0, 26, 27, 16, 20, 2, 29, 13, 21, 0, 0, 16, 7, 2, 24, 26, 22, 22, 4, 8, 12, 28, 7, 13, 5, 2, 25, 16, 18, 10, 1, 21, 6, 21, 23, 10, 13, 22, 16, 14, 6, 3, 3, 27, 6, 17, 27, 0, 8, 31, 27, 18, 2, 30, 15, 24, 16, 10, 13, 15]),
       Design(name="des49",
              gated_factor=0.431337,
              ungated_factor=1.828583,
              cg_factor=2.671407,
              sizing_steps=37.000000,
              reg_groups=[8, 4, 31, 30, 31, 4, 6, 8, 7, 7, 1, 17, 7, 22, 1, 3, 28, 21, 1, 6, 14, 17, 7, 27, 4, 22, 22, 22, 5, 19, 18, 12, 29, 10, 2, 12, 27, 23, 16, 21, 3, 24, 5, 20, 12, 22, 6, 28, 26, 10, 8, 5, 29, 20, 30, 17, 0, 19, 20, 12, 7, 20, 6, 19, 27, 12, 8, 1, 25, 14, 11, 14, 27, 24, 25, 17, 19, 24, 22, 26, 22, 4, 8, 17, 29, 31, 0, 26, 12, 21, 4, 9, 17, 7, 15, 21, 16, 1, 13, 28, 24, 30, 28, 16, 13, 25, 11, 18, 10, 3, 10, 31, 11, 1, 8, 27, 15, 21, 24, 30, 20, 14, 15, 8, 28, 27, 7, 23])
    ]
    return new_designs

designs = reset_designs()
