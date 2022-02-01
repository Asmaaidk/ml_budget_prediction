import pickle
import pandas as pd
import numpy as np
# pip install streamlit
import streamlit as st

#--------------------------#

# Get the models
filename = 'saudi_projects_regression.pkl'
loaded_model = pickle.load(open(filename, 'rb'))

filename_c = 'saudi_projects_classification.pkl'
loaded_model_c = pickle.load(open(filename_c, 'rb'))

#--------------------------#
# Creating the Titles and Image
st.title("Predict project budget")
st.header("Calculating the budget based on input attributes")


#--------------------------#
# User inputs
df_s = pd.DataFrame({'sectors': [ 'Charity', 'Commercial', 'Educational', 'Governmental',
        'Health', 'Industrial', 'Residential', 'Scientific', 'Sports',
        'Tourist']}) 
df_r = pd.DataFrame({'region': ['ABHA', 'AD DIRIYAH', 'AL-JUBAIL', 'ALBAHA', 'ALDAMMAM',
        'ALDHAHRAN', 'ALGHAZALA', 'ALHASSA', 'ALHENAKIYA', 'ALJAZAN',
        'ALJAZAN, ALSHAQEEQ', 'ALJUBAIL', 'ALJUMUM', 'ALKAMIL', 'ALKHAFJI',
        'ALKHARJ', 'ALKHOBAR', 'ALQASEEM, MECCA', 'ALTAIF', 'ALULA',
        'ARAR',
        'ARAR, RIYADH, BURAYDAH, HAIL, ALMUJMAA, SDAIR, JAWF, EASTERN PROVINCE',
        'ARRASS', 'ASEER, KAHMIS MUSHAIT', 'BADR', 'BALJURASHI', 'BRAIDAH',
        'Dumah Al Jandal', 'EASTERN PROVINCE', 'FEIFAA', 'HAFAR ALBATIN',
        'HAIL', 'JAZAN', 'JEDDAH', 'JEDDAH, MECCA',
        'JEDDAH, RIYADH, ALDAMAM, MUHAYIL ASEER, MECCA',
        'KING ABDULLAH CITY', 'LAYLA', 'MADENAH',
        'MADENAH, RIYADH, EASTERN PROVINCE', 'MECCA',
        'MECCA, ALMUZAHMIYA, ALJMUM, ALBARABIR, RIYADH, JEDDAH',
        'MECCA, KING ABDULLAH CITY, MEDINA, JEDDAH', 'MECCA, TAIF',
        'MEDINA', 'NAJRAN', 'RABIGH', 'RAS ALKHAIR', 'RIYADH', 'SAKAKA',
        'SDAIR', 'SHAQRA', 'TABUK', 'TABUK, DHUBA', 'TUBARJAL', 'TURAIF',
        'UNAYZAH', 'WAAD ALSHAMAL', 'YANBAA']})
df_st = pd.DataFrame({'status': ['Announced', 'Canceled', 'Complete', 'Late', 'Stumbled',
        'Suggested projects', 'Under the construction']})

#--------------------------#

# Take the users input
sector = st.selectbox("Select a Sector", df_s['sectors'].unique())
region = st.selectbox("Select the Region", df_r['region'].unique())
status = st.selectbox("What is the project status?", df_st['status'].unique())
area = st.slider("What is the project Area in squered kilo meter?", 1, 13750)

#--------------------------#
# create dictonary to convert the text input to numeric to get back predictions from backend model.
# sectors
s = {'Charity': 0, 'Commercial': 1, 'Educational': 2, 'Governmental' : 3,'Health': 4, 'Industrial': 5, 'Residential' : 6,
     'Scientific': 7, 'Sports' : 8,'Tourist' : 9}
# sector_budget
sb = {'Charity': 473524096855, 'Commercial': 1058790791316, 'Educational': 567443636867, 'Governmental' : 1436611825301,
      'Health': 549859453510, 'Industrial': 1091256760152, 'Residential' : 709916354518,
     'Scientific': 403038920637, 'Sports' : 396629702256,'Tourist' : 672120928423}
