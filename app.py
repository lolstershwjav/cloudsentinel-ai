from dataclasses import dataclass
from statistics import mean, pstdev

@dataclass
class Telemetry:
    gpu_util: float
    failed_logins: int
    egress_mb: float
    tenant: str

def detect(events: list[Telemetry]) -> list[dict]:
    if not events:
        return []
    avg = mean(e.egress_mb for e in events)
    sd = pstdev(e.egress_mb for e in events)
    alerts = []
    for e in events:
        reasons = []
        if e.failed_logins >= 5: reasons.append('repeated authentication failures')
        if e.gpu_util >= 98: reasons.append('GPU saturation')
        if e.egress_mb > avg + 2 * sd and e.egress_mb > 100: reasons.append('unusual network egress')
        if reasons:
            alerts.append({'tenant':e.tenant,'severity':'high' if len(reasons)>1 else 'medium','reasons':reasons})
    return alerts

def explain(alert: dict) -> str:
    return f"Review tenant {alert['tenant']}: {', '.join(alert['reasons'])}. Confirm against logs before taking action."
