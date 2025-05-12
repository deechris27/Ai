# Imagine you have a master chef (the large pretrained model) who's trained in all kinds of cuisines — Italian, Indian, Chinese, French, etc.

# Now, suppose you want this chef to specialize in just vegan Indian food. You could:

# Retrain the chef from scratch – extremely expensive (like training a model from scratch).

# Fine-tune the entire brain of the chef – still costly and slow (like fine-tuning all model parameters).

# OR, give the chef a little notebook with new vegan Indian recipes to refer to — without changing everything the chef already knows.

# This notebook is LoRA.


# Model used tiny-gpt2, Causal Language Model (predicts next word given previous ones).



from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
from peft import get_peft_model, LoraConfig, TaskType
import torch

model_name = "sshleifer/tiny-gpt2" # A tiny GPT-2 model to try on my 16GB RAM windows system
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)


# This defines how LoRA adapters are added:

# r=4: Low-rank adapter dimension (i.e., how much extra info you allow LoRA to inject — smaller r means faster, but less expressive).

# lora_alpha: A scaling factor for the LoRA update (like a learning rate).

# lora_dropout: Adds regularization.

# inference_mode=False: We're doing training/fine-tuning, not inference only.

# task_type=CAUSAL_LM: Tells LoRA where to insert adapters (in attention layers, mostly).


lora_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    inference_mode = False,
    r=4,
    lora_alpha=16,
    lora_dropout=0.1
)

# Applying LoRA

model = get_peft_model(model, lora_config) #This is the core of LoRA
# This above code wraps the GPT-2 model, freezes all original weights (nothing changes in the base model)
# Inserts tiny trainable adapter layers (LoRA matrices A & B) into attention modules.
# When we train this model, only LoRA parameters are updated.


model.print_trainable_parameters() #This will show 99% of the parameters are frozen, only a small fraction are trainable

input_text = "LoRA makes fine-tuning"
inputs = tokenizer(input_text, return_tensors="pt") # Tokenizes the sentence


## Forward pass (Simulate Training)
# Feeds the tokenized sentences into LoRA-augmented GPT-2
# Calculates loss between model's predicted next tokens and the actual input tokens
outputs = model(**inputs, labels=inputs["input_ids"])
loss = outputs.loss

# .backward() is not used since this is just a simulation of one training step and not real training.

print("Loss: ", loss.item())

# The base GPT-2 is like a "frozen master chef" with global knowledge. We're adding a tiny recipe notepad (LoRA) to specialize it in something new — without overwriting what it already knows.

# The above code:

# Loads the chef.

# Gives him a notebook.

# Tests how well he performs using it.