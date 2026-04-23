# unverified 未完待续


# PEFT 库对预训练模型进行提示微调。
# 以使用 PEFT 进行训练的模型示例包括 Bloom、Llama、GPT-J、GPT-2、BERT 等等
# 加载 PEFT 库
# 这个库包含了各种微调技术的 Hugging Face 实现，包括提示调整。
# pip install -q peft==0.8.2
# pip install -q datasets==2.14.5
# 从 transformers 库中，我们导入必要的类来实例化模型和分词器。

from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "bigscience/bloomz-560m"
#model_name="bigscience/bloom-1b1"
NUM_VIRTUAL_TOKENS = 4
NUM_EPOCHS = 6

tokenizer = AutoTokenizer.from_pretrained(model_name)
foundational_model = AutoModelForCausalLM.from_pretrained(
    model_name,
    trust_remote_code=True
)


#this function returns the outputs from the model received, and inputs.
def get_outputs(model, inputs, max_new_tokens=100):
    outputs = model.generate(
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_new_tokens=max_new_tokens,
        #temperature=0.2,
        #top_p=0.95,
        #do_sample=True,
        repetition_penalty=1.5, #Avoid repetition.
        early_stopping=True, #The model can stop before reach the max_length
        eos_token_id=tokenizer.eos_token_id
    )
    return outputs

# https://huggingface.co/datasets/fka/awesome-chatgpt-prompts
# https://huggingface.co/datasets/Abirate/english_quotes


