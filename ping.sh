#!/bin/bash

if [ "$#" -lt 2 ] 
then
  exit 3
fi

if [ $2~/p/ ];
then 
	ping $1 -c 2
fi

#added one extra line
