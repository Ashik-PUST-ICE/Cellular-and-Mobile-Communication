import math

def power_conversion(transmitter_power_watts):
    # Convert watts to milliwatts
    power_mw = transmitter_power_watts * 1000
    # Convert mW to dBm
    power_dbm = 10 * math.log10(power_mw)
    # Convert W to dBW
    power_dbw = 10 * math.log10(transmitter_power_watts)
    return power_dbm, power_dbw

def received_power(distance_m, transmitter_power_w, gt, gr, frequency_hz):
    c = 3 * 10**8  # Speed of light in m/s
    # Calculate wavelength in meters
    wavelength = c / frequency_hz
    # Calculate received power using the Friis transmission equation
    pr = (transmitter_power_w * gt * gr * (wavelength**2)) / ((4 * math.pi * distance_m)**2)
    # Convert from Watts to dBm
    pr_dbm = 10 * math.log10(pr * 1000)  # Convert to mW before logging
    return pr_dbm

def received_power_at_distance(pr_100_dbm, distance_m, reference_distance_m):
    # Calculate the path loss in dB
    path_loss = 20 * math.log10(distance_m / reference_distance_m)
    # Calculate received power at new distance
    pr_new_dbm = pr_100_dbm - path_loss
    return pr_new_dbm

# Given data
transmitter_power_w = 50  # Transmitter power in watts
gt = 1  # Transmitter gain (unity)
gr = 1  # Receiver gain (unity)
frequency_hz = 900 * 10**6  # Carrier frequency in Hz

# Step 1: Convert power
power_dbm, power_dbw = power_conversion(transmitter_power_w)

# Step 2: Calculate received power at 100 m
distance_100_m = 100  # Distance in meters
received_power_100_dbm = received_power(distance_100_m, transmitter_power_w, gt, gr, frequency_hz)

# Step 3: Calculate received power at 10 km
reference_distance_m = 100  # Reference distance in meters
distance_10_km = 10000  # Distance in meters
received_power_10_km_dbm = received_power_at_distance(received_power_100_dbm, distance_10_km, reference_distance_m)

# Display results in the specified format
print(f"Final Results:")
print(f"(a) Transmitter power P_t in dBm: {power_dbm:.1f} dBm")
print(f"(b) Transmitter power P_t in dBW: {power_dbw:.1f} dBW")
print(f"(c) Received power P_r at 100 m in dBm: {received_power_100_dbm:.1f} dBm")
print(f"(d) Received power P_r at 10 km in dBm: {received_power_10_km_dbm:.1f} dBm")
