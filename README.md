# 01 Time Bomb Knapsack problem
This is a implementation of the algorithms proposed by this paper:
>Roberto Montemanni, Derek H. Smith,\
Model-based algorithms for the 0-1 Time-Bomb Knapsack Problem,\
Computers & Operations Research,\
Volume 178,\
2025,\
107010,\
ISSN 0305-0548,\
https://doi.org/10.1016/j.cor.2025.107010.\
(https://www.sciencedirect.com/science/article/pii/S0305054825000383)\
Abstract: A stochastic version of the 0–1 Knapsack Problem recently introduced in the literature and named the 0–1 Time-Bomb Knapsack Problem is the topic of the present work. In this problem, in addition to profit and weight, each item is characterized by a probability of exploding, and therefore destroying all the contents of the knapsack, in case it is loaded. The optimization aims at maximizing the expected profit of the selected items, which takes into account also the probabilities of explosion, while fulfilling the capacity constraint. The problem has real-world applications in logistics and cloud computing. In this work, two model-based algorithms are introduced. They are based on partial linearizations of a non-linear model describing the problem. Extensive computational results on the instances available in the literature are presented to position the new methods as the best-performing ones, while comparing against those previously proposed.\
Keywords: 0-1 Knapsack; Time-bomb; Model-based algorithms; Mixed integer linear programming

# How To Run
the folder is structured as follows
```
01-TB-Knapsack
    |
    |--- data/
    |     |--- generated-instances/
    |--- paper/
    |--- results/
    |--- src/
    |     |--- Algorithms/
    |     |         |--- algorithm1.py 
    |     |         |--- algorithm2.py
    |     |         |--- utils.py
    |     |--- Models/
    |     |       |--- modelP.py
    |     |       |--- modelS.py
    |     |--- scalability.py
    |     |--- test.py
    |--- requirements.txt
```
## Create a Virtual Environment
open a terminal inside the folder.\
To create a virtual environment use the following command
```bash
    python -m venv .venv
```
### Activate Virtual Environment
On Windows, run:
```bash
    .venv\Scripts\activate
```

On Unix or MacOS, run:
```bash
    source .venv/bin/activate
```

## Install the dependencies
```bash
    pip install -r requirements.txt
```

## To run test.py
This file is used to test the proposed models/algorithms on simple instances
```bash
    cd test
```
```bash
    python test.py
```

## To run scalability.py
This file is used to test the proposed models/algorithms on instances of increasing size.\
After the script execution, in the **results folder** you can find the logs, the metrics and plots for both the algorithms
```bash
    cd test
```
```bash
    python scalability.py
```