import pandas as pd
from pathlib import Path
import json

mod_path = Path(__file__).parent
relative_path = '../data/replay_list_all.json'
src_path = (mod_path / relative_path).resolve()

# replay_data = pd.read_json(src_path_1)

with open(src_path, 'r') as f:
    data = json.load(f)

replay_data = pd.json_normalize(data)
print(replay_data.columns)


