"""Docstring"""

def convert_string_to_tuples(text_in):
  """Conv func!"""
  values = text_in.strip('()').split(', ')
  return (float(values[1]),float(values[0]))

def main():
    """Main func!"""
    laongdao_data = convert_string_to_tuples(input())
    print(laongdao_data)

main()
