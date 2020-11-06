from app import app
@app.context_processor
def delete_extra():
    def _delete_extra(title, source):
        index = title.lower().find(source.partition(".")[0].lower())
        return title[0:index-2]
    return dict(delete_extra=_delete_extra)