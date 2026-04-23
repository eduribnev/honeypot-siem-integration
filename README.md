# Integrated HoneyPot & Real-Time SIEM Alert System

Sistema de segurança ativa que utiliza um HoneyPot para atrair tráfego suspeito e um Analisador de Logs para disparo imediato de alertas via Telegram.

## 📋 Descrição do Projeto
Este projeto foi desenvolvido para demonstrar o ciclo completo de Detecção e Resposta a Incidentes (IR). Ele monitora acessos não autorizados em um serviço simulado e utiliza automação em Python para notificar o administrador em tempo real.

## 🛠️ Arquitetura e Funcionalidades
- **Defesa Ativa:** Interface HTTP simulada para registro de tentativas de intrusão.
- **Análise de Logs:** Script resiliente que realiza a leitura contínua (tailing) de arquivos de log.
- **Integração de APIs:** Conexão com a Telegram Bot API para notificações push instantâneas.
- **Tratamento de Dados:** Suporte a diferentes encodings (UTF-8/Latin-1) para garantir compatibilidade em ambientes Windows/Linux.

## 💻 Requisitos
- Python 3.x
- Biblioteca `requests` (`pip install requests`)
- Token de Bot do Telegram e ID de Chat

## 🚀 Como Executar
1. Inicie o HoneyPot: `python honeypot.py`
2. Inicie o Analisador: `python log_analyzer.py`
3. Monitore os alertas no seu dispositivo configurado.
