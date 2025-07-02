# Pioneer Chatbot - Mental Health Support for HUST student

This is my introductory university project: **mental health counseling chatbot** for HUST student. This project uses a pre-trained BART-base model and is deployed on Streamlit.

---

## 🎯 Project Objective

My primary goal of this project is to:
- Provide **emotional support** through a conversational AI assistant.
- Gain hands-on experience with:
  - Transformer-based model fine-tuning
  - Building web-based NLP applications

---

## 📚 Dataset

- **Name**: `Amod/mental_health_counseling_conversations`
- **Source**: [Hugging Face Datasets](https://huggingface.co/datasets/Amod/mental_health_counseling_conversations)
- **Description**: Contains anonymized mental health counseling dialogues with "Context" (user input) and "Response" (counselor reply).

---

## 🧠 Model Architecture

- **Base model**: [`facebook/bart-base`](https://huggingface.co/facebook/bart-base)
- **Type**: Encoder-Decoder model for text generation
- **Fine-tuning**: Model is trained on input-response pairs from counseling conversations.

---

## 🛠️ Installation

Requires Python ≥ 3.7 and the following packages:

```bash
pip install transformers datasets streamlit
