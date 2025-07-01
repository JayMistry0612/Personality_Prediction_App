import pickle

pipe=pickle.load(open('pipe.pkl', 'rb'))

import streamlit as st

st.title("Personality Prediction App")  
st.write("This app predicts personality traits based on user input.")  

tsa=st.text_input(label='Time_spent_alone')
sf=st.text_input(label='Stage_fear(Yes/No)')
sea=st.text_input(label='Social_event_attendance')
go=st.text_input(label='Going_out')
das=st.text_input(label='Drained_after_socializing(Yes/No)')
fcs=st.text_input(label='Friends_circle_size')
pf=st.text_input(label='Post_frequency')

if st.button('Predict Personality'):
    try:
        input_data = [
            tsa,
            sf,
            sea,
            go,
            das,
            fcs,
            pf
        ]
        prediction = pipe.predict([input_data])[0]
        st.success(f'Predicted Personality: {prediction}')
    except Exception as e:
        st.error(f'Error in prediction: {e}')