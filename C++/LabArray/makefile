CC=g++

all: startCompiling interactiveVector reverseVector simpleArray simpleVector vectorMatrix endCompiling 

startCompiling:
	@echo "### Compiling... ###"

interactiveVector: interactiveVector.cpp
	$(CC) -Wall -o interactiveVector interactiveVector.cpp

reverseVector: reverseVector.cpp
	$(CC) -Wall -o reverseVector reverseVector.cpp

simpleArray: simpleArray.cpp
	$(CC) -Wall -o simpleArray simpleArray.cpp

simpleVector: simpleVector.cpp
	$(CC) -Wall -o simpleVector simpleVector.cpp

vectorMatrix: vectorMatrix.cpp
	$(CC) -Wall -o vectorMatrix vectorMatrix.cpp

endCompiling:
	@echo "### End Compiling ###"

clean : cleaningMessage
	rm *.exe

cleaningMessage:
	@echo "Cleaning..."
