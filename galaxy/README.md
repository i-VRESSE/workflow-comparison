# Galaxy

https://galaxyproject.org/
Used from bioinformatics pipelines.

A workflow is constructed from previously executed tools. Each tool input can be exposed as workflow input.

## Pros

* Multi user
* Allows sharing data between users
* has runners https://docs.galaxyproject.org/en/master/lib/galaxy.jobs.runners.html like 
  https://pulsar.readthedocs.io/en/latest/readme.html
* has api https://bioblend.readthedocs.io/en/latest/api_docs/galaxy/docs.html
* has dynamic rules to route jobs to runners

## Cons

* Clunky forms. Need to upload data in seperate step, before submitting tool
* compute on local or HPC batch queue systems with shared filesystem


## Try

See `mine/` for config and tool.

Things to try

* upload archive file + unpack it + run haddock3
  * in single go
  * upload as dataset first then run haddock3 
  * as workflow, where unzip is done as workflow step
* haddock3 container image, see https://training.galaxyproject.org/training-material/topics/admin/tutorials/singularity/tutorial.html
* job on
  * local
  * slurm
  * remote with pulsar
* rules to run tool on some job destination (if big then destination with shared fs)
* execute tool via api, see https://github.com/galaxyproject/bioblend
* only allow member of group to run haddock3, in tool_filters in galaxy.xml and admin user management portal
* orcid login, in /oidc_backends_config.xml.sample

Notes
* Needed galaxy root in shorter path (/data/galaxy) as /home/someone/bla/something/somethingelse/ was too long
