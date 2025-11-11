# 🖥️ Proyecto de Gestión Administrativa - Mini Market

**Descripción**  
Aplicación de escritorio desarrollada en **Python** con **Tkinter** para la gestión administrativa de un Mini Market. El software permite llevar el control de compras, ventas, inventario, proveedores y análisis financiero con visualizaciones gráficas.

---

## 🧩 Tecnologías Destacadas
- **Lenguaje:** Python  
- **GUI:** Tkinter  
- **Diseño UI:** Figma  
- **Base de datos:** SQLite3  
- **Gráficos y Análisis:** Matplotlib, NumPy

---

## ⚙️ Funcionalidades Principales
- 🧾 Visualización de tablas: **compras**, **ventas**, **productos**, **proveedores**.  
- **CRUD** completo (Crear, Leer, Actualizar, Eliminar) en las tablas.  
- 📊 Visualización de gráficos:
  - Gráfica de línea: evolución de ventas.
  - Gráfica de barras: comparación compras vs. ventas.
  - Gráfica de dona: Top 8 productos más vendidos.
  - Gráfica de dona: Top proveedores por volumen de compras.
  - Análisis de métricas: **ventas**, **COGS**, **beneficios**, **ganancias**.  
  - Tabla de estado de stock e inventario con alertas (según configuración).  
- Gestión y personalización de la cuenta y datos del local.  
- Rol de **administrador** con capacidad para supervisar y gestionar otros usuarios.

---

## 📸 Capturas de Pantalla de las Funcionalidades
> Coloca tus imágenes en la carpeta `ScreenShot/` en la raíz del repositorio con los nombres indicados.

- **Menú Principal** - `ScreenShot/main-menu.png`  
  ![Main Menu](./ScreenShot/main-menu.png)

- **Página de Chats / Panel Principal** - `ScreenShot/chats-page.png`  
  ![Chats Page](./ScreenShot/chats-page.png)

- **Página de Quizzes / Módulo de Análisis** - `ScreenShot/quizzes-page.png`  
  ![Quizzes Page](./ScreenShot/quizzes-page.png)

- **Página de Perfil / Estadísticas** - `ScreenShot/perfil-page.png`  
  ![Perfil Page](./ScreenShot/perfil-page.png)

- **Ajustes - Cambio de Contraseña** - `ScreenShot/ajustes-page1.png`  
  ![Ajustes Contraseña](./ScreenShot/ajustes-page1.png)

- **Ajustes - Cambio de Tema Claro/Oscuro** - `ScreenShot/ajustes-page2.png`  
  ![Ajustes Tema](./ScreenShot/ajustes-page2.png)

- **Crear Nuevo Chat / Selección de Modelo** - `ScreenShot/ej-newChat.png`  
  ![Nuevo Chat](./ScreenShot/ej-newChat.png)

- **Crear Nuevo Quiz / Selección de Contexto y Dificultad** - `ScreenShot/ej-newQuiz.png`  
  ![Nuevo Quiz](./ScreenShot/ej-newQuiz.png)

- **Ejemplo de Conversación (Chat DSA)** - `ScreenShot/chat-dsa.png`  
  ![Chat DSA](./ScreenShot/chat-dsa.png)

> Nota: Si tu repo es sólo para la aplicación Tkinter, reemplaza las rutas y nombres de imágenes por los correspondientes a Screenshots del software (ej. `ScreenShot/ventas.png`, `ScreenShot/inventario.png`, etc.). Las imágenes aquí son ejemplos de estructura.

---

## 🗂️ Estructura sugerida del repositorio

```
proyecto-mini-market/
├── app/                     # Código fuente de la aplicación
│   ├── main.py
│   └── ...
├── db/                      # Scripts o backups de la base de datos SQLite
├── docs/                    # Documentación, casos de uso, diagramas
├── ScreenShot/              # Las capturas que se muestran en el README
├── requirements.txt         # Dependencias, si aplica
└── README.md
```

---

## 📚 Notas Académicas
Este proyecto fue realizado como parte de la asignatura anual **Ingeniería de Software I y II**, con una contraparte real y bajo la supervisión constante del docente. Se aplicaron metodologías formales: levantamiento de requerimientos, informe técnico, casos de uso y vistas arquitectónicas (4+1).

---

## ⚙️ Cómo ejecutar (ejemplo)
1. Clona el repositorio:
```bash
git clone https://github.com/usuario/proyecto-mini-market.git
cd proyecto-mini-market
```
2. (Opcional) Crear y activar entorno virtual:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```
3. Instalar dependencias (si aplica):
```bash
pip install -r requirements.txt
```
4. Ejecutar la aplicación:
```bash
python app/main.py
```

---

## 📫 Contacto
Si te interesa conocer más sobre el proyecto o colaborar:
- **Email:** tu_correo@example.com  
- **LinkedIn:** https://www.linkedin.com/in/tu-perfil

---
