# Initialize an empty set to store unique combinations
combinations = set()

# Iterate through all possible combinations
for a in range(11):
    for b in range(11):
        for c in range(11):
            for d in range(11):
                if a + b + c + d == 10:
                    # Convert the combination to a string and add it to the set
                    combination_str = f"{a}{b}{c}{d}"
                    combinations.add(combination_str)

# Print out the unique combinations
for combination in combinations:
    print(combination)
