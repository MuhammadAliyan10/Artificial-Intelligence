from pgmpy.sampling import BayesianModelSampling
from collections import Counter
from Model import model


def generate_sample():
    sampler = BayesianModelSampling(model)
    sample = sampler.forward_sample(size=1)
    return {
        "rain": sample["rain"].values[0],
        "maintenance": sample["maintenance"].values[0],
        "train": sample["train"].values[0],
        "appointment": sample["appointment"].values[0],
    }

N = 10000
data = []
for i in range(N):
    sample = generate_sample()
    if sample["train"] == "delayed":
        data.append(sample["appointment"])

print(Counter(data))
