from vllm import LLM, SamplingParams

llm = LLM(
    model='MediaTek-Research/Breeze-7B-FC-v1_0',
    tensor_parallel_size=1, # number of gpus
    gpu_memory_utilization=0.95,
    dtype='half'
)

turn_end_token_id = 61876 # <|im_end|>
params = SamplingParams(
    temperature=0.001,
    top_p=0.001,
    max_tokens=4096,
    repetition_penalty=1.1,
    stop_token_ids=[turn_end_token_id]
)

def _inference(prompt, llm, params):
    return llm.generate(prompt, params)[0].outputs[0].text

if __name__ == "__main__":
    prompt = [
        {"role": "system", "content": "這是一個測試程式，僅為了下載模型用。"},
    ]
    response = _inference(prompt, llm, params)
    