# Liam Fitzgerald - Parket - Question 2

time = datetime.now() # Could pass through any time to see if bays are available

# Django query to get all parking bays that are available at the given time (now)
ParkingBay.objects.all().exclude(bayaccess__start__lte=time, bayaccess__end__gte=time)