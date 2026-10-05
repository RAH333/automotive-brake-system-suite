"""
Simulates the Lumped Capacitance thermal dissipation transient behavior of a rotor during consecutive high-speed high-energy fade testing.
"""
import numpy as np

class RotorThermalModel:
    def __init__(self, rotor_mass, material_cp, surface_area):
        """
        Rotor mass (kg), Specific Heat cp (J/kg*K), Surface Area (m^2)
        """
        self.m = rotor_mass
        self.cp = material_cp
        self.A = surface_area

    def simulate_fade_test(self, initial_temp, kinetic_energy_per_stop, h_coeff, ambient_temp, num_stops, cycle_time):
        """Simulates temperature spikes and convective cooling over multiple cycles."""
        time_steps = np.arange(0, num_stops * cycle_time, 1)
        temp_profile = []
        current_temp = initial_temp

        for t in time_steps:
            # Heat input at the beginning of each cycle segment
            if t % cycle_time == 0:
                delta_T_gain = kinetic_energy_per_stop / (self.m * self.cp)
                current_temp += delta_T_gain
            
            # Convective cooling loop (dQ = h * A * (T - T_inf))
            cooling_loss = (h_coeff * self.A * (current_temp - ambient_temp)) / (self.m * self.cp)
            current_temp -= cooling_loss
            temp_profile.append(current_temp)
            
        return time_steps, temp_profile
      
