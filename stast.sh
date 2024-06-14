#!/bin/bash

path_content=$PATH

IFS=':' read -ra path_segments <<< "$path_content"

# for segment in "${path_segments[@]}"; do
#     echo "$segment"
# done

buildComposeYaml() {
  cat <<HEADER
version: '3'
services:
  nupil:
    image: nupil_ubuntu:0.0.4
    # command: python /nupil_mount/nupil/main.py
    tty: true
    volumes:
HEADER
      for i in "${path_segments[@]}"; do
      cat <<BLOCK
      - $i:/nupil_mount$i:rw
         
BLOCK
      done
}

buildComposeYaml | docker-compose -f- "$@" up 
