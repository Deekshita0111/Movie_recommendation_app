import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv() #active api key
genai.configure(api_key=os.getenv("GOOGLE_GEMINI_API"))


# MOVIE RECOMMENDATION SYSTEM
st.title(" 🍿🎥✮⋆˙Movie Recommendation system 🍿🎥✮⋆˙")
user_input=st.text_input("Enter the movie name ")
submit = st.button("click here")

#if submit and user_input.strip():
 #   st.markdown("Movie name has been entered")
#else:
#    st.warning("no movie name entered")

model = genai.GenerativeModel("gemini-2.5-flash-lite")

if submit and user_input.strip():
    st.markdown(f"Movie name entered:{user_input}")
    response=model.generate_content(f"generate movie recommendation related to :{user_input}")
    st.write(f"realted recommendations for similar movies: \n{response.text}")

else:
    st.write("you need to enter the name of the movie:")


