# Constants
blocking_probability = 0.02  # 2%
lambda_calls_per_hour = 2  # Average number of calls per user per hour
average_call_duration_hours = 3 / 60  # Average call duration in hours
total_population = 2000000  # Total number of residents

# Traffic intensity calculation
A = lambda_calls_per_hour * average_call_duration_hours  # Offered traffic intensity in Erlangs

# Function to calculate users supported by each system
def calculate_users_supported(cells, channels, A_table):
    # Look up Erlangs for the given number of channels and blocking probability
    A_e = A_table.get(channels, 0)  # Get the Erlangs capacity from the table (for GOS = 0.02)
    if A_e == 0:
        raise ValueError(f"No data for channels: {channels}")
    
    # Calculate total number of users
    total_users = A_e / A * cells  # Total users supported
    return int(total_users)

# Erlangs capacity lookup table for different channel configurations (GOS = 0.02)
A_table = {
    19: 12,   # System A
    57: 45,   # System B
    100: 88   # System C
}

# System A calculations
cells_A = 394
channels_A = 19
users_A = calculate_users_supported(cells_A, channels_A, A_table)
market_penetration_A = (users_A / total_population) * 100

# System B calculations
cells_B = 98
channels_B = 57
users_B = calculate_users_supported(cells_B, channels_B, A_table)
market_penetration_B = (users_B / total_population) * 100

# System C calculations
cells_C = 49
channels_C = 100
users_C = calculate_users_supported(cells_C, channels_C, A_table)
market_penetration_C = (users_C / total_population) * 100

# Total calculations
total_users_supported = users_A + users_B + users_C
combined_market_penetration = (total_users_supported / total_population) * 100

# Output results
print(f"System A: {users_A} users, Market Penetration: {market_penetration_A:.3f}%")
print(f"System B: {users_B} users, Market Penetration: {market_penetration_B:.3f}%")
print(f"System C: {users_C} users, Market Penetration: {market_penetration_C:.3f}%")
print(f"Total Users Supported: {total_users_supported}, Combined Market Penetration: {combined_market_penetration:.3f}%")
