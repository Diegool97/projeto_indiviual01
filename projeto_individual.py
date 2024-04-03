# CRIAÇÃO DA LISTA PARA ARMAZENAR OS RESULTADOS
candidatos = [
['candidato 1', 'e5_t10_p9_s8'],
['candidato 2', 'e10_t7_p7_s8'],
['candidato 3', 'e8_t5_p7_s9'],
['candidato 4', 'e2_t2_p2_s1'],
['candidato 5', 'e10_t10_p8_s9']
]

#OUTROS RESULTADOS O MESMO FORMATO
nome_candidato = input(f'''
===========================================
        Informe o nome do candito:
        => ''')
entrevista = input(f'''
===========================================
        Informe a avaliação da entrevista(e):
        => ''')
teste_teorico = input(f'''
===========================================
        Informe a avaliação do teste teórico(t):
        => ''')
teste_pratico = input(f'''
===========================================
        Informe a avaliação do teste prático(p):
        => ''')
soft_skills = input(f'''
===========================================
        Informe a avaliação do soft skills(s):
        => ''')

# FUNÇÃO QUE BUSCA O CANDIDATO DE ACORDO COM OS CRITÉRIOS DIGITADOS
