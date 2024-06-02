CC=g++


all: startCompiling bool numbers simpleStrings doubleNumber checkvowel \
 divisible divisibleTwo logicWithStrings loopBreak nestedLoop \
 simpleLogic sumLoop endCompiling

startCompiling:
	@echo "### Compiling... ###"

bool: bool.cpp
	$(CC) -Wall -o bool bool.cpp

numbers: numbers.cpp
	$(CC) -Wall -o numbers numbers.cpp

simpleStrings: simpleStrings.cpp
	$(CC) -Wall -o simpleStrings simpleStrings.cpp

doubleNumber: doubleNumber.cpp
	$(CC) -Wall -o doubleNumber doubleNumber.cpp

checkvowel: checkvowel.cpp
	$(CC) -Wall -o checkvowel checkvowel.cpp

divisible: divisible.cpp
	$(CC) -Wall -o divisible divisible.cpp

divisibleTwo: divisibleTwo.cpp
	$(CC) -Wall -o divisibleTwo divisibleTwo.cpp

logicWithStrings: logicWithStrings.cpp
	$(CC) -Wall -o logicWithStrings logicWithStrings.cpp

loopBreak: loopBreak.cpp
	$(CC) -Wall -o loopBreak loopBreak.cpp

nestedLoop: nestedLoop.cpp
	$(CC) -Wall -o nestedLoop nestedLoop.cpp

simpleLogic: simpleLogic.cpp
	$(CC) -Wall -o simpleLogic simpleLogic.cpp

sumLoop: sumLoop.cpp
	$(CC) -Wall -o sumLoop sumLoop.cpp

endCompiling:
	@echo "### End Compiling ###"

clean : cleaningMessage
	rm *.exe

cleaningMessage:
	@echo "Cleaning..."
