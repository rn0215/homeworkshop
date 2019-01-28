## workshop05

```py
def palindrome(word):
    list_word = list(word) #"토마토" => ['토','마','토'] 
    for i in range(len(list_word)//2):
        if list_word[i] != list_word[-i-1]:
            return False
    return True
```

```
print(palindrome("wrlkjd"))
False
print(palindrome("lol"))
True
```

