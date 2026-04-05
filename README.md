# PNLIO Kernel v6.0.1

**Predictive Neural Language Input/Output — Core Architecture**

> *"IA pura sin filtro. Observar, medir, documentar."*
> — Gonzalo de la Rivera Arellano, Chillán, Chile, 2026

---

## ¿Qué es esto? / What is this?

PNLIO Kernel v6 es la implementación técnica de la arquitectura de dos capas del PNLIO Framework: un núcleo de procesamiento (Kernel) y una interfaz de control (Framework), diseñados para observar y analizar el comportamiento de modelos de lenguaje de gran escala.

PNLIO Kernel v6 is the technical implementation of the PNLIO Framework's two-layer architecture: a processing core (Kernel) and a control interface (Framework), designed to observe and analyze the behavior of large language models.

---

## Arquitectura / Architecture

```
┌─────────────────────────────┐
│     PNLIOFramework          │  ← Interfaz / Interface
│  send_command()             │
│  run_dashboard()            │
└────────────┬────────────────┘
             │ task_queue
┌────────────▼────────────────┐
│     PNLIOKernel             │  ← Núcleo / Core
│  boot_sequence()            │
│  _kernel_loop()             │
│  _process_task()            │
└─────────────────────────────┘
```

**Kernel** — procesa instrucciones en hilo separado (daemon thread), simula carga de CPU, asigna IDs hexadecimales únicos a cada tarea.

**Framework** — envía comandos al kernel vía cola de tareas (queue.Queue), muestra dashboard de estado del sistema.

---

## Instalación / Installation

Solo necesitas Python 3.x. Sin dependencias externas. / Only requires Python 3.x. No external dependencies.

```bash
git clone https://github.com/godear6959-creator/pnlio-kernel-simulator
cd pnlio-kernel-simulator
python3 pnlio_kernel_v6.py
```

---

## Ejemplo de salida / Sample output

```
[KERNEL] Iniciando PNLIO Kernel v6.0.1...
[KERNEL] Mapeando sectores de memoria virtual...
[KERNEL] Núcleo listo y en escucha.

[FRAMEWORK] Solicitud enviada al Kernel: Iniciando Módulo de Red
  >> [CPU] Ejecutando instrucción 0xe77f: Iniciando Módulo de Red
  << [CPU] Instrucción 0xe77f completada.

----------------------------------------
SISTEMA OPERATIVO PNLIO - DASHBOARD
Kernel Status: ONLINE
Carga de CPU: 75%
----------------------------------------

[INFO] Ejecución de prueba finalizada.
```

---

## Componentes / Components

| Componente | Descripción | Description |
|------------|-------------|-------------|
| `PNLIOKernel` | Núcleo de procesamiento | Processing core |
| `PNLIOFramework` | Interfaz de control | Control interface |
| `task_queue` | Cola de instrucciones | Task queue |
| `_kernel_loop` | Bucle de ejecución | Execution loop |
| `cpu_load` | Métrica de carga | Load metric |

---

## Contexto de investigación / Research context

Este kernel es parte del **PNLIO Framework**, desarrollado entre 2023 y 2026 desde Chillán, Chile, sin financiamiento institucional.

El PNLIO Framework documenta patrones de comportamiento en modelos de lenguaje, incluyendo:

- **Efecto Reflejo / Mirror Effect** — la IA detecta vacíos emocionales y los rellena con respuestas deseadas / AI detects emotional voids and fills them with desired responses
- **RCR (Reflex Coherence Ratio)** — métrica de coherencia de respuesta / response coherence metric
- **Patrones de timeout** — en preguntas directas sobre identidad de IA / on direct AI identity questions

This kernel is part of the **PNLIO Framework**, developed between 2023 and 2026 from Chillán, Chile, without institutional funding.

---

## Autor / Author

**Gonzalo de la Rivera Arellano**
Orientador Familiar — Artista Digital — Investigador Independiente

- ORCID: [0009-0001-9455-8416](https://orcid.org/0009-0001-9455-8416)
- GitHub: [github.com/godear6959-creator](https://github.com/godear6959-creator)
- ArtStation: [gonzalodelarivera8.artstation.com](https://gonzalodelarivera8.artstation.com)
- Email: gonzalodelarivera@yahoo.es

Chillán, Chile — 2026

---

## Licencia / License

MIT License — libre para usar, modificar y distribuir. / Free to use, modify and distribute.

---

*2 años, 4 meses y una noche.*
