import random

def sorteio_bingo():
    """Simula o sorteio de bolas de bingo (1 a 75)."""

    # Cria uma lista com todos os números de bingo (1 a 75)
    bolas_disponiveis = list(range(1, 76))
    
    # Inicializa uma lista para armazenar os números sorteados
    bolas_sorteadas = []
    
    print("--- 🎰 Início do Sorteio de Bingo (Números 1 a 75) 🎰 ---")
    print(f"Total de bolas para sortear: {len(bolas_disponiveis)}")

    # Loop principal para sortear as bolas até que acabem
    input("\nPressione **Enter** para sortear a primeira bola...")
    
    while bolas_disponiveis:
        # 1. Escolhe uma bola aleatoriamente da lista de disponíveis
        bola_sorteada = random.choice(bolas_disponiveis)
        
        # 2. Remove a bola sorteada da lista de disponíveis
        bolas_disponiveis.remove(bola_sorteada)
        
        # 3. Adiciona a bola sorteada à lista de sorteadas (para registro)
        bolas_sorteadas.append(bola_sorteada)
        
        # 4. Exibe o resultado do sorteio
        print(f"\n✨ **BOLA SORTEADA:** **{bola_sorteada}**")
        print(f"Bolas sorteadas até agora ({len(bolas_sorteadas)}): {bolas_sorteadas}")
        
        # 5. Pausa e espera pela ação do usuário
        if bolas_disponiveis:
            input("\nPressione **Enter** para sortear a próxima bola...")
        else:
            print("\n--- 🛑 Fim do Sorteio. Todas as bolas foram sorteadas! 🛑 ---")

    return bolas_sorteadas

# Executa a função
sorteio_bingo()
