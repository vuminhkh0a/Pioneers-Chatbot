import torch
from transformers import BartTokenizer, BartForConditionalGeneration, Trainer, TrainingArguments
from datasets import load_dataset

dataset = load_dataset("Amod/mental_health_counseling_conversations", split="train")

tokenizer = BartTokenizer.from_pretrained("facebook/bart-base")

def preprocess(example):
    input_text = example["Context"]
    target_text = example["Response"]
    model_inputs = tokenizer(input_text, max_length=512, padding="max_length", truncation=True)

    with tokenizer.as_target_tokenizer():
        labels = tokenizer(target_text, max_length=128, padding="max_length", truncation=True)

    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

tokenized_dataset = dataset.map(preprocess, batched=True)
tokenized_dataset.set_format(type="torch", columns=["input_ids", "attention_mask", "labels"])

model = BartForConditionalGeneration.from_pretrained("facebook/bart-base")

training_args = TrainingArguments(
    output_dir="./pioneer_chatbot_model",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    save_steps=500,
    save_total_limit=2,
    logging_dir="./logs",
    logging_steps=100,
    report_to="none",
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
)

trainer.train()
trainer.save_model("./pioneer_chatbot_model")
