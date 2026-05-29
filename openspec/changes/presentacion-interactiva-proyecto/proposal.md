## Why

Para la defensa de nuestro proyecto de la grúa torre de control dual (cableado USB y depuración inalámbrica), necesitamos un recurso visual e interactivo adicional. Una presentación web integrada y autohospedada permitirá exponer de forma profesional el stack tecnológico, el análisis de las herramientas de desarrollo y la importancia de la documentación en Github ante el jurado de la exposición grupal.

## What Changes

- Crear un archivo HTML autocontenido para la presentación interactiva en `web_server/presentacion.html`.
- Diseñar la página como una presentación de diapositivas interactivas en un formato visualmente impresionante (con soporte para tema claro/oscuro y efectos dinámicos).
- Desarrollar la sección de Stack Tecnológico dividida en lenguajes de programación, herramientas de desarrollo (Antigravity IDE, Arduino IDE, Thonny IDE, VS Code, GitHub, Skills de OpenSpec y Brainstorming) y despliegue físico tripartito (Laptop, ESP32, Arduino Nano).
- Desarrollar la sección de Ventajas de las Herramientas explicando el uso de cada una en el proyecto.
- Desarrollar la sección de Documentación vinculada a Github detallando el control de versiones, autorías, métricas de lenguajes, reversiones estables, rol del archivo README y la integración de requerimientos con OpenSpec.
- Integrar la navegación de esta presentación interactiva en el sistema de páginas existentes.

## Capabilities

### New Capabilities
- `presentacion-interactiva`: Página de presentación interactiva de diapositivas para la defensa del proyecto grupal.

### Modified Capabilities

## Impact

- `web_server/presentacion.html`: Nuevo archivo para la presentación interactiva.
- `web_server/index.html`: Modificado para agregar el botón de navegación a la presentación en la cabecera.
- `web_server/schema.html`: Modificado para agregar el botón de navegación a la presentación en la cabecera.
- `web_server/estudio.html`: Modificado para agregar el botón de navegación a la presentación en la cabecera.
