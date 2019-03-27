import os
import sys
import json
import scipy
import time
import random

import numpy as np

from job import Job

def sample_job_properties(no_of_cpu, no_of_gpu, ram, storage, driver_cores, overhead_memory):

    job_id = int(time.time())
    job_type = int(random.random()*4)
    no_of_cpu = no_of_cpu
    no_of_gpu = no_of_gpu
    ram = ram
    storage = storage
    priority = random.random()*4
    # time is in seconds
    if job_type == 0:
        # ML job
        time = int(random.random()*86400*7)
    elif job_type == 1:
        # web job
        time = int(random.random())
    elif job_type == 2:
        # database job
        time = int(random.random()*60)
    else:
        # indexing job
        time = int(random.random()*3600)
    no_of_threads = int(random.random()*8)
    driver_cores = driver_cores
    output_mode = int(random.random()*2)
    overhead_memory = overhead_memory

    return Job(job_id, job_type, no_of_cpu, no_of_gpu, ram, storage, priority, time, no_of_threads, driver_cores, output_mode, overhead_memory)


def main():
    number_of_jobs_to_generate = 1000

    # normal distribution paramters
    
    cpu_dist_mean = 4
    cpu_dist_standard_deviation = 2

    cpu_dist = np.random.normal(cpu_dist_mean, cpu_dist_standard_deviation, number_of_jobs_to_generate)

    gpu_dist_mean = 3
    gpu_dist_standard_deviation = 1

    gpu_dist = np.random.normal(gpu_dist_mean, gpu_dist_standard_deviation, number_of_jobs_to_generate)

    ram_dist_mean = 10
    ram_dist_standard_deviation = 4

    ram_dist = np.random.normal(ram_dist_mean, ram_dist_standard_deviation, number_of_jobs_to_generate)

    storage_dist_mean = 30
    storage_dist_mean_dist_standard_deviation = 12

    storage_dist = np.random.normal(storage_dist_mean_dist_mean, storage_dist_mean_dist_standard_deviation, number_of_jobs_to_generate)

    driver_dist_mean = 4
    driver_dist_standard_deviation = 2

    driver_dist = np.random.normal(driver_dist_mean, driver_dist_standard_deviation, number_of_jobs_to_generate)

    overhead_dist_mean = 10
    overhead_dist_standard_deviation = 4

    overhead_dist = np.random.normal(overhead_dist_mean, overhead_dist_standard_deviation, number_of_jobs_to_generate)

    jobs = []
    for i in range(number_of_jobs_to_generate):
        jobs.append(sample_job_properties(cpu_dist[i], gpu_dist[i], ram_dist[i], storage_dist[i], driver_dist[i], overhead_dist[i]))
    

if __name__ == '__main__':
    main()