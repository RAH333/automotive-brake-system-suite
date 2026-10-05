"""
Performs 1D statistical and Worst-Case tolerance stack-ups for critical interfaces (e.g., caliper piston travel clearances / pad alignment).
"""
import numpy as np

class ToleranceStackAnalyzer:
    def __init__(self, dimensions, tolerances):
        """
        Accepts lists of nominal dimensions and corresponding symmetric tolerances.
        """
        self.dims = np.array(dimensions)
        self.tols = np.array(tolerances)

    def compute_worst_case(self):
        """Calculates absolute extreme absolute limits."""
        nominal_sum = np.sum(self.dims)
        worst_case_tol = np.sum(np.abs(self.tols))
        return nominal_sum, (nominal_sum - worst_case_tol, nominal_sum + worst_case_tol)

    def compute_rss(self):
        """Calculates statistical Root-Sum-Square (RSS) limits (3-Sigma standard)."""
        nominal_sum = np.sum(self.dims)
        rss_tol = np.sqrt(np.sum(self.tols ** 2))
        return nominal_sum, (nominal_sum - rss_tol, nominal_sum + rss_tol)
      
