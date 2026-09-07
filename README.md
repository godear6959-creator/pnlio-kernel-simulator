# PNLIO Kernel Simulator

## Simulador de kernel neuromórfico local — NIK v10.1 / PNLIO Kernel v6.0.1

Este repositorio contiene un prototipo experimental para estudiar una arquitectura de procesamiento local inspirada en sistemas neuromórficos. El proyecto reúne un simulador de kernel escrito en Python, documentación técnica, un paper de arquitectura y recursos visuales asociados.

El alcance actual debe entenderse como **simulación y exploración de arquitectura**, no como un sistema operativo neuromórfico ni como hardware neuromórfico implementado. El objetivo es proporcionar una base pequeña y trazable para experimentar con colas de tareas, ciclos de ejecución, estados del kernel y una interfaz de framework.

> El repositorio es un prototipo de investigación. Las capacidades descritas deben distinguirse de las funcionalidades efectivamente implementadas en el código disponible.

## Componentes del modelo

La implementación pública actual se organiza en dos clases principales:

| Componente | Función |
|---|---|
| `PNLIOKernel` | Mantiene el estado del kernel, una cola de tareas, un mapa de memoria simulado y un ciclo de procesamiento en segundo plano. |
| `PNLIOFramework` | Actúa como interfaz de alto nivel para enviar comandos al kernel y mostrar un estado básico del sistema. |

El flujo de demostración crea el kernel, inicia su ciclo de ejecución, envía comandos de prueba a una cola y muestra una vista resumida de la carga simulada de CPU. El procesamiento se realiza mediante hilos de Python y retardos artificiales; no representa todavía una SNN ejecutable, aprendizaje STDP, memoria vectorial ChromaDB ni inferencia neuromórfica sobre hardware especializado.

## Estructura del repositorio

```text
.
├── LICENSE
├── NIK_v10.1_MEM_FIX_Arquitectura.png
├── PAPER_NIK_v10.1_MEM_FIX.pdf
├── README.md
├── CORRECCION_DOCUMENTAL_NIK_v10.1.md
├── nik ge.jpg
├── pnlio_kernel_v6.py
└── watermarked_img_1459579470421024 HONGO.jpg
```

## Estado técnico actual

El repositorio documenta una arquitectura conceptual que menciona redes neuronales de picos, plasticidad sináptica, homeostasis y memoria episódica. Sin embargo, la implementación Python visible en `pnlio_kernel_v6.py` es actualmente un simulador de flujo de tareas con `queue.Queue`, `threading`, estados internos y carga de CPU aleatoria.

Esta distinción es importante para la reproducibilidad: el paper presenta el marco de investigación, mientras que el script disponible implementa una demostración mínima del ciclo kernel–framework. Cualquier afirmación sobre SNN, STDP, memoria episódica o ejecución neuromórfica debe considerarse trabajo pendiente hasta que exista código, pruebas y resultados verificables para esas funciones.

## Corrección documental

Se agrega [`CORRECCION_DOCUMENTAL_NIK_v10.1.md`](CORRECCION_DOCUMENTAL_NIK_v10.1.md) como aclaración de trazabilidad. Esta nota **no borra ni reemplaza** el paper `PAPER_NIK_v10.1_MEM_FIX.pdf`, el código ni los recursos existentes; distingue la arquitectura documentada de la implementación Python pública que puede verificarse actualmente.

El paper conserva su valor como especificación y registro de la línea de investigación. El script `pnlio_kernel_v6.py` se identifica como el simulador base visible del ciclo kernel–framework. Las funciones avanzadas descritas en el paper deberán vincularse a código, pruebas y resultados reproducibles a medida que se incorporen al repositorio.

## Revisión de ejecución

Antes de usar el script como demostración ejecutable, se debe validar y corregir su sintaxis Python. La versión pública observada contiene expresiones `f-string` con comillas anidadas en el procesamiento de tareas y en el dashboard. Por ello, el primer paso recomendado es ejecutar una comprobación sintáctica:

```bash
python -m py_compile pnlio_kernel_v6.py
```

Si la comprobación es satisfactoria después de corregir esas expresiones, el flujo previsto será:

```bash
python pnlio_kernel_v6.py
```

No se declara una lista de dependencias externas porque el script revisado utiliza módulos de la biblioteca estándar de Python: `time`, `threading`, `random` y `queue`.

## Paper y documentación

El documento principal de arquitectura está disponible en [`PAPER_NIK_v10.1_MEM_FIX.pdf`](PAPER_NIK_v10.1_MEM_FIX.pdf). La imagen de referencia se encuentra en [`NIK_v10.1_MEM_FIX_Arquitectura.png`](NIK_v10.1_MEM_FIX_Arquitectura.png).

Para fortalecer el valor científico y técnico del proyecto, las próximas iteraciones deberían incluir una especificación formal de los estados del kernel, pruebas automatizadas, mediciones de latencia y throughput, definición reproducible de las métricas, ejemplos de entrada y salida, y una separación explícita entre simulación conceptual e implementación neuromórfica.

## Limitaciones conocidas

El prototipo no debe interpretarse como un kernel de sistema operativo, un modelo de inteligencia artificial autónomo ni una implementación completa de una red neuronal de picos. El código visible no contiene todavía una implementación verificable de STDP, memoria episódica persistente, ChromaDB, entrenamiento SNN o ejecución sobre hardware neuromórfico.

La afirmación de “soberanía” debe entenderse aquí como una **dirección de diseño local y offline**. Para demostrarla técnicamente sería necesario documentar el entorno de ejecución, las dependencias, los flujos de datos, la ausencia de servicios externos y pruebas reproducibles.

## Licencia y autoría

El repositorio se distribuye bajo [Apache License 2.0](LICENSE).

**Autor:** Gonzalo Mauricio de la Rivera Arellano  
**ORCID:** [0009-0001-9455-8416](https://orcid.org/0009-0001-9455-8416)  
**Repositorio:** [godear6959-creator/pnlio-kernel-simulator](https://github.com/godear6959-creator/pnlio-kernel-simulator)

## Referencias

1. [Repositorio público PNLIO Kernel Simulator](https://github.com/godear6959-creator/pnlio-kernel-simulator).
2. [Archivo `pnlio_kernel_v6.py`](https://github.com/godear6959-creator/pnlio-kernel-simulator/blob/main/pnlio_kernel_v6.py).
3. [Paper NIK v10.1 MEM-FIX](https://github.com/godear6959-creator/pnlio-kernel-simulator/blob/main/PAPER_NIK_v10.1_MEM_FIX.pdf).
4. [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).
