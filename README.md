Scramble Solver
===============

## Rules

1. No square may be used more than once.
2. Connected squares must be neighbors.
3. Connected squares must form a real word.

![Neighbors](http://img40.imageshack.us/img40/8409/neighbors.png)

## Searching

Searching should be done using a breadth-first algorithm. For example:

![(0,0)](http://img94.imageshack.us/img94/5025/83315660.png)

```python
parent = None
n = (0,0)
queue = [
    ((0,0),(1,0)),
    ((0,0),(0,1)),
    ((0,0),(1,1))]
```

![(0,0)->(1,0)](http://img407.imageshack.us/img407/7328/0010ek.png)

```python
parent = (0,0)
n = (1,0)
queue = [
    ((0,0),(0,1)),
    ((0,0),(1,1)),
    ((1,0),(2,0)),
    ((1,0),(0,1)),
    ((1,0),(1,1)),
    ((1,0),(1,2))]
```

![(0,0)->(0,1)](http://img195.imageshack.us/img195/6126/0001gm.png)

```python
parent = (0,0)
n = (0,1)
queue = [
    ((0,0),(1,1)),
    ((1,0),(2,0)),
    ((1,0),(0,1)),
    ((1,0),(1,1)),
    ((1,0),(1,2)),
    ((0,1),(1,0)),
    ((0,1),(1,1)),
    ((0,1),(0,2)),
    ((0,1),(1,2))]
```

## Screenshot

![Scaled Screenshot](http://dumpon.us/media/uploads/scaled_screenshot.png)
