from Model import model

state = {
    "rain": "none",
    "maintenance": "no",
    "train": "on time",
    "appointment": "attend",
}

probability = model.get_state_probability(state)
print(probability)
