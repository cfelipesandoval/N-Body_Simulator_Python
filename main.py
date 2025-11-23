from definitions import *
from init import *
from includes.manimScenes import * # Uncomment this with manim installed

import matplotlib.pyplot as plt

# Example Function
def example():
  # Initializing Parameters for Body 1
  mass = 1
  positionVector = np.array([1,0,0])
  velocityVector = np.array([0,1,0])
  
  # Create instance of CelestialBody for Body 1
  Body1 = CelestialBody(mass, positionVector, velocityVector)
  
  # Initializing Parameters for Body 2
  mass = 1
  positionVector = np.array([-1,0,0])
  velocityVector = np.array([0,1,0])
  
  # Create instance of CelestialBody for Body 2
  Body2 = CelestialBody(mass, positionVector, velocityVector)
  
  # Simulation Parameters
  sim_time = 10 # In Years
  dt = 0.01 # In Years
  
  CelestialBody.setGravConst(4 * np.pi ** 2) # Useful for units of solar masses and AU

  # Generate Solutions for all bodies
  [positions, velocities] = CelestialBody.createSim(sim_time, dt)
  
  # Try seeing the shape of the array
  print("Try seeing the shape of the array")
  print(positions.shape) # Format is position[time_index, bodyNum, [x,y,z]]
  print("(time_index, [x,y,z], bodyNum)")
  print("\n")
  
  # Print position of particular body at time t
  t = int(5 / dt) # 5 Years 
  bodyNum = 0 # Body to see position

  print("Print position of particular body at time t")
  print(positions[t,bodyNum])
  print("\n")
  
  # Print all positions for bodyNum over time
  print("Print all positions for body over time")
  print(positions[:,bodyNum])
  
  # Delete all instances of bodies
  CelestialBody.bodies.clear()
  
  # Example for Figure 8 Orbits
  CelestialBody.initBodies(figure8)
  
  [positions, velocities] = CelestialBody.createSim(sim_time, dt)
  
  # Plotting
  t = np.arange(0, sim_time,dt)
  # Plot "x" component of bodies
  for i in range(3):
    plt.plot(t, positions[:,i,0])
    
  plt.title("x-component of Bodies for Figure 8 Orbit")
  plt.legend(["Body 1", "Body 2", "Body 3"])
  plt.show()
  
  # Plot "y" component of bodies
  for i in range(3):
    plt.plot(t, positions[:,i,1])
    
  plt.title("y-component of Bodies for Figure 8 Orbit")
  plt.legend(["Body 1", "Body 2", "Body 3"])
  plt.show()
  
  CelestialBody.bodies.clear()

def main():
  example() # You can read code to better understand the workflow


  ## Uncomment these with manim installed
  # sim_time = 10 # Time simulation is calculated Over
  # run_time = 5 # Time simulation plays over
  # dt = 0.01 # Time step
  
  TwoBP().construct(sim_time, dt, run_time)
  # SolarSystem().construct(sim_time, dt, run_time)
  # Figure8().construct(sim_time, dt, run_time)
  # OrbitingFig8().construct(sim_time, dt, run_time)

if __name__ == "__main__":
  main()
  
  
