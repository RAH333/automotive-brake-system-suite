"""
Ensures calculation integrity via automated continuous units regression tests.
"""
import pytest
from src.vehicle_dynamics import BrakeDynamicsSolver

def test_load_transfer_equilibrium():
    solver = BrakeDynamicsSolver(vehicle_mass=1500, wheelbase=2.5, cg_height=0.5, front_ratio_static=0.5)
    f_load, r_load = solver.calculate_dynamic_loads(deceleration_g=0.0)
    
    # At 0g deceleration, total load must equal static vehicle weight parameters exactly
    total_weight = 1500 * 9.81
    assert pytest.approx(f_load + r_load) == total_weight
  
