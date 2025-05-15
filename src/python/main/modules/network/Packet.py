class Packet:
  data_size: float
  source_name: str
  destination_name: str
  
  def __init__(self, data_size: float, source_name: str, destination_name: 'str') -> None:
    self.data_size = data_size
    self.source_name = source_name
    self.destination_name = destination_name