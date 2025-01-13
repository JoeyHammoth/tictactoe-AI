from Master import Master

import csv

for j in range(1, 11):
    master = Master(type=1, max=j)

    for i in range(5):
        with open('./minimax_tests_2/test_' + str(i) + str(j), 'w', newline='') as file:
            pass
        for x in range(100):
            master.run('./minimax_tests_2/test_' + str(i) + str(j))