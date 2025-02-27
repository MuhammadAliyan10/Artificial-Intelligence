from pgmpy.inference import VariableElimination
from Model import model  # Import the pgmpy BayesianNetwork from Model.py

inference = VariableElimination(model)

evidence = {"train": "delayed"}

predictions = {}
for node in model.nodes():
    if node not in evidence:
        result = inference.query(variables=[node], evidence=evidence)
        predictions[node] = result
    else:
        predictions[node] = evidence[node]

for node in model.nodes():
    prediction = predictions[node]
    if node in evidence:
        print(f"{node}: {evidence[node]}")
    else:
        print(f"{node}")
        for value, probability in zip(prediction.state_names[node], prediction.values):
            print(f"{value}: {probability:.4f}")
