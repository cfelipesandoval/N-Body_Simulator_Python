# The N-Body Simulator
<p align="center">
  <a>
    <img width = 800, src ="https://github.com/cfelipesandoval/N-Body_Simulator_Python/blob/b9806bebc83f8f4791950000dae5f802254cf59b/Example_Videos/OrbitingFig8.gif"
  </a>
</p>

This tool sets out to create a framework to easily create simulations for planetary motion.

## Report and Examples
The "N Body Problem Report.pdf" is a mock paper I wrote for this tool. Check out the Example_Videos folder to see some pre-rendered examples.

## Using the Tool
### Creating Instances
Each body is created as an instance of the class CelestialBody, which can be initialized as
```python
planet = CelestialBody(mass, positionVector, velocityVector)
```
You can look at the class definition and its parameters in definitions.py.

The position and velocity vectors are expected to be numpy arrays which you can initialize as
```python
import numpy as np
positionVector = np.array([x,y,z])
velocityVector = np.array([vx,vy,vz])
```
Creating an instance automatically adds that body to the list of bodies in the scene. 

I recommend initializing by first setting all the parameters and initializing by collecting each parameter into its own array
```python
M = [mass1, mass2 ... , massN] # Masses
pos = [pos1, pos2, ... , posN] # Position Vectors
vel = [ve1, vel2, ... , velN] # Velocity Vectors

for i in range(len(M)):
  CelestialBody(M[i], pos[i], vel[i], radius = rad[i], color = col[i])
```
You can also access individual instances with CelestialBody.bodies[instanceNumber] 

### Simulating
After initializing all bodies, you can run by using the createSim class method of CelestialBody
```python
sim_time = 10 # Example Simulation time
dt = 0.01 # Example Time Step
[positions, velocities] = CelestialBody.createSim(sim_time, dt)
```

The output arrays are organized per body as such at each time
```python
[[[x1,y1,z1]],
[[x2,y2,z2]],
...
[[xN,yN,zN]]]

```

So you can access the vectors by specifying a time and body of interest
```python
[x,y,z] = positions[time,bodyNum]
```

Or you can access all the positions for one body by
```python
positions[:,bodyNum]
```

You can take a look at the example function in the main.py file to get a better understanding of how it works.

## Runge-Kutta
The tool is ran with the 4th order Runge-Kutta method. Although the intention is to run it as explained in the Simulating section, you can also directly use the time step function by calling

```python
dt = 0.01 # Example time step
CelestialBody.RK4_step(dt)
```

Which can be used to simulate real-time.

## Visualization using Manim
The repo includes some files that use the visualizing tool Manim. You can install it by following [these directions](https://github.com/3b1b/manim/tree/master). 
