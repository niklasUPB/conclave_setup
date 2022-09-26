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
        defCol("user_data1_party1", "INTEGER", [1])
    ]
    input_1 = create("input_1", columns_in_party1, {1})
    columns_in_party2 = [
        defCol("primary_key", "INTEGER", [2]),
        defCol("user_data1_party2", "INTEGER", [2])
    ]
    input_2 = create("input_2", columns_in_party2, {2})
    Filter_party1_0 = cc_filter(input_1, "Filter_party1_0", "user_data1_party1", "==", scalar=0)
    Filter_party2_0 = cc_filter(input_2, "Filter_party2_0", "user_data1_party2", "==", scalar=0)
    Filter_party1_1 = cc_filter(input_1, "Filter_party1_1", "user_data1_party1", "==", scalar=1)
    Filter_party2_1 = cc_filter(input_2, "Filter_party2_1", "user_data1_party2", "==", scalar=1)
    join_result1 = join(Filter_party1_1, Filter_party2_1, 'join_result1', ['primary_key'], ['primary_key'])
    join_result0 = join(Filter_party1_0, Filter_party2_0, 'join_result0', ['primary_key'], ['primary_key'])

    #final_result = concat([ join_result0 , join_result1 ], "final_result", ["1","2","3"] )
    collect(join_result0, 1)
    collect(join_result1, 2)
    #collect(final_result, 2)

    return { input_1, input_2}


if __name__ == "__main__":
    with open(sys.argv[1], "r") as c:
        c = json.load(c)
    workflow.run(protocol, c, mpc_framework="jiff", apply_optimisations=True)
    

