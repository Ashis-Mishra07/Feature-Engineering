# Confusion Matrix
'''

It is a nxn matrix , where n represent the number of classes in the dataset.
The  x-axis will be prediction outcome and y-axis will be the actual outcome.
It is used to evaluate the performance of the model.

                     Prediction
                    positive          Negative

      positive         TP                FN

Actual    

      Negative         FP                TN


Now for every value it will count how many are TP , FN ... and fill the matrix , this is 
confusion matrix .

      
'''

# how the model is used for findings

# Accuracy
'''

It is the ratio of correct predicted values over the total predicted values .

Accuracy = Correct Prediction / Total Predictions
Accuracy = (TP + TN) / (TP + TN + FP + FN)
 

For any larger value of TP or TN , it will predict higher value .

So this model is not that much efficient .



Rather we will use

TPR = TP / (TP + FN)  # True Positive Rate
FNR = FN / (FN + TP)  # False Negative Rate


FPR = FP / (FP + TN)  # False Positive Rate
TNR = TN / (TN + FP)  # True Negative Rate


Higher the TPR value and lower the FNR value will be great
Higher the TNR value and lower the FPR value will be great


'''

# Precision
'''

precision = Predictions Actaully Positive / Total Predicted Positive
precision = TP / (TP + FP)


In precision avoiding False Positive is more important than avoiding False Negative .

'''

# Recall
'''

Recall = Predictions Actually Positive / Total Actual Positive
Recall = TP / (TP + FN)


In recall and precison there is actually a trade off , if we increase the recall then the precision will decrease and vice versa .
 

And F1 Score combine these both 

F1 Score = 2 * (Precision * Recall) / (Precision + Recall)
F1 Score = 2 * (1 / (1/Precision + 1/Recall))

F1 is maximum when Precision = Recall


'''


# AUC and ROC  Curve 

'''

AUC -> Area Under the Curve
ROC -> Receiver Operating Characteristic

Originally ROC is used for distinguishing the signal from the noise in the radar signals .
Used to evaluate the performance of the binary classification model .
Gives trade-off between True Positive Rate and False Positive Rate .

ROC Curve is plotted between TPR and FPR .



More the AUC , better is the model .

'''

# Log Loss
'''

Log Loss is used to evaluate the performance of the classification model where the output is 
the probability value between 0 and 1 .

Problem with AUC and ROC is 
Considers only the order of probabilty therefore cant used to compare two models .


Log Loss is the negative average of the log of corrected predicted probabilities for each instance .


'''

# MAE and MSE
'''
Done by regression 
Mean Absolute Error and Mean Squared Error
root mean square error and root mean square log error 
r - squared
adjusted r - squared



Relative square error = MSE(model) / MSE(baseline model) 

if the value is 1 , then the model is as good as the baseline model
ideally the value lies between 0 and 1
if the value is greater than 1 , then the model is worse than the baseline model .


R^2 = 1 - (MSE(model) / MSE(baseline model))
Better the model higher is the R^2 value .




'''