# project_type
pt = {'Charity': 0, 'Commercial': 3, 'Educational': 16, 'Governmental' : 26,'Health': 37, 'Industrial': 57, 'Residential' : 82,
     'Scientific': 83, 'Sports' : 84,'Tourist' : 85}
# region
r = {'ABHA': 0, 'AD DIRIYAH': 1, 'AL-JUBAIL': 2, 'ALBAHA': 3, 'ALDAMMAM': 4,
        'ALDHAHRAN': 5, 'ALGHAZALA': 6, 'ALHASSA': 7, 'ALHENAKIYA': 8, 'ALJAZAN': 9,
        'ALJAZAN, ALSHAQEEQ': 10, 'ALJUBAIL': 11, 'ALJUMUM': 12, 'ALKAMIL': 13, 'ALKHAFJI': 14,
        'ALKHARJ': 15, 'ALKHOBAR': 16, 'ALQASEEM, MECCA': 16, 'ALTAIF': 17, 'ALULA': 18,
        'ARAR': 19,
        'ARAR, RIYADH, BURAYDAH, HAIL, ALMUJMAA, SDAIR, JAWF, EASTERN PROVINCE': 20,
        'ARRASS': 21, 'ASEER, KAHMIS MUSHAIT': 22, 'BADR': 23, 'BALJURASHI': 24, 'BRAIDAH': 25,
        'Dumah Al Jandal': 26, 'EASTERN PROVINCE': 27, 'FEIFAA': 28, 'HAFAR ALBATIN': 29,
        'HAIL': 30, 'JAZAN':31, 'JEDDAH': 32, 'JEDDAH, MECCA': 33,
        'JEDDAH, RIYADH, ALDAMAM, MUHAYIL ASEER, MECCA': 34,
        'KING ABDULLAH CITY': 35, 'LAYLA' : 36, 'MADENAH': 37,
        'MADENAH, RIYADH, EASTERN PROVINCE': 38, 'MECCA': 39,
        'MECCA, ALMUZAHMIYA, ALJMUM, ALBARABIR, RIYADH, JEDDAH': 40 ,
        'MECCA, KING ABDULLAH CITY, MEDINA, JEDDAH': 41, 'MECCA, TAIF': 42,
        'MEDINA': 43, 'NAJRAN': 44, 'RABIGH': 45, 'RAS ALKHAIR': 46, 'RIYADH': 47, 'SAKAKA':48,
        'SDAIR': 49, 'SHAQRA': 50, 'TABUK': 51, 'TABUK, DHUBA': 52, 'TUBARJAL': 53, 'TURAIF': 54,
        'UNAYZAH':55, 'WAAD ALSHAMAL':56, 'YANBAA': 57}
# status
ss = {'Announced':0, 'Canceled':1, 'Complete':2, 'Late': 3, 'Stumbled': 4,
        'Suggested projects': 5, 'Under the construction': 6}

# save the numeric values to get back predictions from backend model.
p_sector = s.get(sector)
p_sbuget = sb.get(sector)
p_type =  pt.get(sector)
p_region = r.get(region)
p_status = ss.get(status) 
p_area = area*1000000

#--------------------------#

# store the inputs
features = [p_sector, p_sbuget, p_type, p_area , p_region, p_status]

# convert user inputs into an array fr the model
final_features = [np.array(features)]

# Get prediction from the models
if st.button('Predict'):           # when the submit button is pressed
    # Reggresion model
    prediction =  loaded_model.predict(final_features)
    st.success(f'The project budget would be: ${round(prediction[0],2)}')
    # Classification model
    prediction_c = loaded_model_c.predict(final_features)
    d = {0 : 'low', 1 : 'medium', 2 : 'high'}
    preds = d.get(prediction_c[0])
    st.success(f'The project budget would be: {preds}')
    
# To run the app we use the terminal 'streamlit run project_app.py'
# All the files must be in the same directry
