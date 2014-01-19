### Commented entries have reasonable defaults.
### Uncomment to edit them.
# Source: <source package name; defaults to package name>
# Section: misc
# Priority: optional
Homepage: http://www.krason.biz/#quickcmd
Standards-Version: 3.9.2

Package: quickcmd
Version: 1.0.0
Maintainer: Grzegorz Krason <contact@krason.biz>
# Pre-Depends: <comma-separated list of packages>
Depends: ttype (>= 1.0.0), python (>= 2.6)
# Recommends: <comma-separated list of packages>
# Suggests: <comma-separated list of packages>
# Provides: <comma-separated list of packages>
# Replaces: <comma-separated list of packages>
Architecture: all
# Copyright: <copyright file; defaults to GPL2>
# Changelog: <changelog file; defaults to a generic changelog>
Readme: README.Debian
# Extra-Files: <comma-separated list of additional files for the doc directory>
Files: ../bin/quickcmd /usr/bin
 ../man1/quickcmd.1.gz /usr/share/man/man1

Description: Gives quick access to the commands defined in advance
 Gives quick access to the commands defined in advance. Each
 command can have own alias. Set of commands and aliases is defined
 in .quickcmd file in your home directory.


