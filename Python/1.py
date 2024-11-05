# Given values
total_bandwidth_khz = 33000  # Total bandwidth in kHz
channel_bandwidth_khz = 50   # Channel bandwidth (25 kHz * 2 for duplex)
control_bandwidth_khz = 1000 # Dedicated control bandwidth in kHz

# Total available channels
total_available_channels = total_bandwidth_khz // channel_bandwidth_khz

# Number of control channels
control_channels = control_bandwidth_khz // channel_bandwidth_khz

# List of cell reuse factors
reuse_factors = [4, 7, 12]

# Calculate and print results for each reuse factor
for reuse_factor in reuse_factors:
    # Total channels per cell
    channels_per_cell = total_available_channels // reuse_factor
    
    # Voice channels per cell
    voice_channels = (total_available_channels - control_channels) // reuse_factor
    
    # Control channels per cell
    control_channels_per_cell = channels_per_cell - voice_channels
    
    # Display results
    print(f"For {reuse_factor}-cell reuse:")
    print(f"  Total channels per cell: {channels_per_cell}")
    print(f"  Voice channels per cell: {voice_channels}")
    print(f"  Control channels per cell: {control_channels_per_cell}")
    print()
