import random 
import mido 
import emoji
import os

adjectivos = [
    "irrevocable", "eldritch", "lambent", "abyssal", "ceremonial", "frangible",
    "auric", "soporific", "eldrichian", "vermillion", "auriferous", "inchoate",
    "plangent", "threnorous", "vorticose", "chthonic", "corvid", "baleful",
    "fluvial", "crystalline", "desolate", "igneous", "astral", "languid",
    "cataclysmic", "vespertine", "saturnine", "mythopoeic", "tactile", "phantasmagoric",
    "incorporeal", "celestine", "macabre", "liminal", "crepitant", "barbaric",
    "wretched", "eldrich", "mephitic", "basilisk", "monolithic", "sibilous",
    "ephemeral", "sacrosanct", "muted", "jagged", "ethereal", "antique",
    "mournful", "penumbral", "eldritchborne", "vellicating", "somber", "astriferous",
    "banshee", "caustic", "hieratic", "lucifugous", "umbriferous", "tempestuous",
    "inevitable", "eldrichlike", "unfathomable", "cimmerian", "arcadian", "volatile",
    "irrevocably", "threnodial", "sublunary", "eldritchcore", "delphic", "vaporbound"
]


foldername = "midi_files_".__add__(random.choice(adjectivos))
if not os.path.exists(foldername):
    os.makedirs(foldername)

from mido import Message, MidiFile, MidiTrack

random_ticks = random.randint(375000,600000)
tempo = int(60000000 / random_ticks)

import pyfiglet
Title = 'PYTHON BEATS'
ASCII_art_1 = pyfiglet.figlet_format(Title,font='3-d')
print(ASCII_art_1)
print(f'TEMPO: {tempo}')






def measures(a,b,c):
    if a == 4 and b == 4:
        beats = 4 * c

    if a == 3 and b == 4:
        beats = 3 * c
    if a == 6 and b == 8:
        beats = 6 * c
    return beats

measured = measures(4,4,8)

def kick():
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)
    track.append(mido.MetaMessage('set_tempo', tempo=random_ticks))



    emojis = [emoji.emojize(':fire:'), emoji.emojize(':beaming_face_with_smiling_eyes:'),emoji.emojize(':zany_face:')]
    random_emoji = random.choice(emojis)
    print(f"\nKICK {random_emoji}:")
    characters = ' .'
    length = 4
    numbers = [
    'wild', 'smooth', 'crazy', 'dark', 'bright', 'heavy', 'light', 
    'sick', 'fire', 'cold', 'hot', 'dirty', 'clean', 'raw', 'crisp',
    'epic', 'massive', 'tiny', 'loud', 'quiet', 'fast', 'slow',
    'bouncy', 'groovy', 'funky', 'jazzy', 'chill', 'hype', 'mellow',
    'aggressive', 'soft', 'hard', 'smooth', 'rough', 'sharp', 'blunt',
    'electric', 'acoustic', 'digital', 'analog', 'vintage', 'modern',
    'classic', 'fresh', 'stale', 'spicy', 'bland', 'sweet', 'bitter',
    'energetic', 'lazy', 'explosive', 'calm', 'chaotic', 'ordered',
    'random', 'precise', 'messy', 'neat', 'broken', 'perfect',
    'glitchy', 'polished', 'gritty', 'silky', 'crusty', 'juicy']

    kickname = 'kick_'.__add__(random.choice(numbers))
    y = ''.join(random.choice(characters) for _ in range(length))
    y1 = ''.join(random.choice(characters) for _ in range(length))
    y2 = ''.join(random.choice(characters) for _ in range(length))
    y3 = ''.join(random.choice(characters) for _ in range(length))
    x = '|' + y +'|'+ y1 +'|'+ y2 +'|'+ y3 + '|'
    for i, char in enumerate(x):
        offset = 480 if i < 0 else 0
        if char == '.':
            
            track.append(Message('note_on', note=60, velocity=110, time=0))
            track.append(Message('note_off', note=60, velocity=110, time=480))
        elif char == ' ':
            track.append(Message('note_on', note=60, velocity=0, time=0))
            track.append(Message('note_off', note=60, velocity=0, time=480))
        else:
            continue
    
    mid.save(f'{foldername}/{kickname}.mid')
    print(f"Beat saved as {kickname}.mid!")
    return x
    


