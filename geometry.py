import scipy

class Hat(Object):
    """ explicitly just unit vector without error
    which is then defined for the various coordinate
    systems based on classes based on this"""
    def __init__(self, x_hat):

        self.r = SP.array((1,))
        self.unit = scipy.matrix(x_hat)
        self.flag = []

    def __mul__(self,hat):
        """ Dot product """
        if self.flag == hat.flag:
            return self.unit.T*hat.unit
        else:
            return self.unit.T*hat.c().unit

    def cross(self):
        return  scipy.matrix(((0,-self.unit[2],self.unit[1]),
                              (self.unit[2],0,-self.unit[0]),
                              (-self.unit[1],self.unit[0],0)))


class CartHat(Hat):
    """ explicitly a cartesian unit vector, but can be set as 
    a cylindrical unit vector by setting the flag to true, all
    vector math defaults to first vector"""

    def __init__(self, x_hat):
        norm = scipy.sqrt(scipy.sum(x_hat**2))
        super(CartHat,self).__init__(x_hat/norm)
        self.flag = False
    
    def c(self):
        """ convert to cylindrical coord """
        return CylHat((scipy.sqrt(self.unit[0]**2+self.unit[1]**2),
                       scipy.arctan2(self.unit[1],self.unit[0]),
                       scipy.unit[2]))

class CylHat(Hat):
    """ explicitly a cylindrical unit vector, but can be set as 
    a cartesian unit vector by using the cart call, all
    vector math defaults to first vector"""
    
    def __init__(self, x_hat):
        norm = scipy.sqrt(x_hat[0]**2 + x_hat[2]**2)
        super(CylHat,self).__init__(x_hat/norm, err=err)
        self.flag = True

    def c(self):
        """ convert to cartesian coord """
        return CartHat((self.unit[0]*scipy.cos(self.unit[1]),
                        self.unit[0]*scipy.sin(self.unit[1]),
                        self.unit[2]))

def angle(Vec1,Vec2):
    return scipy.arccos(Vec1.hat * Vec2.hat) 

def cross(Vec1,Vec2):
    



class Vector(Object)
    
    def __init__(self, x_hat, err=scipy.array((0,0,0)),flag=False):

        self
        if flag:
            super():
            
    


class Point(Vector):
    """ a point class can only be defined relative to an origin"""
    def __init__(self, x_hat, ref, err=scipy.array((0,0,0))):
        
        self.loc = scipy.array(x_hat)
        self.error = scipy.array(err)
        self._origin = ref
        self._depth = ref._depth + 1

    def dist(self, origin):
        common = self._lca(origin)
        for i in 

    def err(self,origin):
        

    def r(self, origin):
        return scipy.sqrt(scipy.sum(self.dist(origin)**2))

    def r_err(self, origin):
        return scipy.sqrt(scipy.sum((self.dist(origin)*self.err(origin))**2)/self.r(origin))
        
    def redefine(self, neworigin):
        """ changes depth of point by calculating with respect to a new
        origin, for calculations with respect to a flux grid, etc. this
        should reduce caluclation substantially."""
        
        self.loc += self.dist(neworigin)
        self.error += self.err(neworigin)
        
        self._origin = neworigin
        self._depth = neworigin._depth + 1

    def _genPointsToParent(self, depth=self._depth):
        """ generate a list of points which leads to the overall basis
        origin of the geometry, its length will be depth"""
        temp = self
        pnts = depth*[0]
        
        for idx in range(depth):
            temp = temp._origin
            pnts[idx] = temp

        return pnts

    def _lca(self, point2):
        """ recursively solve for the common point of reference between two points
        as given by a depth number starting from the base of the tree. It will return
        a number which then provides the looping for various computations."""
        
        pt1 = self._getPointsToParent()
        pt2 = point2._getPointsToParent()
        lim = scipy.min((point2._depth,self._depth))
        found = []

        # find first uncommon ancestor
        idx = -1
        while not found:       
            if pt1[idx] is pt2[idx]:
                idx += -1
                if not lim + idx:
                    found = lim
            else:
                found = -1 - idx
        
        return found
