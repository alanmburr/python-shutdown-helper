PREFIX ?= /usr
MANDIR ?= $(PREFIX)/share/man

all:
	@echo Run \'sudo make install\' to install ShutdownHelper.

install:
	@mkdir -p $(DESTDIR)$(PREFIX)/bin
	@cp -p python-shutdown-helper.py $(DESTDIR)$(PREFIX)/bin/python-shutdownhelper
  @touch $(DESTDIR)$(PREFIX)/bin/shutdownhelper
  @sed -i 2a"# Run ShutdownHelper in python3 correctly\npython3 -u /usr/bin/python-shutdownhelper\n" $(DESTDIR)$(PREFIX)/bin/shutdownhelper
	@chmod 755 $(DESTDIR)$(PREFIX)/bin/shutdownhelper

uninstall:
	@rm -rf $(DESTDIR)$(PREFIX)/bin/python-shutdownhelper
	@rm -rf $(DESTDIR)$(PREFIX)/bin/shutdownhelper
