from TypingMatrix import SingleTyping
import numpy as np
class DualTyping(SingleTyping):
    def __init__(self, typings, scaling, defense):
        SingleTyping.__init__(self)
        self.rankings = []
        self.typings = typings
        self.scaling = scaling
        self.defense = defense
        self.offense = 1-defense
        total = 1
        for i in range(typings):
            total = total * (18-i)
        self.outgoing = np.empty([total, 18])
        self.incoming = np.empty([18, total])
        self.dualtypes = []
        self.count = 0
    def createMatrix(self):
        i = 0
        while i < len(self.pokemon_sorted):
            j = i+1
            while j < len(self.pokemon_sorted):
                newtype = self.pokemon_sorted[i] + " " + self.pokemon_sorted[j]
                self.dualtypes.append(newtype)
                new_outgoing, new_incoming = self.populateMatrix(i, j)
                score = self.calculateScore(new_outgoing, new_incoming)
                self.outgoing[self.count,:] = new_outgoing
                self.incoming[:,self.count] = new_incoming
                self.rankings.append([newtype, score])
                j+=1
            i+=1


    def populateMatrix(self, first, second):
        first_outgoing = self.damage_sorted[first,:]
        first_incoming = self.damage_sorted[:,first]
        second_outgoing = self.damage_sorted[second,:]
        second_incoming = self.damage_sorted[:, second]
        new_outgoing = np.multiply(first_outgoing, second_outgoing)
        new_incoming = np.multiply(first_incoming, second_incoming)
        return new_outgoing, new_incoming
    def calculateScore(self, outgoing, incoming):
        i = 0
        score = 0
        j = 0
        while i < len(outgoing):
            score += self.offense * outgoing[i] * (1 - i * 1/self.scaling)
            i+=1
        incoming = incoming.T
        while j < len(incoming):
            score -= self.defense*incoming[j] * (1 - j * 1/self.scaling)
            j+=1
        return score

test = DualTyping(2, 30, 1)
test.createMatrix()
print("Worst Typings\n")
print(sorted(test.rankings, key = lambda x: x[1])[0:10])
print("Best Typings \n")
print(sorted(test.rankings, key = lambda x: x[1])[-10:])