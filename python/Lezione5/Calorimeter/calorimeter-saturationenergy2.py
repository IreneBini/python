import random
import time

import matplotlib.pyplot as plt
import numpy as np

TRUE_ENERGY = 100. #GeV
ENERGY_RESOLUTION = 0.05 #5%
SATURATION_ENERGY = 108. # no able to measure energy over this number
N = 1000000

def python_cal():
    """
    """
    start_time = time.time()
    meas_energy = []
    for i in range(N):
        E = TRUE_ENERGY * random.normalvariate(1., ENERGY_RESOLUTION)
        if E >= SATURATION_ENERGY:
            E = SATURATION_ENERGY
        meas_energy.append(E)
    elapsed_time = time.time() - start_time
    plt.figure("pure python")
    plt.hist(meas_energy, bins=np.linspace(80., 120., 100))
    print('pure-python', elapsed_time)

def numpy_cal():
    """
    """
    start_time = time.time()
    meas_energy = TRUE_ENERGY * np.random.normal(1., ENERGY_RESOLUTION, size=N)
    meas_energy = np.clip(meas_energy, 0., SATURATION_ENERGY) #overwrite all the element higher
    # than the saturetion, with saturation energy; and all the element lower than 0, with 0
    elapsed_time = time.time() - start_time
    plt.figure('numpy')
    plt.hist(meas_energy, bins=np.linspace(80., 120., 100))
    print('numpy', elapsed_time)

if __name__ == '__main__':
    python_cal()
    numpy_cal()
    plt.show()