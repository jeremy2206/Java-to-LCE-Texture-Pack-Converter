import json
import os.path
import shutil
import tkinter as tk
import webbrowser
from tkinter.scrolledtext import ScrolledText

from PIL import Image, ImageDraw, ImageFont, ImageTk


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

        for image_path, position in tiles_dict.items():
            if os.path.isfile(image_path):
                image_to_paste = Image.open(image_path)
                image_to_paste = self.crop_image(image_to_paste, max_width, max_height)

                # Ensure position is a 2-tuple (x, y) for the top-left corner
                if isinstance(position, tuple) and len(position) == 2:
                    image.paste(image_to_paste, position)
                elif isinstance(position, list) and len(position) == 2:
                    image.paste(image_to_paste, tuple(position))  # Convert list to tuple if necessary
                elif isinstance(position, list) and len(position[0]) == 2:  # If position is a list of 2-tuples
                    image.paste(image_to_paste, position[0])  # Use the first 2-tuple if position is a list of 2-tuples
                else:
                    print(f"Invalid position format for {image_path}: {position}")
            else:
                print(f"Image {image_path} does not exist.")

        image.save(output_path)


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
        # Load the terrain from the JSON file
        with open(self.json_path, "r") as item:
            image_dict = json.load(item)

        # Path to the original terrain image
        input_paths = image_dict["input_paths"]
        input_path = input_paths[str(resolution)]

        multiplier = int(resolution / image_dict["default_resolution"])

        # Output path for the merged terrain image
        output_paths = image_dict["output_paths"]
        output_path = output_paths[0]

        tiles_dict = image_dict["tiles"]

        # Convert position values to tuples of integers, handling nested lists
        for key in tiles_dict.keys():
            if isinstance(tiles_dict[key], list) and isinstance(tiles_dict[key][0], list):
                tiles_dict[key] = [tuple(map(int, coord) for coord in tiles_dict[key])]
            else:
                tiles_dict[key] = tuple(map(int, tiles_dict[key]))

        # Copy the terrain image to the output directory
        shutil.copyfile(input_path, output_path)

        # Multiply coordinates by the resolution factor
        tiles_dict = self.multiply_coordinates(tiles_dict, multiplier)

        # Merge images onto the output terrain image
        self.merge_image(tiles_dict, output_path, resolution, resolution, output_path)

        # Create mipmaps if required
        if len(output_paths) > 1:
            for i, mipmap in enumerate(output_paths[1:], start=1):
                size_multiplier = 2 ** i
                self.resize_image(output_path, mipmap, size_multiplier, size_multiplier)

                text_console.insert(
                    tk.INSERT, f"A mipmap has been made at {output_path}\n"
                )
                text_console.insert(tk.INSERT, "----------------------------------\n")
                text_console.see(tk.END)


# Create App
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


# Global Background
background = tk.Label(TextureApp, bg="#383838")
background.place(x=0, y=0, width=380, height=400)

# Title Border Background
app_title_background_border = tk.Label(TextureApp, bg="#000000")
app_title_background_border.place(x=0, y=38, width=380, height=2)
app_title_background_border.lift()

# Background Credits
background_credit_bottom = tk.Label(TextureApp, bg="#585858")
background_credit_bottom.place(x=0, y=350, width=380, height=30)
background_credit_bottom.lift()
background_credit_bottom_border = tk.Label(TextureApp, bg="#000000")
background_credit_bottom_border.place(x=0, y=419, width=380, height=2)
background_credit_bottom_border.lift()


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
x_multiplieritems.set(optionsitems[0])  # Par d��faut, x16 est sélectionné

dropdown_menuitems = tk.OptionMenu(TextureApp, x_multiplieritems, *optionsitems)
dropdown_menuitems.place(x=210, y=62)
dropdown_menuitems.configure(relief="solid", bd=2)


# ------------------------------------------


def convert_terrain():
    terrain_Handler = AtlasHandler("assets/json/terrain.json")
    terrain_Handler.process_image(int(x_multiplierterrain.get()[1:]))


# Créer le bouton pour choisir la conversion
convert_buttonterrain = tk.Button(
    TextureApp, text="Convert Blocks", command=convert_terrain
)
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


def convert_particles():
    particle_handler = AtlasHandler("assets/json/particles.json")
    particle_handler.process_image(int(x_multiplierparticles.get()[1:]))


# bouton pour choisir la conversion
convert_buttonparticles = tk.Button(
    TextureApp, text="Convert Particles", command=convert_particles
)
convert_buttonparticles.place(x=95, y=142)
convert_buttonparticles.configure(relief="solid", bd=2)

# Définir les options pour le menu déroulant (x16 / x32...)
optionsparticles = ["x8", "x16", "x32", "x64"]

# Déclarez x_multiplier comme une variable de chaîne
x_multiplierparticles = tk.StringVar()
x_multiplierparticles.set(optionsparticles[0])  # Par défaut x16

dropdown_menuparticles = tk.OptionMenu(
    TextureApp, x_multiplierparticles, *optionsparticles
)
dropdown_menuparticles.place(x=210, y=139)
dropdown_menuparticles.configure(relief="solid", bd=2)


