from lab11_items import Book , Magazine

from file_handler import save_items, load_items

from iterator_utils import LibraryIterator, search_items

def main():
    items = [Book("ABC", "J K STAINER"), Book("AI news", "American express"), Magazine("Tech world", 101)]

    print("Library Items: ")
    iterator = LibraryIterator(items)

    for item in iterator:
        print(item.get_detials())

        save_items("library.txt", items)

    data = load_items("library.txt")

    for line in data:
        print(line.strip())

    results = search_items("python", items)

    for item in results:
        print(item.get_detials())


if __name__ == "__main__":
    main()

    