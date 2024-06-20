import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

data={"year":[1920,1930,1940,1950,1960,1970,1980,1990,2000,2010],
      "unemployement_rate":[9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]}

dataframe=pd.DataFrame(data)


main_window=tk.Tk()

figure=plt.figure(figsize=(5,4),dpi=100)

figure_plot=figure.add_subplot(1,1,1)
figure_plot.set_ylabel('unemployement rate')

line_graph=FigureCanvasTkAgg(figure,main_window)

line_graph.get_tk_widget().pack(side=tk.LEFT,fill=tk.BOTH)

dataframe=dataframe[['year','unemployement_rate']].groupby('year').sum()

dataframe.plot(kind='line',legend=True,ax=figure_plot,color='r',marker='o',fontsize=10)
            
figure_plot.set_title('year vs.unemployment.rate')

main_window.mainloop()
