'''
Files to implement / support backend server
'''

from importlib import metadata

from lang_server.chain_factory import get_chain

try:
    __version__ = metadata.version(__package__)
except metadata.PackageNotFoundError:
    # Case where package metadata is not available.
    __version__ = ""

__all__ = [__version__, "get_chain"]
