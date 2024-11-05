while True:
    # Get input values from the user
    total_bandwidth_khz = int(input("Enter total bandwidth in kHz (e.g., 33000): "))
    channel_bandwidth_khz = int(input("Enter channel bandwidth in kHz (e.g., 50): "))
    control_bandwidth_khz = int(input("Enter control channel bandwidth in kHz (e.g., 1000): "))

    # Total available channels
    total_available_channels = total_bandwidth_khz // channel_bandwidth_khz

    # Number of control channels
    control_channels = control_bandwidth_khz // channel_bandwidth_khz

    # Get cell reuse factors from the user
    reuse_factors = input("Enter reuse factors separated by commas (e.g., 4,7,12): ")
    reuse_factors = [int(n.strip()) for n in reuse_factors.split(",")]

    # Calculate and print results for each reuse factor
    for reuse_factor in reuse_factors:
        # Total channels per cell
        channels_per_cell = total_available_channels // reuse_factor
        
        # Voice channels per cell
        voice_channels = (total_available_channels - control_channels) // reuse_factor
        
        # Control channels per cell
        control_channels_per_cell = channels_per_cell - voice_channels
        
        # Display results
        print(f"\nFor {reuse_factor}-cell reuse:")
        print(f"  Total channels per cell: {channels_per_cell}")
        print(f"  Voice channels per cell: {voice_channels}")
        print(f"  Control channels per cell: {control_channels_per_cell}")

    # Ask if the user wants to repeat the process
    repeat = input("\nDo you want to enter another set of values? (yes/no): ").strip().lower()
    if repeat != 'yes':
        print("Exiting the program.")
        break
    

# 1. If a total of 33 MHz of bandwidth is allocated to a particular FDD cellular telephone 
# system which uses two 25 kHz simplex channels to provide full duplex voice and 
# control channels, compute the number of channels available per cell if a system uses- 
# (a)  4-cell reuse.  
# (b) 7-cell reuse.  
# (c) 12-cell reuse. 
# If 1 MHz of the allocated spectrum is dedicated to control channels, determine an 
# equitable distribution of control channels and voice channels in each cell for each of 
# the three systems. 
