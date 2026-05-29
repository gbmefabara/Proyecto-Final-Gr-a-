# Diseño de Especificación: Guía de Estudio Interactiva para Exposición (`estudio.html`)

Este documento detalla el diseño y la estructura para crear la guía de estudio interactiva de la grúa torre, orientada a la preparación de la exposición grupal.

## 1. Contexto
El equipo del proyecto se compone de 4 integrantes: **Johanan Castro** (Coordinador), **Emilia Fabara**, **Renata Duque** y **Polteh Morales**. Para preparar la defensa de su prototipo de grúa torre de control dual, requieren un material didáctico estructurado que divida los contenidos en 4 categorías principales: Programación, Electrónica, Diseño y Pruebas/Funcionamiento.

---

## 2. Objetivos y Exclusiones (Goals / Non-Goals)

**Goals:**
*   Crear una aplicación web interactiva autocontenida en un único archivo `estudio.html`.
*   Implementar un sistema de navegación por pestañas para las 4 secciones temáticas, un guión de asignaciones y un cuestionario interactivo.
*   Distribuir equitativamente los temas mediante un guión de exposición con una matriz 4x4 (cada integrante tiene un subtema asignado por categoría).
*   Añadir herramientas de refuerzo dinámicas como flashcards 3D y un cuestionario (quiz) auto-evaluativo con retroalimentación inmediata.
*   Diseñar una interfaz responsiva y premium con soporte para tema claro y oscuro de forma persistente.

**Non-Goals:**
*   No se contempla la comunicación serie ni conexión de red en este archivo (es netamente educativo y de estudio).
*   No requiere almacenamiento persistente en bases de datos.

---

## 3. Decisiones de Diseño

### Decisión 1: Archivo Único e Independiente (HTML/CSS/JS combinados)
*   **Decisión**: Toda la estructura, los estilos y la interactividad se escribirán dentro del mismo archivo `estudio.html`.
*   **Razón**: Permite la máxima portabilidad. Los estudiantes pueden transferir el archivo a sus teléfonos celulares, tablets o laptops y abrirlo directamente de forma local sin requerir un servidor web en segundo plano ni dependencias de red.
*   **Alternativas consideradas**: Crear hojas de estilo y scripts externos. Se descartó para simplificar la distribución local y el despliegue del recurso.

### Decisión 2: Tabulación de Guiones y Asignaciones
*   **Decisión**: La pestaña "Guión de Exposición" presentará la asignación de temas de forma dinámica mediante tarjetas con filtros por integrante o por tema.
*   **Razón**: Facilita a cada miembro aislar visualmente lo que le corresponde hablar en la exposición, además de ver el flujo general secuencial de la presentación coordinada por Johanan Castro.

### Decisión 3: Cuestionario Interactivo por Software
*   **Decisión**: Usar un cuestionario autoevaluativo con opciones múltiples donde el color (verde/rojo) y explicaciones emergentes guíen al estudiante en sus fallos.
*   **Razón**: Ofrece un aprendizaje activo e inmediato de los conceptos lógicos y físicos de la grúa.

---

## 4. Plan de Verificación y Pruebas

### Pruebas de Usabilidad:
1.  **Navegación**: Abrir `estudio.html` y verificar que las pestañas (Programación, Electrónica, Diseño, Pruebas, Guión, Quiz) cambian de contenido instantáneamente y sin errores en la consola.
2.  **Responsividad**: Simular vista móvil en Chrome DevTools y comprobar que el diseño se adapta limpiamente y los menús son legibles.
3.  **Quiz Interactivo**: Responder las preguntas de prueba y comprobar que se registran los aciertos/errores de forma correcta, desplegando la explicación técnica.
4.  **Flashcards**: Hacer clic en las tarjetas de memorización en la pestaña de Diseño y verificar la rotación en 3D para revelar las respuestas.
