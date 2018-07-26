#!/bin/bash

dir_name_org="data"

i=0
for i in {1..2}; do    
    dir_name=$dir_name_org$i	
    python scraping_yahoo.py $1 $dir_name
    echo $dir_name
done

