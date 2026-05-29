# Diseño de Especificación: Presentación Interactiva del Proyecto (`presentacion.html`)

Este documento detalla el diseño y la estructura técnica para la creación del recurso visual de presentación interactiva de diapositivas orientado a la defensa del proyecto ante el jurado.

## 1. Contexto
Para la exposición del prototipo de la grúa torre de control dual, se requiere un soporte de diapositivas que sea autocontenido, responsivo y visualmente premium. La presentación debe integrarse en el ecosistema web local del proyecto, enlazando directamente con la interfaz de control (`index.html`), el diagrama de conexiones (`schema.html`) y la guía de estudio (`estudio.html`).

---

## 2. Objetivos y Exclusiones (Goals / Non-Goals)

**Goals:**
*   Crear una aplicación de diapositivas en `web_server/presentacion.html`.
*   Implementar un lienzo fijo de 16:9 (1280x720px) que se escale dinámicamente con `transform: scale()` en JS para adaptarse a pantalla completa en cualquier proyector/pantalla sin desbordes.
*   Diseñar una transición de "cámara virtual" 3D que alterne de diapositiva alejando (zoom out), rotando y acercando (zoom in) la nueva diapositiva.
*   Implementar tarjetas con efecto 3D hover y paralaje en la profundidad del logo al pasar el cursor.
*   Integrar los logos de herramientas y lenguajes cargados localmente desde `../img/`.
*   Asegurar navegación bidireccional simétrica en todas las cabeceras de página.

**Non-Goals:**
*   No requiere backend ni llamadas asíncronas de control serie USB en esta página.
*   No requiere conexión a Internet (todo el CSS y JS son internos, logos locales).

---

## 3. Decisiones de Diseño

### Decisión 1: Escalado Proporcional Dinámico (Resolución Fija)
*   **Decisión**: La interfaz se diseña sobre un lienzo de 1280x720px y se escala en JS usando `Math.min(window.innerWidth / 1280, window.innerHeight / 720)`.
*   **Razón**: Evita desalineaciones de texto o desbordes de imágenes en proyectores escolares de baja resolución (ej. 4:3 o 16:10).

### Decisión 2: Transición Prezi-Style en 3D
*   **Decisión**: Usar clases de estado `.slide.next-enter` y `.slide.prev-exit` combinando `scale()`, `rotate()` y `translate()` en CSS.
*   **Razón**: Aporta dinamismo a la presentación manteniendo el rendimiento gráfico óptimo gracias al renderizado por hardware de las transformaciones 3D.

### Decisión 3: Hover 3D con Paralaje en Logos
*   **Decisión**: Aplicar `transform-style: preserve-3d;` en las tarjetas de herramientas y dotar a las imágenes de logo de un `translateZ` mayor al pasar el cursor.
*   **Razón**: Aumenta la interactividad y la estética premium del recurso de estudio.

---

## 4. Plan de Verificación y Pruebas

### Pruebas de Usabilidad:
1.  **Escalamiento**: Cambiar el tamaño del navegador y certificar que la presentación se escala proporcionalmente sin romperse.
2.  **Teclado**: Presionar flecha derecha y flecha izquierda para verificar el cambio de diapositiva con la animación de cámara 3D.
3.  **Hover 3D**: Pasar el cursor sobre las tarjetas del stack y herramientas en la diapositiva 2 y verificar que el logo se eleva en paralaje y la tarjeta se inclina en 3D.
4.  **Enlaces**: Probar todos los enlaces de la cabecera y certificar el paso bidireccional entre Panel, Esquema, Estudio y Presentación.
