# Pioneer Chatbot - Mental Health Support for HUST student

This is my introductory university project: **mental health counseling chatbot** for HUST student. This project uses a pre-trained BART-base model and is deployed on Streamlit.

---

## 1. Project Objective

My primary goal of this project is to:
- Provide **emotional support** for students through an AI assistant.
- Gain more experience with:
  - Transformer-based model fine-tuning
  - Building website for NLP applications
---

## 2. Dataset

- **Name**: `Amod/mental_health_counseling_conversations`
- **Source**: [Hugging Face Datasets](https://huggingface.co/datasets/Amod/mental_health_counseling_conversations)
- **Description**: Contains mental health counseling dialogues with "Context" (user input) and "Response" (counselor reply).

---

## 3. Model Architecture

This project uses `facebook/bart-base` model. (Bidirectional and Auto-Regressive Transformers)** combines the strengths of BERT (bidirectional encoder) and GPT (auto-regressive decoder).

- **Pretrained** on large-scale text corpora via denoising autoencoding and language modeling objectives.
- **Fine-tuned** on the `Amod/mental_health_counseling_conversations` dataset using Hugging Face's `Trainer`, with input as "Context" and target as "Response".
- **Tokenization** handled by `BartTokenizer` with padding and truncation.
- **Optimization** over 3 epochs using `TrainingArguments` with batch size 4.
- **Deployment** via `Streamlit`
---

## 4. Installation

Requires Python ≥ 3.7 and the following packages:

```bash
pip install transformers datasets streamlit
