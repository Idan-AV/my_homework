from my_table import Table
import datetime


class TableReservationSystem:
    def __init__(self, restaurant_name: str, max_time_limit_to_occupy_a_table: int):
        self._max_time_limit_to_occupy_a_table = max_time_limit_to_occupy_a_table
        self._restaurant_name = restaurant_name
        self._my_tables: dict[int, Table] = {}

    def add_table(self, table_id: int, seat_number: int, is_occupied: bool):
        if table_id not in self._my_tables:
            return False
        your_table = Table(table_id, seat_number, is_occupied)
        self._my_tables[table_id] = your_table

    def get_available_tables(self, table_id: int):
        if table_id not in self._my_tables:
            return False
        my_table1 = self._my_tables.get(table_id)
        if not my_table1.is_occupied:
            return table_id, True
        # if self._my_tables[table_id][2]:
        #     return table_id, True

    def reserve_a_table(self, table_id: int, num_of_guests: int):
        if self.get_available_tables and num_of_guests > 0 and table_id in self._my_tables:
            my_table = self._my_tables.get(table_id)
            my_table._is_occupied = True
            my_table._occupied_seats = num_of_guests
            my_table._reservation_start_time = datetime.datetime.now()

            return my_table.get_table_id()

    def release_a_table(self, table_id: int):
        if table_id not in self._my_tables:
            return False

        if self.get_available_tables(table_id):
            my_table_2 = self._my_tables.get(table_id)
            my_table_2._is_occupied = False
            my_table_2.__occupied_seats = 0
            my_table_2._reservation_start_time = None
