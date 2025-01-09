import csv

wins = []
losses = []
draws = []

for i in range(5):
    lost = 0
    win = 0
    draw = 0
    total = 0

    # Open the CSV file in read mode
    with open('./minimax_tests/test_' + str(i), 'r', newline='') as file:
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

print(sum(wins)/len(wins))
print(sum(losses)/len(losses))
print(sum(draws)/len(draws))