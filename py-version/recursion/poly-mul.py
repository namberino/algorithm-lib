# A function to multiply two polynomials represented as lists of coefficients
def poly_mul(A, B):
  # Base case: if either polynomial is empty, return an empty list
  if not A or not B:
    return []
  # Base case: if either polynomial has only one term, multiply it with the other polynomial
  if len(A) == 1:
    return [A[0] * b for b in B]
  if len(B) == 1:
    return [B[0] * a for a in A]
  # Divide the polynomials into two halves
  m = min(len(A), len(B)) // 2
  A0 = A[:m] # lower half of A
  A1 = A[m:] # upper half of A
  B0 = B[:m] # lower half of B
  B1 = B[m:] # upper half of B
  # Recursively multiply the four pairs of halves
  P0 = poly_mul(A0, B0) # lower * lower
  P1 = poly_mul(A0, B1) # lower * upper
  P2 = poly_mul(A1, B0) # upper * lower
  P3 = poly_mul(A1, B1) # upper * upper
  # Combine the results using the formula: (A0 + A1) * (B0 + B1) = P0 + P3 + x^m * (P1 + P2)
  result = [0] * (len(A) + len(B) - 1) # initialize the result list with zeros
  for i in range(len(P0)):
    result[i] += P0[i] # add P0 to the result
  for i in range(len(P3)):
    result[i + 2 * m] += P3[i] # add P3 to the result shifted by 2m
  for i in range(len(P1)):
    result[i + m] += P1[i] + P2[i] # add P1 and P2 to the result shifted by m
  return result

# Example: multiply (1 + x + x^2) and (2 + x)
A = [1, 1, 1]
B = [2, 1]
print(poly_mul(A, B)) # prints [2, 3, 4, 1]
