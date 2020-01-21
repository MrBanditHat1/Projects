class Carbon:

    def __init__(self,carbon_number):
        self.carbon_number = carbon_number
        self.bond_1 = None
        self.bond_2 = None
        self.bond_3 = "Hydrogen"
        self.bond_4 = "Hydrogen"
        
        
class AliphaticCarbonSkeleton:
    
    """The sole responsibilty of this class is to construct an open, non-cyclic hyrdocarbon chain.
       We need not worry about substituents here, that will be defined in another class that would inherit from this one.
       Since it is an open chain, this lends itself very nicely for the implementation of a linked list. Later, when we
       add substituents, an undirected graph would perhaps be more appropriate.
    """
    
    def __init__(self):
        self.root = None
        self.last = None
        self.sequence_tracker = {0} #This set will assure a sequential order, with a O(1) with respect to insertion; since nothing is re-indexed.
        self.length = 0
        print(f"There are no carbon atoms present")
         

    def carbon_insertion(self,carbon_number):
        int_carbon_number = int(carbon_number)
        new_carbon = Carbon(int_carbon_number)
        if carbon_number == 1: # edge case in which we are inserting the first carbon atom. Methane, is the only instance in which a carbon atom                
            if self.length == 0: # will have 4 hydrogen atoms arround it.
                self.root = new_carbon
                self.last = new_carbon
                new_carbon.bond_1 = "Hydrogen"
                new_carbon.bond_2 = "Hydrogen"
                self.sequence_tracker.add(int_carbon_number)
                self.length += 1
                return print(f"There is 1 carbon atom present")
                         
        if carbon_number == len(self.sequence_tracker): # benefiting from the sequence_tracker attribute, the code following this conditional statement
                                                        # will only be ran if the user follows a sequential order in the numeration of carbon atoms.
            if self.length == 1:
                self.root.bond_2 = new_carbon
                new_carbon.bond_1 = self.root
                self.last = new_carbon
            elif self.length > 1:
                self.last.bond_2 = new_carbon
                new_carbon.bond_1 = self.last
                self.last = new_carbon
                new_carbon.bond_2 = "Hydrogen"
        else:
            return print(f"Please input a number that follows sequential order, the carbon numeration is currently {self.sequence_tracker}")
        self.sequence_tracker.add(int_carbon_number)
        self.length += 1
        return print(f"{self.length} carbon atoms connected")

        
    
            
            
x = AliphaticCarbonSkeleton()
            
        
        

























   


        
            
            

        
    
        
