# Phase 1, Lesson 1: Linear Algebra Intuition, Build it, step 1.
# Vector class from the lesson, written from scratch (no libraries).


class Vector:
    def __init__(self, components):
        self.components = list(components)
        self.dim = len(self.components)

    def __add__(self, other):
        return Vector([a + b for a, b in zip(self.components, other.components)])

    def dot(self, other):
        return sum(a * b for a, b in zip(self.components, other.components))

    def magnitude(self):
        return sum(x**2 for x in self.components) ** 0.5

    def cosine_similarity(self, other):
        return self.dot(other) / (self.magnitude() * other.magnitude())

    def __repr__(self):
        return f"Vector({self.components})"


A = Vector([5, 1])
B = Vector([4, 0])
C = Vector([0, 5])
B_loud = Vector([8, 0])

print(f"A . B = {A.dot(B)}")
print(f"A . C = {A.dot(C)}")
print(f"B . C = {B.dot(C)}")
print(f"cos(A, B)      = {A.cosine_similarity(B):.4f}")
print(f"cos(A, C)      = {A.cosine_similarity(C):.4f}")
print(f"cos(A, B_loud) = {A.cosine_similarity(B_loud):.4f}")
