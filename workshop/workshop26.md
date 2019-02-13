## workshop26

### 1.

```python
class StudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
```

### 2.

```python
def new(request):
    form =StudentForm()
    return render(request, "new.html", {'form':form})
```



```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <form method='post'>
		{% csrf_token %}
        {{form}}
        <input type="submit" value="Submit"/>
    </form>
    
    
</body>
</html>
```



