import pandas as pd
import hashlib

def hash_data(data):
    h = hashlib.new("sha256")
    h.update(data)
    return h.digest()

# Function to read and hash specific columns of the CSV file
def hash_selected_columns(file_path, selected_columns):
    hash_result = hashlib.new("sha256")

    # Read only the specified columns from the CSV file into a DataFrame
    df = pd.read_csv(file_path, usecols=selected_columns)

    # Convert the DataFrame to bytes and update the hash
    hash_result.update(df.to_csv(index=False).encode('utf-8'))

    return hash_result.digest()

# File paths
input_file_path = "BTCP1.csv"
output_file_path = "hashedUsers.txt"

# Specify the columns you want to hash
selected_columns = ["id", "possibly_sensitive", "source", "text", "user_screen_name"]

# Hash specific columns of the CSV file
hashed_result = hash_selected_columns(input_file_path, selected_columns)

# Print or save the hash result
print(hashed_result)

# Write the hash result to the output file
with open(output_file_path, 'wb') as file:
    file.write(hashed_result)

print("Hashing complete!")