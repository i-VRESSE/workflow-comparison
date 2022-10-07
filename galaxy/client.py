"""Script to submit job to galaxy

Requirements

```python
pip install bioblend
export GALAXY_API_KEY=<your galaxy api key>
python client.py docking-protein-protein.zip
```

"""
import os
import argparse
from pathlib import Path
from bioblend import galaxy


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("archive", type=Path)
    parser.add_argument("--recipe", default="docking-protein-protein-test.cfg")
    parser.add_argument("--url", default="http://127.0.0.1:8080/")
    args = parser.parse_args()
    api_key = os.environ["GALAXY_API_KEY"]
    tool_id = "haddock3"
    gi = galaxy.GalaxyInstance(url=args.url, key=api_key)
    hist = gi.histories.create_history()
    hist_id = hist["id"]
    print(f"Created history {hist_id}")

    upload_job = gi.tools.upload_file(args.archive, hist_id)
    print(upload_job)
    gi.jobs.wait_for_job(upload_job['jobs'][0]['id'])
    print(f"Uploaded {args.archive}")
    
    upload_output = upload_job['outputs'][0]
    archive_input = {
        "id": upload_output['id'],
        "hid": upload_output['hid'],
        "name": upload_output['name'],
        "tags": upload_output['tags'],
        "src": upload_output["hda_ldda"],
        "keep": False,
    }
    tool_inputs = {
        'recipe': args.recipe,
        'archive': archive_input
    }
    print(tool_inputs)
    job = gi.tools.run_tool(hist_id, tool_id, tool_inputs)
    print(job)
    completed_job = gi.jobs.wait_for_job(job['jobs'][0]['id'])
    print(completed_job)


if __name__ == "__main__":
    main()
