# Blind_NoSQL_Injector
A Python tool for performing Blind NoSQL injection attacks using regex techniques. It automates the process of data exfiltration in NoSQL databases by guessing values through a time-based or error-based Blind injection method. The tool helps penetration testers efficiently identify and exploit vulnerabilities in web applications relying on NoSQL databases.

# Features:
- Performs Blind NoSQL injection attacks using regex-based guessing.
- Supports data exfiltration from NoSQL databases.
- Easy-to-use for pentesters looking to automate the process of finding injectable points.
- Customizable parameters to adapt to different injection points or web applications.

# Requirements:
Python 3.x
requests library (can be installed via pip install requests)
Setup:
Clone the repository (if you haven't already):

```bash
git clone https://github.com/proxpvpx/Blind_NoSQL_Injector.git
```
Navigate to the directory:

```bash
cd Blind_NoSQL_Injector
```
# Modify the necessary variables in the script:

injected_data: The initial value of the data you're trying to guess.
charset: A set of characters to test for the injection (e.g., letters, digits, special characters).
target_url: The target web application's vulnerable endpoint.
success_indicator: A string that indicates a successful response from the server.
data_key: The name of the parameter you're targeting for injection (e.g., "trackingNum").
For example:

```python
target_url = "http://127.0.0.1/vulnerable-endpoint.php"
success_indicator = "True"
data_key = "trackingNum"
```
# Run the tool:

```bash
python3 Blind_NoSQL_injector.py
```
Example Output:
The tool will start exfiltrating data character by character and will print the guessed values as they are discovered. For example:

```bash
[!] Exfiltrating...
MySecurePassword123...
```

# Usage Tips:
- Ensure the target web application is vulnerable to Blind NoSQL injection.
- Modify the charset and success_indicator if the default ones are not effective for your target application.
- Use the tool in a controlled environment (e.g., during a penetration test with permission from the target organization).
# Disclaimer:
This tool is intended for educational purposes and should only be used on applications you have explicit permission to test. Unauthorized access to systems is illegal and unethical.
