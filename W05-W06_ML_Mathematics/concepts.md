# Mathematics for Machine Learning — Concepts

## 1. Vectors

A vector is an ordered collection of numbers that can represent a point, direction, or set of features.

Example:

v = [2, 3]

Vectors are commonly used in machine learning to represent features of a data point.

### Important operations

- Vector addition
- Vector subtraction
- Scalar multiplication
- Magnitude
- Dot product

---

## 2. Matrices

A matrix is a rectangular arrangement of numbers organized into rows and columns.

Example:

A =

[1  2]
[3  4]

Matrices are important in machine learning because datasets, transformations, and neural-network parameters can be represented using matrices.

### Matrix operations

- Addition
- Multiplication
- Matrix-vector multiplication

---

## 3. Dot Product

The dot product combines two vectors into a single scalar value.

For:

a = [a₁, a₂]

b = [b₁, b₂]

The dot product is:

a · b = a₁b₁ + a₂b₂

In machine learning, dot products are used extensively in linear models and neural-network computations.

---

## 4. Eigenvalues and Eigenvectors

For a matrix A, an eigenvector is a vector whose direction remains unchanged when transformed by A.

The relationship is:

Av = λv

where:

- A = matrix
- v = eigenvector
- λ = eigenvalue

### Intuition

The eigenvalue tells us how much the eigenvector is scaled by the transformation.

Eigenvalues and eigenvectors are useful for understanding transformations, dimensionality reduction, and the structure of matrices.

---

# Calculus

## 5. Derivatives

A derivative describes how quickly a function changes with respect to its input.

For:

f(x) = x²

the derivative is:

f'(x) = 2x

Derivatives are fundamental to optimization because they tell us how changing an input affects the output.

---

## 6. Gradients

A gradient extends the idea of a derivative to functions with multiple variables.

For:

f(x, y) = x² + y²

the gradient is:

∇f = [2x, 2y]

The gradient points in the direction of the steepest increase of a function.

In machine learning, gradients indicate how model parameters should change to reduce the loss.

---

## 7. Chain Rule

The chain rule is used to differentiate a composition of functions.

If:

y = f(g(x))

then:

dy/dx = (dy/dg) × (dg/dx)

### Example

For:

y = (2x + 1)²

Let:

u = 2x + 1

Then:

dy/du = 2u

du/dx = 2

Therefore:

dy/dx = (2u)(2)

The chain rule is especially important in neural networks because a network consists of multiple connected functions.

---

## 8. Gradient Descent

Gradient descent is an optimization algorithm used to minimize a function.

The basic update rule is:

x_new = x - α∇f(x)

where:

- x = current parameter
- α = learning rate
- ∇f(x) = gradient

The gradient points toward increasing values, so subtracting it moves the parameter toward lower values.

---

## 9. Connection to Backpropagation

Backpropagation calculates how much each parameter in a neural network contributes to the final error.

The basic process is:

1. The model produces a prediction.
2. The prediction is compared with the target.
3. A loss is calculated.
4. Gradients are calculated using the chain rule.
5. The gradients are passed backward through the network.
6. Gradient descent updates the model parameters.

### Key idea

**Chain rule → gradients → parameter updates**

This is the mathematical intuition behind training neural networks.