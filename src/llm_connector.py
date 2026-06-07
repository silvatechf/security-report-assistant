
import json
import os
from datetime import datetime
from report_generator import TelemetryParser

class SecurityReportAssistant:
    def __init__(self, structured_payload: dict):
        self.payload = structured_payload

    def generate_prompt(self) -> str:
        """
        Builds a strict, corporate security engineering prompt pattern.
        Ensures the output focuses on technical integrity with zero hallucination.
        """
        prompt = (
            "CONTEXTO OPERACIONAL DE SOC:\n"
            f"- Host Objetivo: {self.payload['target_host']}\n"
            f"- Eventos Analizados: {self.payload['total_events_analyzed']}\n"
            f"- Puntuación de Riesgo Máxima: {self.payload['max_risk_score']}/100\n"
            f"- Varianza Temporal de Comportamiento: {self.payload['temporal_behavior_variance']}\n"
            f"- Técnicas MITRE Asociadas: {', '.join(self.payload['mapped_mitre_techniques'])}\n"
            f"- Clasificaciones Detectadas: {', '.join(self.payload['detected_classifications'])}\n"
            "--- \n"
            "INSTRUCCIÓN: Genera un informe ejecutivo de ciberseguridad defensiva en ESPAÑOL. "
            "El tono debe ser sobrio, técnico y enfocado en mitigar riesgos de negocio sin marketing exagerado."
        )
        return prompt

    def mock_llm_stream_response(self) -> str:
        """
        Simulates a deterministic, high-fidelity response from a Security-Augmented LLM.
        Outputs raw Markdown tailored for SOC operations in Barcelona.
        """
        # In a production environment, this method would handle the active HTTP requests
        # to a local LLM server (Ollama) or an enterprise API (OpenAI/Anthropic).
        
        markdown_report = (
            f"# INFORME DE INCIDENTE: ALERTA DE TRIAJE AUTOMATIZADO\n\n"
            f"**Fecha del Análisis:** {self.payload['extraction_timestamp']}\n"
            f"**Área de Operaciones:** Centro de Operaciones de Seguridad (SOC) / Incident Response\n"
            f"**Severidad:** CRÍTICA ({self.payload['max_risk_score']}/100)\n\n"
            f"---\n\n"
            f"## 1. Resumen Ejecutivo\n"
            f"Durante la ventana de observación entre el `{self.payload['analysis_window_start']}` y el `{self.payload['analysis_window_end']}`, "
            f"el pipeline de ingeniería defensiva interceptó y procesó un total de **{self.payload['total_events_analyzed']} eventos** de telemetría de autenticación "
            f"dirigidos al host objetivo `{self.payload['target_host']}`.\n\n"
            f"El motor analítico determinó una varianza de comportamiento temporal de `{self.payload['temporal_behavior_variance']}` milisegundos. "
            f"Una consistencia temporal cercana a cero confirma de forma automatizada un patrón determinista y mecánico, "
            f"clasificando la amenaza como un **Ataque Automatizado Activo** en lugar de un error humano orgánico.\n\n"
            f"## 2. Alineación con Estándares de la Industria (MITRE ATT&CK)\n"
            f"Los indicadores de compromiso (IoCs) y la cadencia del tráfico mapean directamente con los siguientes estándares globales:\n"
            f"- **Táctica:** Acceso a Credenciales (Credential Access)\n"
            f"- **Técnica:** [{', '.join(self.payload['mapped_mitre_techniques'])} - Brute Force](https://attack.mitre.org/techniques/T1110/)\n\n"
            f"## 3. Métricas de Telemetría Analizadas\n"
            f"- **Puntuación de Riesgo Promedio:** {self.payload['average_risk_score']}/100\n"
            f"- **Clasificación de Seguridad:** `HIGH_RISK` / Amenaza Confirmada\n"
            f"- **Indicador de Automatización:** Baja Entropía Temporal Detectada\n\n"
            f"## 4. Plan de Acción de Mitigación Recomendado (Hardening)\n"
            f"1. **Aislamiento Perimetral:** Bloquear el origen de conexión en el Firewall corporativo de forma reactiva e implementar arquitecturas VPN/ZTNA con MFA.\n"
            f"2. **Activación de NLA:** Forzar la Autenticación a Nivel de Red (Network Level Authentication) para mitigar vectores de explotación pre-autenticación.\n"
            f"3. **Políticas de Bloqueo:** Configurar directivas restrictivas de bloqueo de cuentas en el Host ante ráfagas deterministas sucesivas.\n\n"
            f"---\n"
            f"*Informe generado automáticamente por el módulo AI Security Report Assistant de forma agnóstica.*"
        )
        return markdown_report

    def save_report(self, content: str, filename: str = "output/incident_report.md"):
        """Saves the final generated markdown report to the output directory."""
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"[+] Success! Executive report written to: {filename}")
        except IOError as e:
            print(f"[-] Failed to write report file: {str(e)}")

# =====================================================================
# PIPELINE EXECUTION ENGINE
# =====================================================================
if __name__ == "__main__":
    print("[*] Launching Automated SOC Report Assistant Pipeline...")

    # Simulated output from Lab 3
    mock_logs = [
        {"timestamp": "2026-06-07T17:30:00Z", "source_ip": "185.220.101.5", "risk_score": 70.0, "classification": "SUSPICIOUS", "mitre_technique": "T1110"},
        {"timestamp": "2026-06-07T17:30:01Z", "source_ip": "185.220.101.5", "risk_score": 97.0, "classification": "HIGH_RISK", "mitre_technique": "T1110"}
    ]

    # Step 1: Parse data using Lab 4 core module
    parser = TelemetryParser(telemetry_data=mock_logs)
    metrics = parser.process_incidents()

    # Step 2: Pass data to LLM Connector module
    assistant = SecurityReportAssistant(structured_payload=metrics)
    raw_prompt = assistant.generate_prompt()
    
    # Step 3: Extract and Save final findings
    final_report = assistant.mock_llm_stream_response()
    assistant.save_report(content=final_report)
