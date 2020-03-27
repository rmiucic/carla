# carla
In this exercise I used 
1. carla 0.9.7 [carla.org](http://carla.org/) 
2. runnig on Linux ubuntu 16.04 LTS
3. python 3.5 installed in a [conda](https://docs.conda.io/projects/conda/en/latest/index.html) environment
4. tutorials form https://pythonprogramming.net namely Introduction - Self-driving cars with Carla and Python part  and Reinforcement Learning

## Prerequsites
the following is needed
1. in a terminal create conda environment named py35
```shell
conda create -n py35 python=3.5
```
-
2. activate py35 environment
```shell
source activate py35
```
-
3. install needed components
```shell
conda install --channel https://conda.anaconda.org/menpo opencv3
```
```shell
conda install system
```
```shell
conda install py
```
...
4. go to the carla istallation
```shell
cd ~/carla97/PythonAPI/examples/
```

for the reinforced learning install (this is not in the conda environment) 
```
pip install gym
pip install matplotlib
```

## scripts
Use these py scripts in examples of the Python API folder e.g. ```/home/radovan/carla97/PythonAPI/examples```
or change path in the following code  
```python
try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass
import carla
```
The code is following the sendex tutorial on youtube
[Self-driving cars with Carla and Python](https://youtu.be/J1F32aVSYaU) 


## blueprint
vehicle
static
controller
sensor
walker

### Vehicle
vehicle.audi.a2
vehicle.audi.tt
vehicle.audi.etron
vehicle.bmw.isetta
vehicle.carlamotors.carlacola
vehicle.citroen.c3
vehicle.dodge_charger.police
vehicle.harley-davidson.low rider
vehicle.mercedes-benz.coupe
vehicle.bmw.grandtourer
vehicle.toyota.prius
vehicle.yamaha.yzf
vehicle.nissan.patrol
vehicle.bh.crossbike
vehicle.ford.mustang
vehicle.tesla.model3
vehicle.diamondback.century
vehicle.gazelle.omafiets
vehicle.seat.leon
vehicle.lincoln.mkz2017
vehicle.kawasaki.ninja
vehicle.volkswagen.t2
vehicle.nissan.micra
vehicle.chevrolet.impala
vehicle.mini.cooperst
vehicle.jeep.wrangler_rubicon

### Sensors
sensor.other.obstacle
sensor.other.collision
sensor.other.gnss
sensor.camera.semantic_segmentation
sensor.lidar.ray_cast
sensor.other.imu
sensor.other.radar
sensor.camera.depth
sensor.camera.rgb
sensor.other.lane_invasion

### aributes
**vehicle.tesla.model3**
ActorAttribute(id=number_of_wheels,type=int,value=4(const))
ActorAttribute(id=sticky_control,type=bool,value=True)
ActorAttribute(id=object_type,type=str,value=(const))
ActorAttribute(id=color,type=Color,value=Color(140,0,0,255))
ActorAttribute(id=role_name,type=str,value=autopilot)

 **sensor.camera.rgb**
ActorAttribute(id=chromatic_aberration_intensity,type=float,value=0)
ActorAttribute(id=white_clip,type=float,value=0.04)
ActorAttribute(id=toe,type=float,value=0.55)
ActorAttribute(id=shoulder,type=float,value=0.26)
ActorAttribute(id=blur_radius,type=float,value=0)
ActorAttribute(id=blur_amount,type=float,value=1)
ActorAttribute(id=blade_count,type=int,value=5)
ActorAttribute(id=min_fstop,type=float,value=1.2)
ActorAttribute(id=exposure_speed_up,type=float,value=3)
ActorAttribute(id=exposure_min_bright,type=float,value=0.1)
ActorAttribute(id=motion_blur_min_object_screen_size,type=float,value=0.1)
ActorAttribute(id=slope,type=float,value=0.88)
ActorAttribute(id=motion_blur_max_distortion,type=float,value=0.35)
ActorAttribute(id=motion_blur_intensity,type=float,value=0.45)
ActorAttribute(id=enable_postprocess_effects,type=bool,value=True)
ActorAttribute(id=temp,type=float,value=6500)
ActorAttribute(id=iso,type=float,value=1200)
ActorAttribute(id=tint,type=float,value=0)
ActorAttribute(id=calibration_constant,type=float,value=16)
ActorAttribute(id=shutter_speed,type=float,value=60)
ActorAttribute(id=focal_distance,type=float,value=1000)
ActorAttribute(id=exposure_compensation,type=float,value=3)
ActorAttribute(id=exposure_mode,type=str,value=manual)
ActorAttribute(id=lens_y_size,type=float,value=0.08)
ActorAttribute(id=lens_x_size,type=float,value=0.08)
ActorAttribute(id=lens_kcube,type=float,value=0)
ActorAttribute(id=gamma,type=float,value=2.2)
ActorAttribute(id=lens_k,type=float,value=-1)
ActorAttribute(id=exposure_max_bright,type=float,value=2)
ActorAttribute(id=fstop,type=float,value=1.4)
ActorAttribute(id=lens_circle_multiplier,type=float,value=0)
ActorAttribute(id=lens_circle_falloff,type=float,value=5)
ActorAttribute(id=black_clip,type=float,value=0)
ActorAttribute(id=fov,type=float,value=90)
ActorAttribute(id=exposure_speed_down,type=float,value=1)
ActorAttribute(id=image_size_y,type=int,value=600)
ActorAttribute(id=image_size_x,type=int,value=800)
ActorAttribute(id=sensor_tick,type=float,value=0)
ActorAttribute(id=chromatic_aberration_offset,type=float,value=0)
ActorAttribute(id=role_name,type=str,value=front)

**sensor.other.gnss**
ActorAttribute(id=noise_alt_bias,type=float,value=0)
ActorAttribute(id=noise_alt_stddev,type=float,value=0)
ActorAttribute(id=noise_lon_bias,type=float,value=0)
ActorAttribute(id=noise_lon_stddev,type=float,value=0)
ActorAttribute(id=noise_lat_bias,type=float,value=0)
ActorAttribute(id=noise_seed,type=int,value=0)
ActorAttribute(id=noise_lat_stddev,type=float,value=0)
ActorAttribute(id=sensor_tick,type=float,value=0)
ActorAttribute(id=role_name,type=str,value=default)

**sensor.other.imu**
ActorAttribute(id=noise_gyro_stddev_y,type=float,value=0)
ActorAttribute(id=noise_gyro_stddev_x,type=float,value=0)
ActorAttribute(id=noise_gyro_stddev_z,type=float,value=0)
ActorAttribute(id=noise_accel_stddev_y,type=float,value=0)
ActorAttribute(id=noise_accel_stddev_x,type=float,value=0)
ActorAttribute(id=noise_accel_stddev_z,type=float,value=0)
ActorAttribute(id=noise_seed,type=int,value=0)
ActorAttribute(id=noise_gyro_bias_x,type=float,value=0)
ActorAttribute(id=sensor_tick,type=float,value=0)
ActorAttribute(id=noise_gyro_bias_z,type=float,value=0)
ActorAttribute(id=noise_gyro_bias_y,type=float,value=0)
ActorAttribute(id=role_name,type=str,value=default)

## notable issues
the f string was not working for me so for example instead of 
```python
self.rbg_cam.set_attribute("image_size_y",f"{self.im_height}")
```
I used 
```python
self.rbg_cam.set_attribute("image_size_y",str(self.im_height))
```
## how to 
### how to load new map in CARLA 
To load new town follow the instructions from 
https://github.com/carla-simulator/carla/issues/1943

in first terminal open carla
```
<carla install folder>$ ./CarlaUE4.sh
```
in second terminal start conda environment with python 3.5
```
$ source activate py35
```

carla config utility. The following command will list of what is posible to change in real time
```
<carla install folder>/PythonAPI/util$ python config.py -h
```
the otput looks like 
```
(py35) radovan@radovan-GS63VR-6RF:~/carla97/PythonAPI/util$ python config.py -h
usage: config.py [-h] [--host H] [-p P] [-d] [-m MAP] [-r] [--delta-seconds S]
                 [--fps N] [--rendering] [--no-rendering] [--no-sync]
                 [--weather WEATHER] [-i] [-l] [-b FILTER]

Configure and inspect an instance of CARLA Simulator. For further details,
visit https://carla.readthedocs.io/en/latest/configuring_the_simulation/

optional arguments:
  -h, --help            show this help message and exit
  --host H              IP of the host CARLA Simulator (default: localhost)
  -p P, --port P        TCP port of CARLA Simulator (default: 2000)
  -d, --default         set default settings
  -m MAP, --map MAP     load a new map, use --list to see available maps
  -r, --reload-map      reload current map
  --delta-seconds S     set fixed delta seconds, zero for variable frame rate
  --fps N               set fixed FPS, zero for variable FPS (similar to
                        --delta-seconds)
  --rendering           enable rendering
  --no-rendering        disable rendering
  --no-sync             disable synchronous mode
  --weather WEATHER     set weather preset, use --list to see available
                        presets
  -i, --inspect         inspect simulation
  -l, --list            list available options
  -b FILTER, --list-blueprints FILTER
                        list available blueprints matching FILTER (use '*' to
                        list them all)
```
to change town to Town03
```
(py35) radovan@radovan-GS63VR-6RF:~/carla97/PythonAPI/util$ python config.py -m Town03
```
to change weather town to Town03
```
(py35) radovan@radovan-GS63VR-6RF:~/carla97/PythonAPI/util$ python config.py --weather WetCloudySunset
set weather preset 'WetCloudySunset'.
```

list towns and weather
```
(py35) radovan@radovan-GS63VR-6RF:~/carla97/PythonAPI/util$ python config.py --list
weather presets:

    ClearNoon, ClearSunset, CloudyNoon, CloudySunset, Default,
    HardRainNoon, HardRainSunset, MidRainSunset, MidRainyNoon,
    SoftRainNoon, SoftRainSunset, WetCloudyNoon, WetCloudySunset,
    WetNoon, WetSunset.

available maps:

    Town01, Town02, Town03, Town04, Town05.
```
to list all blueprints
```
(py35) radovan@radovan-GS63VR-6RF:~/carla97/PythonAPI/util$ python config.py --list-blueprints '*'
available blueprints (filter '*'):

    controller.ai.walker
    sensor.camera.depth
    sensor.camera.rgb
    sensor.camera.semantic_segmentation
    sensor.lidar.ray_cast
    sensor.other.collision
    sensor.other.gnss
    sensor.other.imu
    sensor.other.lane_invasion
    sensor.other.obstacle
    sensor.other.radar
    static.prop.advertisement
    static.prop.atm
    static.prop.barbeque
    static.prop.barrel
    static.prop.bench01
    static.prop.bench02
    static.prop.bench03
    static.prop.bike helmet
    static.prop.bikeparking
    static.prop.bin
    static.prop.box01
    static.prop.box02
    static.prop.box03
    static.prop.briefcase
    static.prop.brokentile01
    static.prop.brokentile02
    static.prop.brokentile03
    static.prop.brokentile04
    static.prop.busstop
    static.prop.chainbarrier
    static.prop.chainbarrierend
    static.prop.clothcontainer
    static.prop.clothesline
    static.prop.colacan
    static.prop.constructioncone
    static.prop.container
    static.prop.creasedbox01
    static.prop.creasedbox02
    static.prop.creasedbox03
    static.prop.dirtdebris01
    static.prop.dirtdebris02
    static.prop.dirtdebris03
    static.prop.doghouse
    static.prop.fountain
    static.prop.garbage01
    static.prop.garbage02
    static.prop.garbage03
    static.prop.garbage04
    static.prop.garbage05
    static.prop.garbage06
    static.prop.gardenlamp
    static.prop.glasscontainer
    static.prop.gnome
    static.prop.guitarcase
    static.prop.ironplank
    static.prop.kiosk_01
    static.prop.mailbox
    static.prop.maptable
    static.prop.mobile
    static.prop.motorhelmet
    static.prop.pergola
    static.prop.plantpot01
    static.prop.plantpot02
    static.prop.plantpot03
    static.prop.plantpot04
    static.prop.plantpot05
    static.prop.plantpot06
    static.prop.plantpot07
    static.prop.plantpot08
    static.prop.plasticbag
    static.prop.plasticchair
    static.prop.plastictable
    static.prop.platformgarbage01
    static.prop.purse
    static.prop.shop01
    static.prop.shoppingbag
    static.prop.shoppingcart
    static.prop.shoppingtrolley
    static.prop.slide
    static.prop.streetbarrier
    static.prop.streetfountain
    static.prop.streetsign
    static.prop.streetsign01
    static.prop.streetsign04
    static.prop.swing
    static.prop.swingcouch
    static.prop.table
    static.prop.trafficcone01
    static.prop.trafficcone02
    static.prop.trafficwarning
    static.prop.trampoline
    static.prop.trashbag
    static.prop.trashcan01
    static.prop.trashcan02
    static.prop.trashcan03
    static.prop.trashcan04
    static.prop.trashcan05
    static.prop.travelcase
    static.prop.vendingmachine
    static.prop.wateringcan
    static.trigger.friction
    vehicle.audi.a2
    vehicle.audi.etron
    vehicle.audi.tt
    vehicle.bh.crossbike
    vehicle.bmw.grandtourer
    vehicle.bmw.isetta
    vehicle.carlamotors.carlacola
    vehicle.chevrolet.impala
    vehicle.citroen.c3
    vehicle.diamondback.century
    vehicle.dodge_charger.police
    vehicle.ford.mustang
    vehicle.gazelle.omafiets
    vehicle.harley-davidson.low rider
    vehicle.jeep.wrangler_rubicon
    vehicle.kawasaki.ninja
    vehicle.lincoln.mkz2017
    vehicle.mercedes-benz.coupe
    vehicle.mini.cooperst
    vehicle.nissan.micra
    vehicle.nissan.patrol
    vehicle.seat.leon
    vehicle.tesla.model3
    vehicle.toyota.prius
    vehicle.volkswagen.t2
    vehicle.yamaha.yzf
    walker.pedestrian.0001
    walker.pedestrian.0002
    walker.pedestrian.0003
    walker.pedestrian.0004
    walker.pedestrian.0005
    walker.pedestrian.0006
    walker.pedestrian.0007
    walker.pedestrian.0008
    walker.pedestrian.0009
    walker.pedestrian.0010
    walker.pedestrian.0011
    walker.pedestrian.0012
    walker.pedestrian.0013
    walker.pedestrian.0014

```
---
