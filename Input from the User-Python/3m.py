# Problem-3: Calculate the number of users supported for blocking probabilities
# for different numbers of trunked channels in a blocked calls cleared system.

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

def calculate_supported_users(trunked_channels, traffic_intensity_per_user):
    # Get the offered traffic intensity (A) from the table based on trunked channels
    if trunked_channels in erlang_table:
        A = erlang_table[trunked_channels]
        # Calculate total number of users (U)
        U = A / traffic_intensity_per_user
        
        # Since one channel can only support one user, round up to the next whole number
        return max(1, round(U))  # Ensure at least 1 user can be supported
    else:
        return None  # Return None if trunked channels not found in the table

while True:
    # Get user inputs for blocking probability and traffic intensity
    blocking_probability = float(input("Enter the blocking probability (in 0.5 %): "))
    traffic_intensity_per_user = float(input("Enter the traffic intensity per user (in Erlangs 0.1): "))

    # Get trunked channels from user
    trunked_channels_input = input("Enter the trunked channels (comma-separated, e.g., 1, 5, 10, 20, 100): ")
    trunked_channels_list = list(map(int, trunked_channels_input.split(',')))

    # Output results for each number of trunked channels
    for channels in trunked_channels_list:
        users_supported = calculate_supported_users(channels, traffic_intensity_per_user)
        if users_supported is not None:
            print(f"Trunked Channels: {channels}, Supported Users: {users_supported}")
        else:
            print(f"Trunked Channels: {channels} not found in the table.")

    # Ask if the user wants to input more values
    continue_input = input("Do you want to input another set of values? (yes/no): ").strip().lower()
    if continue_input != 'yes':
        break


# 3. How many users can be supported for 0.5% blocking probability for the following 
# number of trunked channels in a blocked calls cleared system? 
# (a) 1,   
# (b) 5,   
# (c) 10,   

# (d) 20,  
# (e) 100.
# Assume each user generates 0.1 Erlangs of traffic. 