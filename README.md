# carla
use these py scripts in examples of the Python API folder e.g. ```/home/radovan/carla97/PythonAPI/examples```
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
