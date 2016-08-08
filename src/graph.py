import networkx as nx
import matplotlib.pyplot as plt
U = ["u1", "u2", "u3", "u4"]
C = [26, 26, 26, 26]


class userAgent(nx.DiGraph):

    def __init__(self, U, C):
        super(userAgent, self).__init__()
        for i in range(len(U)):
            self.add_node(U[i], comfort=C[i])

    def condition_change(self, u, c):
        for i in self.nodes():
            if i is not u:
                if self.has_edge(i, u):
                    self.remove_edge(i, u)
                else:
                    self.add_edge(u, i)
        self.node[u]['comfort'] = c
        print(self.edges())

    def get_authority(self):
        return max((i[1], i[0]) for i in self.out_degree_iter())

    def get_dict(self):
        temp = {}
        for i in self.nodes(True):
            temp[i[0]] = i[1]

        return temp

    def add_user(self, u, c):
        self.add_node(u, comfort=c)

a = userAgent(U, C)

a.condition_change("u3", 27.5)
a.condition_change("u4", 27)
a.condition_change("u4", 27.5)
a.condition_change("u2", 27)
a.add_user("u5", 26)
pos = nx.spring_layout(a)

t = a.get_dict()
for i in t:
    t[i] = i
nx.draw(a, pos, node_size=800)
nx.draw_networkx_labels(a, pos, t, font_size=16)
plt.show()
