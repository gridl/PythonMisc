class Voter:
    def __init__(self,name):
        self.name = name
        self.voted_for = None


    def vote(self, politician):
        self.voted_for = politician
        politician.votes += 1


    def __str__(self):
        return self.name


class Politician:
    def __init__(self,name):
        self.name = name
        self.votes = 0

    def __str__(self):
        return self.name


macron = Politician('Macron')
jean = Voter('Jean')
jean.vote(macron)

print('%s voted for %s' %(jean, jean.voted_for))
print('%s received %d vote(s)' %(macron,macron.votes))