#!/usr/bin/env python
import sys, time, subprocess

#==============================================================================
# Variables
#==============================================================================

# Some descriptive variables
#name                = "virtdc"
#version             = "0.1.0"
#long_description    = """virtdc is a set of API's/tools written to create virtual machines for cloud users efficiently."""
#url                 = "https://github.com/dineshappavoo/virtdc"
#license             = ""

#==============================================================================

def monitor_cpu(vm_id):

	#startWork = 'ssh -q -o StrictHostKeyChecking=no root@'+ip+' nohup bash /root/setup.sh &'
	#subprocess.Popen(startWork, shell=True, stderr=subprocess.PIPE)
	subprocess.Popen(['java', '-jar', '/var/lib/virtdc/vmonere/host/jars/cpumonitor.jar', vm_id])

def monitor_memory(vm_id):

	#startWork = 'ssh -q -o StrictHostKeyChecking=no root@'+ip+' nohup bash /root/setup.sh &'
	#subprocess.Popen(startWork, shell=True, stderr=subprocess.PIPE)
	subprocess.Popen(['java', '-jar', '/var/lib/virtdc/vmonere/host/jars/memorymonitor.jar', vm_id])

def monitor_io(vm_id):

	#startWork = 'ssh -q -o StrictHostKeyChecking=no root@'+ip+' nohup bash /root/setup.sh &'
	#subprocess.Popen(startWork, shell=True, stderr=subprocess.PIPE)
	subprocess.Popen(['java', '-jar', '/var/lib/virtdc/vmonere/host/jars/iomonitor.jar', vm_id])

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   monitor_cpu("VM_Task_1")

