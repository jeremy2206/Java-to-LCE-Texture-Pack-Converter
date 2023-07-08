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

    # Sauvegarder l'image fusionnée en remplaçant l'image "terrain.png"
    terrain.save(output_path)
    TextConsole.insert(tk.INSERT, "terrain.png converted at          output/terrain.png\n")
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
    "input/blocks/acacia_door_bottom.png": (0, 384),
    "input/blocks/acacia_door_top.png": (0, 368),
    "input/blocks/acacia_leaves.png": (176, 320),
    "input/blocks/acacia_log.png": (128, 320),
    "input/blocks/acacia_log_top.png": (144, 320),
    "input/blocks/acacia_planks.png": (112, 192),
    "input/blocks/acacia_sapling.png": (96, 352),
    "input/blocks/acacia_trapdoor.png": (192, 528),
    "input/blocks/activator_rail.png": (208, 176),
    "input/blocks/activator_rail_on.png": (224, 176),
    "input/blocks/allium.png": (0, 352),
    "input/blocks/andesite.png": (48, 256),
    "input/blocks/anvil.png": (112, 208),
    "input/blocks/anvil_base.png": (112, 208),
    "input/blocks/anvil_top.png": (112, 224),
    "input/blocks/anvil_top_damaged_0.png": (112, 224),
    "input/blocks/anvil_top_damaged_1.png": (128, 208),
    "input/blocks/anvil_top_damaged_2.png": (128, 224),
    "input/blocks/attached_melon_stem.png": (32, 416),
    "input/blocks/attached_pumpkin_stem.png": (240, 112),
    "input/blocks/azure_bluet.png": (32, 352),
    "input/blocks/beacon.png": (144, 32),
    "input/blocks/bedrock.png": (16, 16),
    "input/blocks/beetroots_stage0.png": (0, 400),
    "input/blocks/beetroots_stage1.png": (16, 400),
    "input/blocks/beetroots_stage2.png": (32, 400),
    "input/blocks/beetroots_stage3.png": (48, 400),
    "input/blocks/beetroots_stage_0.png": (0, 400),
    "input/blocks/beetroots_stage_1.png": (16, 400),
    "input/blocks/beetroots_stage_2.png": (32, 400),
    "input/blocks/beetroots_stage_3.png": (48, 400),
    "input/blocks/birch_door_bottom.png": (16, 384),
    "input/blocks/birch_door_top.png": (16, 368),
    "input/blocks/birch_leaves.png": (176, 352),
    "input/blocks/birch_log.png": (80, 112),
    "input/blocks/birch_log_top.png": (240, 256),
    "input/blocks/birch_planks.png": (96, 208),
    "input/blocks/birch_sapling.png": (240, 64),
    "input/blocks/birch_trapdoor.png": (208, 528),
    "input/blocks/black_concrete.png": (0, 432),
    "input/blocks/black_concrete_powder.png": (0, 432),
    "input/blocks/black_glazed_terracotta.png": (0, 464),
    "input/blocks/black_stained_glass.png": (0, 288),
    "input/blocks/black_stained_glass_pane_top.png": (0, 304),
    "input/blocks/black_terracotta.png": (0, 272),
    "input/blocks/black_wool.png": (16, 112),
    "input/blocks/blue_concrete.png": (16, 432),
    "input/blocks/blue_concrete_powder.png": (16, 448),
    "input/blocks/blue_glazed_terracotta.png": (16, 464),
    "input/blocks/blue_ice.png": (240, 480),
    "input/blocks/blue_orchid.png": (16, 352),
    "input/blocks/blue_stained_glass.png": (16, 288),
    "input/blocks/blue_stained_glass_pane_top.png": (96, 288),
    "input/blocks/blue_terracotta.png": (16, 272),
    "input/blocks/blue_wool.png": (16, 176),
    "input/blocks/bone_block_side.png": (0, 416),
    "input/blocks/bone_block_top.png": (16, 416),
    "input/blocks/bookshelf.png": (48, 32),
    "input/blocks/brain_coral.png": (176, 480),
    "input/blocks/brain_coral_block.png": (96, 480),
    "input/blocks/brain_coral_fan.png": (176, 496),
    "input/blocks/brewing_stand.png": (208, 144),
    "input/blocks/brewing_stand_base.png": (192, 144),
    "input/blocks/brick.png": (112, 0),
    "input/blocks/brown_concrete.png": (32, 432),
    "input/blocks/brown_concerte_powder.png": (32, 448),
    "input/blocks/brown_glazed_terracotta.png": (32, 464),
    "input/blocks/brown_mushroom.png": (208, 16),
    "input/blocks/brown_mushroom_block.png": (224, 112),
    "input/blocks/brown_stained_glass.png": (32, 288),
    "input/blocks/brown_stained_glass_pane_top.png": (32, 304),
    "input/blocks/brown_terracotta.png": (32, 272),
    "input/blocks/brown_wool.png": (16, 160),
    "input/blocks/bubble_coral.png": (160, 480),
    "input/blocks/bubble_coral_block.png": (80, 480),
    "input/blocks/bubble_coral_fan.png": (160, 496),
    "input/blocks/cactus_bottom.png": (112, 64),
    "input/blocks/cactus_side.png": (96, 64),
    "input/blocks/cactus_top.png": (80, 64),
    "input/blocks/cake_bottom.png": (192, 112),
    "input/blocks/cake_inner.png": (176, 112),
    "input/blocks/cake_side.png": (160, 112),
    "input/blocks/cake_top.png": (144, 112),
    "input/blocks/carrots_stage0.png": (128, 192),
    "input/blocks/carrots_stage1.png": (144, 192),
    "input/blocks/carrots_stage2.png": (160, 192),
    "input/blocks/carrots_stage3.png": (176, 192),
    "input/blocks/carrots_stage_0.png": (128, 192),
    "input/blocks/carrots_stage_1.png": (144, 192),
    "input/blocks/carrots_stage_2.png": (160, 192),
    "input/blocks/carrots_stage_3.png": (176, 192),
    "input/blocks/carved_pumpkin.png": (112, 112),
    "input/blocks/cauldron_bottom.png": (176, 144),
    "input/blocks/cauldron_inner.png": (176, 128),
    "input/blocks/cauldron_side.png": (160, 144),
    "input/blocks/cauldron_top.png": (160, 128),
    "input/blocks/chain_command_block_back.png": (64, 400),
    "input/blocks/chain_command_block_conditional.png": (80, 400),
    "input/blocks/chain_command_block_front.png": (96, 400),
    "input/blocks/chain_command_block_side.png": (112, 400),
    "input/blocks/chipped_anvil_top.png": (128, 208),
    "input/blocks/chiseled_quartz_block.png": (144, 224),
    "input/blocks/chiseled_quartz_block_top.png": (144, 208),
    "input/blocks/chiseled_red_sandstone.png": (224, 352),
    "input/blocks/chiseled_sandstone.png": (224, 352),
    "input/blocks/chiseled_stone_bricks.png": (80, 208),
    "input/blocks/chorus_flower.png": (80, 368),
    "input/blocks/chorus_flower_dead.png": (96, 368),
    "input/blocks/chorus_flower_plant.png": (112, 368),
    "input/blocks/clay.png": (128, 64),
    "input/blocks/coal_block.png": (0, 256),
    "input/blocks/coal_ore.png": (32, 32),
    "input/blocks/coarse_dirt.png": (128, 352),
    "input/blocks/cobblestone.png": (0, 16),
    "input/blocks/cobweb.png": (176, 0),
    "input/blocks/cobblestone_mossy.png": (64, 32),
    "input/blocks/cocoa_stage0.png": (160, 160),
    "input/blocks/cocoa_stage1.png": (144, 160),
    "input/blocks/cocoa_stage2.png": (128, 160),
    "input/blocks/cocoa_stage_0.png": (160, 160),
    "input/blocks/cocoa_stage_1.png": (144, 160),
    "input/blocks/cocoa_stage_2.png": (128, 160),
    "input/blocks/command_block_back.png": (128, 400),
    "input/blocks/command_block_conditional.png": (144, 400),
    "input/blocks/command_block_front.png": (160, 400),
    "input/blocks/command_block_side.png": (176, 400),
    "input/blocks/comparator.png": (176, 176),
    "input/blocks/comparator_off.png": (176, 176),
    "input/blocks/comparator_on.png": (192, 176),
    "input/blocks/cracked_stonebricks.png": (80, 96),
    "input/blocks/crafting_table_front.png": (192, 48),
    "input/blocks/crafting_table_side.png": (176, 48),
    "input/blocks/crafting_table_top.png": (176, 32),
    "input/blocks/cut_red_sandstone.png": (240, 352),
    "input/blocks/cut_sandstone.png": (96, 224),
    "input/blocks/cyan_concrete.png": (48, 432),
    "input/blocks/cyan_concrete_powder.png": (48, 448),
    "input/blocks/cyan_glazed_terracotta.png": (48, 464),
    "input/blocks/cyan_stained_glass.png": (48, 288),
    "input/blocks/cyan_stained_glass_pane_top.png": (48, 304),
    "input/blocks/cyan_terracotta.png": (48, 272),
    "input/blocks/cyan_wool.png": (16, 208),
    "input/blocks/damaged_anvil_top.png": (128, 224),
    "input/blocks/dandelion.png": (208, 0),
    "input/blocks/dark_oak_door_bottom.png": (32, 384),
    "input/blocks/dark_oak_door_top.png": (32, 368),
    "input/blocks/dark_oak_log.png": (128, 336),
    "input/blocks/dark_oak_log_top.png": (144, 336),
    "input/blocks/dark_oak_leaves.png": (176, 336),
    "input/blocks/dark_oak_planks.png": (160, 336),
    "input/blocks/dark_oak_sapling.png": (112, 352),
    "input/blocks/dark_oak_trapdoor.png": (224, 528),
    "input/blocks/dark_prismarine.png": (208, 339),
    "input/blocks/daylight_detector_inverted_top.png": (224, 368),
    "input/blocks/daylight_detector_side.png": (160, 48),
    "input/blocks/daylight_detector_top.png": (144, 48),
    "input/blocks/deadbush.png": (112, 48),
    "input/blocks/dead_brain_coral_block.png": (96, 496),
    "input/blocks/dead_brain_coral_fan.png": (176, 512),
    "input/blocks/dead_bubble_coral_block.png": (80, 496),
    "input/blocks/dead_bubble_coral_fan.png": (160, 512),
    "input/blocks/dead_bush.png": (112, 48),
    "input/blocks/dead_fire_coral_block.png": (112, 496),
    "input/blocks/dead_fire_coral_fan.png": (192, 512),
    "input/blocks/dead_horn_coral_block.png": (128, 496),
    "input/blocks/dead_horn_coral_fan.png": (208, 512),
    "input/blocks/dead_tube_coral_block.png": (64, 496),
    "input/blocks/dead_tube_coral_fan.png": (144, 512),
    "input/blocks/destroy_stage_0.png": (0, 240),
    "input/blocks/destroy_stage_1.png": (16, 240),
    "input/blocks/destroy_stage_2.png": (32, 240),
    "input/blocks/destroy_stage_3.png": (48, 240),
    "input/blocks/destroy_stage_4.png": (64, 240),
    "input/blocks/destroy_stage_5.png": (80, 240),
    "input/blocks/destroy_stage_6.png": (96, 240),
    "input/blocks/destroy_stage_7.png": (112, 240),
    "input/blocks/destroy_stage_8.png": (128, 240),
    "input/blocks/destroy_stage_9.png": (144, 240),
    "input/blocks/detector_rail.png": (48, 192),
    "input/blocks/detector_rail_on.png": (208, 208),
    "input/blocks/diamond_block.png": (128, 16),
    "input/blocks/diamond_ore.png": (32, 48),
    "input/blocks/diorite.png": (80, 256),
    "input/blocks/dirt.png": (32, 0),
    "input/blocks/dirt_podzol_side.png": (144, 352),
    "input/blocks/dirt_podzol_top.png": (160, 352),
    "input/blocks/dispenser_front_horizontal.png": (224, 32),
    "input/blocks/dispenser_front_vertical.png": (128, 32),
    "input/blocks/door_acacia_lower.png": (0, 384),
    "input/blocks/door_acacia_upper.png": (0, 368),
    "input/blocks/door_birch_lower.png": (16, 384),
    "input/blocks/door_birch_upper.png": (16, 368),
    "input/blocks/door_dark_oak_lower.png": (32, 384),
    "input/blocks/door_dark_oak_upper.png": (32, 368),
    "input/blocks/door_iron_lower.png": (32, 96),
    "input/blocks/door_iron_upper.png": (32, 80),
    "input/blocks/door_jungle_lower.png": (48, 384),
    "input/blocks/door_jungle_upper.png": (48, 368),
    "input/blocks/door_spruce_lower.png": (64, 384),
    "input/blocks/door_spruce_upper.png": (64, 368),
    "input/blocks/door_wood_lower.png": (16, 96),
    "input/blocks/door_wood_upper.png": (16, 80),
    "input/blocks/double_plant_fern_bottom.png": (0, 336),
    "input/blocks/double_plant_fern_top.png": (0, 320),
    "input/blocks/double_plant_grass_bottom.png": (16, 336),
    "input/blocks/double_plant_grass_top.png": (16, 320),
    "input/blocks/double_plant_paeonia_bottom.png": (32, 336),
    "input/blocks/double_plant_paeonia_top.png": (32, 320),
    "input/blocks/double_plant_rose_bottom.png": (48, 336),
    "input/blocks/double_plant_rose_top.png": (48, 320),
    "input/blocks/double_plant_sunflower_back.png": (112, 336),
    "input/blocks/double_plant_sunflower_bottom.png": (96, 336),
    "input/blocks/double_plant_sunflower_front.png": (112, 320),
    "input/blocks/double_plant_sunflower_top.png": (96, 320),
    "input/blocks/double_plant_syringa_bottom.png": (64, 336),
    "input/blocks/double_plant_syringa_top.png": (64, 320),
    "input/blocks/dragon_egg.png": (112, 160),
    "input/blocks/dried_kelp_side.png": (16, 496),
    "input/blocks/dried_kelp_top.png": (0, 496),
    "input/blocks/dropper_front_horizontal.png": (176, 16),
    "input/blocks/dropper_front_vertical.png": (160, 32),
    "input/blocks/emerald_block.png": (144, 16),
    "input/blocks/emerald_ore.png": (176, 160),
    "input/blocks/enchanting_table_bottom.png": (112, 176),
    "input/blocks/enchanting_table_side.png": (96, 176),
    "input/blocks/enchanting_table_top.png": (96, 160),
    "input/blocks/end_bricks.png": (128, 368),
    "input/blocks/end_portal_frame_eye.png": (224, 160),
    "input/blocks/end_portal_frame_side.png": (240, 144),
    "input/blocks/end_portal_frame_top.png": (224, 144),
    "input/blocks/end_rod.png": (128, 384),
    "input/blocks/end_stone.png": (240, 160),
    "input/blocks/end_stone_bricks.png": (128, 368),
    "input/blocks/endframe_eye.png": (224, 160),
    "input/blocks/endframe_side.png": (240, 144),
    "input/blocks/endframe_top.png": (224, 144),
    "input/blocks/farmland.png": (112, 80),
    "input/blocks/farmland_dry.png": (112, 80),
    "input/blocks/farmland_moist.png": (96, 80),
    "input/blocks/farmland_wet.png": (96, 80),
    "input/blocks/fern.png": (128, 48),
    "input/blocks/fire_coral.png": (192, 480),
    "input/blocks/fire_coral_block.png": (112, 480),
    "input/blocks/fire_coral_fan.png": (96, 80),
    "input/blocks/flower_allium.png": (0, 352),
    "input/blocks/flower_blue_orchid.png": (16, 352),
    "input/blocks/flower_dandelion.png": (208, 0),
    "input/blocks/flower_houstonia.png": (32, 352),
    "input/blocks/flower_oxeye_daisy.png": (48, 352),
    "input/blocks/flower_pot.png": (160, 176),
    "input/blocks/flower_rose.png": (192, 0),
    "input/blocks/flower_tulip_orange.png": (80, 320),
    "input/blocks/flower_tulip_pink.png": (80, 336),
    "input/blocks/flower_tulip_red.png": (64, 352),
    "input/blocks/flower_tulip_white.png": (80, 352),
    "input/blocks/frosted_ice_0.png": (192, 384),
    "input/blocks/frosted_ice_1.png": (208, 384),
    "input/blocks/frosted_ice_2.png": (224, 384),
    "input/blocks/frosted_ice_3.png": (240, 384),
    "input/blocks/furnace_front.png": (192, 32),
    "input/blocks/furnace_front_off.png": (192, 32),
    "input/blocks/furnace_front_on.png": (208, 48),
    "input/blocks/furnace_side.png": (208, 32),
    "input/blocks/furnace_top.png": (224, 48),
    "input/blocks/glass.png": (16, 48),
    "input/blocks/glass_black.png": (0, 288),
    "input/blocks/glass_blue.png": (16, 288),
    "input/blocks/glass_brown.png": (32, 288),
    "input/blocks/glass_cyan.png": (48, 288),
    "input/blocks/glass_gray.png": (64, 288),
    "input/blocks/glass_green.png": (80, 288),
    "input/blocks/glass_light_blue.png": (96, 288),
    "input/blocks/glass_lime.png": (112, 288),
    "input/blocks/glass_magenta.png": (128, 288),
    "input/blocks/glass_orange.png": (144, 288),
    "input/blocks/glass_pane_top.png": (64, 144),
    "input/blocks/glass_pane_top_black.png": (0, 304),
    "input/blocks/glass_pane_top_blue.png": (16, 304),
    "input/blocks/glass_pane_top_brown.png": (32, 304),
    "input/blocks/glass_pane_top_cyan.png": (48, 304),
    "input/blocks/glass_pane_top_gray.png": (64, 304),
    "input/blocks/glass_pane_top_green.png": (80, 304),
    "input/blocks/glass_pane_top_light_blue.png": (96, 304),
    "input/blocks/glass_pane_top_lime.png": (112, 304),
    "input/blocks/glass_pane_top_magenta.png": (128, 304),
    "input/blocks/glass_pane_top_orange.png": (144, 304),
    "input/blocks/glass_pane_top_pink.png": (160, 304),
    "input/blocks/glass_pane_top_purple.png": (176, 304),
    "input/blocks/glass_pane_top_red.png": (192, 304),
    "input/blocks/glass_pane_top_silver.png": (208, 304),
    "input/blocks/glass_pane_top_white.png": (224, 304),
    "input/blocks/glass_pane_top_yellow.png": (240, 304),
    "input/blocks/glass_pink.png": (160, 288),
    "input/blocks/glass_purple.png": (176, 288),
    "input/blocks/glass_red.png": (192, 288),
    "input/blocks/glass_silver.png": (208, 288),
    "input/blocks/glass_white.png": (224, 288),
    "input/blocks/glass_yellow.png": (240, 288),
    "input/blocks/glowstone.png": (144, 96),
    "input/blocks/gold_block.png": (112, 16),
    "input/blocks/gold_ore.png": (0, 32),
    "input/blocks/granite.png": (112, 256),
    "input/blocks/grass.png": (112, 32),
    "input/blocks/grass_block_side.png": (48, 0),
    "input/blocks/grass_block_side_overlay.png": (96, 32),
    "input/blocks/grass_blocks_snow.png": (64, 64),
    "input/blocks/grass_blocks_top.png": (0, 0),
    "input/blocks/grass_path_side.png": (144, 368),
    "input/blocks/grass_path_top.png": (160, 368),
    "input/blocks/grass_side.png": (48, 0),
    "input/blocks/grass_side_overlay.png": (96, 32),
    "input/blocks/grass_side_snowed.png": (64, 64),
    "input/blocks/grass_top.png": (0, 0),
    "input/blocks/gravel.png": (48, 16),
    "input/blocks/gray_concrete.png": (64, 432),
    "input/blocks/gray_concrete_powder.png": (64, 448),
    "input/blocks/gray_glazed_terracotta.png": (64, 464),
    "input/blocks/gray_stained_glass.png": (64, 288),
    "input/blocks/gray_stained_glass_pane_top.png": (64, 304),
    "input/blocks/gray_terracotta.png": (64, 272),
    "input/blocks/gray_wool.png": (32, 112),
    "input/blocks/green_concrete.png": (80, 432),
    "input/blocks/green_concrete_powder.png": (80, 448),
    "input/blocks/green_glazed_terracotta.png": (80, 464),
    "input/blocks/green_stained_glass.png": (80, 288),
    "input/blocks/green_stained_glass_pane_top.png": (80, 304),
    "input/blocks/green_terracotta.png": (80, 272),
    "input/blocks/green_wool.png": (16, 144),
    "input/blocks/hardened_clay.png": (16, 256),
    "input/blocks/hardened_clay_stained_black.png": (0, 272),
    "input/blocks/hardened_clay_stained_blue.png": (16, 272),
    "input/blocks/hardened_clay_stained_brown.png": (32, 272),
    "input/blocks/hardened_clay_stained_cyan.png": (48, 272),
    "input/blocks/hardened_clay_stained_gray.png": (64, 272),
    "input/blocks/hardened_clay_stained_green.png": (80, 272),
    "input/blocks/hardened_clay_stained_light_blue.png": (96, 272),
    "input/blocks/hardened_clay_stained_lime.png": (112, 272),
    "input/blocks/hardened_clay_stained_magenta.png": (128, 272),
    "input/blocks/hardened_clay_stained_orange.png": (144, 272),
    "input/blocks/hardened_clay_stained_pink.png": (160, 272),
    "input/blocks/hardened_clay_stained_purple.png": (176, 272),
    "input/blocks/hardened_clay_stained_red.png": (192, 272),
    "input/blocks/hardened_clay_stained_silver.png": (208, 272),
    "input/blocks/hardened_clay_stained_white.png": (224, 272),
    "input/blocks/hardened_clay_stained_yellow.png": (240, 272),
    "input/blocks/hay_block_side.png": (160, 240),
    "input/blocks/hay_block_top.png": (208, 240),
    "input/blocks/hopper_inside.png": (192, 224),
    "input/blocks/hopper_outside.png": (192, 208),
    "input/blocks/hopper_top.png": (192, 240),
    "input/blocks/horn_coral.png": (208, 480),
    "input/blocks/horn_coral_block.png": (128, 480),
    "input/blocks/horn_coral_fan.png": (208, 496),
    "input/blocks/ice.png": (48, 64),
    "input/blocks/ice_packed.png": (192, 368),
    "input/blocks/iron_bars.png": (80, 80),
    "input/blocks/iron_block.png": (96, 16),
    "input/blocks/iron_door_bottom.png": (32, 96),
    "input/blocks/iron_door_top.png": (32, 80),
    "input/blocks/iron_ore.png": (16, 32),
    "input/blocks/iron_trapdoor.png": (240, 368),
    "input/blocks/itemframe.png": (144, 176),
    "input/blocks/itemframe_background.png": (144, 176),
    "input/blocks/jack_o_lantern.png": (128, 112),
    "input/blocks/jukebox_side.png": (160, 64),
    "input/blocks/jukebox_top.png": (176, 64),
    "input/blocks/jungle_door_bottom.png": (48, 384),
    "input/blocks/jungle_door_top.png": (48, 368),
    "input/blocks/jungle_leaves.png": (64, 192),
    "input/blocks/jungle_log.png": (144, 144),
    "input/blocks/jungle_log_top.png": (224, 256),
    "input/blocks/jungle_planks.png": (112, 192),
    "input/blocks/jungle_sapling.png": (224, 16),
    "input/blocks/jungle_trapdoor.png": (240, 528),
    "input/blocks/kelp.png": (64, 512),
    "input/blocks/kelp.png": (80, 512),
    "input/blocks/kelp.png": (96, 512),
    "input/blocks/kelp.png": (112, 512),
    "input/blocks/kelp_plant.png": (0, 512),
    "input/blocks/kelp_plant.png": (16, 512),
    "input/blocks/kelp_plant.png": (32, 512),
    "input/blocks/kelp_plant.png": (48, 512),
    "input/blocks/ladder.png": (48, 80),
    "input/blocks/lapis_block.png": (0, 144),
    "input/blocks/lapis_ore.png": (0, 160),
    "input/blocks/large_fern_bottom.png": (0, 336),
    "input/blocks/large_fern_top.png": (0, 320),
    "input/blocks/leaves_acacia.png": (176, 320),
    "input/blocks/leaves_big_oak.png": (176, 336),
    "input/blocks/leaves_birch.png": (0, 160),
    "input/blocks/leaves_jungle.png": (64, 192),
    "input/blocks/leaves_oak.png": (64, 48),
    "input/blocks/leaves_spruce.png": (64, 128),
    "input/blocks/lever.png": (0, 96),
    "input/blocks/light_blue_concrete.png": (96, 432),
    "input/blocks/light_blue_concrete_powder.png": (96, 448),
    "input/blocks/light_blue_glazed_terracotta.png": (96, 464),
    "input/blocks/light_blue_stained_glass.png": (96, 288),
    "input/blocks/light_blue_stained_glass_pane_top.png": (96, 304),
    "input/blocks/light_blue_terracotta.png": (96, 272),
    "input/blocks/light_blue_wool.png": (32, 176),
    "input/blocks/light_gray_concrete.png": (208, 432),
    "input/blocks/light_gray_concrete_powder.png": (208, 448),
    "input/blocks/light_gray_glazed_terracotta.png": (208, 464),
    "input/blocks/light_gray_stained_glass.png": (208, 288),
    "input/blocks/light_gray_stained_glass_pane_top.png": (208, 304),
    "input/blocks/light_gray_terracotta.png": (208, 272),
    "input/blocks/light_gray_wool.png": (16, 224),
    "input/blocks/lilac_bottom.png": (64, 336),
    "input/blocks/lilac_top.png": (64, 320),
    "input/blocks/lily_pad.png": (192, 64),
    "input/blocks/lime_concrete.png": (112, 432),
    "input/blocks/lime_concrete_powder.png": (112, 448),
    "input/blocks/lime_glazed_terracotta.png": (112, 464),
    "input/blocks/lime_stained_glass.png": (112, 288),
    "input/blocks/lime_stained_glass_pane_top.png": (112, 304),
    "input/blocks/lime_terracotta.png": (112, 272),
    "input/blocks/lime_wool.png": (32, 144),
    "input/blocks/log_acacia.png": (128, 320),
    "input/blocks/log_acacia_top.png": (144, 320),
    "input/blocks/log_big_oak.png": (128, 336),
    "input/blocks/log_big_oak_top.png": (144, 336),
    "input/blocks/log_birch.png": (80, 112),
    "input/blocks/log_birch_top.png": (240, 256),
    "input/blocks/log_jungle.png": (144, 144),
    "input/blocks/log_jungle_top.png": (224, 256),
    "input/blocks/log_oak.png": (64, 16),
    "input/blocks/log_oak_top.png": (80, 16),
    "input/blocks/log_spruce.png": (64, 112),
    "input/blocks/log_spruce_top.png": (208, 256),
    "input/blocks/magenta_concrete.png": (128, 432),
    "input/blocks/magenta_concrete_powder.png": (128, 448),
    "input/blocks/magenta_glazed_terracotta.png": (128, 464),
    "input/blocks/magenta_stained_glass.png": (128, 288),
    "input/blocks/magenta_stained_glass_pane_top.png": (128, 304),
    "input/blocks/magenta_terracotta.png": (128, 272),
    "input/blocks/magenta_wool.png": (32, 192),
    "input/blocks/magma.png": (144, 384),
    "input/blocks/melon_side.png": (128, 128),
    "input/blocks/melon_stem.png": (48, 416),
    "input/blocks/melon_stem_connected.png": (32, 416),
    "input/blocks/melon_stem_disconnected.png": (48, 416),
    "input/blocks/melon_top.png": (144, 128),
    "input/blocks/mob_spawner.png": (16, 64),
    "input/blocks/mossy_cobblestone.png": (64, 32),
    "input/blocks/mossy_stone_bricks.png": (64, 96),
    "input/blocks/mushroom_block_inside.png": (224, 128),
    "input/blocks/mushroom_block_skin_brown.png": (224, 112),
    "input/blocks/mushroom_block_skin_inside.png": (208, 112),
    "input/blocks/mushroom_block_skin_stem.png": (208, 128),
    "input/blocks/mushroom_brown.png": (208, 16),
    "input/blocks/mushroom_red.png": (192, 16),
    "input/blocks/mushroom_stem.png": (208, 128),
    "input/blocks/mycelium_side.png": (208, 64),
    "input/blocks/mycelium_top.png": (224, 64),
    "input/blocks/netherrack.png": (112, 96),
    "input/blocks/nether_brick.png": (0, 224),
    "input/blocks/nether_bricks.png": (0, 224),
    "input/blocks/nether_quartz_ore.png": (240, 176),
    "input/blocks/nether_wart_block.png": (160, 384),
    "input/blocks/nether_wart_stage0.png": (32, 224),
    "input/blocks/nether_wart_stage1.png": (48, 224),
    "input/blocks/nether_wart_stage2.png": (64, 224),
    "input/blocks/nether_wart_stage_0.png": (32, 224),
    "input/blocks/nether_wart_stage_1.png": (48, 224),
    "input/blocks/nether_wart_stage_2.png": (64, 224),
    "input/blocks/note_block.png": (32, 256),
    "input/blocks/noteblock.png": (32, 256),
    "input/blocks/oak_door_bottom.png": (16, 96),
    "input/blocks/oak_door_top.png": (16, 80),
    "input/blocks/oak_leave.png": (64, 48),
    "input/blocks/oak_log.png": (64, 16),
    "input/blocks/oak_log_top.png": (80, 16),
    "input/blocks/oak_planks.png": (64, 0),
    "input/blocks/oak_sapling.png": (240, 0),
    "input/blocks/oak_trapdoor.png": (64, 80),
    "input/blocks/observer_back.png": (96, 416),
    "input/blocks/observer_back_off.png": (112, 416),
    "input/blocks/observer_front.png": (64, 416),
    "input/blocks/observer_side.png": (80, 416),
    "input/blocks/observer_top.png": (128, 416),
    "input/blocks/obsidian.png": (80, 32),
    "input/blocks/orange_concrete.png": (144, 432),
    "input/blocks/orange_concrete_powder.png": (144, 448),
    "input/blocks/orange_glazed_terracotta.png": (144, 464),
    "input/blocks/orange_stained_glass.png": (144, 288),
    "input/blocks/orange_stained_glass_pane_top.png": (144, 304),
    "input/blocks/orange_terracotta.png": (144, 272),
    "input/blocks/orange_tulip.png": (80, 320),
    "input/blocks/orange_wool.png": (32, 208),
    "input/blocks/oxeye_daisy.png": (48, 352),
    "input/blocks/packed_ice.png": (192, 368),
    "input/blocks/peony_bottom.png": (32, 336),
    "input/blocks/peony_top.png": (32, 320),
    "input/blocks/pink_concrete.png": (160, 432),
    "input/blocks/pink_concrete_powder.png": (160, 448),
    "input/blocks/pink_glazed_terracotta.png": (160, 464),
    "input/blocks/pink_stained_glass.png": (160, 288),
    "input/blocks/pink_stained_glass_pane_top.png": (160, 304),
    "input/blocks/pink_terracotta.png": (160, 272),
    "input/blocks/pink_tulip.png": (80, 336),
    "input/blocks/pink_wool.png": (32, 128),
    "input/blocks/piston_bottom.png": (208, 96),
    "input/blocks/piston_inner.png": (224, 96),
    "input/blocks/piston_side.png": (192, 96),
    "input/blocks/piston_top.png": (176, 96),
    "input/blocks/piston_top_normal.png": (176, 96),
    "input/blocks/piston_top_sticky.png": (160, 96),
    "input/blocks/planks_acacia.png": (112, 192),
    "input/blocks/planks_big_oak.png": (160, 336),
    "input/blocks/planks_birch.png": (96, 208),
    "input/blocks/planks_jungle.png": (112, 192),
    "input/blocks/planks_oak.png": (64, 0),
    "input/blocks/planks_spruce.png": (96, 192),
    "input/blocks/podzol_side.png": (144, 352),
    "input/blocks/podzol_top.png": (160, 352),
    "input/blocks/polished_andesite.png": (64, 256),
    "input/blocks/polished_diorite.png": (96, 256),
    "input/blocks/polished_granite.png": (128, 256),
    "input/blocks/poppy.png": (192, 0),
    "input/blocks/potato_stage0.png": (144, 256),
    "input/blocks/potato_stage1.png": (160, 256),
    "input/blocks/potato_stage2.png": (176, 256),
    "input/blocks/potato_stage3.png": (192, 256),
    "input/blocks/potato_stage_0.png": (144, 256),
    "input/blocks/potato_stage_1.png": (160, 256),
    "input/blocks/potato_stage_2.png": (176, 256),
    "input/blocks/potato_stage_3.png": (192, 256),
    "input/blocks/powered_rail.png": (48, 160),
    "input/blocks/powered_rail_on.png": (48, 176),
    "input/blocks/prismarine.png": (208, 352),
    "input/blocks/prismarine_bricks.png": (208, 320),
    "input/blocks/prismarine_dark.png": (208, 336),
    "input/blocks/prismarine_rough.png": (208, 352),
    "input/blocks/pumpkin_face_off.png": (112, 112),
    "input/blocks/pumpkin_face_on.png": (128, 112),
    "input/blocks/pumpkin_side.png": (96, 112),
    "input/blocks/pumpkin_stem.png": (240, 96),
    "input/blocks/pumpkin_stem_connected.png": (240, 112),
    "input/blocks/pumpkin_stem_disconnected.png": (240, 96),
    "input/blocks/pumpkin_top.png": (96, 96),
    "input/blocks/purple_concrete.png": (176, 432),
    "input/blocks/purple_concrete_powder.png": (176, 448),
    "input/blocks/purple_glazed_terracotta.png": (176, 464),
    "input/blocks/purple_stained_glass.png": (176, 288),
    "input/blocks/purple_stained_glass_pane_top.png": (176, 304),
    "input/blocks/purple_terracotta.png": (176, 272),
    "input/blocks/purple_wool.png": (16, 192),
    "input/blocks/purpur_block.png": (80, 384),
    "input/blocks/purpur_pillar.png": (96, 384),
    "input/blocks/purpur_pillar_top.png": (112, 384),
    "input/blocks/quartz_block_bottom.png": (176, 240),
    "input/blocks/quartz_block_chiseled.png": (144, 224),
    "input/blocks/quartz_block_chiseled_top.png": (144, 208),
    "input/blocks/quartz_block_lines.png": (160, 224),
    "input/blocks/quartz_block_lines_top.png": (160, 208),
    "input/blocks/quartz_block_side.png": (176, 224),
    "input/blocks/quartz_block_top.png": (176, 208),
    "input/blocks/quartz_ore.png": (240, 176),
    "input/blocks/quartz_pillar.png": (160, 224),
    "input/blocks/quartz_pillar_top.png": (160, 208),
    "input/blocks/rail.png": (0, 128),
    "input/blocks/rail_corner.png": (0, 112),
    "input/blocks/rail_activator.png": (208, 176),
    "input/blocks/rail_activator_powered.png": (224, 176),
    "input/blocks/rail_detector.png": (48, 192),
    "input/blocks/rail_detector_powered.png": (208, 208),
    "input/blocks/rail_golden.png": (48, 160),
    "input/blocks/rail_golden_powered.png": (48, 176),
    "input/blocks/rail_normal.png": (0, 128),
    "input/blocks/rail_normal_turned.png": (0, 112),
    "input/blocks/red_concrete.png": (192, 432),
    "input/blocks/red_concrete_powder.png": (192, 448),
    "input/blocks/red_glazed_terracotta.png": (192, 464),
    "input/blocks/red_mushroom.png": (192, 16),
    "input/blocks/red_mushroom_block.png": (208, 112),
    "input/blocks/red_sand.png": (224, 320),
    "input/blocks/red_sandstone.png": (240, 336),
    "input/blocks/red_sandstone_bottom.png": (224, 336),
    "input/blocks/red_sandstone_carved.png": (224, 352),
    "input/blocks/red_sandstone_normal.png": (240, 336),
    "input/blocks/red_sandstone_smooth.png": (240, 352),
    "input/blocks/red_sandstone_top.png": (240, 320),
    "input/blocks/red_nether_bricks.png": (176, 384),
    "input/blocks/red_stained_glass.png": (192, 288),
    "input/blocks/red_stained_glass_pane_top.png": (192, 304),
    "input/blocks/red_terracotta.png": (192, 272),
    "input/blocks/red_tulip.png": (64, 352),
    "input/blocks/red_wool.png": (16, 128),
    "input/blocks/redstone_block.png": (160, 16),
    "input/blocks/redstone_lamp.png": (48, 208),
    "input/blocks/redstone_lamp_off.png": (48, 208),
    "input/blocks/redstone_lamp_on.png": (64, 208),
    "input/blocks/redstone_ore.png": (48, 48),
    "input/blocks/redstone_torch.png": (48, 96),
    "input/blocks/redstone_torch_off.png": (48, 112),
    "input/blocks/redstone_torch_on.png": (48, 96),
    "input/blocks/reeds.png": (144, 64),
    "input/blocks/repeater.png": (48, 128),
    "input/blocks/repeater_off.png": (48, 128),
    "input/blocks/repeater_on.png": (48, 144),
    "input/blocks/repeating_command_block_back.png": (192, 400),
    "input/blocks/repeating_command_block_conditional.png": (208, 400),
    "input/blocks/repeating_command_block_front.png": (224, 400),
    "input/blocks/repeating_command_block_side.png": (240, 400),
    "input/blocks/rose_bush_bottom.png": (48, 336),
    "input/blocks/rose_bush_top.png": (48, 320),
    "input/blocks/sand.png": (32, 16),
    "input/blocks/sandstone.png": (0, 192),
    "input/blocks/sandstone_bottom.png": (0, 208),
    "input/blocks/sandstone_carved.png": (80, 224),
    "input/blocks/sandstone_normal.png": (0, 192),
    "input/blocks/sandstone_smooth.png": (96, 224),
    "input/blocks/sandstone_top.png": (0, 176),
    "input/blocks/sapling_acacia.png": (96, 352),
    "input/blocks/sapling_birch.png": (240, 64),
    "input/blocks/sapling_jungle.png": (224, 16),
    "input/blocks/sapling_oak.png": (240, 0),
    "input/blocks/sapling_roofed_oak.png": (112, 352),
    "input/blocks/sapling_spruce.png": (240, 48),
    "input/blocks/sea_lantern.png": (208, 368),
    "input/blocks/sea_pickle.png": (224, 480),
    "input/blocks/seagrass.png": (32, 496),
    "input/blocks/seagrass.png": (128, 512),
    "input/blocks/slime_block.png": (192, 192),
    "input/blocks/snow.png": (32, 64),
    "input/blocks/soul_sand.png": (128, 96),
    "input/blocks/spawner.png": (16, 64),
    "input/blocks/sponge.png": (0, 48),
    "input/blocks/sponge_wet.png": (192, 128),
    "input/blocks/spruce_door_bottom.png": (64, 384),
    "input/blocks/spruce_door_top.png": (64, 368),
    "input/blocks/spruce_leaves.png": (64, 128),
    "input/blocks/spruce_log.png": (64, 112),
    "input/blocks/spruce_log_top.png": (208, 256),
    "input/blocks/spruce_planks.png": (96, 192),
    "input/blocks/spruce_sapling.png": (240, 48),
    "input/blocks/spruce_trapdoor.png": (240, 512),
    "input/blocks/stone.png": (16, 0),
    "input/blocks/stone_andesite.png": (48, 256),
    "input/blocks/stone_andesite_smooth.png": (64, 256),
    "input/blocks/stone_brick.png": (96, 48),
    "input/blocks/stone_diorite.png": (80, 256),
    "input/blocks/stone_diorite_smooth.png": (96, 256),
    "input/blocks/stone_granite.png": (112, 256),
    "input/blocks/stone_granite_smooth.png": (128, 256),
    "input/blocks/stone_slab_side.png": (80, 0),
    "input/blocks/stone_slab_top.png": (96, 0),
    "input/blocks/stonebrick.png": (96, 48),
    "input/blocks/stonebrick_carved.png": (80, 208),
    "input/blocks/stonebrick_cracked.png": (80, 96),
    "input/blocks/stonebrick_mossy.png": (64, 96),
    "input/blocks/stripped_acacia_log.png": (32, 528),
    "input/blocks/stripped_acacia_log_top.png": (48, 528),
    "input/blocks/stripped_birch_log.png": (64, 528),
    "input/blocks/stripped_birch_log_top.png": (80, 528),
    "input/blocks/stripped_dark_oak_log.png": (96, 528),
    "input/blocks/stripped_dark_oak_log_top.png": (112, 528),
    "input/blocks/stripped_jungle_log.png": (128, 528),
    "input/blocks/stripped_jungle_log_top.png": (144, 528),
    "input/blocks/stripped_oak_log.png": (0, 528),
    "input/blocks/stripped_oak_log_top.png": (16, 528),
    "input/blocks/stripped_spruce_log.png": (160, 528),
    "input/blocks/stripped_spruce_log_top.png": (176, 528),
    "input/blocks/structure_block.png": (176, 416),
    "input/blocks/structure_block_corner.png": (192, 416),
    "input/blocks/structure_block_data.png": (208, 416),
    "input/blocks/structure_block_load.png": (224, 416),
    "input/blocks/structure_block_save.png": (240, 416),
    "input/blocks/sugar_cane.png": (144, 64),
    "input/blocks/sunflower_back.png": (112, 336),
    "input/blocks/sunflower_bottom.png": (96, 336),
    "input/blocks/sunflower_front.png": (112, 320),
    "input/blocks/sunflower_top.png": (96, 320),
    "input/blocks/tall_grass_bottom.png": (16, 336),
    "input/blocks/tall_grass_top.png": (16, 320),
    "input/blocks/tall_seagrass_bottom.png": (48, 496),
    "input/blocks/tall_seagrass_top.png": (48, 480),
    "input/blocks/tallgrass.png": (112, 32),
    "input/blocks/terracotta.png": (16, 256),
    "input/blocks/tnt_bottom.png": (160, 0),
    "input/blocks/tnt_side.png": (128, 0),
    "input/blocks/tnt_top.png": (144, 0),
    "input/blocks/torch.png": (0, 80),
    "input/blocks/torch_on.png": (0, 80),
    "input/blocks/trapdoor.png": (64, 80),
    "input/blocks/trip_wire.png": (208, 160),
    "input/blocks/trip_wire_source.png": (192, 160),
    "input/blocks/tripwire.png": (208, 160),
    "input/blocks/tripwire_hook.png": (192, 160),
    "input/blocks/tube_coral.png": (144, 480),
    "input/blocks/tube_coral_block.png": (64, 480),
    "input/blocks/tube_coral_fan.png": (144, 496),
    "input/blocks/vine.png": (240, 128),
    "input/blocks/waterlily.png": (192, 64),
    "input/blocks/web.png": (176, 0),
    "input/blocks/wet_sponge.png": (192, 128),
    "input/blocks/wheat_stage0.png": (128, 80),
    "input/blocks/wheat_stage1.png": (144, 80),
    "input/blocks/wheat_stage2.png": (160, 80),
    "input/blocks/wheat_stage3.png": (176, 80),
    "input/blocks/wheat_stage4.png": (192, 80),
    "input/blocks/wheat_stage5.png": (208, 80),
    "input/blocks/wheat_stage6.png": (224, 80),
    "input/blocks/wheat_stage7.png": (240, 80),
    "input/blocks/wheat_stage_0.png": (128, 80),
    "input/blocks/wheat_stage_1.png": (144, 80),
    "input/blocks/wheat_stage_2.png": (160, 80),
    "input/blocks/wheat_stage_3.png": (176, 80),
    "input/blocks/wheat_stage_4.png": (192, 80),
    "input/blocks/wheat_stage_5.png": (208, 80),
    "input/blocks/wheat_stage_6.png": (224, 80),
    "input/blocks/wheat_stage_7.png": (240, 80),
    "input/blocks/white_concrete.png": (224, 432),
    "input/blocks/white_concrete_powder.png": (224, 448),
    "input/blocks/white_glazed_terracotta.png": (224, 464),
    "input/blocks/white_stained_glass.png": (224, 288),
    "input/blocks/white_stained_glass_pane_top.png": (224, 304),
    "input/blocks/white_terracotta.png": (224, 272),
    "input/blocks/white_tulip.png": (80, 352),
    "input/blocks/white_wool.png": (0, 64),
    "input/blocks/wool_colored_black.png": (16, 112),
    "input/blocks/wool_colored_blue.png": (16, 176),
    "input/blocks/wool_colored_brown.png": (16, 160),
    "input/blocks/wool_colored_cyan.png": (16, 208),
    "input/blocks/wool_colored_gray.png": (32, 112),
    "input/blocks/wool_colored_green.png": (16, 144),
    "input/blocks/wool_colored_light_blue.png": (32, 176),
    "input/blocks/wool_colored_lime.png": (32, 144),
    "input/blocks/wool_colored_magenta.png": (32, 192),
    "input/blocks/wool_colored_orange.png": (32, 208),
    "input/blocks/wool_colored_pink.png": (32, 128),
    "input/blocks/wool_colored_purple.png": (16, 192),
    "input/blocks/wool_colored_red.png": (16, 128),
    "input/blocks/wool_colored_silver.png": (16, 224),
    "input/blocks/wool_colored_white.png": (0, 64),
    "input/blocks/wool_colored_yellow.png": (32, 160),
    "input/blocks/yellow_concrete.png": (240, 432),
    "input/blocks/yellow_concrete_powder.png": (240, 448),
    "input/blocks/yellow_glazed_terracotta.png": (240, 464),
    "input/blocks/yellow_stained_glass.png": (240, 288),
    "input/blocks/yellow_stained_glass_pane_top.png": (240, 304),
    "input/blocks/yellow_terracotta.png": (240, 272),
    "input/blocks/yellow_wool.png": (32, 160)
    }

    # Chemin de l'image de terrain d'origine
    terrain_input_path = "assets/texture/terrain.png"

    # Chemin de sortie pour l'image de terrain fusionnée
    terrain_output_path = "output/terrain.png"

    # Copie de l'image de terrain vers le répertoire de sortie
    shutil.copyfile(terrain_input_path, terrain_output_path)

    # Multiplier les coordonnées par 2
    image_dict = multiply_coordinates(image_dict, 1)

    # Appel de la fonction pour fusionner les images sur terrain.png
    merge_images(image_dict, terrain_output_path, 16, 16, terrain_output_path)

    # Redimensionner terrainMipMapLevel2.png en 128x272
    resize_image(terrain_output_path, "output/terrainMipMapLevel2.png", 128, 272)
    TextConsole.insert(tk.INSERT, "terrainMipMapLevel2.png converted output/terrainMipMapLevel2.png\n")
    TextConsole.insert(tk.INSERT, "----------------------------------\n")
    TextConsole.see(tk.END)

    # Copier et redimensionner terrainMipMapLevel2.png pour terrainMipMapLevel3.png
    shutil.copyfile("output/terrainMipMapLevel2.png", "output/terrainMipMapLevel3.png")
    resize_image("output/terrainMipMapLevel3.png", "output/terrainMipMapLevel3.png", 64, 136)
    TextConsole.insert(tk.INSERT, "terrainMipMapLevel3.png converted output/terrainMipMapLevel3.png\n")
    TextConsole.insert(tk.INSERT, "----------------------------------\n")
    TextConsole.see(tk.END)

