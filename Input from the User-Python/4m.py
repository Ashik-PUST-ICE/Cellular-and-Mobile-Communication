# Constants
blocking_probability = 0.02  # 2%
lambda_calls_per_hour = 2  # Average number of calls per user per hour
average_call_duration_hours = 3 / 60  # Average call duration in hours
total_population = 2000000  # Total number of residents

# Traffic intensity calculation
A = lambda_calls_per_hour * average_call_duration_hours  # Offered traffic intensity in Erlangs

# Function to calculate users supported by each system
def calculate_users_supported(cells, channels, A_table):
    A_e = A_table.get(channels, 0)  # Get the Erlangs capacity from the table
    if A_e == 0:
        raise ValueError(f"No data for channels: {channels}")
    
    total_users = A_e / A * cells  # Total users supported
    return int(total_users)

# Erlangs capacity lookup table for different channel configurations
A_table = {
    19: 12,   # For System A
    57: 45,   # For System B
    100: 88   # For System C
}

# Main loop to collect inputs for multiple systems
while True:
    user_inputs = []
    
    while True:
        system_name = input("Enter the system name (A, B, C): ").strip().upper()
        if system_name in ['A', 'B', 'C']:
            cells = int(input(f"Enter the number of cells for System {system_name}: "))
            channels = int(input(f"Enter the number of channels per cell for System {system_name}: "))
            user_inputs.append((system_name, cells, channels))
        # No feedback for invalid input, just continue asking for valid input

        # Option to stop inputting systems
        continue_input = input("Do you want to input another system? (yes/no): ").strip().lower()
        if continue_input != 'yes':
            break

    # Calculations and results
    total_users_supported = 0
    for system_name, cells, channels in user_inputs:
        users = calculate_users_supported(cells, channels, A_table)
        market_penetration = (users / total_population) * 100
        total_users_supported += users
        print(f"System {system_name}: {users} users, Market Penetration: {market_penetration:.3f}%")

    # Combined results
    combined_market_penetration = (total_users_supported / total_population) * 100
    print(f"Total Users Supported: {total_users_supported}, Combined Market Penetration: {combined_market_penetration:.3f}%")

    # Prompt to continue the outer loop
    continue_outer = input("Do you want to input values for another batch? (yes/no): ").strip().lower()
    if continue_outer != 'yes':
        break


# 4. An urban area has a population of 2 million residents. Three competing trunked 
# mobile networks (systems A, B, and C) provide cellular service in this area. System A 
# has 394 cells with 19 channels each, system B has 98 cells with 57 channels each, and 
# system C has 49 cells, each with 100 channels. Find the number of users that can be 
# supported at 2% blocking if each user averages 2 calls per hour at an average call 
# duration of 3 minutes. Assuming that all three trunked systems are operated at 
# maximum capacity, compute the percentage market penetration of each cellular 
# provider.