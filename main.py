from c_array import Array
import random

if __name__ == "__main__":
	valueList = Array(100)
	for i in range(len(valueList)):
		valueList[i] = random.random()
	for v in valueList:
		print(v)
