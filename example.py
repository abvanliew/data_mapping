from data_mapping import DataMapping
from dataclasses import dataclass

@dataclass
class Options( DataMapping ):
  a: str
  b: int
  DataValue: str | None = None

def use_properties_as_parameters( a: str, b: int, **_ ):
  print( f"{a}: {b}" )

def main():
  props = {
    "a": "test",
    "b": 55,
    "DataValue": "value"
  }
  options = Options( **props )
  use_properties_as_parameters( **options )
  print( options.DataValue )

if __name__ == "__main__": main()
