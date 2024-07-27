# 19 July 2024

"""
def set_num_agents_from_file(self):
    pass

def create_network_from_file(self):
    with open("network.txt", 'r') as file:
        for line in file:
            line = line.split(",")
            buyer_ID = int(line[0])
            seller_ID = line[1:]

            seller_ID = [int(i) for i in seller_ID]

            buyer = self.agents_lists[buyer_ID]

            for ID in seller_ID:
                seller = self.agents_list[ID]

                buyer.incoming_links.append(ID)
                seller.outgoing_links.append(buyer_ID)
"""