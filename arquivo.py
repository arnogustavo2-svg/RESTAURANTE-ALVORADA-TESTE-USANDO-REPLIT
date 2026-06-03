esc1 = ""
esc2 = ""


def login():
    global esc1
    print("=" * 30)
    print("Bem-vindo ao Restaurante Alvorada!")
    print("\nO que precisa?")
    print("=" * 30)
    esc1 = input("RESERVAR (sim/não): ").lower()
    escc = input("DELIVERY(sim/não)").lower()
    if escc == "sim":
        #AQUI QUERO QUE O CLIENTE POSSA PEDIR OS PRATOS OU MARMITAS, E QUE TENHA UMA OPÇÂO DE VER O CARRINHO. AI ENTRA O:
        menu_entrega()
    print("=" * 30)
    if esc1 == "sim":
        reserva()
    elif esc1 in ("nao", "não"):
        sair()
    else:
        print("Por favor, selecione uma opção válida.")
        login()



def sair():
    print("=" * 30)
    print("DESEJA SAIR?")
    sai = input("(sim/não): ").lower()
    if sai == "sim":
        print("SAINDO...")
    elif sai in ("não", "nao"):
        print("VOLTANDO AO MENU...")
        login()
    else:
        print("Por favor, selecione uma opção.")
        sair()



def reserva():
    global esc2
    print("=" * 30)
    print("Antes, preciso de algumas informações:")
    nome = input("NOME COMPLETO: ")
    cpf = input("CPF: ")
    telefone = input("TELEFONE")
    idade = input("IDADE: ")
    quant = input("QUANTIDADE DE PESSOAS: ")
    dia = input("DIA DA RESERVA: ")
    print("=" * 30)

    while True:
        print(f"\nRESUMO GERAL:")
        print("=" * 30)
        print(f"NOME COMPLETO: {nome}")
        print(f"CPF: {cpf}")
        print(f"TELEFONE: {telefone}")
        print(f"IDADE: {idade}")
        print(f"QUANTIDADE DE PESSOAS: {quant}")
        print(f"DIA DA RESERVA: {dia}")
        print("=" * 30)
        esc3 = input("DESEJA CONFIRMAR? (sim/não): ").lower()
        if esc3 == "sim":
            print("RESERVA CONFIRMADA!")
            break
        elif esc3 in ("nao", "não"):
            esc4 = input("DESEJA VOLTAR AO MENU? (sim/não): ").lower()
            if esc4 == "sim":
                login()
                break
            elif esc4 in ("nao", "não"):
                reserva()
                break
            else:
                print("Por favor, selecione uma opção.")
        else:
            print("Por favor, selecione uma opção.")



def menu_ADM():
    #AQUI EU QUERO QUE CADA FUNÇÂO A SEGUIR TENHA UMA ABA.aqui é só de adm que vai poder mudar os valores, adicionar ou remover coisas do site do cliente. O MENU É A PRIMEIRA ABA.
    #ABAS DENTRO DO MENU:
    #HORÁRIOS(DIAS DE SEMANA É BUFFET E FINAIS DE SEMANA É RODÍZIO)
    pratos = [] #<QUERO QUE O ADM POSSA COLOCAR OS PRATOS DO BUFFET AQUI E QUE POSSA EXPORTAR IMAGENS UTILIZANDO APPEND
    #O BUFFET PODE TER ENTREGA. QUERO QUE FAÇA ABAS CERTINAS SOMENTE SE NESCEssário
    rodizio = valor_rodizio
    valor_rodizio = input("VALOR DO RODIZIO:")
    buffet = input("VALOR BUFFET")
    pagamentos = "cartão","dinheiro","pix"
    


#QUERO QUE O VALOR DO PRATO TENHA TAMBEM A TAXA DE ENTREGA sE O CLIENTE SELECIONAR SIM.
def pagamento():
    pagamentos = input("")#<AQUI É O CLIENTE QUE ESCOLHE O PAGAMENTO.
    if pagamentos == "cartão" or "cartao" or "dinheiro" or "pix":
    
    else: 
        ess = input  ("DESEJA IR AO MENU?(SIM/NÂO)").lower()
        if ess == "sim":
            login()
        elif ess == "não" or "nao":
            pagamento()          
        else:
            print("POR FAVOR, SELECIONE UMA OPÇÃO.")
            pagamento()
                




def menu_entrega():
    taxa = 7
    esc_entrega = input("DESEJA ENTREGA?(SIM/NÃO)").lower()
    if esc_entrega == "sim":
        print("TAXA ADICIONAL DE R$7,00")
        endereço()
    elif esc_entrega == "não" or "nao":
        pagamento()
    else:
        print("SELECIONE UMA OPÇÃO")
        menu_entrega()
        



def endereço():
            info_endereco = input("ENDEREÇO DE ENTREGA.")
            info_bairro = input("BAIRRO")
            info_complemento = input("COMPLEMENTO")
            if not info_complemento:
                info_complemento = "NÃO INFORMADO"
            print(f"VISÃO GERAL:")
            print(f"ENDEREÇO DE ENTREGA:{info_endereco}")
            print(f"BAIRRO:{info_bairro}")
            print(f"COMPLEMENTO:{info_complemento}")
            print("CONFIRMAR?(sim/não)")
            essa = input("SIM/NÂO").lower()
            if essa == "sim":
                pagamento()
            else:
                endereço()
            


            
    
login()
