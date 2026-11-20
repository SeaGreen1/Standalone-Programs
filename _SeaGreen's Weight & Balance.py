#Weight and Bal program 2
#Goals: Perform all sorts of W&B calculations independent of the databse of aircraft
# Store a databse in a seperate document
# Verify the date of information received from that seperate document
# connect to a UI app and make this look nice
# Print the W&B to a seperate document
# Allow ICAO designator letters without issue

import datetime
import math
import subprocess
import os
import time

#ILCC Planes Information

ValidCessnaModels = ["C172", "C172M", "C172N", "C172L", "C172K"]
ValidPiperModels = ["PA34-200","PA34"]

checkdate = str("Nov 11 2026")

##following is importing the instructor information from a file
KnownInstructors = []
KnownIWeight = []
with open ("instructorinfo.txt") as instinfo:
    data = instinfo.read()
    instinfo.close()
data = (data.split("/n"))
x = len(data)
w = 0
while w < x:
    KnownInstructors.append (data[w])
    KnownIWeight.append (float(data[w+1]))
    w += 2

#import the plane information from
KnownPlanes = []
KnownEWeight= []
KnownEArm = []
KnownEMoment = []
KnownType = []
with open ("planeinfo.txt") as planeinfo:
    data2 = planeinfo.read()
    planeinfo.close()
data2 = (data2.split("/n"))
x = len(data2)

w = 0
while w < x:
    KnownPlanes.append (data2[w])
    KnownEWeight.append (float(data2[w+1]))
    KnownEArm.append (float(data2[w+2]))
    KnownEMoment.append (float(data2[w+3]))
    KnownType.append (data2[w+4])
    w += 5
    
print (type(data2[0]))
print (type(data2[1]))
print (type(data2[2]))
print (type(data2[3]))
print (type(data2[4]))


nation_designators = ("N", "C")

C172ArmArray = [37, 73, 95, 128, 0, 2300]
PsenecaArmArray = [85.5, 118.1, 155.7, 178.7, 22.5, 4200]

#Get information from seperate document here

#subprocess.run (["cmd", "/c", "python", "wt_bal.py"] capture_output = False, text = True)


print (f"Verify critical information against known weight and balance calculations\n \nDatabase current to {checkdate}\n \nManual entry of information required if plane is not in databse\n \nMade by _SeaGreen")
#Inputs from user I

#Tail Number Ammending
n = False
while n == False:
 x = str(input ("Enter the tail number"))
 if len(x) < 7:
   print (f"Tail # is {x}")
   tail_number = x
   if (x[:1]) in nation_designators :
     tail_number = x[1:]
     print (f"Tail # ammended to be {tail_number}")
   n = True
 else:
   print ("Not a valid input")

#Establish instructor name and weight
g = input("Is there an Instructor? (Yes / No)")
if g == "Yes" or g == "yes":
  instructor_name = input ("Enter their name")
  if instructor_name in KnownInstructors:
    instructor_weight = KnownIWeight[KnownInstructors.index(instructor_name)]
  else:
    n = False
    while n == False:
      f = input ("Enter Instructor Weight")
      try:
        f = int(f)
        print (f"Instructor weight set to {x}")
        instructor_weight = f
        n = True
      except:
       print ("Not a valid input")
else:
  instructor_weight = int(0)

n = False
while n == False:
 f = input ("Enter pilot weight")
 try:
   f = int(f)
   print (f"Pilot weight set to {f}")
   n = True
 except:
   print ("Not a valid input")

frontweight = int(f + instructor_weight)

if tail_number in KnownPlanes:
    emptyweight = (KnownEWeight[KnownPlanes.index (tail_number)])
    print (f"Empty weight set to {emptyweight}")
    emptyarm = (KnownEArm[KnownPlanes.index (tail_number)])
    print (f"Empty arm set to {emptyarm}")
    emptymoment = (KnownEMoment[KnownPlanes.index (tail_number)])
    print (f"Empty moment set to {emptymoment}")
    aircraft_type = (KnownType[KnownPlanes.index(tail_number)])
    print (f"Aircraft type set to {aircraft_type}")
else: 
  emptyweight = input ("Empty weight of the aircraft:")
  emptyarm = input ("Empty arn of the aircraft:")
  emptymoment = input ("Empty moment of the aircraft:")
  aircraft_type = input ("Aircraft type:")

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
                    ] # me placing this here indicates to future readers that I am used to javascript currently
    fuelarm = input ("Fuel Arm:")

