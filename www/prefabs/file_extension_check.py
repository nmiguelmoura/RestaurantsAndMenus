class File_extension_check:
    '''Class that checks for file extension against a list of allowed ones.'''

    # List of allowed extensions.
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

    def __init__(self):
        pass

    def check(self, filename):
        # Check if filename extensions is allowed.
        # As seen in flask docs
        # (http://flask.pocoo.org/docs/0.12/patterns/fileuploads/).
        return '.' in filename and filename.rsplit('.', 1)[
                                       1].lower() in self.ALLOWED_EXTENSIONS

    def get_extension(self, filename):
        # Return the extension of a file.
        return '.' in filename and filename.rsplit('.', 1)[1].lower()

    def get_available_extensios(self):
        # Return a list of available extensions.
        return self.ALLOWED_EXTENSIONS
