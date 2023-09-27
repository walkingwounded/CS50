#figlet lab test - library week


import sys
import random
from pyfiglet import Figlet
figlet = Figlet()

figlet_list = ['doh', 'house_of', '1943____', 'taxi____', 'charset_', 'ticks', 'fbr1____', 'c1______', 'goofy', 'smtengwar', 'trek', 'clb8x10', 'kgames_i', '4x4_offr', 'char4___', 'broadway', 'barbwire', 'type_set', 'unarmed_', 'lean', 'clr6x8', 'top_duck', 'battlesh', 'pebbles', 'contrast', 'starwars', 'charact2', 'bubble', 'speed', 'script__', 'stencil2', 'small', 'italics_', 'letterw3', 'cli8x8', 'c_consen', 'a_zooloo', 'coinstak', 'xsansb', 'nancyj-fancy', 'utopiai', 'sansi', 'z-pilot_', 'cybersmall', 'fair_mea', 'tty', 'runic', 'ivrit', 'xbritei', 'xbritebi', 'basic', 'banner', 'ti_pan__', 'mig_ally', 'cricket', 'fireing_', 'catwalk', 'eftitalic', 'graceful', 'yie_ar_k', 'univers', 'mad_nurs', '3-d', 'clb8x8', 'fp1_____', 'heavy_me', 'clr5x8', 'peaks', 'cosmike', 'war_of_w', 'asslt__m', 'xhelvi', 'crawford', 'xsbookbi', 'big', 'whimsy', 'eca_____', 'double', 'diamond', 'isometric3', 'cour', 'clr6x6', 'helv', 'zone7___', 'r2-d2___', 'high_noo', 'skateroc', 'smisome1', 'space_op', 'clr4x6', 'c2______', 'mirror', 'hyper___', 'sans', 'funky_dr', 'cosmic', 'raw_recu', 'italic', 'xbriteb', 'moscow', 'skate_ro', 'pyramid', 'smslant', 'britei', 'shimrod', 'mcg_____', 'joust___', 'atc_gran', 'colossal', 'eftiwall', 'relief2', 'future_1', 'threepoint', 'fuzzy', 'sm______', 'spc_demo', 'sansbi', 'bell', 'eftichess', 'bulbhead', 'rad_phan', 'marquee', 'xcouri', 'xsbook', 'e__fist_', 'slant', 'xsans', 'smkeyboard', 'epic', 'fraktur', 'rounded', 'weird', 'ebbs_1__', 'gradient', 'xcourb', 'decimal', 'ghost_bo', 'lazy_jon', 'short', 'eftipiti', 'stacey', 'pacos_pe', '6x10', 'demo_1__', 'alphabet', 'caligraphy', 'tomahawk', 'outrun__', 'alligator2', 'ttyb', 'b_m__200', 'graffiti', 'larry3d', 'mshebrew210', 'yie-ar__', 'times', 'sbookb', 't__of_ap', 'nvscript', 'street_s', 'battle_s', 'banner4', 'eftirobot', 'tsm_____', 'rozzo', 'nancyj-underlined', 'coil_cop', 'star_war', 'ok_beer_', 'home_pak', 'fp2_____', 'super_te', 'beer_pub', 'tec1____', 'digital', 'timesofl', 'letter_w', 'aquaplan', 'isometric2', 'maxfour', 'jerusalem', 'dcs_bfmo', 'pawn_ins', 'gothic', 'helvi', 'p_s_h_m_', 'charact1', 'eftiwater', 'utopia', 'road_rai', 'doom', 'bubble_b', 'charact4', '5lineoblique', 'magic_ma', 'xsbookb', 'cybermedium', 'f15_____', 'eftifont', 'ticksslant', 'tengwar', 'odel_lak', 'hades___', 'rad_____', 'tubular', 'clr5x10', 'sblood', 'c_ascii_', 'stealth_', 'kban', 'brite', 'calgphy2', 'zig_zag_', 'druid___', 'serifcap', 'chunky', 'linux', 'ogre', 'roman___', 'smshadow', 'mayhem_d', 'jazmine', 'future_6', 'tombstone', 'xchartr', 'tsn_base', 'briteb', 'utopiab', 'block', 'skateord', 'tinker-toy', 'slscript', 'fairligh', 'twin_cob', 'hollywood', 'npn_____', 'katakana', 'char3___', 'stop', 'xsansi', 'acrobatic', 'xbrite', 'usa_____', 'phonix__', 'sketch_s', 'o8', 'dotmatrix', 'asc_____', 'green_be', 'nfi1____', 'demo_2__', 'd_dragon', 'sbooki', 'thin', 'fourtops', 'puffy', '3x5', 'gothic__', 'inc_raw_', 'rowancap', 'computer', 'sbook', 'banner3-D', 'tecrvs__', 'helvb', 'fbr12___', 'ascii___', 'arrows', 'char1___', 'clb6x10', 'char2___', 'master_o', 'os2', 'alligator', 'krak_out', 'rockbox_', 'chartr', 'binary', 'poison', 'notie_ca', 'xhelv', 'bubble__', 'deep_str', 'octal', 'avatar', 'rally_sp', 'runyc', 'shadow', 'wavy', 'lockergnome', 'clr8x10', 'sbookbi', 'rci_____', 'thick', 'helvbi', 'p_skateb', 'mini', 'usa_pq__', 'xcour', 'chartri', 'faces_of', 'greek', 'term', 'xsbooki', 'madrid', 'ts1_____', 'xsansbi', 'platoon_', 'xhelvb', 'clr7x10', 'future_5', 'tsalagi', 'tanja', 'clr5x6', 'modern__', 'fbr_stri', 'britebi', 'hills___', 'caus_in_', 'mnemonic', 'advenger', '5x7', 'isometric4', 'rev', 'invita', 'vortron_', 'xttyb', 'xtty', 'roman', 'pod_____', 'baz__bil', 'xhelvbi', 'pawp', 'clr8x8', 'letters', 'cursive', 'sansb', 'kik_star', 'fbr_tilt', 'stencil1', 'xtimes', 'com_sen_', 'grand_pr', 'rampage_', 'ebbs_2__', 'rainbow_', 'charact3', 'ripper!_', 'bigchief', 'subteran', 'nancyj', '5x8', 'defleppard', 'usaflag', 'triad_st', 'courb', 'platoon2', 'clr6x10', '64f1____', 'fbr2____', 'smscript', 'atc_____', 'standard', 'rectangles', 'charact5', 'dwhistled', 'rally_s2', 'finalass', 'ucf_fan_', 'fantasy_', 'morse', 'couri', 'xcourbi', 'nipples', 'ntgreek', 'devilish', 'heroboti', 'rot13', 'lexible_', 'flyn_sh', 'relief', 'rok_____', 'clr7x8', 'banner3', 'characte', 'straight', 'trashman', 'tec_7000', 'script', 'hex', 'cyberlarge', 'twopoint', 'drpepper', 'ugalympi', 'panther_', 'fender', 'charact6', 'tav1____', 'courbi', 'stampatello', 'future_2', 'pepper', 'slide', 'lcd', 'stellar', 'isometric1', 'convoy__', 'gauntlet', 'xchartri', 'demo_m__', 'radical_', 'assalt_m', 'new_asci', 'hypa_bal', 'etcrvs__', 'future_4', 'rastan__', 'mike', 'future_3', 'tiles', 'future_8', 'contessa', 'future_7', 'utopiabi', '6x9'
]

def main():
    if len(sys.argv) == 1:
        i = input("Input: ")
        f = figlet.setFont(font=str(random.choice(figlet_list)))
        print(figlet.renderText(i))
    elif len(sys.argv) <3:
        sys.exit("Invalid usage")
    elif len(sys.argv) >3:
        sys.exit("Invalid usage")
    elif sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid usage")
    elif sys.argv[2] not in figlet_list:
        sys.exit("Invalid usage")
    else:
        i = input("Input: ")
        f = figlet.setFont(font=str(sys.argv[2]))
        print(figlet.renderText(i))

main()


### Testing figlet
# i = input("Input: ")
# f = figlet.setFont(font="weird")
# print(figlet.renderText(i))
# r = random.choice(figlet_list)
# print(r)

# figlet = Figlet()
# figlet.getFonts()
# figlet.setFont(font=f)
# print(figlet.renderText(s))

