# Clock Gating Lab

## Introduction
This lab is aimed to make an introduction on how to look for QoR (Quality of Results) improvements based on simulations.

## Description
In this experience, we simulate the power savings of Clock gate insertion, constrained to the tradeoff between:
* minimum bitwidth: how many registers a clock gate needs to gate to be efficient. It depends on how much power a clock gate uses versus how much power it will save from the registers.
* maximum fanout:  maximum number of registers that a clock gate should gate. Larger number of registers needs bigger clock gates, that consume more power.

## Tasks
* Extract the meaninful data from the reports of each design.
* Use this data to guide the search of an optimum minimum_bitwitdh and maximum_fanout that minimizes the power consumption of each desing ( one combination that suites best to all designs).

## Usage
### Dependencies
* Python 3
### Run
python main.py --minimum_bitwidth \<number> --maximum_fanout \<number>
### Reports
Report for each design are stored in the reports directory.

### Notes
Have fun!