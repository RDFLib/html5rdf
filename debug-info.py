
import platform
import sys


info = {
    "impl": platform.python_implementation(),
    "version": platform.python_version(),
    "revision": platform.python_revision(),
    "maxunicode": sys.maxunicode,
    "maxsize": sys.maxsize
}

search_modules = ["chardet", "genshi", "html5rdf", "lxml"]
found_modules = []

for m in search_modules:
    try:
        __import__(m)
    except ImportError:
        pass
    else:
        found_modules.append(m)

info["modules"] = ", ".join(found_modules)


print("""html5rdf debug info:

Python %(version)s (revision: %(revision)s)
Implementation: %(impl)s

sys.maxunicode: %(maxunicode)X
sys.maxsize: %(maxsize)X

Installed modules: %(modules)s""" % info)
