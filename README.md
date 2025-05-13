# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/images/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Cap 1 - A consolidação de um sistema

## 👨‍👩 Grupo

Grupo de número <b>5</b> formado pelos integrantes mencionados abaixo.

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/cirohenrique/">Ciro Henrique</a> ( <i>RM559040</i> )
- <a href="javascript:void(0)">Enyd Bentivoglio</a> ( <i>RM560234</i> )
- <a href="https://www.linkedin.com/in/marcofranzoi/">Marco Franzoi</a> ( <i>RM559468</i> )
- <a href="https://www.linkedin.com/in/rodrigo-mazuco-16749b37/">Rodrigo Mazuco</a> ( <i>RM559712</i> )

## 👩‍🏫 Professores:

### Tutor(a) 
- <a href="https://www.linkedin.com/in/leonardoorabona/">Leonardo Ruiz Orabona</a>

### Coordenador(a)
- <a href="https://www.linkedin.com/in/profandregodoi/">André Godoi</a>

## 📜 Descrição

<b>Referência</b>: https://on.fiap.com.br/mod/assign/view.php?id=486416&c=13085

Cada versão do projeto está distribuída em um repositório devido ao avanço de suas funcionalidades. Portanto, em cada item abaixo, serão feitas referências para esses repositórios para uma melhor análise.

> ### Versão 1

