from enum import Enum


class Weapons(Enum):
    # Medium Ranged Weapons
    AKM = 1
    CB_01_REPEATER = 2 # Had to adjust for enum naming constraints / CB-01 REPEATER
    CERBERUS_12GA = 3
    CHIMERA_XB = 4 # Had to adjust for enum naming constraints / CHIMERA-XB
    CL_40 = 5 # Had to adjust for enum naming constraints / CL-40
    FAMAS = 6
    FCAR = 7
    MODEL_1887 = 8
    P90 = 9
    PIKE_556 = 10 # Had to adjust for enum naming constraints / PIKE-556
    R_357 = 11 # Had to adjust for enum naming constraints / R.357

    # Heavy Ranged Weapons
    _50_AKIMBO = 12 # Had to adjust for enum naming constraints / .50 Akimbo
    BFR_TITAN = 13
    FLAMETHROWER = 14
    KS_23 = 15 # Had to adjust for enum naming constraints / KS-23
    LEWIS_GUN = 16
    M134_MINIGUN = 17
    M60 = 18
    MGL32 = 19
    SA1216 = 20
    SHAK_50 = 21 # Had to adjust for enum naming constraints / SHAK-50

    # Light Ranged Weapons
    _93R = 22 # Had to adjust for enum naming constraints / 93R
    ARN_220 = 23 # Had to adjust for enum naming constraints / ARN-220
    LH1 = 24
    M11 = 25
    M26_MATTER = 26
    RECURVE_BOW = 27
    SH1900 = 28
    SR_84 = 29 # Had to adjust for enum naming constraints / SR-84
    V9S = 30
    XP_54 = 31 # Had to adjust for enum naming constraints / XP-54

    # Medium Melee Weapons
    DUAL_BLADES = 32
    RIOT_SHIELD = 33

    # Heavy Melee Weapons
    SLEDGEHAMMER = 34
    SPEAR = 35
    
    # Light Melee Weapons
    DAGGER = 36
    SWORD = 37
    THROWING_KNIVES = 38 # Works best with the project's Melee properties, even though it's a ranged weapon.