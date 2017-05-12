def createuser():
	user = {}

	name = raw_input("Please enter your name: ")
	print "you entered", name

	b_no = raw_input("Please enter your bootcamp id: ")
	print "you entered", b_no

	user.update({b_no:name})

	return user

def createcalender():

	calender = {}

	b_no = raw_input("Please enter your bootcamp id: ")

	c_name = raw_input("Please enter the calender name: ")
	print "Calender name", c_name

	calender.update({b_no:c_name})

	return calender


#def create events():

#def viewevents():

#def viewlastevent():
	


