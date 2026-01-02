## fm3chanic Themes for XFCE4-Terminal

This repository contains all color themes for the XFCE4 terminal emulator I've created so far.<br> 
It is the main terminal emulator of the XFCE4 desktop environment for Linux.

Themes which have been created during my project of color theming Vtubers are in the directory "vtuber_project". The directory "other" contains all color themes which where created outside of the project.

**[HTML Reference Sheets & Galery Non-Project Themes](https://github.com/fm3chanic/color_schemes)**<br>
**[Vtuber Project | Information & Galery](https://github.com/fm3chanic/vtuber_project)**

> [!IMPORTANT]
> Please note that all color themes have been originally created for Notepad++, which has the tendency to show colors lighter as they are in other applications. Therefore it might occur that the color theme is a bit on the darker side.

### Installation:

Copy the theme file to `~/.local/share/xfce4/terminal/colorschemes` and restart the application.<br>
The theme should now be selectable in the "Colors" tab of the "Preferences" as one of the preset colorschemes

> [!NOTE]
> It might be necessary to create the directory first as `/xfce4/terminal/colorschemes` might be missing in `~/.local/share`.

### Contribution:

The themes are based on the mapped template in directory **/tools**.<br>
The python script (_\[...\]\_load_colors.py_) reads the colors from a html file from [color_schemes](https://github.com/fm3chanic/color_schemes) and uses replace to fill in the colors.<br>

If you want to work on colors it makes the most sense to change the colors in repository [color_schemes](https://github.com/fm3chanic/color_schemes) so the changes can be applied to all applications using the theme.<br>
If you want to work on the mapping of the colors it might make sense to change the base template, so changes can be applied to all themes of this application.<br>

Neverless, **I also welcome contribution not following this standard**. The standard was made to keep it maintainable for one person, not to block community ideas.<br>