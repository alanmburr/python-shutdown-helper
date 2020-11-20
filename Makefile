PREFIX ?= /usr
MANDIR ?= $(PREFIX)/share/man

all:
	@echo Run \'sudo make install\' to install ShutdownHelper.

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
