`front_cmp = (n//10**(num_digits-(i+1)))%10`
have to take the %10 because otherwise, if n = 39993, in the second round of the loop when `i` is 1, the part of the expression that reads `n//10**(num_digits-(i+1)` will return 39, and we need to `%` by 10 in order to pull off just that inner 9.
