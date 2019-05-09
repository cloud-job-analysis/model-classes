import os
import sys
import json
import threading
import time
import random
import threading
import socket
import pickle
import subprocess
from multiprocessing import Process


class Agent():
    def __init__(self, id, agent_name, cpu, gpu, ram, storage, driver_cores, no_of_threads):
        self.agent_name = agent_name
        self.resource_lock = threading.Semaphore(1)
        self.conn_lock = threading.Semaphore(1)
        self.is_flask_running_lock = threading.Semaphore(1)
        self.is_hadoop_running_lock = threading.Semaphore(1)
        self.job_ids_lock = threading.Semaphore(1)
        self.is_flask_running = False
        self.is_hadoop_running = False
        self.job_ids = {}
        self.id = id
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

    def ready(self, socket, conn):

        # Send resource statistics to master
        resources_available = self.get_available_resources()
        self.send_update_to_master(socket, conn, resources_available)

    def send_update_to_master(self, socket, conn, resources):
        conn.sendall(pickle.dumps(resources))

    def waiting_for_use(self, socket, conn):
        # If all resources used, go to busy
        # Wait for job object from master
        data = conn.recv(1024)
        incoming_job_received = pickle.loads(data)
        if self.reduce_available_resources(incoming_job_received):
            return incoming_job_received
        else:
            return None

    def get_available_resources(self):

        # return a dictionary
        self.resource_lock.acquire()
        resource_dict = {}
        resource_dict["agent_id"] = self.id
        resource_dict["cpu"] = self.cpu
        resource_dict["gpu"] = self.gpu
        resource_dict["ram"] = self.ram
        resource_dict["storage"] = self.storage
        resource_dict["driver_cores"] = self.driver_cores
        resource_dict["no_of_threads"] = self.no_of_threads
        self.resource_lock.release()
        return resource_dict

    def reduce_available_resources(self, incoming_job_received):
        self.resource_lock.acquire()
        new_cpu = self.cpu
        new_ram = self.ram
        self.resource_lock.release()
        new_gpu = self.gpu
        new_storage = self.storage
        new_driver_cores = self.driver_cores
        new_no_of_threads = self.no_of_threads
        if "cpu" in incoming_job_received:
            if incoming_job_received["cpu"] > new_cpu:
                return False
            else:
                new_cpu -= incoming_job_received["cpu"]
        if "gpu" in incoming_job_received:
            if incoming_job_received["gpu"] > self.gpu:
                return False
            else:
                new_gpu -= incoming_job_received["gpu"]
        if "ram" in incoming_job_received:
            if incoming_job_received["ram"] > new_ram:
                return False
            else:
                new_ram -= incoming_job_received["ram"]
        if "storage" in incoming_job_received:
            if incoming_job_received["storage"] > self.storage:
                return False
            else:
                new_storage -= incoming_job_received["storage"]
        if "driver_cores" in incoming_job_received:
            if incoming_job_received["driver_cores"] > self.driver_cores:
                return False
            else:
                new_driver_cores -= incoming_job_received["driver_cores"]

        if "no_of_threads" in incoming_job_received:
            if incoming_job_received["no_of_threads"] > self.no_of_threads:
                return False
            else:
                new_no_of_threads -= incoming_job_received["no_of_threads"]
        self.resource_lock.acquire()
        self.cpu = new_cpu
        self.gpu = new_gpu
        self.ram = new_ram
        self.resource_lock.release()
        self.storage = new_storage
        self.driver_cores = new_driver_cores
        self.no_of_threads = new_no_of_threads
        return True

    def increase_available_resources(self, incoming_job_received):
        self.resource_lock.acquire()
        self.cpu += incoming_job_received.get("cpu", 0)
        self.gpu += incoming_job_received.get("gpu", 0)
        self.ram += incoming_job_received.get("ram", 0)
        self.storage += incoming_job_received.get("storage", 0)
        self.driver_cores += incoming_job_received.get("driver_cores", 0)
        self.no_of_threads += incoming_job_received.get("no_of_threads", 0)
        self.resource_lock.release()

    def execute_job(self, job, socket, conn):

        time.sleep(5)

        start = time.time()
        if job["type"] == 'flask_job':
            self.is_flask_running_lock.acquire()
            if not self.is_flask_running:
                server = "python flask/app.py"
                subprocess.Popen(server, shell=True)
                self.is_flask_running = True
                time.sleep(2)
            self.is_flask_running_lock.release()
        if job["type"] == "mr_job":
            self.is_hadoop_running_lock.acquire()
            if not self.is_hadoop_running:
                dfs = "/usr/local/hadoop/sbin/start-dfs.sh"
                subprocess.call(dfs, shell=True)
                self.is_hadoop_running = True
            self.is_hadoop_running_lock.release()
        subprocess.call(job["command"], shell=True)
        self.increase_available_resources(job)
        update_to_master = job
        update_to_master["agent_id"] = self.id
        update_to_master["job_runtime"] = time.time() - start
        self.send_update_to_master(socket, conn, update_to_master)

    def socket_setup(self, port):
        host = '0.0.0.0'
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        print("socket bound" + host)
        s.listen()
        conn, addr = s.accept()
        return s, conn

    def execute_agent(self, socket, conn):
        while True:
            job = self.waiting_for_use(socket, conn)
            if job != None:
                threading.Thread(target=self.execute_job, args=(
                    job, socket, conn), daemon=True).start()
                job = None

    def run(self):
        socket, conn = self.socket_setup(8000)
        self.ready(socket, conn)
        self.execute_agent(socket, conn)
        conn.close()
        socket.close()


def main():
    agent_name = "1"
    cpu = 29
    gpu = 2
    ram = 85  # GB
    storage = 2048  # GB
    driver_cores = 2
    no_of_threads = 4
    agent = Agent(1, agent_name, cpu, gpu, ram,
                  storage, driver_cores, no_of_threads)
    agent.run()


if __name__ == '__main__':
    main()
