import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import json
import shutil
import webbrowser
import os.path
from PIL import ImageTk, Image, ImageFont, ImageDraw


# ----------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------- #


def crop_imageitems(imageitems, max_widthitems, max_heightitems):
    widthitems, heightitems = imageitems.size
    if widthitems > max_widthitems or heightitems > max_heightitems:
        leftitems = 0
        topitems = 0
        rightitems = min(widthitems, max_widthitems)
        bottomitems = min(heightitems, max_heightitems)
        imageitems = imageitems.crop((leftitems, topitems, rightitems, bottomitems))
    return imageitems

def multiply_coordinatesitems(image_dictitems, factoritems):
    multiplied_image_dictitems = {}
    for image_pathitems, positionitems in image_dictitems.items():
        multiplied_positionitems = tuple(coorditems * factoritems for coorditems in positionitems)
        multiplied_image_dictitems[image_pathitems] = multiplied_positionitems
    return multiplied_image_dictitems

def merge_imagesitems(image_dictitems, items_image, max_widthitems, max_heightitems, output_pathitems):
    items = Image.open(items_image)

    for image_pathitems, positionitems in image_dictitems.items():
        if os.path.isfile(image_pathitems):
            imageitems = Image.open(image_pathitems)
            imageitems = crop_imageitems(imageitems, max_widthitems, max_heightitems)
            items.paste(imageitems, positionitems)
        else:
            print(f"L'image {image_pathitems} n'existe pas.")

    # Sauvegarder l'image fusionnée en remplaçant l'image "items.png"
    items.save(output_pathitems)
    text_console.insert(tk.INSERT, "items.png converted at            output/items.png\n")
    text_console.insert(tk.INSERT, "----------------------------------\n")
    text_console.see(tk.END)

def resize_imageitems(input_pathitems, output_pathitems, new_widthitems, new_heightitems):
    if os.path.isfile(input_pathitems):
        imageitems = Image.open(input_pathitems)
        resized_imageitems = imageitems.resize((new_widthitems, new_heightitems), Image.LANCZOS)
        resized_imageitems.save(output_pathitems)
    else:
        print(f"L'image {input_pathitems} n'existe pas.")

def process_imagesitems():
    # Charger le terrain à partir du fichier JSON
    with open("assets/json/items.json", 'r') as items:
        image_dictitems = json.load(items)

    # Chemin de l'image de terrain d'origine
    terrain_input_pathitems = "assets/texture/items.png"

    # Chemin de sortie pour l'image de terrain fusionnée
    terrain_output_pathitems = "output/items.png"

    # Copie de l'image de terrain vers le répertoire de sortie
    shutil.copyfile(terrain_input_pathitems, terrain_output_pathitems)

    # Multiplier les coordonnées par 2
    image_dictitems = multiply_coordinatesitems(image_dictitems, 1)

    # Appel de la fonction pour fusionner les images sur items.png
    merge_imagesitems(image_dictitems, terrain_output_pathitems, 16, 16, terrain_output_pathitems)


# ----------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------- #


def crop_imageterrain(imageterrain, max_widthterrain, max_heightterrain):
    widthterrain, heightterrain = imageterrain.size
    if widthterrain > max_widthterrain or heightterrain > max_heightterrain:
        leftterrain = 0
        topterrain = 0
        rightterrain = min(widthterrain, max_widthterrain)
        bottomterrain = min(heightterrain, max_heightterrain)
        imageterrain = imageterrain.crop((leftterrain, topterrain, rightterrain, bottomterrain))
    return imageterrain

def multiply_coordinatesterrain(image_dict_terrain, factor_terrain):
    multiplied_image_dict_terrain = {}
    for image_path_terrain, coordinates_terrain in image_dict_terrain.items():
        if isinstance(coordinates_terrain[0], list):
            multiplied_coordinates_terrain = [(coord[0] * factor_terrain, coord[1] * factor_terrain) for coord in coordinates_terrain]
        else:
            multiplied_coordinates_terrain = [(coordinates_terrain[0] * factor_terrain, coordinates_terrain[1] * factor_terrain)]
        multiplied_image_dict_terrain[image_path_terrain] = multiplied_coordinates_terrain
    return multiplied_image_dict_terrain

def merge_imagesterrain(image_dictterrain, terrain_image, max_widthterrain, max_heightterrain, output_pathterrain):
    terrain = Image.open(terrain_image)

    for image_pathterrain, positionsterrain in image_dictterrain.items():
        if os.path.isfile(image_pathterrain):
            for positionterrain in positionsterrain:
                imageterrain = Image.open(image_pathterrain)
                cropped_imageterrain = crop_imageterrain(imageterrain, max_widthterrain, max_heightterrain)
                terrain.paste(cropped_imageterrain, positionterrain)
        else:
            print(f"L'image {image_pathterrain} n'existe pas.")

    # Sauvegarder l'image fusionnée en remplaçant l'image "terrain.png"
    terrain.save(output_pathterrain)
    text_console.insert(tk.INSERT, "terrain.png converted at          output/terrain.png\n")
    text_console.insert(tk.INSERT, "----------------------------------\n")
    text_console.see(tk.END)

def resize_imageterrain(input_pathterrain, output_pathterrain, new_widthterrain, new_heightterrain):
    if os.path.isfile(input_pathterrain):
        imageterrain = Image.open(input_pathterrain)
        resized_imageterrain = imageterrain.resize((new_widthterrain, new_heightterrain), Image.LANCZOS)
        resized_imageterrain.save(output_pathterrain)
    else:
        print(f"L'image {input_pathterrain} n'existe pas.")

def process_imagesterrain():
    multiplier_strterrain = x_multiplierterrain.get()

    if multiplier_strterrain == "x16":
        multiplierterrain = 1
        terrain_image_path = "assets/texture/terrain.png"
    elif multiplier_strterrain == "x32":
        multiplierterrain = 2
        terrain_image_path = "assets/texture/terrain32.png"
    else:
        return
    # Dictionnaire des images avec leurs positions

    with open('assets/json/terrain.json', 'r') as terrain:
        image_dictterrain = json.load(terrain)
    # Chemin de l'image de sortie
    terrain_output_path = "output/terrain.png"

    # Copie de l'image de terrain vers le répertoire de sortie
    shutil.copyfile(terrain_image_path, terrain_output_path)

    # Multiplier les coordonnées par le facteur choisi (x16 ou x32)
    image_dictterrain = multiply_coordinatesterrain(image_dictterrain, multiplierterrain)

    # Appel de la fonction pour fusionner les images sur terrain.png
    merge_imagesterrain(image_dictterrain, terrain_output_path, 16 * multiplierterrain, 16 * multiplierterrain, terrain_output_path)


    # Redimensionner terrainMipMapLevel2.png en 128x272 ou 256x544
    resize_imageterrain(terrain_output_path, "output/terrainMipMapLevel2.png", 128 * multiplierterrain, 272 * multiplierterrain)
    text_console.insert(tk.INSERT, "terrainMipMapLevel2.png converted output/terrainMipMapLevel2.png\n")
    text_console.insert(tk.INSERT, "----------------------------------\n")
    text_console.see(tk.END)

    # Copier et redimensionner terrainMipMapLevel2.png pour terrainMipMapLevel3.png
    shutil.copyfile("output/terrainMipMapLevel2.png", "output/terrainMipMapLevel3.png")
    resize_imageterrain("output/terrainMipMapLevel3.png", "output/terrainMipMapLevel3.png", 64 * multiplierterrain, 136 * multiplierterrain)
    text_console.insert(tk.INSERT, "terrainMipMapLevel3.png converted output/terrainMipMapLevel3.png\n")
    text_console.insert(tk.INSERT, "----------------------------------\n")
    text_console.see(tk.END)


# ----------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------- #


def multiply_coordinatesparticles(image_dictparticles, factorparticles):
    multiplied_image_dictparticles = {}
    for image_pathparticles, positionsparticles in image_dictparticles.items():
        if isinstance(positionsparticles[0], list):
            multiplied_positionsparticles = [(coordparticles[0] * factorparticles, coordparticles[1] * factorparticles) for coordparticles in positionsparticles]
        else:
            multiplied_positionsparticles = [(positionsparticles[0] * factorparticles, positionsparticles[1] * factorparticles)]
        multiplied_image_dictparticles[image_pathparticles] = multiplied_positionsparticles
    return multiplied_image_dictparticles

def merge_imagesparticles(image_dictparticles, particle_image, max_widthparticles, max_heightparticles, output_pathparticles):
    particle = Image.open(particle_image)

    for image_pathparticles, positionsparticles in image_dictparticles.items():
        if os.path.isfile(image_pathparticles):
            for positionparticles in positionsparticles:
                imageparticles = Image.open(image_pathparticles)
                particle.paste(imageparticles, positionparticles)
        else:
            print(f"L'image {image_pathparticles} n'existe pas.")

    # Sauvegarder l'image fusionnée en remplaçant l'image "particles.png"
    particle.save(output_pathparticles)

    text_console.insert(tk.INSERT, "particles.png converted at        output/particles.png\n")
    text_console.insert(tk.INSERT, "----------------------------------\n")
    text_console.see(tk.END)

def resize_imageparticles(input_pathparticles, output_pathparticles, new_widthparticles, new_heightparticles):
    if os.path.isfile(input_pathparticles):
        imageparticles = Image.open(input_pathparticles)
        resized_imageparticles = imageparticles.resize((new_widthparticles, new_heightparticles), Image.LANCZOS)
        resized_imageparticles.save(output_pathparticles)
    else:
        print(f"L'image {input_pathparticles} n'existe pas.")

def process_images():
    multiplier_strparticles = x_multiplierparticles.get()

    if multiplier_strparticles == "x8":
        multiplierparticles = 1
        particle_image_path = "assets/texture/particles.png"
    elif multiplier_strparticles == "x16":
        multiplierparticles = 2
        particle_image_path = "assets/texture/particles16.png"
    elif multiplier_strparticles == "x32":
        multiplierparticles = 4
        particle_image_path = "assets/texture/particles32.png"
    elif multiplier_strparticles == "x64":
        multiplierparticles = 8
        particle_image_path = "assets/texture/particles64.png"
    else:
        return

    #liste d'images
    with open("assets/json/particles.json", 'r') as particles:
        image_dictparticles = json.load(particles) 

    # Chemin de l'image de sortie
    particle_output_path = "output/particles.png"

    # Copie de l'image de particle vers la sortie
    shutil.copyfile(particle_image_path, particle_output_path)

    # Multiplier les coordonnées par le facteur choisi (x16 ou x32...)
    image_dictparticles = multiply_coordinatesparticles(image_dictparticles, multiplierparticles)

    # Appel de la fonction pour fusionner les images sur particles.png
    merge_imagesparticles(image_dictparticles, particle_output_path, 16 * multiplierparticles, 16 * multiplierparticles, particle_output_path)


# ----------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------- #


def multiply_coordinatespainting(image_dictpainting, factorpainting):
    multiplied_image_dictpainting = {}
    for image_pathpainting, positionspainting in image_dictpainting.items():
        if isinstance(positionspainting[0], list):
            multiplied_positionspainting = [[coordpainting[0] * factorpainting, coordpainting[1] * factorpainting] for coordpainting in positionspainting]
        else:
            multiplied_positionspainting = [(coordpainting[0] * factorpainting, coordpainting[1] * factorpainting) for coordpainting in positionspainting]
        multiplied_image_dictpainting[image_pathpainting] = multiplied_positionspainting
    return multiplied_image_dictpainting

def merge_imagespainting(image_dictpainting, painting_image, max_widthpainting, max_heightpainting, output_pathpainting):
    painting = Image.open(painting_image)

    for image_pathpainting, positionspainting in image_dictpainting.items():
        if os.path.isfile(image_pathpainting):
            for positionpainting in positionspainting:
                imagepainting = Image.open(image_pathpainting)
                painting.paste(imagepainting, positionpainting)
        else:
            print(f"L'image {image_pathpainting} n'existe pas.")

    # Sauvegarder l'image fusionnée en remplaçant l'image "kz.png"
    painting.save(output_pathpainting)

    text_console.insert(tk.INSERT, "kz.png converted at output/kz.png\n")
    text_console.insert(tk.INSERT, "----------------------------------\n")
    text_console.see(tk.END)

