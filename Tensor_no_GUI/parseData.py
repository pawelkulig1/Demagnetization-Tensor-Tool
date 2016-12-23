from mpmath import *
class ParseData():
    def __init__(self, width, depth, height, x, y, z, widthEl, depthEl, heightEl, axis): #shape == 0 rect, shape==1 cyll
        self.width = width
        self.depth = depth
        self.height = height
        self.x = x
        self.y = y
        self.z = z
        self.widthEl = widthEl
        self.depthEl = depthEl
        self.heightEl = heightEl
        self.axis = axis
        self.error = self.formValidation()

    def formValidation(self):

        if self.axis=="rectangle":
            self.axis = -1
        elif self.axis=="xy":
            self.axis = 0
        elif self.axis=="yz":
            self.axis = 1
        elif self.axis=="xz":
            self.axis = 2

        try:
            self.width = mp.mpf(self.width)
            self.depth = mp.mpf(self.depth)
            self.height = mp.mpf(self.height)
            self.x = mp.mpf(self.x)
            self.y = mp.mpf(self.y)
            self.z = mp.mpf(self.z)
            self.widthEl = mp.mpf(self.widthEl)
            self.depthEl = mp.mpf(self.depthEl)
            self.heightEl = mp.mpf(self.heightEl)
        except:
            #self.alert("Some emitter data are not numbers!")
                return "alert", "Some data are not numbers!"
            
        if self.width>1e-05:
           return "yesOrNo", "width seems very big. Are sure to use it to calculation?"
         
        if self.depth>1e-05:
           return "yesOrNo", "depth seems very big Are sure to use it to calculation?"
        
        if self.height>1e-05:
            return "yesOrNo", "height seems very big are you sure to use it to calculation?"
        

        if self.width<=0:
            return  "alert", "width must be greater than 0!"

        if self.depth<=0:
            return  "alert", "depth must be greater than 0!"

        if self.depth<=0:
            return  "alert", "depth must be greater than 0!"

        
        if self.widthEl*self.depthEl*self.heightEl>1000:
            return "yesOrNo", "Huge amount of elements may have big impact on calculation time are you sure you want to continue?"

        if self.widthEl<1:
            return  "alert", "Object must have minimum 1 element in width"

        if self.depthEl<1:
            return  "alert", "Object must have minimum 1 element in depth"

        if self.heightEl<1:
            return  "alert", "Object must have minimum 1 element in height"

        return "", ""

