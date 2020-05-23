from vpython import color,vector, mag2, mag, sphere
from numpy import pi
from constants import G,k,dt

class Body():
    '''
    A class representing all the bodies
    in the simulation.
    '''
    def __init__(self, radius = None, pos = None, velocity = None, colour = None,density = None):
        self.radius = radius or 6.9634*1e9
        self.density = density or 1408  #avg sun density
        self.mass = (4/3)*pi*(self.radius**3)*self.density
        self.pos = pos or vector(0,0,0)
        self.velocity = velocity or vector(0,0,0)
        self.color = colour or color.green
        self.ball = sphere(pos = self.pos, radius = self.radius, color = self.color,
                           make_trail=True, trail_type='points', interval=100, retain=20)

    def move(self):
        self.pos += self.velocity*dt
        self.ball.pos = self.pos

    def attract(self, attractor):
        force = k*G*(self.mass*attractor.mass)/(mag2(attractor.pos - self.pos))
        force *= (attractor.pos - self.pos).norm()
        #print(force)
        self.velocity += force*dt
        #attractor.velocity -= force*dt
        #Sattractor.move()
        self.move()
    def is_collision(self, other):
        if (mag(self.pos-other.pos) <= self.radius + other.radius):
            return True
        else:
            return False

    def merged(self, other):
        m = self.mass + other.mass
        radius = (0.75*(1/pi)*(1/1408)*m)*(1/3)
        v = (self.mass*self.velocity + other.mass*other.velocity)/(m)
        position = (self.pos*self.mass + other.pos*other.mass)/(m)
        return m, radius, v,position
