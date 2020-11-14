import requests, json, os, yaml, sys
#
# this python script is used to iterate over a list of tasks and using the loop inside the list of tasks
#
playbook = sys.argv[1]
otherProjects = sys.argv[2]
external = sys.argv[3]
str = otherProjects.replace("\'", "\"")
data_loaded = json.loads(str)
index = 0
for item in data_loaded:
    os.system('ansible-playbook {0} --extra-vars \'{{"openstack_project":{1}}}\' --extra-vars \'{{"openstack_project_index":{2}}}\' --extra-vars \'{{"externalNetwork":{3}}}\''.format(playbook, json.dumps(item), index, json.dumps(external)))
    index = index + 1