from datetime import datetime

def make_alert(event_id: str, risk_score: float, reason: str) -> dict:
    """Create a simple structured alert for the prototype."""
    return {
        "event_id": event_id,
        "risk_score": round(float(risk_score), 4),
        "reason": reason,
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }
