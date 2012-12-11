#! usr/bin/env python

from code import pacman
import sys
from code import editor
if '-editor' in sys.argv:
    editor.main()
else:
    pacman.main()
