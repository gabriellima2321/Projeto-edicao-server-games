import psutil

def is_process_running(process_name):
    # Itera sobre todos os processos em execução
    for process in psutil.process_iter(['pid', 'name']):
        try:
            # Verifica se o nome do processo corresponde ao nome fornecido
            if process.info['name'].lower() == process_name.lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


# Exemplo de uso
process_name = "VRising.exe"