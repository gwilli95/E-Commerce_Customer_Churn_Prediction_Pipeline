# Data science pipeline project Using open source data

Using uci data, build a model and generate prediction
 
## Data Used
[UCI Breast Cancer Dataset](https://archive.ics.uci.edu/dataset/14/breast+cancer)

## Model Used
Random Forest, implemted via Scikit-Learn

## Results
```
rain classification report:
               precision    recall  f1-score   support

           B       1.00      1.00      1.00       286
           M       1.00      1.00      1.00       169

    accuracy                           1.00       455
   macro avg       1.00      1.00      1.00       455
weighted avg       1.00      1.00      1.00       455

Test classification report:
               precision    recall  f1-score   support

           B       0.96      0.99      0.97        71
           M       0.98      0.93      0.95        43

    accuracy                           0.96       114
   macro avg       0.97      0.96      0.96       114
weighted avg       0.97      0.96      0.96       114
```

## Next Steps
- Import data differently
- Store results in folders
- Remove data from git
- Add src folder