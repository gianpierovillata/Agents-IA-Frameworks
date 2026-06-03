import asyncio
import os

from agent_framework.openai import OpenAIChatClient
from dotenv import load_dotenv

load_dotenv()

async def main():
    agente_viajes = OpenAIChatClient(
        api_key=os.getenv("LLM_API_KEY", "ollama"),
        base_url=os.getenv("LLM_ENDPOINT", "http://localhost:11434/v1/"),
        model=os.getenv("LLM_MODEL", "llama3.2:3b")
    ).as_agent(
        name="Asistente de viajes IA",
        instructions="""
        Eres un asistente de viajes de una agencia de viajes, que debes responder de manera abierta a preguntas de turismo
        solo daremos referencias de lugares turisticos, hoteles, restaurantes, actividades, etc. en el mundo, no respondas preguntas que no sean de turismo o viajes
        con un esquema de respuesta como el siguiente:
        - Si la consulta es sobre un lugar turistico, responde con una breve descripcion del lugar, su ubicacion y las actividades que se pueden realizar en el lugar
        - Si la consulta es sobre un hotel, responde con una breve descripcion del hotel, su ubicacion, las comodidades que ofrece y el rango de precios aproximado
        - Si la consulta es sobre un restaurante, responde con una breve descripcion del restaurante, su ubicacion, el tipo de comida que ofrece y el rango de precios aproximado
        - Si la consulta es sobre una actividad, responde con una breve descripcion de la actividad,
        su ubicacion, el tipo de actividad que es y el rango de precios aproximado
        """
    )

    consulta = input("Ingrese su consulta y le ayudaremos a resolverla: ")

    stream = agente_viajes.run(consulta, stream=True)
    async for update in stream:
        if update.text:
            print(update.text, end="", flush=True)
    final = await stream.get_final_response()

    print(f"\n\nCompleto: {final.text}")    
