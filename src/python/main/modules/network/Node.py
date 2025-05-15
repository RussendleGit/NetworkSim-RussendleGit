from simpy import Environment
from modules.network.Link import Link
from modules.network.Packet import Packet

class Node:
  env: Environment
  name: str
  links: dict['Node', Link]
  def __init__(self, env: Environment, name: str) -> None:
    self.env = env
    self.name = name
    self.links = {}

  def add_link(self, other_node: 'Node', bandwidth: float) -> None:
    link: Link = Link(self.env, bandwidth)
    self.links[other_node] = link
  
  def send_packet(self, packet: Packet, next_hop: 'Node'):
    print(f"{self.name} sending packet to {next_hop.name} at {self.env.now}")
    link: Link = self.links[next_hop]
    self.env.process(link.transmit(packet))
    yield self.env.timeout(0)
  
  def __str__(self) -> str:
    return f"device: {self.name}"

  def __repr__(self) -> str:
    return f"device: {self.name}"