import requests
import time
import os
import sys

# --- CONFIGURAÇÕES ---
TOKEN = "8775030926:AAEw8wjmemztfGutr8qG39K--ncxZP4cU-Q"
CHAT_ID = "1317999322"
LOG_FILE = "honeypot_log.txt"

def enviar_alerta_telegram(mensagem):
    """Envia a notificação para o Telegram via API."""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    dados = {"chat_id": CHAT_ID, "text": mensagem}
    try:
        response = requests.post(url, data=dados)
        if response.status_code == 200:
            print(f"[OK] Alerta enviado ao Telegram com sucesso.")
        else:
            print(f"[ERRO] Falha na API do Telegram: {response.status_code}")
    except Exception as e:
        print(f"[ERRO] Falha de conexão: {e}")

def monitorar_honeypot():
    """Monitora o arquivo de log em tempo real (Tail -f)."""
    print(f"{'='*50}")
    print(f"SERVIÇO DE MONITORAMENTO SIEM ATIVO")
    print(f"Arquivo: {LOG_FILE}")
    print(f"{'='*50}")

    # Verifica se o arquivo existe antes de começar
    if not os.path.exists(LOG_FILE):
        print(f"[AVISO] O arquivo {LOG_FILE} ainda não existe. Aguardando criação...")
        while not os.path.exists(LOG_FILE):
            time.sleep(2)

    with open(LOG_FILE, "r", encoding="latin-1") as f:
        # Move o cursor para o final do arquivo para ignorar logs antigos
        f.seek(0, os.SEEK_END)
        
        try:
            while True:
                linha = f.readline()
                if not linha:
                    time.sleep(1)  # Aguarda novas entradas
                    continue

                # Lógica de detecção: procura pela palavra-chave do seu HoneyPot
                if "ALERTA DE INTRUSÃO" in linha:
                    log_limpo = linha.strip()
                    print(f"\n[!] EVENTO DETECTADO: {log_limpo}")
                    
                    # Formata a mensagem para o Telegram (com Emoji para destaque)
                    alerta = (
                        f"🚨 *ALERTA DE INTRUSÃO* 🚨\n\n"
                        f"📅 *Log:* {log_limpo}\n\n"
                        f"🛡️ *Sistema:* SIEM Caseiro v1.0"
                    )
                    enviar_alerta_telegram(alerta)
                    
        except KeyboardInterrupt:
            print("\n[!] Monitoramento interrompido pelo usuário.")
            sys.exit()

if __name__ == "__main__":
    monitorar_honeypot()