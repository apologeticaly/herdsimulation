class Virus(object):
    '''Properties and attributes of the virus used in Simulation.'''

    def __init__(self, name, repro_rate, mortality_rate):
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate


def test_virus_instantiation():
    #TODO: Create your own test that models the virus you are working with
    '''Check to make sure that the virus instantiator is working.'''
    ebola = Virus("Ebola", 0.7, 0.25)
    assert ebola.name == "Ebola"
    assert ebola.repro_rate == 0.7
    assert ebola.mortality_rate == 0.25

    
if __name__ == "__main__":
    test_virus_instantiation()