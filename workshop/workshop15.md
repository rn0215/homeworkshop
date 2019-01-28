## workshop 15

### 1.

```sql
CREATE TABLE bands(id INTEGER,name TEXT,debut INTEGER);

```

```sql
INSERT INTO bands VALUES(1,'Queen',1973);
INSERT INTO bands VALUES(2,'Coldplay',1998);
INSERT INTO bands VALUES(3,'MCR',2001);
```



## 2.

```sql
SELECT id,name FROM bands;
```



## 3.

```sql
SELECT * FROM bands WHERE debut<=2000;
```

