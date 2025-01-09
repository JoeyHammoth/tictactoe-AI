from Master import Master

import csv

master = Master()

for i in range(5):
    with open('./minimax_tests/test_' + str(i), 'w', newline='') as file:
        pass
    for x in range(100):
        master.run('./minimax_tests/test_' + str(i))