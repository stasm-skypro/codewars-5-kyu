"""ОПИСАНИЕ:
В этом упражнении вы укрепите свое мастерство паж-фу. Вы завершите класс
PaginationHelper, который является вспомогательным классом, полезным для
запроса сведений о разбиении по страницам, связанных с массивом.

Класс предназначен для приема массива значений и целого числа, указывающего,
сколько элементов будет разрешено на каждой странице. Типы значений,
содержащихся в коллекции/массиве, не имеют значения.

Ниже приведены некоторые примеры использования этого класса.
helper = PaginationHelper(['a','b','c','d','e','f'], 4)
helper.page_count() # should == 2
helper.item_count() # should == 6
helper.page_item_count(0) # should == 4
helper.page_item_count(1) # last page - should == 2
helper.page_item_count(2) # should == -1 since the page is invalid

# page_index takes an item index and returns the page that it belongs on
helper.page_index(5) # should == 1 (zero based index)
helper.page_index(2) # should == 0
helper.page_index(20) # should == -1
helper.page_index(-10) # should == -1 because negative indexes are invalid."""

from math import ceil


# TODO: complete this class

class PaginationHelper:

    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        return ceil(len(self.collection) / self.items_per_page)

    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index > self.page_count() -1 or page_index < 0:
            return -1
        return self.items_per_page - \
            ceil((((page_index + 1) * \
            self.items_per_page) % \
            self.item_count())%self.items_per_page)

    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index > self.item_count() - 1 or item_index < 0:
            return -1
        return ceil((item_index + 1) / self.items_per_page) - 1


# Test cases
collection = ['a','b','c','d','e','f']
helper = PaginationHelper(collection, 4)

assert(helper.page_count() == 2)  # page_count is returning incorrect value
assert(helper.item_count() == 6)  # item_count returned incorrect value

assert(helper.page_item_count(0) ==  4)  # page_item_count returned incorrect value for page_index 0
assert(helper.page_item_count(1) ==  2)  # page_item_count returned incorrect value for page_index 1
assert(helper.page_item_count(2) == -1)  # page_item_count returned incorrect value for page_index 2

assert(helper.page_index(  5) ==  1)  # page_index returned incorrect value for item_index 5
assert(helper.page_index(  2) ==  0)  # page_index returned incorrect value for item_index 2
assert(helper.page_index( 20) == -1)  # page_index returned incorrect value for item_index 20
assert(helper.page_index(-10) == -1)  # page_index returned incorrect value for item_index -10

empty = PaginationHelper([], 10)
assert(empty.item_count() == 0)  # item_count is returning incorrect value
assert(empty.page_count() == 0)  # page_count is returning incorrect value
assert(empty.page_index( 0) == -1)  # page_index(0) called when there was an empty collection
assert(empty.page_index( 1) == -1)  # page_index(1) called when there was an empty collection
assert(empty.page_index(-1) == -1)  # page_index(-1) called when there was an empty collection
assert(empty.page_item_count(0) == -1)  # page_item_count is returning incorrect value for page_index 0
assert(empty.page_item_count(1) == -1)  # page_item_count is returning incorrect value for page_index 1
assert(empty.page_item_count(-1) == -1)  # page_item_count is returning incorrect value for page_index -1