import base64

# Your encoded Base64 string
encoded_str = "MWMkNzIxRVxNMSs+YmtzMWMkNzIxRVxNMSs+YmtzMWMkNzIxRVxcNCs+dHR0MWMkNzQxKkFEMCs+YmtzMWMkNzQxKkFEMCs+YmtzMWMkNzIxRVxNMSs+YmtzMWMkNzQxKkFEMCs+YmtzMWMkNzIxRVxNMSs+YmtzMWMkNzIxRVxNMSs+YmtzMkQ/NzMwSGA4LSs+dG5yMWM2QzkxRVxTMis+dHR0MkRRQzMyJz1fNSs+YnF1MWM/STUxRVxNNCs+YnF1MWM2QzQyJz1fNis+YmtzMWMkNzIyQlhuNSs+YnF1MWM2QzQyJz1fNSs+YnF1MWM/STcwSGAyMSs+dHR0MWM2QzQyJz1fNSs+YnF1MWM2QzQyJz1fNSs+YnF1MWM2QzQyJz1fNSs+YnUhMkQ/NzExRVxNMSs+YmtzMWM/STcxKkFEMCs+YmtzMWMkNzIxRVxNMSs+YmtzMWMkNzIxRVxNMSs+YmtzMWMkNzIyQlhuMys+YnUhMWMkNzIxRVxNMSs+YmtzMWMkNzIxRVxNNCs+YnF1MWM2QzQyJz1fNSs+YnF1MWM2QzQyJz1fNSs+YnF1MWM2QzQyJz1fNis+YmtzMWMkNzIxRVxNMSs+YmtzMWMkNzIyQlhuNSs+YmtzMWMkNzIxRVxNMSs+YmtzMWMkNzIxRVxNMSs+YmtzMWMkNzIxRVxNMSs+YmtzMWMkNzIxRVxNMSs+YmtzMWMkNzIxRVxNMSs+YmtzMWMkNzIxRVxNMSs+YmtzMWMkNzIxRVxNMSs+YmtzMWMkNzIxRVxNMSs+YnUhMkQ/NzExRVxNMSs+YmtzMWMkNzIxRVxNMSs+YmtzMWMkNzIxRVxNMSs+YmtzMWM/STUxRVxNMSs+YnUhMWMkNzIxRVxNNCs+YnF1MWM2QzQyJz1fNSs+YnF1MWM2QzQyJz1fNSs+YnF1MWM/STUxRVxNNCs+YnF1MWM2QzQyJz1fNSs+YnF1MWM2QzQyJz1fNSs+YnF1MWM2QzQyQlhoNCs+YmtzMWMkNzIxRVxNMSs+YmtzMWMkNzIxRVxNMSs+YmtzMWMkNzIxRVxNMSs+YmtzMWMkNzIxRVxNMSs+YmtzMWM/STUyJz1fNSs+YnF1MWM2QzQyQlhoNis+YnF1MWM2QzQyJz1fNSs+YnF1MWM2QzQyJz1fNSs+YnF1MWM2QzQyJz1fNSs+YnUhMWMkNzIxRVxNMSs+YmtzMWMkNzIxRVxNNCs+dHR0MWMkNzIxRVxNNA=="

# Decode the Base64 string
decoded_bytes = base64.b64decode(encoded_str)

# Convert to ASCII or continue decoding as necessary
decoded_str = decoded_bytes.decode('ascii', errors='ignore')  # Change 'ascii' to another encoding if needed

print("Decoded output:")
print(decoded_str)