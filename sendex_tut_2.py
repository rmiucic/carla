'''
Self-driving cars with Carla and Python tutorial 2
from youtube at
https://youtu.be/2hM44nr7Wms

+simple script to get bluprint from library
+set spawn point 
+spawn tha vehicle into the world
+set throtle 

'''



import glob
import os
import sys
import random
import time

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass
import carla

actor_list = []

try:
    client = carla.Client("localhost",2000)
    client.set_timeout(2.0)

    world=client.get_world()

    blueprint_library = world.get_blueprint_library()

    bp = blueprint_library.filter("model3")[0]
    print(bp)
    
    spawn_point = random.choice(world.get_map().get_spawn_points())

    vehicle = world.spawn_actor(bp, spawn_point)
    #vehicle.set_autopilot(True)

    vehicle.apply_control(carla.VehicleControl(throttle=1.0, steer=0.0))
    actor_list.append(vehicle)

    time.sleep(10)

finally:
    for actor in actor_list:
        actor.destroy()
    print("all clean up!")




