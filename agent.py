import os
import sys
import json
import threading
import time
import random

from Queue import Queue

class Agent():
    def __init__(self, agent_name, cpu, gpu, ram, storage, driver_cores, no_of_threads):
        self.agent_name = agent_name
        self.cpu = threading.Semaphore(cpu)
        self.gpu = threading.Semaphore(gpu)
        self.ram = threading.Semaphore(ram)
        self.storage = threading.Semaphore(storage)
        self.driver_cores = threading.Semaphore(driver_cores)
        self.no_of_threads = threading.Semaphore(no_of_threads)

    def idle():
        # In this state, if master broadcast is received, go to ready

        if master_broadcast_received:
            self.ready()

    def ready():

        # Send resource statistics to master
        resources_available = self.get_available_resources()

    def send_update_to_master(resources):
        pass

    def busy():
        # all resources used up, cannot take more requests
        pass

    def waiting_for_use():
        # In this state, if job incoming, modify available resources and send stats to master
        # If all resources used, go to busy
        if incoming_job_received:
            # check if resources available then perform what is written after
            modify_available_resources(job_resources)
            resources_available = self.get_available_resources()
            send_update_to_master(resources_available)

            # if all resources used up, go to busy

    def get_available_resources():

        # return a dictionary
        resource_dict = {}
        resource_dict[agent_name] = self.agent_name
        resource_dict[cpu] = self.cpu
        resource_dict[gpu] = self.gpu
        resource_dict[ram] = self.ram
        resource_dict[storage] = self.storage
        resource_dict[driver_cores] = self.driver_cores
        resource_dict[no_of_threads] = self.no_of_threads

        return resource_dict

    def modify_available_resources(cpu_used, gpu_used, ram_used, storage_used, driver_cores_used, no_of_threads_used):
        self.cpu -= cpu_used
        self.gpu -= gpu_used
        self.ram -= ram_used
        self.storage -= storage_used
        self.driver_cores -= driver_cores_used
        self.no_of_threads -=no_of_threads_used

if __name__ == '__main__':
    main()