def resize_imagepainting(input_pathpainting, output_pathpainting, new_widthpainting, new_heightpainting):
    if os.path.isfile(input_pathpainting):
        imagepainting = Image.open(input_pathpainting)
        resized_imagepainting = imagepainting.resize((new_widthpainting, new_heightpainting), Image.LANCZOS)
        resized_imagepainting.save(output_pathpainting)
    else:
        print(f"L'image {input_pathpainting} n'existe pas.")

def process_imagespainting():
    multiplier_strpainting = x_multiplierpainting.get()

    if multiplier_strpainting == "x16":
        multiplierpainting = 1
        painting_image_pathpainting = "assets/texture/kz.png"
    elif multiplier_strpainting == "x32":
        multiplierpainting = 2
        painting_image_pathpainting = "assets/texture/kz32.png"
    elif multiplier_strpainting == "x64":
        multiplierpainting = 4
        painting_image_pathpainting = "assets/texture/kz64.png"
    elif multiplier_strpainting == "x128":
        multiplierpainting = 8
        painting_image_pathpainting = "assets/texture/kz128.png"
    else:
        return

    #liste d'images
    with open("assets/json/painting.json", 'r') as painting:
        image_dictpainting = json.load(painting) 

    # Chemin de l'image de sortie
    painting_output_path = "output/kz.png"

    # Copie de l'image de painting vers la sortie
    shutil.copyfile(painting_image_pathpainting, painting_output_path)

    # Multiplier les coordonnées par le facteur choisi (x16 ou x32...)
    image_dictpainting = multiply_coordinatespainting(image_dictpainting, multiplierpainting)

    # Appel de la fonction pour fusionner les images sur kz.png
    merge_imagespainting(image_dictpainting, painting_output_path, 16 * multiplierpainting, 16 * multiplierpainting, painting_output_path)


# ----------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------- #


# Créer l'app
TextureApp = tk.Tk()
TextureApp.title("Texture Pack Converter Java to LCE")
icon_path = os.path.abspath("assets/icon.ico")
TextureApp.iconbitmap(icon_path)
TextureApp.geometry("380x380")
TextureApp.resizable(False, False)

# ------------------------------------------

# Load images
youtube_image_path = os.path.abspath("assets/youtube.png")
youtube_image = Image.open(youtube_image_path)
youtube_image_size = youtube_image.resize((23, 20), Image.LANCZOS)
youtube_photo_image = ImageTk.PhotoImage(youtube_image_size)

discord_image_path = os.path.abspath("assets/discord.png")
discord_image = Image.open(discord_image_path)
discord_image_size = discord_image.resize((23, 20), Image.LANCZOS)
discord_photo_image = ImageTk.PhotoImage(discord_image_size)

github_image_path = os.path.abspath("assets/github.png")
github_image = Image.open(github_image_path)
github_image_size = github_image.resize((23, 20), Image.LANCZOS)
github_photo_image = ImageTk.PhotoImage(github_image_size)

# Load Font 
font_mojangles = os.path.abspath("assets/Mojangles.ttf")

# ------------------------------------------

#   **--Background--**

# Global Background
background = tk.Label(TextureApp, bg="#383838")
background.place(x=0, y=0, width=380, height=400)

# Title Border Background
app_title_background_border = tk.Label(TextureApp, bg="#000000")
app_title_background_border.place(x=0, y=38, width=380, height=2)
app_title_background_border.lift()

# Background Youtube Discord
bacground_info_bottom = tk.Label(TextureApp, bg="#585858")
bacground_info_bottom.place(x=0, y=350, width=380, height=30)
bacground_info_bottom.lift()
bacground_info_bottom_border = tk.Label(TextureApp, bg="#000000")
bacground_info_bottom_border.place(x=0, y=419, width=380, height=2)
bacground_info_bottom_border.lift()


# ------------------------------------------
# ------------------------------------------
# ------------------------------------------


# Créer le bouton de la conversion
process_buttonitems = tk.Button(TextureApp, text="Convert Items (x16)", command=process_imagesitems)
process_buttonitems.place(x=127.5, y=62)
process_buttonitems.configure(relief="solid", bd=2)


# ------------------------------------------
# ------------------------------------------
# ------------------------------------------


