## workshop06

### 1.

```
def my_sqrt(n):
                                 
    left = 1
    right = n
    answer = 0
                                 
    while abs(answer**2 - n) > 0.00001:
                                 
        answer = (left + right) / 2                           
        if answer**2 < n:
        	left = answer
        else:
            right = answer
    return answer
        

```

```
my_sqrt(2)
1.414215087890625
```



