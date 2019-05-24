import sys
import termios
import tty
from pyparrot.Bebop import Bebop

bebop = Bebop(drone_type="Bebop2")

print("connecting")
success = bebop.connect(10)
print(success)

try:
    if (success):
        print("sleeping")
        bebop.smart_sleep(2)

        bebop.ask_for_state_update()

        # set safe indoor parameters
        bebop.set_max_tilt(5)
        bebop.set_max_vertical_speed(1)

        # trying out the new hull protector parameters - set to 1 for a hull protection and 0 without protection
        bebop.set_hull_protection(1)

        tty.setcbreak(sys.stdin.fileno())
        while True:
            target = sys.stdin.read(1)

            if target == "t":
                print("take off")
                bebop.safe_takeoff(10)

            elif target == "w":
                print("move front")
                bebop.fly_direct(roll=0, pitch=30, yaw=0,
                                vertical_movement=0, duration=0.25)
                
            elif target == "s":
                print("move back")
                bebop.fly_direct(roll=0, pitch=-30, yaw=0,
                                vertical_movement=0, duration=0.25)

            elif target == "a":
                print("move left")
                bebop.fly_direct(roll=-30, pitch=0, yaw=0,
                                vertical_movement=0, duration=0.25)
                
            elif target == "d":
                print("move right")
                bebop.fly_direct(roll=30, pitch=0, yaw=0,
                                vertical_movement=0, duration=0.25)
                

            elif target == "[A":
                print("move up")
                bebop.fly_direct(roll=0, pitch=0, yaw=0,
                                vertical_movement=10, duration=0.25)
                
            elif target == "[B":
                print("move down")
                bebop.fly_direct(roll=0, pitch=0, yaw=0,
                                vertical_movement=-10, duration=0.25)
                
            elif target == "[C":
                print("move clockwise")
                bebop.fly_direct(roll=0, pitch=0, yaw=50,
                                vertical_movement=0, duration=0.1)
            elif target == "[D":
                print("move conclockwise")
                bebop.fly_direct(roll=0, pitch=0, yaw=-50,
                                vertical_movement=0, duration=0.1)

            elif target == "f":
                print("flip")
                bebop.flip(direction="front")

            elif target == "l":
                print("land")
                bebop.safe_land(10)

            elif target == "q":
                print("end")
                bebop.safe_land(10)
                break

        print("DONE - disconnecting")
        bebop.smart_sleep(5)
        print(bebop.sensors.battery)
        bebop.disconnect()

except:
    print("error!")
    bebop.safe_land(10)
    print("DONE - disconnecting")
    bebop.smart_sleep(5)
    print(bebop.sensors.battery)
    bebop.disconnect()