# Pioneer Chatbot - Mental Health Support for HUST student

This is an introductory university project focusing on **Natural Language Processing (NLP)** and the development of a **mental health counseling chatbot** for freshmen. The project demonstrates how to fine-tune a transformer-based model on real counseling data and deploy it with a simple web interface.

---

## 📌 Table of Contents

- [🎯 Project Objective](#-project-objective)
- [📚 Dataset](#-dataset)
- [🧠 Model Architecture](#-model-architecture)
- [🛠️ Installation](#️-installation)
- [🏋️‍♂️ Training the Model](#️-training-the-model)
- [💬 Running the Chatbot](#-running-the-chatbot)
- [🧪 Example Interaction](#-example-interaction)
- [📁 Project Structure](#-project-structure)
- [📈 Future Improvements](#-future-improvements)
- [🔐 Disclaimer](#-disclaimer)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 🎯 Project Objective

The primary goal of this project is to:
- Provide **emotional support** through a conversational AI assistant.
- Give students hands-on experience with:
  - Data preprocessing
  - Transformer-based model training
  - Building web-based NLP applications

---

## 📚 Dataset

- **Name**: `Amod/mental_health_counseling_conversations`
- **Source**: [Hugging Face Datasets](https://huggingface.co/datasets/Amod/mental_health_counseling_conversations)
- **Description**: Contains anonymized mental health counseling dialogues with "Context" (user input) and "Response" (counselor reply).

---

## 🧠 Model Architecture

- **Base model**: [`facebook/bart-base`](https://huggingface.co/facebook/bart-base)
- **Type**: Encoder-Decoder (seq2seq) model for text generation
- **Fine-tuning**: Model is trained on input-response pairs from counseling conversations.

---

## 🛠️ Installation

Make sure you have Python ≥ 3.7. Then install the required packages:

```bash
pip install transformers datasets streamlit
