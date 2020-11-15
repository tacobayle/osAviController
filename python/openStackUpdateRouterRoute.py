import requests, json, os, yaml, sys
#
# this python script is used to iterate over a list of tasks and using the loop inside the list of tasks
#
credsFile = sys.argv[1]
routerId = sys.argv[2]
cidr = sys.argv[3]
gw  = sys.argv[4]
os.system('. {0} ; openstack router add route --route destination={1},gateway={2} {3} ;'.format(credsFile, cidr, gw, routerId))
