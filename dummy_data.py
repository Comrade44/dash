import random
import string

# Function to generate a random string of length < 20
def random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

# Generate list of dictionaries
dummy_data = []
for i in range(10):
    entry = {
        "id": i,
        "list_number": random.randint(1, 4),
        "content": random_string(random.randint(1, 19)),
        "completed":random.choice([True, False])
    }
    dummy_data.append(entry)
