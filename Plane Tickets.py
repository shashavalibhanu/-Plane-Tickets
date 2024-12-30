
"""Functions to automate Conda airlines ticketing system."""
seat = ["A","B","C","D"]

def generate_seat_letters(number):
    for i in range(number):
        mod = i % 4
        yield seat[mod]
    
    
    
  
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start agaiean with A.

    Example: A, B, C, D

    """

    pass


def generate_seats(number):
    generate_seats = generate_seat_letters(number)
    row = 0
    for seats in generate_seats:
        if seats == "A":
            row +=1
        if row == 13:
            row += 1
        yield str(row)+seats
        
    
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    pass

def assign_seats(passengers):
    output = {}
    seat_list = generate_seats(len(passengers))
    for passenger in passengers:
        output[passenger]=next(seat_list)
    return output
        
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    pass

def generate_codes(seat_numbers, flight_id):
    for seat_number in seat_numbers:
        yield (seat_number + flight_id).ljust(12,'0')

    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    pass
