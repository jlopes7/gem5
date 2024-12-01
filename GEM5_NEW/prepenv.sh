#!/usr/bin/env bash

set -Eo pipefail

mkdir -p $HOME/local

echo "Downloading GCC 10.1"
wget -O- https://ftp.mirrorservice.org/sites/sourceware.org/pub/gcc/releases/gcc-10.1.0/gcc-10.1.0.tar.gz | tar zxvf - -C $HOME/local

pushd . &>/dev/null

cd $HOME/local/gcc-10.1.0
echo "Download and prepare the prerequisites"
$PWD/contrib/download_prerequisites
RC=$?

if [ $RC -eq 0 ]
then	echo "Configure GCC for C and C++"
	./configure --prefix=$HOME/local --disable-multilib --enable-languages=c,c++
	RC=$?
fi

if [ $RC -eq 0 ]
then	echo "Build GCC..."
	make -j `nproc`
	RC=$?
fi

if [ $RC -eq 0 ]
then	echo "Install GCC..."
	make install
	RC=$?
fi

if [ $RC -eq 0 ]
then	echo -e "\nGCC successfully installed!"
	$HOME/local/bin/gcc --version
	echo -e "\nAdd the following entries to the system environment variables before building GEM5:"
	echo -e "export PATH=\$HOME/local/bin:\$PATH"
	echo -e "export LD_LIBRARY_PATH=\$HOME/local/lib:\$LD_LIBRARY_PATH"
	echo -e "export PKG_CONFIG_PATH=\$HOME/local/lib/pkgconfig:\$PKG_CONFIG_PATH"

	echo -e "\nTo build ARM in GEM5 now, use:"
	echo -e "scons-3 USE_HDF5=0 -j `nproc` build/ARM/gem5.opt"
fi

popd >/dev/null

exit $RC

