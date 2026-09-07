# Corrección documental — NIK v10.1-MEM-FIX

**Fecha de corrección:** 7 de septiembre de 2026  
**Repositorio:** [godear6959-creator/pnlio-kernel-simulator](https://github.com/godear6959-creator/pnlio-kernel-simulator)

## Propósito de esta corrección

Esta nota se agrega para aclarar la relación entre el documento técnico `PAPER_NIK_v10.1_MEM_FIX.pdf` y el archivo de código `pnlio_kernel_v6.py` actualmente visible en este repositorio. **No reemplaza, elimina ni invalida el paper original**. Su función es separar con precisión la especificación documentada de la implementación pública que puede verificarse directamente.

## Alcance de los materiales existentes

El paper describe la arquitectura conceptual y técnica de **PNLIO Framework v6.0.1 / NIK v10.1-MEM-FIX**, incluyendo una SNN de tres capas, dinámica LIF, STDP, homeostasis adaptativa, modulación EMP, memoria episódica, ChromaDB y una interfaz REST.

El archivo Python público `pnlio_kernel_v6.py` corresponde al **simulador base del ciclo kernel–framework**. Su implementación visible utiliza clases `PNLIOKernel` y `PNLIOFramework`, una cola de tareas, un hilo de procesamiento, estados internos y una carga de CPU simulada. En la versión pública revisada no aparecen todavía todas las funciones avanzadas descritas en el paper.

| Material | Interpretación correcta |
|---|---|
| `PAPER_NIK_v10.1_MEM_FIX.pdf` | Especificación y documentación de la arquitectura NIK v10.1-MEM-FIX y de sus resultados reportados. |
| `pnlio_kernel_v6.py` | Simulador base público del flujo de tareas entre framework y kernel. |
| `README.md` | Punto de entrada actualizado que distingue el prototipo visible de la arquitectura documentada. |

## Corrección de interpretación

Las capacidades avanzadas descritas en el paper deben considerarse **parte de la arquitectura documentada y de la línea de investigación** hasta que el código correspondiente, sus dependencias, pruebas y datos de validación estén disponibles en este repositorio. La presencia del paper no debe interpretarse automáticamente como evidencia de que cada módulo descrito está implementado en el script Python público actual.

Esta aclaración no borra ni modifica los resultados reportados. Solo mejora la trazabilidad entre documentación, código y evidencia reproducible. Las futuras versiones podrán incorporar los módulos avanzados y actualizar esta nota con referencias a archivos, commits y pruebas concretas.

## Archivos preservados

La presente corrección conserva sin eliminación los siguientes materiales existentes:

- `PAPER_NIK_v10.1_MEM_FIX.pdf`.
- `pnlio_kernel_v6.py`.
- `NIK_v10.1_MEM_FIX_Arquitectura.png`.
- `nik ge.jpg`.
- `watermarked_img_1459579470421024 HONGO.jpg`.
- `LICENSE`.

## Referencias

1. [README del repositorio](README.md).
2. [Paper NIK v10.1 MEM-FIX](PAPER_NIK_v10.1_MEM_FIX.pdf).
3. [Simulador Python del kernel](pnlio_kernel_v6.py).
