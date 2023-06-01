# Código na shell do Python

Código desenvolvido utilizando a shell do Python sobre datetime

```python
python -m venv venv

# Windows
.\venv\Scripts\activate
#Linus e Mac
source venv/bin/activate

pip install ipython

deactivate

pip freeze > requirements.txt

pip install -r requirements.txt

#datetime
from datetime import datetime as dt
x_date = dt.now()
type(x_date)
# <class 'datetime.datetime'>
x_date
# datetime.datetime(2022, 11, 22, 10, 18, 19, 159104)
x_date.minute
# 18
x_date.year
# 2022
x_date.day
# 22
x_date.timestamp()
# 1669123099.159104
y_date = dt.now()
y_date
# datetime.datetime(2022, 11, 22, 10, 20, 22, 160133)
interval = y_date - x_date
interval
# datetime.timedelta(seconds=123, microseconds=1029)
type(interval)
# <class 'datetime.timedelta'>
interval.total_seconds()
# 123.001029
x_str_date = x_date.strftime("%d/%m/%Y")
x_str_date
# '22/11/2022'
x_str_date = x_date.strftime("%d-%m-%Y")
x_str_date
# '22-11-2022'
y_str_date = '03/03/93'
y_obj_date = dt.strptime(y_str_date, "%d/%m/%y")
y_obj_date
# datetime.datetime(1993, 3, 3, 0, 0)
x_date
# datetime.datetime(2022, 11, 22, 10, 18, 19, 159104)
x_date - y_obj_date
# datetime.timedelta(days=10856, seconds=37099, microseconds=159104)
y_obj_date = dt.strptime(y_str_date, "%d-%m-%y")
# ValueError: time data '03/03/93' does not match format '%d-%m-%y'
```
