from simpy import Environment, Store, Event
from typing import Generator
from modules.network.Packet import Packet

class Link:
  env: Environment
  bandwidth: float
  queue: Store
  def __init__(self, env: Environment, bandwidth: float) -> None:
    self.env = env
    self.bandwidth = bandwidth
    self.queue = Store(env)

  def transmit(self, packet: Packet) -> Generator[Event, float, None]:
    tranmission_time: float = packet.data_size * 8 / self.bandwidth
    yield self.env.timeout(tranmission_time)
    print(f"Packet transmited from {packet.source_name} to {packet.destination_name} in {tranmission_time:.2f} seconds")
