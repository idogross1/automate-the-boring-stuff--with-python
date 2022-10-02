# import pprint
# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# count = {}

# for c in message:
#     count.setdefault(c, 0)
#     count[c] = count[c]+1
# pprint.pprint(count)


# Define pieces and colors
pieces = ['king','queen','rook', 'knight','bishop', 'pawn']
colors = ['b', 'w']
# Set of all chess pieces
all_pieces = set(color+piece for piece in pieces for color in colors)
print(all_pieces)