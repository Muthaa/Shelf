import ebooklib
from ebooklib import epub

book = epub.read_epub('dragon bound.epub')

# for image in book.get_items_of_type(ebooklib.ITEM_IMAGE):
#     print(image)

for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
    print(item)