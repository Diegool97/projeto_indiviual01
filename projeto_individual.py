# CRIAÇÃO DA LISTA PARA ARMAZENAR OS RESULTADOS
candidatos = [
['candidato 1', 'e5_t10_p9_s8'],
['candidato 2', 'e10_t7_p7_s8'],
['candidato 3', 'e8_t5_p7_s9'],
['candidato 4', 'e2_t2_p2_s1'],
['candidato 5', 'e10_t10_p8_s9']
]

#OUTROS RESULTADOS O MESMO FORMATO
entrevista = int(input(f'''
===========================================
        Informe a avaliação da entrevista(e):
        => '''))
teste_teorico = int(input(f'''
===========================================
        Informe a avaliação do teste teórico(t):
        => '''))
teste_pratico = int(input(f'''
===========================================
        Informe a avaliação do teste prático(p):
        => '''))
soft_skills = int(input(f'''
===========================================
        Informe a avaliação do soft skills(s):
        => '''))

# FUNÇÃO QUE BUSCA O CANDIDATO DE ACORDO COM OS CRITÉRIOS DIGITADOS
def busca_candidato(candidatos, nota_minima_entrevista, nota_minima_teste_teorico, nota_minima_teste_pratico, nota_minima_soft_skills):
    candidatos_compativeis = []
    for candidato in candidatos:
        notas = candidato[1].split('_')  # DIVISÃO DA STRING EM PARTES PARA ESTRAÇÃO
        nota_entrevista = int(notas[0][1:])  
        nota_teste_teorico = int(notas[1][1:])  
        nota_teste_pratico = int(notas[2][1:])  
        nota_soft_skills = int(notas[3][1:])  
        if (nota_entrevista >= entrevista and
            nota_teste_teorico >= teste_teorico and
            nota_teste_pratico >= teste_pratico and
            nota_soft_skills >= soft_skills):
            candidatos_compativeis.append(candidato)
    return candidatos_compativeis

candidatos_encontrados = busca_candidato(candidatos, entrevista, teste_teorico, teste_pratico, soft_skills)

# EXIBIÇÃO DO RESULTADO
if candidatos_encontrados:
    print("\nCandidatos compatíveis encontrados:")
    for candidato in candidatos_encontrados:
        print(f"Nome: {candidato[0]}")
else:
    print("\nNenhum candidato compatível encontrado com os critérios especificados.")



