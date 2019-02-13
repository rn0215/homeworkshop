## homework26

### 1.

```
from .forms import MovieForm
```

### 2.

```
{{ form.as_p }}
```

### 3.

```
def create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_date.get['name']
            age = form.cleaned_data.get['age']
```

