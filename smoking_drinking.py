# 4........................MODEL DEPLOYMENT AND MONITORING..........................

import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn
import pickle
from streamlit_option_menu import option_menu



# Load the pre-trained models
with open('Smoking_stats.pkl', 'rb') as smoking_model_file:
    smoking_model = pickle.load(smoking_model_file)

with open('Drinking_stats.pkl', 'rb') as drinking_model_file:
    drinking_model = pickle.load(drinking_model_file)

def main():
    # Create a menu to choose between smoking and drinking predictions
    menu = st.sidebar.selectbox("CHOOSE AN OPTION", ["Home", "Smoking Prediction", "Drinking Prediction"])
    
    if menu == "Home":
        st.sidebar.image('pngwing.com (24).png')
        st.markdown("<h1 style = 'top_margin: 0rem; text-align: centre; color: #557A46'>WELCOME TO SMOKING AND DRINKING PREDICTION APP</h1>", unsafe_allow_html= True)
        st.write("Please choose your menu options and follow guildlines thoroughly.")
        st.image('pngwing.com (23).png', width=700)
    


    elif menu == "Smoking Prediction":
        st.subheader("PREDICTING SMOKING STATUS")
        username = st.text_input('Enter your name')
        if st.button('submit name'):
            st.success(f"Welcome {username}. Pls use according to usage guidelines")
        
        st.image('pngwing.com (18).png', width=700)

        st.markdown("<h1 style = 'top_margin: 0rem; text-align: centre; color: #557A46'>PROJECT SUMMARY</h1>", unsafe_allow_html= True)

        st.markdown("<p style = 'top_margin: 0rem; text-align: justify; color: #00C4FF'>Predicting smoking behavior is a complex task that involves a variety of factors, including genetics, environmental influences, and personal choices. Researchers have developed models and methods to predict smoking behavior based on various data sources and factors. predicting smoking behavior is a multidisciplinary endeavor that relies on various factors and data sources. While predictive models can provide valuable insights and aid in public health efforts, they should be used ethically and responsibly, considering individual privacy and societal well-being.</p>", unsafe_allow_html=True)
    
        data = pd.read_csv('sampled_data.csv')
        heat = plt.figure(figsize = (20,20))
        sns.heatmap(data.drop(['sex', 'DRK_YN'],axis = 1).corr(),annot=True,cmap='coolwarm',linewidths=0.5)
        plt.title('Correlation Heatmap',fontsize = 25)

        st.write(heat)

        data = pd.read_csv('sampled_data.csv')
        st.write(data.sample(10))

        st.sidebar.image('pngwing.com (20).png', caption= f'Welcome {username}')
        input_type = st.sidebar.selectbox('Select Your Prefered Input Type', ['Slider Input', 'Number Input'])
        ['gamma_GTP', 'hemoglobin', 'sex', 'triglyceride', 'BLDS', 'serum_creatinine', 'HDL_chole', 'age', 'urine_protein']

        if input_type == 'Slider Input':
            gamma = st.sidebar.slider('gamma_GTP', data['gamma_GTP'].min(), data['gamma_GTP'].max())
            hemoglobin = st.sidebar.slider('hemoglobin', data['hemoglobin'].min(), data['hemoglobin'].max())
            sex = st.sidebar.select_slider('sex', data['sex'].unique())
            triglyceride = st.sidebar.slider('triglyceride', data['triglyceride'].min(), data['triglyceride'].max())
            BLDS = st.sidebar.slider('BLDS', data['BLDS'].min(), data['BLDS'].max())
            serum = st.sidebar.slider('serum_creatinine', data['serum_creatinine'].min(), data['serum_creatinine'].max())
            chole = st.sidebar.slider('HDL_chole', data['HDL_chole'].min(), data['HDL_chole'].max())
            age = st.sidebar.slider('age', data['age'].min(), data['age'].max())
            urine = st.sidebar.slider('urine_protein', data['urine_protein'].min(), data['urine_protein'].max())

        else:
            gamma = st.sidebar.number_inputer('gamma_GTP', data['gamma_GTP'].min(), data['gamma_GTP'].max())
            hemoglobin = st.sidebar.number_input('hemoglobin', data['hemoglobin'].min(), data['hemoglobin'].max())
            sex = st.sidebar.selectbox('sex', data['sex'].unique())
            triglyceride = st.sidebar.number_input('triglyceride', data['triglyceride'].min(), data['triglyceride'].max())
            BLDS = st.sidebar.number_input('BLDS', data['BLDS'].min(), data['BLDS'].max())
            serum = st.sidebar.number_input('serum_creatinine', data['serum_creatinine'].min(), data['serum_creatinine'].max())
            chole = st.sidebar.number_inputider('HDL_chole', data['HDL_chole'].min(), data['HDL_chole'].max())
            age = st.sidebar.number_input('age', data['age'].min(), data['age'].max())
            urine = st.sidebar.number_input('urine_protein', data['urine_protein'].min(), data['urine_protein'].max())



        st.markdown("<br>", unsafe_allow_html= True)  

    # Bring all the inputs into a dataframe
        input_variable = pd.DataFrame([{'gamma_GTP' : gamma, 'hemoglobin' : hemoglobin, 'sex' : sex, 'triglyceride' : triglyceride, 'BLDS' : BLDS, 'serum_creatinine' : serum, 'HDL_chole' : chole, 'age' : age, 'urine_protein' : urine}])
        st.write(input_variable)

        from sklearn.preprocessing import LabelEncoder, StandardScaler
        encoder = LabelEncoder()
        scaler = StandardScaler()

        for i in input_variable:
            if input_variable[i].dtypes != 'O':
               input_variable[i] = scaler.fit_transform(input_variable[[i]])
            else:
                input_variable[i] = encoder.fit_transform(input_variable[i]) 

