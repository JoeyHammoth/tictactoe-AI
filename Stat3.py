from Master import Master

import csv

master = Master(type=2)

for i in range(5):
    with open('./neural_tests/test_' + str(i), 'w', newline='') as file:
        pass
    for x in range(100):
        master.run('./neural_tests/test_' + str(i))