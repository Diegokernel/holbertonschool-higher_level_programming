#!/bin/bash
#end a POST request with the contents of a file, passed with the filename as the second argument of the script, in the body of the request
curl -s -X POST -H "Content-Type: application/json" -d @$2 $1
