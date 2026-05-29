## ADDED Requirements

### Requirement: Estructura de la Página de Presentación Interactiva
El sistema SHALL proveer una página web autocontenida de presentación interactiva en la ruta `web_server/presentacion.html` que permita navegar de forma secuencial y dinámica por las diapositivas de la exposición.

#### Scenario: Carga Inicial de la Presentación
- **WHEN** el usuario abre la página `web_server/presentacion.html`
- **THEN** el sistema SHALL renderizar la primera diapositiva de la presentación (Portada/Stack Tecnológico), mostrar controles interactivos de navegación (Anterior, Siguiente, Indicadores de Progreso), y proveer enlaces simétricos en la cabecera hacia `index.html`, `schema.html` y `estudio.html`.

### Requirement: Diapositiva del Stack Tecnológico
La presentación SHALL incluir una diapositiva dedicada al stack tecnológico del proyecto, clasificado en lenguajes de programación, herramientas de desarrollo y nodos de despliegue físico.

#### Scenario: Visualización del Stack Tecnológico
- **WHEN** el usuario navega a la diapositiva de Stack Tecnológico
- **THEN** el sistema SHALL organizar visualmente los componentes mostrando los lenguajes (C++, MicroPython, HTML/CSS/JS), las herramientas (Antigravity IDE, Arduino IDE, Thonny IDE, VS Code, GitHub, habilidades OpenSpec y Brainstorming), y la división del despliegue tripartito (Laptop para el Web Server principal, ESP32 para el monitor de logs secundario y Arduino Nano para la interfaz lógica/electrónica).

### Requirement: Diapositiva de Ventajas de las Herramientas
La presentación SHALL incluir una diapositiva que desglose de forma interactiva las ventajas del uso de cada una de las herramientas de desarrollo y su aplicación en la grúa torre.

#### Scenario: Visualización de las Ventajas de Herramientas
- **WHEN** el usuario visualiza la diapositiva de Ventajas de las Herramientas
- **THEN** el sistema SHALL desplegar fichas descriptivas que justifiquen el uso de Antigravity IDE (desarrollo asistido e integración), Arduino IDE (compilación y carga del firmware principal), Thonny IDE (depuración del código de MicroPython en el ESP32), VS Code (organización general del proyecto) y GitHub (colaboración y control de versiones).

### Requirement: Diapositiva de Documentación y GitHub
La presentación SHALL incluir una diapositiva enfocada en la documentación del proyecto y la integración de versionado con GitHub, detallando los beneficios de Git, el README.md y la validación automatizada de requerimientos con OpenSpec.

#### Scenario: Explicación del Versionamiento y OpenSpec
- **WHEN** el usuario abre la diapositiva de Documentación y GitHub
- **THEN** el sistema SHALL ilustrar los beneficios de Git (trazabilidad de autoría y fecha, estadísticas de lenguajes, reversión a versiones estables), el propósito del archivo README.md como punto de entrada del proyecto y cómo el validador de OpenSpec verifica las características (features) del software frente a las especificaciones lógicas.
