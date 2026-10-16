estoque = [
    ["Pão", 10], # Linha 0
    ["Hambúrguer", 2], # Linha 1
    ["Queijo", 15], # Linha 2
    ["Carne", 12], # Linha 3
    ["Refrigerante", 9] # Linha 4
]    # Coluna 0  ,  1   
fila_entrega = []
carrinho_cliente = []

# Loop de pedidos e estoque
for insumo in estoque:
    

    # Variáveis de quantidade e produto no estoque
    ingrediente_estoque = insumo[0]
    quantidade_estoque = insumo[1]
    # Verificador de quantidade no estoque
    if quantidade_estoque < 5:
        print(f"ALERTA: Estoque baixo de {ingrediente_estoque}, apenas {quantidade_estoque} encontrado(s) no estoque!")
        pass

# Entrada e armazenamento dos dados do cliente
cliente_nome = input("Digite seu nome para começar seu pedido: ").strip().lower().capitalize()
if cliente_nome not in fila_entrega:
    fila_entrega.append(cliente_nome)

# Entrada do pedido e exibição do cardápio ao cliente
print(f"Nosso cardápio:\n- {estoque[1][0]}\n- {estoque[4][0]}")
pedido_cliente = input(f"O que gostaria de pedir hoje {cliente_nome}? ").lower().strip()

disponivel = True

while True:      
    # Condição para encerrar o programa
    if pedido_cliente == "meu carrinho":
        if len(carrinho_cliente) > 0:
            print("No seu carrinho já está incluso:")
            for item in carrinho_cliente:
                match item:
                    case "Hambúrguer" | "Refrigerante" | "Batata Frita" | "Sorvete":
                        print(f"- {item}")
                        pedido_cliente = input("\nGostaria de pedir algo mais?(digite SAIR para finalizar)  ").lower().strip()
        else:
            print("Carrinho vazio!\n")
            pedido_cliente = input(f"Gostaria de começar a pedir? ").lower().strip()

    elif pedido_cliente == "sair":
        break

    match pedido_cliente:
        # Processamento: Cliente pediu hamburguer e será removido os ingredientes do estoque
        case "hamburguer" | "hambúrguer" | "burguer" | "burger":
            
            # Se houver falta de ingrediente
            for ingrediente in estoque:
                if ingrediente[0] in ["Pão", "Queijo", "Carne"] and ingrediente[1] < 1:
                    print(f"O item {ingrediente} está indisponível no momento! Sentimos muito...")
                    disponivel = False
                    break

            # Se os ingredientes estiverem disponíveis
            if disponivel:
                for ingrediente in estoque:
                    # Remove os ingredientes para criar o Hambúrguer
                    if ingrediente[0] in ["Pão", "Queijo", "Carne"]:
                        ingrediente[1] -= 1

                    # Hambúrguer é adicionado no estoque e então removido
                    if ingrediente[0] == "Hambúrguer":
                        ingrediente[1] += 1
                        ingrediente[1] -= 1
                        carrinho_cliente.append("Hambúrguer")
                        
            print(f"Seu {estoque[1][0]} está sendo preparado!")
        
        case "refrigerante" | "refri":
            for ingrediente in estoque:
                
                if ingrediente[0] in ["Refrigerante"] and ingrediente[1] < 1:
                    print(f"O item {ingrediente} está indisponível no momento! Sentimos muito...")
                    disponivel = False
                    break

            if disponivel:
                    for ingrediente in estoque:
                        if ingrediente[0] == "Refrigerante":
                            ingrediente[1] -= 1
                            carrinho_cliente.append("Refrigerante")
            print(f"Seu {estoque[4][0]} foi incluído no seu pedido!")
        
        case _:
            print("Pedido não encontrado em nosso menu! Por favor, escolha algo que estiver em nosso cardápio!")

    pedido_cliente = input("Gostaria de pedir algo mais?(digite SAIR para finalizar)  ").lower().strip()
fila_entrega.pop(0)
print("Obrigado por pedir conosco!")

"""
Remover o código todo de dentro do for porque não faz sentido algum
Colocar o for dentro do match/case pra não ter que dar "copia e cola"
da redução dos itens no estoque
"""
    