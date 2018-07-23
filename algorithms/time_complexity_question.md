## Time Complexity Question

What is the time complexity of the code snippet below?

```
int j = 0;
for(i = 0; i < n; ++i) {
    while(j < n && arr[i] < arr[j]) {
        j++;
    }
}
```

The time complexity might appear at first glance to be O(*n*^2), or dependent on the size and/or values of the array `arr`.  However, since `j` is never reset, the inner loop only runs once; the outer loop runs the next *n*-1 iterations but executes nothing inside these iterations.
