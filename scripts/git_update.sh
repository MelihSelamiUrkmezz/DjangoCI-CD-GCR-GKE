#!/bin/bash

image="gcr.io/eternal-wonder-376414/pimages"

#get timestamp for the tag
timestamp=$(date +%Y%m%d%H%M%S)

tag=$timestamp
echo $tag