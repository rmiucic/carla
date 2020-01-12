'''
Self-driving cars with Carla and Python tutorial 2
from youtube at
https://youtu.be/2hM44nr7Wms

+simple script to get bluprint from library
+set spawn point 
+spawn tha vehicle into the world
+set throtle 

+atach camera to the vehicle
+read camera image
+prep image to rgb in numpy 
+display images

'''

import glob
import os
import sys
import random
import time
import numpy as np
import cv2

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass
import carla

IM_WIDTH = 640
IM_HEIGHT = 480

actor_list = []

def process_image(image):
    i = np.array(image.raw_data)
    #print(i.shape)
    i2 = i.reshape((IM_HEIGHT, IM_WIDTH, 4)) #there are 4 channels in this image rgba (red, green, blue, and alfa)
    i3 = i2[:,:,:3] # rgb only not the alfa value
    cv2.imshow("", i3)
    cv2.waitKey(1)
    return i3/255
    #print(dir(image))
    #print("\n")

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


    cam_bp = blueprint_library.find("sensor.camera.rgb")
    #cam_bp.set_attribute("image_size_x", f"{IM_WIDTH}")
    #cam_bp.set_attribute("image_size_x","640")
    cam_bp.set_attribute("image_size_x",str(IM_WIDTH))

    #cam_bp.set_attribute("image_size_y", f"{IM_HEIGHT}") #for some reason f-string is giving me error
    #cam_bp.set_attribute("image_size_x","480")
    cam_bp.set_attribute("image_size_y", str(IM_HEIGHT))
    

    cam_bp.set_attribute("fov","110")

    spawn_point = carla.Transform(carla.Location(x=2.5, z=0.7))

    sensor = world.spawn_actor(cam_bp, spawn_point, attach_to = vehicle)
    actor_list.append(sensor)
    sensor.listen(lambda data: process_image(data))


    time.sleep(10)

finally:
    for actor in actor_list:
        actor.destroy()
    print("all clean up!")




