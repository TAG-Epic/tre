from tre import setup

from logging import getLogger, DEBUG

l = getLogger("tre")
setup(l)
l.setLevel(DEBUG)

l.debug("debug")
l.info("info")
l.warning("warn")
l.error("error")
l.critical("critical")
