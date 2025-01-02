# Algorithms to study radio emissions and stellar wind

import math

# 1. Ratio between cyclotron frequency and plasma frequency
def cyclotron_to_plasma_ratio(cyclotron_frequency, plasma_frequency):
    return cyclotron_frequency / plasma_frequency

# 2. Cyclotron frequency calculation
def cyclotron_frequency(electron_charge, magnetic_field, electron_mass):
    return (electron_charge * magnetic_field) / (2 * math.pi * electron_mass)

# 3. Plasma frequency calculation
def plasma_frequency(electron_density, electron_mass):
    epsilon_0 = 8.854e-12  # Permittivity of free space (F/m)
    return (electron_density * (electron_charge**2) / (electron_mass * epsilon_0))**0.5

# 4. Check if cyclotron mechanism is effective
def is_cyclotron_mechanism_effective(cyclotron_frequency, plasma_frequency):
    return cyclotron_frequency > plasma_frequency

# Constants for testing
electron_charge = 1.602e-19  # Elementary charge (C)
electron_mass = 9.109e-31    # Mass of an electron (kg)
magnetic_field = 1e-3        # Magnetic field strength (T)
electron_density = 1e6       # Electron density (m^-3)

# Example calculations
cyclotron_freq = cyclotron_frequency(electron_charge, magnetic_field, electron_mass)
plasma_freq = plasma_frequency(electron_density, electron_mass)
ratio = cyclotron_to_plasma_ratio(cyclotron_freq, plasma_freq)
effective = is_cyclotron_mechanism_effective(cyclotron_freq, plasma_freq)

print("Cyclotron Frequency:", cyclotron_freq)
print("Plasma Frequency:", plasma_freq)
print("Ratio:", ratio)
print("Is Cyclotron Mechanism Effective?", effective)
