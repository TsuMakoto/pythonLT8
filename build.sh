#!/bin/bash

cat $1.md > tmp.md
sed -i '/^$/d' tmp.md
published="publish/slide.md"
IFS=''
rm $published
while read line
do
  if [ ${line:0:1} = "#" ]; then
    echo ""    >> $published
    echo "---" >> $published
    echo ""    >> $published
    echo ""    >> $published
    echo $line >> $published
  else
    echo $line >> $published
  fi
done < tmp.md
rm tmp.md

cp -r img publish/
marp $published -o publish/index.html