#Date and Time
time = datetime.datetime.now ()
date = [time.strftime ("%a"), time.strftime ("%b"), time.strftime ("%d"), time.strftime ("%X"), time.strftime ("%x")]



n = False
while n == False:
 f = input ("Rear weight:")
 try:
   f = int(f)
   rearweight = f
   print (f"Rear weight set to {f}")
   n = True
 except ValueError:
   print ("Not a valid input")

n = False
while n == False:
 f = input ("Baggage area 1 weight:")
 try:
   f = int(f)
   baggage1weight = f
   print (f"Baggage area 1 weight set to {f}")
   n = True
 except ValueError:
   print ("Not a valid input")

if aircraft_type not in ValidCessnaModels:
 n = False
 while n == False:
  f = input ("Baggage area 2 weight:")
  try:
    f = int(f)
    baggage2weight = f
    print (f"Baggage area 2 set to {f}")
    n = True
  except ValueError:
    print ("Not a valid input")


else: 
  if aircraft_type in ValidPiperModels:
   vaatmax = 146
  else: 
    vaatmax = 97
    baggage2weight = int(0)

n = False
while n == False:
 f = input ("Fuel Onboard (gal):")
 try:
   f = int(f)
   useablefuelweight = int(f * 6)
   print (f"Fuel onboard set to {f} gallons")
   n = True
 except ValueError:
   print ("Not a valid input")

n = False
if aircraft_type in ValidCessnaModels:
 taxifuelweight = 12
 n = True
while n == False:
 f = input ("Taxi / Run-up Fuel (gal):")
 try:
   int(f)
   taxifuelweight = f * 6
   print (f"Taxi / Run-up set to {f} gallons")
   n = True
 except ValueError:
   print ("Not a valid input")

n = False
while n == False:
 f = input ("Expected Fuel use (gal):")
 try:
   f = int(f)
   flightfuelweight = f * 6
   print (f"Fuel Burn set to {f}")
   n = True
 except ValueError:
   print ("Not a valid input")


#Inputs from user II

if aircraft_type in ValidCessnaModels: 
 FinalArmArray = C172ArmArray
 fuelarm = 47.8
 lpa = True
if aircraft_type in ValidPiperModels:
 FinalArmArray = PsenecaArmArray
 fuelarm = 93.6
 lpa = True
if lpa == False:
    print ("Aircraft Arm Data not Found, Please Enter:")
    FinalArmArray = [input ("Front Seat (Average) Arm:"), 
                     input ("Rear Seat Arm:"), 
                     input ("Baggage Area 1 Arm:"), 
                     input ("Baggage Area 2 Arm:"), 
                     0, 
                     0
                    ] # me placing this here indicates to future readers that I am used to javascript currently
    fuelarm = input ("Fuel Arm:")

frontarm = float(FinalArmArray[0])
reararm = float(FinalArmArray[1])
baggage1arm = float(FinalArmArray[2])
baggage2arm = float(FinalArmArray[3])
if aircraft_type not in ValidCessnaModels:
  frontbaggagearm = float(FinalArmArray [4])
typemaxweight = int(FinalArmArray [5])

#calculated weight versus input weight

calculatedemptymoment = emptyweight * emptyarm
if calculatedemptymoment != emptymoment: print (f"Measured empty moment is {emptymoment} and calculated empty moment is {calculatedemptymoment}")
if input ("press 1 to use calculated empty moment, else measured will be used") == 1: emptymoment = calculatedemptymoment
emptymoment /= 1000

#Performing the math - remember to check with the user if their moment is to be calculated or entered

frontmoment = (frontweight * frontarm / 1000)
rearmoment = (rearweight * reararm / 1000)
baggage1moment = (baggage1weight * baggage1arm / 1000)
if aircraft_type in ValidPiperModels:
 baggage2moment = (baggage2weight * baggage2arm / 1000)
if aircraft_type in ValidCessnaModels:
 baggage2moment = 0
useablefuelmoment = (useablefuelweight * fuelarm / 1000)
taxifuelmoment = (taxifuelweight * fuelarm / 1000)
flightfuelmoment = (flightfuelweight * fuelarm / 1000)
rampweight = (emptyweight + useablefuelweight + frontweight + rearweight + baggage1weight + baggage2weight)
print (f"{emptymoment} {useablefuelmoment}, {frontmoment}, {rearmoment}, {baggage1moment}, {baggage2moment},")
rampmoment = (emptymoment + useablefuelmoment + frontmoment + rearmoment + baggage1moment + baggage2moment)
ramparm = (rampmoment * 1000 / rampweight)
takeoffweight = (rampweight - taxifuelweight)
takeoffmoment = (rampmoment - taxifuelmoment)
takeoffarm = (takeoffmoment * 1000 / takeoffweight)
landingweight = (takeoffweight - flightfuelweight)
landingmoment = (takeoffmoment - flightfuelmoment)
landingarm = (landingmoment * 1000 / landingweight)

