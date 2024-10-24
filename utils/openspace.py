import random

from table import Seat, Table


class Openspace:
    def __init__(self, num_tables: int, seats_per_tables: int):
        """"""
        
        self.num_tables = num_tables
        self.tables_openspace: list = [Table(seats_per_tables) for _ in range(num_tables)]

    def setup_openspace(self, names: list) -> None:
        """"""

        random.shuffle(names)

        for name in names:
            seated = False
            for table in self.tables_openspace:
                if table.set_occupant_table(name):
                    seated = True
                    break
            
            if not seated:
                print(f"{name} could no be seated.")
        
    def __str__(self) -> str :
        """"""
        result = []
        for i, table in enumerate(self.tables_openspace, 1):
            result.append(f"Table {i}: {table}")
        return "\n".join(result)
    