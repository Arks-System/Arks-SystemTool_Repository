#!/bin/bash

pushd `dirname $0` > /dev/null
MAIN_PATH=`pwd -P`
popd > /dev/null

cd "${MAIN_PATH}"

chmod g+rwxs repository/
#chown :www-data repository/ -R

./generate_toollist.py | tee ./repository/toollist.txt
./get_assembly_version.sh | tee ./repository/versions.txt
