
class YuShuBook:

    isbn_url = "http://t.yushu.im/v2/book/isbn/{}"
    keyword_url = "http://t.yushu.im/v2/book/search?q={}&count={}&start={}"

    def search_by_isbn(self, isbn):
        YuShuBook.isbn_url.format(isbn)


    def search_by_keyword(self):
        pass