# ------------------------------------------


def convert_painting():
    painting_handler = AtlasHandler("assets/json/painting.json")
    painting_handler.process_image(int(x_multiplierpainting.get()[1:]))


# bouton pour choisir la conversion
convert_buttonpainting = tk.Button(
    TextureApp, text="Convert Paintings", command=convert_painting
)
convert_buttonpainting.place(x=95, y=182)
convert_buttonpainting.configure(relief="solid", bd=2)

# Définir les options pour le menu déroulant (x16 / x32...)
optionspainting = ["x16", "x32", "x64", "x128"]

# Déclarez x_multiplier comme une variable de chaîne
x_multiplierpainting = tk.StringVar()
x_multiplierpainting.set(optionspainting[0])  # Par défaut x16

dropdown_menupainting = tk.OptionMenu(
    TextureApp, x_multiplierpainting, *optionspainting
)
dropdown_menupainting.place(x=210, y=179)
dropdown_menupainting.configure(relief="solid", bd=2)


# ------------------------------------------



# Create Widget ScrolledText
text_console = ScrolledText(TextureApp, width=34, height=7)
text_console.place(x=42.5, y=223)
text_console.insert(
    tk.INSERT, "Version : 1.3 - Check if any      update have been made.\n"
)
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
app_title_image = Image.new(
    "RGBA", (app_title_image_width, app_title_image_height), (255, 255, 255, 0)
)
app_title_draw = ImageDraw.Draw(app_title_image)
app_title_outline_color = (0, 0, 0)
app_title_outline_position = (31.5, 4)
app_title_draw.text(
    app_title_outline_position,
    app_title_text,
    font=app_title_font,
    fill=app_title_outline_color,
)

# Draw Text
app_title_text_color = (255, 255, 255)
app_title_text_position = (29, 2)
app_title_draw.text(
    app_title_text_position,
    app_title_text,
    font=app_title_font,
    fill=app_title_text_color,
)

# Convert Image to tk
app_title_imagetk = ImageTk.PhotoImage(app_title_image)

# Show Image
app_title = tk.Label(TextureApp, image=app_title_imagetk, bg="#585858")
app_title.place(x=0, y=0)


# ------------------------------------------


# Credits
def jerem2206_youtube_link(event):
    webbrowser.open("https://www.youtube.com/channel/UC004A2sK0Pr0dD6MJzy6cTQ")

def jerem2206_github_link(event):
    webbrowser.open("https://github.com/jeremy2206")

def boreal_github_link(event):
    webbrowser.open("https://github.com/bor-real")

def show_credits():
    credits_window = tk.Toplevel(TextureApp)
    credits_window.title("Credits")
    credits_window.geometry("300x250")
    credits_window.resizable(False, False)
    credits_window.iconbitmap(icon_path)

    frame = tk.Frame(credits_window)
    frame.pack(expand=True)

    # Texte en haut fixe
    credits_label = tk.Label(frame, text="Credits", font=("Helvetica", 18))
    credits_label.grid(row=0, column=1)

    jerem2206_label = tk.Label(frame, text="Jerem2206", font=("Helvetica", 13))
    jerem2206_label.grid(row=1, column=1, pady=5)

    jerem2206_youtube_img = tk.Label(frame, image=youtube_photo_image, bd=1, relief="solid")
    jerem2206_youtube_img.grid(row=3, column=0, padx=10)
    jerem2206_youtube_img.bind("<Button-1>", jerem2206_youtube_link)
    jerem2206_youtube_text = tk.Label(frame, text="Jerem2206")
    jerem2206_youtube_text.grid(row=2, column=0, padx=10)

    jerem2206_github_img = tk.Label(frame, image=github_photo_image, bd=1, relief="solid")
    jerem2206_github_img.grid(row=3, column=1, padx=10)
    jerem2206_github_img.bind("<Button-1>", jerem2206_github_link)
    jerem2206_github_text = tk.Label(frame, text="Jeremy2206")
    jerem2206_github_text.grid(row=2, column=1, padx=10)

    jerem2206_discord_img = tk.Label(frame, image=discord_photo_image, bd=1, relief="solid")
    jerem2206_discord_img.grid(row=3, column=2, padx=10)
    jerem2206_discord_text = tk.Label(frame, text="jeremestici")
    jerem2206_discord_text.grid(row=2, column=2, padx=10)
    
    # ------------------------------------------------------------- #

    boreal_label = tk.Label(frame, text="Boreal", font=("Helvetica", 13))
    boreal_label.grid(row=4, column=1, pady=5)  # Utilisez columnspan pour étendre sur 3 colonnes

    boreal_github_img = tk.Label(frame, image=github_photo_image, bd=1, relief="solid")
    boreal_github_img.grid(row=6, column=1, padx=10)
    boreal_github_text = tk.Label(frame, text="Boreal")
    boreal_github_text.grid(row=5, column=1, padx=10)


credits_button = tk.Button(TextureApp, text="Credits", command=show_credits)
credits_button.configure(relief="solid", bd=2)
credits_button.place(x=160, y=352)




TextureApp.mainloop()
