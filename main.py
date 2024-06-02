import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import json
import shutil
import webbrowser
import os.path
from PIL import ImageTk, Image, ImageFont, ImageDraw

class AtlasHandler:
    def __init__(self, json_path):
        self.json_path = json_path

    def crop_image(self, image, max_width, max_height):
        width, height = image.size
        if width > max_width or height > max_height:
            left = 0
            top = 0
            right = min(width, max_width)
            bottom = min(height, max_height)
            image = image.crop((left, top, right, bottom))
        return image

    def multiply_coordinates(self, tiles_dict, factor):
        multiplied_tiles_dict = {}
        for image_path, position in tiles_dict.items():

            multiplied_position = tuple(coord * factor for coord in position)
            multiplied_tiles_dict[image_path] = multiplied_position
        return multiplied_tiles_dict

    def merge_image(self, tiles_dict, items_image, max_width, max_height, output_path):
        image = Image.open(items_image)

        for image_path, positionitems in tiles_dict.items():
            if os.path.isfile(image_path):
                image_to_paste = Image.open(image_path)
                image_to_paste = self.crop_image(image_to_paste, max_width, max_height)
                image.paste(image_to_paste, positionitems)
            else:
                print(f"L'image {image_path} n'existe pas.")

        image.save(output_path)
        
        text_console.insert(tk.INSERT, f"The file has been converted at  {output_path}\n")
        text_console.insert(tk.INSERT, "----------------------------------\n")
        text_console.see(tk.END)

    def resize_image(self, input_path, output_path, division_width, division_height):
        if os.path.isfile(input_path):
            image = Image.open(input_path)

            width = int(image.width / division_width)
            height = int(image.height / division_height)

            resized_image = image.resize((width, height), Image.LANCZOS)
            resized_image.save(output_path)
        else:
            print(f"L'image {input_path} n'existe pas.")

    def process_image(self, resolution):
        # Charger le terrain à partir du fichier JSON
        with open(self.json_path, 'r') as item:
            image_dict = json.load(item)

        # Chemin de l'image de terrain d'origine
        input_paths = image_dict["input_paths"]
        input_path = input_paths[str(resolution)]

        multiplier = int(resolution / image_dict["default_resolution"])

        # Chemin de sortie pour l'image de terrain fusionnée
        output_paths = image_dict["output_paths"]
        output_path = output_paths[0]

        tiles_dict = image_dict["tiles"]

        # Copie de l'image de terrain vers le répertoire de sortie
        shutil.copyfile(input_path, output_path)

        # Astuce malveillante pour obtenir le nom de la première clé
        image_dict = self.multiply_coordinates(tiles_dict, multiplier)

        # Appel de la fonction pour fusionner les images sur items.png
        self.merge_image(tiles_dict, output_path, resolution, resolution, output_path)

        if len(output_paths) > 1:
            for i, mipmap in enumerate(output_paths[1:], start=1):
                size_multiplier = 2 ** i
                self.resize_image(output_path, mipmap, size_multiplier, size_multiplier)

                text_console.insert(tk.INSERT, f"A mipmap has been made at {output_path}\n")
                text_console.insert(tk.INSERT, "----------------------------------\n")
                text_console.see(tk.END)

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
background_info_bottom = tk.Label(TextureApp, bg="#585858")
background_info_bottom.place(x=0, y=350, width=380, height=30)
background_info_bottom.lift()
background_info_bottom_border = tk.Label(TextureApp, bg="#000000")
background_info_bottom_border.place(x=0, y=419, width=380, height=2)
background_info_bottom_border.lift()


# ------------------------------------------
# ------------------------------------------
# ------------------------------------------

def convert_items():
    item_handler = AtlasHandler("assets/json/items.json")
    item_handler.process_image(int(x_multiplieritems.get()[1:]))

# Créer le bouton de la conversion
convert_buttonitems = tk.Button(TextureApp, text="Convert Items", command=convert_items)
convert_buttonitems.place(x=95, y=62)
convert_buttonitems.configure(relief="solid", bd=2)
# Définir les options pour le menu déroulant (x16 et x32)
optionsitems = ["x16"]
# Déclarez x_multiplier comme une variable de chaîne
x_multiplieritems = tk.StringVar()
x_multiplieritems.set(optionsitems[0])  # Par défaut, x16 est sélectionné

dropdown_menuitems = tk.OptionMenu(TextureApp, x_multiplieritems, *optionsitems)
dropdown_menuitems.place(x=210, y=62)
dropdown_menuitems.configure(relief="solid", bd=2)

# ------------------------------------------
# ------------------------------------------
# ------------------------------------------

def convert_terrain():
    terrain_Handler = AtlasHandler("assets/json/terrain.json")
    terrain_Handler.process_image(int(x_multiplierterrain.get()[1:]))

# Créer le bouton pour choisir la conversion
convert_buttonterrain = tk.Button(TextureApp, text="Convert Blocks", command=convert_terrain)
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

# ------------------------------------------
# ------------------------------------------
# ------------------------------------------

def convert_particles():
    particle_handler = AtlasHandler("assets/json/particles.json")
    particle_handler.process_image(int(x_multiplierparticles.get()[1:]))

# bouton pour choisir la conversion
convert_buttonparticles = tk.Button(TextureApp, text="Convert Particles", command=convert_particles)
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

# ------------------------------------------
# ------------------------------------------
# ------------------------------------------

def convert_painting():
    painting_handler = AtlasHandler("assets/json/painting.json")
    painting_handler.process_image(int(x_multiplierpainting.get()[1:]))

# bouton pour choisir la conversion
convert_buttonpainting = tk.Button(TextureApp, text="Convert Paintings", command=convert_painting)
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
