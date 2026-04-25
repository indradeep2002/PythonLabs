class LibraryIterator:

    def __init__(self, items):
        self._items = items 

        self._index = 0


    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index < len(self._items):
            item = self._items[self._index]
            self._index += 1 
            return item 
        
        else: 
            raise StopIteration
        

def search_items(keyword, items):
    for item in items:
        if keyword.lower() in item.get_details().lower():
            yield item 

