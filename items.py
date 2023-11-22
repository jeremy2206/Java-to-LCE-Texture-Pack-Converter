import tkinter as tk
from PIL import ImageTk, Image, ImageFont, ImageDraw
from tkinter.scrolledtext import ScrolledText
import shutil
import webbrowser
import os.path

def crop_image(image, max_width, max_height):
    width, height = image.size
    if width > max_width or height > max_height:
        left = 0
        top = 0
        right = min(width, max_width)
        bottom = min(height, max_height)
        image = image.crop((left, top, right, bottom))
    return image

def multiply_coordinates(image_dict, factor):
    multiplied_image_dict = {}
    for image_path, position in image_dict.items():
        multiplied_position = tuple(coord * factor for coord in position)
        multiplied_image_dict[image_path] = multiplied_position
    return multiplied_image_dict

def merge_images(image_dict, terrain_image, max_width, max_height, output_path):
    terrain = Image.open(terrain_image)

    for image_path, position in image_dict.items():
        if os.path.isfile(image_path):
            image = Image.open(image_path)
            image = crop_image(image, max_width, max_height)
            terrain.paste(image, position)
        else:
            print(f"L'image {image_path} n'existe pas.")

    # Sauvegarder l'image fusionnée en remplaçant l'image "items.png"
    terrain.save(output_path)
    TextConsole.insert(tk.INSERT, "items.png converted at            output/items.png\n")
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
    # Dictionnaire des images avec leurs positions
    image_dict = {
    "input/items/acacia_boat.png": (128, 208),
    "input/items/acacia_door.png": (0, 208),
    "input/items/apple.png": (160, 0),
    "input/items/apple_golden.png": (176, 0),
    "input/items/armor_stand.png": (128, 192),
    "input/items/arrow.png": (80, 32),
    "input/items/baked_potato.png": (96, 112),
    "input/items/barrier.png": (48, 176),
    "input/items/beef.png": (144, 96),
    "input/items/beef_cooked.png": (160, 96),
    "input/items/beef_raw.png": (144, 96),
    "input/items/beetroot.png": (16, 192),
    "input/items/beetroot_seeds.png": (32, 192),
    "input/items/beetroot_soup.png": (48, 192),
    "input/items/bed.png": (208, 32),
    "input/items/birch_boat.png": (144, 208),
    "input/items/birch_door.png": (16, 208),
    "input/items/blaze_powder.png": (208, 144),
    "input/items/blaze_rod.png": (192, 96),
    "input/items/bone.png": (192, 16),
    "input/items/bone_meal.png": (240, 176),
    "input/items/book.png": (176, 48),
    "input/items/book_enchanted.png": (240, 192),
    "input/items/book_normal.png": (176, 48),
    "input/items/book_writable.png": (176, 176),
    "input/items/book_written.png": (192, 176),
    "input/items/bow.png": (80, 16),
    "input/items/bow_pulling_0.png": (80, 96),
    "input/items/bow_pulling_1.png": (80, 112),
    "input/items/bow_pulling_2.png": (80, 128),
    "input/items/bow_standby.png": (80, 16),
    "input/items/bowl.png": (112, 64),
    "input/items/bread.png": (144, 32),
    "input/items/brewing_stand.png": (192, 160),
    "input/items/brick.png": (96, 16),
    "input/items/broken_elytra.png": (240, 16),
    "input/items/bucket.png": (160, 64),
    "input/items/bucket_empty.png": (160, 64),
    "input/items/bucket_lava.png": (192, 64),
    "input/items/bucket_milk.png": (208, 64),
    "input/items/bucket_water.png": (176, 64),
    "input/items/cake.png": (208, 16),
    "input/items/carrot.png": (128, 112),
    "input/items/carrot_golden.png": (96, 144),
    "input/items/carrot_on_a_stick.png": (96, 96),
    "input/items/cauldron.png": (192, 144),
    "input/items/chainmail_boots.png": (16, 48),
    "input/items/chainmail_chestplate.png": (16, 16),
    "input/items/chainmail_helmet.png": (16, 0),
    "input/items/chainmail_leggings.png": (16, 32),
    "input/items/charcoal.png": (128, 160),
    "input/items/chest_minecart.png": (112, 144),
    "input/items/chicken.png": (144, 112),
    "input/items/chicken_cooked.png": (160, 112),
    "input/items/chicken_raw.png": (144, 112),
    "input/items/chorus_fruit.png": (240, 32),
    "input/items/chorus_fruit_popped.png": (240, 48),
    "input/items/clay_ball.png": (144, 48),
    "input/items/coal.png": (112, 0),
    "input/items/cocoa_beans.png": (224, 112),
    "input/items/cod.png": (144, 80),
    "input/items/cod_bucket.png": (192, 240),
    "input/items/command_block_minecart.png": (112, 208),
    "input/items/comparator.png": (80, 144),
    "input/items/cooked_beef.png": (160, 96),
    "input/items/cooked_chicken.png": (160, 112),
    "input/items/cooked_cod.png": (160, 80),
    "input/items/cooked_mutton.png": (64, 192),
    "input/items/cooked_porkchop.png": (128, 80),
    "input/items/cooked_rabbit.png": (80, 192),
    "input/items/cooked_salmon.png": (96, 208),
    "input/items/cookie.png": (192, 80),
    "input/items/cyan_dye.png": (224, 160),
    "input/items/dark_oak_boat.png": (160, 208),
    "input/items/dark_oak_door.png": (32, 208),
    "input/items/diamond.png": (112, 48),
    "input/items/diamond_axe.png": (48, 112),
    "input/items/diamond_boots.png": (48, 48),
    "input/items/diamond_chestplate.png": (48, 16),
    "input/items/diamond_helmet.png": (48, 0),
    "input/items/diamond_hoe.png": (48, 128),
    "input/items/diamond_horse_armor.png": (48, 144),
    "input/items/diamond_leggings.png": (48, 32),
    "input/items/diamond_pickaxe.png": (48, 96),
    "input/items/diamond_shovel.png": (48, 80),
    "input/items/diamond_sword.png": (48, 64),
    "input/items/door_acacia.png": (0, 208),
    "input/items/door_birch.png": (16, 208),
    "input/items/door_dark_oak.png": (32, 208),
    "input/items/door_iron.png": (192, 32),
    "input/items/door_jungle.png": (48, 208),
    "input/items/door_spruce.png": (64, 208),
    "input/items/door_wood.png": (176, 32),
    "input/items/dragon_breath.png": (32, 160),
    "input/items/dried_kelp.png": (128, 256),
    "input/items/dye_powder_black.png": (224, 64),
    "input/items/dye_powder_blue.png": (224, 128),
    "input/items/dye_powder_brown.png": (224, 112),
    "input/items/dye_powder_cyan.png": (224, 160),
    "input/items/dye_powder_gray.png": (240, 64),
    "input/items/dye_powder_green.png": (224, 96),
    "input/items/dye_powder_light_blue.png": (240, 128),
    "input/items/dye_powder_lime.png": (240, 96),
    "input/items/dye_powder_magenta.png": (240, 144),
    "input/items/dye_powder_orange.png": (240, 160),
    "input/items/dye_powder_pink.png": (240, 80),
    "input/items/dye_powder_purple.png": (224, 144),
    "input/items/dye_powder_red.png": (224, 80),
    "input/items/dye_powder_silver.png": (224, 176),
    "input/items/dye_powder_white.png": (240, 176),
    "input/items/dye_powder_yellow.png": (240, 112),
    "input/items/egg.png": (192, 0),
    "input/items/elytra.png": (240, 0),
    "input/items/emerald.png": (160, 176),
    "input/items/enchanted_book.png": (240, 192),
    "input/items/end_crystal.png": (96, 32),
    "input/items/ender_eye.png": (176, 144),
    "input/items/ender_pearl.png": (176, 96),
    "input/items/emerald.png": (160, 176),
    "input/items/experience_bottle.png": (176, 160),
    "input/items/feather.png": (128, 16),
    "input/items/fermented_spider_eye.png": (160, 128),
    "input/items/filled_map.png": (208, 192),
    "input/items/fire_charge.png": (224, 32),
    "input/items/fireball.png": (224, 32),
    "input/items/fireworks.png": (144, 192),
    "input/items/fireworks_charge.png": (160, 192),
    "input/items/fireworks_charge_overlay.png": (176, 192),
    "input/items/fireworks_rocket.png": (144, 192),
    "input/items/fireworks_star.png": (160, 192),
    "input/items/fireworks_star_overlay.png": (176, 192),
    "input/items/firework_rocket.png": (144, 192),
    "input/items/firework_star.png": (160, 192),
    "input/items/firework_star_overlay.png": (176, 192),
    "input/items/fish_clownfish_raw.png": (96, 160),
    "input/items/fish_cod_cooked.png": (160, 80),
    "input/items/fish_cod_raw.png": (144, 80),
    "input/items/fish_pufferfish_raw.png": (96, 176),
    "input/items/fish_salmon_cooked.png": (96, 208),
    "input/items/fish_salmon_raw.png": (96, 192),
    "input/items/fishing_rod.png": (80, 64),
    "input/items/fishing_rod_cast.png": (80, 80),
    "input/items/fishing_rod_uncast.png": (80, 64),
    "input/items/flint.png": (96, 0),
    "input/items/flint_and_steel.png": (80, 0),
    "input/items/flower_pot.png": (208, 176),
    "input/items/furnace_minecart.png": (112, 160),
    "input/items/ghast_tear.png": (176, 112),
    "input/items/glass_bottle.png": (192, 128),
    "input/items/glistering_melon_slice.png": (144, 128),
    "input/items/glowstone_dust.png": (144, 64),
    "input/items/gold_axe.png": (64, 112),
    "input/items/gold_boots.png": (64, 48),
    "input/items/gold_chestplate.png": (64, 16),
    "input/items/gold_ingot.png": (112, 32),
    "input/items/gold_leggings.png": (64, 32),
    "input/items/gold_nugget.png": (192, 112),
    "input/items/gold_helmet.png": (64, 0),
    "input/items/gold_hoe.png": (64, 128),
    "input/items/gold_horse_armor.png": (64, 144),
    "input/items/gold_pickaxe.png": (64, 96),
    "input/items/gold_shovel.png": (64, 80),
    "input/items/gold_sword.png": (64, 64),
    "input/items/golden_axe.png": (64, 112),
    "input/items/golden_apple.png": (176, 0),
    "input/items/golden_boots.png": (64, 48),
    "input/items/golden_carrot.png": (96, 144),
    "input/items/golden_chestplate.png": (64, 16),
    "input/items/golden_leggings.png": (64, 32),
    "input/items/golden_helmet.png": (64, 0),
    "input/items/golden_hoe.png": (64, 128),
    "input/items/golden_horse_armor.png": (64, 144),
    "input/items/golden_pickaxe.png": (64, 96),
    "input/items/golden_shovel.png": (64, 80),
    "input/items/golden_sword.png": (64, 64),
    "input/items/gray_dye.png": (240, 64),
    "input/items/green_dye.png": (224, 96),
    "input/items/gunpowder.png": (128, 32),
    "input/items/heart_of_the_sea.png": (176, 256),
    "input/items/hopper.png": (128, 176),
    "input/items/hopper_minecart.png": (112, 176),
    "input/items/ink_sac.png": (224, 64),
    "input/items/iron_axe.png": (32, 112),
    "input/items/iron_boots.png": (32, 48),
    "input/items/iron_chestplate.png": (32, 16),
    "input/items/iron_door.png": (192, 32),
    "input/items/iron_helmet.png": (32, 0),
    "input/items/iron_hoe.png": (32, 128),
    "input/items/iron_horse_armor.png": (32, 144),
    "input/items/iron_ingot.png": (112, 16),
    "input/items/iron_leggings.png": (32, 32),
    "input/items/iron_nugget.png": (64, 224),
    "input/items/iron_pickaxe.png": (32, 96),
    "input/items/iron_shovel.png": (32, 80),
    "input/items/iron_sword.png": (32, 64),
    "input/items/item_frame.png": (224, 192),
    "input/items/jungle_boat.png": (176, 208),
    "input/items/jungle_door.png": (48, 208),
    "input/items/kelp.png": (112, 256),
    "input/items/lapis_lazuli.png": (224, 128),
    "input/items/lava_bucket.png": (192, 64),
    "input/items/lead.png": (64, 160),
    "input/items/leather.png": (112, 96),
    "input/items/leather_boots.png": (0, 48),
    "input/items/leather_boots_overlay.png": (0, 192),
    "input/items/leather_chestplate.png": (0, 16),
    "input/items/leather_chestplate_overlay.png": (0, 160),
    "input/items/leather_helmet.png": (0, 0),
    "input/items/leather_helmet_overlay.png": (0, 144),
    "input/items/leather_horse_armor.png": (0, 256),
    "input/items/leather_leggings.png": (0, 32),
    "input/items/leather_leggings_overlay.png": (0, 176),
    "input/items/light_blue_dye.png": (240, 128),
    "input/items/light_gray_dye.png": (224, 176),
    "input/items/lime_dye.png": (240, 96),
    "input/items/lingering_potion.png": (32, 176),
    "input/items/map.png": (192, 48),
    "input/items/map_empty.png": (192, 48),
    "input/items/map_filled.png": (208, 192),
    "input/items/magenta_dye.png": (240, 144),
    "input/items/magma_cream.png": (208, 160),
    "input/items/melon.png": (208, 96),
    "input/items/melon_seeds.png": (224, 48),
    "input/items/melon_slice.png": (208, 96),
    "input/items/melon_speckled.png": (144, 128),
    "input/items/milk_bucket.png": (208, 64),
    "input/items/minecart.png": (112, 128),
    "input/items/minecart_chest.png": (112, 144),
    "input/items/minecart_command_block.png": (112, 208),
    "input/items/minecart_furnace.png": (112, 160),
    "input/items/minecart_hopper.png": (112, 176),
    "input/items/minecart_normal.png": (112, 128),
    "input/items/minecart_tnt.png": (112, 192),
    "input/items/mushroom_stew.png": (128, 64),
    "input/items/music_disc_11.png": (160, 240),
    "input/items/music_disc_13.png": (0, 240),
    "input/items/music_disc_blocks.png": (32, 240),
    "input/items/music_disc_cat.png": (16, 240),
    "input/items/music_disc_chirp.png": (48, 240),
    "input/items/music_disc_far.png": (64, 240),
    "input/items/music_disc_mall.png": (80, 240),
    "input/items/music_disc_mellohi.png": (96, 240),
    "input/items/music_disc_stal.png": (112, 240),
    "input/items/music_disc_strad.png": (128, 240),
    "input/items/music_disc_wait.png": (176, 240),
    "input/items/music_disc_ward.png": (144, 240),
    "input/items/mutton.png": (64, 176),
    "input/items/mutton_cooked.png": (64, 192),
    "input/items/mutton_raw.png": (64, 176),
    "input/items/name_tag.png": (48, 160),
    "input/items/nautilus_shell.png": (160, 256),
    "input/items/nether_brick.png": (80, 160),
    "input/items/nether_star.png": (144, 176),
    "input/items/nether_wart.png": (208, 112),
    "input/items/netherbrick.png": (80, 160),
    "input/items/oak_boat.png": (128, 128),
    "input/items/oak_door.png": (176, 32),
    "input/items/oak_sign.png": (160, 32),
    "input/items/orange_dye.png": (240, 160),
    "input/items/painting.png": (160, 16),
    "input/items/paper.png": (160, 48),
    "input/items/phantom_membrane.png": (240, 256),
    "input/items/pink_dye.png": (240, 80),
    "input/items/poisonous_potato.png": (96, 128),
    "input/items/popped_chorus_fruit.png": (240, 48),
    "input/items/porkchop.png": (112, 80),
    "input/items/porkchop_cooked.png": (128, 80),
    "input/items/porkchop_raw.png": (112, 80),
    "input/items/potato.png": (112, 112),
    "input/items/potato_baked.png": (96, 112),
    "input/items/potato_poisonous.png": (96, 128),
    "input/items/potion.png": (192, 128),
    "input/items/potion_bottle_empty.png": (192, 128),
    "input/items/potion_bottle_drinkable.png": (192, 128),
    "input/items/potion_bottle_splash.png": (160, 144),
    "input/items/potion_bottle_lingering.png": (32, 176),
    "input/items/potion_overlay.png": (208, 128),
    "input/items/prismarine_crystals.png": (224, 208),
    "input/items/prismarine_shard.png": (208, 208),
    "input/items/pufferfish.png": (96, 176),
    "input/items/pufferfish_bucket.png": (224, 240),
    "input/items/pumpkin_pie.png": (128, 144),
    "input/items/pumpkin_seed.png": (208, 48),
    "input/items/pumpkin_seeds.png": (208, 48),
    "input/items/purple_dye.png": (224, 144),
    "input/items/quartz.png": (192, 192),
    "input/items/rabbit.png": (80, 176),
    "input/items/rabbit_cooked.png": (80, 192),
    "input/items/rabbit_foot.png": (80, 224),
    "input/items/rabbit_hide.png": (96, 224),
    "input/items/rabbit_raw.png": (80, 176),
    "input/items/rabbit_stew.png": (80, 208),
    "input/items/record_11.png": (160, 240),
    "input/items/record_13.png": (0, 240),
    "input/items/record_blocks.png": (32, 240),
    "input/items/record_cat.png": (16, 240),
    "input/items/record_chirp.png": (48, 240),
    "input/items/record_far.png": (64, 240),
    "input/items/record_mall.png": (80, 240),
    "input/items/record_mellohi.png": (96, 240),
    "input/items/record_stal.png": (112, 240),
    "input/items/record_strad.png": (128, 240),
    "input/items/record_wait.png": (176, 240),
    "input/items/record_ward.png": (144, 240),
    "input/items/red_dye.png": (224, 80),
    "input/items/redstone.png": (128, 48),
    "input/items/redstone_dust.png": (128, 48),
    "input/items/reeds.png": (176, 16),
    "input/items/repeater.png": (96, 80),
    "input/items/rotten_flesh.png": (176, 80),
    "input/items/saddle.png": (128, 96),
    "input/items/salmon.png": (96, 192),
    "input/items/salmon_bucket.png": (208, 240),
    "input/items/scute.png": (208, 256),
    "input/items/sea_pickle.png": (144, 256),
    "input/items/seeds_melon.png": (224, 48),
    "input/items/seeds_pumpkin.png": (208, 48),
    "input/items/seeds_wheat.png": (144, 0),
    "input/items/shears.png": (208, 80),
    "input/items/shulker_shell.png": (48, 224),
    "input/items/sign.png": (160, 32),
    "input/items/slimeball.png": (224, 16),
    "input/items/slime_ball.png": (224, 16),
    "input/items/snowball.png": (224, 0),
    "input/items/spawn_egg.png": (144, 144),
    "input/items/spawn_egg_overlay.png": (144, 160),
    "input/items/spectral_arrow.png": (16, 144),
    "input/items/spider_eye.png": (176, 128),
    "input/items/spider_eye_fermented.png": (160, 128),
    "input/items/splash_bottle.png": (160, 144),
    "input/items/splash_potion.png": (160, 144),
    "input/items/spruce_boat.png": (192, 208),
    "input/items/spruce_door.png": (64, 208),
    "input/items/stick.png": (80, 48),
    "input/items/stone_axe.png": (16, 112),
    "input/items/stone_hoe.png": (16, 128),
    "input/items/stone_pickaxe.png": (16, 96),
    "input/items/stone_shovel.png": (16, 80),
    "input/items/stone_sword.png": (16, 64),
    "input/items/string.png": (128, 0),
    "input/items/structure_void.png": (0, 224),
    "input/items/sugar.png": (208, 0),
    "input/items/sugar_cane.png": (176, 16),
    "input/items/tipped_arrow_base.png": (16, 160),
    "input/items/tipped_arrow_head.png": (16, 176),
    "input/items/tnt_minecart.png": (112, 192),
    "input/items/totem_of_undying.png": (32, 224),
    "input/items/trident.png": (224, 256),
    "input/items/tropical_fish.png": (96, 160),
    "input/items/tropical_fish_bucket.png": (240, 240),
    "input/items/turtle_helmet.png": (192, 256),
    "input/items/water_bucket.png": (176, 64),
    "input/items/wheat.png": (144, 16),
    "input/items/wheat_seeds.png": (144, 0),
    "input/items/wood_axe.png": (0, 112),
    "input/items/wood_hoe.png": (0, 128),
    "input/items/wood_pickaxe.png": (0, 96),
    "input/items/wood_shovel.png": (0, 80),
    "input/items/wood_sword.png": (0, 64),
    "input/items/wooden_armorstand.png": (128, 192),
    "input/items/wooden_axe.png": (0, 112),
    "input/items/wooden_hoe.png": (0, 128),
    "input/items/wooden_pickaxe.png": (0, 96),
    "input/items/wooden_shovel.png": (0, 80),
    "input/items/wooden_sword.png": (0, 64),
    "input/items/writable_book.png": (176, 176),
    "input/items/written_book.png": (192, 176),
    "input/items/yellow_dye.png": (240, 112)
    }

    # Chemin de l'image de terrain d'origine
    terrain_input_path = "assets/texture/items.png"

    # Chemin de sortie pour l'image de terrain fusionnée
    terrain_output_path = "output/items.png"

    # Copie de l'image de terrain vers le répertoire de sortie
    shutil.copyfile(terrain_input_path, terrain_output_path)

    # Multiplier les coordonnées par 2
    image_dict = multiply_coordinates(image_dict, 1)

    # Appel de la fonction pour fusionner les images sur items.png
    merge_images(image_dict, terrain_output_path, 16, 16, terrain_output_path)

