import json
import os

ARQUIVO = os.path.join(os.path.dirname(__file__), '..', 'data', 'atividades.json')

def carregar_atividades():
    try:
        with open(ARQUIVO, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_atividades(atividades):
    with open(ARQUIVO, 'w', encoding='utf-8') as f:
        json.dump(atividades, f, indent=2, ensure_ascii=False)

def buscar_atividade(id):
    atividades = carregar_atividades()
    return next((a for a in atividades if a["id"] == id), None)
