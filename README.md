# Figure template (combination of gnuplot and tikz)

Compilation:

```sh
gnuplot -c template.gp
```

This will call pdflatex separately and compile everything into a final output `template.pdf`.
If you want to rename, you should rename both the `.gp` and `.tex` files so they keep the same name.

Usage `mkfig`:

```mkfig [figname]
```

to create `[figname].gp` and `[figname].tex` files in the working directory.  

Install `mkfig`:

```make install
``` 


Uninstall `mkfig`:

```make uninstall
``` 
 
