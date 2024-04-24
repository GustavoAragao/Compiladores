def analizador_lexico(conteudo_arquivo):
    estado_atual = '0'  # estado como string para possivel uso futuro
    # lista que ira armazenar nossas tuplas (linha , coluna, token, lexema)
    tokens_reconhecidos = []
    erros = []
    lexema_atual = ""
    linha_atual = 0
    coluna_atual = 0

    tam_linha = len(conteudo_arquivo)
    # usado para verificação de erros
    tam_ultima_coluna = len(conteudo_arquivo[tam_linha-1])

    while linha_atual < tam_linha:
        coluna_atual = 0  # reseta a coluna para cada nova linha
        while coluna_atual < len(conteudo_arquivo[linha_atual]):
            caractere = conteudo_arquivo[linha_atual][coluna_atual]
            coluna_atual += 1  # atualização da coluna atual
            match estado_atual:
                case '0':
                    if caractere.isdigit():
                        estado_atual = '1'
                        lexema_atual += caractere
                    elif caractere == '.':
                        estado_atual = '5'
                        lexema_atual += caractere
                    elif 'A' <= caractere <= 'F':
                        estado_atual = '21'
                        lexema_atual += caractere
                    elif caractere == '"':
                        estado_atual = '24'
                        lexema_atual += caractere
                    elif 'a' <= caractere <= 'z':
                        estado_atual = '25'
                        lexema_atual += caractere
                    elif caractere == '#':
                        estado_atual = '29'
                    elif caractere == '<':
                        estado_atual = '31'
                    elif caractere == '>':
                        estado_atual = '37'
                    elif caractere == '=':
                        estado_atual = '38'
                    elif caractere == '-':
                        tokens_reconhecidos.append(
                            (linha_atual, coluna_atual, 'tk_menos', ''))
                        estado_atual = '0'
                    elif caractere == '~':
                        tokens_reconhecidos.append(
                            (linha_atual, coluna_atual, 'tk_negação', ''))
                        estado_atual = '0'
                    elif caractere == '+':
                        tokens_reconhecidos.append(
                            (linha_atual, coluna_atual, 'tk_mais', ''))
                        estado_atual = '0'
                    elif caractere == '*':
                        tokens_reconhecidos.append(
                            (linha_atual, coluna_atual, 'tk_mult', ''))
                        estado_atual = '0'
                    elif caractere == '%':
                        tokens_reconhecidos.append(
                            (linha_atual, coluna_atual, 'tk_resto', ''))
                        estado_atual = '0'
                    elif caractere == '&':
                        tokens_reconhecidos.append(
                            (linha_atual, coluna_atual, 'tk_e_logico', ''))
                        estado_atual = '0'
                    elif caractere == '|':
                        tokens_reconhecidos.append(
                            (linha_atual, coluna_atual, 'tk_ou_logico', ''))
                        estado_atual = '0'
                    elif caractere == ':':
                        tokens_reconhecidos.append(
                            (linha_atual, coluna_atual, 'tk_dois_pontos', ''))
                        estado_atual = '0'
                    elif caractere == '(':
                        tokens_reconhecidos.append(
                            (linha_atual, coluna_atual, 'tk_ab_parent', ''))
                        estado_atual = '0'
                    elif caractere == ')':
                        tokens_reconhecidos.append(
                            (linha_atual, coluna_atual, 'tk_fe_parent', ''))
                        estado_atual = '0'
                    elif caractere.isspace():
                        estado_atual = "0"  # ignorar erros para caracteres invisíveis retornando para estado 0
                    else:
                        erros.append(
                            (linha_atual, coluna_atual, 'esse caractere não pode iniciar nenhum tk'))
                case '1':
                    if caractere.isdigit():
                        estado_atual = '2'
                        lexema_atual += caractere
                    elif caractere == '.':
                        estado_atual = '6'
                        lexema_atual += caractere
                    elif caractere == 'x':
                        estado_atual = '22'
                        lexema_atual += caractere
                    else:
                        tokens_reconhecidos.append(
                            (linha_atual, (coluna_atual - len(lexema_atual)), 'tk_int', lexema_atual))
                        estado_atual = '0'
                        lexema_atual = ""
                        coluna_atual -= 1
                case '2':
                    if caractere.isdigit():
                        estado_atual = '3'
                        lexema_atual += caractere
                    elif caractere == '.':
                        estado_atual = '6'
                        lexema_atual += caractere
                    elif caractere == '/':
                        estado_atual = '10'
                        lexema_atual += caractere
                    elif caractere == '_':
                        estado_atual = '14'
                        lexema_atual += caractere
                    else:
                        tokens_reconhecidos.append(
                            (linha_atual,  (coluna_atual - len(lexema_atual)), 'tk_int', lexema_atual))
                        estado_atual = '0'
                        lexema_atual = ""
                        coluna_atual -= 1
                case '3':
                    if caractere.isdigit():
                        estado_atual = '4'
                        lexema_atual += caractere
                    elif caractere == '.':
                        estado_atual = '6'
                        lexema_atual += caractere
                    else:
                        tokens_reconhecidos.append(
                            (linha_atual, (coluna_atual - len(lexema_atual)), 'tk_int', lexema_atual))
                        estado_atual = '0'
                        lexema_atual = ""
                        coluna_atual -= 1
                case '4':
                    if not caractere.isdigit():
                        tokens_reconhecidos.append(
                            (linha_atual,  (coluna_atual - len(lexema_atual)), 'tk_int', lexema_atual))
                        estado_atual = '0'
                        lexema_atual = ""
                        coluna_atual -= 1
                case '5':
                    if caractere.isdigit():
                        estado_atual = '6'
                        lexema_atual += caractere
                    else:
                        erros.append(
                            (linha_atual, coluna_atual-1, 'float mal formatado'))
                        estado_atual = '0'
                        lexema_atual = ""
                        coluna_atual -= 1
                case '6':
                    if caractere.isdigit():
                        estado_atual = '6'
                        lexema_atual += caractere
                    elif caractere == 'e':
                        estado_atual = '7'
                        lexema_atual += caractere
                    else:
                        tokens_reconhecidos.append(
                            (linha_atual,  (coluna_atual - len(lexema_atual)), 'tk_float', lexema_atual))
                        estado_atual = '0'
                        lexema_atual = ""
                        coluna_atual -= 1
                case '7':
                    if caractere.isdigit():
                        estado_atual = '9'
                        lexema_atual += caractere
                    elif caractere == '-':
                        estado_atual = '8'
                        lexema_atual += caractere
                    else:
                        erros.append(
                            (linha_atual, coluna_atual, 'float mal formatado'))
                        estado_atual = '0'
                        lexema_atual = ""
                        coluna_atual -= 1
                case '8':
                    if caractere.isdigit():
                        estado_atual = '9'
                        lexema_atual += caractere
                case '9':
                    if caractere.isdigit():
                        estado_atual = '9'
                        lexema_atual += caractere
                    else:
                        tokens_reconhecidos.append(
                            (linha_atual,  (coluna_atual - len(lexema_atual)), 'tk_float', lexema_atual))
                        estado_atual = '0'
                        lexema_atual = ""
                        coluna_atual -= 1
                case '10':
                    if caractere.isdigit():
                        estado_atual = '11'
                        lexema_atual += caractere
                    else:
                        erros.append(
                            (linha_atual, (coluna_atual - len(lexema_atual)), 'data mal formatada'))
                        estado_atual = '0'
                        lexema_atual = ""
                        coluna_atual -= 1
                case '11':
                    if caractere.isdigit():
                        estado_atual = '12'
                        lexema_atual += caractere
                    else:
                        erros.append(
                            (linha_atual, (coluna_atual - len(lexema_atual)), 'data mal formatada'))
                        estado_atual = '0'
                        lexema_atual = ""
                        coluna_atual -= 1
                case '12':
                    if caractere == '/':
                        estado_atual = '13'
                        lexema_atual += caractere
                    else:
                        erros.append(
                            (linha_atual, (coluna_atual - len(lexema_atual)), 'data mal formatada'))
                        estado_atual = '0'
                        lexema_atual = ""
                        coluna_atual -= 1
                case '13':
                    if caractere.isdigit():
                        estado_atual = '18'
                        lexema_atual += caractere
                    else:
                        erros.append(
                            (linha_atual, (coluna_atual - len(lexema_atual)), 'data mal formatada'))
                        estado_atual = '0'
                        lexema_atual = ""
                        coluna_atual -= 1
                case '14':
                    if caractere.isdigit():
                        estado_atual = '15'
                        lexema_atual += caractere
                    else:
                        erros.append(
                            (linha_atual, (coluna_atual - len(lexema_atual)), 'data mal formatada'))
                        estado_atual = '0'
                        lexema_atual = ""
                        coluna_atual -= 1
                case '15':
                    if caractere.isdigit():
                        estado_atual = '16'
                        lexema_atual += caractere
                    else:
                        erros.append(
                            (linha_atual, (coluna_atual - len(lexema_atual)), 'data mal formatada'))
                        estado_atual = '0'
                        lexema_atual = ""
                        coluna_atual -= 1
                case '16':
                    if caractere == '_':
                        estado_atual = '17'
                        lexema_atual += caractere
                    else:
                        erros.append(
                            (linha_atual, (coluna_atual - len(lexema_atual)), 'data mal formatada'))
                        estado_atual = '0'
                        lexema_atual = ""
                        coluna_atual -= 1
                case '17':
                    if caractere.isdigit():
                        estado_atual = '18'
                        lexema_atual += caractere
                    else:
                        erros.append(
                            (linha_atual, (coluna_atual - len(lexema_atual)), 'data mal formatada'))
                        estado_atual = '0'
                        lexema_atual = ""
                        coluna_atual -= 1
                case '18':
                    if caractere.isdigit():
                        estado_atual = '19'
                        lexema_atual += caractere
                    else:
                        erros.append(
                            (linha_atual, (coluna_atual - len(lexema_atual)), 'data mal formatada'))
                        estado_atual = '0'
                        lexema_atual = ""
                        coluna_atual -= 1
                case '19':
                    if caractere.isdigit():
                        estado_atual = '20'
                        lexema_atual += caractere
                    else:
                        erros.append(
                            (linha_atual, (coluna_atual - len(lexema_atual)), 'data mal formatada'))
                        estado_atual = '0'
                        lexema_atual = ""
                        coluna_atual -= 1
                case '20':
                    if caractere.isdigit():
                        lexema_atual += caractere
                        tokens_reconhecidos.append(
                            (linha_atual,  (coluna_atual - len(lexema_atual)), 'tk_data', lexema_atual))
                        lexema_atual = ''
                        estado_atual = '0'
                    else:
                        erros.append(
                            (linha_atual, (coluna_atual - len(lexema_atual)), 'data mal formatada'))
                        estado_atual = '0'
                        lexema_atual = ""
                        coluna_atual -= 1
                case '21':
                    if caractere == 'x':
                        estado_atual = '22'
                        lexema_atual += caractere
                    else:
                        erros.append(
                            (linha_atual, coluna_atual-1, 'endereço mal formatado'))
                        estado_atual = '0'
                        lexema_atual = ""
                        coluna_atual -= 1
                case '22':
                    if 'A' <= caractere <= 'F' or caractere.isdigit():
                        estado_atual = '23'
                        lexema_atual += caractere
                    else:
                        erros.append(
                            (linha_atual, (coluna_atual - len(lexema_atual)), 'endereço mal formatado'))
                        estado_atual = '0'
                        lexema_atual = ""
                        coluna_atual -= 1
                case '23':
                    if 'A' <= caractere <= 'F' or caractere.isdigit():
                        estado_atual = '23'
                        lexema_atual += caractere
                    else:
                        tokens_reconhecidos.append(
                            (linha_atual, (coluna_atual - len(lexema_atual)), 'tk_endereço', lexema_atual))
                        estado_atual = '0'
                        lexema_atual = ""
                        coluna_atual -= 1
                case '24':
                    if caractere == '\n':
                        erros.append(
                            (linha_atual, coluna_atual-1, 'cadeia não fechada'))
                        estado_atual = '0'
                        lexema_atual = ""
                    elif caractere == '"':
                        lexema_atual += caractere
                        tokens_reconhecidos.append(
                            (linha_atual, (coluna_atual - len(lexema_atual)), 'tk_cadeia', lexema_atual))
                        estado_atual = '0'
                        lexema_atual = ""
                    else:
                        estado_atual = '24'
                        lexema_atual += caractere
                case '25':
                    if 'A' <= caractere <= 'Z':
                        estado_atual = '26'
                        lexema_atual += caractere
                    elif 'a' <= caractere <= 'z':
                        estado_atual = '28'
                        lexema_atual += caractere
                    else:
                        erros.append(
                            (linha_atual, coluna_atual-1, 'id ou reservada mal formatada'))
                        estado_atual = '0'
                        lexema_atual = ""
                case '26':
                    if 'a' <= caractere <= 'z':
                        estado_atual = '27'
                        lexema_atual += caractere
                    else:
                        tokens_reconhecidos.append(
                            (linha_atual, (coluna_atual - len(lexema_atual)), 'tk_id', lexema_atual))
                        estado_atual = '0'
                        lexema_atual = ""
                        coluna_atual -= 1
                case '27':
                    if 'A' <= caractere <= 'Z':
                        estado_atual = '26'
                        lexema_atual += caractere
                    else:
                        tokens_reconhecidos.append(
                            (linha_atual, (coluna_atual - len(lexema_atual)), 'tk_id', lexema_atual))
                        estado_atual = '0'
                        lexema_atual = ""
                        coluna_atual -= 1
                case '28':
                    if 'a' <= caractere <= 'z' or caractere == '_':
                        estado_atual = '28'
                        lexema_atual += caractere
                    else:
                        if verifica_reservadas(lexema_atual):
                            tokens_reconhecidos.append(
                                (linha_atual, (coluna_atual - len(lexema_atual)), ('tk_'+lexema_atual), ''))
                        else:
                            erros.append(
                                (linha_atual, (coluna_atual - len(lexema_atual)), 'palavra reservada não encontrada'))
                        estado_atual = '0'
                        lexema_atual = ""
                        coluna_atual -= 1
                case '29':
                    if caractere == '\n':
                        estado_atual = '0'
                    else:
                        estado_atual = '30'
                case '30':
                    if caractere == '\n':
                        estado_atual = '0'
                    else:
                        estado_atual = '30'
                case '31':
                    if caractere == '<':
                        estado_atual = '32'
                    elif caractere == '>':
                        tokens_reconhecidos.append(
                            (linha_atual, (coluna_atual - 2), 'tk_dif', ''))
                        estado_atual = '0'
                    elif caractere == '=':
                        estado_atual = '36'
                    else:
                        tokens_reconhecidos.append(
                            (linha_atual, (coluna_atual - 1), 'tk_menor', ''))
                        estado_atual = '0'
                        coluna_atual -= 1
                case '32':
                    if caractere == '<':
                        estado_atual = '33'
                        # guarda linha e coluna  em caso de erro de comentario nao fechado
                        coluna_erro = coluna_atual
                        linha_erro = linha_atual
                    else:
                        erros.append(
                            (linha_atual, (coluna_atual - 2), 'comentario mal formatado'))
                        estado_atual = '0'
                        coluna_atual -= 1
                case '33':
                    if caractere == '>':
                        estado_atual = '34'
                    else:
                        estado_atual = '33'
                        # verificando se chegou no fim do arquivo em caso de comentario não fechado
                        if linha_atual == tam_linha-1 and coluna_atual == tam_ultima_coluna-1:
                            erros.append((linha_erro, coluna_erro,
                                         'comentario não fechado'))
                            estado_atual = '0'
                            # volta linha e coluna para inico do comentario
                            linha_atual = linha_erro
                            coluna_atual = coluna_erro
                case '34':
                    if caractere == '>':
                        estado_atual = '35'
                    else:
                        estado_atual = '33'
                case '35':
                    if caractere == '>':
                        estado_atual = '0'
                    else:
                        estado_atual = '33'
                case'36':
                    if caractere == '=':
                        tokens_reconhecidos.append(
                            (linha_atual, coluna_atual-3, 'tk_atribuição', ''))
                        estado_atual = '0'
                    else:
                        tokens_reconhecidos.append(
                            (linha_atual, coluna_atual-2, 'tk_menor_eq', ''))
                        estado_atual = '0'
                        coluna_atual -= 1
                case '37':
                    if caractere == '=':
                        tokens_reconhecidos.append(
                            (linha_atual, coluna_atual-2, 'tk_maior_eq', ''))
                        estado_atual = '0'
                    else:
                        tokens_reconhecidos.append(
                            (linha_atual, coluna_atual-1, 'tk_maior', ''))
                        estado_atual = '0'
                        coluna_atual -= 1
                case '38':
                    if caractere == '=':
                        tokens_reconhecidos.append(
                            (linha_atual, coluna_atual-2, 'tk_igual', ''))
                        estado_atual = '0'
                    else:
                        erros.append((linha_atual, coluna_atual-1,
                                     'operador igual mal formatado'))
                        estado_atual = '0'
                        coluna_atual -= 1
                case _:
                    # caso defalt, apenas para melhor desenvolvimento do programa
                    print(f"erro: estado {estado_atual} invalido")

        linha_atual += 1  # atualização da linha atual

    return tokens_reconhecidos, erros


