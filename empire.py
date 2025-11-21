import randomname

class Empire:
    name: str = ""
    
    def __ini__(self):
        self.name: str = "Test"
        
    def name_get(self):
        return self.name
    
    def name_set(self, name):
        self.name = name

# Generate a name using all available categories
print(randomname.get_name())

# Generate a name with specific categories
print(randomname.get_name(adj=('music_theory',), noun=('cats', 'food')))   