# Créer le bouton pour choisir la conversion
convert_buttonterrain = tk.Button(TextureApp, text="Convert Blocks", command=process_imagesterrain)
convert_buttonterrain.place(x=95, y=102)
convert_buttonterrain.configure(relief="solid", bd=2)
# Définir les options pour le menu déroulant (x16 et x32)
optionsterrain = ["x16", "x32"]
# Déclarez x_multiplier comme une variable de chaîne
x_multiplierterrain = tk.StringVar()
x_multiplierterrain.set(optionsterrain[0])  # Par défaut, x16 est sélectionné

dropdown_menuterrain = tk.OptionMenu(TextureApp, x_multiplierterrain, *optionsterrain)
dropdown_menuterrain.place(x=210, y=99)
dropdown_menuterrain.configure(relief="solid", bd=2)

# Action de clic pour le bouton x16
def x16_button_clickterrain():
    x_multiplierterrain.set(1)
    convert_buttonterrain.config(text="Convert Blocks (x16)")

# Action de clic pour le bouton x32
def x32_button_clickterrain():
    x_multiplierterrain.set(2)
    convert_buttonterrain.config(text="Convert Blocks (x32)")


# ------------------------------------------
# ------------------------------------------
# ------------------------------------------


# bouton pour choisir la conversion
convert_buttonparticles = tk.Button(TextureApp, text="Convert Particles", command=process_images)
convert_buttonparticles.place(x=95, y=142)
convert_buttonparticles.configure(relief="solid", bd=2)

# Définir les options pour le menu déroulant (x16 / x32...)
optionsparticles = ["x8", "x16", "x32", "x64"]

# Déclarez x_multiplier comme une variable de chaîne
x_multiplierparticles = tk.StringVar()
x_multiplierparticles.set(optionsparticles[0])  # Par défaut x16

dropdown_menuparticles = tk.OptionMenu(TextureApp, x_multiplierparticles, *optionsparticles)
dropdown_menuparticles.place(x=210, y=139)
dropdown_menuparticles.configure(relief="solid", bd=2)

# Action de clic pour le bouton x16 et autres
def x16_button_clickparticles():
    x_multiplierparticles.set(1)
    convert_buttonparticles.config(text="Convert Particles (x8)")

def x32_button_clickparticles():
    x_multiplierparticles.set(2)
    convert_buttonparticles.config(text="Convert Particles (x16)")

def x32_button_clickparticles():
    x_multiplierparticles.set(4)
    convert_buttonparticles.config(text="Convert Particles (x32)")

def x32_button_clickparticles():
    x_multiplierparticles.set(8)
    convert_buttonparticles.config(text="Convert Particles (x64)")


# ------------------------------------------
# ------------------------------------------
# ------------------------------------------


# bouton pour choisir la conversion
convert_buttonpainting = tk.Button(TextureApp, text="Convert Paintings", command=process_imagespainting)
convert_buttonpainting.place(x=95, y=182)
convert_buttonpainting.configure(relief="solid", bd=2)

# Définir les options pour le menu déroulant (x16 / x32...)
optionspainting = ["x16", "x32", "x64", "x128"]

# Déclarez x_multiplier comme une variable de chaîne
x_multiplierpainting = tk.StringVar()
x_multiplierpainting.set(optionspainting[0])  # Par défaut x16

dropdown_menupainting = tk.OptionMenu(TextureApp, x_multiplierpainting, *optionspainting)
dropdown_menupainting.place(x=210, y=179)
dropdown_menupainting.configure(relief="solid", bd=2)

# Action de clic pour le bouton x16 et autres
def x16_button_clickpainting():
    x_multiplierpainting.set(1)
    convert_buttonpainting.config(text="Convert Painting (x16)")

def x32_button_clickpainting():
    x_multiplierpainting.set(2)
    convert_buttonpainting.config(text="Convert Painting (x32)")

def x32_button_clickpainting():
    x_multiplierpainting.set(4)
    convert_buttonpainting.config(text="Convert Painting (x64)")

def x32_button_clickpainting():
    x_multiplierpainting.set(8)
    convert_buttonpainting.config(text="Convert Painting (x128)")
# ------------------------------------------
# ------------------------------------------
# ------------------------------------------


# Créer le widget ScrolledText
text_console = ScrolledText(TextureApp, width=34, height=7)
text_console.place(x=42.5, y=223)
text_console.insert(tk.INSERT, "Version : 1.3 - Check if any      update have been made.\n")
text_console.insert(tk.INSERT, "----------------------------------\n")
text_console.configure(relief="solid", bd=2)

