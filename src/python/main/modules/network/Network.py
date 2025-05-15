from simpy import Environment
from random import randint, uniform
from modules.network.Node import Node
from modules.network.Packet import Packet

def generate_packets(
    env: Environment, 
    node: Node, 
    destination: Node, 
    rand_packet_size_scale: tuple[float, float] = (100.0, 1000.0), 
    timeout_scale: tuple[int, int] = (1, 5),
    iterator: int = 5
    ):
  for i in range(iterator): # type: ignore
    packet: Packet = Packet(uniform(rand_packet_size_scale[0], rand_packet_size_scale[1]), node.name, destination.name)
    env.process(node.send_packet(packet, destination))
    yield env.timeout(randint(timeout_scale[0], timeout_scale[1]))
