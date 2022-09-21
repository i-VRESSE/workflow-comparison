# Build cns 

On Ubuntu 16.04 with AMD Ryzen 5600G.

```shell
docker run -ti --rm -v $PWD:/src ubuntu:16.04
```

```shell
apt update
apt install -y build-essential nano gfortran tcsh
gfortran --version
# GNU Fortran (Ubuntu 5.4.0-6ubuntu1~16.04.12) 5.4.0 20160609
# Tried on Ubuntu22 and gfortran 11.2.0 failed compile on Error: Type mismatch 
cd /src
# From cns homepage after registration
tar -zxf cns_solve_1.3_all.tar.gz 
cd cns_solve_1.3
# Set to /src/cns_solve_1.3
nano cns_solve_env 
nano .cns_solve_env_sh 
source .cns_solve_env_sh 
# Add `-static` to LDFLAGS
nano instlib/machine/supported/intel-x86_64bit-linux/Makefile.header.2.gfortran
# From dropbox 
# https://www.dropbox.com/s/wliubqovuusqdvr/cns.tgz?dl=0
# See https://github.com/haddocking/haddock3/issues/329#issuecomment-1043554801
tar -xf ../cns.tgz 
mv cns1.3/* source/
make install
exit
```

```
cp cns_solve_1.3/intel-x86_64bit-linux/source/cns_solve-2209211134.exe <haddock3 repo>/bin/cns
```
