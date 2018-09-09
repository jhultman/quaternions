import numpy as np


class Quaternion:

    def __init__(self, *args):
        assert len(args) in (1, 4)
        if len(args) == 4:
            vec = np.array(args)
        elif len(args[0]) == 4:
            vec = np.array(args[0])
        else: raise ValueError
        self._vec = vec
        

    def __getitem__(self, i):
        return self.vec.__getitem__(i)
   

    def __str__(self):
        return self.vec.__str__()
    

    def __repr__(self):
        return self.vec.__repr__()
    

    def __iter__(self):
        return self.vec.__iter__()
       

    def __add__(q0, q1):
        return q0.vec + q1.vec


    def __sub__(q0, q1):
        return q0.vec - q1.vec


    def __div__(*args):
        msg = '''Division ambiguous. Use 
        multiplication by inverse.'''
        raise NotImplementedError(msg)
    

    def __floordiv__(*args):
        Quaternion.__div__(*args)
        

    def __truediv__(*args):
        Quaternion.__div__(*args)
    

    def __neg__(self):
        return Quaternion(*-self.vec)
    

    def __pos__(self):
        return self
   

    def __rmul__(q, a):
        vec = a * q.vec
        return Quaternion(*vec)


    def __mul__(q0, q1):
        '''Hamiltonian product of q0 and q1.'''
        w0, x0, y0, z0 = q0
        w1, x1, y1, z1 = q1

        w = + w0*w1 - x0*x1 - y0*y1 - z0*z1
        x = + w0*x1 + x0*w1 + y0*z1 - z0*y1
        y = + w0*y1 - x0*z1 + y0*w1 + z0*x1
        z = + w0*z1 + x0*y1 - y0*x1 + z0*w1
        return Quaternion(w, x, y, z)
    

    @property
    def w(self):
        return self.vec[0]


    @property
    def xyz(self):
        return self.vec[1:]
      

    @property
    def norm(self):
        return np.linalg.norm(self.vec)
    

    @property
    def vec(self):
        return self._vec
   

    @property
    def conj(self):
        return Quaternion(self.w, *-self.xyz)
    

    @property
    def inv(self):
        return 1 / self.norm * self.conj
    

    def from_xyz(xyz):
        return Quaternion(0, *xyz)


    def rotation(theta, axis):
        axis /= np.linalg.norm(axis)
        w = np.cos(theta / 2)
        xyz = np.sin(theta / 2) * axis
        return Quaternion(w, *xyz)
    

    def euler_rotation(theta):
        msg = 'Expected length 3 theta for x, y, z axes.'
        assert len(theta) == 3, msg
        
        I = np.eye(3)
        rot = lambda i: Quaternion.rotation(theta[i], I[i, :])
        return rot(0) * rot(1) * rot(2)
    

    def rotate(v, q):
        '''Rotate pure quaternion v by q.'''
        return q * v * q.inv
