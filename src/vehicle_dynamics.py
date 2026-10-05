"""
This module performs fundamental system-level sizing calculations, front/rear dynamic braking force distribution, and stops-to-rest kinematics.
"""
import numpy as np

class BrakeDynamicsSolver:
    def __init__(self, vehicle_mass, wheelbase, cg_height, front_ratio_static):
        """
        Initializes vehicle parameters for longitudinal dynamics.
        Mass (kg), Wheelbase (m), CG Height (m), Static distribution (0-1)
        """
        self.m = vehicle_mass
        self.L = wheelbase
        self.h = cg_height
        self.f_static = front_ratio_static
        self.g = 9.81

    def calculate_dynamic_loads(self, deceleration_g):
        """Calculates load transfer during deceleration."""
        ax = deceleration_g * self.g
        load_transfer = (self.m * ax * self.h) / self.L
        
        front_load_static = self.m * self.g * (1 - self.f_static) # Simplified static distribution assumption
        # Accurate calculation based on weight distribution:
        front_load = (self.m * self.g * (1 - self.f_static)) + load_transfer
        rear_load = (self.m * self.g * self.f_static) - load_transfer
        return front_load, rear_load

    def ideal_braking_curve(self, max_mu=1.0):
        """Generates the ideal front vs rear adhesion utilization curve."""
        decelerations = np.linspace(0.1, max_mu, 50)
        front_pressures = []
        rear_pressures = []
        
        for decel in decelerations:
            f_load, r_load = self.calculate_dynamic_loads(decel)
            front_pressures.append(f_load * decel)
            rear_pressures.append(r_load * decel)
            
        return np.array(front_pressures), np.array(rear_pressures)
      