# ------------------------------------------

# Créer l'app
TextureApp = tk.Tk()
TextureApp.title("Converter : Terrain (x16)")
IconPath = os.path.abspath("assets/iconitem.ico")
TextureApp.iconbitmap(IconPath)
TextureApp.geometry("380x280")
TextureApp.resizable(False, False)

# ------------------------------------------

# Load images
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

# Load Font 
FontMojangles = os.path.abspath("assets/Mojangles.ttf")

# ------------------------------------------

#   **--Background--**

# Global Background
Background = tk.Label(TextureApp, bg="#383838")
Background.place(x=0, y=0, width=380, height=400)

# Title Border Background
BorderBackgroundTitleApp = tk.Label(TextureApp, bg="#000000")
BorderBackgroundTitleApp.place(x=0, y=38, width=380, height=2)
BorderBackgroundTitleApp.lift()

# Background Youtube Discord
BackgroundYoutubeDiscord = tk.Label(TextureApp, bg="#585858")
BackgroundYoutubeDiscord.place(x=0, y=250, width=380, height=30)
BackgroundYoutubeDiscord.lift()
BorderBackgroundYoutubeDiscord = tk.Label(TextureApp, bg="#000000")
BorderBackgroundYoutubeDiscord.place(x=0, y=419, width=380, height=2)
BorderBackgroundYoutubeDiscord.lift()

