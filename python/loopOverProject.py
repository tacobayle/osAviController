import requests, json, os, yaml, sys
#
# this python script is used to iterate over a list of tasks and using the loop inside the list of tasks
#
playbook = sys.argv[1]
jsonFile = sys.argv[2]
data_loaded = json.load(open(jsonFile))
index = 0
for item in data_loaded["openstack"]["project"]["others"]:
    os.system('ansible-playbook {0} --extra-vars \'{{"openstack_project":{1}}}\' --extra-vars \'{{"openstack_project_index":{2}}}\' --extra-vars \'{{"externalNetwork":{3}}}\' --extra-vars \'{{"public_key_file":{4}}}\''.format(playbook, json.dumps(item["name"]), index, json.dumps(data_loaded["openstack"]["networks"]["external"]["name"]), json.dumps(data_loaded["openstack"]["key"][0]["public_key_file"])))
    index = index + 1