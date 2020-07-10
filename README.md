**INTRO**<br/>
This project address the problem of creating a parser that would keep track of drivers and their trips</br>

**SOLUTION**<br/>
The overall solution has 4 main object 1). Drivers, 2). Driver, 3). Trips, 4). Trip.<br/>
The Drivers object was modeled to inherit the functionality of a dictionary. In the Drivers object the name of the
 driver is the key. The value of the Drivers object is the Driver object.
 <br/>
 <br/>
 The Driver Object holds the details of the driver one detail is the trips of the driver. The trips is represented
 of the Trips object. The idea to have the driver object is to build on to it if there are other details beside trips to be added on.<br/>
 <br/>
 The Trips Object contains an array that holds individual's trip object. The also contains sums up the distance driven,
 the time driven, and updates the total average speed.<br/>
 <br/>
 The Trip Object takes in the start and end times along with the time driven. It then calculates how long the drive was,
 and the speed of the trip.
 <br/>
 <br/>
 
 **PROCESS**<br/>
Know that the Trip Object didn't rely on another object, I decided to go ahead and create the trip object. 
I used TDD to create the object.<br/>
After I created the Trips Object, I went ahead and created the Trips Object since it only relied on the Trip object.
Since both the Trip Object and the Trip Object calculated the speed I moved the calculate_speed method into a helper file
That could be shared with both objects.<br/> 
After creating the Trips Object I went ahead and created the Driver Object wich calls methods and properties from
the Trips Object.<br/>
When the Driver Object was created, I went ahead and created the Drivers Object wich acte as a dictionary and calls
methods from the Driver Object.<br/>
After creating the Objects, I went ahead and created the Parser Method to parse the input text.

**INSTRUCTIONS**<br/>
To run this use ```python3.7 main.py testdir/inputtest.txt```<br/> 
To run tests use ```python3.7 -m unittest discover testdir```

 
 
 
 