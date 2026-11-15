import json
from app import *
rows = [Telemetry(40,0,20,f'baseline-{i}') for i in range(8)]
rows += [Telemetry(99,7,500,'demo'), Telemetry(60,6,22,'training')]
print(json.dumps(detect(rows)))
