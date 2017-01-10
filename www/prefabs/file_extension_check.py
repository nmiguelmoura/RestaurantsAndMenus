class File_extension_check:
    def __init__(self):
        pass

    def check(self, filename):
        ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def get_extension(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower()
