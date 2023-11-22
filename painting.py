import tkinter as tk
from PIL import ImageTk, Image, ImageFont, ImageDraw
from tkinter.scrolledtext import ScrolledText
import shutil
import webbrowser
import os.path
from collections import defaultdict  # pour images multiples

def multiply_coordinates(image_dict, factor):
    multiplied_image_dict = {}
    for image_path, positions in image_dict.items():
        multiplied_positions = [(coord[0] * factor, coord[1] * factor) for coord in positions]
        multiplied_image_dict[image_path] = multiplied_positions
    return multiplied_image_dict

def merge_images(image_dict, painting_image, max_width, max_height, output_path):
    painting = Image.open(painting_image)

    for image_path, positions in image_dict.items():
        if os.path.isfile(image_path):
            for position in positions:
                image = Image.open(image_path)
                painting.paste(image, position)
        else:
            print(f"L'image {image_path} n'existe pas.")

    # Sauvegarder l'image fusionnée en remplaçant l'image "kz.png"
    painting.save(output_path)

    TextConsole.insert(tk.INSERT, "kz.png converted at output/kz.png\n")
    TextConsole.insert(tk.INSERT, "----------------------------------\n")
    TextConsole.see(tk.END)

def resize_image(input_path, output_path, new_width, new_height):
    if os.path.isfile(input_path):
        image = Image.open(input_path)
        resized_image = image.resize((new_width, new_height), Image.LANCZOS)
        resized_image.save(output_path)
    else:
        print(f"L'image {input_path} n'existe pas.")

def process_images():
    multiplier_str = x_multiplier.get()

    if multiplier_str == "x16":
        multiplier = 1
        painting_image_path = "assets/texture/kz.png"
    elif multiplier_str == "x32":
        multiplier = 2
        painting_image_path = "assets/texture/kz32.png"
    elif multiplier_str == "x64":
        multiplier = 4
        painting_image_path = "assets/texture/kz64.png"
    elif multiplier_str == "x128":
        multiplier = 8
        painting_image_path = "assets/texture/kz128.png"
    else:
        return

    #liste d'images
    image_dict = defaultdict(list)

    image_dict["input/painting/alban.png"].append((32, 0))
    image_dict["input/painting/alban.png"].append((32, 16))
    image_dict["input/painting/aztec.png"].append((16, 0))
    image_dict["input/painting/aztec.png"].append((16, 16))
    image_dict["input/painting/aztec2.png"].append((48, 0))
    image_dict["input/painting/aztec2.png"].append((48, 16))
    image_dict["input/painting/back.png"].append((192, 0))
    image_dict["input/painting/back.png"].append((208, 0))
    image_dict["input/painting/back.png"].append((224, 0))
    image_dict["input/painting/back.png"].append((240, 0))
    image_dict["input/painting/back.png"].append((192, 16))
    image_dict["input/painting/back.png"].append((208, 16))
    image_dict["input/painting/back.png"].append((224, 16))
    image_dict["input/painting/back.png"].append((240, 16))
    image_dict["input/painting/back.png"].append((192, 32))
    image_dict["input/painting/back.png"].append((208, 32))
    image_dict["input/painting/back.png"].append((224, 32))
    image_dict["input/painting/back.png"].append((240, 32))
    image_dict["input/painting/back.png"].append((192, 48))
    image_dict["input/painting/back.png"].append((208, 48))
    image_dict["input/painting/back.png"].append((224, 48))
    image_dict["input/painting/back.png"].append((240, 48))
    image_dict["input/painting/bomb.png"].append((64, 0))
    image_dict["input/painting/bomb.png"].append((64, 16))
    image_dict["input/painting/burning_skull.png"].append((128, 192))
    image_dict["input/painting/bust.png"].append((32, 128))
    image_dict["input/painting/courbet.png"].append((32, 32))
    image_dict["input/painting/creebet.png"].append((128, 32))
    image_dict["input/painting/donkey_kong.png"].append((192, 112))
    image_dict["input/painting/fighters.png"].append((0, 96))
    image_dict["input/painting/graham.png"].append((16, 64))
    image_dict["input/painting/kebab.png"].append((0, 0))
    image_dict["input/painting/kebab.png"].append((0, 16))
    image_dict["input/painting/match.png"].append((0, 128))
    image_dict["input/painting/pigscene.png"].append((64, 192))
    image_dict["input/painting/plant.png"].append((80, 0))
    image_dict["input/painting/plant.png"].append((80, 16))
    image_dict["input/painting/pointer.png"].append((0, 192))
    image_dict["input/painting/pool.png"].append((0, 32))
    image_dict["input/painting/sea.png"].append((64, 32))
    image_dict["input/painting/skeleton.png"].append((192, 64))
    image_dict["input/painting/skull_and_roses.png"].append((128, 128))
    image_dict["input/painting/stage.png"].append((64, 128))
    image_dict["input/painting/sunset.png"].append((96, 32))
    image_dict["input/painting/void.png"].append((96, 128))
    image_dict["input/painting/wanderer.png"].append((0, 64))
    image_dict["input/painting/wasteland.png"].append((96, 0))
    image_dict["input/painting/wasteland.png"].append((96, 16))
    image_dict["input/painting/wither.png"].append((160, 128))

    # Chemin de l'image de sortie
    painting_output_path = "output/kz.png"

    # Copie de l'image de painting vers la sortie
    shutil.copyfile(painting_image_path, painting_output_path)

    # Multiplier les coordonnées par le facteur choisi (x16 ou x32...)
    image_dict = multiply_coordinates(image_dict, multiplier)

    # Appel de la fonction pour fusionner les images sur kz.png
    merge_images(image_dict, painting_output_path, 16 * multiplier, 16 * multiplier, painting_output_path)

