# PyTCPScan <img src="https://github.com/werdelesmarcio/PyTCPScan/blob/main/Images/icon.png" width=25> 

[![Maintainability](https://api.codeclimate.com/v1/badges/eefb5e71110a85b4ac3f/maintainability)](https://codeclimate.com/github/werdelesmarcio/PyTCPScan2/maintainability)   [![Build status](https://ci.appveyor.com/api/projects/status/050o62vq1v03wv4c?svg=true)](https://ci.appveyor.com/project/werdelesmarcio/pytcpscan2)   [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=werdelesmarcio_PyTCPScan2&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=werdelesmarcio_PyTCPScan2)   [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=werdelesmarcio_PyTCPScan2&metric=bugs)](https://sonarcloud.io/summary/new_code?id=werdelesmarcio_PyTCPScan2)   <img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/werdelesmarcio/PyTCPScan2">   <img alt="GitHub" src="https://img.shields.io/github/license/werdelesmarcio/PyTCPScan2">   <img alt="Twitter" src="https://img.shields.io/twitter/url?label=gh05tb0y&logo=twitter&logoColor=green&style=social&url=https%3A%2F%2Ftwitter.com%2Fc4s3_w1nt3rmut3">

_Repositório para a aplicação PyTCPScan._

## PyTCPScan
Consiste em uma aplicação voltada para sistemas **GNU/Linux** e tem como finalidade, a 
execução de scaner de portas simples, onde irá verificar quais são as portas estão abertas 
dentro de um range de portas informados por argumentos e retornar **STATUS OPEN**, para os 
casos de as portas varridas estarem abertas. 

Os argumentos informados consistem no endereço de host do alvo que será analisado, seguidos 
das portas inicial e final que comporão o range.

**OBS.: Se sua meta é de escanear apenas uma porta, pode colocar o mesmo valor para 
os dois ultimos parâmetros.**

Está em sua versão 2.0 _(beta)_ e ainda está em fase de desenvolvimento.

## Começando
Estas são as instruções para que você tenha uma cópia do **PyTCPScan** em sua maquina para fins 
de desenvolvimento e teste.

## Pré-requisitos:
* É necessário está rodando uma distro linux;
* Ter instalado em sua máquina o interpretador python na versão 3.xx e o pip3. _(geralmente vem por padrão nas distro linux)_.;
* Fazer o update e upgrade do sistema antes de rodar.

## Instalando:
_Não é necessário instalar o PyTCPScan_

---

_OBS.: Para usar como executável, lembrar de dar permissão de execução_
**sudo chmod +x pytcpscan.py**

---

## Execução 
Para executar a aplicação deve passar o argumento com o host do alvo, a porta inicial
e a porta final. Ele irá verificar quais portas estão com o Status Open.

**./pytcpscan  [target] [init_port] [final_port]**

_Exemplo de Resposta:_

<img src="https://github.com/werdelesmarcio/PyTCPScan2/blob/master/Images/Capturar2.PNG">

Leia [as Diretivas de Contribuição](https://github.com/werdelesmarcio/PyTCPScan2/blob/master/Archives/CONTRIBUTING.md) para obter mais detalhes de como contribuir para o projeto.

## Autor:
* **Werdeles Marcio de C. Soares**:**(gh05tb0y)** - _Desenvolvedor_

## Licença: 
***Este projeto está sob Licença GPL-3.0.***
Consulte o arquivo [de Licença](https://github.com/werdelesmarcio/PyTCPScan2/blob/master/Archives/LICENSE) para obter mais detalhes.

## Agradecimentos:
* Obrigado à todos os que apoiam o projeto de alguma forma.

## Contatos
Se quiser entrar em contato, crie um **issue** no GitHub ou envie um e-mail para werdelesmarcio@gmail.com. Obrigado!

<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/werdelesmarcio/PyTCPScan2?style=for-the-badge">   <img alt="GitHub contributors" src="https://img.shields.io/github/contributors/werdelesmarcio/PyTCPScan2?style=for-the-badge">

<img src = "https://github.com/werdelesmarcio/PyTCPScan2/blob/master/Images/SoftwareLivre.png?raw=true" width =130 align="Right">
<img src = "https://github.com/werdelesmarcio/PyTCPScan2/blob/master/Images/PoweredByLinux.png?raw=true" width =80 align="Right">
