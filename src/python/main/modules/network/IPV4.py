class IPV4:
  addresses: list[str]
  values: list[int]
  def __init__(self) -> None:
    self.addresses = []
    self.values = [10, 0, 0, 0]

  def add_ip_address(self) -> str:
    new_ip: str = '.'.join(str(v) for v in self.values)
    self.addresses.append(new_ip)
    for i in range(len(self.values) -1, -1, -1):
      self.values[i] += 1
      if self.values[i] > 255:
        self.values[i] = 0
      else:
        break

    return new_ip