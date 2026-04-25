def save_items(filename, items):
    with open(filename, 'w') as file:
        for item in items:
            file.write(item.get_detials() + "\n")

def load_items(filename):
    try:
        with open(filename, 'r') as file:
            return file.readlines()
        
    except FileNotFoundError:
        return "No data found"