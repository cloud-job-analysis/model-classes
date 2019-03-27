import os
import sys
import json
import scipy
import time
import random

import numpy as np

"""
job_type - ML, web, database, indexing (0 to 3) - can increase and modify as needed
output_mode - write to disk or stderr (0 or 1)
no_of_threads - number of threads it should be executed on (nginx is multi-threaded)
driver_cores - number of driver cores (one of Spark's Application properties)
overhead_memory - extra memory that can be used (one of Spark's Application properties)
"""

class Job:
    def __init__(self, job_id, job_type, no_of_cpu, no_of_gpu, ram, storage, priority, time, no_of_threads, driver_cores, output_mode, overhead_memory):
        self.job_id = job_id
        self.job_type = job_type
        self.no_of_gpu = no_of_gpu
        self.no_of_cpu = no_of_cpu
        self.ram = ram
        self.storage = storage
        self.priority = priority
        self.time = time
        self.no_of_threads = no_of_threads
        self.driver_cores = driver_cores
        self.output_mode = output_mode
        self.overhead_memory = overhead_memory

