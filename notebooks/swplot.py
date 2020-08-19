import matplotlib as mpl
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
import numpy as np

# groupvar, xvar, yvar,

def disp_figure01(xscale_label, yscale_label, groupvar, xvar, yvar, xlabel_name, ylabel_name, dataset01, dataset02, save_location):
    # Edit the font, font size, and axes width
    mpl.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams['font.size'] = 24
    plt.rcParams['axes.linewidth'] = 2

    # Create figure object and store it in a variable called 'fig'
    # (width, height) in inches
    fig = plt.figure(figsize=(7, 6))
    # Add axes object to our figure that takes up entire figure
    ax = fig.add_axes([0, 0, 1, 1])

    # Adding log scales in axis
    #plt.xscale('log')
    #plt.yscale('log')

    #xscale_label = "linear" # it can also be "log"
    #yscale_label = "linear" # it can also be "log
    # Adding linear scales in axis
    plt.xscale(xscale_label)
    plt.yscale(yscale_label)

    #Adding TItle for the figure
    # plt.title('S/d vs We')

    # Add two axes objects to create an inset figure
    #ax1 = fig.add_axes([0, 0, 1, 1])
    #ax2 = fig.add_axes([0.5, 0.5, 0.4, 0.4])

    # Hide the top and right spines of the axis
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    # Edit the major and minor ticks of the x and y axes (keep this fixed)
    ax.xaxis.set_tick_params(which='major', size=10, width=2, direction='inout')
    ax.xaxis.set_tick_params(which='minor', size=7, width=2, direction='inout')
    ax.yaxis.set_tick_params(which='major', size=10, width=2, direction='inout')
    ax.yaxis.set_tick_params(which='minor', size=7, width=2, direction='inout')

    # These will vary
    #xlabel_name = '$\mathregular{We_{l_c}^{1/5}}$'
    #ylabel_name = '$\mathregular{S/d}$'
    # Add the axis label with latex expressions
    ax.set_xlabel(r"{}".format(xlabel_name), labelpad=5)
    ax.set_ylabel(r"{}".format(ylabel_name), labelpad=5)

    # Plot and show our data


    # Creating the groups for legend
    groups = dataset01.groupby(groupvar)
    for l, grp in groups:
        ax.plot(grp[xvar], grp[yvar],'k+',label = l)
    groups2 = dataset02.groupby(groupvar)
    for l, grp in groups2:
        ax.plot(grp[xvar], grp[yvar],'ko',label = l)

    # Enabling legends
    #ax.legend(loc='lower right', frameon=True)

    #the save location can vary
    #save_location = "C:\\Users\\sabbi\\Dropbox\\Darryl James\\Mendeley_library\\JetEntrainment\\Selective\\Qualifying_docs\\SW_Python\\output\\S_dvsWe.png"

    # Save the figure
    fig.savefig(save_location, dpi=300, transparent=False, bbox_inches='tight')

    plt.show()


    return ax.plot


def func(x, a, b):
    # return a * np.exp(b * x)
    return a * x + b

def disp_figure_fit(xscale_label, yscale_label, groupvar, xvar, yvar, xlabel_name, ylabel_name, dataset01, dataset02, xFit, ppars1, ppars2, save_location):
    # Edit the font, font size, and axes width
    mpl.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams['font.size'] = 24
    plt.rcParams['axes.linewidth'] = 2

    # Create figure object and store it in a variable called 'fig'
    # (width, height) in inches
    fig = plt.figure(figsize=(7, 6))
    # Add axes object to our figure that takes up entire figure
    ax = fig.add_axes([0, 0, 1, 1])

    # Adding log scales in axis
    #plt.xscale('log')
    #plt.yscale('log')

    #xscale_label = "linear" # it can also be "log"
    #yscale_label = "linear" # it can also be "log
    # Adding linear scales in axis
    plt.xscale(xscale_label)
    plt.yscale(yscale_label)

    #Adding TItle for the figure
    # plt.title('S/d vs We')

    # Add two axes objects to create an inset figure
    #ax1 = fig.add_axes([0, 0, 1, 1])
    #ax2 = fig.add_axes([0.5, 0.5, 0.4, 0.4])

    # Hide the top and right spines of the axis
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    # Edit the major and minor ticks of the x and y axes (keep this fixed)
    ax.xaxis.set_tick_params(which='major', size=10, width=2, direction='inout')
    ax.xaxis.set_tick_params(which='minor', size=7, width=2, direction='inout')
    ax.yaxis.set_tick_params(which='major', size=10, width=2, direction='inout')
    ax.yaxis.set_tick_params(which='minor', size=7, width=2, direction='inout')

    # These will vary
    #xlabel_name = '$\mathregular{We_{l_c}^{1/5}}$'
    #ylabel_name = '$\mathregular{S/d}$'
    # Add the axis label with latex expressions
    ax.set_xlabel(r"{}".format(xlabel_name), labelpad=5)
    ax.set_ylabel(r"{}".format(ylabel_name), labelpad=5)

    # Plot and show our data


    # Creating the groups for legend
    groups = dataset01.groupby(groupvar)
    for l, grp in groups:
        ax.plot(grp[xvar], grp[yvar],'k+',label = l)
    groups2 = dataset02.groupby(groupvar)
    for l, grp in groups2:
        ax.plot(grp[xvar], grp[yvar],'ko',label = l)

    plt.plot(xFit, func(xFit, *ppars1), 'r--', label = 'fitted: a=%3.2f, b=%5.2f'% tuple(ppars1))
    plt.plot(xFit, func(xFit, *ppars2), 'r--', label = 'fitted: a=%3.2f, b=%5.2f'% tuple(ppars2))



    # Enabling legends
    #ax.legend(loc='lower right', frameon=True)

    #the save location can vary
    #save_location = "C:\\Users\\sabbi\\Dropbox\\Darryl James\\Mendeley_library\\JetEntrainment\\Selective\\Qualifying_docs\\SW_Python\\output\\S_dvsWe.png"

    # Save the figure
    fig.savefig(save_location, dpi=300, transparent=False, bbox_inches='tight')

    plt.show()


    return ax.plot




if __name__ == "__main__":
    import numpy as np
    import pandas as pd 
    
    file_name = 'C:\\Users\\sabbi\\Dropbox\\Darryl James\\Mendeley_library\\JetEntrainment\\Selective\\Qualifying_docs\\SW_Python\\input\\single.csv' 
    data_single = pd.read_csv(file_name)
    file_name = 'C:\\Users\\sabbi\\Dropbox\\Darryl James\\Mendeley_library\\JetEntrainment\\Selective\\Qualifying_docs\\SW_Python\\input\\utube.csv' 
    data_utube = pd.read_csv(file_name)

    print("Done")

    xscale_label = "linear"
    yscale_label = "linear"

    print("Done")
    
    groupvar = "fluids"
    xvar = "We_lc"
    yvar = "S_d"

    print("Done")

    xlabel_name = "$\mathregular{We_{l_c}^{1/5}}$"
    ylabel_name = "$\mathregular{S/d}$"

    print("Done")

    save_location = "C:\\Users\\sabbi\\Dropbox\\Darryl James\\Mendeley_library\\JetEntrainment\\Selective\\Qualifying_docs\\SW_Python\\output\\S_dvsWe.png"

    print("Done")

    disp_figure01(xscale_label, yscale_label, groupvar, xvar, yvar, xlabel_name, ylabel_name, data_single, data_utube, save_location)

    print("Done")