# Create a tab for prediction and interpretation
        pred_result, interpret = st.tabs(["Prediction Tab", "Interpretation Tab"])
        prediction = None
        with pred_result:
            if st.button('PREDICT'):
                st.markdown("<br>", unsafe_allow_html= True)
                prediction = smoking_model.predict(input_variable)
                st.write("Smoking Status :", prediction)
                st.toast('Input is Predicted')
            else:
                st.write('Pls press the predict button for prediction')
    

        with interpret:
            st.subheader('Model Interpretation')
            if prediction == 1:
                st.write(['Due to all the variables identified, the result shows that you are a "NON SMOKER'])
            elif prediction == 2:
                st.write(['Due to all the variables identified, the result shows that you are an "EX SMOKER'])  
            elif prediction == 3:
                st.write(['Due to all the variables identified, the result shows that you are a "SMOKER'])              
  


    elif menu == "Drinking Prediction":
        st.subheader("PREDICTING DRINKING STATUS")
        username = st.text_input('Enter your name')
        if st.button('submit name'):
            st.success(f"Welcome {username}. Pls use according to usage guidelines")
        
        st.image('pngwing.com (19).png', width=700)

        st.markdown("<h1 style = 'top_margin: 0rem; text-align: centre; color: #557A46'>PROJECT SUMMARY</h1>", unsafe_allow_html= True)

        st.markdown("<p style = 'top_margin: 0rem; text-align: justify; color: #00C4FF'>Predicting drinking behavior can be a complex task and depends on various factors, including individual differences, social and environmental influences, and personal motivations. It's important to note that predicting individual drinking behavior is highly context-specific and may not always be accurate due to the complexity of human behavior and the multifaceted nature of alcohol consumption. Accurate predictions may require a combination of the factors mentioned above and advanced statistical modeling.</p>", unsafe_allow_html=True)
    
        data = pd.read_csv('sampled_data.csv')
        heat = plt.figure(figsize = (20,20))
        sns.heatmap(data.drop(['sex', 'DRK_YN'],axis = 1).corr(),annot=True,cmap='coolwarm',linewidths=0.5)
        plt.title('Correlation Heatmap',fontsize = 25)

        st.write(heat)

        data = pd.read_csv('sampled_data.csv')
        st.write(data.sample(10))

        st.sidebar.image('pngwing.com (21).png', caption= f'Welcome {username}')
        input_type = st.sidebar.selectbox('Select Your Prefered Input Type', ['Slider Input', 'Number Input'])
        ['gamma_GTP', 'hemoglobin', 'sex', 'triglyceride', 'BLDS', 'serum_creatinine', 'HDL_chole', 'age', 'urine_protein']

        if input_type == 'Slider Input':
            gamma = st.sidebar.slider('gamma_GTP', data['gamma_GTP'].min(), data['gamma_GTP'].max())
            hemoglobin = st.sidebar.slider('hemoglobin', data['hemoglobin'].min(), data['hemoglobin'].max())
            sex = st.sidebar.select_slider('sex', data['sex'].unique())
            triglyceride = st.sidebar.slider('triglyceride', data['triglyceride'].min(), data['triglyceride'].max())
            BLDS = st.sidebar.slider('BLDS', data['BLDS'].min(), data['BLDS'].max())
            serum = st.sidebar.slider('serum_creatinine', data['serum_creatinine'].min(), data['serum_creatinine'].max())
            chole = st.sidebar.slider('HDL_chole', data['HDL_chole'].min(), data['HDL_chole'].max())
            age = st.sidebar.slider('age', data['age'].min(), data['age'].max())
            urine = st.sidebar.slider('urine_protein', data['urine_protein'].min(), data['urine_protein'].max())

        else:
            gamma = st.sidebar.number_inputer('gamma_GTP', data['gamma_GTP'].min(), data['gamma_GTP'].max())
            hemoglobin = st.sidebar.number_input('hemoglobin', data['hemoglobin'].min(), data['hemoglobin'].max())
            sex = st.sidebar.selectbox('sex', data['sex'].unique())
            triglyceride = st.sidebar.number_input('triglyceride', data['triglyceride'].min(), data['triglyceride'].max())
            BLDS = st.sidebar.number_input('BLDS', data['BLDS'].min(), data['BLDS'].max())
            serum = st.sidebar.number_input('serum_creatinine', data['serum_creatinine'].min(), data['serum_creatinine'].max())
            chole = st.sidebar.number_inputider('HDL_chole', data['HDL_chole'].min(), data['HDL_chole'].max())
            age = st.sidebar.number_input('age', data['age'].min(), data['age'].max())
            urine = st.sidebar.number_input('urine_protein', data['urine_protein'].min(), data['urine_protein'].max())



        st.markdown("<br>", unsafe_allow_html= True)  

    # Bring all the inputs into a dataframe
        input_variable = pd.DataFrame([{'gamma_GTP' : gamma, 'hemoglobin' : hemoglobin, 'sex' : sex, 'triglyceride' : triglyceride, 'BLDS' : BLDS, 'serum_creatinine' : serum, 'HDL_chole' : chole, 'age' : age, 'urine_protein' : urine}])
        st.write(input_variable)

        from sklearn.preprocessing import LabelEncoder, StandardScaler
        encoder = LabelEncoder()
        scaler = StandardScaler()

        for i in input_variable:
            if input_variable[i].dtypes != 'O':
               input_variable[i] = scaler.fit_transform(input_variable[[i]])
            else:
                input_variable[i] = encoder.fit_transform(input_variable[i]) 

