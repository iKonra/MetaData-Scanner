# Meta-Data Scanner

Meta-Data Scanner es una herramienta en Python para extraer y mostrar los metadatos EXIF de imágenes. Usa la biblioteca **Pillow** para leer los metadatos y **Colorama** para resaltar la salida en la terminal.

## 📌 Características
- Extrae metadatos EXIF de imágenes.
- Soporta datos de tipo texto y binarios.
- Formato de salida en consola con colores.
- Fácil de usar, solo requiere ingresar el nombre del archivo.

## 📂 Instalación
Asegúrate de tener Python 3 instalado y ejecuta el siguiente comando para instalar las dependencias necesarias:

```sh
pip install pillow colorama pyfiglet
```

## 🚀 Uso
Coloca las imágenes dentro de la carpeta `MetaData/` y ejecuta el script:

```sh
python script.py
```

Luego, ingresa el nombre del archivo de imagen con su extensión. Ejemplo:
```
Enter the image filename (with extension): foto.jpg
```
Si la imagen tiene metadatos EXIF, se mostrarán en la terminal.

## 📜 Ejemplo de Salida
```
--- Metadata Found ---
ImageWidth               : 4128
ImageLength              : 1908
Make                     : samsung
Model                    : SM-M205F
Software                 : M205FDDS8CUC1
DateTime                 : 2021:06:18 12:08:37
```



