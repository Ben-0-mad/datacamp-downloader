import copyreg
import ssl

from colorama import init

from .session import Session

# use Colorama to make Termcolor work on Windows too
init()

active_session = Session.load()
datacamp = active_session.datacamp
# handle ssl saving issues
copyreg.pickle(ssl.SSLContext, lambda obj: (obj.__class__, (obj.protocol,)))
