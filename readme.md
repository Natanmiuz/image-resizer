¡Por supuesto! Aquí tienes un README completo y profesional en español para el proyecto Natanmiuz/image-resizer, asumiendo que es un redimensionador de imágenes en Python y siguiendo las mejores prácticas. Si necesitas personalizar alguna sección (como instrucciones de despliegue o ejemplos de uso específicos), dime y lo adapto.

---

# Image Resizer

## Descripción

**Image Resizer** es una herramienta escrita en Python para redimensionar imágenes de forma sencilla y eficiente. Permite a los usuarios ajustar el tamaño de múltiples imágenes en lote, mantener la relación de aspecto y guardar los resultados en un directorio específico. Es ideal para fotógrafos, desarrolladores web y cualquier persona que necesite procesar grandes cantidades de imágenes.

## Características

- Redimensionamiento de imágenes individual o por lotes.
- Mantiene la relación de aspecto automáticamente o permite personalizarla.
- Soporte para formatos de imagen comunes: JPEG, PNG, BMP, GIF, entre otros.
- Especifica dimensiones exactas o porcentaje de escalado.
- Guarda las imágenes redimensionadas en un directorio de salida.
- Interfaz de línea de comandos fácil de usar.
- Código limpio y ampliamente documentado.

## Requisitos

- Python 3.7 o superior
- [Pillow](https://python-pillow.org/) (biblioteca para el procesamiento de imágenes)

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/Natanmiuz/image-resizer.git
   cd image-resizer
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

Puedes utilizar el script principal desde la terminal. Aquí tienes algunos ejemplos:

### Redimensionar una sola imagen

```bash
python resize.py --input imagen.jpg --output salida.jpg --width 800 --height 600
```

### Redimensionar todas las imágenes de una carpeta manteniendo la relación de aspecto

```bash
python resize.py --input-dir ./imagenes --output-dir ./redimensionadas --width 1024
```

### Redimensionar por porcentaje

```bash
python resize.py --input imagen.jpg --output salida.jpg --scale 0.5
```

### Opciones disponibles

| Parámetro         | Descripción                                                  | Obligatorio |
|-------------------|-------------------------------------------------------------|:-----------:|
| `--input`         | Archivo de imagen a redimensionar                           | Sí (o `--input-dir`) |
| `--output`        | Archivo de salida para la imagen redimensionada             | Sí (o `--output-dir`)|
| `--input-dir`     | Carpeta con imágenes a redimensionar                        | Sí (o `--input`)     |
| `--output-dir`    | Carpeta donde guardar las imágenes redimensionadas          | Sí (o `--output`)    |
| `--width`         | Nuevo ancho en píxeles                                      | No          |
| `--height`        | Nueva altura en píxeles                                     | No          |
| `--scale`         | Escalado proporcional (ej.: 0.5 = 50%)                      | No          |
| `--keep-aspect`   | Mantener relación de aspecto (por defecto: True)            | No          |

## Ejemplo de uso

```bash
python resize.py --input-dir ./fotos_viaje --output-dir ./fotos_redimensionadas --width 800 --keep-aspect
```

## Contribuir

¡Las contribuciones son bienvenidas! Por favor, abre un issue o un pull request para sugerencias, reportar errores o proponer mejoras.

1. Haz un fork del repositorio.
2. Crea una rama para tu función o corrección.
3. Haz tus cambios y asegúrate de que pasan los tests (si existen).
4. Envía un pull request explicando tus cambios.

## Licencia

LICENCIA DE LIBRE USO, NO BUSCAMOS NI RECONOCIMIENTO NI PLATA.

## Autor

Desarrollado por [Natanmiuz](https://github.com/Natanmiuz).

---

¿Quieres que adapte el README a un framework específico (por ejemplo, interfaz gráfica), o deseas que incluya ejemplos avanzados? Si necesitas el archivo en formato Markdown listo para copiar y pegar, házmelo saber.