def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.readlines()  # Lê linhas do arquivo e armazena em uma lista
            # adicionando espaço no fim do arquivo para sempre ter um não digito para poder retornar o tk
            ultima_linha = len(conteudo)-1
            conteudo[ultima_linha] += ' '

        return conteudo
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
        return None


def verifica_reservadas(lexema_atual):
    reservadas = ['rotina', 'fim_rotina', 'se',
                  'senao', 'imprima', 'leia', 'para', 'enquanto']

    if lexema_atual in reservadas:
        return True
    else:
        return False


def mostrar_erros(conteudo_arquivo, lista_erros):
    print("\n\nLista de erros:\n")
    for num, linha in enumerate(conteudo_arquivo, start=1):
        # rstrip() remove o \n no final da linha
        print(f"[{num}]{linha.rstrip()}")

        for linha_erro, coluna_erro, codigo_erro in lista_erros:
            linha_erro += 1  # para mostrar a linha corretamente a partir de 1
            if linha_erro == num:
                marcação = '-' * (coluna_erro - 1) + '^'
                quant_digitos = len(str(num))
                print(f"{' ' * (quant_digitos+2)}{marcação}")

        for linha_erro, coluna_erro, codigo_erro in lista_erros:
            linha_erro += 1
            if linha_erro == num:
                print(f"erro linha {linha_erro} coluna {
                      coluna_erro}: {codigo_erro}")

    print()  # Imprime uma linha em branco no final


