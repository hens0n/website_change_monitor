#!/bin/python
# Jacob Henson
# https://github.com/cyberphilia

# Standard Modules
import time
import math
# My modules
from config import *
import web_util
# import email_util



def run():
	start_timer()
	

def start_timer():
	time_start = time.time()
	while (1):
		time_current = time.time()
		seconds = (time_current - time_start)
		minutes = seconds/60
		if(seconds >= 86400):
			time_start = time.time()		
		check_sites_frequency(minutes)
		time.sleep(60)

	
def check_sites_frequency(minutes):
	for site in sites_list:		
		modulus = math.floor(minutes % site.frequency)	
		if (modulus == 0):
			site.count = site.count+1
			print ('name: %s, frequency: %d, count: %d' % (site.name, site.frequency,site.count))
			if(web_util.compare_pevious_and_current(site2)):
				# send email
				print 'Email sent'



if __name__ == '__main__':
	pass
	# print __name__
