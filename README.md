![Imagen del proyecto](./nik%20ge.jpg)

# PNLIO Framework v6.0.1 & NIK v10.1: Arquitectura de un Kernel Neuromórfico Local y Soberano

**Autor:** Gonzalo Mauricio de la Rivera Arellano (Godear24)  
**Rol:** Investigador Independiente, Artista Digital y Orientador Familiar  
**Ubicación:** Chillán, Región del Ñuble, Chile  
**ORCID:** [0009-0001-9455-8416](https://orcid.org/0009-0001-9455-8416)  
**Repositorio Oficial:** [godear6959-creator/nik-neuromorphic-kernel](https://github.com/godear6959-creator/nik-neuromorphic-kernel)  
**Licencia:** Apache License 2.0 (ver LICENSE)

---

## RESUMEN (*ABSTRACT*)

El presente documento expone la especificación técnica y marco conceptual del **PNLIO Framework v6.0.1** y el **Neuromorphic Inference Kernel (NIK v10.1-MEM-FIX)**. A diferencia de las arquitecturas tradicionales basadas en Grandes Modelos de Lenguaje (LLMs) dependientes de infraestructura cloud centralizada, NIK propone un paradigma de computación neuromórfica híbrida $100\%$ local y offline. El sistema integra una Red Neuronal Espicular (*Spiking Neural Network* - SNN) de tres capas (64-128-16), aprendizaje sináptico mediante Plasticidad Dependiente del Tiempo de Disparo (*Spike-Timing-Dependent Plasticity* - STDP), regulación por homeostasis de umbrales adaptativos y un motor de memoria episódica persistente sobre ChromaDB. Este desarrollo demuestra la viabilidad técnica de la inferencia soberana, garantizando el control total de los datos en el borde (*edge computing*).

**Palabras clave:** *Neuromorphic Computing, Spiking Neural Networks (SNN), STDP, Threshold Homeostasis, Episodic Memory, ChromaDB, PNLIO Framework, Local AI.*

---

## 1. INTRODUCCIÓN

El desarrollo dominante de la Inteligencia Artificial moderna ha privilegiado el escalado de modelos de lenguaje sobre arquitecturas de servidor centralizadas. Aunque eficaces, estos entornos presentan vulnerabilidades estructurales respecto a la privacidad, latencia de red, dependencia de suscripciones de software y falta de soberanía de datos.

Diseñado y desarrollado de forma independiente entre 2023 y 2026 en Chillán, Chile, el marco **PNLIO (Predictive Neural Language Input/Output)** propone una alternativa: desacoplar la inteligencia de la nube y ejecutar un simulador de kernel neuromórfico capaz de procesar señales, mantener memoria temporal/vectorial y regular sus propios estados neurodinámicos localmente.

---

## 2. ARQUITECTURA DE SISTEMA (DOS CAPAS)

El sistema opera bajo un diseño modular compuesto por dos entidades principales interactuando mediante colas de tareas asíncronas:

