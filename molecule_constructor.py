class Carbon:

    def __init__(self,carbon_number):
        self.carbon_number = carbon_number
        self.bond_1 = "Hydrogen"
        self.bond_2 = "Hydrogen"
        self.bond_3 = "Hydrogen"
        self.bond_4 = "Hydrogen"

class Nitrogen:
    def __init__(self):
        self.identifier = "Nitrogen"
        self.bond_1 = "Hydrogen"
        self.bond_2 = "Hydrogen"
        self.bond_3 = "Hydrogen"
class Oxygen:
    def __init__(self):
        self.identifier = "Oxygen"
        self.bond_1 = "Hydrogen"
        self.bond_2 = "Hydrogen"
class Flourine:
    def __init__(self):
        self.identifier = "Flourine"
        self.bond_1 = "Hydrogen"
class Bromine:
     def __init__(self):
         self.identifier = "Bromine"
         self.bond_1 = "Hydrogen"
    
        
        
class AliphaticCarbonSkeleton():
    
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

    def _get_linked(self,index):
        if index == self.length:
            return self.last
        if index == 0:
            return self.root
        if self.root == None:
            return print("No atoms to traverse")
        else:
            counter = 1
            tracker = self.root
            while counter != index:
                tracker = tracker.bond_2
                counter += 1
            return tracker
        
    def _substituent_insertion(self,carbon_number,substituent):
        if carbon_number <= 0 or carbon_number >= self.length:
            return print("Input a carbon number from the parent chain")
        if carbon_number == 1:
            return self.root
        if carbon_number == self.length:
            return self.last
        if self.root == None:
            return print("No atoms to traverse")
        new_node = substituent(carbon_number)
        return new_node 
    
    

    def carbon_insertion(self,carbon_number):
        int_carbon_number = int(carbon_number)
        new_carbon = Carbon(int_carbon_number)
        if carbon_number == 1: # edge case in which we are inserting the first carbon atom. Methane, is the only instance in which a carbon atom                
            if self.length == 0: # will have 4 hydrogen atoms arround it.
                self.root = new_carbon
                self.last = new_carbon
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
                #new_carbon.bond_2 = "Hydrogen"
        else:
            return print(f"Please input a number that follows sequential order, the carbon numeration is currently {self.sequence_tracker}")
        self.sequence_tracker.add(int_carbon_number)
        self.length += 1
        return print(f"{self.length} carbon atoms connected")


class Substituents(AliphaticCarbonSkeleton):

    def __init__(self):
        self.parent_branching = {}
        self.substituent_branching = {}
        super().__init__()

    def _parent_helper(self,carbon_number_string,new_substituent):
        self.parent_branching.setdefault(carbon_number_string,[])                          
        self.parent_branching[carbon_number_string].append(new_substituent.identifier) 
        
    def parent_substituent_insertion(self,carbon_number,substituent):           # There is a lot of repeated code in this class instance, ideas are being considered to ameliorate the issue 
        """This insertion can only be done on a carbon in the parent chain"""
        new_substituent = substituent()
        substituted_carbon = self._get_linked(carbon_number)
        carbon_number_string = f"Carbon number {substituted_carbon.carbon_number}" 
        if substituted_carbon.bond_1 == "Hydrogen":
            self._parent_helper(carbon_number_string,new_substituent)
            substituted_carbon.bond_1= new_substituent
            new_substituent.bond_1 = substituted_carbon
            return print(f"{new_substituent.identifier} connected to carbon number {substituted_carbon.carbon_number} bond number 1")
        if substituted_carbon.bond_2 == "Hydrogen":
            self._parent_helper(carbon_number_string,new_substituent)
            substituted_carbon.bond_2= new_substituent
            new_substituent.bond_1 = substituted_carbon
            return print(f"{new_substituent.identifier} connected to carbon number {substituted_carbon.carbon_number} bond number 2")
        if substituted_carbon.bond_3 == "Hydrogen":
            self._parent_helper(carbon_number_string,new_substituent)
            substituted_carbon.bond_3= new_substituent
            new_substituent.bond_1 = substituted_carbon
            return print(f"{new_substituent.identifier} connected to carbon number {substituted_carbon.carbon_number} bond number 3")
        if substituted_carbon.bond_4 == "Hydrogen":
            self._parent_helper(carbon_number_string,new_substituent)
            substituted_carbon.bond_4 = new_substituent
            new_substituent.bond_1 = substituted_carbon
            return print(f"{new_substituent.identifier} connected to carbon number {substituted_carbon.carbon_number} bond number 4")
        else:
            return print("Please enter a bond number that is not occupied by an R group")

    
    
           
            
x = Substituents()
        

























   


        
            
            

        
    
        
