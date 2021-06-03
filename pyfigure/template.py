import numpy as np
import os
import glob
import subprocess
import matplotlib as mpl
import matplotlib.pyplot as plt

figname = os.path.splitext(os.path.basename(__file__))[0]

# Default matplotlib setting
mpl.rc('axes.spines', top=False, right=False)
mpl.rc('font', size=10)
mpl.rc('figure', figsize=(100/2.54, 100/2.54), titlesize=12)
mpl.rc('axes', titlesize=12, labelsize=12)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)
mpl.rc('legend', fontsize=12)
mpl.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,

})
mpl.rcParams['text.latex.preamble'] = [
    r"\usepackage{sfmath, xcolor}",
    r"\usepackage[scaled=1]{helvet}",
    r"\usepackage{amsmath}",
    r"\renewcommand{\familydefault}{\sfdefault}"
]


def add_axes1(fig, lm, bm, rm, tm):
    """Helper function for adding axes using lm, bm, rm, hh
    """
    ww = rm - lm
    hh = tm - bm
    ax = fig.add_axes((lm, bm, ww, hh))
    return ax


def add_axes2(fig, lm, bm, width, height):
    """Helper function for adding axes using lm, rm, width, height 
    """
    ax = fig.add_axes((lm, bm, width, height))
    return ax


def compile_and_cleanup():
    """ Compile figures and remove tmp files
    """
    subprocess.run(['pdflatex', f'./{figname}.tex'])
    subprocess.run(['pdfcrop', f'./{figname}.pdf', f'./{figname}.pdf'])
    os.remove('./_tmp.pdf')
    for fl in glob.glob('./*.aux'):
        os.remove(fl)
    for fl in glob.glob('./*.log'):
        os.remove(fl)


def run(fig):
    """This is where the magic happens
    Use add_axes1 and add_axes2 to add axes to the fig
    """

    # Example figure
    ax = add_axes1(fig, lm=0.1, bm=0.87, rm=0.13, tm=0.9)
    x = np.linspace(0, 10, 1001)
    y = np.sin(x)
    ax.plot(x, y)
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")


if __name__ == '__main__':
    fig = plt.figure()
    run(fig)
    fig.savefig('_tmp.pdf', transparent=True)
    compile_and_cleanup()
