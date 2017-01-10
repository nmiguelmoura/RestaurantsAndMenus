class File_extension_check:
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

    def __init__(self):
        pass

    def check(self, filename):

        return '.' in filename and filename.rsplit('.', 1)[1].lower() in self.ALLOWED_EXTENSIONS

    def get_extension(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower()

    def get_available_extensios(self):
        return self.ALLOWED_EXTENSIONS
