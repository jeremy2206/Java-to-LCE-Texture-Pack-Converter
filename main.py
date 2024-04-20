import tkinter as tk
from PIL import ImageTk, Image, ImageFont, ImageDraw
from tkinter.scrolledtext import ScrolledText
import shutil
import webbrowser
import os.path
from collections import defaultdict  # pour images multiples


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #


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
    TextConsole.insert(tk.INSERT, "items.png converted at            output/items.png\n")
    TextConsole.insert(tk.INSERT, "----------------------------------\n")
    TextConsole.see(tk.END)

def resize_imageitems(input_pathitems, output_pathitems, new_widthitems, new_heightitems):
    if os.path.isfile(input_pathitems):
        imageitems = Image.open(input_pathitems)
        resized_imageitems = imageitems.resize((new_widthitems, new_heightitems), Image.LANCZOS)
        resized_imageitems.save(output_pathitems)
    else:
        print(f"L'image {input_pathitems} n'existe pas.")

def process_imagesitems():
    # Dictionnaire des images avec leurs positions
    image_dictitems = {
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
    terrain_input_pathitems = "assets/texture/items.png"

    # Chemin de sortie pour l'image de terrain fusionnée
    terrain_output_pathitems = "output/items.png"

    # Copie de l'image de terrain vers le répertoire de sortie
    shutil.copyfile(terrain_input_pathitems, terrain_output_pathitems)

    # Multiplier les coordonnées par 2
    image_dictitems = multiply_coordinatesitems(image_dictitems, 1)

    # Appel de la fonction pour fusionner les images sur items.png
    merge_imagesitems(image_dictitems, terrain_output_pathitems, 16, 16, terrain_output_pathitems)


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #


def crop_imageterrain(imageterrain, max_widthterrain, max_heightterrain):
    widthterrain, heightterrain = imageterrain.size
    if widthterrain > max_widthterrain or heightterrain > max_heightterrain:
        leftterrain = 0
        topterrain = 0
        rightterrain = min(widthterrain, max_widthterrain)
        bottomterrain = min(heightterrain, max_heightterrain)
        imageterrain = imageterrain.crop((leftterrain, topterrain, rightterrain, bottomterrain))
    return imageterrain

def multiply_coordinatesterrain(image_dictterrain, factorterrain):
    multiplied_image_dictterrain = {}
    for image_pathterrain, positionsterrain in image_dictterrain.items():
        multiplied_positionsterrain = [(coordterrain[0] * factorterrain, coordterrain[1] * factorterrain) for coordterrain in positionsterrain]
        multiplied_image_dictterrain[image_pathterrain] = multiplied_positionsterrain
    return multiplied_image_dictterrain

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
    TextConsole.insert(tk.INSERT, "terrain.png converted at          output/terrain.png\n")
    TextConsole.insert(tk.INSERT, "----------------------------------\n")
    TextConsole.see(tk.END)

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
    image_dictterrain = defaultdict(list)

    image_dictterrain["input/blocks/acacia_door_bottom.png"].append((0, 384))
    image_dictterrain["input/blocks/acacia_door_top.png"].append((0, 368))
    image_dictterrain["input/blocks/acacia_leaves.png"].append((176, 320))
    image_dictterrain["input/blocks/acacia_log.png"].append((128, 320))
    image_dictterrain["input/blocks/acacia_log_top.png"].append((144, 320))
    image_dictterrain["input/blocks/acacia_planks.png"].append((160, 320))
    image_dictterrain["input/blocks/acacia_sapling.png"].append((96, 352))
    image_dictterrain["input/blocks/acacia_trapdoor.png"].append((192, 528))
    image_dictterrain["input/blocks/activator_rail.png"].append((208, 176))
    image_dictterrain["input/blocks/activator_rail_on.png"].append((224, 176))
    image_dictterrain["input/blocks/allium.png"].append((0, 352))
    image_dictterrain["input/blocks/andesite.png"].append((48, 256))
    image_dictterrain["input/blocks/anvil.png"].append((112, 208))
    image_dictterrain["input/blocks/anvil_base.png"].append((112, 208))
    image_dictterrain["input/blocks/anvil_top.png"].append((112, 224))
    image_dictterrain["input/blocks/anvil_top_damaged_0.png"].append((112, 224))
    image_dictterrain["input/blocks/anvil_top_damaged_1.png"].append((128, 208))
    image_dictterrain["input/blocks/anvil_top_damaged_2.png"].append((128, 224))
    image_dictterrain["input/blocks/attached_melon_stem.png"].append((32, 416))
    image_dictterrain["input/blocks/attached_pumpkin_stem.png"].append((240, 112))
    image_dictterrain["input/blocks/azure_bluet.png"].append((32, 352))
    image_dictterrain["input/blocks/beacon.png"].append((144, 32))
    image_dictterrain["input/items/barrier.png"].append((176, 368))
    image_dictterrain["input/blocks/bedrock.png"].append((16, 16))
    image_dictterrain["input/blocks/beetroots_stage0.png"].append((0, 400))
    image_dictterrain["input/blocks/beetroots_stage1.png"].append((16, 400))
    image_dictterrain["input/blocks/beetroots_stage2.png"].append((32, 400))
    image_dictterrain["input/blocks/beetroots_stage3.png"].append((48, 400))
    image_dictterrain["input/blocks/beetroots_stage_0.png"].append((0, 400))
    image_dictterrain["input/blocks/beetroots_stage_1.png"].append((16, 400))
    image_dictterrain["input/blocks/beetroots_stage_2.png"].append((32, 400))
    image_dictterrain["input/blocks/beetroots_stage_3.png"].append((48, 400))
    image_dictterrain["input/blocks/birch_door_bottom.png"].append((16, 384))
    image_dictterrain["input/blocks/birch_door_top.png"].append((16, 368))
    image_dictterrain["input/blocks/birch_leaves.png"].append((176, 352))
    image_dictterrain["input/blocks/birch_log.png"].append((80, 112))
    image_dictterrain["input/blocks/birch_log_top.png"].append((240, 256))
    image_dictterrain["input/blocks/birch_planks.png"].append((96, 208))
    image_dictterrain["input/blocks/birch_sapling.png"].append((240, 64))
    image_dictterrain["input/blocks/birch_trapdoor.png"].append((208, 528))
    image_dictterrain["input/blocks/black_concrete.png"].append((0, 432))
    image_dictterrain["input/blocks/black_concrete_powder.png"].append((0, 432))
    image_dictterrain["input/blocks/black_glazed_terracotta.png"].append((0, 464))
    image_dictterrain["input/blocks/black_stained_glass.png"].append((0, 288))
    image_dictterrain["input/blocks/black_stained_glass_pane_top.png"].append((0, 304))
    image_dictterrain["input/blocks/black_terracotta.png"].append((0, 272))
    image_dictterrain["input/blocks/black_wool.png"].append((16, 112))
    image_dictterrain["input/blocks/blue_concrete.png"].append((16, 432))
    image_dictterrain["input/blocks/blue_concrete_powder.png"].append((16, 448))
    image_dictterrain["input/blocks/blue_glazed_terracotta.png"].append((16, 464))
    image_dictterrain["input/blocks/blue_ice.png"].append((240, 480))
    image_dictterrain["input/blocks/blue_orchid.png"].append((16, 352))
    image_dictterrain["input/blocks/blue_stained_glass.png"].append((16, 288))
    image_dictterrain["input/blocks/blue_stained_glass_pane_top.png"].append((16, 304))
    image_dictterrain["input/blocks/blue_terracotta.png"].append((16, 272))
    image_dictterrain["input/blocks/blue_wool.png"].append((16, 176))
    image_dictterrain["input/blocks/bone_block_side.png"].append((0, 416))
    image_dictterrain["input/blocks/bone_block_top.png"].append((16, 416))
    image_dictterrain["input/blocks/bookshelf.png"].append((48, 32))
    image_dictterrain["input/blocks/brain_coral.png"].append((176, 480))
    image_dictterrain["input/blocks/brain_coral_block.png"].append((96, 480))
    image_dictterrain["input/blocks/brain_coral_fan.png"].append((176, 496))
    image_dictterrain["input/blocks/brewing_stand.png"].append((208, 144))
    image_dictterrain["input/blocks/brewing_stand_base.png"].append((192, 144))
    image_dictterrain["input/blocks/brick.png"].append((112, 0))
    image_dictterrain["input/blocks/bricks.png"].append((112, 0))
    image_dictterrain["input/blocks/brown_concrete.png"].append((32, 432))
    image_dictterrain["input/blocks/brown_concrete_powder.png"].append((32, 448))
    image_dictterrain["input/blocks/brown_glazed_terracotta.png"].append((32, 464))
    image_dictterrain["input/blocks/brown_mushroom.png"].append((208, 16))
    image_dictterrain["input/blocks/brown_mushroom_block.png"].append((224, 112))
    image_dictterrain["input/blocks/brown_stained_glass.png"].append((32, 288))
    image_dictterrain["input/blocks/brown_stained_glass_pane_top.png"].append((32, 304))
    image_dictterrain["input/blocks/brown_terracotta.png"].append((32, 272))
    image_dictterrain["input/blocks/brown_wool.png"].append((16, 160))
    image_dictterrain["input/blocks/bubble_coral.png"].append((160, 480))
    image_dictterrain["input/blocks/bubble_coral_block.png"].append((80, 480))
    image_dictterrain["input/blocks/bubble_coral_fan.png"].append((160, 496))
    image_dictterrain["input/blocks/cactus_bottom.png"].append((112, 64))
    image_dictterrain["input/blocks/cactus_side.png"].append((96, 64))
    image_dictterrain["input/blocks/cactus_top.png"].append((80, 64))
    image_dictterrain["input/blocks/cake_bottom.png"].append((192, 112))
    image_dictterrain["input/blocks/cake_inner.png"].append((176, 112))
    image_dictterrain["input/blocks/cake_side.png"].append((160, 112))
    image_dictterrain["input/blocks/cake_top.png"].append((144, 112))
    image_dictterrain["input/blocks/carrots_stage0.png"].append((128, 192))
    image_dictterrain["input/blocks/carrots_stage1.png"].append((144, 192))
    image_dictterrain["input/blocks/carrots_stage2.png"].append((160, 192))
    image_dictterrain["input/blocks/carrots_stage3.png"].append((176, 192))
    image_dictterrain["input/blocks/carved_pumpkin.png"].append((112, 112))
    image_dictterrain["input/blocks/cauldron_bottom.png"].append((176, 144))
    image_dictterrain["input/blocks/cauldron_inner.png"].append((176, 128))
    image_dictterrain["input/blocks/cauldron_side.png"].append((160, 144))
    image_dictterrain["input/blocks/cauldron_top.png"].append((160, 128))
    image_dictterrain["input/blocks/chain_command_block_back.png"].append((64, 400))
    image_dictterrain["input/blocks/chain_command_block_conditional.png"].append((80, 400))
    image_dictterrain["input/blocks/chain_command_block_front.png"].append((96, 400))
    image_dictterrain["input/blocks/chain_command_block_side.png"].append((112, 400))
    image_dictterrain["input/blocks/chipped_anvil_top.png"].append((128, 208))
    image_dictterrain["input/blocks/chiseled_quartz_block.png"].append((144, 224))
    image_dictterrain["input/blocks/chiseled_quartz_block_top.png"].append((144, 208))
    image_dictterrain["input/blocks/chiseled_red_sandstone.png"].append((224, 352))
    image_dictterrain["input/blocks/chiseled_sandstone.png"].append((80, 224))
    image_dictterrain["input/blocks/chiseled_stone_bricks.png"].append((80, 208))
    image_dictterrain["input/blocks/chorus_flower.png"].append((80, 368))
    image_dictterrain["input/blocks/chorus_flower_dead.png"].append((96, 368))
    image_dictterrain["input/blocks/chorus_flower_plant.png"].append((112, 368))
    image_dictterrain["input/blocks/chorus_plant.png"].append((112, 368))
    image_dictterrain["input/blocks/clay.png"].append((128, 64))
    image_dictterrain["input/blocks/coal_block.png"].append((0, 256))
    image_dictterrain["input/blocks/coal_ore.png"].append((32, 32))
    image_dictterrain["input/blocks/coarse_dirt.png"].append((128, 352))
    image_dictterrain["input/blocks/cobblestone.png"].append((0, 16))
    image_dictterrain["input/blocks/cobweb.png"].append((176, 0))
    image_dictterrain["input/blocks/cobblestone_mossy.png"].append((64, 32))
    image_dictterrain["input/blocks/cocoa_stage0.png"].append((160, 160))
    image_dictterrain["input/blocks/cocoa_stage1.png"].append((144, 160))
    image_dictterrain["input/blocks/cocoa_stage2.png"].append((128, 160))
    image_dictterrain["input/blocks/cocoa_stage_0.png"].append((160, 160))
    image_dictterrain["input/blocks/cocoa_stage_1.png"].append((144, 160))
    image_dictterrain["input/blocks/cocoa_stage_2.png"].append((128, 160))
    image_dictterrain["input/blocks/command_block_back.png"].append((128, 400))
    image_dictterrain["input/blocks/command_block_conditional.png"].append((144, 400))
    image_dictterrain["input/blocks/command_block_front.png"].append((160, 400))
    image_dictterrain["input/blocks/command_block_side.png"].append((176, 400))
    image_dictterrain["input/blocks/comparator.png"].append((176, 176))
    image_dictterrain["input/blocks/comparator_off.png"].append((176, 176))
    image_dictterrain["input/blocks/comparator_on.png"].append((192, 176))
    image_dictterrain["input/blocks/conduit.png"].append((96, 128))
    image_dictterrain["input/blocks/cracked_stonebricks.png"].append((80, 96))
    image_dictterrain["input/blocks/crafting_table_front.png"].append((192, 48))
    image_dictterrain["input/blocks/crafting_table_side.png"].append((176, 48))
    image_dictterrain["input/blocks/crafting_table_top.png"].append((176, 32))
    image_dictterrain["input/blocks/cut_red_sandstone.png"].append((240, 352))
    image_dictterrain["input/blocks/cut_sandstone.png"].append((96, 224))
    image_dictterrain["input/blocks/cyan_concrete.png"].append((48, 432))
    image_dictterrain["input/blocks/cyan_concrete_powder.png"].append((48, 448))
    image_dictterrain["input/blocks/cyan_glazed_terracotta.png"].append((48, 464))
    image_dictterrain["input/blocks/cyan_stained_glass.png"].append((48, 288))
    image_dictterrain["input/blocks/cyan_stained_glass_pane_top.png"].append((48, 304))
    image_dictterrain["input/blocks/cyan_terracotta.png"].append((48, 272))
    image_dictterrain["input/blocks/damaged_anvil_top.png"].append((128, 224))
    image_dictterrain["input/blocks/dandelion.png"].append((208, 0))
    image_dictterrain["input/blocks/dark_oak_door_bottom.png"].append((32, 384))
    image_dictterrain["input/blocks/dark_oak_door_top.png"].append((32, 368))
    image_dictterrain["input/blocks/dark_oak_log.png"].append((128, 336))
    image_dictterrain["input/blocks/dark_oak_log_top.png"].append((144, 336))
    image_dictterrain["input/blocks/dark_oak_leaves.png"].append((176, 336))
    image_dictterrain["input/blocks/dark_oak_planks.png"].append((160, 336))
    image_dictterrain["input/blocks/dark_oak_sapling.png"].append((112, 352))
    image_dictterrain["input/blocks/dark_oak_trapdoor.png"].append((224, 528))
    image_dictterrain["input/blocks/dark_prismarine.png"].append((208, 336))
    image_dictterrain["input/blocks/daylight_detector_inverted_top.png"].append((224, 368))
    image_dictterrain["input/blocks/daylight_detector_side.png"].append((160, 48))
    image_dictterrain["input/blocks/daylight_detector_top.png"].append((144, 48))
    image_dictterrain["input/blocks/deadbush.png"].append((112, 48))
    image_dictterrain["input/blocks/dead_brain_coral_block.png"].append((96, 496))
    image_dictterrain["input/blocks/dead_brain_coral_fan.png"].append((176, 512))
    image_dictterrain["input/blocks/dead_bubble_coral_block.png"].append((80, 496))
    image_dictterrain["input/blocks/dead_bubble_coral_fan.png"].append((160, 512))
    image_dictterrain["input/blocks/dead_bush.png"].append((112, 48))
    image_dictterrain["input/blocks/dead_fire_coral_block.png"].append((112, 496))
    image_dictterrain["input/blocks/dead_fire_coral_fan.png"].append((192, 512))
    image_dictterrain["input/blocks/dead_horn_coral_block.png"].append((128, 496))
    image_dictterrain["input/blocks/dead_horn_coral_fan.png"].append((208, 512))
    image_dictterrain["input/blocks/dead_tube_coral_block.png"].append((64, 496))
    image_dictterrain["input/blocks/dead_tube_coral_fan.png"].append((144, 512))
    image_dictterrain["input/blocks/destroy_stage_0.png"].append((0, 240))
    image_dictterrain["input/blocks/destroy_stage_1.png"].append((16, 240))
    image_dictterrain["input/blocks/destroy_stage_2.png"].append((32, 240))
    image_dictterrain["input/blocks/destroy_stage_3.png"].append((48, 240))
    image_dictterrain["input/blocks/destroy_stage_4.png"].append((64, 240))
    image_dictterrain["input/blocks/destroy_stage_5.png"].append((80, 240))
    image_dictterrain["input/blocks/destroy_stage_6.png"].append((96, 240))
    image_dictterrain["input/blocks/destroy_stage_7.png"].append((112, 240))
    image_dictterrain["input/blocks/destroy_stage_8.png"].append((128, 240))
    image_dictterrain["input/blocks/destroy_stage_9.png"].append((144, 240))
    image_dictterrain["input/blocks/detector_rail.png"].append((48, 192))
    image_dictterrain["input/blocks/detector_rail_on.png"].append((208, 208))
    image_dictterrain["input/blocks/diamond_block.png"].append((128, 16))
    image_dictterrain["input/blocks/diamond_ore.png"].append((32, 48))
    image_dictterrain["input/blocks/diorite.png"].append((80, 256))
    image_dictterrain["input/blocks/dirt.png"].append((32, 0))
    image_dictterrain["input/blocks/dirt_path_side.png"].append((144, 368))
    image_dictterrain["input/blocks/dirt_path_top.png"].append((160, 368))
    image_dictterrain["input/blocks/dirt_podzol_side.png"].append((144, 352))
    image_dictterrain["input/blocks/dirt_podzol_top.png"].append((160, 352))
    image_dictterrain["input/blocks/dispenser_front.png"].append((224, 32))
    image_dictterrain["input/blocks/dispenser_front_horizontal.png"].append((224, 32))
    image_dictterrain["input/blocks/dispenser_front_vertical.png"].append((128, 32))
    image_dictterrain["input/blocks/door_acacia_lower.png"].append((0, 384))
    image_dictterrain["input/blocks/door_acacia_upper.png"].append((0, 368))
    image_dictterrain["input/blocks/door_birch_lower.png"].append((16, 384))
    image_dictterrain["input/blocks/door_birch_upper.png"].append((16, 368))
    image_dictterrain["input/blocks/door_dark_oak_lower.png"].append((32, 384))
    image_dictterrain["input/blocks/door_dark_oak_upper.png"].append((32, 368))
    image_dictterrain["input/blocks/door_iron_lower.png"].append((32, 96))
    image_dictterrain["input/blocks/door_iron_upper.png"].append((32, 80))
    image_dictterrain["input/blocks/door_jungle_lower.png"].append((48, 384))
    image_dictterrain["input/blocks/door_jungle_upper.png"].append((48, 368))
    image_dictterrain["input/blocks/door_spruce_lower.png"].append((64, 384))
    image_dictterrain["input/blocks/door_spruce_upper.png"].append((64, 368))
    image_dictterrain["input/blocks/door_wood_lower.png"].append((16, 96))
    image_dictterrain["input/blocks/door_wood_upper.png"].append((16, 80))
    image_dictterrain["input/blocks/double_plant_fern_bottom.png"].append((0, 336))
    image_dictterrain["input/blocks/double_plant_fern_top.png"].append((0, 320))
    image_dictterrain["input/blocks/double_plant_grass_bottom.png"].append((16, 336))
    image_dictterrain["input/blocks/double_plant_grass_top.png"].append((16, 320))
    image_dictterrain["input/blocks/double_plant_paeonia_bottom.png"].append((32, 336))
    image_dictterrain["input/blocks/double_plant_paeonia_top.png"].append((32, 320))
    image_dictterrain["input/blocks/double_plant_rose_top.png"].append((48, 320))
    image_dictterrain["input/blocks/double_plant_sunflower_back.png"].append((112, 336))
    image_dictterrain["input/blocks/double_plant_sunflower_bottom.png"].append((96, 336))
    image_dictterrain["input/blocks/double_plant_sunflower_front.png"].append((112, 320))
    image_dictterrain["input/blocks/double_plant_sunflower_top.png"].append((96, 320))
    image_dictterrain["input/blocks/double_plant_syringa_bottom.png"].append((64, 336))
    image_dictterrain["input/blocks/double_plant_syringa_top.png"].append((64, 320))
    image_dictterrain["input/blocks/dragon_egg.png"].append((112, 160))
    image_dictterrain["input/blocks/dried_kelp_side.png"].append((16, 496))
    image_dictterrain["input/blocks/dried_kelp_top.png"].append((0, 496))
    image_dictterrain["input/blocks/dropper_front.png"].append((176, 16))
    image_dictterrain["input/blocks/dropper_front_horizontal.png"].append((176, 16))
    image_dictterrain["input/blocks/dropper_front_vertical.png"].append((160, 32))
    image_dictterrain["input/blocks/emerald_block.png"].append((144, 16))
    image_dictterrain["input/blocks/emerald_ore.png"].append((176, 160))
    image_dictterrain["input/blocks/enchanting_table_bottom.png"].append((112, 176))
    image_dictterrain["input/blocks/enchanting_table_side.png"].append((96, 176))
    image_dictterrain["input/blocks/enchanting_table_top.png"].append((96, 160))
    image_dictterrain["input/blocks/end_bricks.png"].append((128, 368))
    image_dictterrain["input/blocks/end_portal_frame_eye.png"].append((224, 160))
    image_dictterrain["input/blocks/end_portal_frame_side.png"].append((240, 144))
    image_dictterrain["input/blocks/end_portal_frame_top.png"].append((224, 144))
    image_dictterrain["input/blocks/end_rod.png"].append((128, 384))
    image_dictterrain["input/blocks/end_stone.png"].append((240, 160))
    image_dictterrain["input/blocks/end_stone_bricks.png"].append((128, 368))
    image_dictterrain["input/blocks/endframe_eye.png"].append((224, 160))
    image_dictterrain["input/blocks/endframe_side.png"].append((240, 144))
    image_dictterrain["input/blocks/endframe_top.png"].append((224, 144))
    image_dictterrain["input/blocks/farmland.png"].append((112, 80))
    image_dictterrain["input/blocks/farmland_dry.png"].append((112, 80))
    image_dictterrain["input/blocks/farmland_moist.png"].append((96, 80))
    image_dictterrain["input/blocks/farmland_wet.png"].append((96, 80))
    image_dictterrain["input/blocks/fern.png"].append((128, 48))
    image_dictterrain["input/blocks/fire_coral.png"].append((192, 480))
    image_dictterrain["input/blocks/fire_coral_block.png"].append((112, 480))
    image_dictterrain["input/blocks/fire_coral_fan.png"].append((192, 496))
    image_dictterrain["input/blocks/flower_allium.png"].append((0, 352))
    image_dictterrain["input/blocks/flower_blue_orchid.png"].append((16, 352))
    image_dictterrain["input/blocks/flower_dandelion.png"].append((208, 0))
    image_dictterrain["input/blocks/flower_houstonia.png"].append((32, 352))
    image_dictterrain["input/blocks/flower_oxeye_daisy.png"].append((48, 352))
    image_dictterrain["input/blocks/flower_pot.png"].append((160, 176))
    image_dictterrain["input/blocks/flower_rose.png"].append((192, 0))
    image_dictterrain["input/blocks/flower_tulip_orange.png"].append((80, 320))
    image_dictterrain["input/blocks/flower_tulip_pink.png"].append((80, 336))
    image_dictterrain["input/blocks/flower_tulip_red.png"].append((64, 352))
    image_dictterrain["input/blocks/flower_tulip_white.png"].append((80, 352))
    image_dictterrain["input/blocks/frosted_ice_0.png"].append((192, 384))
    image_dictterrain["input/blocks/frosted_ice_1.png"].append((208, 384))
    image_dictterrain["input/blocks/frosted_ice_2.png"].append((224, 384))
    image_dictterrain["input/blocks/frosted_ice_3.png"].append((240, 384))
    image_dictterrain["input/blocks/furnace_front.png"].append((192, 32))
    image_dictterrain["input/blocks/furnace_front_off.png"].append((192, 32))
    image_dictterrain["input/blocks/furnace_front_on.png"].append((208, 48))
    image_dictterrain["input/blocks/furnace_side.png"].append((208, 32))
    image_dictterrain["input/blocks/furnace_top.png"].append((224, 48))
    image_dictterrain["input/blocks/glass.png"].append((16, 48))
    image_dictterrain["input/blocks/glass_black.png"].append((0, 288))
    image_dictterrain["input/blocks/glass_blue.png"].append((16, 288))
    image_dictterrain["input/blocks/glass_brown.png"].append((32, 288))
    image_dictterrain["input/blocks/glass_cyan.png"].append((48, 288))
    image_dictterrain["input/blocks/glass_gray.png"].append((64, 288))
    image_dictterrain["input/blocks/glass_green.png"].append((80, 288))
    image_dictterrain["input/blocks/glass_light_blue.png"].append((96, 288))
    image_dictterrain["input/blocks/glass_lime.png"].append((112, 288))
    image_dictterrain["input/blocks/glass_magenta.png"].append((128, 288))
    image_dictterrain["input/blocks/glass_orange.png"].append((144, 288))
    image_dictterrain["input/blocks/glass_pane_top.png"].append((64, 144))
    image_dictterrain["input/blocks/glass_pane_top_black.png"].append((0, 304))
    image_dictterrain["input/blocks/glass_pane_top_blue.png"].append((16, 304))
    image_dictterrain["input/blocks/glass_pane_top_brown.png"].append((32, 304))
    image_dictterrain["input/blocks/glass_pane_top_cyan.png"].append((48, 304))
    image_dictterrain["input/blocks/glass_pane_top_gray.png"].append((64, 304))
    image_dictterrain["input/blocks/glass_pane_top_green.png"].append((80, 304))
    image_dictterrain["input/blocks/glass_pane_top_light_blue.png"].append((96, 304))
    image_dictterrain["input/blocks/glass_pane_top_lime.png"].append((112, 304))
    image_dictterrain["input/blocks/glass_pane_top_magenta.png"].append((128, 304))
    image_dictterrain["input/blocks/glass_pane_top_orange.png"].append((144, 304))
    image_dictterrain["input/blocks/glass_pane_top_pink.png"].append((160, 304))
    image_dictterrain["input/blocks/glass_pane_top_purple.png"].append((176, 304))
    image_dictterrain["input/blocks/glass_pane_top_red.png"].append((192, 304))
    image_dictterrain["input/blocks/glass_pane_top_silver.png"].append((208, 304))
    image_dictterrain["input/blocks/glass_pane_top_white.png"].append((224, 304))
    image_dictterrain["input/blocks/glass_pane_top_yellow.png"].append((240, 304))
    image_dictterrain["input/blocks/glass_pink.png"].append((160, 288))
    image_dictterrain["input/blocks/glass_purple.png"].append((176, 288))
    image_dictterrain["input/blocks/glass_red.png"].append((192, 288))
    image_dictterrain["input/blocks/glass_silver.png"].append((208, 288))
    image_dictterrain["input/blocks/glass_white.png"].append((224, 288))
    image_dictterrain["input/blocks/glass_yellow.png"].append((240, 288))
    image_dictterrain["input/blocks/glowstone.png"].append((144, 96))
    image_dictterrain["input/blocks/gold_block.png"].append((112, 16))
    image_dictterrain["input/blocks/gold_ore.png"].append((0, 32))
    image_dictterrain["input/blocks/granite.png"].append((112, 256))
    image_dictterrain["input/blocks/grass.png"].append((112, 32))
    image_dictterrain["input/blocks/grass_block_side.png"].append((48, 0))
    image_dictterrain["input/blocks/grass_block_side_overlay.png"].append((96, 32))
    image_dictterrain["input/blocks/grass_block_top.png"].append((0, 0))
    image_dictterrain["input/blocks/grass_block_snow.png"].append((64, 64))
    image_dictterrain["input/blocks/grass_blocks_snow.png"].append((64, 64))
    image_dictterrain["input/blocks/grass_blocks_top.png"].append((0, 0))
    image_dictterrain["input/blocks/grass_path_side.png"].append((144, 368))
    image_dictterrain["input/blocks/grass_path_top.png"].append((160, 368))
    image_dictterrain["input/blocks/grass_side.png"].append((48, 0))
    image_dictterrain["input/blocks/grass_side_overlay.png"].append((96, 32))
    image_dictterrain["input/blocks/grass_side_snowed.png"].append((64, 64))
    image_dictterrain["input/blocks/grass_top.png"].append((0, 0))
    image_dictterrain["input/blocks/gravel.png"].append((48, 16))
    image_dictterrain["input/blocks/gray_concrete.png"].append((64, 432))
    image_dictterrain["input/blocks/gray_concrete_powder.png"].append((64, 448))
    image_dictterrain["input/blocks/gray_glazed_terracotta.png"].append((64, 464))
    image_dictterrain["input/blocks/gray_stained_glass.png"].append((64, 288))
    image_dictterrain["input/blocks/gray_stained_glass_pane_top.png"].append((64, 304))
    image_dictterrain["input/blocks/gray_terracotta.png"].append((64, 272))
    image_dictterrain["input/blocks/gray_wool.png"].append((32, 112))
    image_dictterrain["input/blocks/green_concrete.png"].append((80, 432))
    image_dictterrain["input/blocks/green_concrete_powder.png"].append((80, 448))
    image_dictterrain["input/blocks/green_glazed_terracotta.png"].append((80, 464))
    image_dictterrain["input/blocks/green_stained_glass.png"].append((80, 288))
    image_dictterrain["input/blocks/green_stained_glass_pane_top.png"].append((80, 304))
    image_dictterrain["input/blocks/green_terracotta.png"].append((80, 272))
    image_dictterrain["input/blocks/green_wool.png"].append((16, 144))
    image_dictterrain["input/blocks/hardened_clay.png"].append((16, 256))
    image_dictterrain["input/blocks/hardened_clay_stained_black.png"].append((0, 272))
    image_dictterrain["input/blocks/hardened_clay_stained_blue.png"].append((16, 272))
    image_dictterrain["input/blocks/hardened_clay_stained_brown.png"].append((32, 272))
    image_dictterrain["input/blocks/hardened_clay_stained_cyan.png"].append((48, 272))
    image_dictterrain["input/blocks/hardened_clay_stained_gray.png"].append((64, 272))
    image_dictterrain["input/blocks/hardened_clay_stained_green.png"].append((80, 272))
    image_dictterrain["input/blocks/hardened_clay_stained_light_blue.png"].append((96, 272))
    image_dictterrain["input/blocks/hardened_clay_stained_lime.png"].append((112, 272))
    image_dictterrain["input/blocks/hardened_clay_stained_magenta.png"].append((128, 272))
    image_dictterrain["input/blocks/hardened_clay_stained_orange.png"].append((144, 272))
    image_dictterrain["input/blocks/hardened_clay_stained_pink.png"].append((160, 272))
    image_dictterrain["input/blocks/hardened_clay_stained_purple.png"].append((176, 272))
    image_dictterrain["input/blocks/hardened_clay_stained_red.png"].append((192, 272))
    image_dictterrain["input/blocks/hardened_clay_stained_silver.png"].append((208, 272))
    image_dictterrain["input/blocks/hardened_clay_stained_white.png"].append((224, 272))
    image_dictterrain["input/blocks/hardened_clay_stained_yellow.png"].append((240, 272))
    image_dictterrain["input/blocks/hay_block_side.png"].append((160, 240))
    image_dictterrain["input/blocks/hay_block_top.png"].append((208, 240))
    image_dictterrain["input/blocks/hopper_inside.png"].append((192, 224))
    image_dictterrain["input/blocks/hopper_outside.png"].append((192, 208))
    image_dictterrain["input/blocks/hopper_top.png"].append((192, 240))
    image_dictterrain["input/blocks/horn_coral.png"].append((208, 480))
    image_dictterrain["input/blocks/horn_coral_block.png"].append((128, 480))
    image_dictterrain["input/blocks/horn_coral_fan.png"].append((208, 496))
    image_dictterrain["input/blocks/ice.png"].append((48, 64))
    image_dictterrain["input/blocks/ice_packed.png"].append((192, 368))
    image_dictterrain["input/blocks/iron_bars.png"].append((80, 80))
    image_dictterrain["input/blocks/iron_block.png"].append((96, 16))
    image_dictterrain["input/blocks/iron_door_bottom.png"].append((32, 96))
    image_dictterrain["input/blocks/iron_door_top.png"].append((32, 80))
    image_dictterrain["input/blocks/iron_ore.png"].append((16, 32))
    image_dictterrain["input/blocks/iron_trapdoor.png"].append((240, 368))
    image_dictterrain["input/blocks/itemframe.png"].append((144, 176))
    image_dictterrain["input/blocks/item_frame.png"].append((144, 176))
    image_dictterrain["input/blocks/itemframe_background.png"].append((144, 176))
    image_dictterrain["input/blocks/jack_o_lantern.png"].append((128, 112))
    image_dictterrain["input/blocks/jukebox_side.png"].append((160, 64))
    image_dictterrain["input/blocks/jukebox_top.png"].append((176, 64))
    image_dictterrain["input/blocks/jungle_door_bottom.png"].append((48, 384))
    image_dictterrain["input/blocks/jungle_door_top.png"].append((48, 368))
    image_dictterrain["input/blocks/jungle_leaves.png"].append((64, 192))
    image_dictterrain["input/blocks/jungle_log.png"].append((144, 144))
    image_dictterrain["input/blocks/jungle_log_top.png"].append((224, 256))
    image_dictterrain["input/blocks/jungle_planks.png"].append((112, 192))
    image_dictterrain["input/blocks/jungle_sapling.png"].append((224, 16))
    image_dictterrain["input/blocks/jungle_trapdoor.png"].append((240, 528))
    image_dictterrain["input/blocks/kelp.png"].append((64, 512))
    image_dictterrain["input/blocks/kelp.png"].append((80, 512))
    image_dictterrain["input/blocks/kelp.png"].append((96, 512))
    image_dictterrain["input/blocks/kelp.png"].append((112, 512))
    image_dictterrain["input/blocks/kelp_plant.png"].append((0, 512))
    image_dictterrain["input/blocks/kelp_plant.png"].append((16, 512))
    image_dictterrain["input/blocks/kelp_plant.png"].append((32, 512))
    image_dictterrain["input/blocks/kelp_plant.png"].append((48, 512))
    image_dictterrain["input/blocks/ladder.png"].append((48, 80))
    image_dictterrain["input/blocks/lapis_block.png"].append((0, 144))
    image_dictterrain["input/blocks/lapis_ore.png"].append((0, 160))
    image_dictterrain["input/blocks/large_fern_bottom.png"].append((0, 336))
    image_dictterrain["input/blocks/large_fern_top.png"].append((0, 320))
    image_dictterrain["input/blocks/leaves_acacia.png"].append((176, 320))
    image_dictterrain["input/blocks/leaves_big_oak.png"].append((176, 336))
    image_dictterrain["input/blocks/leaves_birch.png"].append((176, 352))
    image_dictterrain["input/blocks/leaves_jungle.png"].append((64, 192))
    image_dictterrain["input/blocks/leaves_oak.png"].append((64, 48))
    image_dictterrain["input/blocks/leaves_spruce.png"].append((64, 128))
    image_dictterrain["input/blocks/lever.png"].append((0, 96))
    image_dictterrain["input/blocks/light_blue_concrete.png"].append((96, 432))
    image_dictterrain["input/blocks/light_blue_concrete_powder.png"].append((96, 448))
    image_dictterrain["input/blocks/light_blue_glazed_terracotta.png"].append((96, 464))
    image_dictterrain["input/blocks/light_blue_stained_glass.png"].append((96, 288))
    image_dictterrain["input/blocks/light_blue_stained_glass_pane_top.png"].append((96, 304))
    image_dictterrain["input/blocks/light_blue_terracotta.png"].append((96, 272))
    image_dictterrain["input/blocks/light_blue_wool.png"].append((32, 176))
    image_dictterrain["input/blocks/light_gray_concrete.png"].append((208, 432))
    image_dictterrain["input/blocks/light_gray_concrete_powder.png"].append((208, 448))
    image_dictterrain["input/blocks/light_gray_glazed_terracotta.png"].append((208, 464))
    image_dictterrain["input/blocks/light_gray_stained_glass.png"].append((208, 288))
    image_dictterrain["input/blocks/light_gray_stained_glass_pane_top.png"].append((208, 304))
    image_dictterrain["input/blocks/light_gray_terracotta.png"].append((208, 272))
    image_dictterrain["input/blocks/light_gray_wool.png"].append((16, 224))
    image_dictterrain["input/blocks/lilac_bottom.png"].append((64, 336))
    image_dictterrain["input/blocks/lilac_top.png"].append((64, 320))
    image_dictterrain["input/blocks/lily_pad.png"].append((208, 96))
    image_dictterrain["input/blocks/lime_concrete.png"].append((112, 432))
    image_dictterrain["input/blocks/lime_concrete_powder.png"].append((112, 448))
    image_dictterrain["input/blocks/lime_glazed_terracotta.png"].append((112, 464))
    image_dictterrain["input/blocks/lime_stained_glass.png"].append((112, 288))
    image_dictterrain["input/blocks/lime_stained_glass_pane_top.png"].append((112, 304))
    image_dictterrain["input/blocks/lime_terracotta.png"].append((112, 272))
    image_dictterrain["input/blocks/lime_wool.png"].append((32, 144))
    image_dictterrain["input/blocks/magenta_concrete.png"].append((128, 432))
    image_dictterrain["input/blocks/magenta_concrete_powder.png"].append((128, 448))
    image_dictterrain["input/blocks/magenta_glazed_terracotta.png"].append((128, 464))
    image_dictterrain["input/blocks/magenta_stained_glass.png"].append((128, 288))
    image_dictterrain["input/blocks/magenta_stained_glass_pane_top.png"].append((128, 304))
    image_dictterrain["input/blocks/magenta_terracotta.png"].append((128, 272))
    image_dictterrain["input/blocks/magenta_wool.png"].append((32, 192))
    image_dictterrain["input/blocks/magma.png"].append((144, 384))
    image_dictterrain["input/blocks/magma_block.png"].append((144, 384))
    image_dictterrain["input/blocks/melon_side.png"].append((128, 128))
    image_dictterrain["input/blocks/melon_stem.png"].append((48, 416))
    image_dictterrain["input/blocks/melon_stem_connected.png"].append((32, 416))
    image_dictterrain["input/blocks/melon_stem_disconnected.png"].append((48, 416))
    image_dictterrain["input/blocks/melon_top.png"].append((144, 128))
    image_dictterrain["input/blocks/mob_spawner.png"].append((16, 64))
    image_dictterrain["input/blocks/mossy_cobblestone.png"].append((64, 32))
    image_dictterrain["input/blocks/mossy_stone_bricks.png"].append((64, 96))
    image_dictterrain["input/blocks/mushroom_block_inside.png"].append((224, 128))
    image_dictterrain["input/blocks/mushroom_block_skin_brown.png"].append((224, 112))
    image_dictterrain["input/blocks/mushroom_block_skin_inside.png"].append((208, 112))
    image_dictterrain["input/blocks/mushroom_block_skin_stem.png"].append((208, 128))
    image_dictterrain["input/blocks/mushroom_brown.png"].append((208, 16))
    image_dictterrain["input/blocks/mushroom_red.png"].append((192, 16))
    image_dictterrain["input/blocks/mushroom_stem.png"].append((208, 128))
    image_dictterrain["input/blocks/mycelium_side.png"].append((208, 64))
    image_dictterrain["input/blocks/mycelium_top.png"].append((224, 64))
    image_dictterrain["input/blocks/netherrack.png"].append((112, 96))
    image_dictterrain["input/blocks/nether_brick.png"].append((0, 224))
    image_dictterrain["input/blocks/nether_bricks.png"].append((0, 224))
    image_dictterrain["input/blocks/nether_quartz_ore.png"].append((240, 176))
    image_dictterrain["input/blocks/nether_wart_block.png"].append((160, 384))
    image_dictterrain["input/blocks/nether_wart_stage0.png"].append((32, 224))
    image_dictterrain["input/blocks/nether_wart_stage1.png"].append((48, 224))
    image_dictterrain["input/blocks/nether_wart_stage2.png"].append((64, 224))
    image_dictterrain["input/blocks/nether_wart_stage_0.png"].append((32, 224))
    image_dictterrain["input/blocks/nether_wart_stage_1.png"].append((48, 224))
    image_dictterrain["input/blocks/nether_wart_stage_2.png"].append((64, 224))
    image_dictterrain["input/blocks/note_block.png"].append((32, 256))
    image_dictterrain["input/blocks/noteblock.png"].append((32, 256))
    image_dictterrain["input/blocks/oak_door_bottom.png"].append((16, 96))
    image_dictterrain["input/blocks/oak_door_top.png"].append((16, 80))
    image_dictterrain["input/blocks/oak_leave.png"].append((64, 48))
    image_dictterrain["input/blocks/oak_leaves.png"].append((64, 48))
    image_dictterrain["input/blocks/oak_log.png"].append((64, 16))
    image_dictterrain["input/blocks/oak_log_top.png"].append((80, 16))
    image_dictterrain["input/blocks/oak_planks.png"].append((64, 0))
    image_dictterrain["input/blocks/oak_sapling.png"].append((240, 0))
    image_dictterrain["input/blocks/oak_trapdoor.png"].append((64, 80))
    image_dictterrain["input/blocks/observer_back.png"].append((96, 416))
    image_dictterrain["input/blocks/observer_back_off.png"].append((112, 416))
    image_dictterrain["input/blocks/observer_back_on.png"].append((112, 416))
    image_dictterrain["input/blocks/observer_front.png"].append((64, 416))
    image_dictterrain["input/blocks/observer_side.png"].append((80, 416))
    image_dictterrain["input/blocks/observer_top.png"].append((128, 416))
    image_dictterrain["input/blocks/obsidian.png"].append((80, 32))
    image_dictterrain["input/blocks/orange_concrete.png"].append((144, 432))
    image_dictterrain["input/blocks/orange_concrete_powder.png"].append((144, 448))
    image_dictterrain["input/blocks/orange_glazed_terracotta.png"].append((144, 464))
    image_dictterrain["input/blocks/orange_stained_glass.png"].append((144, 288))
    image_dictterrain["input/blocks/orange_stained_glass_pane_top.png"].append((144, 304))
    image_dictterrain["input/blocks/orange_terracotta.png"].append((144, 272))
    image_dictterrain["input/blocks/orange_tulip.png"].append((80, 320))
    image_dictterrain["input/blocks/orange_wool.png"].append((32, 208))
    image_dictterrain["input/blocks/oxeye_daisy.png"].append((48, 352))
    image_dictterrain["input/blocks/packed_ice.png"].append((192, 368))
    image_dictterrain["input/blocks/peony_bottom.png"].append((32, 336))
    image_dictterrain["input/blocks/peony_top.png"].append((32, 320))
    image_dictterrain["input/blocks/pink_concrete.png"].append((160, 432))
    image_dictterrain["input/blocks/pink_concrete_powder.png"].append((160, 448))
    image_dictterrain["input/blocks/pink_glazed_terracotta.png"].append((160, 464))
    image_dictterrain["input/blocks/pink_stained_glass.png"].append((160, 288))
    image_dictterrain["input/blocks/pink_stained_glass_pane_top.png"].append((160, 304))
    image_dictterrain["input/blocks/pink_terracotta.png"].append((160, 272))
    image_dictterrain["input/blocks/pink_tulip.png"].append((80, 336))
    image_dictterrain["input/blocks/pink_wool.png"].append((32, 128))
    image_dictterrain["input/blocks/piston_bottom.png"].append((208, 96))
    image_dictterrain["input/blocks/piston_inner.png"].append((224, 96))
    image_dictterrain["input/blocks/piston_side.png"].append((192, 96))
    image_dictterrain["input/blocks/piston_top.png"].append((176, 96))
    image_dictterrain["input/blocks/piston_top_normal.png"].append((176, 96))
    image_dictterrain["input/blocks/piston_top_sticky.png"].append((160, 96))
    image_dictterrain["input/blocks/planks_acacia.png"].append((112, 192))
    image_dictterrain["input/blocks/planks_big_oak.png"].append((160, 336))
    image_dictterrain["input/blocks/planks_birch.png"].append((96, 208))
    image_dictterrain["input/blocks/planks_jungle.png"].append((112, 192))
    image_dictterrain["input/blocks/planks_oak.png"].append((64, 0))
    image_dictterrain["input/blocks/planks_spruce.png"].append((96, 192))
    image_dictterrain["input/blocks/podzol_side.png"].append((144, 352))
    image_dictterrain["input/blocks/podzol_top.png"].append((160, 352))
    image_dictterrain["input/blocks/polished_andesite.png"].append((64, 256))
    image_dictterrain["input/blocks/polished_diorite.png"].append((96, 256))
    image_dictterrain["input/blocks/polished_granite.png"].append((128, 256))
    image_dictterrain["input/blocks/poppy.png"].append((192, 0))
    image_dictterrain["input/blocks/potato_stage0.png"].append((144, 256))
    image_dictterrain["input/blocks/potato_stage1.png"].append((160, 256))
    image_dictterrain["input/blocks/potato_stage2.png"].append((176, 256))
    image_dictterrain["input/blocks/potato_stage3.png"].append((192, 256))
    image_dictterrain["input/blocks/potato_stage_0.png"].append((144, 256))
    image_dictterrain["input/blocks/potato_stage_1.png"].append((160, 256))
    image_dictterrain["input/blocks/potato_stage_2.png"].append((176, 256))
    image_dictterrain["input/blocks/potato_stage_3.png"].append((192, 256))
    image_dictterrain["input/blocks/potatoes_stage0.png"].append((144, 256))
    image_dictterrain["input/blocks/potatoes_stage1.png"].append((160, 256))
    image_dictterrain["input/blocks/potatoes_stage2.png"].append((176, 256))
    image_dictterrain["input/blocks/potatoes_stage3.png"].append((192, 256))
    image_dictterrain["input/blocks/powered_rail.png"].append((48, 160))
    image_dictterrain["input/blocks/powered_rail_on.png"].append((48, 176))
    image_dictterrain["input/blocks/prismarine.png"].append((208, 352))
    image_dictterrain["input/blocks/prismarine_bricks.png"].append((208, 320))
    image_dictterrain["input/blocks/prismarine_dark.png"].append((208, 336))
    image_dictterrain["input/blocks/prismarine_rough.png"].append((208, 352))
    image_dictterrain["input/blocks/pumpkin_face_off.png"].append((112, 112))
    image_dictterrain["input/blocks/pumpkin_face_on.png"].append((128, 112))
    image_dictterrain["input/blocks/pumpkin_side.png"].append((96, 112))
    image_dictterrain["input/blocks/pumpkin_stem.png"].append((240, 96))
    image_dictterrain["input/blocks/pumpkin_stem_connected.png"].append((240, 112))
    image_dictterrain["input/blocks/pumpkin_stem_disconnected.png"].append((240, 96))
    image_dictterrain["input/blocks/pumpkin_top.png"].append((96, 96))
    image_dictterrain["input/blocks/purple_concrete.png"].append((176, 432))
    image_dictterrain["input/blocks/purple_concrete_powder.png"].append((176, 448))
    image_dictterrain["input/blocks/purple_glazed_terracotta.png"].append((176, 464))
    image_dictterrain["input/blocks/purple_stained_glass.png"].append((176, 288))
    image_dictterrain["input/blocks/purple_stained_glass_pane_top.png"].append((176, 304))
    image_dictterrain["input/blocks/purple_terracotta.png"].append((176, 272))
    image_dictterrain["input/blocks/purple_wool.png"].append((16, 192))
    image_dictterrain["input/blocks/purpur_block.png"].append((80, 384))
    image_dictterrain["input/blocks/purpur_pillar.png"].append((96, 384))
    image_dictterrain["input/blocks/purpur_pillar_top.png"].append((112, 384))
    image_dictterrain["input/blocks/quartz_block_bottom.png"].append((176, 240))
    image_dictterrain["input/blocks/quartz_block_chiseled.png"].append((144, 224))
    image_dictterrain["input/blocks/quartz_block_chiseled_top.png"].append((144, 208))
    image_dictterrain["input/blocks/quartz_block_lines.png"].append((160, 224))
    image_dictterrain["input/blocks/quartz_block_lines_top.png"].append((160, 208))
    image_dictterrain["input/blocks/quartz_block_side.png"].append((176, 224))
    image_dictterrain["input/blocks/quartz_block_top.png"].append((176, 208))
    image_dictterrain["input/blocks/quartz_ore.png"].append((240, 176))
    image_dictterrain["input/blocks/quartz_pillar.png"].append((160, 224))
    image_dictterrain["input/blocks/quartz_pillar_top.png"].append((160, 208))
    image_dictterrain["input/blocks/rail.png"].append((0, 128))
    image_dictterrain["input/blocks/rail_corner.png"].append((0, 112))
    image_dictterrain["input/blocks/rail_activator.png"].append((208, 176))
    image_dictterrain["input/blocks/rail_activator_powered.png"].append((224, 176))
    image_dictterrain["input/blocks/rail_detector.png"].append((48, 192))
    image_dictterrain["input/blocks/rail_detector_powered.png"].append((208, 208))
    image_dictterrain["input/blocks/rail_golden.png"].append((48, 160))
    image_dictterrain["input/blocks/rail_golden_powered.png"].append((48, 176))
    image_dictterrain["input/blocks/rail_normal.png"].append((0, 128))
    image_dictterrain["input/blocks/rail_normal_turned.png"].append((0, 112))
    image_dictterrain["input/blocks/red_concrete.png"].append((192, 432))
    image_dictterrain["input/blocks/red_concrete_powder.png"].append((192, 448))
    image_dictterrain["input/blocks/red_glazed_terracotta.png"].append((192, 464))
    image_dictterrain["input/blocks/red_mushroom.png"].append((192, 16))
    image_dictterrain["input/blocks/red_mushroom_block.png"].append((208, 112))
    image_dictterrain["input/blocks/red_sand.png"].append((224, 320))
    image_dictterrain["input/blocks/red_sandstone.png"].append((240, 336))
    image_dictterrain["input/blocks/red_sandstone_bottom.png"].append((224, 336))
    image_dictterrain["input/blocks/red_sandstone_carved.png"].append((224, 352))
    image_dictterrain["input/blocks/red_sandstone_normal.png"].append((240, 336))
    image_dictterrain["input/blocks/red_sandstone_smooth.png"].append((240, 352))
    image_dictterrain["input/blocks/red_sandstone_top.png"].append((240, 320))
    image_dictterrain["input/blocks/red_nether_bricks.png"].append((176, 384))
    image_dictterrain["input/blocks/red_stained_glass.png"].append((192, 288))
    image_dictterrain["input/blocks/red_stained_glass_pane_top.png"].append((192, 304))
    image_dictterrain["input/blocks/red_terracotta.png"].append((192, 272))
    image_dictterrain["input/blocks/red_tulip.png"].append((64, 352))
    image_dictterrain["input/blocks/red_wool.png"].append((16, 128))
    image_dictterrain["input/blocks/redstone_block.png"].append((160, 16))
    image_dictterrain["input/blocks/redstone_lamp.png"].append((48, 208))
    image_dictterrain["input/blocks/redstone_lamp_off.png"].append((48, 208))
    image_dictterrain["input/blocks/redstone_lamp_on.png"].append((64, 208))
    image_dictterrain["input/blocks/redstone_ore.png"].append((48, 48))
    image_dictterrain["input/blocks/redstone_torch.png"].append((48, 96))
    image_dictterrain["input/blocks/redstone_torch_off.png"].append((48, 112))
    image_dictterrain["input/blocks/redstone_torch_on.png"].append((48, 96))
    image_dictterrain["input/blocks/reeds.png"].append((144, 64))
    image_dictterrain["input/blocks/repeater.png"].append((48, 128))
    image_dictterrain["input/blocks/repeater_off.png"].append((48, 128))
    image_dictterrain["input/blocks/repeater_on.png"].append((48, 144))
    image_dictterrain["input/blocks/repeating_command_block_back.png"].append((192, 400))
    image_dictterrain["input/blocks/repeating_command_block_conditional.png"].append((208, 400))
    image_dictterrain["input/blocks/repeating_command_block_front.png"].append((224, 400))
    image_dictterrain["input/blocks/repeating_command_block_side.png"].append((240, 400))
    image_dictterrain["input/blocks/rose_bush_bottom.png"].append((48, 336))
    image_dictterrain["input/blocks/rose_bush_top.png"].append((48, 320))
    image_dictterrain["input/blocks/sand.png"].append((32, 16))
    image_dictterrain["input/blocks/sandstone.png"].append((0, 192))
    image_dictterrain["input/blocks/sandstone_bottom.png"].append((0, 208))
    image_dictterrain["input/blocks/sandstone_carved.png"].append((80, 224))
    image_dictterrain["input/blocks/sandstone_normal.png"].append((0, 192))
    image_dictterrain["input/blocks/sandstone_smooth.png"].append((96, 224))
    image_dictterrain["input/blocks/sandstone_top.png"].append((0, 176))
    image_dictterrain["input/blocks/sapling_acacia.png"].append((96, 352))
    image_dictterrain["input/blocks/sapling_birch.png"].append((240, 64))
    image_dictterrain["input/blocks/sapling_jungle.png"].append((224, 16))
    image_dictterrain["input/blocks/sapling_oak.png"].append((240, 0))
    image_dictterrain["input/blocks/sapling_roofed_oak.png"].append((112, 352))
    image_dictterrain["input/blocks/sapling_spruce.png"].append((240, 48))
    image_dictterrain["input/blocks/sea_lantern.png"].append((208, 368))
    image_dictterrain["input/blocks/sea_pickle.png"].append((224, 480))
    image_dictterrain["input/blocks/seagrass.png"].append((128, 512))
    image_dictterrain["input/blocks/seagrass.png"].append((32, 496))
    image_dictterrain["input/blocks/slime_block.png"].append((192, 192))
    image_dictterrain["input/blocks/smooth_stone_slab_side.png"].append((80, 0))
    image_dictterrain["input/blocks/smooth_stone.png"].append((96, 0))
    image_dictterrain["input/blocks/snow.png"].append((32, 64))
    image_dictterrain["input/blocks/soul_sand.png"].append((128, 96))
    image_dictterrain["input/blocks/spawner.png"].append((16, 64))
    image_dictterrain["input/blocks/sponge.png"].append((0, 48))
    image_dictterrain["input/blocks/sponge_wet.png"].append((192, 128))
    image_dictterrain["input/blocks/spruce_door_bottom.png"].append((64, 384))
    image_dictterrain["input/blocks/spruce_door_top.png"].append((64, 368))
    image_dictterrain["input/blocks/spruce_leaves.png"].append((64, 128))
    image_dictterrain["input/blocks/spruce_log.png"].append((64, 112))
    image_dictterrain["input/blocks/spruce_log_top.png"].append((208, 256))
    image_dictterrain["input/blocks/spruce_planks.png"].append((96, 192))
    image_dictterrain["input/blocks/spruce_sapling.png"].append((240, 48))
    image_dictterrain["input/blocks/spruce_trapdoor.png"].append((240, 512))
    image_dictterrain["input/blocks/stone.png"].append((16, 0))
    image_dictterrain["input/blocks/stone_andesite.png"].append((48, 256))
    image_dictterrain["input/blocks/stone_andesite_smooth.png"].append((64, 256))
    image_dictterrain["input/blocks/stone_brick.png"].append((96, 48))
    image_dictterrain["input/blocks/stone_bricks.png"].append((96, 48))
    image_dictterrain["input/blocks/stone_diorite.png"].append((80, 256))
    image_dictterrain["input/blocks/stone_diorite_smooth.png"].append((96, 256))
    image_dictterrain["input/blocks/stone_granite.png"].append((112, 256))
    image_dictterrain["input/blocks/stone_granite_smooth.png"].append((128, 256))
    image_dictterrain["input/blocks/stone_slab_side.png"].append((80, 0))
    image_dictterrain["input/blocks/stone_slab_top.png"].append((96, 0))
    image_dictterrain["input/blocks/stonebrick.png"].append((96, 48))
    image_dictterrain["input/blocks/stonebrick_carved.png"].append((80, 208))
    image_dictterrain["input/blocks/stonebrick_cracked.png"].append((80, 96))
    image_dictterrain["input/blocks/stonebrick_mossy.png"].append((64, 96))
    image_dictterrain["input/blocks/stripped_acacia_log.png"].append((32, 528))
    image_dictterrain["input/blocks/stripped_acacia_log_top.png"].append((48, 528))
    image_dictterrain["input/blocks/stripped_birch_log.png"].append((64, 528))
    image_dictterrain["input/blocks/stripped_birch_log_top.png"].append((80, 528))
    image_dictterrain["input/blocks/stripped_dark_oak_log.png"].append((96, 528))
    image_dictterrain["input/blocks/stripped_dark_oak_log_top.png"].append((112, 528))
    image_dictterrain["input/blocks/stripped_jungle_log.png"].append((128, 528))
    image_dictterrain["input/blocks/stripped_jungle_log_top.png"].append((144, 528))
    image_dictterrain["input/blocks/stripped_oak_log.png"].append((0, 528))
    image_dictterrain["input/blocks/stripped_oak_log_top.png"].append((16, 528))
    image_dictterrain["input/blocks/stripped_spruce_log.png"].append((160, 528))
    image_dictterrain["input/blocks/stripped_spruce_log_top.png"].append((176, 528))
    image_dictterrain["input/blocks/structure_block.png"].append((176, 416))
    image_dictterrain["input/blocks/structure_block_corner.png"].append((192, 416))
    image_dictterrain["input/blocks/structure_block_data.png"].append((208, 416))
    image_dictterrain["input/blocks/structure_block_load.png"].append((224, 416))
    image_dictterrain["input/blocks/structure_block_save.png"].append((240, 416))
    image_dictterrain["input/blocks/sugar_cane.png"].append((144, 64))
    image_dictterrain["input/blocks/sunflower_back.png"].append((112, 336))
    image_dictterrain["input/blocks/sunflower_bottom.png"].append((96, 336))
    image_dictterrain["input/blocks/sunflower_front.png"].append((112, 320))
    image_dictterrain["input/blocks/sunflower_top.png"].append((96, 320))
    image_dictterrain["input/blocks/tall_grass_bottom.png"].append((16, 336))
    image_dictterrain["input/blocks/tall_grass_top.png"].append((16, 320))
    image_dictterrain["input/blocks/tall_seagrass_bottom.png"].append((48, 496))
    image_dictterrain["input/blocks/tall_seagrass_top.png"].append((48, 480))
    image_dictterrain["input/blocks/tallgrass.png"].append((112, 32))
    image_dictterrain["input/blocks/terracotta.png"].append((16, 256))
    image_dictterrain["input/blocks/tnt_bottom.png"].append((160, 0))
    image_dictterrain["input/blocks/tnt_side.png"].append((128, 0))
    image_dictterrain["input/blocks/tnt_top.png"].append((144, 0))
    image_dictterrain["input/blocks/torch.png"].append((0, 80))
    image_dictterrain["input/blocks/torch_on.png"].append((0, 80))
    image_dictterrain["input/blocks/trapdoor.png"].append((64, 80))
    image_dictterrain["input/blocks/trip_wire.png"].append((208, 160))
    image_dictterrain["input/blocks/trip_wire_source.png"].append((192, 160))
    image_dictterrain["input/blocks/tripwire.png"].append((208, 160))
    image_dictterrain["input/blocks/tripwire_hook.png"].append((192, 160))
    image_dictterrain["input/blocks/tube_coral.png"].append((144, 480))
    image_dictterrain["input/blocks/tube_coral_block.png"].append((64, 480))
    image_dictterrain["input/blocks/tube_coral_fan.png"].append((144, 496))
    image_dictterrain["input/blocks/turtle_egg.png"].append((112, 128))
    image_dictterrain["input/blocks/turtle_egg_slightly_cracked.png"].append((112, 144))
    image_dictterrain["input/blocks/turtle_egg_very_cracked.png"].append((128, 144))
    image_dictterrain["input/blocks/vine.png"].append((240, 128))
    image_dictterrain["input/blocks/waterlily.png"].append((192, 64))
    image_dictterrain["input/blocks/web.png"].append((176, 0))
    image_dictterrain["input/blocks/wet_sponge.png"].append((192, 128))
    image_dictterrain["input/blocks/wheat_stage0.png"].append((128, 80))
    image_dictterrain["input/blocks/wheat_stage1.png"].append((144, 80))
    image_dictterrain["input/blocks/wheat_stage2.png"].append((160, 80))
    image_dictterrain["input/blocks/wheat_stage3.png"].append((176, 80))
    image_dictterrain["input/blocks/wheat_stage4.png"].append((192, 80))
    image_dictterrain["input/blocks/wheat_stage5.png"].append((208, 80))
    image_dictterrain["input/blocks/wheat_stage6.png"].append((224, 80))
    image_dictterrain["input/blocks/wheat_stage7.png"].append((240, 80))
    image_dictterrain["input/blocks/wheat_stage_0.png"].append((128, 80))
    image_dictterrain["input/blocks/wheat_stage_1.png"].append((144, 80))
    image_dictterrain["input/blocks/wheat_stage_2.png"].append((160, 80))
    image_dictterrain["input/blocks/wheat_stage_3.png"].append((176, 80))
    image_dictterrain["input/blocks/wheat_stage_4.png"].append((192, 80))
    image_dictterrain["input/blocks/wheat_stage_5.png"].append((208, 80))
    image_dictterrain["input/blocks/wheat_stage_6.png"].append((224, 80))
    image_dictterrain["input/blocks/wheat_stage_7.png"].append((240, 80))
    image_dictterrain["input/blocks/white_concrete.png"].append((224, 432))
    image_dictterrain["input/blocks/white_concrete_powder.png"].append((224, 448))
    image_dictterrain["input/blocks/white_glazed_terracotta.png"].append((224, 464))
    image_dictterrain["input/blocks/white_stained_glass.png"].append((224, 288))
    image_dictterrain["input/blocks/white_stained_glass_pane_top.png"].append((224, 304))
    image_dictterrain["input/blocks/white_terracotta.png"].append((224, 272))
    image_dictterrain["input/blocks/white_tulip.png"].append((80, 352))
    image_dictterrain["input/blocks/white_wool.png"].append((0, 64))
    image_dictterrain["input/blocks/wool_colored_black.png"].append((16, 112))
    image_dictterrain["input/blocks/wool_colored_blue.png"].append((16, 176))
    image_dictterrain["input/blocks/wool_colored_brown.png"].append((16, 160))
    image_dictterrain["input/blocks/wool_colored_cyan.png"].append((16, 208))
    image_dictterrain["input/blocks/wool_colored_gray.png"].append((32, 112))
    image_dictterrain["input/blocks/wool_colored_green.png"].append((16, 144))
    image_dictterrain["input/blocks/wool_colored_light_blue.png"].append((32, 176))
    image_dictterrain["input/blocks/wool_colored_lime.png"].append((32, 144))
    image_dictterrain["input/blocks/wool_colored_magenta.png"].append((32, 192))
    image_dictterrain["input/blocks/wool_colored_orange.png"].append((32, 208))
    image_dictterrain["input/blocks/wool_colored_pink.png"].append((32, 128))
    image_dictterrain["input/blocks/wool_colored_purple.png"].append((16, 192))
    image_dictterrain["input/blocks/wool_colored_red.png"].append((16, 128))
    image_dictterrain["input/blocks/wool_colored_silver.png"].append((16, 224))
    image_dictterrain["input/blocks/wool_colored_white.png"].append((0, 64))
    image_dictterrain["input/blocks/wool_colored_yellow.png"].append((32, 160))
    image_dictterrain["input/blocks/yellow_concrete.png"].append((240, 432))
    image_dictterrain["input/blocks/yellow_concrete_powder.png"].append((240, 448))
    image_dictterrain["input/blocks/yellow_glazed_terracotta.png"].append((240, 464))
    image_dictterrain["input/blocks/yellow_stained_glass.png"].append((240, 288))
    image_dictterrain["input/blocks/yellow_stained_glass_pane_top.png"].append((240, 304))
    image_dictterrain["input/blocks/yellow_terracotta.png"].append((240, 272))
    image_dictterrain["input/blocks/yellow_wool.png"].append((32, 160))

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
    TextConsole.insert(tk.INSERT, "terrainMipMapLevel2.png converted output/terrainMipMapLevel2.png\n")
    TextConsole.insert(tk.INSERT, "----------------------------------\n")
    TextConsole.see(tk.END)

    # Copier et redimensionner terrainMipMapLevel2.png pour terrainMipMapLevel3.png
    shutil.copyfile("output/terrainMipMapLevel2.png", "output/terrainMipMapLevel3.png")
    resize_imageterrain("output/terrainMipMapLevel3.png", "output/terrainMipMapLevel3.png", 64 * multiplierterrain, 136 * multiplierterrain)
    TextConsole.insert(tk.INSERT, "terrainMipMapLevel3.png converted output/terrainMipMapLevel3.png\n")
    TextConsole.insert(tk.INSERT, "----------------------------------\n")
    TextConsole.see(tk.END)


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #


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


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #


def multiply_coordinatespainting(image_dictpainting, factorpainting):
    multiplied_image_dictpainting = {}
    for image_pathpainting, positionspainting in image_dictpainting.items():
        multiplied_positionspainting= [(coordpainting[0] * factorpainting, coordpainting[1] * factorpainting) for coordpainting in positionspainting]
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

    TextConsole.insert(tk.INSERT, "kz.png converted at output/kz.png\n")
    TextConsole.insert(tk.INSERT, "----------------------------------\n")
    TextConsole.see(tk.END)

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
    image_dictpainting = defaultdict(list)

    image_dictpainting["input/painting/alban.png"].append((32, 0))
    image_dictpainting["input/painting/alban.png"].append((32, 16))
    image_dictpainting["input/painting/aztec.png"].append((16, 0))
    image_dictpainting["input/painting/aztec.png"].append((16, 16))
    image_dictpainting["input/painting/aztec2.png"].append((48, 0))
    image_dictpainting["input/painting/aztec2.png"].append((48, 16))
    image_dictpainting["input/painting/back.png"].append((192, 0))
    image_dictpainting["input/painting/back.png"].append((208, 0))
    image_dictpainting["input/painting/back.png"].append((224, 0))
    image_dictpainting["input/painting/back.png"].append((240, 0))
    image_dictpainting["input/painting/back.png"].append((192, 16))
    image_dictpainting["input/painting/back.png"].append((208, 16))
    image_dictpainting["input/painting/back.png"].append((224, 16))
    image_dictpainting["input/painting/back.png"].append((240, 16))
    image_dictpainting["input/painting/back.png"].append((192, 32))
    image_dictpainting["input/painting/back.png"].append((208, 32))
    image_dictpainting["input/painting/back.png"].append((224, 32))
    image_dictpainting["input/painting/back.png"].append((240, 32))
    image_dictpainting["input/painting/back.png"].append((192, 48))
    image_dictpainting["input/painting/back.png"].append((208, 48))
    image_dictpainting["input/painting/back.png"].append((224, 48))
    image_dictpainting["input/painting/back.png"].append((240, 48))
    image_dictpainting["input/painting/bomb.png"].append((64, 0))
    image_dictpainting["input/painting/bomb.png"].append((64, 16))
    image_dictpainting["input/painting/burning_skull.png"].append((128, 192))
    image_dictpainting["input/painting/bust.png"].append((32, 128))
    image_dictpainting["input/painting/courbet.png"].append((32, 32))
    image_dictpainting["input/painting/creebet.png"].append((128, 32))
    image_dictpainting["input/painting/donkey_kong.png"].append((192, 112))
    image_dictpainting["input/painting/fighters.png"].append((0, 96))
    image_dictpainting["input/painting/graham.png"].append((16, 64))
    image_dictpainting["input/painting/kebab.png"].append((0, 0))
    image_dictpainting["input/painting/kebab.png"].append((0, 16))
    image_dictpainting["input/painting/match.png"].append((0, 128))
    image_dictpainting["input/painting/pigscene.png"].append((64, 192))
    image_dictpainting["input/painting/plant.png"].append((80, 0))
    image_dictpainting["input/painting/plant.png"].append((80, 16))
    image_dictpainting["input/painting/pointer.png"].append((0, 192))
    image_dictpainting["input/painting/pool.png"].append((0, 32))
    image_dictpainting["input/painting/sea.png"].append((64, 32))
    image_dictpainting["input/painting/skeleton.png"].append((192, 64))
    image_dictpainting["input/painting/skull_and_roses.png"].append((128, 128))
    image_dictpainting["input/painting/stage.png"].append((64, 128))
    image_dictpainting["input/painting/sunset.png"].append((96, 32))
    image_dictpainting["input/painting/void.png"].append((96, 128))
    image_dictpainting["input/painting/wanderer.png"].append((0, 64))
    image_dictpainting["input/painting/wasteland.png"].append((96, 0))
    image_dictpainting["input/painting/wasteland.png"].append((96, 16))
    image_dictpainting["input/painting/wither.png"].append((160, 128))

    # Chemin de l'image de sortie
    painting_output_path = "output/kz.png"

    # Copie de l'image de painting vers la sortie
    shutil.copyfile(painting_image_pathpainting, painting_output_path)

    # Multiplier les coordonnées par le facteur choisi (x16 ou x32...)
    image_dictpainting = multiply_coordinatespainting(image_dictpainting, multiplierpainting)

    # Appel de la fonction pour fusionner les images sur kz.png
    merge_imagespainting(image_dictpainting, painting_output_path, 16 * multiplierpainting, 16 * multiplierpainting, painting_output_path)


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #


# Créer l'app
TextureApp = tk.Tk()
TextureApp.title("Texture Pack Converter Java to LCE")
IconPath = os.path.abspath("assets/icon.ico")
TextureApp.iconbitmap(IconPath)
TextureApp.geometry("380x380")
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
BackgroundYoutubeDiscord.place(x=0, y=350, width=380, height=30)
BackgroundYoutubeDiscord.lift()
BorderBackgroundYoutubeDiscord = tk.Label(TextureApp, bg="#000000")
BorderBackgroundYoutubeDiscord.place(x=0, y=419, width=380, height=2)
BorderBackgroundYoutubeDiscord.lift()


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
TextConsole = ScrolledText(TextureApp, width=34, height=7)
TextConsole.place(x=42.5, y=223)
TextConsole.insert(tk.INSERT, "Version : 1.3 - Check if any      update have been made.\n")
TextConsole.insert(tk.INSERT, "----------------------------------\n")
TextConsole.configure(relief="solid", bd=2)

# ------------------------------------------

#   **--Title and Background--** 

TitleAppText = "Texture Pack Converter"
TitleAppFontSize = 25
TitleAppFont = ImageFont.truetype(FontMojangles, TitleAppFontSize)

# Image and Border
TitleAppImageWidth = 390
TitleAppImageHeight = 35
TitleAppImage = Image.new("RGBA", (TitleAppImageWidth, TitleAppImageHeight), (255, 255, 255, 0))
TitleAppDraw = ImageDraw.Draw(TitleAppImage)
TitleAppOutlineColor = (0, 0, 0)
TitleAppOutlinePosition = (31.5, 4)
TitleAppDraw.text(TitleAppOutlinePosition, TitleAppText, font=TitleAppFont, fill=TitleAppOutlineColor)

# Draw Text
TitleAppTextColor = (255, 255, 255)
TitleAppTextPosition = (29, 2)
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
