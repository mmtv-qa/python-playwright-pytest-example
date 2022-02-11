class Page:

    def __init__(self, context, base_url: str):
        self._page = context.new_page()
        self._base_url = base_url