if aircraft_type in ValidCessnaModels:
 Va = float(97 * math.sqrt(rampweight / typemaxweight))
 envelopeforward = 52.5
 envelopeaft = 109.0
else:
 Va = float(vaatmax * math.sqrt(rampweight / typemaxweight))
 envelopeforward = 82.0
 envelopeaft = 94.6

#print to user

print (f"{tail_number}, is a {aircraft_type}", end =" ")
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
if aircraft_type != ("C172M" or "C172L" or "C172K"):
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
print ("Please contact SeaGreen1 via GitHub for an updated version of the program if any issues are encountered")
print ( )

def sFileName():
    h = os.getenv("HOME")
    if h:
        p = h + "\\Documents\\"
    else:
        u = os.getenv("USERPROFILE")
        if not u:
            p = "C:\\"
        else:
            p = u + "\\Documents\\"

    n = time.strftime("results_%Y-%b-%d_%H%M.txt")
    fn = f"{p}{n}"
    # print(f"filename = {p}{n}")
    return fn

print (f"{tail_number}, is a {aircraft_type}", end =" ")
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
print ("Please contact SeaGreen1 via GitHub for an updated version of the program if any issues are encountered")
print ( )


with open(sFileName(), "w") as f:
  f.write(f"Verify critical information against known weight and balance calculations\n \nDatabase current to {checkdate}\n \nManual entry of information required if plane is not in database\n \nMade by _SeaGreen\n \n")
  f.write(f"{tail_number} is a {aircraft_type} with max gross weight of {typemaxweight}\n \n" )
  f.write(f"The empty weight is {emptyweight} | arm is {emptyarm:.2f} | and moment is {emptymoment:.2f}\n")
  f.write(f"Front / passenger weight is {frontweight} | arm is {frontarm:.2f} | and moment is {frontmoment:.2f}\n")
  f.write(f"The rear seat weight is {rearweight} | arm is {reararm:.2f} | and moment is {rearmoment:.2f}\n")
  f.write (f"The first baggage area weight is {baggage1weight} | arm is {baggage1arm:.2f} | and moment is {baggage1moment:.2f}\n")
  if aircraft_type in ValidCessnaModels:
    f.write ("The second baggage area weight is --  arm is -- and moment is --\n")
  else:
    f.write (f"The second baggage weight is {baggage2weight:.2f} | arm is {baggage2arm:.2f} | and moment is {baggage2moment:.2f}\n")
  f.write (f"Ramp weight is {rampweight:.2f} | arm is {ramparm:.2f} and moment is {rampmoment:.2f}\n")
  f.write (f"Taxi / run-up fuel weight is {taxifuelweight:.2f} | arm is {fuelarm:.2f} and moment is {taxifuelmoment:.2f}\n")
  f.write (f"Takeoff weight is {takeoffweight:.2f} | arm is {takeoffarm} and moment is {takeoffmoment:.2f}\n")
  f.write (f"Fuel consumption weight is {flightfuelweight:.2f} | arm is {fuelarm:.2f} and moment is {flightfuelmoment:.2f}\n")
  f.write (f"Landing weight is {landingweight:.2f} | arm is {landingarm:.2f} and moment is {landingmoment:.2f}\n \n")
  if aircraft_type == ("C172M" or "C172L" or "C172K"):
    f.write(f"C.G. at takeoff -- | at landing --\nC.G. limit FWD -- | at AFT --\n \n")
    f.write (f"Total moment at takeoff {takeoffmoment:.2f} | at landing {landingmoment:.2f}\n")
  else:
    f.write(f"C.G. at takeoff {takeoffmoment:.2f} | at landing {landingmoment:.2f}\nC.G. limit FWD {envelopeforward:.2f} | at AFT {envelopeaft:.2f}\n \n")
    f.write(f"Total moment at takeoff -- | at landing --\n")
  f.write (f"The VA today is {Va:.2f}\n")
  f.write(f"{date}\n")

input("enter to end")