# Create a tab for prediction and interpretation
        pred_result, interpret = st.tabs(["Prediction Tab", "Interpretation Tab"])
        prediction = None
        with pred_result:
            if st.button('PREDICT'):
                st.markdown("<br>", unsafe_allow_html= True)
                prediction = drinking_model.predict(input_variable)
                st.write("Drinking Status :", prediction)
                st.toast('Input is Predicted')
            else:
                st.write('Pls press the predict button for prediction')
    

        with interpret:
            st.subheader('Model Interpretation')
            if prediction == 0:
                st.write(['Due to all the variables identified, the result shows that you are an "HEAVY DRINKER"'])
            elif prediction == 1:
                st.write(['Due to all the variables identified, the result shows that you are not a "NON DRINKER"'])  
                          
  


if __name__ == '__main__':
    main()

# # ---------------------LOAD MODEL--------------------
# model1 = pickle.load(open('Smoking_stats.pkl', "rb"))
# model2 = pickle.load(open('Drinking_stats.pkl', "rb"))

# st.markdown("<h1 style = 'text-align: centre; color: #F11A7B'>SMOKING AND DRINKING PREDICTION PROJECT</h1> ", unsafe_allow_html = True)
# st.markdown("<h3 style = ''text-align: centre; text-align: right; color: #8062D6'>Built By Hope FINAL PROJECT</h3>", unsafe_allow_html= True)

# st.image('pngwing.com (18).png', width=700)

# st.markdown("<h1 style = 'top_margin: 0rem; text-align: centre; color: #557A46'>PROJECT SUMMARY</h1>", unsafe_allow_html= True)

# st.markdown("<p style = 'top_margin: 0rem; text-align: justify; color: #00C4FF'>Financial inclusion refers to the effort to provide individuals and businesses with access to affordable and appropriate financial products and services. The goal of financial inclusion is to ensure that all people, regardless of their socioeconomic status, have access to basic financial tools and resources to manage their financial lives, save for the future, invest in opportunities, and protect themselves against financial shocks.Financial inclusion is seen as a key driver of economic development and poverty reduction. It can help individuals and communities build assets, access opportunities, and improve their overall well-being. Governments, financial institutions, and international organizations often work together to promote financial inclusion through policy initiatives, regulatory changes, and the development of financial products and services tailored to the needs of underserved populations</p>", unsafe_allow_html=True)

# st.markdown("<br><br>", unsafe_allow_html= True)

# username = st.text_input('Enter your name')
# if st.button('submit name'):
#     st.success(f"Welcome {username}. Pls use according to usage guidelines")

# data = pd.read_csv('sampled_data.csv')
# heat = plt.figure(figsize = (20,15))
# sns.heatmap(data.drop(['sex', 'DRK_YN'],axis = 1).corr(),annot=True,cmap='coolwarm',linewidths=0.5)
# # plt.title('Correlation Heatmap',fontsize = 25)

# st.write(heat)

# data = pd.read_csv('sampled_data.csv')
# st.write(data.sample(10))

# # Sidebar to select the page
# MENU = st.sidebar.slider("Choose a page", ["SMOKING", "DRINKING"])
# if MENU == " SMOKING":
#     st.sidebar.image('pngwing.com (19).png', caption= f'Welcome {username}')
#     input_type = st.sidebar.slider('Select Your Prefered Input Type', ['Slider Input', 'Number Input'])

    




# # elif MENU == "DRINKING":
# #     # Define the code for Page 2
# #     model2.run()  # Run the second model


   


