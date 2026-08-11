import numpy as np


print("=" * 60)
print("   MATHEMATICS FOR MACHINE LEARNING")
print("   HACK-O-WEEK | W05-W06")
print("=" * 60)


# ============================================================
# 1. VECTORS
# ============================================================

print("\n1. VECTORS")

v1 = np.array([2, 3])
v2 = np.array([4, 1])

print("Vector v1:", v1)
print("Vector v2:", v2)

print("Vector addition:", v1 + v2)
print("Vector subtraction:", v1 - v2)

magnitude = np.linalg.norm(v1)
print("Magnitude of v1:", round(magnitude, 2))


# ============================================================
# 2. DOT PRODUCT
# ============================================================

print("\n2. DOT PRODUCT")

dot_product = np.dot(v1, v2)

print("v1 · v2 =", dot_product)
print("Dot product measures the relationship between two vectors.")


# ============================================================
# 3. MATRICES
# ============================================================

print("\n3. MATRICES")

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nA + B:")
print(A + B)

print("\nA × B:")
print(A @ B)

print("\nMatrix-vector multiplication:")
print(A @ v1)


# ============================================================
# 4. EIGENVALUES AND EIGENVECTORS
# ============================================================

print("\n4. EIGENVALUES AND EIGENVECTORS")

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:")
print(np.round(eigenvalues, 2))

print("\nEigenvectors:")
print(np.round(eigenvectors, 2))

print("\nIntuition:")
print("An eigenvector keeps its direction after a matrix transformation.")
print("The eigenvalue represents how much that direction is scaled.")


# ============================================================
# 5. DERIVATIVE
# ============================================================

print("\n5. DERIVATIVE")

# f(x) = x²
# f'(x) = 2x

x = 3
derivative = 2 * x

print("Function: f(x) = x²")
print("At x =", x)
print("Derivative f'(x) =", derivative)


# Numerical derivative using finite difference

def function(x):
    return x ** 2


x = 3
h = 0.0001

numerical_derivative = (
    function(x + h) - function(x)
) / h

print("Numerical derivative:", round(numerical_derivative, 4))


# ============================================================
# 6. GRADIENT
# ============================================================

print("\n6. GRADIENT")

# f(x, y) = x² + y²
#
# ∂f/∂x = 2x
# ∂f/∂y = 2y

x = 2
y = 3

gradient = np.array([
    2 * x,
    2 * y
])

print("Function: f(x, y) = x² + y²")
print("Point: (2, 3)")
print("Gradient:", gradient)

print("The gradient points in the direction of steepest increase.")


# ============================================================
# 7. CHAIN RULE
# ============================================================

print("\n7. CHAIN RULE")

# y = (2x + 1)²
#
# Let u = 2x + 1
#
# dy/du = 2u
# du/dx = 2
#
# dy/dx = (dy/du) × (du/dx)

x = 2
u = 2 * x + 1

dy_du = 2 * u
du_dx = 2

chain_rule_result = dy_du * du_dx

print("Function: y = (2x + 1)²")
print("x =", x)
print("u = 2x + 1 =", u)
print("dy/du =", dy_du)
print("du/dx =", du_dx)
print("dy/dx =", chain_rule_result)


# ============================================================
# 8. GRADIENT DESCENT
# ============================================================

print("\n8. GRADIENT DESCENT")

# Minimize:
# f(x) = x²
#
# Gradient:
# f'(x) = 2x
#
# Update rule:
# x_new = x - learning_rate × gradient

x = 5.0
learning_rate = 0.1

print("Starting x:", x)

for step in range(5):

    gradient = 2 * x

    x = x - learning_rate * gradient

    print(
        f"Step {step + 1}: "
        f"gradient = {gradient:.4f}, "
        f"x = {x:.4f}"
    )


# ============================================================
# 9. BACKPROPAGATION INTUITION
# ============================================================

print("\n9. BACKPROPAGATION INTUITION")

print("1. A model makes a prediction.")
print("2. The prediction is compared with the actual value.")
print("3. A loss/error is calculated.")
print("4. Gradients show how parameters affect the loss.")
print("5. The chain rule calculates gradients through layers.")
print("6. Parameters are updated using gradient descent.")


# ============================================================
# SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("✓ Vectors and vector operations")
print("✓ Dot product")
print("✓ Matrix operations")
print("✓ Eigenvalues and eigenvectors")
print("✓ Derivatives")
print("✓ Gradients")
print("✓ Chain rule")
print("✓ Gradient descent")
print("✓ Backpropagation intuition")

print("\nW05-W06 Mathematics for Machine Learning completed.")