#Weight and Balance program

#Databases
SpencerPlanes = ["102LA", "1074T", "13830", "5397R", "6835H", "7647H", "13301", "20592", "761LA", "1039U","737FT"]
EsthervillePlanes = ["13033", "13203", "13693", "20742", "5200H", "5444H", "80159", "1039U", "737FH"]
SpencerInstructors = ["Peyton", "Kyle", "Jocelyn", "Dwayne", "ZacharyS", "Lucas", "Joe", "Aria", "Alaina", "Maverick", "Morgan"]
EsthervilleInstructors = ["Dwayne", "Jessica", "Isaac", "ZacharyB", "Brandon", "Trinity", "Raynee", "Samuel", "Lucas", "Ethan", "Andrew", "Abigail", "Dakota", "Timothy", ]
SpencerInstWeights = [150, 145, 140, 160, 145, 150, 130, 130, 130, 140, 140, 160]
EsthervilleInstWeights = [160, 130, 130, 145, 145, 130, 130, 130, 130, 130, 130, 130, 130, 130]
SpencerPlaneTypes = ["C172K", "C172M", "C172M", "C172M", "C172M", "C172M", "C172M", "C172M", "C172M", "PA34", "PA34"]
EsthervillePlaneTypes = [, , ]
SpencerPlaneEwgt = [, , ]
EsthervillePlaneEwgt = [, , ]
SpencerPlaneEarm = [, , ]
EsthervillePlaneEarm = [, , ]
SpencerPlaneEmoment = [, , ]
EsthervillePlaneEmoment = [, , ]
C172ArmArray = [37, 73, 95, 128, 0, 2300]
PsenecaArmArray = [85.5, 118.1, 155.7, 178.7, 22.5 4200]

ValidCessnaModels = ["C172", "C172M", "C172N", "C172L", "C172K"]
ValidPiperModels = ["PA34-200","PA34"]

#"102LA", "1074T", "13830", "5397R", "6835H", "7647H", "13301", "20592", "761LA", "1039U","737FT"
#"13033", "13203", "13693", "20742", "5200H", "5444H", "80159", "1039U", "737FH", "", "", "", "", "", "", "", "", "", "", "", "", "", 

#guidance to user
print ("Information on planes was last checked October 4th 2026, verify critical information")
print ("For first use of the program with a plane, verify its calculations against hand-done math")
print ("For planes not owned by Iowa Lakes Community College, manual information entry will be required")
print ("Entering weights as something other than a number may result in program crash")# resolve this later
print ( )

#Gathering the instructor
x = False
iwspw = False
iwest = False

print ("Enter weight of user:")
userweight = input ( )

print ("Do you have a passenger or instructor on board?")
opu = input ("(yes / no) :")
if opu == ("no"):
    x = True
    print ("Enter non-passenger front seat weight:")
    InstructorWeight = input ( )
while x == False:
 print ('Enter Full names, for the name Zachary, use "ZacharyS" or "ZacharyB" as there are two.')
 print ('Enter Instructor Name:')
 InstructorName = input ( )
 try:
   InstructorName in SpencerInstructors
   iwspw = True
   x = True
 except:
   try:
     InstructorName in EsthervilleInstructors
     iwest = True
     x = True
   except:
     print (f"Instructor {InstructorName} not in database, please enter weight manually:")
     InstructorWeight = input ( )
     if InstructorWeight > 0 : weightfoundsuccesfully = True
     x = True

#Set Intructor weight

if iwest == True: 
  InstructorWeight = (EsthervilleInstWeights[EsthervilleInstructors.index (InstructorName)])
  if InstructorWeight > 0 : weightfoundsuccesfully = True
if iwspw == True:
  InstructorWeight = (SpencerInstWeights[SpencerInstructors.index (InstructorName)])
  if InstructorWeight > 0 : weightfoundsuccesfully = True
  

if weightfoundsuccesfully == True:
  print ("Passenger Weight set to: {InstructorWeight}")

aircraft_type = ["C172M"]
aircraft_year = [0]
typemaxweight = [0]
envelopeforward = [0]
envelopeaft = [0]
weightfoundsuccesfully = False

#entering the date today
import datetime
time = datetime.datetime.now ()
date = [time.strftime ("%a"), time.strftime ("%b"), time.strftime ("%d"), time.strftime ("%X"), time.strftime ("%x")]

