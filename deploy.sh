#!/bin/bash -ex
#Tearing down
[ -z "$1" ] && myblueprint="" || myblueprint=$1
cfy blueprint upload -b $myblueprint openstack-blueprint.yaml
cfy deployment create -vvv --skip-plugins-validation $myblueprint -b $myblueprint -i inputs-citycloud.yaml
cfy -v executions start -d $myblueprint install
