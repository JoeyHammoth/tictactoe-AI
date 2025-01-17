from main_assets.Master import Master

import csv

for j in range(0, 2000, 100):
    master = Master(c=0.2, iterations=j)

    for i in range(5):
        with open('./mcts_tests_3/test_' + str(i) + str(j), 'w', newline='') as file:
            pass
        for x in range(100):
            master.run('./mcts_tests_3/test_' + str(i) + str(j))