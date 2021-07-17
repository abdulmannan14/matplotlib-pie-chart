import matplotlib.pyplot as plt
#   red = E14728
#   blue 1 = 0C43C0
#   blue 2 =0588E9
#   blue 3 =6C8BCA
#   purple = 505190
#   green  = 35AB0F
colours = ['#E14728', '#0C43C0', '#0588E9', '#6C8BCA', '#505190', '#35AB0F', '#505190',
           '#35AB0F', '#0C43C0', '#0588E9', '#6C8BCA', '#505190', '#35AB0F', '#505190',
           '#35AB0F', '#0C43C0', '#0C43C0', '#0588E9', '#6C8BCA', '#505190', '#35AB0F',
           '#505190', '#35AB0F', '#0C43C0', '#0588E9', '#6C8BCA', '#505190', '#35AB0F',
           '#505190', '#35AB0F']
sector_label = []
sector_value = []
explode_list = []
colors = []
input_size = int(input("please enter the number of sections"))
if input_size <= 32:
    if input_size >= 3:
        for i in range(input_size):
            names = input("please enter name of  section")
            if ',' in names:
                sector_label.append(names)
                sector_value.append(60)
                explode_list.append(0.006)
            else:
                sector_label.append(names)
                sector_value.append(30)
                explode_list.append(0.006)
        for i in range(input_size):
            colors.append(colours[i])
        sector_to_focus = int(input("please enter the sequence number of sector you want to get focused"))
        sector_to_focus=sector_to_focus-1
        focused_sector_radius = float(input("please enter  focused sector radius(recommended 0.006-0.1)!!! For not focusing please type 0.006 "))
        explode_list[sector_to_focus] = focused_sector_radius
        explode = explode_list
        inner_radius = float(input("please set inner radius between (between 0.1-0.9)"))
        outer_radius = float(input("please set outer radius between (Recommonded 0.5-2.0 )"))
        outer_radius= inner_radius+outer_radius
        def make_autopct(sector_label):
            def my_autopct(pct):
                make_autopct.counter += 1
                return sector_label[make_autopct.counter]
            return my_autopct
        make_autopct.counter = -1
        wedges,text,autopct=plt.pie(
            sector_value,
            colors=colors,
            autopct=make_autopct(sector_label),
            # pctdistance=0.75,
            # explode=explode,
            counterclock=False,
            startangle=90,
            radius=1,
            textprops={'color': "w",'fontsize':20},
            wedgeprops={'edgecolor': 'black'},
            shadow=False,
        )
        wedges[sector_to_focus].set_radius(focused_sector_radius+1)
        # draw circle
        centre_circle = plt.Circle((0,0), inner_radius, color='black', linewidth=3.25, fc='white')
        fig = plt.gcf()
        fig.patch.set_facecolor('black')
        # Adding Circle in Pie chart
        fig.gca().add_artist(centre_circle)
        # Adding Title of chart
        plt.title('Sughosh Work', color='white')
        # plt.axis('equal')
        # plt.tight_layout()
        # Displaing Chart
        dpi = int(input("please type DPI for saving picture resolution best will be from 100-500"))
        plt.show()
        fig.savefig('chart1.png',transparent=False,dpi=dpi)
    else:
        print("please enter input larger then 3 ")
else:
    print("please enter input smaller then 32 ")
