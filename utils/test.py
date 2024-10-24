
from table import Seat, Table
from openspace import Openspace

def test_openspace():
    openspace = Openspace(num_tables=3, seats_per_tables=4)
    
    names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]

    openspace.setup_openspace(names)
    print("\nFinal state:")
    print(openspace)

test_openspace()
