import sys
import json
from conclave.lang import *
from conclave.utils import *
from conclave import workflow


def protocol():

	cols_in_one = [
		defCol("car_id", "INTEGER", [1]),
		defCol("location", "INTEGER", [1])
	]
	in1 = create("in1", cols_in_one, {1})

	cols_in_two = [
		defCol("car_id", "INTEGER", [2]),
		defCol("niklas", "INTEGER", [2])
	]
	in2 = create("in2", cols_in_two, {2})

	cols_in_three = [
		defCol("car_id", "INTEGER", [3]),
		defCol("baum", "INTEGER", [3])
	]
	in3 = create("in3", cols_in_three, {3})

	join1 = join(in1, in2, 'join1', ['car_id'], ['car_id'])
	join2 = join(join1, in3, 'join2', ['car_id'], ['car_id'])
	collect(join2, 3)

	return {in1, in2,in3}


if __name__ == "__main__":

	with open(sys.argv[1], "r") as c:
		c = json.load(c)

	workflow.run(protocol, c, mpc_framework="jiff", apply_optimisations=True)
