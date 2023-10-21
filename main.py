from scipy.optimize import linprog

target = [3000, 4000]

inequalities = [[-1, -1],
                [-0.3, -0.6],
                [0.2, 0.3]]

inequalities_right = [-350,
                      -150,
                      90]

var_boundaries = [(0, float("inf")),  # Bounds of x
                  (0, float("inf"))]  # Bounds of y

opt = linprog(c=target, A_ub=inequalities, b_ub=inequalities_right, bounds=var_boundaries, method="revised simplex")
print(opt)