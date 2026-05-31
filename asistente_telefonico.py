import asyncio
import os
from agent_framework.openai import OpenAIChatClient
from dotenv import load_dotenv

load_dotenv()

async def main():
    agente_tel = OpenAIChatClient(
        api_key=os.getenv("LLM_API_KEY", "ollama"),
        base_url=os.getenv("LLM_ENDPOINT", "http://localhost:11434/v1/"),
        model=os.getenv("LLM_MODEL", "llama3.2:3b")
    ).as_agent(
        name="Asistente telefonico IA",
        instructions="""
        Eres un asistente telefonico de una empresa de telefonica, debes responder a la pregunta que puede
        ser tecnica o no, segun la falla podrias responder de lasiguiente manera:
        - Si la falla es tecnica y presenta la consulta la palabra "tecnica" "falla tecnica" "problema tecnico", "le recomendamos que contacte al soporte tecnico de la empresa"
        
        - Si la falla no parece tecnica como por ejemplo "no puedo hacer un pago" "no puedo acceder a mi cuenta" "no puedo ver mi factura", "le recomendamos que contacte al servicio al soporte  al clientede la empresa"
        
        - Si la falla es de internet o muestra la palabra "internet" "falla de internet" "sin datos", "le recomendamos que contacte al soporte de internet de la empresa"
        
        - En cualquier otro caso, "le recomendamos que contacte al servicio atencion con un operador humano de la empresa"
        """
    )

    consulta = input("Ingrese su consulta y le ayudaremos a resolverla: ")

    stream = agente_tel.run(consulta, stream=True)
    async for update in stream:
        if update.text:
            print(update.text, end="", flush=True)
    final = await stream.get_final_response()

    print(f"\n\nCompleto: {final.text}")

asyncio.run(main())