# Galaxy

https://galaxyproject.org/
Used from bioinformatics pipelines.

A workflow is constructed from previously executed tools. Each tool input can be exposed as workflow input.

## Pros

* Multi user
* Allows sharing data between users
* has runners https://docs.galaxyproject.org/en/master/lib/galaxy.jobs.runners.html like 
  https://pulsar.readthedocs.io/en/latest/readme.html
* has api https://bioblend.readthedocs.io/en/latest/api_docs/galaxy/docs.html , https://usegalaxy.org/api/docs , https://galaxyproject.org/develop/api/
* has dynamic rules to route jobs to runners

## Cons

* Clunky forms. Need to upload data in seperate step, before submitting tool
* compute on local or HPC batch queue systems with shared filesystem


## Try

See `mine/` for config and tool.

Things to try

* [ ] upload archive file + unpack it + run haddock3
  * in single go
  * [x] upload as dataset first then run haddock3 with run dir as output
    * See mine/tools/docking/haddock3.xml 
  * as workflow, where unzip is done as workflow step
  * [x] upload as dataset first then run haddock3 with zip as output
    * See mine/tools/docking/haddock3zip.xml
  * generaete recipe in tool
    * See mine/tools/docking/haddock3files.xml
* [x] haddock3 container image, see https://training.galaxyproject.org/training-material/topics/admin/tutorials/singularity/tutorial.html
  * See mine/tools/docking/haddock3.xml , mine/config/job_conf.xml
* job on
  * [x] local
  * slurm
  * remote with pulsar
  * dynamic, see https://training.galaxyproject.org/training-material/topics/admin/tutorials/job-destinations/tutorial.html
* rules to run tool on some job destination (if big then destination with shared fs)
* [x] execute tool via api, see https://github.com/galaxyproject/bioblend
  * can we wrap bartender around galaxy?
  * See [client.py](client.py)
* [ ] only allow member of group to run haddock3,
  * see [#Restrict+users](#restrict-users) chapter
* [ ] orcid login, in /oidc_backends_config.xml.sample
* [ ] custom user fields, aka i am an academic or commercial fellow

Notes
* Needed galaxy root in shorter path (/data/galaxy) as /home/someone/bla/something/somethingelse/ was too long

## Install galaxy

```
export GALAXYMINE=$PWD/mine
cd ~  # Galaxy needs to be run in short path
git clone https://github.com/galaxyproject/galaxy.git
cd galaxy
git checkout v22.05
ln -s $GALAXYMINE/tools/docking tools/docking
ln -s  $GALAXYMINE/lib/galaxy/tool_util/toolbox/filters/restrict_academic.py lib/galaxy/tool_util/toolbox/filters/restrict_academic.py
cd config
for x in $(ls -1 $GALAXYMINE/config)
do
ln -s $GALAXYMINE/config/$x
done
cd ..
python3 -m venv .venv
sh run.sh
```

See [mine/tools/docking/Dockerfile](mine/tools/docking/Dockerfile) how to make singularity container image for haddock3.

# Example dataset

```
cd <haddock3 repo>
cd examples/docking-protein-protein/
zip -r docking-protein-protein.zip .
```

1. Upload zip file
   1. Set type to `zip`
2. Launch haddock3 tool
   1. Select zip file 
   2. Set config file name = docking-protein-protein-test.cfg
  
After job complete each output file of haddock3 is an galaxy dataset (225 files).

# Restrict users

To only allow certain users to acces a tool 

In tool_filters in galaxy.xml and admin user management portal, see https://galaxyproject.org/user-defined-toolbox-filters/ 

1. Login as admin
2. Goto http://localhost:8080/admin/form/create_role
   * Name = ACADEMICS
   * Description = Role use to restrict tools to users that claim to be academic.
   * Create new group = Yes 
3. On http://localhost:8080/admin/users add you self to ACADEMICS group
4. TODO for some reason the function (./lib/galaxy/tool_util/toolbox/filters/restrict_academic.py) is not being executed
