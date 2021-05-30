# terminate the instance
import sys
import os
import boto
import boto.ec2
import boto.ec2.connection

def connect():

	file = open('credentialAWS.txt','r')
	lines = file.read()
	content = lines.split()

	#print content
	ACCESS_KEY_ID = content[1]
	SECRET_ACCESS_KEY = content[3]

	try:
		connObj = boto.ec2.connect_to_region('us-east-1',aws_access_key_id = ACCESS_KEY_ID, aws_secret_access_key = SECRET_ACCESS_KEY)
	except Exception as e:
		print "________Exception from connection_______--> ", e
	return connObj

run = True

print '''To terminate your instance, please enter the instance id in command...'''

while run:

	instance_id = raw_input()

	try:
		connObj = connect()
		try:
			connObj.terminate_instances(instance_ids = [instance_id])
		except Exception as e:
			print "Terminate Expection -->", e

		for instance in connObj.get_only_instances(instance_ids = [instance_id]):
			if instance.id == instance_id:
				if instance.state != 'running':
					print "terminate successfully..."
					run = False
					rootDeviceName = connObj.get_instance_attribute(instance_id = instance.id, attribute = 'rootDeviceName')			
					print 'rootDeviceName after termination: ', rootDeviceName
				else:
					print "terminate failure..."
					run = True


		# To verify that your instance uses EBS as root device
		# When an instance is stopped, all data on a non- EBS device will be removed permanently
		# and will NOT be accessible after the instance is restarted.
		'''rootDeviceName = /dev/sda1'''
	except Exception as e:
		print 'terminate exception....', e
		run = True


# while run:
# 	# the user enter python terminator.py instance_id
# 	if len(sys.argv) == 2:
# 		# read the instance id from command line
# 		instance_id = sys.argv[1]
# 		connObj = connect()
# 		try:
# 			connObj.terminate_instances(instance_ids = [instance_id])
# 		except Exception as e:
# 			print "Terminate Expection -->", e
# 			run = False

# 		for instance in connObj.get_only_instances(instance_ids = [instance_id]):
# 			if instance.id == instance_id:
# 				if instance.state != 'running':
# 					print "terminate successfully..."
# 					run = False
# 				else:
# 					print "terminate failure..."
# 					run = False

# 		# To verify that your instance uses EBS as root device
# 		# When an instance is stopped, all data on a non- EBS device will be removed permanently
# 		# and will NOT be accessible after the instance is restarted.
# 		'''rootDeviceName = /dev/sda1'''
# 		rootDeviceName = connObj.get_instance_attribute(instance_id = instance.id, attribute = 'rootDeviceName')			
# 		print 'rootDeviceName after termination: ', rootDeviceName
# 	else:
# 		print "Wrong format, please enter again..."




