"""Docstring"""
def main():
    """We do taxes we pay taxes."""
    earnings = int(input())
    tax = 0

    if earnings <= 150000:
        tax = 0
    elif earnings <= 300000:
        tax = (earnings - 150000) * 0.05
    elif earnings <= 500000:
        tax = (earnings - 300000) * 0.10 + 150000 * 0.05
    elif earnings <= 750000:
        tax = (earnings - 500000) * 0.15 + 200000 * 0.10 + 150000 * 0.05
    elif earnings <= 1000000:
        tax = (earnings - 750000) * 0.20 + 250000 * 0.15 + 200000 * 0.10 + 150000 * 0.05
    elif earnings <= 2000000:
        tax = (earnings - 1000000) * 0.25 + 250000 * 0.20 + 250000 * 0.15 + 200000 * 0.10 \
              + 150000 * 0.05
    elif earnings <= 4000000:
        tax = (earnings - 2000000) * 0.30 + 1000000 * 0.25 + 250000 * 0.20 + 250000 * 0.15 \
              + 200000 * 0.10 + 150000 * 0.05
    else:
        tax = (earnings - 4000000) * 0.35 + 2000000 * 0.30 + 1000000 * 0.25 + 250000 * 0.20 \
              + 250000 * 0.15 + 200000 * 0.10 + 150000 * 0.05

    print(int(tax))

main()
