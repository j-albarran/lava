#!/bin/bash
echo "Sample" >> file.txt

x=""

while read line
do
    x="${x}line"
done <file.txt

if [ "$x" == "Sample" ]
then
   lava-test-case script --result pass
else
   lava-test-case script --result fail
fi

