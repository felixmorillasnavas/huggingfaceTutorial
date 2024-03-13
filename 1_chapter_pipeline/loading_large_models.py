# # pip install accelerate
# import torch
# from transformers import pipeline
#
# pipe = pipeline(model="facebook/opt-1.3b", torch_dtype=torch.bfloat16, device_map="cpu")
# output = pipe("This is a cool example!", do_sample=True, top_p=0.95)
# print(output)

# pip install accelerate bitsandbytes
import torch
from transformers import pipeline

pipe = pipeline(model="facebook/opt-1.3b", device_map="cpu", model_kwargs={"load_in_8bit": True})
output = pipe("This is a cool example!", do_sample=True, top_p=0.95)

print(output)

# Does not work may install it again poetry cache clear --all pypi and poetry add bitsandbytes@0.42.0 and all other packages