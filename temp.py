import json
from dataclasses import dataclass

@dataclass
class details:
    name: str
    section: str

pd_details = details(
    name="Arijit",
    section="C"
)

jsonstr = json.dumps(pd_details.__dict__)

with open("data.json", "w") as jsonfile:
    jsonfile.write(jsonstr)
    # jsonfile.close()