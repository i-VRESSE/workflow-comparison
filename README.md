# Comparison of existing workflow engines

See if any of them can be used as base for ivresse.
Each directory holds report for a workflow engine.

## Requirements

* Submit job to a queue
* Job is constructed out of parts that can be replaced with alternate implementations
* Part of job can be array of computations
* Multi user
    * authenicate against openid connect
    * data from users should not be readable by other unless
* Files need to be on shared filesystem or downloaded/uploaded
* Compute on
    * local machine for testing or small deployments
    * SLURM cluster
    * cloud (VM/container/function)
* Compute on disk intensive on SLURM cluster and rest on cloud
* For maintenance disable SLURM cluster so all calculations are done in cloud or vice versa
* Has graphical way to construct a workflow from nodes