#basic entries for information
cgwithinlimits = False

fuelarm = [0]#done
emptyweight = [0]
emptyarm = [0]
calculatedemptymoment = [0]
emptymoment = [0]
frontweight = [0]#done
frontarm = [0]#done
frontmoment = [0]
rearweight = [0]
reararm = [0]#done
rearmoment = [0]
baggage1weight = [0]
baggage1arm = [0]#done
baggage1moment = [0]
baggage2weight = [0]
baggage2arm = [0]#doneish? maybe need to make exceptions
baggage2moment = [0]
useablefuelgallons = [0]
useablefuelweight = [0]
useablefuelmoment = [0]
rampweight = [0]
ramparm = [0]
rampmoment = [0]
taxifuelweight = [0]
taxifuelmoment = [0]
takeoffweight = [0]
takeoffarm = [0]
takeoffmoment = [0]
flightfuelgallons = [0]
flightfuelweight = [0]
flightfuelmoment = [0]
landingweight = [0]
landingarm = [0]
landingmoment = [0]
Va = [0]

print ("How much weight will be in the backseat?")
rearweight = input ( )
print ("How much weight will be in the first baggage area?")
baggage1weight = input ( )
if aircraft_type !in ValidCessnaModels:
 print ("How much weight will be in the second baggage area?")
 = input ( )
print ("?")
 = input ( )
print ("?")
 = input ( )
print ("?")
 = input ( )

#Get all weight inputs from the user before this point for consistency

n = True
# this loop will confirm the tail number entry, and if it is not in the list, grab the information to use for calculations
while n == True:
    print ('enter the tail number of the aircraft without the ICAO designator letter (enter the ICAO designator letter to manually enter data)')
    tail_number = [input (" ")]
    try:
        tail_number in SpencerPlanes
        print (f"you entered {tail_number}")
        emptyweight = (SpencerPlaneEwgt[SpencerPlanes.index (tail_number)])
        emptyarm = (SpencerPlaneEarm[SpencerPlanes.index (tail_number)])
        emptymoment = (SpencerPlaneEmoment[SpencerPlanes.index (tail_number)])
        n = False
    except: 
        try: 
          tail_number in EsthervillePlanes
          print (f"you entered {tail_number}")
          emptyweight = (EsthervillePlaneEwgt[EsthervillePlanes.index (tail_number)])
          emptyarm = (EsthervillePlaneEarm[EsthervillePlanes.index (tail_number)])
          emptymoment = (EsthervillePlaneEmoment[EsthervillePlanes.index (tail_number)])
          n = False

        #enter the information if your entered tail number is not on the list
        except:
         print (f"you entered {tail_number} which was not found in database")
         print ("do you wish to enter information manually?")
         if input ("enter 1 to continue, else reselect tail number") == 1: 
           print ("enter the type of the aircraft (ex: C172M, PA34, PA34-200, etc...)")
           aircraft_type = [input ( )]
           n = False

if aircraft_type in ValidCessnaModels: 
 FinalArmArray = C172ArmArray
 fuelarm = [47.8]
 lpa = True
if aircraft_type in ValidPiperModels:
 FinalArmArray = PsenecaArmArray
 fuelarm = [93.6]
 lpa = True
if lpa == False:
    print ("Aircraft Arm Data not Found, Please Enter:")
    FinalArmArray = [input ("Front Seat (Average) Arm:"), 
                     input ("Rear Seat Arm:"), 
                     input ("Baggage Area 1 Arm:"), 
                     input ("Baggage Area 2 Arm:"), 
                     0, 
                     0
                    ] # me placing this here indicates to future readers that i am used to javascript currently
    fuelarm = input ("Fuel Arm:")

#Pre-Math

calculatedemptymoment = {emptyweight * emptyarm}
if calculatedemptymoment != emptymoment: print (f"Measured empty moment is {emptymoment} and calculated empty moment is {calculatedemptymoment}")
if input ("press 1 to use calculated empty moment, else measured will be used") == 1: emptymoment = calculatedemptymoment

#Performing the math - remember to check with the user if their moment is to be calculated or entered
if aircraft_type in ValidPiperModels:


  


#Displaying the math to the user

print (f"{tail_number}, is a {aircraft_type}, {aircraft_year}" end=" ")
if lpa == True:
 print (f"with a max gross weight of {typemaxweight}")
