# TuPrimeraPagina-Leonardo

## Descripción
Proyecto Django con patrón MVT que incluye:
- Herencia de HTML.
- 3 clases en models: `Categoria`, `Autor`, `Publicacion`.
- Formulario para insertar datos por cada modelo.
- Formulario para buscar publicaciones en la base de datos.

## Funcionalidades
1. **Inicio:** Página principal con enlaces a las opciones.
2. **Nueva Categoría:** Formulario para crear categorías.
3. **Nuevo Autor:** Formulario para crear autores.
4. **Nueva Publicación:** Formulario para crear publicaciones.
5. **Buscar Publicación:** Permite buscar publicaciones en la base de datos.

## Cómo probarlo
1️⃣ Clonar el repo  
2️⃣ Crear entorno virtual  
3️⃣ Correr migraciones  
4️⃣ Levantar servidor con `python manage.py runserver`

---

## Orden para probar en el navegador
- `127.0.0.1:8000/` → Inicio  
- `127.0.0.1:8000/categoria/nueva/`  
- `127.0.0.1:8000/autor/nuevo/`  
- `127.0.0.1:8000/publicacion/nueva/`  
- `127.0.0.1:8000/publicacion/buscar/`
