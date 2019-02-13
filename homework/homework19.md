## homework19

### 1.

```
csrf 공격
```

### 2.

```
request.POST.get("title")
```

### 3.

```
{% extends "todo/base.html" %}

{% block bodyblock %}
    <form action="/todos/{{todo.id}}/update/" method="post">
        {% csrf_token %}
        <input type="text" name="title" value="{{todo.title}}"/>
        <input type="text" name="content" value="{{todo.content}}"/>
        <input type="date" name="due_date" value="{{todo.due_date|date:'Y-m-d'}}"/>
        <input type="submit" value="Submit"/>
    </form>
{% endblock %}
```

