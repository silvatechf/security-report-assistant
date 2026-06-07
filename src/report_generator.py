
import json
from datetime import datetime
from statistics import mean, stdev

class TelemetryParser:
    def __init__(self, telemetry_data: list):
        self.telemetry_data = telemetry_data
        self.extracted_metrics = {}

    def process_incidents(self) -> dict:
        """
        Parses raw JSON telemetry, calculates real behavioral metrics,
        and isolates critical IoCs for the downstream reporting engine.
        """
        if not self.telemetry_data:
            raise ValueError("Telemetry data pipeline is empty. Cannot process.")

        source_ips = set()
        risk_scores = []
        mitre_techniques = set()
        timestamps = []
        classifications = set()
        
        # Extract operational data from structured logs
        for event in self.telemetry_data:
            source_ips.add(event.get("source_ip"))
            risk_scores.append(event.get("risk_score", 0.0))
            mitre_techniques.add(event.get("mitre_technique"))
            timestamps.append(event.get("timestamp"))  # CORREGIDO: Uso correto de .append() para listas
            classifications.add(event.get("classification"))

        # Calculate real mathematical indicators (No static fallbacks)
        max_risk = max(risk_scores) if risk_scores else 0.0
        avg_risk = mean(risk_scores) if risk_scores else 0.0
        risk_variance = stdev(risk_scores) if len(risk_scores) > 1 else 0.0

        self.extracted_metrics = {
            "target_host": list(source_ips)[0] if source_ips else "UNKNOWN",
            "total_events_analyzed": len(self.telemetry_data),
            "max_risk_score": round(max_risk, 2),
            "average_risk_score": round(avg_risk, 2),
            "temporal_behavior_variance": round(risk_variance, 2),
            "mapped_mitre_techniques": list(filter(None, mitre_techniques)),
            "detected_classifications": list(filter(None, classifications)),
            "analysis_window_start": min(timestamps) if timestamps else "N/A",
            "analysis_window_end": max(timestamps) if timestamps else "N/A",
            "extraction_timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        }
        
        return self.extracted_metrics

# =====================================================================
# SIMULADOR DE VALIDACIÓN OPERACIONAL (READY TO RUN)
# =====================================================================
if __name__ == "__main__":
    print("[*] Initiating Lab 4 Telemetry Parser Validation...")

    # Mocking real output coming straight from our Lab 3 Triage Pipeline
    mock_lab3_output = [
        {
            "timestamp": "2026-06-04T18:40:01Z",
            "source_ip": "185.220.101.5",
            "risk_score": 70.00,
            "classification": "SUSPICIOUS_ACTIVITY",
            "mitre_technique": "T1110",
            "description": "POTENTIAL MALICIOUS ATTEMPT"
        },
        {
            "timestamp": "2026-06-04T18:40:02Z",
            "source_ip": "185.220.101.5",
            "risk_score": 97.00,
            "classification": "HIGH_RISK",
            "mitre_technique": "T1110",
            "description": "CRITICAL THREAT - AUTOMATED ATTACK DETECTED"
        }
    ]

    try:
        # Initialize the engineering parser
        parser = TelemetryParser(telemetry_data=mock_lab3_output)
        structured_payload = parser.process_incidents()

        print("\n[+] Extraction Successful! Structured Payload for LLM Stream:")
        print(json.dumps(structured_payload, indent=4))
        
    except Exception as e:
        print(f"[-] Validation failed: {str(e)}")
