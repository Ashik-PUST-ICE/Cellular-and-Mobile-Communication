# Problem-3: Calculate the number of users supported for a 0.5% blocking probability
# for different numbers of trunked channels in a blocked calls cleared system.

# Given values
blocking_probability = 0.5  # in percent
traffic_intensity_per_user = 0.1  # in Erlangs

# Convert blocking probability from percentage to decimal
pb = blocking_probability / 100

# Erlang B capacity table for 0.5% GOS (blocking probability)
erlang_table = {
    1: 0.005,
    2: 0.105,
    4: 0.701,
    5: 1.1300,
    10: 3.9600,
    20: 11.1000,
    100: 80.9000
}

def calculate_supported_users(trunked_channels):
    # Get the offered traffic intensity (A) from the table based on trunked channels
    if trunked_channels in erlang_table:
        A = erlang_table[trunked_channels]
        # Calculate total number of users (U)
        U = A / traffic_intensity_per_user
        
        # Since one channel can only support one user, round up to the next whole number
        return max(1, round(U))  # Ensure at least 1 user can be supported
    else:
        return None  # Return None if trunked channels not found in the table

# List of trunked channels to test
trunked_channels_list = [1, 5, 10, 20, 100]

# Output results for each number of trunked channels
for channels in trunked_channels_list:
    users_supported = calculate_supported_users(channels)
    print(f"Trunked Channels: {channels}, Supported Users: {users_supported}")
