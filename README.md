## 📸 Demonstração em Tempo Real

Para validar o sistema, realizei um teste de intrusão simulado. Abaixo, você pode ver o fluxo completo:

### 1. A Armadilha (Visão do Atacante)
O HoneyPot simula uma tela de aviso de segurança corporativa para registrar qualquer tentativa de acesso não autorizado.
![Tela do HoneyPot](images/Screenshot#2020260423%20125014%20Brave.jpg)

### 2. O Monitoramento (Visão do Sistema)
No momento do acesso, o HoneyPot gera o log e o **Log Analyser** detecta a atividade instantaneamente, processando os dados e disparando o alerta via API.
![Logs e Processamento](images/Honey-pot%20-%20Analyser%20-%201.png)
![Confirmação de Envio](images/Honey-pot%20-%20Analyser%20-%202.png)

### 3. O Alerta (Visão do Analista)
Em menos de um segundo, a notificação detalhada chega ao dispositivo móvel do administrador através do Telegram.
![Alerta no Telegram](images/Screenshot_20260423_125101_Telegram.jpg)