print(kick())



def hihat():
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)
    track.append(mido.MetaMessage('set_tempo', tempo=random_ticks))



    emojis = [emoji.emojize(':fire:'), emoji.emojize(':beaming_face_with_smiling_eyes:'),emoji.emojize(':zany_face:')]
    random_emoji = random.choice(emojis)
    print(f"\nHIHATS {random_emoji}:")
    characters = '-. '
    length = 8
    numbers = [
    "skibidi", "rizzed", "goofy", "sigma", "gyatt", "delulu", 
    "fanumtaxed", "npc", "aura", "zesty", "ohio", "based", 
    "cringeful", "meaty", "gritty", "drippy", "cooked", "bussin", 
    "mid", "rizzless", "glazed", "chillmaxxed", "auraful", 
    "womped", "brainrotted", "alpha", "omega", "core", "tweaky", 
    "schizo", "baldcore", "real", "unserious", "yapped", "baked", 
    "slumped", "goated", "crazy", "feral", "mewing", "yappedout"]

    hatname = 'hihat_'.__add__(random.choice(numbers))
    y = ''.join(random.choice(characters) for _ in range(length))
    y1 = ''.join(random.choice(characters) for _ in range(length))
    y2 = ''.join(random.choice(characters) for _ in range(length))
    y3 = ''.join(random.choice(characters) for _ in range(length))
    x = '|' + y +'|'+ y1 +'|'+ y2 +'|'+ y3 + '|'
    for i, char in enumerate(x):
        if char == '.':
            
            track.append(Message('note_on', note=60, velocity=110, time=0))
            track.append(Message('note_off', note=60, velocity=110, time=240))
        elif char == ' ':
            track.append(Message('note_on', note=60, velocity=0, time=0))
            track.append(Message('note_off', note=60, velocity=0, time=240))
        elif char == '-':
            track.append(Message("note_on", note = 60, velocity = 110, time=0))
            track.append(Message("note_off", note = 60, velocity = 110, time=60))
            track.append(Message("note_on", note = 60, velocity = 110, time=0))
            track.append(Message("note_off", note = 60, velocity = 110, time=60))
            track.append(Message("note_on", note = 60, velocity = 110, time=0))
            track.append(Message("note_off", note = 60, velocity = 110, time=60))
            track.append(Message('note_on', note=60, velocity=0, time=0))
            track.append(Message('note_off', note=60, velocity=0, time=60))
            
        else:
            continue
    
    mid.save(f'{foldername}/{hatname}.mid')
    print(f"Beat saved as {hatname}.mid!")
    return x
    
print(hihat())

def snare():
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)
    track.append(mido.MetaMessage('set_tempo', tempo=random_ticks))
    emojis = [emoji.emojize(':fire:'), emoji.emojize(':beaming_face_with_smiling_eyes:'),emoji.emojize(':zany_face:')]
    random_emoji = random.choice(emojis)
    print(f"\nSNARE {random_emoji}:")
    characters = ' .'
    length = 4
    numbers = [
    "ethereal", "liminal", "eldritch", "phantasmic", "sonorous", "sepulchral",
    "verdant", "jejune", "diaphanous", "lachrymose", "nocturnal", "glacial",
    "effervescent", "subliminal", "taciturn", "zephyric", "discordant",
    "mycelial", "tenebrous", "halcyon", "incandescent", "melancholic",
    "somnolent", "gossamer", "moribund", "labyrinthine", "opalescent",
    "atavistic", "primordial", "nymphic", "cacophonic", "baroque",
    "histrionic", "eldritch", "paradoxical", "acerbic", "visceral",
    "chimeric", "florid", "lurid", "fugacious", "sibilant", "corrosive",
    "transcendent", "wraithlike", "cryptic", "numinous", "turbid",
    "blithe", "effulgent", "oblique", "sardonic"]

    snarename = 'snare_'.__add__(random.choice(numbers))
    y = ''.join(random.choice(characters) for _ in range(length))
    y1 = ''.join(random.choice(characters) for _ in range(length))
    y2 = ''.join(random.choice(characters) for _ in range(length))
    y3 = ''.join(random.choice(characters) for _ in range(length))
    x = '|' + y +'|'+ y1 +'|'+ y2 +'|'+ y3
    for i, char in enumerate(x):
        offset = 480 if i < 0 else 0
        if char == '.':
            
            track.append(Message('note_on', note=60, velocity=110, time=0))
            track.append(Message('note_off', note=60, velocity=110, time=480))
        elif char == ' ':
            track.append(Message('note_on', note=60, velocity=0, time=0))
            track.append(Message('note_off', note=60, velocity=0, time=480))
        else:
            continue
    
    mid.save(f'{foldername}/{snarename}.mid')
    print(f"Beat saved as {snarename}.mid!")
    return x


