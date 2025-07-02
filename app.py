import streamlit as st
from transformers import BartTokenizer, BartForConditionalGeneration
import torch

model = BartForConditionalGeneration.from_pretrained("./pioneer_chatbot_model")
tokenizer = BartTokenizer.from_pretrained("facebook/bart-base")
model.eval()

st.title("Pioneer Chatbot - Mental health")
st.write("Hi! Please tell me your thought!")

user_input = st.text_input("You:", "")

if user_input:
    inputs = tokenizer(user_input, return_tensors="pt", max_length=512, truncation=True)
    with torch.no_grad():
        output_ids = model.generate(
            inputs["input_ids"],
            max_length=100,
            num_beams=5,
            early_stopping=True
        )
    response = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    st.write(f"Chatbot: {response}")
