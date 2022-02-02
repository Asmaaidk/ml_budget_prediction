# <p align="center"> SA Projects' Budgets Predictions</p>
#### <p align="center">Team: Techy Fighters</p>
###### <p align="center">Asmaa Alqurashi - Yousef Al-Mousa - Shoug Alsulami - Boshra Almaghthawi - Abdulmajeed Yaseen</p>
#### Capstone Project in Machine Learning to predict the budget of projects in Saudi Arabia  
In order to reach the 2030 vision on supporting the economy and reduce wastage or shortage of money and manpower, we decided to implement a through investigation and determine the prediction of the budgets for future projects so that everything is already known before the planning process which gives leeway and
flexibility to handling new ideas and its variations

---
### 📊 Dataset
[Saudi projects dataset](https://www.kaggle.com/ghadahaltwalah/saudi-projects-dataset) is maintained using web-scrapping from [Saudi projects](https://saudiprojects.net/) which is a media platform tracking projects and development in the Kingdom of Saudi Arabia.
The dataset features are:
- sectors
- sector budgets
- project name
- project type
- project area
- start date
- end date
- region
- status

The dataset was <b>translated</b>, <b>cleand</b>, <b>unified</b> and <b>analyzed</b>. And three columns were added from these data: <b>year</b>, <b>month</b> and <b>project duration</b>.

#### 📈 The Dashboard



---
### 💡 Models
After handling the missing data, scaling and encoding our train and test data we tried different models to get two different solution: regression and classification.

#### Regression
Regression predict the actual predicted budget and the following models were implemented: Linear Regression, Decision Tree Regressor, Random Forest Regressor, SVR, and XGB regressor.

#### Classification
Classification predict the range of the budget: High, Medium or Low and the following models were implemented: Decision Tree Classifier, Random Forest Classifier, SVC, and XGB Classifier.

---
### ✔️ Results
The result of regression and calcification models shown different results with different accuracy scores. But the best result has been with XGB Classifier models with training set accuracy of 96.0 % and testing set accuracy of 96.0% . The features were selected are sectors , sector_budgets , type_project , project_area, region_project ,and status_project. The project area has shown the most importance feature. According to cost function records, the best iteration predictions of mean budget absolute error was 212824308.35 above or below the actual price.

---
### 💻 Web App

<p align="center">
  <img src="https://user-images.githubusercontent.com/18037696/152024447-deab81db-2a03-4f4c-9a3f-d727d13b4061.gif">
</p>

This app was built useing *streamlit*.



---
### 🔎 Future Work
Looking for another resources of Saudi project and finding new features to increase the accuracy of the prediction.
