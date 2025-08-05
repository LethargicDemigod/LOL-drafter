import csv
import torch

def load_champion_vectors(csv_path):
    champ_to_vec = {}
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["champion"]
            vec = torch.tensor([
                float(row["damage"]),
                float(row["toughness"]),
                float(row["control"]),
                float(row["mobility"]),
                float(row["utility"])
            ], dtype=torch.float32)
            champ_to_vec[name] = vec
    return champ_to_vec
