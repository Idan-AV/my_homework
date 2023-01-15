import datetime


class Table:
    def __init__(self, table_id: int, seats_number: int, is_occupied: bool = False, reservation_time_limit: int = 0,
                 occupied_seats: int = 0,
                 reservation_start_time: datetime = 0):
        self._reservation_time_limit = reservation_time_limit
        self._reservation_start_time = reservation_start_time
        self._occupied_seats = occupied_seats
        self._is_occupied: bool = is_occupied
        self._seats_number = seats_number
        self._table_id = table_id

    def get_number_of_seats(self):
        return self._seats_number

    def get_table_id(self):
        return self._table_id

    def get_time_limit(self):
        return self._reservation_time_limit

    def is_available(self):
        if not self._is_occupied:
            return False
        return True

    def reserve_a_table(self, num_of_guests):
        if self.is_available() and num_of_guests > 0:
            self._is_occupied = True
            self._occupied_seats = num_of_guests
            self._reservation_start_time = datetime.datetime.now()

    def release_a_table(self):
        if not self._is_occupied:
            self._is_occupied = False
            self._occupied_seats = 0
            self._reservation_start_time = None

    @property
    def is_occupied(self):
        return self._is_occupied
