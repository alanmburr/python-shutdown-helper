PREFIX ?= /usr
MANDIR ?= $(PREFIX)/share/man

all:
	@echo Run \'sudo make install\' to install ShutdownHelper.

install:
	@mkdir -p $(DESTDIR)$(PREFIX)/bin
	@cp -p gtk.py $(DESTDIR)$(PREFIX)/bin/shutdownhelper
	@chmod 755 $(DESTDIR)$(PREFIX)/bin/shutdownhelper
	@cp -p shutdown-helper.1.gz $(MANDIR)/man1/shutdown-helper.1.gz

uninstall:
	@rm -rf $(DESTDIR)$(PREFIX)/bin/python-shutdownhelper
	@rm -rf $(DESTDIR)$(PREFIX)/bin/shutdownhelper
	@echo Not deleting manpage.
	@echo To delete manpage, run \'sudo rm -f /usr/share/man/man1/shutdown-helper.1.gz\'
	
	
remove:
	@rm -rf $(DESTDIR)$(PREFIX)/bin/python-shutdownhelper
	@rm -rf $(DESTDIR)$(PREFIX)/bin/shutdownhelper
	@rm -f $(MANDIR)/man1/shutdown-helper.1.gz
