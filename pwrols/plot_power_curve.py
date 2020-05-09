import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

def plot_power_curve(power_df, num_days, metric_name):
    """Returns an image file illustrating the power curve.
  
    This function takes a dataframe of power estimates as well as a list of hypothetical 
    run times for the hypothesis test, and assembles them into a heat map of the form (X,Y,Z)
    where X is the hypothetical run time in days, Y is the hypothetical effect size, and
    Z is the estimated statistical power.
  
    Parameters: 
    power_df (Pandas dataframe): Pandas dataframe containing the MDEs and power estimates
    num_days (list of integers): A list of the number of days (integers) of hypothetical run times
    metric_name (string): The name of the metric used in the hypothetical A/B test 
    
    Returns: 
    None: Saves a .png file to the local machine
    """    
    
    plt.tight_layout()
    
    ##### Specify the default font size for the legend ###################
    sns.set(font_scale=1.5)
    
    ##### Specify the default font #######################################
    plt.rcParams.update(
    {
        'text.usetex': False,
        'font.family': 'stixgeneral',
        'mathtext.fontset': 'stix',
    }
    )
    
    ##### Create plot #########################################
    fig, ax = plt.subplots(figsize=(12,7)) 
    p = sns.heatmap(power_df, 
                    annot=power_df, 
                    fmt="", 
                    cmap='RdYlGn', 
                    linewidths=0.3, 
                    annot_kws={"size": 13},
                    cbar_kws={'label': 'Estimated\nStatistical\nPower'})
    
    ##### Manually overlay title #########################################
    title = 'Estimated Statistical Power for a Hypothesis Test of:\n{}'.format(metric_name)
    fig.suptitle(title, size=28)
    fig.subplots_adjust(top=0.85)
    fig.subplots_adjust(left=0.25)
    
    ##### Specify the formatting for the legend ##########################
    ax.figure.axes[-1].yaxis.label.set_size(22)
    ax.figure.axes[-1].yaxis.label.set_rotation(0)
    ax.figure.axes[-1].yaxis.set_label_coords(6.0,0.8)
    
    p.set_yticklabels(labels = power_df.index, rotation=0, fontsize=18)
    p.set_xticklabels(labels = num_days, rotation=0, fontsize=18)
    
    ##### Label Axes #####################################################
    p.set_xlabel('Hypothetical Run Time in Days', 
                 rotation=0, fontsize=22, x=0.50, labelpad=10)
    p.set_ylabel('Hypothetical\nEffect\nSize\n-----\nRelative:\n(Absolute)', 
                 rotation=0, fontsize=22, y=0.50, labelpad=70)   
    
    ##### Save the results ###############################################
    plt.savefig('Power_Curve.png', bbox_inches='tight')
