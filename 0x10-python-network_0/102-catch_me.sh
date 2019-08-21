#!/bin/bash
#script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!
curl -sd "user_id=98" -H "Origin: HolbertonSchool" -LX PUT 0.0.0.0:5000/catch_me
