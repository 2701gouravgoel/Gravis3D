from body import Body
from numpy.random import normal
from vpython import *
from vpython import color
import array as arr

class Nbodies:
    """
    A class to implement all bodies.
    """
    def __init__(self, N = None):
        self.N = N or 10
        x,y,z = normal(0,1e11,N), normal(0,1e11,N), normal(0,1e11,N)
        vx,vy,vz = normal(0,1e7,N), normal(0,1e7,N), normal(0,1e7,N)
        r = abs(normal(1e9,1e8,N))
        self.bodies = []
        for i in range(0,N):
            newbody = Body(radius = r[i], pos = vector(x[i],y[i],z[i]), velocity = vector(vx[i],vy[i],vz[i]))
            #newbody = Body()
            self.bodies.append(newbody)
    
    def update(self):
        for i in range(self.N):
            for j in range(self.N):
                if i!=j:
                    self.bodies[i].attract(self.bodies[j])
                    #self.bodies[i].move()

        while(i <self.N):
            if(i>=self.N):
                break
            while(j <self.N):
                #print(self.N)
                if(j>=self.N or i>=self.N):
                    break
                if i!=j:
                    if(self.bodies[i].is_collision(self.bodies[j])):
                        m, r, v,p= self.bodies[i].merged(self.bodies[j])
                        self.bodies.remove(self.bodies[i])
                        if(i<j):
                            self.bodies.remove(self.bodies[j-1])
                        else:
                            self.bodies.remove(self.bodies[j])
                        d = (3*m)/(4*pi*r*r*r)
                        newbody = Body(radius=r,pos=p,velocity=v, colour=color.orange ,density=d)
                        self.bodies.append(newbody)
                        self.N=self.N -1
                        print(self.N,'n')
                        if(j>=self.N-1 or i>=self.N-1):
                            break
                j=j+1
            if(i>=self.N-1):
                break
            i+=1
                    


