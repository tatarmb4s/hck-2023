#Athor: Copyright © 2023: Tatár Mátyás Bence (https://github.com/tatarmb4s/) - All Right Reserved

#Pizza feladat

#importok
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, LLMPredictor, PromptHelper, ServiceContext, StorageContext, load_index_from_storage
from llama_index.node_parser import SimpleNodeParser
from langchain.chat_models import ChatOpenAI
import os, json, re
if not os.environ.get("OPENAI_API_KEY"):
    #Kulcs: hackatonos
    # os.environ["OPENAI_API_KEY"] = "IDE-KELL-A-KULCSOT" # ide kell majd az emailban kapott kulcsot bemásolni
    os.environ["OPENAI_API_KEY"] = "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" # ide kell majd az emailban kapott kulcsot bemásolni
context, Gstatus = "", "null" # kontextus
docs = SimpleDirectoryReader("D:\\Race\\Hackaton\\pizzabot\\trainData\\").load_data()
def Reader(path):
    pass
Reader("pizzabot\\output\\trainData")
try:
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    vIndex = load_index_from_storage(storage_context)
except:    
    maxInp, tokens, chunkS, mx_chunk_overlap = 4096, 300, 600, 20
    
    prHelper = PromptHelper(maxInp, tokens, mx_chunk_overlap, chunk_size_limit=chunkS)
    llmPreder = LLMPredictor(llm=ChatOpenAI(temperature=0.4, model_name="gpt-3.5-turbo",max_tokens=tokens))
    service_context = ServiceContext.from_defaults(llm_predictor=llmPreder, prompt_helper=prHelper)
    
    vIndex = GPTVectorStoreIndex.from_documents(documents=docs,service_context=service_context)
    vIndex.storage_context.persist()

qEngine = vIndex.as_query_engine()

def JSONGetter(text):
    global Gstatus
    first = text.index('{')
    last = text.index('}')
    jsonText = text[first:last+1]
    jsonText = re.sub(r'//.*', '', jsonText)
    pyData = json.loads(jsonText)
    Gstatus = pyData['status']
    # print(pyData['response'], "\n---\n")
    return pyData

#Ellenőrzi, hogy az LLM szerint vége van e a folyamatnak, és rákérdez még egyszer.
def isVege(pyData):
    if pyData['status'] == "end":
        response = JSONGetter(BotAsker("Kérdezz rá a rendelés végére / Ask for the end of order"))
        if response['status'] == "end":
            # print(response['response'])
            pass
        else:
            BotAsker(input("Te: "))
    else:
        BotAsker(input("Te: "))
# A bot chat intercafe, a meglévő tudásbázist használva.
def BotAsker(bemenet):
    global context
    context += f"USER:\n{bemenet}\n"
    qResp = qEngine.query(context)
    context += f"ASSISTANT:\n{qResp}\n"
    pyData = JSONGetter(qResp.response)
    print("PizzaAI: ",pyData['response'])
    if pyData['status'] == "end":
        print("Rendelés leadva!")
        print(pyData['notes'])
    else:
        isVege(pyData)
    return qResp
    
BotAsker(input("Te: "))
#Athor: Copyright © 2023: Tatár Mátyás Bence (https://github.com/tatarmb4s/) - All Right Reserved