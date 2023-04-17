import pickle
import numpy as np
import streamlit as st
import os
print(os.getcwd())

def load_model(modelfile):
    loaded_model = pickle.load(open(modelfile, 'rb'))
    return loaded_model


def main():

    # Set page title and favicon
    st.set_page_config(page_title="Crop Recommendation", page_icon='🌱',layout='wide')
    st.markdown('''# Crop Recommendation 🌱''')
    st.subheader('Find out the most suitable crop to grow in your farm 👨‍🌾')
    # Add header image and title
    st.image('https://images.nationalgeographic.org/image/upload/t_edhub_resource_key_image/v1638892233/EducationHub/photos/crops-growing-in-thailand.jpg', use_column_width=True)
    st.write('')
    st.write('')
    st.write('')
    st.markdown('''
    ## Let's See How It Work's
    #### Optimize crop selection with our machine learning model. Input all relevant parameters and receive tailored recommendations that enhance productivity and profitability, with the potential to revolutionize your farming practices. 
    ''')


    # Add sidebar section
    st.sidebar.subheader('ℹ️ Information')
    st.sidebar.write("""
    Precision agriculture is an innovative approach to farming that seeks to optimize crop production by using data-driven insights. One of the key aspects of precision agriculture is crop recommendation, which involves considering a variety of factors to determine the best crops to grow. Our ML-powered web-app takes this approach to the next level by leveraging machine learning algorithms to provide highly accurate and precise crop recommendations tailored to the specific needs of your farm. By using our app, you can make informed decisions about which crops to grow, resulting in improved yields, lower costs, and increased profitability. Try it out today and see the difference precision agriculture can make!
    """)
    st.sidebar.markdown("""
    # By Swayam
    """)


    # Add main content section

    st.write('')
    st.write('')
    st.write('')
    col1, col2 = st.columns([1, 1])
    with col1:
        st.write('### Enter the following details:')
        N = st.number_input('Nitrogen (N)', 1, 10000)
        P = st.number_input('Phosphorus (P)', 1, 10000)
        K = st.number_input('Potassium (K)', 1, 10000)
        temp = st.number_input('Temperature (°C)', 0.0, 100000.0)
        humidity = st.number_input('Humidity (%)', 0.0, 100000.0)
        ph = st.number_input('Ph', 0.0, 100000.0)
        rainfall = st.number_input('Rainfall (mm)', 0.0, 100000.0)
        if st.button('Predict'):
            feature_list = [N, P, K, temp, humidity, ph, rainfall]
            single_pred = np.array(feature_list).reshape(1, -1)
            loaded_model = load_model('crop.pkl')
            prediction = loaded_model.predict(single_pred)
            st.write('')
            st.write('')
            st.write('')
            st.write('### Results 🔍')
            st.write(f'{prediction.item().title()}.bo are recommended by the A.I for your farm.')

    with col2:
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.image('https://images.squarespace-cdn.com/content/v1/63064607eb816a4d50027fd1/1662579637156-17TGAIEEXOQ68AJAS2ZF/Eden+Green+Kale+Row.jpg?format=1000w', use_column_width=True)


if __name__ == '__main__':
    main()
