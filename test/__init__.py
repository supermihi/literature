from os.path import abspath, join, dirname
from contextlib import contextmanager
import tempfile, shutil

from bibtexvcs import database


def datadir():
    return join(abspath(dirname(__file__)), 'data')



@contextmanager    
def tmpDatabase():
    tmpdir = tempfile.mkdtemp()
    newDir = join(tmpdir, 'btvcs')
    shutil.copytree(join(datadir(), 'sampleDB'), newDir)
    try:
        yield database.Database(newDir)
    finally:
        shutil.rmtree(tmpdir)

@contextmanager
def tmpClonedDatabase(source):
    tmpdir = tempfile.mkdtemp()
    newDir = join(tmpdir, 'btvcs')
    try:
        yield database.Database.cloneDatabase('mercurial', source, newDir)
    finally:
        shutil.rmtree(tmpdir)