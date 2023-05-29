#readme

Szükséges programok:
- python 3.11.2
  - pip packagek:
    - venv
      - pip install langchain, llama_index, openai, venv

Az OpenAI api kulcsot a következő helyre kell bemásolni:
`pizzabot/pizzabot.py` 12.sor
```py
    os.environ["OPENAI_API_KEY"] = "IDE-KELL-A-KULCSOT" # ide kell majd az emailban kapott kulcsot bemásolni
```

https://youtu.be/gEa2xLy4xS0