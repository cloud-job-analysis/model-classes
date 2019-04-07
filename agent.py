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
        # self.cpu = threading.Semaphore(cpu)
        # self.gpu = threading.Semaphore(gpu)
        # self.ram = threading.Semaphore(ram)
        # self.storage = threading.Semaphore(storage)
        # self.driver_cores = threading.Semaphore(driver_cores)
        # self.no_of_threads = threading.Semaphore(no_of_threads)
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram
        self.storage = storage
        self.driver_cores = driver_cores
        self.no_of_threads = no_of_threads

    def idle(self):
        # In this state, if master broadcast is received, go to ready
        # Start listening for master broadcast received
        master_broadcast_received = True
        return master_broadcast_received
        if master_broadcast_received:
            self.ready()

    def ready(self):

        # Send resource statistics to master
        resources_available = self.get_available_resources()
        self.send_update_to_master(resources_available)

    def send_update_to_master(self, resources):
        print("Sending available resources=", resources, " to master." )
        # rpc communication here

    def busy(self):
        # all resources used up, cannot take more requests
        pass

    def waiting_for_use(self):
        # If all resources used, go to busy
        # Wait for job object from master
        # incoming_job_received = RPC CALL FROM MASTER
        incoming_job_received = [{"id" : 1, "cpu" : 3, "gpu" : 1, "storage" : 6, "ram" : 8}, {"id": 2,  "cpu" : 4, "gpu" : 2, "storage" : 10, "ram" : 20}]
        idx = random.randint(0, 1)
        self.reduce_available_resources(incoming_job_received[idx])
        return incoming_job_received[idx]
        # resources_available = self.get_available_resources()
        # send_update_to_master(resources_available)
        # if all resources used up, go to busy

    def get_available_resources(self):

        # return a dictionary
        resource_dict = {}
        resource_dict["agent_name"] = self.agent_name
        resource_dict["cpu"] = self.cpu
        resource_dict["gpu"] = self.gpu
        resource_dict["ram"] = self.ram
        resource_dict["storage"] = self.storage
        resource_dict["driver_cores"] = self.driver_cores
        resource_dict["no_of_threads"] = self.no_of_threads

        return resource_dict

    def reduce_available_resources(self, incoming_job_received):
        self.cpu -= incoming_job_received["cpu"]
        self.gpu -= incoming_job_received["gpu"]
        self.ram -= incoming_job_received["ram"]
        self.storage -= incoming_job_received["storage"]
        try:
            self.driver_cores -= incoming_job_received["driver_cores"]
        except KeyError:
            pass
        try:
            self.no_of_threads -= incoming_job_received["no_of_threads"]
        except KeyError:
            pass
        print("Resources reduced")

    def increase_available_resources(self, incoming_job_received):
        self.cpu += incoming_job_received["cpu"]
        self.gpu += incoming_job_received["gpu"]
        self.ram += incoming_job_received["ram"]
        self.storage += incoming_job_received["storage"]
        try:
            self.driver_cores += incoming_job_received["driver_cores"]
        except KeyError:
            pass
        try:
            self.no_of_threads += incoming_job_received["no_of_threads"]
        except KeyError:
            pass
        print("Resources added back")

    def execute_job(self, job):
        print("Running job")
        print(job)
        print(time.time())
        time.sleep(5)
        print(time.time())
        print("Job executed")
        self.increase_available_resources(job)

    def run(self):
        ready = self.idle()
        while ready:
            self.ready()
            job = self.waiting_for_use()
            self.execute_job(job)
            




def main():
    # get resources available in agent machine and comment out next initialization lines
    agent_name = "1"
    cpu = 4
    gpu = 1
    ram = 32 #GB
    storage = 2048 #GB
    driver_cores = 2
    no_of_threads = 4
    agent = Agent(agent_name, cpu, gpu, ram, storage, driver_cores, no_of_threads)
    agent.run()

if __name__ == '__main__':
    main()