
class Component:
    def to_dict(self):
        if self.children is not None:
            children = [c.to_dict() for c in self.children]
        else:
            children = None
        return {
            'elementName': self.elementName,
            'attributes': self.attributes,
            'children': children,
        }

class Card(Component):

    def __init__(self, attributes, *children):
        self.elementName = 'Card'
        self.attributes = attributes
        self.children = children

class CardHeader(Component):

    def __init__(self, attributes):
        self.elementName = 'CardHeader'
        self.attributes = attributes
        self.children = None


class CardsView:
    def __init__(self, attributes, *children):
        self.children = children

    def to_dict(self):
        return {
            'view': {'type': 'CARDS'},
            'result': [c.to_dict() for c in self.children],
        }
