import sys
import time
import datetime
from datetime import date
from datetime import timedelta
import re
def checkdate(dt):
	try:
		time.strptime(dt,'%m/%d/%Y')
		return True
	except ValueError:
		return False

if (len(sys.argv) == 1):
	print "Please provide a command ( \"add\", \"search\", or \"delete\")\n"

elif sys.argv[1] == "add":
	if len(sys.argv)==4:
		if checkdate(sys.argv[3]) == False:
			print "Expecting a date as the fourth argument. Entered value is not in the correct format(MM/DD/YYYY)"
			exit(1)
		else: 
			fadd=open("tasklist.txt","a+")
			fadd.write(sys.argv[3]+"->")
			fadd.write(sys.argv[2]+"\n")
			fadd.close()
	else:
		print "Please check the number of arguments and run the program again"
		exit(1)

elif sys.argv[1] == "search":
	if len(sys.argv)==3:
		fsearch=open("tasklist.txt","r")
		info=str(sys.argv[2])
		iflag=0
		for line in fsearch:
			if info in line:
				print line
				iflag=1
		if iflag==0:
			print "The item is not available in the file"
		fsearch.close()

	elif len(sys.argv)==4:
		if sys.argv[2]=='-r' or sys.argv[2]=='-d':
			if sys.argv[2]=='-r':
				pattern=str(sys.argv[3])
				fsearchr=open("tasklist.txt","r")
				for line in fsearchr:
					matchr=re.search(pattern,line)
					if matchr:
						print line
				
				fsearchr.close()
				
			else:
				if str.isdigit(sys.argv[3]):
					today=date.today()
					n=int(sys.argv[3])
					dateincr=datetime.timedelta(days=1)
					last=today+timedelta(n)
					dateflag=0
					while today <= last:
						fsearchd=open("tasklist.txt","r")
	
						datestring=str(today.strftime("%m/%d/%Y"))
						for line in fsearchd:
							if datestring in line:
								print line
								dateflag=1
						today += dateincr
						fsearchd.close()
					if dateflag==0:
						print "No tasks due in "+str(n)+" days"	
				
				else:
					print "Incorrect type for number of days argument "
		else:
			print "Invalid option passed for search command"
			exit(1)

	else:
		print "Please check the number of arguments passed"
		exit(1)

elif sys.argv[1] == "delete":
	if len(sys.argv)==4:

		if checkdate(sys.argv[3]) == False:
			print "Expecting a date as the fourth argument. Entered value is not in the correct format(MM/DD/YYYY)"
			exit(1)
		else: 
		
			fdelete=open("tasklist.txt","r")
			descrp=str(sys.argv[2])
			ddate=str(sys.argv[3])
			space=[]
			deleteflag=0
			for line in fdelete:
				if not (descrp in line and ddate in line):
					space.append(line)
				else:
					deleteflag=1

			fdelete.close()
			fdelete=open("tasklist.txt","w")
			fdelete.writelines(space)
			fdelete.close()
			if deleteflag==0:
				print "There is no matching entry for the combination of description and date provided"
			

	else:
		print "Please check the number of arguments needed to execute delete command"
		exit(1)

else:
	print "Invalid command"
	exit(1)