# ------------------------------------------



# Créer le bouton de la conversion
process_button = tk.Button(TextureApp, text="Convert Items (x16)", command=process_images)
process_button.place(x=127.5, y=62)
process_button.configure(relief="solid", bd=2)

# Créer le widget ScrolledText
TextConsole = ScrolledText(TextureApp, width=34, height=7)
TextConsole.place(x=42.5, y=113)
TextConsole.insert(tk.INSERT, "Version : 1.2 - Check if any      update have been made.\n")
TextConsole.insert(tk.INSERT, "----------------------------------\n")
TextConsole.configure(relief="solid", bd=2)

# ------------------------------------------

#   **--Title and Background--** 

TitleAppText = "Items Pack Converter x16"
TitleAppFontSize = 25
TitleAppFont = ImageFont.truetype(FontMojangles, TitleAppFontSize)

# Image and Border
TitleAppImageWidth = 390
TitleAppImageHeight = 35
TitleAppImage = Image.new("RGBA", (TitleAppImageWidth, TitleAppImageHeight), (255, 255, 255, 0))
TitleAppDraw = ImageDraw.Draw(TitleAppImage)
TitleAppOutlineColor = (0, 0, 0)
TitleAppOutlinePosition = (19.5, 4)
TitleAppDraw.text(TitleAppOutlinePosition, TitleAppText, font=TitleAppFont, fill=TitleAppOutlineColor)

# Draw Text
TitleAppTextColor = (255, 255, 255)
TitleAppTextPosition = (17, 2)
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
