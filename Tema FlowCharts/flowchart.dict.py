
personas = [
    {"name": "Alice", "number": 10},
    {"name": "Bob", "number": 20},
    {"name": "Charlie", "number": 30},
]

# Initialize total and count
total = 0
count = 0

for p in personas:
    total += p["number"]  # Add the number to total
    count += 1  # Increment count
    
# Calculate the average
average = total / count

# Output the result
print(f"The average of the numbers is: {average}")
