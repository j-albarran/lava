#!/bin/bash

x="`echo "Sample"`"

if [ "$x" == "Sample" ]
then
   lava-test-case script --result pass
else
   lava-test-case script --result fail
fi

