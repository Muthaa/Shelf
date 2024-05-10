# Initialize an empty list to store unique combinations
combinations = []

# Iterate through all possible combinations
for a in range(11):
    for b in range(11):
        for c in range(11):
            for d in range(11):
                if a + b + c + d == 10:
                    # Convert the combination to a string and add it to the list
                    combination_str = f"{a}{b}{c}{d}"
                    combinations.append(combination_str)

# Print out the combinations in four columns
columns = 16
column_width = len(max(combinations, key=len)) + 1  # Adjust the width based on the longest combination
for i in range(0, len(combinations), columns):
    row = combinations[i:i + columns]
    print("".join(str(combination).ljust(column_width) for combination in row))
