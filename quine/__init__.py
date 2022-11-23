from base64 import b64encode

def _embed(source):
    """
    Inserts the given source code into the quine template, returning the source
    for the 'quined' program.
    """
    tmp_source = """import base64
b64source = '{}'
__source__ = base64.b64decode(b64source).replace('%', b64source, 1)

{}"""
    inner = tmp_source.format('%', source)
    b64inner = b64encode(inner)
    return tmp_source.format(b64inner, source)

def quinefy(old_filename, new_filename):
    """
    Converts a file into a quine version of itself. This process adds a new
    global variable declaration, __source__, which contains the entire source
    of the program as a string.

    Only a (large) header is added to the file, the rest of the source is left
    untouched.
    """
    with open(old_filename) as old_file:
        source = old_file.read()

    with open(new_filename, 'w') as new_file:
        new_file.write(_embed(source))

if __name__ == '__main__':
    quinefy('hello_world.py', 'hello_quine.py')
