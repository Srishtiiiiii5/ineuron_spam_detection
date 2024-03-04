import streamlit as st
from joblib import dump, load

model = load('implement.joblib')

def predict_spam(text):
    # Preprocess the input text (if needed)
    # For example, you might want to tokenize and vectorize the text
    prediction = model.predict([text])

    return prediction

if __name__ == '__main__':
    st.title('SPAM DETECTION APP')
    st.write('Enter an email message to checck its spam or not')

    # User input for text
    user_input = st.text_input('Enter text')
    
    if st.button('Predict'):
        prediction = predict_spam(user_input)
        if prediction==0:
            prediction= "not spam.\n OK REPORT"
        else:
            prediction= "spam"
            
        st.write('Predicted sentiment:', prediction)
    
