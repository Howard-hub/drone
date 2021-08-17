from dronekit import connect, VehicleMode, LocationGlobalRelative
from pymavlink import mavutil
import time
import argparse
import re  
parser = argparse.ArgumentParser()
parser.add_argument('--connect', default='127.0.0.1:14550')
args = parser.parse_args()

# Connect to the Vehicle

print 'Connecting to vehicle on: %s' % args.connect
vehicle = connect(args.connect, baud=57600, wait_ready=True)

def arm_and_takeoff(aTargetAltitude):
    
    print("fly test") 

    print ("GUIDED")
    vehicle.mode    = VehicleMode("GUIDED")
    print ("UNLOCK")
    vehicle.armed   = True
    print ("fly")
    vehicle.simple_takeoff(aTargetAltitude)
    while True:
        z=str(vehicle.rangefinder)
        string=z
        a=re.findall(r"\d+\.?\d*",string)
        c=float(a[0])
        print("hight",c)
        if c>=aTargetAltitude*0.95:
            print ("final")
            break
        time.sleep(1)
#move
def send_ned_velocity(velocity_x, velocity_y, velocity_z, duration):
    """
    Move vehicle in direction based on specified velocity vectors.
    """
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
        0,       # time_boot_ms (not used)
        0, 0,    # target system, target component
        mavutil.mavlink.MAV_FRAME_LOCAL_NED, # frame
        0b0000111111000111, # type_mask (only speeds enabled)
        0, 0, 0, # x, y, z positions (not used)
        velocity_x, velocity_y, velocity_z, # x, y, z velocity in m/s
        0, 0, 0, # x, y, z acceleration (not used)
        0, 0)    # yaw, yaw_rate (not used) 
    for x in range(0,duration):
        vehicle.send_mavlink(msg)
        time.sleep(0.05)
#yaw
def condition_yaw(heading, relative=True):
    if relative:
        is_relative=1 
    else:
        is_relative=0
    
    
    if not relative:
        direction = 0 
    
    msg = vehicle.message_factory.command_long_encode(
        0, 0,       # target system, target component 
        mavutil.mavlink.MAV_CMD_CONDITION_YAW, # command
        0,          # confirmation
        heading,    # param 1, yaw in degrees   
        0,          # param 2, yaw speed (not used)  
        1,          # param 3, direction  
        is_relative,# param 4, relative or absolute degrees  
        0, 0, 0)    # param 5-7, not used  
    vehicle.send_mavlink(msg)
#start fly
print("blue=1, green=2: ")
color = input()
arm_and_takeoff(1)
time.sleep(3)
print("move")
send_ned_velocity(0.021,-0.3,0,19)
time.sleep(1)
condition_yaw(274)
time.sleep(5)
send_ned_velocity(0.021,-0.3,0,20)
time.sleep(1)
condition_yaw(180)
time.sleep(3)
print("set fly back")
vehicle.mode = VehicleMode("LAND")
print "Mode: %s" % vehicle.mode.name
print("close")
vehicle.close()