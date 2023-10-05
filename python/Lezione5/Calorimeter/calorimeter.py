import random
import time

import matplotlib.pyplot as plt
import numpy as np

TRUE_ENERGY = 100. #GeV
ENERGY_RESOLUTION = 0.05 #5%
N = 1000000

def python_cal():
    """
    """
    start_time = time.time()
    meas_energy = []
    for i in range(N):
        meas_energy.append(TRUE_ENERGY * random.normalvariate(1., ENERGY_RESOLUTION))
    elapsed_time = time.time() - start_time
    plt.figure("pure python")
    plt.hist(meas_energy, bins=np.linspace(80., 120., 100))
    print('pure-python', elapsed_time)


def numpy_cal():
    """
    """
    start_time = time.time()
    meas_energy = TRUE_ENERGY * np.random.normal(1., ENERGY_RESOLUTION, size=N)
    elapsed_time = time.time() - start_time
    plt.figure('numpy')
    plt.hist(meas_energy, bins=np.linspace(80., 120., 100))
    print('numpy', elapsed_time)

if __name__ == '__main__':
    python_cal()
    numpy_cal()
    plt.show()
