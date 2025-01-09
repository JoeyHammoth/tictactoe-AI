import csv

lost = 0
win = 0
draw = 0
total = 0

# Open the CSV file in read mode
with open('result.csv', 'r', newline='') as file:
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

print(win/total * 100)
print(lost/total * 100)
print(draw/total * 100)