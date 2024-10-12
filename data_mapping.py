from collections.abc import Mapping
from dataclasses import dataclass

@dataclass
class DataMapping( Mapping ):
  def __len__( self ): return self.__dict__.__len__()
  def __getitem__( self, key: str ): return self.__dict__.__getitem__( key )
  def __iter__( self ): return self.__dict__.__iter__()