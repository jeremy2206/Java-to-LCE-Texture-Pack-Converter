import tkinter as tk
from PIL import ImageTk, Image, ImageFont, ImageDraw
from tkinter.scrolledtext import ScrolledText
import shutil
import webbrowser
import os.path
from collections import defaultdict  # pour images multiples

def multiply_coordinatesparticles(image_dictparticles, factorparticles):
    multiplied_image_dictparticles = {}
    for image_pathparticles, positionsparticles in image_dictparticles.items():
        multiplied_positionsparticles = [(coordparticles[0] * factorparticles, coordparticles[1] * factorparticles) for coordparticles in positionsparticles]
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

    TextConsole.insert(tk.INSERT, "particles.png converted at        output/particles.png\n")
    TextConsole.insert(tk.INSERT, "----------------------------------\n")
    TextConsole.see(tk.END)

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
    image_dictparticles = defaultdict(list)

    image_dictparticles["input/particle/angry.png"].append((8, 40))
    image_dictparticles["input/particle/bubble.png"].append((16, 16))
    image_dictparticles["input/particle/critical_hit.png"].append((8, 32))
    image_dictparticles["input/particle/angry.png"].append((8, 40))
    image_dictparticles["input/particle/damage.png"].append((24, 32))
    image_dictparticles["input/particle/drip_fall.png"].append((8, 56))
    image_dictparticles["input/particle/drip_hang.png"].append((0, 56))
    image_dictparticles["input/particle/drip_land.png"].append((16, 56))
    image_dictparticles["input/particle/effect_0.png"].append((0, 64))
    image_dictparticles["input/particle/effect_1.png"].append((8, 64))
    image_dictparticles["input/particle/effect_2.png"].append((16, 64))
    image_dictparticles["input/particle/effect_3.png"].append((24, 64))
    image_dictparticles["input/particle/effect_4.png"].append((32, 64))
    image_dictparticles["input/particle/effect_5.png"].append((40, 64))
    image_dictparticles["input/particle/effect_6.png"].append((48, 64))
    image_dictparticles["input/particle/effect_7.png"].append((56, 64))
    image_dictparticles["input/particle/enchanted_hit.png"].append((16, 32))
    image_dictparticles["input/particle/flame.png"].append((0, 24))
    image_dictparticles["input/particle/generic_0.png"].append((0, 0))
    image_dictparticles["input/particle/generic_1.png"].append((8, 0))
    image_dictparticles["input/particle/generic_2.png"].append((16, 0))
    image_dictparticles["input/particle/generic_3.png"].append((24, 0))
    image_dictparticles["input/particle/generic_4.png"].append((32,0))
    image_dictparticles["input/particle/generic_5.png"].append((40, 0))
    image_dictparticles["input/particle/generic_6.png"].append((48, 0))
    image_dictparticles["input/particle/generic_7.png"].append((56, 0))
    image_dictparticles["input/particle/glint.png"].append((16, 40))
    image_dictparticles["input/particle/glitter_0.png"].append((0, 88))
    image_dictparticles["input/particle/glitter_1.png"].append((8, 88))
    image_dictparticles["input/particle/glitter_2.png"].append((16, 88))
    image_dictparticles["input/particle/glitter_3.png"].append((24, 88))
    image_dictparticles["input/particle/glitter_4.png"].append((32, 88))
    image_dictparticles["input/particle/glitter_5.png"].append((40, 88))
    image_dictparticles["input/particle/glitter_6.png"].append((48, 88))
    image_dictparticles["input/particle/glitter_7.png"].append((56, 88))
    image_dictparticles["input/particle/heart.png"].append((0, 40))
    image_dictparticles["input/particle/lava.png"].append((8, 24))
    image_dictparticles["input/particle/note.png"].append((0, 32))
    image_dictparticles["input/particle/sga_a.png"].append((8, 112))
    image_dictparticles["input/particle/sga_b.png"].append((16, 112))
    image_dictparticles["input/particle/sga_c.png"].append((24, 112))
    image_dictparticles["input/particle/sga_d.png"].append((32, 112))
    image_dictparticles["input/particle/sga_e.png"].append((40, 112))
    image_dictparticles["input/particle/sga_f.png"].append((48, 112))
    image_dictparticles["input/particle/sga_g.png"].append((56, 112))
    image_dictparticles["input/particle/sga_h.png"].append((64, 112))
    image_dictparticles["input/particle/sga_i.png"].append((72, 112))
    image_dictparticles["input/particle/sga_j.png"].append((80, 112))
    image_dictparticles["input/particle/sga_k.png"].append((88, 112))
    image_dictparticles["input/particle/sga_l.png"].append((96, 112))
    image_dictparticles["input/particle/sga_m.png"].append((104, 112))
    image_dictparticles["input/particle/sga_n.png"].append((112, 112))
    image_dictparticles["input/particle/sga_o.png"].append((120, 112))
    image_dictparticles["input/particle/sga_p.png"].append((0, 120))
    image_dictparticles["input/particle/sga_q.png"].append((8, 120))
    image_dictparticles["input/particle/sga_r.png"].append((16, 120))
    image_dictparticles["input/particle/sga_s.png"].append((24, 120))
    image_dictparticles["input/particle/sga_t.png"].append((32, 120))
    image_dictparticles["input/particle/sga_u.png"].append((40, 120))
    image_dictparticles["input/particle/sga_v.png"].append((48, 120))
    image_dictparticles["input/particle/sga_w.png"].append((56, 120))
    image_dictparticles["input/particle/sga_x.png"].append((64, 120))
    image_dictparticles["input/particle/sga_y.png"].append((72, 120))
    image_dictparticles["input/particle/sga_z.png"].append((80, 120))
    image_dictparticles["input/particle/spark_0.png"].append((0, 80))
    image_dictparticles["input/particle/spark_0.png"].append((8, 80))
    image_dictparticles["input/particle/spark_0.png"].append((16, 80))
    image_dictparticles["input/particle/spark_0.png"].append((24, 80))
    image_dictparticles["input/particle/spark_0.png"].append((32, 80))
    image_dictparticles["input/particle/spark_0.png"].append((40, 80))
    image_dictparticles["input/particle/spark_0.png"].append((48, 80))
    image_dictparticles["input/particle/spark_0.png"].append((56, 80))
    image_dictparticles["input/particle/spell_0.png"].append((0, 72))
    image_dictparticles["input/particle/spell_1.png"].append((8, 72))
    image_dictparticles["input/particle/spell_2.png"].append((16, 72))
    image_dictparticles["input/particle/spell_3.png"].append((24, 72))
    image_dictparticles["input/particle/spell_4.png"].append((32, 72))
    image_dictparticles["input/particle/spell_5.png"].append((40, 72))
    image_dictparticles["input/particle/spell_6.png"].append((48, 72))
    image_dictparticles["input/particle/spell_7.png"].append((56, 72))
    image_dictparticles["input/particle/splash_0.png"].append((24, 8))
    image_dictparticles["input/particle/splash_1.png"].append((32, 8))
    image_dictparticles["input/particle/splash_2.png"].append((40, 8))
    image_dictparticles["input/particle/splash_3.png"].append((48, 8))

    # Chemin de l'image de sortie
    particle_output_path = "output/particles.png"

    # Copie de l'image de particle vers la sortie
    shutil.copyfile(particle_image_path, particle_output_path)

    # Multiplier les coordonnées par le facteur choisi (x16 ou x32...)
    image_dictparticles = multiply_coordinatesparticles(image_dictparticles, multiplierparticles)

    # Appel de la fonction pour fusionner les images sur particles.png
    merge_imagesparticles(image_dictparticles, particle_output_path, 16 * multiplierparticles, 16 * multiplierparticles, particle_output_path)

