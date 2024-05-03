class Supplier:
    """Parent class representing a supplier"""
    supplier_count = 0


    def __init__(self, name, address, contact):
        Supplier.supplier_count += 1
        self.supplier_id = f"SP{Supplier.supplier_count}"  # Generate supplier ID automatically
        self.name = name
        self.address = address
        self.contact = contact

    def set_supplier_id(self, id):
        self.supplier_id = id



class Caterer(Supplier):
    """Subclass representing a caterer"""


    def __init__(self, name, address, contact, menu, min_guests, max_guests):
        super().__init__(name, address, contact)
        self.menu = menu
        self.min_guests = min_guests
        self.max_guests = max_guests


class Cleaner(Supplier):
    """Subclass representing a cleaner"""

    def __init__(self, name, address, contact, services):
        super().__init__(name, address, contact)
        self.services = services


class FurnitureSupplier(Supplier):
    """Subclass representing a furniture supplier"""

    def __init__(self, name, address, contact, available_items):
        super().__init__(name, address, contact)
        self.available_items = available_items


class DecorationSupplier(Supplier):
    """Subclass representing a decoration supplier"""

    decoration_count = 0

    def __init__(self, name, address, contact, available_decorations):
        super().__init__(name, address, contact)
        DecorationSupplier.decoration_count += 1
        self.decoration_id = f"DS{DecorationSupplier.decoration_count}"  # Generate decoration supplier ID automatically
        self.available_decorations = available_decorations
