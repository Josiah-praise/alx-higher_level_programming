#!/bin/bash
# shows the content length of url passed as argument
curl -sI "$1" | grep Content-Length | cut -d" " -f2
