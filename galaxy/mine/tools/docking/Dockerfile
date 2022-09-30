#
# Prep
#   1. bin/cns must be present and not be a symlink
#
# Build with
#
#   docker build -t haddocking/haddock3:b69f6e3d .
#
# Run with
#
#   docker run -ti --rm haddocking/haddock3:d460a0a5 --help
#
# Convert to apptainer with
#
#   apptainer build haddock3-b69f6e3d.sif docker-daemon://haddocking/haddock3:b69f6e3d
#
# Move to galaxy
#
#  mv haddock3-b69f6e3d.sif $GALAXYROOT/tools/docking
#
# Adjust path in $GALAXYROOT/tools/docking/haddock3_macros.xml
#
FROM python:3.10.7-buster

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt 

COPY . .

RUN python setup.py develop --no-deps

RUN apt update && apt install -yq zip

ENTRYPOINT [ "/usr/local/bin/haddock3" ]
