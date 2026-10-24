from io import BytesIO
import os
from PIL import Image, ImageOps
import requests

def procesar_wallpaper_local(nombre_archivo_entrada, ruta_salida):
    try:
        # Construir la ruta completa dentro de la carpeta Descargas actual
        ruta_completa = os.path.expanduser(f"~/Descargas/{"specialHerbs.jpg"}")
        
        print(f"Abriendo imagen desde: {"~/Descargas/"}...")
        
        # Abrir la imagen local
        img = Image.open(ruta_completa)
        
        # Convertir a RGB si es necesario (por ejemplo, si fuera PNG o formato extraño)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
            
        # Resolución exacta para la ThinkPad X1 Carbon (1920x1080)
        ancho_objetivo = 1920
        alto_objetivo = 1080
        
        print("Ajustando a 1920x1080 con alta calidad (LANCZOS)...")
        img_final = ImageOps.fit(
            img, 
            (ancho_objetivo, alto_objetivo), 
            method=Image.Resampling.LANCZOS, 
            centering=(0.5, 0.5)
        )
        
        # Guardar el resultado (por defecto lo guardará también en Descargas)
        ruta_salida_completa = os.path.expanduser(f"~/Descargas/{ruta_salida}")
        img_final.save(ruta_salida_completa, quality=95)
        print(f"¡Listo! Wallpaper guardado con éxito en: {ruta_salida_completa}")
        
    except Exception as e:
        print(f"Ocurrió un error al procesar la imagen: {e}")

# --- EJECUCIÓN ---
# Usa tu imagen 'specialHerbs.jpg' y guarda el resultado como 'wallpaper_specialHerbs.jpg'
procesar_wallpaper_local("specialHerbs.jpg", "wallpaper_specialHerbs.jpg")