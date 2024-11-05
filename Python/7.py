import math

def calculate_path_loss(fc, hte, hre, d):
    # Calculate the correction factor for effective mobile antenna height
    a_hre = 3.2 * (math.log10(11.75 * hre)) ** 2 - 4.97

    # Calculate path loss using the Okumura-Hata model
    path_loss = (69.55 +
                 26.16 * math.log10(fc) -
                 13.82 * math.log10(hte) -
                 a_hre +
                 (44.9 - 6.55 * math.log10(hte)) * math.log10(d))
    
    return path_loss

# Input values
fc = 900  # Frequency in MHz
hte = 100  # Base station height in meters
hre = 2    # Mobile station height in meters
d = 4      # Distance in kilometers

# Calculate path loss
path_loss = calculate_path_loss(fc, hte, hre, d)
print(f"The path loss is approximately {path_loss:.2f} dB.")



# Problem-7: Determine the path loss of a 900MHz cellular system in a large city from a 
# base station with the height of 100m and mobile station installed in a vehicle with antenna 
# height of 2m. The distance between mobile and base station is 4 km.