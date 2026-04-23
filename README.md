# Integrated HoneyPot & Real-Time SIEM Alert System

Este projeto demonstra a criação de um ecossistema de segurança ativa composto por um **HoneyPot** (armadilha) e um **Analisador de Logs (SIEM)** que dispara alertas em tempo real via Telegram.

## 🚀 Funcionalidades
- **HoneyPot HTTP:** Simula um serviço corporativo para atrair e registrar acessos suspeitos.
- **Análise em Tempo Real:** Monitoramento contínuo de logs (tail-f style) com Python.
- **Alertas Instantâneos:** Integração com Telegram Bot API para notificação imediata de incidentes.
- **Resiliência de Encoding:** Tratamento de logs em sistemas Windows (Latin-1/UTF-8).

## 🛠️ Tecnologias
- Python 3.x
- Telegram Bot API
- Bibliotecas: `requests`, `time`, `os`

## 📋 Como usar
1. Clone o repositório.
2. Configure seu `TOKEN` e `CHAT_ID` no arquivo `log_analyzer.py`.
3. Execute o HoneyPot: `python honeypot.py`.
4. Execute o Analisador em outro terminal: `python log_analyzer.py`.
5. Acesse `http://localhost:8080` e receba o alerta no seu celular!

## 📸 Demonstração
![Alerta no Telegram](link_da_sua_imagem_9)
*(Dica: Faça upload da imagem do alerta no celular para a pasta do GitHub e linke-a aqui)*
