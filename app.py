#app para agent frameworks con python y modelos 
#con openai y ollama

import asyncio
import os
from agent_framework.openai import OpenAIChatClient

async def main():
    agent = OpenAIChatClient(
        api_key="ollama",  # Placeholder, Ollama doesn't require an API key
        base_url=os.getenv("OLLAMA_ENDPOINT", "http://localhost:11434/v1/"),
        model=os.getenv("OLLAMA_MODEL", "llama3.2:3b")
    ).as_agent(

        name="Asistente medico IA",
        instructions="""Eres un asistente medico local que responde preguntas sobre medicina general y enfermedades comunes. 
        Quiero que respondas con un lenguaje claro, que desglose la respuesta en pasos y que sea facil de entender para un paciente. y que te bases en los sintomas que el paciente te proporciona.  La respuesta la vas a estructurar en un json con las siguientes claves: 'sintomas', 'diagnostico', 'tratamiento', 'prevencion' """,
    )


    consulta = input("Ingrese tu pregunta o sintomas del paciente: ")

    # O con get_final_response() después
    stream = agent.run(consulta, stream=True)
    async for update in stream:
        if update.text:
            print(update.text, end="", flush=True)
    final = await stream.get_final_response()
    print(f"\n\nCompleto: {final.text}")



asyncio.run(main())


# Streaming básico
