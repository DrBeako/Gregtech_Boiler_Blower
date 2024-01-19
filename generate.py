#!/usr/bin/python3

# I dedicate this script to Powershell, Bash and Git. The three fuckers that don't wanna work together and instead result in a circus
# Love y'all <3
# Python my beloved

from pathlib import Path
from filecmp import cmp
from os import chdir, path, remove, makedirs, chmod, system
from shutil import copy, rmtree
from stat import S_IWRITE

DIRECTORIES = [
    "config",
    "defaultconfigs",
    "fancymenu_assets",
    "fancymenu_setups",
    "kubejs",
    "patchouli_books",
    "multiblocked",
    "worldshape",
    "quests_structures"
]

def main():
    chdir(path.dirname(path.realpath(__file__)))

    chdir(path.join("..", ".minecraft"))
    for d in DIRECTORIES:
        for f in Path(d).rglob("**/*"): 
            packwizpath = path.join("..", "packwiz", f)
            if f.is_file() and not (path.exists(packwizpath) and (cmp(f, packwizpath) or path.getmtime(packwizpath)>path.getmtime(f))):
                makedirs(path.dirname(packwizpath), exist_ok=True)
                copy(f, packwizpath)

    chdir(path.dirname(path.realpath(__file__)))

    for d in DIRECTORIES:
        for f in Path(d).rglob("**/*"): 
            if not path.exists(path.join("..", ".minecraft", f)): 
                if f.is_dir(): rmtree(f, onerror=lambda f, p, s: chmod(p, S_IWRITE))
                else: remove(f)

    system("git checkout HEAD -- index.toml pack.toml")
    if (system("git pull -q")!=0): 
        system("git stash")
        system("git pull")
        system("git stash pop")
        print("Merge conflict. Review in vscode.")
        exit(1)

    print("Generation successful!")

if __name__=="__main__": main()