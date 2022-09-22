import sys
import json
import timeit
from conclave.lang import *
from conclave.utils import *
from conclave import workflow

from time import gmtime, strftime


def protocol():
    columns_in_party1 = [
        defCol("primary_key", "INTEGER", [1]),
        defCol("user_data1_party1", "INTEGER", [1]),
        defCol("user_data2_party1", "INTEGER", [1]),
        defCol("user_data3_party1", "INTEGER", [1])
    ]
    input_1 = create("input_1", columns_in_party1, {1})

    columns_in_party2 = [
        defCol("primary_key", "INTEGER", [2]),
        defCol("user_data1_party2", "INTEGER", [2]),
        defCol("user_data2_party2", "INTEGER", [2]),
        defCol("user_data3_party2", "INTEGER", [2])
    ]
    input_2 = create("input_2", columns_in_party2, {2})


    join_result = join(input_1, input_2, 'join_result', ['primary_key'], ['primary_key'])
    collect(join_result, 1)
    collect(join_result, 2)

    return { input_1, input_2 }


if __name__ == "__main__":
    with open(sys.argv[1], "r") as c:
        c = json.load(c)
    workflow.run(protocol, c, mpc_framework="jiff", apply_optimisations=True)
    

