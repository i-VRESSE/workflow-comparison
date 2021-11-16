# Dask

The workflow is defined as Python code using the [Dask](https://dask.org).

Workflow is constructed by chaining delayed functions and dataframes.

## Example

Below is code where the functions could be decorated with [@dask.delayed](https://docs.dask.org/en/latest/delayed.html).

```python
from haddock.modules.cns import generate_topology
from haddock.modules.docking import rigid_body_docking, semi_flexible_refinement, water_refinement
from haddock.modules.analysis import cluster_complexes

molecules = ['foo.pdb', 'bar.pdb']
topology = generate_topology(molecules)
rigid_complexes = rigid_body_docking(topology)
semi_flexible_complexes = semi_flexible_refinement(rigid_complexes)
water_refinement_complexes = water_refinement(water_refinement_complexes)

clusters = cluster_complexes(water_refinement_complexes)

if __name__ == "__main__":
    # Until now a DAG was constructed lazy, by calling compute the DAG is executed
    clusters.compute()
```

Run sequentially/threaded

```shell
python3 job.py
```

Or run distributed/parallel

```shell
import job
from dask.distributed import Client, SSHCluster
cluster = SSHCluster(["localhost", "localhost"])
client = Client(cluster)

future = client.submit(job.clusters)
result = future.result()
```

## Pros

* Used a lot
* Just Python code,
    * No new language to learn
    * Use as package in Jupyter notebook
* multiprocessing is abstracted into

## Cons

* Not multi user out of box. Could be achieved with [Dask gateway](https://gateway.dask.org/)
* Expects shared file system or remote file system like S3
* No seperation between workflow template and worklfow executation with args