"""
The orchestration entry point that executes simulations, processes calculations, and saves visual performance charts.
"""
import os
import matplotlib.pyplot as plt
from src.vehicle_dynamics import BrakeDynamicsSolver
from src.thermal_analysis import RotorThermalModel
from src.tolerance_stack import ToleranceStackAnalyzer

def main():
    print("--- Executing Brake System Engineering Verification ---")
    
    # 1. Vehicle Dynamics Run
    solver = BrakeDynamicsSolver(vehicle_mass=1800, wheelbase=2.75, cg_height=0.55, front_ratio_static=0.6)
    f_force, r_force = solver.ideal_braking_curve()
    
    # 2. Thermal Analysis Simulation
    rotor = RotorThermalModel(rotor_mass=8.5, material_cp=460, surface_area=0.12)
    time, temps = rotor.simulate_fade_test(initial_temp=25, kinetic_energy_per_stop=120000, 
                                           h_coeff=45, ambient_temp=25, num_stops=5, cycle_time=45)
    
    # 3. Stack-up Clearance Analysis
    # Vector components: Bracket thickness, Caliper clearance, Pad backplate
    stack = ToleranceStackAnalyzer(dimensions=[25.0, 4.5, -5.0], tolerances=[0.05, 0.1, 0.08])
    nom, wc_bounds = stack.compute_worst_case()
    _, rss_bounds = stack.compute_rss()

    print(f"Clearance Nominal: {nom:.3f} mm")
    print(f"Worst-Case Gap Range: {wc_bounds[0]:.3f} to {wc_bounds[1]:.3f} mm")
    print(f"Statistical RSS Gap Range: {rss_bounds[0]:.3f} to {rss_bounds[1]:.3f} mm")

    # Generate Performance Plot Dashboards
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.plot(f_force, r_force, 'g-', label='Ideal Adhesion Allocation Curve')
    plt.xlabel('Front Brake Braking Force (N)')
    plt.ylabel('Rear Brake Braking Force (N)')
    plt.grid(True)
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.plot(time, temps, 'r-', label='Rotor Fade Cycle (Temp)')
    plt.xlabel('Elapsed Testing Time (s)')
    plt.ylabel('Disc Temperature (°C)')
    plt.grid(True)
    plt.legend()
    
    plt.tight_layout()
    os.makedirs('outputs', exist_ok=True)
    plt.savefig('outputs/performance_metrics.png')
    print("Verification metrics successfully saved to outputs/performance_metrics.png")

if __name__ == '__main__':
    main()
  
