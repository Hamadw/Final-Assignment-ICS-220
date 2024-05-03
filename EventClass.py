class Event:
    """A class that represents events"""
    event_count = 0

    # Constructor
    def __init__(self, event_type, theme, date, time, duration, venue_address, client_id, guest_list, catering_company, cleaning_company, decorations_company, entertainment_company, furniture_supply_company, invoice):
        Event.event_count += 1
        self.event_id = f"E{Event.event_count}"  # Generate event ID automatically
        self.event_type = event_type
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venue_address = venue_address
        self.client_id = client_id
        self.guest_list = guest_list
        self.catering_company = catering_company
        self.cleaning_company = cleaning_company
        self.decorations_company = decorations_company
        self.entertainment_company = entertainment_company
        self.furniture_supply_company = furniture_supply_company
        self.invoice = invoice

    # A function to print the details of an event
    def __str__(self):
        return f"Event ID: {self.event_id}, Type: {self.event_type}, Theme: {self.theme}, Date: {self.date}, Time: {self.time}, Duration: {self.duration}, Venue Address: {self.venue_address}, Client ID: {self.client_id}, Guest List: {self.guest_list}, Catering Company: {self.catering_company}, Cleaning Company: {self.cleaning_company}, Decorations Company: {self.decorations_company}, Entertainment Company: {self.entertainment_company}, Furniture Supply Company: {self.furniture_supply_company}, Invoice: {self.invoice}"

    def set_event_id(self, id):
        self.event_id = id
