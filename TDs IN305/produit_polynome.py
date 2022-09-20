poly1 = [1,2,1]
entier_lambda = 3
for i in range(len(poly1)):
    poly1[i] *= entier_lambda
print(poly1)

poly1 = [1,2,1]
poly2 = [3,1,5,1]
if poly1 < poly2: #Pour que poly 1 soit toujours supérieur ou égal à poly 2
    poly1,poly2 = poly2,poly1
for i in range(len(poly1)):
    poly1[i] *= poly2[i]
print(poly1)