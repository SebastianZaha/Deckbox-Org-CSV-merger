class DeckboxCardEntry:
    name = ""
    edition = ""
    cardNumber = ""
    condition = ""
    language = ""
    foil = ""
    signed = ""
    artistProof = ""
    alteredArt = ""
    misprint = ""
    promo = ""
    textless = ""
    myprice = ""
    type = ""
    cost = ""
    rarity = ""
    price = ""
    imageUrl = ""

    def __init__(self, name, edition, cardNumber, condition,
                 language, foil, signed, artistProof, alteredArt,
                 missprint, promo, textless, myPrice,
                 type, cost, rarity, price, imageUrl):
        self.name = name
        self.edition = edition
        self.cardNumber = cardNumber
        self.condition = condition
        self.language = language
        self.foil = foil
        self.signed = signed
        self.artistProof = artistProof
        self.alteredArt = alteredArt
        self.misprint = missprint
        self.price = promo
        self.textless = textless
        self.myPrice = myPrice
        self.type = type
        self.cost = cost
        self.rarity = rarity
        self.price = price
        self.imageUrl = imageUrl


    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False
    def __ne__(self, other):
        return not self.__eq__(other)

    def __iter__(self):
        for each in self.__dict__.keys():
            yield self.__getattribute__(each)

    def __str__(self):
        return self.__dict__.__str__()

    def __hash__(self):
        return hash(tuple(self))
