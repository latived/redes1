# Redes 1 + Teste de Software (ainda não iniciado)
projeto redes 1 \[ic/ufal] \[prazo: 17/05]

regras:
1. deve-se obrigatoriamente utilizar os conceitos de socket, considerando funções primitivas como:
  * socket(), 
  * read() ou recv(), 
  * write()

obs: dependendo da linguagem utilizada, o nome dessas funções pode mudar.

2. uso de thread é bastante encorajado.
ado a tempo. contém erros.# info sobre projetoado a tempo. contém erros.# info sobre projeto

*STATUS: não completado a tempo. contém erros.*

- [x] definir o que será
    - Jogo de xadrez via console (linha de comando)
- [x] definir protocolo usado
    - TCP
    - AÇÕES (ver próxima seção)
- [ ] definir funcionalidades
- [ ] definir as issues e milestones


# Ações

Mensagens:
    - criador da sala
        - CREATE <type>, onde _<type>_ indica o tipo do jogo (1x1, único; ou 2x2, equipe [pode ser abreviado: 1 ou 2])
            - tal comando retorna um ID para o jogo (game_id)
        - ADD <player_id> <team>=[creator,other]
        - REMOVE <player_id> [future]
        - START <game_id> 
            - movimentos são implícios, exceto para trocar de partida on the fly 
            (isso nao faz o jogador sair da partida, mas apenas troca o
            foco)
            - FOCUS <game_id> troca o foco da partida tal para aquela com
                <game_id> [future]

            - CONF PLAY <game_id> <option>=<value> [future]
            - <game_id> é o id da partida criada 
            - <option> pode ser
                - time_move=<n>, onde <n> é em segundos (60 até 600, 1 a 10
                    minutos), para cada move
                - time_play=<n>, mesmo acima só que para partida
                - start_with=[white,black], indica se o time do criador vai
                    começar ou não o jogo
                - team_name=<string>
    - qualquer jogador: 
        - PLAY <game_id> para se conectar à sala da partida 
        - SHOW <game_id> para mostrar o tabuleiro da partida (que está
            conectada) [future?]
        - LIST <game> [future]
            - my_games, pra listar os jogos conectados
            - all_games, para listar jogos criados
            - open_games, para listar jogos disponíveis
            - closed_games, para listar jogos terminados (e possivelmente
                visualizar movimentos feitos na partida)
        - CONF <option>=<value>, onde temos [future]
                - max_games=<n>, onde o jogador configura o total de jogos 
                pode estar conectado (padrão é max_games=2)
                - username=<new_username> (padrão player_<id>, tal que <id> é
                definido pela ordem de conexão com servidor/jogo)
        - HELP [future]
        - EXIT <game_id> [pode ser 1-0/0-1 pra entregar o jogo msm]
        - QUIT

## Observações

O delimitador é o *espaço em branco*. Em algumas resptas do servidor para o
cliente são usados outros delimitadores, como a quebra de linha.

A ideia do jogo era poder criar partidas no terminal, conectar-se e
jogá-las--com a possibilidade pausá-las e focar em outra partida no momento.

Cada turno seria de um time específico (das peças brancas, ou das peças
pretas), usando a notação algébrica de xadrez.

Uma das funcionalidades seria poder visualizar jogos _curses_, importando
arquivos de formato PGN e afins.

Apenas CREATE, START, PLAY e QUIT foram implementados. No entanto, bugs
apareceram que comprometeram o funcionamento adequado de tais mensagens.
