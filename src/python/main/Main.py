from simpy import Environment
from modules.network.IPV4 import IPV4
from modules.network.Node import Node
from modules.network.Network import generate_packets



if __name__ == "__main__":
  env: Environment = Environment()
  ipv4: IPV4 = IPV4()
  node: list[Node] = []
  for i in range(74): 
    node.append(Node(env, ipv4.add_ip_address()))
  print(node)

  node[52].add_link(node[12], 1000)
  node[12].add_link(node[52], 500)
  node[62].add_link(node[12], 500)
  
  env.process(generate_packets(env, node[52], node[62]))
  env.run(until=18)
