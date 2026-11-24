# Echoes-Of-Nexus-Proyecto-Integrador
Proyecto Integrador, Abdiel Montufar, David Davila, Carlos Sukasi 

# Echoes of Nexus

Proyecto integrador de primer nivel · Lógica de Programación · UIDE · Paralelo [B] desarrollado en **Python** que consiste en un videojuego de acción en primera persona basado en *raycasting*[cite: 1]. El proyecto cuenta con un motor propio dividido en módulos para el manejo del mapa, renderizado, jugador, enemigos (NPCs), armas, búsqueda de caminos (*pathfinding*), objetos/sprites y audio[cite: 1].

## Integrantes

- **[Abdiel Montufar]** 
- **[David Dávila]** 
- **[Carlos Sukasi]** 


## Estructura del proyecto

- `main.py`: punto de entrada y bucle principal del juego[cite: 1].
- `settings.py`: configuraciones generales del juego[cite: 1].
- `map.py`: estructura y diseño del mapa[cite: 1].
- `player.py`: lógica y movimiento del jugador[cite: 1].
- `raycasting.py`: cálculo de proyección y renderizado en perspectiva[cite: 1].
- `object_renderer.py` y `sprite_object.py`: renderizado de texturas, elementos visuales y *sprites*[cite: 1].
- `object_handler.py`: administración de objetos, *sprites* y entidades en escena[cite: 1].
- `npc.py` y `pathfinding.py`: comportamiento, estados y rutas de enemigos (incluye recursos visuales de enemigos como *caco_demon*, *cyber_demon* y *soldier*)[cite: 1].
- `weapon.py`: lógica y animaciones de arma (incluye recursos de *shotgun*)[cite: 1].
- `sound.py`: reproducción de música de fondo y efectos de sonido (`resources/sound/`)[cite: 1].
- `resources/`: texturas, *sprites*, dígitos de interfaz, pantallas de victoria/derrota y archivos de audio[cite: 1].
- `requirements.txt`: dependencias del proyecto[cite: 1].

## Cómo ejecutarlo

1. **Extrae el archivo comprimido** `Echoes of nexus.zip` y abre una terminal dentro de la carpeta `Echoes of nexus`[cite: 1].
2. **Verifica que tengas Python instalado** (en el paquete se observan entornos y cachés de Python 3.11 / 3.14; se recomienda Python 3.11+)[cite: 1].
3. **Configura el entorno e instala dependencias**:
   - Si deseas crear un entorno virtual limpio:
     ```bash
     python -m venv .venv
     ```
     Actívalo:
     - **Windows (PowerShell):** `.\.venv\Scripts\Activate.ps1`
     - **Windows (CMD):** `.\.venv\Scripts\activate.bat`
     - **Linux / macOS:** `source .venv/bin/activate`
   - Instala las dependencias listadas en `requirements.txt`[cite: 1]:
     ```bash
     pip install -r requirements.txt
     ```