# Créer l'app
TextureApp = tk.Tk()
TextureApp.title("Converter : Painting")
IconPath = os.path.abspath("assets/iconpainting.ico")
TextureApp.iconbitmap(IconPath)
TextureApp.geometry("380x280")
TextureApp.resizable(False, False)

# ------------------------------------------

# charger les images
youtubeImagePath = os.path.abspath("assets/youtube.png")
YoutubeImage = Image.open(youtubeImagePath)
YoutubeImageSize = YoutubeImage.resize((23, 20), Image.LANCZOS)
YoutubePhotoImage = ImageTk.PhotoImage(YoutubeImageSize)

discordImagePath = os.path.abspath("assets/discord.png")
DiscordImage = Image.open(discordImagePath)
DiscordImageSize = DiscordImage.resize((23, 20), Image.LANCZOS)
DiscordPhotoImage = ImageTk.PhotoImage(DiscordImageSize)

githubImagePath = os.path.abspath("assets/github.png")
GitHubImage = Image.open(githubImagePath)
GitHubImageSize = GitHubImage.resize((23, 20), Image.LANCZOS)
GitHubPhotoImage = ImageTk.PhotoImage(GitHubImageSize)

# charger la police d'écriture 
FontMojangles = os.path.abspath("assets/Mojangles.ttf")

# ------------------------------------------

#   **--Background--**

# couleur de fond
Background = tk.Label(TextureApp, bg="#383838")
Background.place(x=0, y=0, width=380, height=400)

# titre et rebord
BorderBackgroundTitleApp = tk.Label(TextureApp, bg="#000000")
BorderBackgroundTitleApp.place(x=0, y=38, width=380, height=2)
BorderBackgroundTitleApp.lift()

# fond logo
BackgroundYoutubeDiscord = tk.Label(TextureApp, bg="#585858")
BackgroundYoutubeDiscord.place(x=0, y=250, width=380, height=30)
BackgroundYoutubeDiscord.lift()
BorderBackgroundYoutubeDiscord = tk.Label(TextureApp, bg="#000000")
BorderBackgroundYoutubeDiscord.place(x=0, y=419, width=380, height=2)
BorderBackgroundYoutubeDiscord.lift()

# ------------------------------------------

#   **--Bouton--**

# bouton pour choisir la conversion
convert_button = tk.Button(TextureApp, text="Convert Paintings", command=process_images)
convert_button.place(x=95, y=62)
convert_button.configure(relief="solid", bd=2)

# Définir les options pour le menu déroulant (x16 / x32...)
options = ["x16", "x32", "x64", "x128"]

# Déclarez x_multiplier comme une variable de chaîne
x_multiplier = tk.StringVar()
x_multiplier.set(options[0])  # Par défaut x16

# Créer le widget ScrolledText
TextConsole = ScrolledText(TextureApp, width=34, height=7)
TextConsole.place(x=42.5, y=113)
TextConsole.insert(tk.INSERT, "Version : 1.2 - Check if any      update have been made.\n")
TextConsole.insert(tk.INSERT, "----------------------------------\n")
TextConsole.configure(relief="solid", bd=2)

dropdown_menu = tk.OptionMenu(TextureApp, x_multiplier, *options)
dropdown_menu.place(x=200, y=59)
dropdown_menu.configure(relief="solid", bd=2)

# Action de clic pour le bouton x16 et autres
def x16_button_click():
    x_multiplier.set(1)
    convert_button.config(text="Convert Painting (x16)")

def x32_button_click():
    x_multiplier.set(2)
    convert_button.config(text="Convert Painting (x32)")

