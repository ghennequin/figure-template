.PHONY: install
install: 
	chmod +x ./mkfig
	chmod +x ./mktalk
	sudo ln -s -f `pwd`/mkfig /usr/local/bin/mkfig
	sudo ln -s -f `pwd`/mktalk /usr/local/bin/mktalk

.PHONY: clean
clean:
	sudo unlink /usr/local/bin/mkfig
	sudo unlink /usr/local/bin/mktalk

.PHONY: uninstall
uninstall : clean
 



