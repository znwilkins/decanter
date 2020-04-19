#!/usr/bin/env bash

PATH=$PATH:/opt/zeek/bin/

FILE=$1
zeek -r $FILE decanter_dump_input.bro

SOURCE=decanter.log
TARGET="${FILE%%.*}.decanter"
mv $SOURCE $TARGET
rm *.log

