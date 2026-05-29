# Guía de Estudio y Prompt de Replicación para Exposición: Grúa Torre de Control Dual

Este archivo contiene un prompt estructurado y reutilizable para recrear la **Guía de Estudio Interactiva (`estudio.html`)** en cualquier modelo de lenguaje de IA (como Gemini, Claude o ChatGPT). Permite generar un recurso educativo portátil, autocontenido y responsivo para preparar defensas de proyectos de hardware/software.

---

## 🏗️ Prompt Reutilizable para la IA

Copia y pega el siguiente bloque de texto en una IA para generar la página web de estudio interactiva:

```markdown
Actúa como un diseñador frontend premium y un desarrollador Full-Stack experto en sistemas embebidos (Arduino, MicroPython) y educación tecnológica. Necesito que crees un único archivo HTML llamado `estudio.html` que sirva como una guía de estudio interactiva, responsiva y autocontenida para preparar la defensa y exposición grupal de un prototipo de grúa torre de control dual (cableado USB y depuración inalámbrica).

La aplicación web debe ser totalmente offline (cero dependencias de red, excepto fuentes de Google Fonts, todo el CSS y JS en el mismo archivo) y contar con una estética moderna de panel de administración (glassmorphism, tema oscuro profundo y tema claro intercambiable, transiciones suaves y microanimaciones).

### 1. Estructura y Navegación
- **Diseño Desktop**: Una barra lateral de navegación izquierda fija y elegante (`sidebar`) que permita conmutar entre las pestañas de estudio.
- **Diseño Móvil**: Una barra de navegación inferior (`bottom-nav`) compacta para pantallas táctiles, ocultando la barra lateral.
- **Cabecera**: Título dinámico de la pestaña activa, botón flotante circular para alternar el tema claro (fondo crema `#f8fafc` y textos oscuros) y oscuro (fondo azul noche profundo `#0b0f19` con acentos cian y morados), y botones de enlace rápidos para regresar a `index.html` (Panel) y `schema.html` (Esquema) usando una clase `.nav-btn` estilizada.

### 2. Pestañas Temáticas de Estudio (Contenido)

#### Pestaña 1: 💻 Programación (Software)
- Explicar detalladamente el principio de **control exclusivo** en el Arduino Nano mediante la variable lógica `controlWebActivo` para prevenir colisiones de comandos.
- Un acordeón colapsable con el sketch C++ de Arduino que configure `SoftwareSerial` en pines D12(RX)/D9(TX) para logs de depuración inalámbrica.
- Un acordeón colapsable con el firmware de MicroPython en el ESP32 que levante un servidor web asíncrono y administre una cola circular (FIFO) de logs de máximo 50 líneas.
- Un acordeón colapsable con el script de JavaScript del navegador que use la `Web Serial API` para leer y escribir tramas JSON asíncronas directamente por USB sin bloquear el hilo principal.

#### Pestaña 2: 🔌 Electrónica (Hardware)
- Una tabla ordenada con el mapeo físico de los Joysticks analógicos (A0, A1, A2, A3), canales de depuración serie y controladores de motores.
- Explicar detalladamente el **divisor de tensión resistivo** (resistencias de 1kΩ y 2kΩ) necesario para rebajar la señal TX de 5V del Arduino a los 3.3V tolerados por el pin RX2 del ESP32, incluyendo el gráfico ASCII del circuito y la fórmula matemática.
- Explicar la separación crítica de las líneas de alimentación: 5V lógica (USB/Arduino) vs 9V potencia (transformador externo de 2A conectado al pin VM del puente H TB6612FNG) para evitar caídas de tensión ("brownouts").

#### Pestaña 3: 📐 Diseño y Arquitectura
- Explicar la arquitectura de comunicación dual: Control cableado USB de alta prioridad y diagnóstico inalámbrico Wi-Fi pasivo de baja prioridad.
- Mostrar una cuadrícula comparativa entre la Web Serial API y Web Sockets/HTTP.
- Incluir un contenedor con 3 **Flashcards Giratorias en 3D** (tarjetas conceptuales que giran al hacer clic) para repasar:
  1. *Web Serial API*
  2. *SoftwareSerial*
  3. *Estabilidad del Prototipo* (mitigación de OutOfMemory en el ESP32).

#### Pestaña 4: 🧪 Pruebas y Funcionamiento
- Explicar el funcionamiento del mecanismo de seguridad **Watchdog por Software (Timeout)**: la web envía caracteres cada 250 ms y si el Arduino no recibe nada en 500 ms detiene todos los motores.
- Detallar el procedimiento de validación física del monitor inalámbrico en el celular usando el SSID AP `ESP32-Grua-Setup` y la IP `192.168.4.1`.

#### Pestaña 5: 🗣️ Guión de Exposición (Matriz 4x4)
Estructurar el orden de intervención y los textos secuenciales del guión para los 4 integrantes del grupo divididos por las 4 categorías:
1. **Johanan Castro** (Coordinador)
2. **Emilia Fabara** (Frontend)
3. **Renata Duque** (Hardware)
4. **Polteh Morales** (Redes)
*(Cada integrante expone exactamente un subtema por pestaña temaria: diseño, programación, electrónica y pruebas, en bloques bien definidos).*

#### Pestaña 6: ❓ Quiz y Autoevaluación
- **Cuestionario Interactivo**: 4 preguntas de opción múltiple.
- **Retos Prácticos de Ingeniería**: 3 retos prácticos basados en `schema.html`:
  - *Reto 1*: Cambiar el pulsador SW de A3 a D13 (código e implicaciones electrónicas pull-up).
  - *Reto 2*: Reasignar SoftwareSerial TX al pin D10 y modificar el divisor de tensión.
  - *Reto 3*: Mover el control PWM de Elevación de D6 a D3 e intercambiarlo con el Carro para resolver conflictos.
- **Motor de Evaluación en JS**: La función `checkAnswer` debe recibir el ID de pregunta, el índice seleccionado, el índice correcto y una explicación:
  ```javascript
  function checkAnswer(questionNum, optionIndex, correctIndex, explanation)
  ```
  Debe deshabilitar los botones de la pregunta, colorear de verde/rojo la opción seleccionada, resaltar de verde la correcta en caso de error, y mostrar la explicación técnica.
- **Banco de Preguntas Teóricas y Retos**: Añadir debajo del cuestionario una sección colapsable interactiva con un buscador por palabras clave (`input`) y un filtro de categorías (`select`). Este banco contendrá 20 preguntas teóricas detalladas con respuestas ocultas bajo acordeones y 4 retos prácticos de diseño (calibración de joysticks, inversión de giro física/lógica, límites de carrera virtuales y diagnóstico de enlace serie).

Aplica la lógica de filtrado del banco en JavaScript manipulando el display (`block` o `none`) de los elementos con clase `.bank-item` en función de la entrada del usuario y la categoría seleccionada.

```