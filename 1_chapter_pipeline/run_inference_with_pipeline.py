# from transformers import pipeline
#
# # transcriber = pipeline(task="automatic-speech-recognition")
# #
# # print(transcriber("https://huggingface.co/datasets/Narsil/asr_dummy/resolve/main/mlk.flac"))
#
# pipe = pipeline(task="text-classification")
# print(pipe("This restaurant is awesome"))

import datasets
from transformers import pipeline
from transformers.pipelines.pt_utils import KeyDataset
from tqdm.auto import tqdm

pipe = pipeline("automatic-speech-recognition", model="facebook/wav2vec2-base-960h", device="cpu")
dataset = datasets.load_dataset(path="superb", name="asr", split="test", trust_remote_code=True)

text = pipe(dataset[0]["file"])

print(dataset[0]["text"])


def tokenize(text):
    return set(text.lower().split())


tokens1 = tokenize(dataset[0]["text"])
tokens2 = tokenize(text["text"])


def jaccard_similarity(tokens1, tokens2):
    intersection = tokens1.intersection(tokens2)
    union = tokens1.union(tokens2)
    return len(intersection) / len(union)


similarity = jaccard_similarity(tokens1, tokens2)
print(f"Jaccard Similarity: {similarity}")


for out in tqdm(pipe(KeyDataset(dataset, "file"))):
    print(out)
    # {"text": "NUMBER TEN FRESH NELLY IS WAITING ON YOU GOOD NIGHT HUSBAND"}
    # {"text": ....}
