text = input()

symbols_counts_as_dict = {}

for symbol in text:
    if symbol not in symbols_counts_as_dict:
        symbols_counts_as_dict[symbol] = 0
    symbols_counts_as_dict[symbol] += 1

for symbol, count in sorted(symbols_counts_as_dict.items()):
    print(f"{symbol}: {count} time/s")
