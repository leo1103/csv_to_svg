import csv
import textwrap
import svgwrite
import os

input_file = 'history_sheet_test.csv'
output_folder = 'svg_images_100'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)
with open(input_file, newline='', encoding ='utf-8') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=';')
    for row in csvreader:

        EVENT_INDEX=row[0]
        EVENT_DATE=row[1]
        EVENT_DESC=row[2]
        
        dwg = svgwrite.Drawing(filename=os.path.join(output_folder,EVENT_INDEX+".svg"))
        dwg.embed_font(name="Sriracha", filename='Sriracha.ttf')
        dwg.embed_stylesheet("""
            .sriracha31 {
                font-family: "Sriracha";
                font-size: 25pt;
                dominant-baseline:middle;
                text-anchor:start
            }
            .sriracha16 {
                font-family: "Sriracha";
                font-size: 12pt;
                dominant-baseline:middle;
                text-anchor:start
            }            
        """)

        
        dwg.viewbox(width=579, height=572)


        # IMAGE
        image = dwg.image("https://raw.githubusercontent.com/leo1103/csv_to_svg/master/Sandwich.jpg", insert=("0%", "0%"), size=("100%", "100%"))
        image.fit(horiz='center', vert='middle', scale='meet')
        dwg.add(image)
        
        # DATE
        date = dwg.g(class_="sriracha31")
        date.add(dwg.text(EVENT_DATE, insert=('24%', '23.5%'),fill='#36405C'))
        dwg.add(date)
        
        # DESCRIPTION
        # settings are valid for all text added to 'g'
        desc = textwrap.wrap(EVENT_DESC, 33)
        for i, line in enumerate(desc):
            description = dwg.g(class_="sriracha16")
            description.add(dwg.text(line, insert=('28%', int(270/3) + 28 * (i + 4)),fill='#36405C'))
            dwg.add(description)
        dwg.save()
