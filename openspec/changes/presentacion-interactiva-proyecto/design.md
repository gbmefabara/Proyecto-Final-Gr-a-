## Context

Para la defensa de nuestro proyecto de la grúa torre de control dual ante el jurado, es vital contar con una presentación estructurada, visualmente impactante y que se ejecute de forma ágil. Al integrar la presentación como una página HTML autocontenida en el servidor local del proyecto, garantizamos que el expositor pueda alternar sin problemas entre la interfaz de control principal (`index.html`), la guía de conexiones (`schema.html`), la guía de estudio (`estudio.html`) y la propia presentación de diapositivas (`presentacion.html`), todo dentro del mismo navegador y sin requerir internet.

## Goals / Non-Goals

**Goals:**
*   Crear una aplicación web de presentación de diapositivas autocontenida en `web_server/presentacion.html`.
*   Diseñar una interfaz premium interactiva con soporte de tema claro/oscuro persistente y animaciones fluidas para el cambio de diapositivas.
*   Permitir la navegación mediante teclado (flechas izquierda/derecha) y clics en botones de control y bullets de progreso.
*   Exponer de manera clara el Stack Tecnológico, las Ventajas de las Herramientas y la Documentación integrada en Github (incluyendo OpenSpec y el README).
*   Garantizar la navegación bidireccional simétrica entre todas las páginas del proyecto (`index.html`, `schema.html`, `estudio.html`, `presentacion.html`).

**Non-Goals:**
*   No requiere almacenamiento persistente ni interacción directa con la conexión serial del microcontrolador.
*   No requiere conexión de backend externa ni dependencias de frameworks JS pesados (como React, Angular) para mantener la portabilidad.

## Decisions

### Decisión 1: Navegación de Diapositivas por CSS y Clases JS
*   **Decisión**: Utilizar clases CSS active (`.slide.active`) combinadas con transformaciones de traducción horizontal (`translateX`) o desvanecimientos opacos (`opacity`) en Javascript para realizar transiciones fluidas.
*   **Razón**: Garantiza transiciones rápidas y limpias sin necesidad de librerías externas de presentación de diapositivas (como Reveal.js), manteniendo el archivo 100% autocontenido y liviano.

### Decisión 2: Soporte Multicanal de Navegación (Teclado + Botones)
*   **Decisión**: Escuchar eventos de teclado (`keydown` para `ArrowRight` y `ArrowLeft`) además de los botones táctiles en pantalla y bullets de progreso interactivos.
*   **Razón**: Permite al expositor usar un control remoto de diapositivas (clicker), el teclado de la laptop o una pantalla táctil de celular/tablet de manera indistinta durante la defensa.

### Decisión 3: Estructura del Grid de Stack y Fichas de GitHub
*   **Decisión**: Usar CSS Grid y CSS Flexbox para organizar de manera uniforme los 3 apartados del stack tecnológico y las ventajas de las herramientas, usando la misma paleta HSL premium del sistema de diseño (cian, verde menta, gris grafito).
*   **Razón**: Asegura que la información sea visualmente legible a gran distancia (proyectores de aula) y se adapte automáticamente al ancho de pantalla del dispositivo.

## Risks / Trade-offs

*   **Riesgo**: La resolución del proyector en el aula de defensa puede ser baja (ej. 1024x768 o 1280x720) y deformar el texto o los grids.
    *   *Mitigación*: Implementar layouts responsivos fluidos con escalas basadas en porcentajes y flexbox, y utilizar media queries específicas para resoluciones de aspecto 4:3 clásicas para asegurar que el contenido nunca se desborde o se solape.
