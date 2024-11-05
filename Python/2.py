import math

# Constants
required_sir_db = 15  # Required S/I ratio in dB
num_cochannel_cells = 6  # Number of co-channel interfering cells (i0)

# Function to calculate Q (frequency reuse factor) based on cluster size N
def calculate_frequency_reuse_factor(N):
    return math.sqrt(3 * N)

# Function to calculate S/I ratio in dB
def calculate_sir(q, n, i0):
    return 10 * math.log10((q ** n) / i0)

# Path loss exponents and corresponding initial cluster sizes to test
path_loss_exponents = [4, 3]
initial_cluster_sizes = [7, 12]  # Starting cluster sizes for the cases

# Iterate over path loss exponents
for n in path_loss_exponents:
    # Start with the first cluster size for each path loss exponent
    for N in initial_cluster_sizes:
        # Calculate frequency reuse factor Q
        Q = calculate_frequency_reuse_factor(N)
        
        # Calculate S/I ratio
        sir_db = calculate_sir(Q, n, num_cochannel_cells)
        
        # Display results
        print(f"\nFor path loss exponent n = {n} and cluster size N = {N}:")
        print(f"  Frequency Reuse Factor (Q): {Q:.3f}")
        print(f"  Calculated S/I Ratio: {sir_db:.2f} dB")
        
        # Check if this meets the required S/I
        if sir_db >= required_sir_db:
            print(f"  This cluster size (N = {N}) meets the required S/I ratio of {required_sir_db} dB.")
            break
        else:
            print(f"  This cluster size (N = {N}) does NOT meet the required S/I ratio.")
