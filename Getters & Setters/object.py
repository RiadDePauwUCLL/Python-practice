class Attractie:
    def __init__(self, naam, grootte):
        self.naam = naam
        self.grootte = grootte
        self.bezoekers = 0

    @property
    def naam(self):
        return self._naam
    
    @naam.setter
    def naam(self, nieuwe_naam):
        if not nieuwe_naam:
            raise ValueError('Naam kan niet leeg zijn')
        self._naam = nieuwe_naam
    
    @property
    def grootte(self):
        return self._grootte
    
    @grootte.setter
    def grootte(self, nieuwe_grootte):
        if not nieuwe_grootte:
            raise ValueError('Mag niet leeg zijn en/of kleiner dan 130')
        else:
            self._grootte = nieuwe_grootte
            
    def info(self):
        print(f"De naam is {self._naam} en grootte is {self._grootte}")

attractie = Attractie('QSDSQdSQD', '')
attractie.info()
attractie.grootte()