# Machine Learning Microservice Restful API
This is a implementation of a Machine Learning Microservice Restful API. The service provided is a age and gender 
time series prediction. The service takes an input of the last age and gender detected and predicts the ext sample.

## Input type
There are two input types which are the gender and age

### gender
```python
gender = ['male', 'female']
```
Therefore if male was detected it would be
```python
gender = [1,0]
```

### Age
age are grouped into 8 categories
```python
age = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
```
Therefore if the age was 5 it would be

```python
age = [0,1,0,0,0,0,0,0]
```

The input is gender + age

```python
gender = [1,0]
age = [0,1,0,0,0,0,0,0]
last = gender+age
```
## Making request

```python
import requests
import json

payload = json.dumps({'last': [1, 0, 1, 0, 0, 0, 0, 0, 0, 0]})
r = requests.post('http://127.0.0.1:5000/predict', json=payload)
data = json.loads(r.content)
print(data)
```


