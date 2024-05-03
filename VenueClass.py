class Venue:
    """A class that represents venues"""

    venue_count = 0

    # Constructor
    def __init__(self, name, address, contact, min_guests, max_guests):
        Venue.venue_count += 1
        self.venue_id = f"V{Venue.venue_count}"  # Generate venue ID automatically
        self.name = name
        self.address = address
        self.contact = contact
        self.min_guests = min_guests
        self.max_guests = max_guests

    # A function to print the details of a venue
    def __str__(self):
        return f"Venue ID: {self.venue_id}, Name: {self.name}, Address: {self.address}, Contact: {self.contact}, Min Guests: {self.min_guests}, Max Guests: {self.max_guests}"
