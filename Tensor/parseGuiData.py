class GuiData():
    def __init__(self, width, depth, height, x, y, z, widthEl, depthEl, heightEl,):
       self.width = width
       self.depth = depth
       self.height = height
       self.x = x
       self.y = y
       self.z = z
       self.widthEl = widthEl
       self.depthEl = depthEl
       self.heightEl = heightEl
       self.formValidation()

    def formValidation(self):
        try:                                                           
            self.width = float(self.width)
            self.depth = float(self.depth)
            self.height = float(self.height)
            self.x = float(self.x)
            self.y = float(self.y)
            self.z = float(self.z)
            self.widthEl = float(self.widthEl)
            self.depthEl = float(self.depthEl)
            self.heightEl = float(self.heightEl)
            print(self.x, self.widthEl)
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
            return "yesOrNo", "Huge amount of elements may have huge impact on calculation time"

        if self.widthEl<1:
            return  "alert", "Object must have minimum 1 element in width"

        if self.depthEl<1:
            return  "alert", "Object must have minimum 1 element in depth"

        if self.heightEl<1:
            return  "alert", "Object must have minimum 1 element in height"

