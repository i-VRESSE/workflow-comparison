# Prefect orion

[Prefect Orion](https://orion-docs.prefect.io/) is the second-generation workflow orchestration engine, now available as a technical preview.

## Pros

* flow parameters type available as JSON schema
* result can be cached to disk
* can use [dask worker resources](http://distributed.dask.org/en/stable/resources.html) to schedule task to run only on worker with certain resource. For example task which requires local big disk.
* can store workflow seperate from parameters
* uses python types and pydantic for validation. Could be used to check whether tasks can be connected

## Cons

* Not production code yet
* Missing docs
