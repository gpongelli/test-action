#!/bin/bash

set -ex

OPENSSL_VERSION="1.1.1t"
CWD=$(pwd)

mkdir -p /opt/openssl

virtualenv env
. env/bin/activate
pip install -U setuptools
pip install -U wheel pip
curl -O https://www.openssl.org/source/openssl-${OPENSSL_VERSION}.tar.gz
tar xvf openssl-${OPENSSL_VERSION}.tar.gz
cd openssl-${OPENSSL_VERSION}
./config no-shared no-ssl2 no-ssl3 -fPIC --prefix=/opt/openssl
make && make install
cd ..
