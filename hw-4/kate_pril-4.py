class PaginationHelper:
    collection = []
    items_per_page = 0

    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        tmp = self.item_count() // self.items_per_page
        if self.item_count() % self.items_per_page == 0:
            return tmp
        else:
            return tmp + 1

    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index >= self.page_count() or page_index < 0:
            return -1
        elif page_index < self.page_count() - 1:
            return self.items_per_page
        elif self.item_count() % self.items_per_page == 0:
            return self.items_per_page
        else:
            return self.item_count() - ((self.item_count() // self.items_per_page) * self.items_per_page)

    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index >= self.item_count() or item_index < 0:
            return -1
        elif item_index < self.items_per_page:
            return 0
        else:
            return item_index // self.items_per_page
