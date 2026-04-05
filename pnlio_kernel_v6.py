import time
import threading
import random
import queue

# --- SECCIÓN: PNLIO KERNEL v6 (NÚCLEO) ---
class PNLIOKernel:
    def __init__(self):
        self.version = "6.0.1"
        self.is_active = False
        self.memory_map = {}
        self.task_queue = queue.Queue()
        self.cpu_load = 0

    def boot_sequence(self):
        """Inicializa los recursos del sistema."""
        print(f"[KERNEL] Iniciando PNLIO Kernel v{self.version}...")
        time.sleep(0.5)
        print("[KERNEL] Mapeando sectores de memoria virtual...")
        self.is_active = True
        
        # Hilo del ciclo de ejecución del Kernel
        threading.Thread(target=self._kernel_loop, daemon=True).start()
        print("[KERNEL] Núcleo listo y en escucha.\n")

    def _kernel_loop(self):
        """Bucle de procesamiento de bajo nivel."""
        while self.is_active:
            if not self.task_queue.empty():
                task = self.task_queue.get()
                self._process_task(task)
            time.sleep(0.1)

    def _process_task(self, task):
        """Simulación de procesamiento de CPU."""
        task_id = task["id"]
        print(f"  >> [CPU] Ejecutando instrucción 0x{task_id:04x}: {task["cmd"]}")
        self.cpu_load = random.randint(10, 85)
        time.sleep(random.uniform(0.3, 0.8))
        print(f"  << [CPU] Instrucción 0x{task_id:04x} completada.")

# --- SECCIÓN: PNLIO FRAMEWORK (INTERFAZ) ---
class PNLIOFramework:
    def __init__(self, kernel):
        self.kernel = kernel
        self.app_name = "PNLIO Standard Environment"

    def send_command(self, command_text):
        """Envía una petición del framework al kernel."""
        task_id = random.getrandbits(16)
        payload = {"id": task_id, "cmd": command_text}
        print(f"[FRAMEWORK] Solicitud enviada al Kernel: {command_text}")
        self.kernel.task_queue.put(payload)

    def run_dashboard(self):
        """Muestra el estado del sistema."""
        print("-" * 40)
        print(f"SISTEMA OPERATIVO PNLIO - DASHBOARD")
        print(f"Kernel Status: {"ONLINE" if self.kernel.is_active else "OFFLINE"}")
        print(f"Carga de CPU: {self.kernel.cpu_load}%")
        print("-" * 40)

# --- INSTANCIACIÓN Y EJECUCIÓN ---
if __name__ == "__main__":
    # 1. Instanciar componentes
    core = PNLIOKernel()
    bridge = PNLIOFramework(core)

    # 2. Arrancar sistema
    core.boot_sequence()

    # 3. Simular aplicaciones del Framework usando el Kernel
    apps_to_run = [
        "Iniciando Módulo de Red",
        "Cargando Librerías de Gráficos",
        "Sincronizando Base de Datos",
        "Limpieza de Caché"
    ]

    for app in apps_to_run:
        bridge.send_command(app)
        time.sleep(0.5)

    # 4. Mantener vivo para observar procesos
    time.sleep(2)
    bridge.run_dashboard()
    print("\n[INFO] Ejecución de prueba finalizada.")