print ( )
print (f"Empty Weight: {emptyweight}", end =" | ")
print (f"Empty Weight Arm: {emptyarm}", end =" | ")
print (f"Empty Weight Moment: {emptymoment}")
print ( )
print (f"Front Passenger / Pilot Weight: {frontweight}", end =" | ")
print (f"Front Passenger / Pilot Arm: {frontarm}", end =" | ")
print (f"Front Passenger / Pilot Moment: {frontmoment}")
print ( )
print (f"Rear Seat / Passenger Weight: {rearweight}", end =" | ")
print (f"Rear Seat / Passenger Arm: {reararm}", end =" | ")
print (f"Rear Seat / Passenger Moment: {rearmoment}")
print ( )
print (f"Baggage Area 1 Weight: {baggage1weight}", end =" | ")
print (f"Baggage Area 1 Arm: {baggage1arm}", end =" | ")
print (f"Baggage Area 1 Moment: {baggage1moment}")
print ( )
print (f"Baggage Area 2 Weight: {baggage2weight}", end =" | ")
print (f"Baggage Area 2 Arm: {baggage2arm}", end =" | ")
print (f"Baggage Area 2 Moment: {baggage2moment}")
print ( )
print (f"Useable Fuel Weight: {useablefuelweight}", end =" | ")
print (f"Useable Fuel Arm: {fuelarm}", end =" | ")
print (f"Useable Fuel Moment: {useablefuelmoment}")
print ( )
print (f"Ramp Weight: {rampweight}", end =" | ")
print (f"Ramp Arm: {ramparm}", end =" | ")
print (f"Ramp Moment: {rampmoment}")
print ( )
print (f"Taxi / Runup Fuel Weight: {taxifuelweight}", end =" | ")
print (f"Taxi / Ramp Fuel Arm: {fuelarm}", end =" | ")
print (f"Taxi / Ramp Fuel Moment: {taxifuelmoment}")
print ( )
print (f"Takeoff Weight: {takeoffweight}", end =" | ")
print (f"Takeoff Arm: {takeoffarm}", end =" | ")
print (f"Takeoff Moment: {takeoffmoment}")
print ( )
print (f"In-flight Fuel Usage Weight: {flightfuelweight}", end =" | ")
print (f"In-flight Fuel Usage Arm: {fuelarm}", end =" | ")
print (f"In-flight Fuel Usage Moment: {flightfuelmoment}")
print ( )
print (f"Landing Weight: {landingweight}", end =" | ")
print (f"Landing Arm: {landingarm}", end =" | ")
print (f"Landing Moment: {landingmoment}")
print ( )
print ( )
if aircraft_type != ("C172M" or "C172L"):
 print (f"C.G. at Takeoff: {takeoffweight / takeoffarm}", end=" | ")
 print (f"C.G. at Landing: {landingweight / landingarm}")
 print ( )
 print (f"C/G. Limits for Aircraft Type FWD Limit: {envelopeforward}", end=" | ")
 print (f"C.G. Aft Limit: {envelopeaft}")
 print ( )
 print (f"Total Moment at Takeoff: -", end=" | ")
 print (f"Total Moment at Landing: -")
 print (f"C.G. Enveloppe Limits for Aircraft Type FWD limit: -", end=" | ")
 print (f"AFT limit: -")
else:
 print (f"C.G. at Takeoff: -", end=" | ")
 print (f"C.G. at Landing: -")
 print ( )
 print (f"C/G. Limits for Aircraft Type FWD Limit: -", end=" | ")
 print (f"C.G. Aft Limit: -")
 print ( )
 print (f"Total Moment at Takeoff: {takeoffmoment}", end=" | ")
 print (f"Total Moment at Landing: {landingmoment}")
 print (f"C.G. Enveloppe Limits for Aircraft Type FWD limit: {envelopeforward}", end=" | ")
 print (f"AFT limit: {envelopeaft}")
print ( )
print (f"The V(a) today is {Va}")
print ( )
print (date)
print ( )
print ( )
print ("Remember to Verify all information and perform a check using known values before trusting the information")
print ("Please contact (+1) 952 412 5892 for an updated version of the program if any issues are encountered")
print ( )
print ("Links to Additional Information:")
print ("https://flyfourforces.com/library")
print ("https://flyfourforces.com/scheduler_v3_2")