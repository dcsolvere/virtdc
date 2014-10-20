#!/usr/bin/python

#The file accepts new job and run the job on the specified node
#This is the part of VM placement and scaling
#This takes the VM guest configuration file from the local disk and create a new VM in current node or in a different one
import sys, subprocess
import pickle
from VM_Framework_Utility import getGuestIP
from VM_Info_Updater import updateGuestIP

#==============================================================================
# Variables
#==============================================================================

# Some descriptive variables
# This will eventually be passed to the setup function, but we already need them
# for doing some other stuff so we have to declare them here.
#name                = "vmplacementandscaling"
#version             = "0.1"
#long_description    = """vmplacementandscaling is a set of API's/tools written to create virtual machines for cloud users efficiently."""
#url                 = "https://github.com/dineshappavoo/VMPlacementAndScaling"
#license             = ""

#==============================================================================
host_vm_dict={}

def loadPickleDictionary() :
	try :
		with open('../com.vmplacement.framework/host_vm_dict.pkl', 'r') as pickle_in:
			dictionary = pickle.load(pickle_in)
			return dictionary
	except:
		print 'Cannot open node_dict.pkl file'
		sys.exit(1)

def runJobOnVM(hostName, vmid):
	host_vm_dict=loadPickleDictionary()
	ip=host_vm_dict[hostName][vmid]
	print ip	
	scpTask='scp ~/com.vmplacement.data/vms'vmid+'.csv root@'+ip':/root/task.dat'
	scpdata = subprocess.check_output(scpTask, shell=True, stderr=subprocess.PIPE)
	
	rebootCmd='ssh -q -o StrictHostKeyChecking=no root@'+ip+' reboot'
	rebootGuest = subprocess.check_output(rebootCmd, shell=True, stderr=subprocess.PIPE)
	guestNewIP = getGuestIP(vmid, 'root', 'Teamb@123')
	updateGuestIP(hostName, vmid, guestNewIP)	#Add this function in VM_info_Updater.py	

	jobPermCmd='ssh -q -o StrictHostKeyChecking=no root@'+ip+' chmod +x /root/task.dat'
	jobPerm = subprocess.check_output(jobPermCmd, shell=True, stderr=subprocess.PIPE)	
	
runJobOnVM("node1","Test_node1")

	
	
