# Especificación de Diseño: Cuestionario de Estudio Interactivo (TorreGrúa)

Este documento define la estructura y el comportamiento técnico del nuevo archivo `cuestionario.html`, diseñado para ayudar a los estudiantes a estudiar la electrónica y programación del proyecto Grúa Torre de Control Dual.

## Objetivos del Diseño

1. **Libro de Conceptos Rápidos**: Sección introductoria interactiva para repasar Puente H, motores vs motorreductores, GND común, señales analógicas/digitales y comunicación serial.
2. **Cuestionario Interactivo con Campo de Escritura**: 17 preguntas con áreas de texto donde el estudiante redacta su respuesta antes de pulsar un botón para compararla con la oficial.
3. **Métricas de Rendimiento (Scoreboard)**: Sistema de autoevaluación basado en clics (*"¡Le atiné!"* / *"Necesito repasar"*) con barra de progreso y cálculo dinámico de puntuación en tiempo real.
4. **Diseño Luxury Institucional**: Conservar la paleta de colores azul marino (`#192b6d`) y amarillo/oro (`#ede221`) del Colegio Paulo VI con efectos glassmorphism.

---

## 1. Estructura de la Interfaz (`cuestionario.html`)

El archivo se ubicará en `web_server/cuestionario.html` y heredará la barra lateral de navegación de `estudio.html`.

### Estilos CSS:
Se utilizarán las mismas variables CSS institucionales:
```css
:root {
    --bg-color: #070b1b;
    --bg-gradient: radial-gradient(circle at 50% 50%, #0f183d 0%, #050814 100%);
    --panel-bg: rgba(13, 23, 60, 0.65);
    --border-color: rgba(237, 226, 33, 0.18);
    --text-primary: #ffffff;
    --text-secondary: #9da8d1;
    --accent-color: #ede221;
    --accent-glow: rgba(237, 226, 33, 0.25);
}
```

### Componentes Especiales de UI:
* **Scoreboard Flotante**: Una barra superior estática con:
  * Progreso de completado (ej: `5 de 17 respondidas`).
  * Puntaje acumulado de aciertos (`Puntaje de Exposición: 80%`).
  * Insignia dinámica de estado (ej: `"Aprendiz"`, `"Mecatrónico Junior"`, `"Expositor Estrella"`).
* **Tarjetas del Cuestionario**:
  * Un elemento `textarea` para escribir la respuesta.
  * Un botón para comparar (`.btn-compare`).
  * Un panel colapsable que revela la respuesta oficial al lado de su texto escrito.
  * Botones de puntuación rápida:
    * Botón verde: *"¡Me acerqué bastante!"* (`+1` punto, marca la pregunta como completada correctamente).
    * Botón rojo: *"Debo estudiar más"* (`+0` puntos, marca como completada pero incorrecta).

---

## 2. Contenido del Banco de Conceptos y Cuestionario

El contenido se estructurará en 4 categorías:
1. **Electrónica de Fuerza**: Motores vs motorreductores, Puente H, alimentación (9V vs 5V), corriente y PWM.
2. **Señales y Control**: Joysticks (analógico/digital), tierra común (GND) y puertos de red.
3. **Arquitectura y Software**: UART/Serial, lenguajes de programación y topología de servidores (3 servidores).
4. **Metodología y Herramientas**: Git/GitHub, README.md, requirements.md, openspec y control de cambios (commits).

---

## 3. Integración en `estudio.html`

Para garantizar la coherencia del flujo de usuario:
1. Añadiremos un enlace en la barra de navegación lateral y en el menú inferior móvil de `estudio.html` apuntando a `cuestionario.html`.
2. En la pestaña de *Quiz y Autoevaluación* (Tab 6) de `estudio.html`, colocaremos un banner destacado que invite a los alumnos a estudiar en el cuestionario interactivo externo.
