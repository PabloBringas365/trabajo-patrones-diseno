# Trabajo sobre Patrones de Diseño

Esta es mi práctica sobre patrones de diseño de software. Primero he puesto un pequeño resumen teórico basándome en lo que he leído en Refactoring Guru, y después detallo los ejemplos prácticos que he programado en Python.

---

## 1. Justificación Teórica

### ¿Qué son los patrones de diseño?
Según *Refactoring Guru*, los patrones de diseño son soluciones habituales a problemas comunes que ocurren con frecuencia en el diseño de software. No se trata de fragmentos de código específicos que se puedan copiar y pegar, sino de conceptos generales o planos prefabricados que se pueden adaptar y personalizar para resolver un problema de diseño en un código particular.

### ¿Cuándo se usan?
Se deben utilizar en la fase de diseño del software cuando identificamos que nos estamos enfrentando a un problema clásico de estructura, creación o comunicación entre objetos. Su uso está ligado a la necesidad de mantener el código limpio, flexible y fácil de entender de cara al futuro.

### ¿Por qué son útiles?
* **Soluciones probadas:** Son un "kit de herramientas" con soluciones a problemas cotidianos testeadas y optimizadas por miles de desarrolladores antes que nosotros.
* **Estandarización:** Definen un vocabulario común para todo el equipo de desarrollo. Es mucho más eficiente decir *"aquí he aplicado un Singleton"* que explicar detalladamente toda la lógica de restricciones de la clase.
* **Profesionalización:** Ayudan a aprender cómo resolver problemas utilizando principios de diseño de software orientado a objetos.

### ¿Forman parte del diseño, la arquitectura o la microarquitectura?
Los patrones de diseño forman parte del **diseño detallado y la microarquitectura** del software. 
Mientras que la *arquitectura* define la estructura macroscópica de todo el sistema (como decidir si se usa un modelo cliente-servidor, microservicios, etc.), los *patrones de diseño* actúan a un nivel más bajo y enfocado. Organizan de manera interna las relaciones, responsabilidades y comunicaciones entre las clases y los objetos individuales que componen esos módulos arquitectónicos.

---

## 2. Patrones Elegidos e Implementación

Para este trabajo se han seleccionado e implementado dos patrones de diseño en el lenguaje **Python**, abordando dos situaciones reales diferentes para cada uno:

### A) Patrón Creacional: Singleton
Este patrón asegura que una clase tenga una única instancia en memoria en todo momento y proporciona un punto de acceso global a ella.
* `singleton_logger.py`: Implementación de un sistema de registro único de eventos (Logger) para centralizar los mensajes del sistema sin conflictos.
* `singleton_bd.py`: Configuración de un gestor de conexiones a una base de datos para evitar la apertura innecesaria y costosa de múltiples conexiones.

### B) Patrón de Comportamiento: Strategy 
Este patrón permite definir una familia de algoritmos, encapsular cada uno en una clase independiente y hacer que sus objetos sean completamente intercambiables en tiempo de ejecución.
* `strategy_calculadora.py`: Una calculadora que intercambia dinámicamente sus operaciones matemáticas básicas (Sumar o Restar) según la selección del usuario.
* `strategy_envios.py`: Un módulo logístico para una tienda online que calcula el coste del transporte aplicando diferentes algoritmos de envío (Normal o Expres).

---

## Enlace al Vídeo Explicativo
