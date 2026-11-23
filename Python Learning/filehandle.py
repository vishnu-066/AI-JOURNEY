import time
#with enumerate .......
with open("data.txt", "r") as file:
    for index, line in enumerate(file):
        if index == 0:
            continue  # Skip the header row
        print(f"Processing row {index}: {line.strip()}",flush=True)


# without enumerate    .......

with open("data.txt", "r") as file:
    for line in file:
        
        print(f"{line.strip()}",flush=True)

        time.sleep(1)  # Simulate some processing time