def mostrar_somatorio_tokens(lista_tokens):
    # Dicionário para contar a frequência de cada token
    frequencia_tokens = {}

    # Contagem dos tokens
    for _, _, token, _ in lista_tokens:
        if token in frequencia_tokens:
            frequencia_tokens[token] += 1
        else:
            frequencia_tokens[token] = 1

    # Ordenação do dicionário pela quantidade de usos (valor)
    tokens_ordenados = sorted(
        frequencia_tokens.items(), key=lambda x: x[1], reverse=True)

    # Impressão dos resultados
    print("\n\nSomatório de tokens reconhecidos:\n")
    print("{:<15} | {:<10}".format("token", "usos"))
    for token, frequencia in tokens_ordenados:
        print("{:<15} | {:<3}".format(token, frequencia))


# Nome do arquivo a ser lido
nome_arquivo = "exemplo2.cic"

# Lê o arquivo e armazena seu conteúdo
conteudo_arquivo = ler_arquivo(nome_arquivo)

# Verifica se o conteúdo do arquivo foi lido com sucesso
if conteudo_arquivo is not None:
    lista_tk, erro = analizador_lexico(conteudo_arquivo)
    print("\n\nResultado da análise léxica:\n")

    # mostra lista de tokens reconhecidos
    print("{:>4} | {:>4} | {:<15} | {:<10}".format(
        "lin", "col", "token", "lexema"))
    for linha, coluna, token, lexema in lista_tk:
        print("{:>4} | {:>4} | {:<15} | {:<10}".format(
            linha+1, coluna, token, lexema))
    # mostra somatorio de tokens reconhecidos
    mostrar_somatorio_tokens(lista_tk)

    # mostra codigo fonte com identificação de erros
    mostrar_erros(conteudo_arquivo, erro)

else:
    exit()
