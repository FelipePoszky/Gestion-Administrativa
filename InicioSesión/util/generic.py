import PIL
from PIL import ImageTk, Image, ImageDraw, ImageFilter


def leer_imagen(path, size):
    return ImageTk.PhotoImage(Image.open(path).resize(size, PIL.Image.Resampling.LANCZOS))


def centrar_ventana(ventana,aplicacion_ancho, aplicacion_largo):
    pantall_ancho = ventana.winfo_screenwidth()
    pantall_largo = ventana.winfo_screenheight()
    x = int((pantall_ancho/2) - (aplicacion_ancho/2))
    y = int((pantall_largo/2) - (aplicacion_largo/2))
    return ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y-20}")


def make_circle_image(path, size=(234, 234), shadow_radius=12, shadow_color=(0,0,0,120)):
    img = Image.open(path).convert("RGBA")
    # Recorta la imagen al cuadrado central
    w, h = img.size
    min_side = min(w, h)
    left = (w - min_side) // 2
    top = (h - min_side) // 2
    right = left + min_side
    bottom = top + min_side
    img = img.crop((left, top, right, bottom))
    # Redimensiona al tamaño final
    img = img.resize(size, Image.LANCZOS)

    # Tamaño con sombra    
    shadow_size = (size[0] + shadow_radius*2, size[1] + shadow_radius*2)

    # Crear fondo transparente para la sombra
    final_img = Image.new("RGBA", shadow_size, (0,0,0,0))

    # Crear la sombra circular
    shadow = Image.new('RGBA', shadow_size, (0,0,0,0))
    shadow_draw = ImageDraw.Draw(shadow)
    shadow_draw.ellipse(
        (shadow_radius, shadow_radius, shadow_radius+size[0], shadow_radius+size[1]),
        fill=shadow_color
    )
    shadow = shadow.filter(ImageFilter.GaussianBlur(radius=shadow_radius))

    # Pegar la sombra en la imagen final
    final_img.paste(shadow, (0,0), shadow)

    # Crear máscara circular para la imagen de perfil
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + size, fill=255)
    img.putalpha(mask)
    # Pegar la imagen de perfil sobre la sombra
    final_img.paste(img, (shadow_radius, shadow_radius), img)

    return ImageTk.PhotoImage(final_img)
