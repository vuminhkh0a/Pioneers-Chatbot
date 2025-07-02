# Pioneer Chatbot - Mental Health Support for HUST student

This is my introductory university project: **mental health counseling chatbot** for HUST student. This project uses a pre-trained BART-base model and is deployed on Streamlit.

---

## 1. Project Objective

My primary goal of this project is to:
- Provide **emotional support** through a conversational AI assistant.
- Gain hands-on experience with:
  - Transformer-based model fine-tuning
  - Building web-based NLP applications

---

## 2. Dataset

- **Name**: `Amod/mental_health_counseling_conversations`
- **Source**: [Hugging Face Datasets](https://huggingface.co/datasets/Amod/mental_health_counseling_conversations)
- **Description**: Contains anonymized mental health counseling dialogues with "Context" (user input) and "Response" (counselor reply).

---

## 3. Model Architecture

This project utilizes the `facebook/bart-base` model — a Transformer-based sequence-to-sequence model with an encoder-decoder architecture, suitable for text generation.

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
