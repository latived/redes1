# redes1
projeto redes 1 \[ic/ufal] \[prazo: 17/05]

regras:
1. deve-se obrigatoriamente utilizar os conceitos de socket, considerando funções primitivas como:
  * socket(), 
  * read() ou recv(), 
  * write()

obs: dependendo da linguagem utilizada, o nome dessas funções pode mudar.

2. uso de thread é bastante encorajado.

# info sobre projeto

**não pode ser chat, nem jogo da velha, nem mais o que?**

- [x] definir o que será (joguin? app fodinha?)
- [ ] definir protocolo usado
- [ ] definir funcionalidades
- [ ] definir as issues e milestones

# será um joguin de xadrez via cli/gui

- notação usada é a _algébrica_
  [wiki](https://en.wikipedia.org/wiki/Algebraic_notation_(chess))
  - cada quadrado tem sua própria identificação: \[a-h, coluna/file; 1-8,
    linhas/rank]
  - cada peça (exceto peão) é identificada por sua primeira letra, em
    maiúsculo (em inglês msm aqui): K (king), Q (queen), etc.
    - peão sao identificados pela ausência de tal letra.
  - cada movimento é indicado pela letra (maiúscula) da peça + coordenada do
    quadrado: exemplo, movendo bispo para e5 -> _Be5_
  - cada captura é indicada por um _x_ antes do destino: exemplo, bispo captura
    peça em e5 -> _Bxe5_
    - no caso do peão, a coluna (file) indica qual peão captura qual: **exd5**
    - capturas _en passant_ possuem o sufixo **e.p** ao fim, e o file
      indicado é o de destino (não do peão capturado): **exd6e.p.**
    - se duas ou mais peças podem mover-se para o mesmo quadrado, a
      identificação é incrementada por:
        1. coluna/file de saída (se diferirem); ou
        2. linha/rank de saída (files iguais, ranks diferentes); ou
        3. ambos file e rank (casos raros, quando peões são promovidos).
        4. exemplos:
            - Cavalos em **g1** e **d2** podem mover para **f3**, então
            temos o movimento especificado como **Ngf3** ou **Ndf3**.
            - Cavalos em **g5** e **g1**, os movimentos são **N5f3** ou
              **N1f3**. 
            - Duas torres em **d3** e **h5** podem se mover para **d5**, mas
              torre em **d3** que se move: **Rdd5**
            - lembrando que um _x_ deve ser inserido pra indicar captura:
              **N5xf3**
  - promoções tem a peça para qual vai ser promovida no final, após **=**: **e8=Q**, onde _Q_
    indica _Queen_
  - oferta de empate: **=**
  - _castling_ -> **0-0** (lado do rei) ou **0-0-0** (lado da rainha)
    - no lugar o **0** pode ser usar **O**
  - _check_ -> **+** no final da notação do movimento (**++** para _double
    check_)
  - _checkmate_ -> **#**
  - _end of game_ -> **1-0** no final de um movimento para indiciar que os
    Brancos ganharam, **0-1** para indicar que os Pretos ganharam; e ½–½ indica
    um empate
    - a indicação de fim de jogo pode ser feita sem movimento (desistência, por
      exemplo)

# definir protocolo

**lembra que deve ser multithread**

vejamos... jogo de xadrez entre 2 apenas, mas pode ter suporte pra equipe (2x2)

protocolo explícito+implícito (considerando jogo iniciado)
    - explícito no início do jogo (antes da partida): 
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
            - EXIT <game_id> [pode ser 1-0/0-1 pra entregar o jogo msm?]
            - QUIT
                
        - 

## cliente
    - abre cliente, ja conecta com servidor
## servidor
    - usa thread para cada requisição
