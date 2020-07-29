# Versão em português
## Protótipo de validação
Este repositório traz o protótipo desenvolvido como forma de validação para a proposta de arquitetura que visa balizar o desenvolvimento de softwares para gerência de firewalls em redes híbridas.

## Instalação do software
Faça o download do projeto utilizando git

`git clone https://github.com/mmfiorenza/sbseg_version`

Acesse a pasta do projeto.

Execute o script "prepares_environment.sh" para instalação das dependências

`sudo bash utils/prepares_environment.sh`


## Uso
Execute os módulos tradutores utilizando o script “run_application.sh”

```bash
sudo bash utils/run_application.sh
```

Execute a API para recepção das intenções

```bash
python3.7 api.py
```

Utilize o metodo HTTP POST (por exemplo: comando curl) para enviar a intenção em NILE para a aplicação:

```bash
curl --data-binary "@intent.txt" -X POST http://localhost:5000
```
Exemplos das três intenções suportadas estão disponíveis na pasta “examples”.


## Suporte
Este software não possui nenhuma forma de suporte. Caso tenha alguma dúvida favor enviar um e-mail para mauriciofiorenza.aluno@unipampa.edu.br.


## Creditos
* Desenvolvimento: Maurício Fiorenza
* Orientação: Diego Kreutz



# English version
## Validation prototype
This repository presents the prototype developed as a form of validation for the proposed architecture that aims to guide the development of software for firewall management in hybrid networks.


## Software installation
Download the project using git

`git clone https://github.com/mmfiorenza/intent_translator.git`

Access the project folder.

Run the "prepares_environment.sh" script to install the dependenciess

`sudo bash utils/prepares_environment.sh`


## Usage
Run the translator modules using the script “run_application.sh”

```bash
sudo bash utils/run_application.sh
```

Run the API to receive intentions

```bash
python3.7 api.py
```

Use the HTTP POST method (for example: curl command) to send the intention in NILE to the application:

```bash
curl --data-binary "@intent.txt" -X POST http://localhost:5000
```
Examples of the three supported intentions are available in the “examples” folder.


## Support
This software does not have any form of support. If you have any questions please send an email to mauriciofiorenza.aluno@unipampa.edu.br.


## Credits
* Development: Maurício Fiorenza
* Mentor: Diego Kreutz
