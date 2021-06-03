# Lab Templates

## Gnuplot Figure template (combination of gnuplot and tikz)

Compilation:

```sh
gnuplot -c template.gp
```

This will call pdflatex separately and compile everything into a final output `template.pdf`.
If you want to rename, you should rename both the `.gp` and `.tex` files so they keep the same name.

Usage `mkfig`:

```sh
mkfig [figname]
```

to create `[figname].gp` and `[figname].tex` files in the working directory.  

Install `mkfig`:

```sh
make install
``` 


Uninstall `mkfig`:

```sh
make uninstall
``` 

## Python Figure template (combination of matplotlib and tikz)

Compilation:

```sh
python template.py
```

Usage `mkpyfig`:

```sh
mkpyfig [figname]
```

to create `[figname].py` and `[figname].tex` files in the working directory.  


# Talk template 

Compilation:

```sh
pdflatex slides.tex
```

This will call compile the slides.

Usage `mktalk`:

```sh
mktalk [talkname]
```

to create a folder [talkname] that contains `slides.tex` and `figs`

Install `mkfig` and `mktalk`:

```sh
make install
``` 


Uninstall `mkfig` and `mktalk`:

```sh
make uninstall
``` 
 