# Créer l'app
TextureApp = tk.Tk()
TextureApp.title("Converter : particle")
IconPath = os.path.abspath("assets/iconparticle.ico")
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
convert_button = tk.Button(TextureApp, text="Convert Particles", command=process_images)
convert_button.place(x=100, y=62)
convert_button.configure(relief="solid", bd=2)

# Définir les options pour le menu déroulant (x16 / x32...)
optionsparticles = ["x8", "x16", "x32", "x64"]

# Déclarez x_multiplier comme une variable de chaîne
x_multiplierparticles = tk.StringVar()
x_multiplierparticles.set(optionsparticles[0])  # Par défaut x16

# Créer le widget ScrolledText
TextConsole = ScrolledText(TextureApp, width=34, height=7)
TextConsole.place(x=42.5, y=113)
TextConsole.insert(tk.INSERT, "Version : 1.2 - Check if any      update have been made.\n")
TextConsole.insert(tk.INSERT, "----------------------------------\n")
TextConsole.configure(relief="solid", bd=2)

dropdown_menu = tk.OptionMenu(TextureApp, x_multiplierparticles, *optionsparticles)
dropdown_menu.place(x=200, y=59)
dropdown_menu.configure(relief="solid", bd=2)

# Action de clic pour le bouton x16 et autres
def x16_button_click():
    x_multiplierparticles.set(1)
    convert_button.config(text="Convert Particles (x8)")

def x32_button_click():
    x_multiplierparticles.set(2)
    convert_button.config(text="Convert Particles (x16)")

def x32_button_click():
    x_multiplierparticles.set(4)
    convert_button.config(text="Convert Particles (x32)")

def x32_button_click():
    x_multiplierparticles.set(8)
    convert_button.config(text="Convert Particles (x64)")


# ------------------------------------------

#   **--Titre et Fond--** 

TitleAppText = "Particles Pack Converter"
TitleAppFontSize = 24
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
