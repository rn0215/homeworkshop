## 1.

```sqlite
CREATE TABLE friends(
    id INTEGER.
    name TEXT,
    location TEXT
);
```

## 2.

```sqlite
INSERT INTO friends VALUES (1, "Justin", "Seoul");
INSERT INTO friends VALUES (2, "Simon", "New York");
INSERT INTO friends VALUES (3, "Chang", "Las Vegas");
INSERT INTO friends VALUES (4, "John", "Sydney");
```

## 3.

```sqlite
ALTER TABLE friends add column married INTEGER;
```

### 4.

```sqlite
UPDATE friends SET location="LA" WHERE id=1;
UPDATE firends SET location="LasVegas" WHERE id=2;
UPDATE friends SET married=1 WHERE id=1;
UPDATE friends SET married=0 WHERE id=2;
UPDATE friends SET married=0 WHERE id=3;
UPDATE friends SET married=1 WHERE id=4;
```

### 5.

```sqlite
DELETE friends WHERE married=0;
```

```sqlite
DROP TABLE friends
```

