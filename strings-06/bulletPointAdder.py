#! python3
import pyperclip
listStr = pyperclip.paste()
lists = listStr.split('\n')
for i in range(len(lists)):
    lists[i] = f'* {lists[i]}'
lists = '\n'.join(lists)
pyperclip.copy(lists)

# Lists of animals
# Lists of aquarium life
# Lists of biologists by author abbreviation
# Lists of cultivars