def x32_button_click():
    x_multiplier.set(4)
    convert_button.config(text="Convert Painting (x64)")

def x32_button_click():
    x_multiplier.set(8)
    convert_button.config(text="Convert Painting (x128)")


# ------------------------------------------

#   **--Titre et Fond--** 

TitleAppText = "Painting Pack Converter"
TitleAppFontSize = 25
TitleAppFont = ImageFont.truetype(FontMojangles, TitleAppFontSize)

# Image and Border
TitleAppImageWidth = 390
TitleAppImageHeight = 35
TitleAppImage = Image.new("RGBA", (TitleAppImageWidth, TitleAppImageHeight), (255, 255, 255, 0))
TitleAppDraw = ImageDraw.Draw(TitleAppImage)
TitleAppOutlineColor = (0, 0, 0)
TitleAppOutlinePosition = (37.5, 4)
TitleAppDraw.text(TitleAppOutlinePosition, TitleAppText, font=TitleAppFont, fill=TitleAppOutlineColor)

# Draw Text
TitleAppTextColor = (255, 255, 255)
TitleAppTextPosition = (36, 2)
TitleAppDraw.text(TitleAppTextPosition, TitleAppText, font=TitleAppFont, fill=TitleAppTextColor)

# Convert Image to tk
TitleAppImagetk = ImageTk.PhotoImage(TitleAppImage)

# Show Image
TitleApp = tk.Label(TextureApp, image=TitleAppImagetk, bg="#585858")
TitleApp.place(x=0, y=0)

# ------------------------------------------

#    **--YouTube Button--**

# Image
YoutubeIMG = tk.Label(TextureApp, image=YoutubePhotoImage, bg="#585858", bd=1, relief="solid")
YoutubeIMG.place(x=213, y=TextureApp.winfo_height() - 3, anchor="sw")

# Text
YoutubeText = tk.Label(TextureApp, text="Jerem2206", bg="#585858", fg="#FFFFFF")
YoutubeText.place(x=200, y=TextureApp.winfo_height() - 25, anchor="sw")
YoutubeText.place_forget()

# Display text
def YoutubeShowText(event):
    YoutubeText.place(x=200, y=TextureApp.winfo_height() - 25, anchor="sw")

# Hide text
def YoutubeHideText(event):
    YoutubeText.place_forget()

# Link
def YoutubeLink(event):
    webbrowser.open("https://www.youtube.com/channel/UC004A2sK0Pr0dD6MJzy6cTQ")

# Bind events
YoutubeIMG.bind("<Enter>", YoutubeShowText)
YoutubeIMG.bind("<Leave>", YoutubeHideText)
YoutubeIMG.bind("<Button-1>", YoutubeLink)


# ------------------------------------------

#   **--Discord Button--**

# Image
DiscordIMG = tk.Label(TextureApp, image=DiscordPhotoImage, bg="#585858", bd=1, relief="solid")
DiscordIMG.place(x=130, y=TextureApp.winfo_height() - 3, anchor="sw")

# Text
DiscordText = tk.Label(TextureApp, text="jeremestici", bg="#585858", fg="#FFFFFF")
DiscordText.place(x=113, y=TextureApp.winfo_height() - 25, anchor="sw")
DiscordText.place_forget()

# Display text
def DiscordShowText(event):
    DiscordText.place(x=113, y=TextureApp.winfo_height() - 25, anchor="sw")

# Hide text
def DiscordHideText(event):
    DiscordText.place_forget()

# Bind events
DiscordIMG.bind("<Enter>", DiscordShowText)
DiscordIMG.bind("<Leave>", DiscordHideText)


# ------------------------------------------

#    **--GitHub Button--**

# Image
GitHubIMG = tk.Label(TextureApp, image=GitHubPhotoImage, bg="#585858", bd=1, relief="solid")
GitHubIMG.place(x=171, y=TextureApp.winfo_height() - 3, anchor="sw")

# Text
GitHubText = tk.Label(TextureApp, text="jeremy2206", bg="#585858", fg="#FFFFFF")
GitHubText.place(x=151, y=TextureApp.winfo_height() - 25, anchor="sw")
GitHubText.place_forget()

# Display text
def GitHubShowText(event):
    GitHubText.place(x=151, y=TextureApp.winfo_height() - 25, anchor="sw")

# Hide text
def GitHubHideText(event):
    GitHubText.place_forget()

# Link
def GitHubLink(event):
    webbrowser.open("https://github.com/jeremy2206")

# Bind events
GitHubIMG.bind("<Enter>", GitHubShowText)
GitHubIMG.bind("<Leave>", GitHubHideText)
GitHubIMG.bind("<Button-1>", GitHubLink)

TextureApp.mainloop()
