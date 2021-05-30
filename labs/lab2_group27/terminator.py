# terminate the instance
import sys
import os
import boto
import boto.ec2
import boto.ec2.connection
import deploy

run = True

print '''Welcome To Use Terminator.py, to terminate your instance, please enter like 'python terminator.py instanceId' '''

while run:
	# the user enter python terminator.py instance_id
	if len(sys.argv) == 2:
		# read the instance id from command line
		instance_id = sys.argv[1]
		connObj = deploy.connect()
		try:
			connObj.terminate_instances(instance_ids = [instance_id])
		except Exception as e:
			print "Terminate Expection -->", e
			run = False

		for instance in connObj.get_only_instances(instance_ids = [instance_id]):
			if instance.id == instance_id:
				if instance.state != 'running':
					print "terminate successfully..."
					run = False
				else:
					print "terminate failure..."
					run = False

		# To verify that your instance uses EBS as root device
		# When an instance is stopped, all data on a non- EBS device will be removed permanently
		# and will NOT be accessible after the instance is restarted.
		'''rootDeviceName = /dev/sda1'''
		rootDeviceName = connObj.get_instance_attribute(instance_id = instance.id, attribute = 'rootDeviceName')			
		print 'rootDeviceName after termination: 'rootDeviceName
	else:
		print "Wrong format, please enter again..."




