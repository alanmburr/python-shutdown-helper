PREFIX ?= /usr
MANDIR ?= $(PREFIX)/share/man

all:
	@echo Run \'sudo make install\' to install ShutdownHelper.
	
download:
	@mkdir -p $HOME/Downloads/shutdown-helper
	@curl https://raw.githubusercontent.com/wackyblackie/python-shutdown-helper/master/LICENSE >> $HOME/Downloads/shutdown-helper/LICENSE
	@curl https://raw.githubusercontent.com/wackyblackie/python-shutdown-helper/master/gtk.py >> $HOME/Downloads/shutdown-helper/gtk.py
	@curl https://raw.githubusercontent.com/wackyblackie/python-shutdown-helper/master/shutdown-helper.1.gz >> $HOME/Downloads/shutdown-helper/shutdown-helper.1.gz
	@curl https://raw.githubusercontent.com/wackyblackie/python-shutdown-helper/master/shutdown-helper.8.gz >> $HOME/Downloads/shutdown-helper/shutdown-helper.8.gz
	@curl https://raw.githubusercontent.com/wackyblackie/python-shutdown-helper/master/tk.py >> $HOME/Downloads/shutdown-helper/tk.py
	@echo "Finished downloading files. Run 'sudo make install' to install them."

install:
	@mkdir -p $(DESTDIR)$(PREFIX)/bin
	@cp -p gtk.py $(DESTDIR)$(PREFIX)/bin/shutdown-helper
	@chmod 755 $(DESTDIR)$(PREFIX)/bin/shutdown-helper
	@cp -p shutdown-helper.1.gz $(DESTDIR)$(MANDIR)/man1/shutdown-helper.1.gz
	@cp -p shutdown-helper.8.gz $(DESTDIR)$(MANDIR)/man8/shutdown-helper.8.gz

uninstall:
	@rm -rf $(DESTDIR)$(PREFIX)/bin/shutdown-helper
	@echo Not deleting manpage.
	@echo To delete manpage, run \'sudo rm -f /usr/share/man/man8/shutdown-helper.8.gz /usr/share/man/man1/shutdown-helper.1.gz\' 
	
	
remove:
	@rm -f $(DESTDIR)$(PREFIX)/bin/shutdown-helper
	@rm -f $(DESTDIR)$(MANDIR)/man1/shutdown-helper.1.gz
	@rm -f $(DESTDIR)$(MANDIR)/man8/shutdown-helper.8.gz
