import math

# Constants
c = 3 * 10**8  # Speed of light in m/s
f = 900  # Frequency in MHz
g = 2.55  # Gain of antenna in dB

# Question (a)
# Convert gain from dB to linear scale
gain_linear = 10 ** (g / 10)  # Gain in linear scale

# Calculate wavelength in meters
lambda_ = c / (f * 10**6)

# Calculate length of the antenna (1/4 of wavelength)
L = lambda_ / 4  # Length of the antenna in meters

# Display results for part (a)
print('For (a)')
print('---------')
print(f'Length of the antenna: {L * 100:.2f} cm')  # Convert to cm
print(f'Gain of the antenna: {gain_linear:.2f} = {g:.2f} dB\n')

# Question (b)
d = 5000  # T-R separation distance in meters
E0 = 10**-3  # Electric-field in V/m
d0 = 1000  # Reference distance in meters
ht = 50  # Height of transmitting antenna in meters
hr = 1.5  # Height of receiving antenna in meters

# Electric Field Calculation
Er_d = (2 * E0 * d0 * 2 * math.pi * ht * hr) / (lambda_ * d**2)  # Electric Field in V/m

# Effective Aperture Calculation
Ae = (gain_linear * lambda_**2) / (4 * math.pi)  # Effective Aperture in m²

# Received Power Calculation
Pr = (Er_d**2 / (120 * math.pi)) * Ae  # Received power in watts
Pr_dB = 10 * math.log10(Pr)  # Received power in dBW
Pr_dBm = Pr_dB + 30  # Convert to dBm

# Display results for part (b)
print('For (b)')
print('---------')
print(f'Electric Field, Er(d): {Er_d:.9f} V/m')
print(f'Effective Aperture, Ae: {Ae:.3f} m²')
print(f'Received power at 5 km distance Er(5 km): {Pr_dB:.2f} dBW')
print(f'Received power at 5 km distance Er(5 km): {Pr_dBm:.2f} dBm')