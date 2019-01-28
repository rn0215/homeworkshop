## 1.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>ssafy</title>
</head>
<body>
    <style>
        #ssafy > p:nth-child(2){
            color:red;
        }
        #ssafy > p:nth-of-type(2){
            color:blue;
        }     

    </style>
    <div id="ssafy">
        <h2>어떻게선택될까?</h2>
        <p>첫번째</p>
        <p>두번째</p>
        <p>세번째</p>
        <p>네번째</p>

    </div>
    
</body>
</html>
```

차이점 - nth-child는 자식중에서 2번째 색깔을 바꾸고 nth-of-type는 같은타입중에서 2번째를 바꾼다