import sys
import os
import boto
import boto.ec2
import boto.ec2.connection
import time

ACCESS_KEY_ID = 'AKIAITBBRI7SKFNOQQ4QX'
SECRET_ACCESS_KEY = 'xxxxxxxxx'
key_pair_name = 'key_pair_test1'
SecurityGroupName = 'csc326-group27'
AMI = 'ami-xxxxx'

def connect():
	try:
		connObj = boto.ec2.connect_to_region('us-east-1',aws_access_key_id = ACCESS_KEY_ID, aws_secret_access_key = SECRET_ACCESS_KEY)
	except Exception as e:
		print "________Exception from connection_______--> ", e
	return connObj

def deploy():
	'''Step1'''
	# connect to us-east-1 with aws_access_key_id and aws_secret_access_key
	connObj = connect()

	'''Step2'''
	# create key pair
	try:
		# delete previous key_pair_test file first 
		os.system("rm -f %s" % key_pair_name+'.pem')
		key_pair = connObj.create_key_pair(key_pair_name)
		key_pair.save('.')
	except Exception as e:
		print "________Exception from key pair--> ", e

	'''Step3'''
	# create security group
	try:
		security_group = connObj.create_security_group(SecurityGroupName, 'mySecurityGroup')
		connObj.authorize_security_group(group_name=security_group.name, ip_protocol='icmp', from_port=-1, to_port=-1, cidr_ip='0.0.0.0/0')
		connObj.authorize_security_group(group_name=security_group.name, ip_protocol='tcp', from_port=22, to_port=22, cidr_ip='0.0.0.0/0')
		connObj.authorize_security_group(group_name=security_group.name, ip_protocol='tcp', from_port=80, to_port=80, cidr_ip='0.0.0.0/0')
	except Exception as e:
		print "________Exception from Security Group--> ", e

	'''Step4'''
	# run the instances
	try:
		reserve = connObj.run_instances(image_id  = AMI, key_name = key_pair_name, security_groups = [SecurityGroupName], instance_type = 't1.micro')
		
		# instanceStatus = connObj.get_all_instance_status(instance_ids=reserve.instances)	
		# for ins in instanceStatus:
		# 	print "_______instance status_________:", ins

		for instance in reserve.instances:
			print "________Instance state__________: ",instance.state
	except Exception as e:
		print "________Exception from instance--> ", e

	'''Once the state of the instance is changed to "running", 
	    you can access your instance with the key-pair generated 
	    in step 1 with the following command $ ssh -i key_pair.pem ubuntu@<PUBLIC-IP-ADDRESS>
	    Note that the default user name for the Ubuntu AMIs is "ubuntu". The public IP address
		of the instance can be found with boto.ec2.instance.Instance.ip_address'''
	# suspend the program until state becomes running	
	while reserve.instances[0].update() != 'running':
			time.sleep(2)

	print "state of the instance is now running!"			

	'''To copy a file from your local machine to the AWS instance, you may use the following command.
			scp -i key_pair.pem <FILE-PATH> ubuntu@<PUBLIC-IP-ADDRESS>:~/<REMOTE-PATH>'''

	'''Setup static IP address'''

	print "waiting for setup static IP address..."

	try:
		address = connObj.allocate_address()
		address.associate(instance_id = reserve.instances[0].id)
	except Exception as e:
		print "________Exception from address--> ", e

	print  "Address_Ip: ",address.public_ip
	print  "instanceId: ",reserve.instances[0].id

	return (connObj,reserve.instances[0].update())

if __name__ == "__main__":
	deploy()