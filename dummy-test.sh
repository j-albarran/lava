#!/bin/bash

x="`echo "Sampe"`"

if [ "$x" == "Sample" ]
then
   lava-test-case script --result pass
else
   lava-test-case script --result fail
fi

