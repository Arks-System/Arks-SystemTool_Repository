#!/bin/bash

pushd `dirname $0` > /dev/null
MAIN_PATH=`pwd -P`
popd > /dev/null

cd "${MAIN_PATH}"

str="$(strings -el repository/Arks-SystemTool.exe)"
awk_fmt='BEGIN { RS = "" ; FS = "\n" }{ print $1 "=" $2 }'

echo -e "$str"|grep "ProductVersion" -A 1 | awk "${awk_fmt}"
echo -e "$str"|grep "Assembly Version" -A 1 | awk "${awk_fmt}"
