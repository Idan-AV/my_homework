class Apartment:
    def __init__(self, address: str, parking_type: str, rooms_num: int, size_in_sq_meters: int, is_villa: bool,
                 monthly_municipal_tax: int, has_balcony: bool, floor: int, is_penthouse: bool, deal_state: str):
        self._deal_state = deal_state
        self._is_penthouse = is_penthouse
        self._floor = floor
        self._has_balcony = has_balcony
        self._monthly_municipal_tax = monthly_municipal_tax
        self._is_villa = is_villa
        self._size_in_sq_meters = size_in_sq_meters
        self._rooms_num = rooms_num
        self._address = address
        self._parking_type = parking_type

    def get_monthly_municipal_tax(self):
        return self._monthly_municipal_tax

    def get_size_in_sq_meters(self):
        return self._size_in_sq_meters

    def get_floor(self):
        return self._floor

    def get_address(self):
        return self._address

    def __str__(self):
        return f"the apartment is in {self.get_address()}"


class ApartmentForSale(Apartment):
    def __init__(self, address: str, parking_type: str, rooms_num: int, size_in_sq_meters: int, is_villa: bool,
                 monthly_municipal_tax: int, has_balcony: bool, floor: int, is_penthouse: bool, deal_state: str,
                 sale_price: int):
        super().__init__(address, parking_type, rooms_num, size_in_sq_meters, is_villa, monthly_municipal_tax,
                         has_balcony, floor, is_penthouse, deal_state)
        self._sale_price = sale_price
        self._agency_fee = 0

    def my_agency_fee(self):
        my_fee1 = (self._sale_price * 0.02)
        self._agency_fee += my_fee1
        return self._agency_fee

    def my_deal_state(self):
        if self._deal_state == "open":
            return True
        return False


class ApartmentForRent(Apartment):
    def __init__(self, address: str, parking_type: str, rooms_num: int, size_in_sq_meters: int, is_villa: bool,
                 monthly_municipal_tax: int, has_balcony: bool, floor: int, is_penthouse: bool, deal_state: str,
                 rent_price_per_month: int):
        super().__init__(address, parking_type, rooms_num, size_in_sq_meters, is_villa, monthly_municipal_tax,
                         has_balcony, floor, is_penthouse, deal_state)
        self.rent_price_per_month = rent_price_per_month
        self._agency_fee1 = 0

    def my_agency_fee2(self):
        my_fee2 = (self.rent_price_per_month * 0.02)
        self._agency_fee1 += my_fee2
        return self._agency_fee1

    def my_deal_state2(self):
        if self._deal_state == "open":
            return True
        return False


# if __name__ == '__main__':
    # a1 = ApartmentForRent("lod","Angle Parking",3,100,False,500,True,4,True,"open",3000 )
    # print(a1.my_agency_fee2())
    # print(a1.rent_price_per_month)
    # print(a1.my_deal_state2())
    # a=ApartmentForSale("lod","Angle Parking",3,100,False,500,True,4,True,"open",500000)
    # print(a.my_agency_fee())
    # print(a.my_deal_state())
