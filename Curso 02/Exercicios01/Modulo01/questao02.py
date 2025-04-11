import platform

sistema = platform.system()
versao = platform.version()
arquitetura = platform.machine()

print("Sistema operacional:", sistema)
print("Versão do sistema:", versao)
print("Arquitetura do processador:", arquitetura)
