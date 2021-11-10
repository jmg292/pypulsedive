class Comments(object):

    FIELD_MAP = {
        "cid": "cid",
        "comment": "comment",
        "stamp_added": "stamp_added",
        "stamp_updated": "stamp_updated",
        "title": "title",
        "uid": "uid",
        "username": "username"
    }

    def __init__(self):
        self.cid = ""
        self.comment = ""
        self.stamp_added = ""
        self.stamp_updated = ""
        self.title = ""
        self.uid = ""
        self.username = ""

    @staticmethod
    def from_dictionary(comments_dict: dict):
        comments = Comments()
        field_map = getattr(comments.__class__, "FIELD_MAP")
        for key_name in field_map:
            if key_name in comments_dict:
                setattr(comments, field_map[key_name], comments_dict[key_name])
        return comments