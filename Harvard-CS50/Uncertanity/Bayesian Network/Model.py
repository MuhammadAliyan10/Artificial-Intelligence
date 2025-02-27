from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD


model = BayesianNetwork()


model.add_edges_from(
    [
        ("rain", "maintenance"),
        ("rain", "train"),
        ("maintenance", "train"),
        ("train", "appointment"),
    ]
)


rain_cpd = TabularCPD(
    variable="rain",
    variable_card=3,
    values=[[0.7], [0.2], [0.1]],
    state_names={"rain": ["none", "light", "heavy"]},
)

maintenance_cpd = TabularCPD(
    variable="maintenance",
    variable_card=2,
    values=[[0.4, 0.2, 0.1], [0.6, 0.8, 0.9]],
    evidence=["rain"],
    evidence_card=[3],
    state_names={"maintenance": ["yes", "no"], "rain": ["none", "light", "heavy"]},
)

train_cpd = TabularCPD(
    variable="train",
    variable_card=2,
    values=[[0.8, 0.9, 0.6, 0.7, 0.4, 0.5], [0.2, 0.1, 0.4, 0.3, 0.6, 0.5]],
    evidence=["rain", "maintenance"],
    evidence_card=[3, 2],
    state_names={
        "train": ["on time", "delayed"],
        "rain": ["none", "light", "heavy"],
        "maintenance": ["yes", "no"],
    },
)

appointment_cpd = TabularCPD(
    variable="appointment",
    variable_card=2,
    values=[[0.9, 0.6], [0.1, 0.4]],
    evidence=["train"],
    evidence_card=[2],
    state_names={"appointment": ["attend", "miss"], "train": ["on time", "delayed"]},
)

model.add_cpds(rain_cpd, maintenance_cpd, train_cpd, appointment_cpd)

model.check_model()

print(model)
