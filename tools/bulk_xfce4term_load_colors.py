# Disclaimer:
# this code was made to work with specific files in mind
# HTML files based on "color_scheme_template.html" 
# you can find this template in https://github.com/fm3chanic/color_schemes
# the target file is "xfce4term_theme_template.theme"
# you can find this template in https://github.com/fm3chanic/xfce4-terminal_themes

import pandas as pd
import sys
import os

def main(filename):
    #define required lists
    tab1_values = []
    tab2_values = []

    #define valuse for replacement
    tab1_replace = ['BackGround1','BackGround2','BackGround3','ForeGround1','ForeGround2','ForeGround3','HighLight1','HighLight2','HighLight3']
    tab2_replace = ['Main1','Main2','Main3','Main4','Main5','Main6','Sub1','Sub2','Sub3','Sub4','Sub5','Sub6']

    input_file = f'{filename}.html'
    output_file = f'{filename}.theme'

    #output of read_html() is a list with two data frames
    df = pd.read_html(input_file, header=0)

    #copying data frames to create dedicated lists
    tab1 = df[0]
    tab1_values = tab1.iloc[0:9,1].tolist()

    tab2 = df[1]
    tab2_values = tab2.iloc[0:12,1].tolist()

    # reading the template
    f = open('xfce4term_theme_template.theme', 'r', encoding='utf-8')
    content = f.read()
    f.close()

    #iterating through lists
    #mapped expression will be replaced with color codes accordingly
    for i in range(9):
        content = content.replace(tab1_replace[i], tab1_values[i])

    for i in range(12):
        content = content.replace(tab2_replace[i], tab2_values[i])    

    content = content.replace("ThemeName", filename)

    # creating the completed output file
    f = open(output_file, 'w', newline='\n', encoding='utf-8')
    f.write(content)
    f.close()
    
source_files = []
source_files = os.listdir()
file_count = len(source_files)
filename = source_files[0]
i = 0

while filename != source_files[(file_count - 1)]:
    x = filename.find(".html")
    if x > 1:
        filename = filename.replace(".html", "")
        main(filename)
    i += 1
    filename = source_files[i]