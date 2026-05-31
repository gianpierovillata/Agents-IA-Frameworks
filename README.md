# Agents IA Framework

Agentes conversacionales construidos con **Microsoft Agent Framework** y modelos locales vía **Ollama**.

## Requisitos

- Python 3.10+
- [Ollama](https://ollama.com/) instalado y corriendo localmente
- Modelo descargado: `ollama pull llama3.2:3b`

## Instalación

```bash
git clone <repo>
cd Agents-IA-Framework
pip install agent-framework python-dotenv
```

## Configuración

Copia `.env` (ya incluido) con variables genéricas para cambiar de proveedor sin tocar código:

```env
LLM_API_KEY=ollama
LLM_ENDPOINT=http://localhost:11434/v1/
LLM_MODEL=llama3.2:3b
```

Para usar OpenAI real solo cambias el `.env`:

```env
LLM_API_KEY=sk-proj-...
LLM_ENDPOINT=https://api.openai.com/v1/
LLM_MODEL=gpt-4o
```

## Agentes

### 🩺 Medic Assistant (`medic-asistant.py`)

Asistente médico que recibe síntomas y devuelve un diagnóstico estructurado en JSON con:

- `sintomas` — síntomas descritos
- `diagnostico` — posible condición
- `tratamiento` — recomendaciones
- `prevencion` — medidas preventivas

```bash
python medic-asistant.py
```

### 📞 Asistente Telefónico (`asistente_telefonico.py`)

Asistente de soporte técnico que clasifica fallas y deriva al área correspondiente:

- Falla técnica → soporte técnico
- Falla no técnica → servicio al cliente
- Falla de internet → soporte de internet

```bash
python asistente_telefonico.py
```

## Características técnicas

- **Microsoft Agent Framework** — sucesor de AutoGen + Semantic Kernel
- **Streaming** — respuestas en tiempo real con `stream=True`
- **Variables genéricas** — `LLM_*` en `.env` para cambiar de proveedor sin modificar código
- **Ollama local** — datos privados, sin conexión externa

## Pendientes / Próximos pasos

- [ ] Agregar **function tools** para clasificación estructurada de síntomas
- [ ] Agregar **memoria conversacional** con `InMemoryHistoryProvider`
- [ ] Agregar **sesiones** para contexto multi-turno
- [ ] Manejo de errores (Ollama no corriendo, timeout, etc.)
- [ ] `requirements.txt`

## Licencia

MIT