print(snare())


def melody():
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)
    track.append(mido.MetaMessage('set_tempo', tempo=random_ticks))

    print("\nMELODY:")
    print(f"Key: C")
    characters = "-_=≡ "
    c_scale = [60, 62, 64, 65, 67, 69, 71, 72]
    random_note = random.choice(c_scale)
    triad_note = random.choice(c_scale)
    minor_triad = triad_note + 3
    random_note1 = random.choice(c_scale)
    length = 8
    adjectives = [
    "eldritch", "luminous", "arcane", "somber", "igneous", "vaporous",
    "phantasmal", "cerulean", "ebullient", "mellifluous", "bucolic", "eldritch",
    "apocryphal", "turbulent", "velveteen", "iridescent", "crepuscular",
    "efflorescent", "ineffable", "pellucid", "blasphemous", "chromatic",
    "candescent", "mirthless", "carnelian", "sanguine", "verdigris",
    "haunted", "delirious", "coruscating", "translucent", "eldritch",
    "auroral", "quixotic", "dissonant", "volatile", "wistful", "gnarled",
    "fractal", "miasmic", "diluvian", "manic", "reverent", "stygian",
    "frigid", "threnodic", "lucid", "brumal", "sylvan", "somatic",
    "cosmic", "parched", "hypnagogic", "mercurial", "sublime", "sinister",
    "brittle", "viscid", "untamed", "eldritch", "dappled", "hollow",
    "eldritch", "ghastly", "evanescent", "volatile", "umbral", "echoic"]

    melodyname = 'melody_'.__add__(random.choice(adjectives))
    y = ''.join(random.choice(characters) for _ in range(length))
    y1 = ''.join(random.choice(characters) for _ in range(length))
    y2 = ''.join(random.choice(characters) for _ in range(length))
    y3 = ''.join(random.choice(characters) for _ in range(length))
    x = '|' + y +'|'+ y1 +'|'+ y2 +'|'+ y3
    for i, char in enumerate(x):
        offset = 480 if i < 0 else 0
        if char == '-':
            
            track.append(Message('note_on', note=random_note, velocity=110, time=0))
            track.append(Message('note_off', note=random_note, velocity=110, time=480))
        elif char == '=':
            track.append(Message('note_on', note=triad_note, velocity=110, time=0))
            track.append(Message('note_on', note=minor_triad, velocity=110, time=0))
            track.append(Message('note_off', note=triad_note, velocity=110, time=480))  
            track.append(Message('note_off', note=minor_triad, velocity=110, time=0))      
        elif char == '≡':
            track.append(Message('note_on', note=60, velocity=110, time=0))
            track.append(Message('note_on', note=63, velocity=110, time=0))
            track.append(Message('note_on', note=67, velocity=110, time=0))
            track.append(Message('note_off', note=60, velocity=110, time=480))
            track.append(Message('note_off', note=63, velocity=110, time=0))
            track.append(Message('note_on', note=67, velocity=110, time=0))  
        elif char == '_':
            track.append(Message('note_on', note=(triad_note + 1), velocity=110, time=0))
            track.append(Message('note_off', note=(triad_note + 1), velocity=110, time=480))
        elif char == ' ':
            track.append(Message('note_on', note=60, velocity=0, time=0))
            track.append(Message('note_off', note=60, velocity=0, time=480))
        else:
            continue
    
    mid.save(f'{foldername}/{melodyname}.mid')
    print(f"Beat saved as {melodyname}.mid!")
    return x



print(melody())

print(f'\nALL FILES STORED IN {foldername}')





