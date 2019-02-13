## homework21

### 1.

```
    {% for comment in question.comment_set.all %}
        <h4>{{comment.content}}</h4>
    {% endfor %}
```

### 2.

```
"/questions/{{question.id}}/comments/create/"
```

