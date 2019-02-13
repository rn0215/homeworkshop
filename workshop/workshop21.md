# workshop21

## 

### 1.

```python
from django.db import models
# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=100)
  
    def __str__(self):
        return self.title
        
class Choice(models.Model):
    #어떤정보를 가져올지 (부모역할): on_delete=models.CASCADE
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    votes = modelf.IntegerField()
    
    def __str__(self):
        return self.content
```



#### html

```html
{% extends "question/base.html" %}

{% block bb %}
<h1>{{question.title}}</h1>
    {% for choice in question.choice_set.all %}
        <h4>{{choice.votes}}</h4>
    {% endfor %}
{% endblock %}
```



