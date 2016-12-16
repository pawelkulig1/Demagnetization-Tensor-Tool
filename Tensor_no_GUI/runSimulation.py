import simulation
import parseData


'''Here is configuration file and here we can change values for simualation, example data are for emitter cyllinder shape in xy axis and rectangle'''

########################################################################################################################
                                                    #EMITTER

emitterShape = "c" # it is going to be cyllyndric
emitterAxis = str("xy") #xy, yz, xz - possible values if we choose rectangle then set it to -1

#collectorShape = "r"
#collectorAxis = str("yz")

emitterWidth = ("1e-9") #width of whole structure which is going to be divided [nm]
emitterDepth = ("5e-7")
emitterHeight = ("5e-7")

emitterX = ("0")  #[nm]
#position of left bottom front corner from which (shape is going to be cut) -
# for instance when we choose cyllinder firts we create rectangle and then from this rectangle we are cuting cyllinder
emitterY = ("0")
emitterZ = ("0")

emitterWidthEl = ("1") # on how many elements our structure will be divided it is important to make them cubic shape
emitterDepthEl = ("50")
emitterHeightEl = ("50")

########################################################################################################################

########################################################################################################################
                                                    #COLLECTOR
collectorShape = "r" #rectangle
collectorAxis = "-1"

collectorWidth = ("1e-9") #width of whole structure which is going to be divided [nm]
collectorDepth = ("5e-7")
collectorHeight = ("5e-7")

collectorX = ("0")  #[nm]
#position of left bottom front corner from which (shape is going to be cut) -
# for instance when we choose cyllinder firts we create rectangle and then from this rectangle we are cuting cyllinder
collectorY = ("0")
collectorZ = ("0")

collectorWidthEl = ("1") # on how many elements our structure will be divided it is important to make them cubic shape
collectorDepthEl = ("50")
collectorHeightEl = ("50")

########################################################################################################################

########################################################################################################################
                                                    #UTILITY
nThreads = 0
#how many threads will program use if you leave it 0 it will automatically detect amount of possible threads


########################################################################################################################

########################################################################################################################
                                                    #DON'T TOUCH

emitter = parseData.ParseData(emitterWidth, emitterDepth, emitterHeight, emitterX, emitterY, emitterZ,
                  emitterWidthEl,
                  emitterDepthEl, emitterHeightEl, emitterAxis)


collector = parseData.ParseData(collectorWidth, collectorDepth, collectorHeight, collectorX, collectorY,
                    collectorZ, collectorWidthEl, collectorDepthEl, collectorHeightEl,
                    collectorAxis)

if emitter.error[0] == 'alert':
    print(emitter.error[1], "emitter")
    exit()

if emitter.error[0] == "yesOrNo":
    print(emitter.error[1], "emitter")

if collector.error[0] == 'alert':
    print(collector.error[1], "collector")
    exit()

if collector.error[0] == "yesOrNo":
    print(collector.error[1], "collector")

simulation.simulate(emitter, collector, nThreads)



