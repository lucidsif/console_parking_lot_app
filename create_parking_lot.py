class create_parking_lot(object):
    def __init__(self, numOfSlots):
        self.slots = []
        for num in range(numOfSlots):
            self.slots.append(False)
        print('Created a parking lot with %s slots' %(numOfSlots))

    def check_if_registration_unique(self, registration):
        for slot in self.slots:
            if isinstance(slot, dict) and slot['registration'] == registration:
                return False
        return True   

    def park(self, registration, color):
        isRegistrationUnique = self.check_if_registration_unique(registration)
        if isRegistrationUnique == False:
            return 'Sorry, that registration already exists in our lot.'
        try:
            closestSlotIdx = self.find_closest_spot()
            self.slots[closestSlotIdx] = {'registration': registration, 'color': color}
            return closestSlotIdx
        except TypeError:
            return 'Sorry, parking lot is full'

    def find_closest_spot(self):
        try:
            return self.slots.index(False)
        except ValueError:
            return 'No available spots'

    def leave(self, ticketNumber):
        self.slots[ticketNumber] = False
        return 'Slot number %s is free' %(ticketNumber)

    def registration_numbers_for_cars_with_color(self, color):
        return [slot.get('registration') for slot in self.slots if isinstance(slot, dict) and slot.get('color') == color]

    def slot_numbers_for_cars_with_color(self, color):
        slots = []
        currentIdx = 0
        while (currentIdx < len(self.slots)):
            currentSlot = self.slots[currentIdx]
            if (isinstance(currentSlot, dict) and currentSlot.get('color') == color):
                slots.append(currentIdx)
            currentIdx += 1
        return slots

    def slot_number_for_registration_number(self, registration):
        currentIdx = 0
        while (currentIdx < len(self.slots)):
            currentSlot = self.slots[currentIdx]
            if (isinstance(currentSlot, dict) and currentSlot.get('registration') == registration):
                return currentIdx
            else:
                currentIdx += 1
        return 'Not found'
    
    def status(self):
        filledSlots = []
        currentIdx = 0
        while(currentIdx < len(self.slots)):
            currentSlot = self.slots[currentIdx]
            if (isinstance(currentSlot, dict)):
                vehicleInformation = {
                    'slot': currentIdx,
                    'registration': currentSlot['registration'],
                    'color': currentSlot['color']
                }
                filledSlots.append(vehicleInformation)
            currentIdx += 1
        return filledSlots


