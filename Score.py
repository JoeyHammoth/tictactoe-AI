import csv

total_wins = []
total_loss = []
total_draws = []
for j in range(1, 11):
    wins = []
    losses = []
    draws = []
    for i in range(5):
        lost = 0
        win = 0
        draw = 0
        total = 0

        # Open the CSV file in read mode
        with open('./minimax_tests/test_' + str(i) + str(j), 'r', newline='') as file:
            reader = csv.reader(file)  # Create a CSV reader object
            
            # Loop through each row in the CSV
            for row in reader:
                if (int(row[0]) == 1):
                    lost += 1
                elif (int(row[0]) == 3):
                    draw += 1
                else: 
                    win += 1
                total += 1

        print("Test_" + str(i))
        print(win/total * 100)
        print(lost/total * 100)
        print(draw/total * 100)
        print('\n')

        wins.append(win/total * 100)
        losses.append(lost/total * 100)
        draws.append(draw/total * 100)

    print("max_depth: " + str(j))
    print("win rate: " + str(sum(wins)/len(wins)))
    print("loss rate: " + str(sum(losses)/len(losses)))
    print("draw rate: " + str(sum(draws)/len(draws)))

    total_wins.append(sum(wins)/len(wins))
    total_loss.append(sum(losses)/len(losses))
    total_draws.append(sum(draws)/len(draws))

print('\n')
print(total_wins)
print(total_loss)
print(total_draws)