from bokeh.plotting import figure,output_file,show,ColumnDataSource,save
from bokeh.models.tools import HoverTool
from bokeh.transform import factor_cmap
from bokeh.palettes import Greens256
import pandas

#Citeste din setul de date
df=pandas.read_csv('db.csv')

source=ColumnDataSource(df)

#Afiseaza totul intr-ul file .html
output_file('bokeh.html')

#O variabila care imi retine numele locatiilor din setul de date
loc_list=source.data['Location'].tolist()

#Plot-ul
p=figure(
    y_range=loc_list,
    plot_width=1920,
    plot_height=1080,
    title='F1 Races on each circuit (1950-2020)',
    x_axis_label='Count'
    
)

p. title. text_font = "times"
p. title. text_font_style = "italic"
p.xaxis.axis_label_text_font_size = "20px"


#Generarea chart-ului
p.hbar(
    y='Location',
    right='Name',
    left=0,
    height=0.4,
    fill_color=factor_cmap(
        'Location',
        palette=Greens256,
        factors=loc_list
    ),
    fill_alpha=1,
    source=source
)


#Alte instrumente pentru chart
mouse=HoverTool()
mouse.tooltips="""
    <div class="btn">
        <h2 align="center">@Location</h2>
        <div><strong>Country: </strong>@aa</div>
        <div><strong>City name: </strong>@Country</div>
         <div><strong>Number of competitions hosted: </strong>@Name</div>
        <div><strong>Image</strong><br><img src="@Number" alt="" width="250"/></div>
    </div>

"""

p.add_tools(mouse)

#Afisare de rezulatate
#show(p)

#Save file
save(p)

