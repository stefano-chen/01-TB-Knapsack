from Algorithms.algorithm1 import iterative_algorithm_p
from Algorithms.algorithm2 import iterative_algorithm_s
from pathlib import Path
import logging
import numpy as np

import matplotlib.pyplot as plt

# Logger configuration
logger = logging.getLogger("scalability")
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(message)s")

file_handler = logging.FileHandler(Path("../results/scalability.txt"))
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Parse file content to 01 TB Knapsack instance
def file_to_instance(file_lines):
    weights = []
    profits = []
    survival_probs = []

    n_items, capacity = file_lines[0].strip().split(" ")
    for k in range(1, len(file_lines)):
        weight, profit, survival_prob = file_lines[k].strip().split(" ")
        weights.append(float(weight))
        profits.append(float(profit))
        survival_probs.append(float(survival_prob))

    return int(n_items), float(capacity), weights, profits, survival_probs


if __name__ == "__main__":
    iters_p = []
    durations_p = []
    iters_s = []
    durations_s = []
    MAX_TIME = 120

    # Testing on instances with increasing size
    for i in [100, 500, 1000, 5000]:
        n_instances = 0
        instances_path = Path(f"../data/generated-instances/{i}")
        for file in instances_path.iterdir():
            with open(file) as f:
                n, c, w, p, q = file_to_instance(f.readlines())
                n_instances += 1
                sol, val, _, n_iter, duration = iterative_algorithm_p(n, c, w, p, q, MAX_TIME)
                iters_p.append(n_iter)
                durations_p.append(duration)
                logger.info(f"[AlgP][instance of size {i}] n.{n_instances} => {n_iter} iterations in {duration} seconds [expected profit = {val}]")
                sol, val, _, n_iter, duration = iterative_algorithm_s(n, c, w, p, q, MAX_TIME)
                iters_s.append(n_iter)
                durations_s.append(duration)
                logger.info(f"[AlgS][instance of size {i}] n.{n_instances} => {n_iter} iterations in {duration} seconds [expected profit = {val}]")


    # Log metrics
    logger.info(f"\naverage number of iterations Algorithm P: {np.mean(iters_p)}")
    logger.info(f"average computation time Algorithm P: {np.mean(durations_p)}")
    logger.info(f"average number of iterations Algorithm P on instance of size 100: {np.mean(iters_p[0:90])}")
    logger.info(f"average computation time Algorithm P on instance of size 100: {np.mean(durations_p[0:90])}")
    logger.info(f"average number of iterations Algorithm P on instance of size 500: {np.mean(iters_p[90:180])}")
    logger.info(f"average computation time Algorithm P on instance of size 500: {np.mean(durations_p[90:180])}")
    logger.info(f"average number of iterations Algorithm P on instance of size 1000: {np.mean(iters_p[180:270])}")
    logger.info(f"average computation time Algorithm P on instance of size 1000: {np.mean(durations_p[180:270])}")
    logger.info(f"average number of iterations Algorithm P on instance of size 5000: {np.mean(iters_p[270:])}")
    logger.info(f"average computation time Algorithm P on instance of size 5000: {np.mean(durations_p[270:])}")

    logger.info(f"\naverage number of iterations Algorithm S: {np.mean(iters_s)}")
    logger.info(f"average computation time Algorithm S: {np.mean(durations_s)}")
    logger.info(f"average number of iterations Algorithm S on instance of size 100: {np.mean(iters_s[0:90])}")
    logger.info(f"average computation time Algorithm S on instance of size 100: {np.mean(durations_s[0:90])}")
    logger.info(f"average number of iterations Algorithm S on instance of size 500: {np.mean(iters_s[90:180])}")
    logger.info(f"average computation time Algorithm S on instance of size 500: {np.mean(durations_s[90:180])}")
    logger.info(f"average number of iterations Algorithm S on instance of size 1000: {np.mean(iters_s[180:270])}")
    logger.info(f"average computation time Algorithm S on instance of size 1000: {np.mean(durations_s[180:270])}")
    logger.info(f"average number of iterations Algorithm S on instance of size 5000: {np.mean(iters_s[270:])}")
    logger.info(f"average computation time Algorithm S on instance of size 5000: {np.mean(durations_s[270:])}")

    # Create plots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16,8)) # type: plt.Figure, (plt.Axes, plt.Axes)
    fig.suptitle("Algorithm P")
    ax1.plot(iters_p, "-b", label="iterations")
    ax2.plot(durations_p, "-r", label="compute time")
    ax1.set_xlabel("number of instances")
    ax1.set_ylabel("number of iterations")
    ax1.vlines([90,180,270], 0, 1, color="green", transform=ax1.get_xaxis_transform())
    ax2.set_xlabel("number of instances")
    ax2.set_ylabel("compute time (seconds)")
    ax2.vlines([90,180,270], 0, 1, color="green", transform=ax2.get_xaxis_transform())
    plt.savefig(Path("../results/algorithm_p.png"))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16,8)) # type: plt.Figure, (plt.Axes, plt.Axes)
    fig.suptitle("Algorithm S")
    ax1.plot(iters_s, "-b", label="iterations")
    ax2.plot(durations_s, "-r", label="compute time")
    ax1.set_xlabel("number of instances")
    ax1.set_ylabel("number of iterations")
    ax1.vlines([90,180,270], 0, 1, color="green", transform=ax1.get_xaxis_transform())
    ax2.set_xlabel("number of instances")
    ax2.set_ylabel("compute time (seconds)")
    ax2.vlines([90,180,270], 0, 1, color="green", transform=ax2.get_xaxis_transform())
    plt.savefig(Path("../results/algorithm_s.png"))