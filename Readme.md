# Vapours

*Predicting the stage of depression of the patient and inferring if he/she fels suicidal or not.*

## Installation

1. Clone the repo.
2. Change directory to repo.

```
pip install -r requirements.txt
```

## How to run

```
python3 manage.py runserver
```

```
.
.
.
.
  "10 in version 0.20 to 100 in 0.22.", FutureWarning)
/home/zanark/CODING/DTU/Vapors/Vapors_app/phq_pred.py:48: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples,), for example using ravel().
  rfc6.fit(phq6_df_train[["PHQ6A","PHQ6B", "PHQ6C", "PHQ6D"]], phq6_df_train[["PHQ6"]])
/home/zanark/.local/lib/python3.6/site-packages/sklearn/ensemble/forest.py:246: FutureWarning: The default value of n_estimators will change from 10 in version 0.20 to 100 in 0.22.
  "10 in version 0.20 to 100 in 0.22.", FutureWarning)
/home/zanark/CODING/DTU/Vapors/Vapors_app/phq_pred.py:50: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples,), for example using ravel().
  rfc7.fit(phq7_df_train[["PHQ7A","PHQ7B", "PHQ7C", "PHQ7D"]], phq7_df_train[["PHQ7"]])
System check identified no issues (0 silenced).
April 03, 2019 - 14:09:54
Django version 2.1.5, using settings 'Vapors.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
Performing system checks...


```

Visit &nbsp;&nbsp;&nbsp; ` http://127.0.0.1:8000/ `  &nbsp;&nbsp; to access the web application on local server.