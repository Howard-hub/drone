from dronekit import connect, VehicleMode, LocationGlobalRelative
from pymavlink import mavutil
import time
#123
import argparse  
parser = argparse.ArgumentParser()
parser.add_argument('--connect', default='127.0.0.1:14550')
args = parser.parse_args()

# Connect to the Vehicle

print 'Connecting to vehicle on: %s' % args.connect
vehicle = connect(args.connect, baud=57600, wait_ready=False)
vehicle.wait_ready(True,timeout=300)
vehicle.mode = VehicleMode("STABILIZE")

while(1):
    print"star armed"
    
    print "Autopilot Firmware version: %s" % vehicle.version
    #顯示autopilot版本
    print "Global Location: %s" % vehicle.location.global_frame
    #全球衛星定位系統
    print "Global Location (relative altitude): %s" % vehicle.location.global_relative_frame

    print "Local Location: %s" % vehicle.location.local_frame

    print "Attitude: %s" % vehicle.attitude

    print "Velocity: %s" % vehicle.velocity
    #速度
    print "GPS: %s" % vehicle.gps_0
    #gps資訊
    print "Groundspeed: %s" % vehicle.groundspeed

    print "Airspeed: %s" % vehicle.airspeed

    print "Gimbal status: %s" % vehicle.gimbal

    print "Battery: %s" % vehicle.battery

    print "EKF OK?: %s" % vehicle.ekf_ok

    print "Rangefinder: %s" % vehicle.rangefinder

    print "Heading: %s" % vehicle.heading

    print "Is Armable?: %s" % vehicle.is_armable

    print "System status: %s" % vehicle.system_status.state

    print "Mode: %s" % vehicle.mode.name
    
    print "Armed: %s" % vehicle.armed
    
    print("sleep 10 seconds.")
    #休息10秒
    time.sleep(10)
    print"Armed off"
    print("printed after 10 seconds.")