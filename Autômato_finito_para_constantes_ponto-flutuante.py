def dfa(string, current, edges, accepting):
    if string == "":
        return current in accepting
    else:
        letter = string[0]
        remainder = string[1:]
        if (current, letter) in edges:
            newstate = edges[(current, letter)]
            return dfa(remainder, newstate, edges, accepting)
        return False

initial = 0
edges = {}

edges[(0,'+')] = 1
edges[(0,'-')] = 1

edges[(0,'0')] = 2
edges[(0,'1')] = 2
edges[(0,'2')] = 2
edges[(0,'3')] = 2
edges[(0,'4')] = 2
edges[(0,'5')] = 2
edges[(0,'6')] = 2
edges[(0,'7')] = 2
edges[(0,'8')] = 2
edges[(0,'9')] = 2
edges[(0,'.')] = 5

edges[(1,'0')] = 4
edges[(1,'1')] = 4
edges[(1,'2')] = 4
edges[(1,'3')] = 4
edges[(1,'4')] = 4
edges[(1,'5')] = 4
edges[(1,'6')] = 4
edges[(1,'7')] = 4
edges[(1,'8')] = 4
edges[(1,'9')] = 4

edges[(4,'0')] = 4
edges[(4,'1')] = 4
edges[(4,'2')] = 4
edges[(4,'3')] = 4
edges[(4,'4')] = 4
edges[(4,'5')] = 4
edges[(4,'6')] = 4
edges[(4,'7')] = 4
edges[(4,'8')] = 4
edges[(4,'9')] = 4
edges[(4,'.')] = 5

edges[(5,'0')] = 5
edges[(5,'1')] = 5
edges[(5,'2')] = 5
edges[(5,'3')] = 5
edges[(5,'4')] = 5
edges[(5,'5')] = 5
edges[(5,'6')] = 5
edges[(5,'7')] = 5
edges[(5,'8')] = 5
edges[(5,'9')] = 5

edges[(2,'0')] = 2
edges[(2,'1')] = 2
edges[(2,'2')] = 2
edges[(2,'3')] = 2
edges[(2,'4')] = 2
edges[(2,'5')] = 2
edges[(2,'6')] = 2
edges[(2,'7')] = 2
edges[(2,'8')] = 2
edges[(2,'9')] = 2
edges[(2,'.')] = 5


accepting = [5]

string = input()
print( dfa(string, initial, edges, accepting) )
