#!/bin/bash

if [ "$1" = "build_generator" ]; then
  docker build -t generator ./generator

elif [ "$1" = "run_generator" ]; then
  docker run -v "$PWD/data:/data" generate

elif [ "$1" = "create_local_data" ]; then
  python generator/generate.py ./local_data

elif [ "$1" = "build_reporter" ]; then
  docker build -t reporter ./reporter

elif [ "$1" = "run_generator" ]; then
  docker run -v "$PWD/data:/data" reporter


