import math

# Function to calculate frequency reuse factor Q based on cluster size N
def calculate_frequency_reuse_factor(N):
    return math.sqrt(3 * N)

# Function to calculate S/I ratio in dB
def calculate_sir(q, n, i0):
    return 10 * math.log10((q ** n) / i0)

# Main loop to allow multiple inputs
while True:
    try:
        # Get user input for required S/I ratio and number of co-channel cells
        required_sir_db = float(input("Enter the required S/I ratio in dB (e.g., 15): "))
        num_cochannel_cells = int(input("Enter the number of co-channel interfering cells (e.g., 6): "))

        # Get path loss exponent and cluster sizes
        path_loss_exponent = int(input("Enter the path loss exponent (e.g., 3 or 4): "))
        cluster_sizes = input("Enter possible cluster sizes separated by commas (e.g., 7, 12): ")
        
        # Convert cluster sizes from string to list of integers
        cluster_sizes = [int(size.strip()) for size in cluster_sizes.split(",")]

        # Iterate over cluster sizes
        for N in cluster_sizes:
            # Calculate frequency reuse factor Q
            Q = calculate_frequency_reuse_factor(N)
            
            # Calculate S/I ratio
            sir_db = calculate_sir(Q, path_loss_exponent, num_cochannel_cells)
            
            # Display results
            print(f"\nFor path loss exponent n = {path_loss_exponent} and cluster size N = {N}:")
            print(f"  Frequency Reuse Factor (Q): {Q:.3f}")
            print(f"  Calculated S/I Ratio: {sir_db:.2f} dB")
            
            # Check if this meets the required S/I
            if sir_db >= required_sir_db:
                print(f"  This cluster size (N = {N}) meets the required S/I ratio of {required_sir_db} dB.")
            else:
                print(f"  This cluster size (N = {N}) does NOT meet the required S/I ratio.")

    except ValueError:
        print("Invalid input. Please enter numeric values where required.")
    
    # Ask if the user wants to repeat the process
    repeat = input("\nDo you want to enter another set of values? (yes/no): ").strip().lower()
    if repeat != 'yes':
        print("Exiting the program.")
        break



# 2. If a signal to interference ratio of 15 dB is required for satisfactory forward channel 
# performance of a cellular system, what is the frequency reuse factor and cluster size 
# that should be used for maximum capacity if the path loss exponent is- 
# (a) n = 4.    
# (b) n = 3. 
# Assume that there are 6 co-channels cells in the first tier and all of them are at the 
# same distance from the mobile. Use suitable approximations. 