# ------------------------------------------

#   **--Title and Background--** 

app_title_text = "Texture Pack Converter"
app_title_font_size = 25
app_title_font = ImageFont.truetype(font_mojangles, app_title_font_size)

# Image and Border
app_title_image_width = 390
app_title_image_height = 35
app_title_image = Image.new("RGBA", (app_title_image_width, app_title_image_height), (255, 255, 255, 0))
app_title_draw = ImageDraw.Draw(app_title_image)
app_title_outline_color = (0, 0, 0)
app_title_outline_position = (31.5, 4)
app_title_draw.text(app_title_outline_position, app_title_text, font=app_title_font, fill=app_title_outline_color)

# Draw Text
app_title_text_color = (255, 255, 255)
app_title_text_position = (29, 2)
app_title_draw.text(app_title_text_position, app_title_text, font=app_title_font, fill=app_title_text_color)

# Convert Image to tk
app_title_imagetk = ImageTk.PhotoImage(app_title_image)

# Show Image
app_title = tk.Label(TextureApp, image=app_title_imagetk, bg="#585858")
app_title.place(x=0, y=0)

# ------------------------------------------

#    **--YouTube Button--**

# Image
youtube_img = tk.Label(TextureApp, image=youtube_photo_image, bg="#585858", bd=1, relief="solid")
youtube_img.place(x=213, y=TextureApp.winfo_height() - 3, anchor="sw")

# Text
youtube_text = tk.Label(TextureApp, text="Jerem2206", bg="#585858", fg="#FFFFFF")
youtube_text.place(x=200, y=TextureApp.winfo_height() - 25, anchor="sw")
youtube_text.place_forget()

# Display text
def youtube_show_text(event):
    youtube_text.place(x=200, y=TextureApp.winfo_height() - 25, anchor="sw")

# Hide text
def youtube_hide_text(event):
    youtube_text.place_forget()

# Link
def youtube_link(event):
    webbrowser.open("https://www.youtube.com/channel/UC004A2sK0Pr0dD6MJzy6cTQ")

# Bind events
youtube_img.bind("<Enter>", youtube_show_text)
youtube_img.bind("<Leave>", youtube_hide_text)
youtube_img.bind("<Button-1>", youtube_link)


# ------------------------------------------

#   **--Discord Button--**

# Image
discord_img = tk.Label(TextureApp, image=discord_photo_image, bg="#585858", bd=1, relief="solid")
discord_img.place(x=130, y=TextureApp.winfo_height() - 3, anchor="sw")

# Text
discord_text = tk.Label(TextureApp, text="jeremestici", bg="#585858", fg="#FFFFFF")
discord_text.place(x=113, y=TextureApp.winfo_height() - 25, anchor="sw")
discord_text.place_forget()

# Display text
def DiscordShowText(event):
    discord_text.place(x=113, y=TextureApp.winfo_height() - 25, anchor="sw")

# Hide text
def DiscordHideText(event):
    discord_text.place_forget()

# Bind events
discord_img.bind("<Enter>", DiscordShowText)
discord_img.bind("<Leave>", DiscordHideText)


# ------------------------------------------

#    **--GitHub Button--**

# Image
github_img = tk.Label(TextureApp, image=github_photo_image, bg="#585858", bd=1, relief="solid")
github_img.place(x=171, y=TextureApp.winfo_height() - 3, anchor="sw")

# Text
github_text = tk.Label(TextureApp, text="jeremy2206", bg="#585858", fg="#FFFFFF")
github_text.place(x=151, y=TextureApp.winfo_height() - 25, anchor="sw")
github_text.place_forget()

# Display text
def github_show_text(event):
    github_text.place(x=151, y=TextureApp.winfo_height() - 25, anchor="sw")

# Hide text
def github_hide_text(event):
    github_text.place_forget()

# Link
def github_link(event):
    webbrowser.open("https://github.com/jeremy2206")

# Bind events
github_img.bind("<Enter>", github_show_text)
github_img.bind("<Leave>", github_hide_text)
github_img.bind("<Button-1>", github_link)

TextureApp.mainloop()
