"""Docstung"""

def main():
    "Main func!"
    h = int(input())
    m = int(input())
    m_angle = m * 6.0
    h_angle = (h % 12) * 30.0 + m * 0.5
    diff = (h_angle - m_angle) % 360.0
    print("True" if 0 <= diff < 6.0 else "False")

main()
