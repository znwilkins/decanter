#!/usr/bin/env bash

FILE=$1
zeek -r $FILE decanter_dump_input.bro

SOURCE=decanter.log
TARGET="${FILE%%.*}.log"
mv $SOURCE $TARGET

