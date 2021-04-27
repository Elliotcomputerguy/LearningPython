#!/usr/bin/env python

# Membership operators "in / not in" are operators used to validate the membership of a value. 
# It test for membership in a sequence, such as strings, lists, or tuples. 
# ===============================================================
# Example:

sneakers = ['Jordan', 'Nike', 'Yeezy', 'Adidas']
customerSneakerRequest = 'Zanotti'

for sneaker in sneakers:
    if customerSneakerRequest in sneakers:
        print(f'sneaker {customerSneakerRequest} is available')
    else:
        print(f'sneaker {customerSneakerRequest} is not available')

for sneaker in sneakers:
    if customerSneakerRequest not in sneakers:
        print(f'sneaker {customerSneakerRequest} is not available')
    else:
        print(f'sneaker {customerSneakerRequest} is available')

# ===============================================================
