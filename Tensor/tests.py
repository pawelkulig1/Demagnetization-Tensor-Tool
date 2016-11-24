from simulation import *
from parseGuiData import *
from simulation import *

#emitterShape = "r"
#emitterAxis = "-1"

emitterShape = "c"
emitterAxis = str("yz")


#collectorShape = "r"
#collectorAxis = "-1"

collectorShape = "c"
collectorAxis = str("yz")

emitterWidth = ("1e-9")
emitterDepth = ("1e-7")
emitterHeight = ("1e-7")

emitterX = ("0")
emitterY = ("0")
emitterZ = ("0")

emitterWidthEl = ("1")
emitterDepthEl = ("100")
emitterHeightEl = ("100")

emitter = GuiData(emitterWidth, emitterDepth, emitterHeight, emitterX, emitterY, emitterZ,
                  emitterWidthEl,
                  emitterDepthEl, emitterHeightEl, emitterAxis)
'''
collectorWidth = ("1e-8")
collectorDepth = ("1e-8")
collectorHeight = ("1e-9")

collectorX = ("0")
collectorY = ("0")
collectorZ = ("0")

collectorWidthEl = ("1")
collectorDepthEl = ("10")
collectorHeightEl = ("10")'''

collector = GuiData(emitterWidth, emitterDepth, emitterHeight, emitterX, emitterY,
                    emitterZ, emitterWidthEl, emitterDepthEl, emitterHeightEl,
                    collectorAxis)

simulation = SimulateThread(emitter, collector, 4)
simulation.run()

'''
xpoint = 2.22+1e-9
ypoint = 2.22+4e-9
zpoint = 2.22+4e-9

width = 1e-9
depth = 1e-8
height = 1e-8

xpoz = 2.22
ypoz = 2.22
zpoz = 2.22

#if ((xpoint - self.width - self.xpoz) ** 2 / self.width ** 2) + ((ypoint - self.depth-self.ypoz) ** 2 / self.depth ** 2) <= 1 and zpoint <= self.zpoz + self.height and zpoint >= self.zpoz:

print(((ypoint-depth - ypoz) ** 2 / (depth ** 2)) + ((zpoint-height - zpoz) ** 2 /(height ** 2)) <= 1 and xpoint <= width+xpoz and xpoint >= xpoz)
'''