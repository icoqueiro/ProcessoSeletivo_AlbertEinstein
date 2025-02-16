import asyncio
import time

async def chamada_falsa(chamada:int, tempo: float):
  #aqui está a função que simula as chamadas de rede
  await asyncio.sleep(tempo)
  print(f"chamada {chamada} gerada em {tempo} segundos." )

async def main():
  #aqui está a função principal assíncrona
   tempo_inicio = time.time()
   tasks =    [chamada_falsa(1, 4.0), 
              chamada_falsa(2,  1.0), 
              chamada_falsa(3, 3.0),
              ]
   #chama as tarefas simulataneamente
   await asyncio.gather(*tasks)

   tempo_exec = time.time() - tempo_inicio
   print(f"Tempo total de execução: {tempo_exec} segundos.")
   #retorna o tempo total de execução
   print("\nTarefas pendentes")
   for task in asyncio.all_tasks():
     print(task)

#correcao de erro que estava dando referente a rotina do código
try:
  loop = asyncio.get_event_loop()
  if loop.is_running():
    loop.create_task(main())
  else:
    loop.run_until_complete(main())
except Exception as error:
  print("erro")