import numpy as np

# Class Definition
class CelestialBody:
  bodies = [] # List contains all instances of object CelestialBody
  G = 6.6743e-11
  
  # NEED TO FIX INPUT G PARAMETER OR SOMETHING
  def initBodies(initFunc):
    M, pos, vel, col, rad = initFunc()
    
    # Initializing bodies in scene with initial conditions
    for i in range(len(M)):
      CelestialBody(M[i], pos[i], vel[i], radius = rad[i], color = col[i])
  
  def setGravConst(G):
    CelestialBody.G = G
  
  def __init__(self, mass, pos, vel, radius = 0.1, color = "#FFFFFF"):
    CelestialBody.bodies.append(self)
    # Initializing
    self.__pos = np.array(pos, dtype='d') # Initializing initial position
    self.__vel = np.array(vel, dtype='d') # Initializing initial velocity
    self.__mass = mass # Storing mass
    self.__radius = radius # Storing radius for animation
    self.__color = color # Storing color for animation
    
    self.bodyNum = len(CelestialBody.bodies) # Setting body number in array containing all bodies
  
  # Getters
  def getPos(self):
    return self.__pos
  
  def getVel(self):
    return self.__vel
  
  def getMass(self):
    return self.__mass
  
  def getRadius(self):
    return self.__radius
  
  def getColor(self):
    return self.__color
  
  # Setters
  def setPos(self, pos):
    self.__pos = pos
  
  def setVel(self, vel):
    self.__vel = vel
  
  def addPos(self, pos):
    self.__pos += pos
  
  def addVel(self, vel):
    self.__vel += vel
  
  def setMass(self, mass):
    self.__mass = mass
  
  def setRadius(self, radius):
    self.__radius = radius
  
  def setColor(self, color):
    self.__color = color
  
  # RK4 Functions
  def getK(poss, vels, mass):
    # Initializing variables
    accs = np.zeros((len(CelestialBody.bodies),3))
    
    # Turning into numpy array
    poss = np.array(poss)
    vels = np.array(vels)
    
    # Loop through the contribution of every "other" body
    for i in range(len(CelestialBody.bodies)):
      # np.delete makes sure the contributions from other bodies are taken into account
      possCurr = np.delete(poss, i, axis = 0) # Positions of "other" bodies
      massCurr = np.delete(mass, i, axis = 0) # Mass of "other" bodies
      
      for j in range(len(CelestialBody.bodies) - 1):
        # Add contributions to the acceleration due to every "other" body
        accs[i] -= CelestialBody.G * massCurr[j] * ((poss[i] - possCurr[j]) / np.linalg.norm(poss[i] - possCurr[j]) ** 3)
    
    return [vels, accs]
    
  def RK4_step(dt):
    # Initializing empty arrays to store "K" values for Runge-Kutta algorithm 
    # for position and velocity independently
    KR = np.zeros((4,len(CelestialBody.bodies),3))
    KV = np.zeros((4,len(CelestialBody.bodies),3))
    
    # Initializing empty arrays to store "K" values for the current step for the Runge-Kutta algorithm
    KRcurr = np.zeros((len(CelestialBody.bodies),3))
    KVcurr = np.zeros((len(CelestialBody.bodies),3))
    
    div = np.array([1,2,2,1]) # This is the constants for each iteration of "K"
    
    # Loop four times as it is RK4 and there are 4 "K's"
    for i in range(4):
      poss = []
      vels = []
      mass = []
      
      # Find input values to calculate the respective "K"
      for body, kr, kv in zip(CelestialBody.bodies, KRcurr, KVcurr):
        poss.append(body.getPos() + kr * dt / div[i])
        vels.append(body.getVel() + kv * dt / div[i])
        mass.append(body.getMass())

      KRcurr, KVcurr = CelestialBody.getK(poss, vels, mass) # Get value of current "K"
      KR[i], KV[i] = KRcurr, KVcurr # Set current K for position and velocity Independently
    
    for i in range(len(CelestialBody.bodies)):
      CelestialBody.bodies[i].addPos((1/6) * div @ KR[:,i] * dt) # Add step
      CelestialBody.bodies[i].addVel((1/6) * div @ KV[:,i] * dt) # Add step
    
  def createSim(sim_time, dt):
    """Get positions of bodies over a given time interval using RK4 algorithm
    
    Inputs: 
      time: Time interval to simulate over    
      dt: Time step
      G: Gravitational constant, default = 1
    
    Outputs:
      positions: Position of bodies at times t * dt of format
      [[[x1,y1,z1]],
      [[x2,y2,z2]],
      ...
      [[xN,yN,zN]]]
      
    """
    # Initialize empty array for position over time
    positions = np.zeros((int(sim_time/dt), len(CelestialBody.bodies), 3))
    velocities = np.zeros((int(sim_time/dt), len(CelestialBody.bodies), 3))
    
    for t in range(int(sim_time/dt)):
      currPos = [] # Current position
      currVel = [] # Current velocity
      
      for body in CelestialBody.bodies:
        currPos.append(body.getPos()) # Append current position to index of body
        currVel.append(body.getVel()) # Append current velocity to index of body

      positions[t] = currPos # Set position at time t of each body
      velocities[t] = currVel # Set position at time t of each body
      
      CelestialBody.RK4_step(dt) # Take a RK step
    
    return np.array(positions), np.array(velocities)
