#!/bin/bash

#path to patch.sh
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

#make sure the correct version of cwltool is installed
OLDVERSION="'cwltool --version'"
if [[ $OLDVERSION != *"1.0.20170217172322"* ]]; then
    pip uninstall cwltool
    pip install cwltool==1.0.20170217172322
fi

CWLPATH="'python $DIR/getcwlpath.py'"

#replace main, job, process
mv $DIR/cwltool-ucsc/job.py $DIR/cwltool-ucsc/process.py $DIR/cwltool-ucsc/main.py $CWLPATH