4. **Inicia el juego** ejecutando `main.py`[cite: 1]:
   ```bash
   python main.py

#CONTROLES DEL JUEGO 

Moverse: [W, A, S, D / Flechas]
Apuntar / Mirar: [Mouse / Teclas]
Disparar: [Clic izquierdo / Barra espaciadora]
Salir: [ESC / Cerrar ventana]


## Trazabilidad con la Fase 2 (Diseño en RAPTOR y Arquitectura)

En esta sección se relaciona el diseño lógico elaborado en la **Fase 2** (*Echoes of the Nexus*)[cite: 2] con los módulos implementados en el código de **Python** (`Echoes of nexus`)[cite: 1]. *(Completa los rangos de líneas `[Líneas X-Y]` revisando cada archivo en tu editor)[cite: 1].*

### Tabla de trazabilidad: Diagrama de la Fase 2, Archivo y líneas, y Qué cambió

| Diagrama de la Fase 2 | Archivo y líneas | Qué cambió |
| :--- | :--- | :--- |
| **DF1: Partida completa** (`DF1_partida.rap`) — Menú Jugar/Salir, inicialización de variables, turnos y cierre de partida[cite: 6] | `main.py` `[Líneas X-Y]`<br>`settings.py` `[Líneas X-Y]`[cite: 1] | Se reemplazó la lectura de consola (`GET opcion`) y el flujo secuencial de texto por el bucle principal del videojuego, la gestión de eventos y la inicialización de configuración y ventana[cite: 1, 6]. |
| **DF2: Validación de la jugada** (`DF2_validacion.rap`) — Ataque del jugador, daño y evaluación de vida $\le 0$[cite: 7, 9] | `player.py` `[Líneas X-Y]`<br>`weapon.py` `[Líneas X-Y]`<br>`npc.py` `[Líneas X-Y]`[cite: 1] | El ataque pasó de ser una respuesta de texto (`¿Desea disparar? ("si")`) con daño directo en consola a ejecutarse mediante controles del jugador, lógica/animación de arma y actualización de vida y estados de los NPCs[cite: 1, 9]. |
| **DF3: Fin de la partida** (`DF3_fin.rap` / `diagrama_juego.rap`) — Condiciones de victoria/derrota y cierre[cite: 10, 14] | `main.py` `[Líneas X-Y]`<br>`object_renderer.py` `[Líneas X-Y]`[cite: 1] | Se adaptó la detección de fin de partida a las condiciones reales del juego y se sustituyeron los mensajes `PUT` de consola por el renderizado visual en pantalla (`win.png` y `game_over.png`)[cite: 1, 10, 11]. |
| **Arquitectura Cliente-Servidor (LAN)** — Gestión de estado, turnos y comunicación entre Jugador 1 y Jugador 2[cite: 19, 20] | `main.py` `[Líneas X-Y]`<br>`object_handler.py` `[Líneas X-Y]`<br>`map.py` `[Líneas X-Y]`[cite: 1] | La arquitectura de red LAN TCP (puerto 5000) diseñada en la Fase 2 se contrasta con la implementación local en Python, donde el mapa, los *sprites* y el manejo de objetos/enemigos operan directamente dentro del motor del juego[cite: 1, 19, 20]. |

### Resumen de cambios respecto a la Fase 2

* **De consola (`GET` / `PUT`) a entorno visual e interactivo:** En los diagramas de RAPTOR las entradas y salidas se representaban como lecturas y mensajes de texto (`GET opcion`, `GET disparar`, `PUT ...`), mientras que en Python el juego utiliza renderizado gráfico, *sprites*, texturas, sonidos y controles en tiempo real[cite: 1, 6, 9].
* **Evolución de la lógica de combate y entidades:** Mientras `DF2_validacion.rap` modelaba un combate simplificado con valores fijos (`player`, `enemy`, `daplayer`, `daenemy`) y `DF3_fin.rap` / `diagrama_juego.rap` evaluaba puntuaciones o condiciones básicas de victoria/fin, el código en Python incorpora movimiento, *raycasting*, búsqueda de caminos (*pathfinding*), animaciones de arma y distintos tipos de enemigos (*caco_demon*, *cyber_demon*, *soldier*)[cite: 1, 9, 10, 14].
* **Ajustes en reglas, turnos y estado de la partida:** Durante el diseño en RAPTOR se definieron variables de control (`turno`, `opcion`, `juego_terminado`, `player1`, `player2`, `enemy1`, `attack1`) y condiciones de salida para evitar ciclos infinitos o datos residuales; al llevarlo a Python, el estado del juego se organiza en módulos especializados (`player.py`, `npc.py`, `weapon.py`, `object_handler.py`, `main.py`) según las mecánicas implementadas[cite: 1, 5, 11, 21].

## Licencia
Este proyecto se distribuye bajo la licencia MIT. El texto completo está en el archivo `LICENSE`.

## Declaración de autoría
Declaramos que el código de este repositorio fue escrito por los integrantes del equipo (**Abdiel Montúfar**, **David Dávila** y **Carlos Sukasi**), salvo los recursos citados en la sección «Créditos»[cite: 2].

## Créditos
| Recurso (código, librería, imagen…) | Autor o fuente | Dónde se usa | Licencia |
|---|---|---|---|
| Pygame (`pygame`) | Comunidad Pygame | Ventana, bucle de eventos, gráficos y sonido (`main.py`, `sound.py`, `object_renderer.py`)[cite: 1] | LGPL |
| *Sprites* de enemigos, arma y objetos (`caco_demon`, `cyber_demon`, `soldier`, `shotgun`, `green_light`, `red_light`, `candlebra`) | Recursos gráficos del proyecto / estilo *Doom* clásico[cite: 1] | Entidades, animaciones y objetos en escena (`resources/sprites/`, `object_handler.py`, `sprite_object.py`, `npc.py`, `weapon.py`)[cite: 1] | [Uso académico / Por verificar] |
| Texturas, dígitos de interfaz y pantallas (`1.png`–`5.png`, `sky.png`, `blood_screen.png`, `digits/`, `win.png`, `game_over.png`) | Recursos visuales del proyecto[cite: 1] | Escenarios, HUD y estados de victoria/derrota (`resources/textures/`, `object_renderer.py`)[cite: 1] | [Uso académico / Por verificar] |
| Música y efectos de sonido (`theme.mp3`, `shotgun.wav`, `npc_attack.wav`, `npc_death.wav`, `npc_pain.wav`, `player_pain.wav`) | Recursos de audio del proyecto[cite: 1] | Música de fondo y sonidos de combate (`resources/sound/`, `sound.py`)[cite: 1] | [Uso académico / Por verificar] |

### Uso de IA
| Herramienta | Para qué la usamos | Qué revisamos o cambiamos nosotros |
|---|---|---|
| Asistente de IA (Gemini)[cite: 21] | Apoyo en el diseño de la lógica de programación en RAPTOR, estructura de arquitectura cliente-servidor LAN y redacción/organización de la documentación del proyecto (`README.md` y guion de presentación)[cite: 21]. | Validamos los diagramas en RAPTOR, revisamos el funcionamiento real del juego en Python, completamos los rangos de líneas del código y verificamos la estructura de archivos y recursos[cite: 1, 21]. |


