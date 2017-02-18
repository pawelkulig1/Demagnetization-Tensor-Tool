import simulation
import parseData
import mpmath as mp

if __name__ == '__main__':   

	'''Here is configuration file and here we can change values for simualation, example data are for emitter cyllinder shape in xy axis and rectangle receiver'''

	########################################################################################################################
														#EMITTER
    
	emitterShape = "c" # it is going to be cyllyndric
	emitterAxis = str("xy") #xy, yz, xz - possible values if we choose rectangle then set it to -1

	#receiverShape = "r"
	#receiverAxis = str("yz")

	emitterWidth = ("10e-9") #width of whole structure which is going to be divided [nm]
	emitterDepth = ("10e-9")
	emitterHeight = ("1e-9")

	emitterX = ("0")  #[m]
	#position of left bottom front corner from which (shape is going to be cut) -
	# for instance when we choose cyllinder firts we create rectangle and then from this rectangle we are cuting cyllinder
	emitterY = ("0")
	emitterZ = ("4e-9")

	emitterWidthEl = ("10") # on how many elements our structure will be divided it is important to make them cubic shape
	emitterDepthEl = ("10")
	emitterHeightEl = ("1")

	########################################################################################################################

	########################################################################################################################
													#receiver
	receiverShape = "r" #rectangle
	#receiverAxis = "-1"


	receiverWidth = ("10e-9") #width of whole structure which is going to be divided [nm]
	receiverDepth = ("10e-9")
	receiverHeight = ("1e-9")

	receiverX = ("0")  #[m]
	#position of left bottom front corner from which (shape is going to be cut) -
	# for instance when we choose cyllinder firts we create rectangle and then from this rectangle we are cuting cyllinder
	receiverY = ("0")
	receiverZ = ("0")

	receiverWidthEl = ("25") # on how many elements our structure will be divided it is important to make them cubic shape
	receiverDepthEl = ("25")
	receiverHeightEl = ("1")

	########################################################################################################################

	########################################################################################################################
														#UTILITY
	nThreads = 0
	#how many threads will program use if you leave it 0 it will automatically detect amount of possible threads
	mp.mp.dps = 64

	########################################################################################################################

	########################################################################################################################

	if emitterShape=="r":														#DON'T TOUCH
		emitterAxis="-1"
		
	if receiverShape=="r":
		receiverAxis="-1"


	emitter = parseData.ParseData(emitterWidth, emitterDepth, emitterHeight, emitterX, emitterY, emitterZ,
					  emitterWidthEl,
					  emitterDepthEl, emitterHeightEl, emitterAxis)


	receiver = parseData.ParseData(receiverWidth, receiverDepth, receiverHeight, receiverX, receiverY,
						receiverZ, receiverWidthEl, receiverDepthEl, receiverHeightEl,
						receiverAxis)

	if emitter.error[0] == 'alert':
		print(emitter.error[1], "emitter")
		exit()

	if emitter.error[0] == "yesOrNo":
		print(emitter.error[1], "emitter")

	if receiver.error[0] == 'alert':
		print(receiver.error[1], "receiver")
		exit()

	if receiver.error[0] == "yesOrNo":
		print(receiver.error[1], "receiver")

	simulation.simulate(emitter, receiver, nThreads)
	
	input("Press Enter to continue...")
