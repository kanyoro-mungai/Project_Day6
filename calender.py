def createuser():
	user = {name:b_no}

	name = raw_input("Please enter your name: ")
	print "you entered", name

	b_no = raw_input("Please enter your bootcamp id: ")
	print "you entered", b_no

	user.update({name:b_no})

	return user

def createcalender():

	calender = {b_no:c_name}

	b_no = raw_input("Please enter your bootcamp id: ")

	c_name = raw_input("Please enter the calender name: ")
	print "Calender name", c_name

	calender.update({})

	return calender


#def create events():

#def viewevents():

#def viewlastevent():
	


