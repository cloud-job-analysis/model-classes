# Agent

Each agent represents a machine capable of executing jobs assigned to it by the user. To ensure that an agent can execute jobs in parallel while also waiting for new jobs, we implemented a multi threaded agent. 

When the agent starts, it is assigned a list of resources - number of CPUs, number of GPUs, available storage, available memory. It is also assigned a unique Agent ID. Then, the agent starts listening on the host machine on port 8000. 

The master connects with the agent by sending a request to the agent on port 8000. As soon as the master claims an agent, the agent gets a list of all its available resources and sends this resource offer to the master. Next, the agent waits for the master to assign it a job. 

Once the agent is assigned a job, it creates a new "child" thread to execute this job as long as the agent has enough resources available to execute the job. The parent goes back to waiting for new jobs. The parent thread executes this process within a loop. 

The child thread, created by the agent to execute the assigned job, executes the command passed by the master using the subprocess Python module. It waits until the task is completed. It then computes the run time for the job and returns this to the master. The agent continues running till the master is up. Once the master is done executing, the agent closes its connection with the master and shuts down.

#### Instructions

1. Install docker and docker compose in case you don't have it installed already.
   1. Check the docker installation instructions [here](https://docs.docker.com/install/). Don't forget to add the current user to the docker group
   2. Install docker compose as shown [here](https://docs.docker.com/compose/install/)
2. Clone this repository
3. `cd model-classes`
4. `docker-compose up`
   This will take some time as it first builds the image which involves installing hadoop and all the other required dependencies. 





