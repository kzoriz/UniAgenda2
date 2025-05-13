from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
import json
from .utils import carregar_atividades, salvar_atividades, buscar_atividade

def index(request):
    return render(request, 'atividades/index.html')

@csrf_exempt
def atividades(request):
    if request.method == "GET":
        return JsonResponse(carregar_atividades(), safe=False)

    elif request.method == "POST":
        dados = json.loads(request.body)
        atividades = carregar_atividades()
        novo_id = max([a['id'] for a in atividades], default=0) + 1
        dados["id"] = novo_id
        dados["status"] = "pendente"
        atividades.append(dados)
        salvar_atividades(atividades)
        return JsonResponse(dados, status=201)

    return HttpResponseNotAllowed(['GET', 'POST'])

@csrf_exempt
def atividade_detalhe(request, id):
    atividades = carregar_atividades()

    if request.method == "GET":
        atividade = buscar_atividade(id)
        return JsonResponse(atividade if atividade else {}, status=404 if not atividade else 200)

    elif request.method == "PUT":
        dados = json.loads(request.body)
        for i, a in enumerate(atividades):
            if a['id'] == id:
                atividades[i].update(dados)
                salvar_atividades(atividades)
                return JsonResponse(atividades[i])
        return JsonResponse({'erro': 'Atividade não encontrada'}, status=404)

    elif request.method == "DELETE":
        atividades = [a for a in atividades if a['id'] != id]
        salvar_atividades(atividades)
        return JsonResponse({'mensagem': 'Atividade deletada'})

    return HttpResponseNotAllowed(['GET', 'PUT', 'DELETE'])
