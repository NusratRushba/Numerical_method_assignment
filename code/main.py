from interpolation_setup import x, y, x_fine, y_spline, y_lagrange
from plot_results import plot_interpolations

if __name__ == "__main__":
    plot_interpolations(x, y, x_fine, y_spline, y_lagrange)
