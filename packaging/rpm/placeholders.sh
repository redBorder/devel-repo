#!/bin/bash

# list of files where we need to replace placeholders
files=("resources/username.repo")

f_usage() {
  echo "usage: $0 -u USERNAME -v VERSION -b BUILDNUMBER"
  exit 0
}

while getopts "hu:v:b:" opt; do
  case $opt in
      u) username="$OPTARG"
          ;;
      v) version="$OPTARG"
          ;;
      b) buildnumber="$OPTARG"
          ;;
      *) f_usage
          ;;
  esac
done

if [ -z $username ]; then
    f_usage
fi

if [ -z $version ]; then
    f_usage
fi

if [ -z $buildnumber ]; then
    f_usage
fi

for file in "${files[@]}"; do
    sed -i "s/{{USERNAME}}/$username/g" $file
    sed -i "s/{{VERSION}}/$version/g" $file
    sed -i "s/{{BUILDNUMBER}}/$buildnumber/g" $file
done