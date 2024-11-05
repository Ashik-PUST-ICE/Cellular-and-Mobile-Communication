import math

def calculate_path_loss(fc, hb):
    # Calculate the T-R separation distance in kilometers
    d_km = math.sqrt(20**2 + 30**2) / 1000  # Convert meters to kilometers

    # Calculate path loss using the Okumura-Hata model
    path_loss = (135.41 +
                 12.49 * math.log10(fc) -
                 4.99 * math.log10(hb) +
                 (46.84 - 2.34 * math.log10(hb)) * math.log10(d_km))
    
    return path_loss

# Given values
fc = 1.8  # Frequency in GHz
hb = 20   # Base station height in meters

# Calculate path loss
path_loss = calculate_path_loss(fc, hb)
print(f"The path loss is approximately {path_loss:.2f} dB.")
