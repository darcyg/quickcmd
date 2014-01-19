==========
 quickcmd
==========

------------------------------------------------------
Gives quick access to the commands defined in advance.
------------------------------------------------------

:Author: Grzegorz Krason <contact@krason.biz>
:Date:   2014-01-19
:Copyright: public domain
:Version: 1.0.0
:Manual section: 1
:Website: http://krason.biz/#quickcmd

SYNOPSIS
========

  quickcmd [-h] [-l] [-p] [-i] [-n N] [-c P] [--debug] [-V] [alias]

DESCRIPTION
===========

Gives quick access to the commands defined in advance. Each command can 
have own alias. Set of commands and aliases is defined in .quickcmd file
in your home directory.

OPTIONS
=======

positional arguments:
  alias             Exexute command specyfied by alias

optional arguments:
  -h, --help        show this help message and exit
  -l, --list        List available aliases
  -p, --stdout      Print command instead of executing
  -i, --insert      Edit command before execution
  -n N, --number N  Item number (applicable when more than one item
                    have the same alias)
  -c P, --config P  Config file; default is ~/.quickcmd
  --debug           Print whole call stack when exception occures
  -V, --version     Show version number and exit

KEY BINDINGS
============

::

               ARROW_UP         - select previous command
  alternative: k
               ARROW_DOWN       - select next command
  alternative: j

               PAGE_UP          - move selection to the previous group
  alternative: SHIFT+ARROW_UP
  alternative: SHIFT+k

               CTRL+C           - close application
  alternative: q

               RETURN           - close application and execute selected command
  alternative: x
               INSERT           - close application and type selected command
  alternative: i
               p                - close application and print selected command

               /                - turn on/off search mode
               e                - edit configuration file
               TAB              - switch view between aliases and commands
               v                - change layout between:
                                  1. All items and displayable comments
                                  2. No comments
                                  3. No comments, items are sorted


