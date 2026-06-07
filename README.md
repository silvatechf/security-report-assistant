# SOC Automation Lab 4: AI Security Report Assistant

Este laboratorio técnico implementa un pipeline de automatización para operaciones de seguridad (SecOps) diseñado para mitigar la fatiga de alertas en el SOC y acelerar el Tiempo Medio de Respuesta (MTTR). 

El sistema actúa como un microservicio en Python que ingiere la telemetría estructurada proveniente del motor de triaje analítico (Lab 3), procesa los Indicadores de Compromiso (IoCs) mediante análisis estadístico y utiliza un modelo de lenguaje (LLM) de forma totalmente determinista y agnóstica para consolidar informes ejecutivos e informes técnicos de incidentes en formato Markdown.

---

## 🎯 Objetivos Técnicos del Laboratorio

* **Ingeniería de Datos de Seguridad:** Normalización y estructuración de payloads JSON complejos provenientes de sensores perimetrales.
* **Automatización del Flujo de Trabajo (SOAR):** Reducción del trabajo operativo manual mediante la generación automatizada de documentación de incidentes.
* **Cómputo Descriptivo:** Análisis de la varianza y desviación estándar del comportamiento temporal para la toma de decisiones del pipeline.
* **Integración con Ecosistemas Corporativos (SIEM Ready):** Diseño de estructuras compatibles con el estándar de la industria (Splunk Core).

---

## 🏛️ Arquitectura del Pipeline Automatizado

El flujo de ejecución se compone de tres capas desacopladas bajo principios de Clean Code:

1. **Capa de Ingesta y Parsing (`src/report_generator.py`):** Modulo encargado de la lectura segura de los logs de telemetría. Extrae de forma dinámica las marcas de tiempo, calcula la entropía y varianza de los ataques y consolida las métricas clave sin recurrir a datos estáticos.
2. **Capa de Abstracción e Integración (`src/llm_connector.py`):** Diseña un patrón de prompt estricto y corporativo que formatea los metadatos y simula/conecta con la API del modelo de lenguaje para obtener una respuesta contextualizada de alta fidelidad.
3. **Capa de Presentación Ejecutiva (`output/`):** Generación automática del archivo `incident_report.md` en español técnico, estructurado con resúmenes ejecutivos, técnicas defensivas y recomendaciones de mitigación activa.

---

## 📊 Validación Visual e Interfaz Operacional (Splunk Integration)

Para demostrar cómo este pipeline de automatización se integra de forma nativa en la infraestructura de un SOC empresarial de elite, se ha diseñado un cuadro de mando utilizando la especificación de interfaz estándar de la industria.

A continuación se muestra el resultado real del pipeline interactuando con el entorno de monitorización en tiempo real, reflejando el procesamiento de un ataque automatizado de fuerza bruta de baja entropía temporal:

![Splunk Security Monitor Dashboard](assets/splunk_monitor.html) 
*(Nota: Inserta aquí el archivo de la captura de pantalla que acabas de realizar salvándola como assets/splunk_monitor.png o similar)*

### Componentes de la Interfaz Implementada:
* **Métricas Clave (KPIs):** Contador de eventos totales ingeridos en la ventana de tiempo, resalte visual del score de riesgo crítico (**97.00/100**) e identificación del host objetivo bajo ataque (`185.220.101.5`).
* **Tabla de Evidencias Estructurada:** Logs de triaje activos normalizados con marcas de tiempo precisas, severidad mapeada dinámicamente y la clasificación automatizada correspondiente.

---

## 🛡️ Alineación con Estándares Globales

El pipeline está completamente integrado con los marcos de referencia internacionales de ciberseguridad defensiva:
* **Táctica de la Matriz:** Acceso a Credenciales (Credential Access).
* **Técnica Específica:** [MITRE ATT&CK T1110 – Brute Force](https://attack.mitre.org/techniques/T1110/).

---

## 🛠️ Stack Tecnológico Utilizado

* **Lenguaje Core:** Python 3 (Aislado mediante entorno virtual nativo `.venv` bajo cumplimiento PEP 668).
* **Librerías Estándar:** `statistics` (para el cálculo de varianza temporal de ráfagas mecánicas), `json`, `datetime`.
* **Especificación de Dashboards:** Splunk Simple XML / HTML Enterprise Layout.
* **Entorno de Desarrollo:** Linux (Kali Linux Environment) controlado de forma remota mediante el ecosistema del Host anfitrión.

---

## 🎓 Propósito del Proyecto

Este repositorio es un laboratorio de ciberseguridad de carácter estrictamente educativo y de portafolio profesional. Demuestra cómo aplicar la automatización de procesos y el uso inteligente de herramientas en la ingeniería defensiva moderna para resolver problemas financieros (ahorro de almacenamiento en SIEM) y operativos (reducción del estrés del analista de SOC) dentro del tejido empresarial actual.