# ------------------------------------------

# Créer l'app
TextureApp = tk.Tk()
TextureApp.title("Converter : Terrain (x16)")
IconPath = os.path.abspath("assets/iconterrain16_1.ico")
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
process_button = tk.Button(TextureApp, text="Convert Blocks (x16)", command=process_images)
process_button.place(x=127.5, y=62)
process_button.configure(relief="solid", bd=2)

# Créer le widget ScrolledText
TextConsole = ScrolledText(TextureApp, width=34, height=7)
TextConsole.place(x=42.5, y=113)
TextConsole.insert(tk.INSERT, "Version : 1.0 - Check if any      update have been made.\n")
TextConsole.insert(tk.INSERT, "----------------------------------\n")
TextConsole.configure(relief="solid", bd=2)

# ------------------------------------------

#   **--Title and Background--** 

TitleAppText = "Blocks Pack Converter x16"
TitleAppFontSize = 25
TitleAppFont = ImageFont.truetype(FontMojangles, TitleAppFontSize)

# Image and Border
TitleAppImageWidth = 390
TitleAppImageHeight = 35
TitleAppImage = Image.new("RGBA", (TitleAppImageWidth, TitleAppImageHeight), (255, 255, 255, 0))
TitleAppDraw = ImageDraw.Draw(TitleAppImage)
TitleAppOutlineColor = (0, 0, 0)
TitleAppOutlinePosition = (10.5, 4)
TitleAppDraw.text(TitleAppOutlinePosition, TitleAppText, font=TitleAppFont, fill=TitleAppOutlineColor)

# Draw Text
TitleAppTextColor = (255, 255, 255)
TitleAppTextPosition = (9, 2)
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
