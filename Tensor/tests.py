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
collectorAxis = str("xy")

emitterWidth = ("1e-9")
emitterDepth = ("1e-8")
emitterHeight = ("1e-8")

emitterX = ("0")
emitterY = ("0")
emitterZ = ("0")

emitterWidthEl = ("1")
emitterDepthEl = ("10")
emitterHeightEl = ("10")

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
                    emitterAxis)

simulation = SimulateThread(emitter, collector, 4)
simulation.run()