A primeira versão do projeto está disponível no repositório [fase 1](https://github.com/RM559712/fase1).

Nesta fase, foram desenvolvidas funcionalidades sem integração com banco de dados relacional. Algumas funcionalidades utilizam uma estrutura <i>json</i> para armazenamento temporário dos dados, localizada no diretório "/data".

A principal funcionalidade nesta versão é a execução de cálculos para auxílio no plantio de determinadas culturas pré-definidas, que são: Café, Milho, Arroz, Soja e Cana-de-açúcar. 

A partir da cultura selecionada, o usuário pode realizar os seguintes cálculos:

1. Cálculo para área de plantio baseado em espaçamentos
2. Cálculo para área de plantio baseado em densidade
3. Cálculo para quantidade de ruas baseado em área de plantio
4. Cálculo para quantidade de plantas baseado em quantidade de ruas
5. Cálculo para quantidade de insumos baseado em quantidade de ruas
6. Cálculo para quantidade de insumos baseado em taxa de aplicação

Para cada cultura selecionada, são utilizados parâmetros específicos para que cada cálculo seja executado com precisão.

No menu principal, é possível ainda visualizar um histórico de cálculos executados para cada cultura e tipo de cálculo. Além disso, é possível editar um cálculo já realizado utilizando outros parâmetros e também a exclusão caso seja necessário.

Também são disponibilizadas outras funcionalidades para auxílio no plantio, como a visualização de um relatório dos cálculos executados e também a visualização de um relatório meteorológico para áreas específicas, ambas utilizando a linguagem R.

> ### Versão 2

A segunda versão do projeto está disponível no repositório [fase 2](https://github.com/RM559712/fase2).

Nesta fase, houve um avanço tecnológico na qual passou a utilizar uma estrutura de banco de dados relacional com Oracle.

A principal funcionalidade nesta versão é a execução de análises para simulação de alertas meteorológicos, com o intuito de auxiliar no plantio de culturas previamente cadastradas, de acordo com regiões especificadas pelo usuário.

O usuário pode cadastrar diferentes culturas, definindo parâmetros necessários para que o seu plantio ocorra da melhor maneira possível. Dessa forma, é possível simular plantios de uma ou mais culturas em diferentes regiões do planeta, respeitando parâmetros padrões ou específicos para cada região.

Os parâmetros que podem ser definidos no cadastro das culturas são:

1. <strong>Temperatura ideal</strong>: pode ser definido um range contendo temperatura mínima e/ou máxima;
2. <strong>Umidade ideal</strong>: pode ser definido um range contendo umidade mínima e/ou máxima;
3. <strong>Velocidade do vento ideal</strong>: pode ser definido um range contendo velocidade mínima e/ou máxima;
4. <strong>Quantidade de chuva ideal</strong>: pode ser definido um range contendo quantidade mínima e/ou máxima;

Com as culturas previamente cadastradas e configuradas, é possível executar simulações de alertas meteorológicos, bastando informar a região desejada.

Os parâmetros que podem ser definidos para execução das simulações são:

1. <strong>Cidade, estado/província e país</strong>: esse formato é mais convencional, devendo ser informado no padrão [nome_cidade],[sigla_estado_província],[sigla_país] ( ex.: São Paulo,SP,BR , Rio grande do sul,RS,BR , Noventa Vicentina,Ve,IT , etc. );
2. <strong>Latitude e longitude</strong>: esse formato é mais específico, devendo ser informado no padrão [latitude], [longitude] ( ex.: 43.98882933123789, 18.180055506117746 , -21.786002807359086, -46.56287094468699, 45.41024449730194, 11.877725912383978 , etc. );

Ao final do processo, é gerado um relatório detalhando as condições meteorológicas para cada um dos parâmetros utilizados no cadastro da cultura, incluindo uma conclusão ao final informando se as condições para plantio estão favoráveis ou desfavoráveis, considerando os próximos 5 dias a partir da data e hora de execução e com intervalos de 6 horas.

> ### Versão 3

A terceira versão do projeto está disponível no repositório [fase 3](https://github.com/RM559712/fase3_cap1).

Nesta fase, foram adicionadas funcionalidades que auxiliam ainda mais no plantio, como o cadastro de culturas, cadastro e configuração de plantações, cadastro e configuração de sensores de medição, funcionalidade para inicialização de irrigação manual ou automática através das configurações definidas nas plantações em conjunto com medições meteorológicas para a região e, por fim, visualização do histórico de medições efetuadas através dos sensores cadastrados e configurados.

Os parâmetros que podem ser definidos no cadastro das plantações são:

1. <strong>Temperatura ideal</strong>: pode ser definido um range contendo temperatura mínima e/ou máxima;
2. <strong>Umidade ideal</strong>: pode ser definido um range contendo umidade mínima e/ou máxima;
3. <strong>Luminosidade ideal</strong>: pode ser definido um range contendo nível mínimo e/ou máximo;
4. <strong>Radiação solar ideal</strong>: pode ser definido um range contendo nível mínimo e/ou máximo;
5. <strong>Salinidade ideal</strong>: pode ser definido um range contendo nível mínimo e/ou máximo;
6. <strong>pH ideal</strong>: pode ser definido um range contendo nível mínimo e/ou máximo;
7. <strong>Latitude</strong>: pode ser definida a latitude da região da plantação;
8. <strong>Longitude</strong>: pode ser definida a longitude da região da plantação;
9. <strong>Quantidade de horas para verificação de chuva</strong>: pode ser definido uma quantidade de horas;
10. <strong>Quantidade média máxima de chuva</strong>: pode ser definido uma quantidade média de chuva;

Os tipos de sensores que podem ser cadastrados são:

1. Sensor de Temperatura do solo;
2. Sensor de Umidade do solo;
3. Sensor de luminosidade;
4. Sensor de radiação;
5. Sensor de salinidade do solo;
6. Sensor de pH do solo;

Com as culturas devidamente cadastradas e associadas às suas plantações, é possível armazenar medições a partir de sensores, nas quais podem utilizar a API do sistema, ou manualmente caso a conexão entre o sensor e a API apresente problemas. Sempre que uma medição é armazenada, um processo de irrigação pode ser inicializado automaticamente, levando em consideração as configurações da plantação em conjunto com as medições meteorológicas da região, nas quais são fornecidas através dos parâmetros latitude e longitude configurados também no cadastro da plantação. Existe também a possibilidade de uma irrigação ser inicializada manualmente para situações específicas nas quais independem do resultado da medição de sensores.

Ao final do processo, é possível visualizar um histórico das irrigações executadas nas plantações, onde são disponibilizadas informações como a origem do processo (<i>manual ou automática</i>), quantidade de água utilizada, status de execução (<i>em execução ou finalizado</i>) e data e hora de início e término dependendo do status.

> ### Versão 4

A quarta versão do projeto está disponível no repositório [fase 4](https://github.com/RM559712/fase4_cap1).

Nesta fase, foram adicionadas melhorias técnicas no sistema visando diminuir o tempo de processamento tanto no armazenamento das medições, que podem ser efetuadas por API ou manualmente, quanto na listagem do histórico das irrigações executadas nas plantações, e também a opção para geração de gráfico de dispersão a partir do histórico de execução das irrigações, na qual pode ser visualizado tanto em formato padrão a partir do <i>prompt</i> como também em formato <i>web</i> a partir da biblioteca Streamlit.

> ### Versão 5

A quinta versão do projeto está disponível no repositório [fase 5](https://github.com/RM559712/fase5_cap1).

Nesta fase, o projeto seguiu para o contexto de infraestrutura. Foram feitas diversas análises no mercado até concluírmos que os serviços prestados pela AWS possuem o melhor custo-benefício.

Os principais pontos que fizeram com que escolhessemos a AWS são:

- Escalabilidade 
- Redundância e resiliência
- Segurança, compliance e regulamentações
- Suporte técnico e manutenção

> ### Versão 6

A sexta versão do projeto está disponível no repositório [fase 6](https://github.com/RM559712/fase6_cap1).

Nesta fase, foram efetuadas comparações técnicas entre os modelos YOLOv5 e YOLOv8 e CNN sequencial para detecção de objetos. 

Na execução dos testes, foram utilizados os modelos YOLOv5 (<i>60 e 80 épocas</i>), YOLOv8 (<i>60 e 80 épocas</i>) e CNN Sequencial (<i>60 e 80 épocas</i>). 

Diante dos testes efetuados, foram apontados:

- <strong>YOLOv5</strong>: Estrutura modular, fácil de customizar, excelente documentação;
- <strong>YOLOv8</strong>: Setup simplificado com comando único, integração com Ultralytics;
- <strong>CNN</strong>: Implementação simples ótima para prototipação;

> ### Versão 7

A sétima versão do projeto está disponível no repositório [fase 7](https://github.com/RM559712/fase7_cap1).

Nesta fase, foram adicionadas melhorias que visam principalmente auxiliar o gerenciamento das plantações quando irrigações forem inicializadas ou finalizadas. Agora, sempre que uma medição for cadastrada no sistema a partir de algum sensor instalado nas plantações ou quando um processo de irrigação for inicializado a partir das configurações da plantação e das medições meteorológicas da região, uma notificação será enviada para o setor responsável pelo gerenciamento.

Dessa maneira, o setor responsável pelo gerenciamento receberá as seguintes informações:

- <strong>Cadastro de medição</strong>: serão enviadas informações relacionadas à medição;
- <strong>Inicialização de irrigação</strong>: serão enviadas informações relacionadas ao início da irrigação;
- <strong>Finalização de irrigação</strong>: serão enviadas informações relacionadas ao término da irrigação;

O componente responsável pelo envio de notificações utilizará o serviço da AWS.

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

1. <b>assets</b>: Diretório para armazenamento de arquivos complementares da estrutura do sistema.
    - Diretório "images": Diretório para armazenamento de imagens.

2. <b>config</b>: Diretório para armazenamento de arquivos em formato <i>json</i> contendo configurações.

3. <b>document</b>: Diretório para armazenamento de documentos relacionados ao sistema.

4. <b>scripts</b>: Diretório para armazenamento de scripts.

5. <b>src</b>: Diretório para armazenamento de código fonte do sistema.

6. <b>tests</b>: Diretório para armazenamento de resultados de testes.
	- Diretório "images": Diretório para armazenamento de imagens relacionadas aos testes efetuados.

7. <b>README.md</b>: Documentação do projeto em formato markdown.

<i><strong>Importante</strong>: A estrutura de pastas foi mantida neste formato para atender ao padrão de entrega dos projetos.</i>

## 🔧 Como executar o código

Como se trata de uma versão em formato <i>prompt</i>, para execução das funcionalidades, os seguintes passos devem ser seguidos:

1. Utilizando algum editor de código compatível com a linguagem de programação Python (<i>VsCode, PyCharm, etc.</i>), acesse o diretório "./src/prompt".
2. Neste diretório, basta abrir o arquivo "main.py" e executá-lo.

Alguns módulos do sistema podem ser executados em formato <i>web</i> utilizando Streamlit conforme descritos em [Descrição](https://github.com/RM559712/fase4_cap1?tab=readme-ov-file#-descri%C3%A7%C3%A3o). Para acessá-los, os seguintes passos devem ser seguidos:

1. Utilizando algum editor de código compatível com a linguagem de programação Python (<i>VsCode, PyCharm, etc.</i>), acesse o diretório "./src/web/modules/{nome_do_modulo}".
2. Neste diretório, basta identificar o arquivo desejado e executar o comando `streamlit run {nome_do_arquivo}.py`.

Para essa versão não são solicitados parâmetros para acesso como por exemplo <i>username</i>, <i>password</i>, <i>token access</i>, etc.

## 🗃 Histórico de lançamentos

* 1.0.0 - 23/05/2025

## 📋 Licença

Desenvolvido pelo Grupo 5 para o projeto da fase 6 (<i>Cap 1 - A consolidação de um sistema</i>) da <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a>. Está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>