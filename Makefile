.PHONY: install
install: 
	chmod +x ./mkfig
	sudo ln -s -f `pwd`/mkfig /usr/local/bin/mkfig

.PHONY: clean
clean:
	sudo unlink /usr/local/bin/mkfig

.PHONY: uninstall
uninstall : clean
 



