# Gregtech: Boiler Blower
Credits:
Lrdmtns: Lead Dev and Creator

# Development

## Making a development instance

### Requirements
- Git (https://git-scm.com/)
- Packwiz (https://packwiz.infra.link/installation/)
- Python3 (https://www.python.org/)
- MultiMC (or a derivative) (https://multimc.org/, https://prismlauncher.org/; if you are using prism+linux, it is not recommended to use the flatpak version, as it uses a sandbox that is known to cause problems)
- Java8 specifically (https://adoptium.net/temurin/releases/?version=8)

### Installing
- Create a bare-bone mc instance running 1.12.2 on the newest forge.
- Clone https://github.com/DrBeako/Gregtech_Boiler_Blower/ to a directory called packwiz, it should be located in the same directory as your minecraft folder. Ex:

![image](https://github.com/DrBeako/Gregtech_Boiler_Blower/assets/77862418/b846f4a4-2fac-4a5d-8496-020bac74e6b9)

- Download https://github.com/packwiz/packwiz-installer-bootstrap/releases and paste it into your minecraft folder.
- You could also do this with GitHub Desktop if you know how to do it.
#### Windows
- Set the pre-launch on your prism/multimc instance to: 
- `cmd /c python3 "$INST_DIR/packwiz/update.py"`
- And the post-launch to:
- `cmd /c python3 "$INST_DIR/packwiz/generate.py"`
#### Linux
- If your python command runs python3, you can use just python.
- Prelaunch:
- `/bin/bash -c python3 "$INST_DIR/packwiz/update.py"`
- Postlaunch:
- `/bin/bash -c python3 "$INST_DIR/packwiz/generate.py"`

Launch the instance & get developing!

### Updating
- Re-launch the instance

### Pushing
- Open your packwiz directory.
- Run `git add .` in your terminal in the packwiz folder.
- Run `git commit -am "(whatever message you want the commit to say)"`
- and finally, run `git push`

## Adding mods

- In the packwiz folder, run the command `packwiz curseforge install (project slug)`
- To find the project slug, first open up a curseforge mod's page, and look at the end of the website link, Ex:

![image](https://github.com/DrBeako/Gregtech_Boiler_Blower/assets/77862418/fa80f288-7f58-42bb-a418-6b3c0e90a73b)


