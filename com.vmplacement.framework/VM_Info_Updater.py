#!/usr/bin/python
import pickle
import sys
from Guest import Guest
from VM_Framework_Utility import getGuestIP

#==============================================================================
# Variables
#==============================================================================

# Some descriptive variables
#name                = "vmplacementandscaling"
#version             = "0.1"
#long_description    = """vmplacementandscaling is a set of API's/tools written to create virtual machines for cloud users efficiently."""
#url                 = "https://github.com/dineshappavoo/VMPlacementAndScaling"
#license             = ""

#==============================================================================

#Global variables
#host_vm_dict={}


def loadPickleDictionary() :
	try :
		with open('../com.vmplacement.framework/node_dict.pkl', 'r') as pickle_in:
			dictionary = pickle.load(pickle_in)
			return dictionary
	except:
		print 'Cannot open node_dict.pkl file'
		sys.exit(1)

def loadPickleHostVMDictionary() :
	try :
		with open('../com.vmplacement.framework/host_vm_dict.pkl', 'r') as pickle_in:
			dictionary = pickle.load(pickle_in)
			return dictionary
	except:
		print 'Cannot open host_vm_dict.pkl file'
		return None
#Not used
def getHostVMDict() :
	vm_dict=loadPickleHostVMDictionary()
	if vm_dict is not None :
		return vm_dict

def addOrUpdateDictionaryOfVM(hostName,vmid, guest) :
	#code to add the dictionary elements
	host_vm_dict=loadPickleHostVMDictionary()
	node_dict=loadPickleDictionary()
	for key, value in node_dict.iteritems() :
		if key not in host_vm_dict :
			host_vm_dict[key]={}
            		#For Testing
			#host_vm_dict[key]={"vm1":Guest("192.168.1.14","vm1", float(1), float(3),float(42424),float(424242),float(1))}
	host_vm_dict[hostName][vmid]=guest
	pickleNodeVMDictionary(host_vm_dict)
	print host_vm_dict

def pickleNodeVMDictionary(dictionary) :
	with open('host_vm_dict.pkl','w') as host_vm_pickle_out:
    		pickle.dump(dictionary,host_vm_pickle_out)
		#host_vm_pickle_out.close()

#Function calls
addOrUpdateDictionaryOfVM('node1', 'Task1',Guest("192.168.1.14","Task1", float(1), float(3),float(42424),float(424242),float(1)))
#print host_vm_dict
