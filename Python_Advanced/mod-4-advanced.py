'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    15 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    relationship_status = list()
    
    from_member_profile = social_graph[from_member]
    if to_member in from_member_profile["following"]:
        relationship_status.append("follower")
    
    to_member_profile = social_graph[to_member]
    if from_member in to_member_profile["following"]:
        relationship_status.append("following")
        
    if "following" in relationship_status and "follower" in relationship_status:
        relationship_status.clear()
        relationship_status.append("friends")
    
    if not relationship_status:
        relationship_status = "no relationship"
    
    relationship_status = ''.join([str(x) for x in relationship_status])
    return (str(relationship_status))


def tic_tac_toe(board):
    '''Tic Tac Toe. 
    15 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    symbols = []
    for element in board:
        if type(element) is list:
            for i in element:
                symbols.append(i)
        
    symbols = list(set(symbols))
    
    if '' in symbols:
        symbols.remove('')
        
    first_player = symbols[0]
    second_player = symbols[1]
    blank = ''
    
    first_player_Wins = []
    second_player_Wins = []
    
    for i in board:
        if first_player in i and second_player not in i and blank not in i:
            first_player_Wins.append(first_player, "Horizontal")
        if second_player in i and first_player not in i and blank not in i:
            second_player_Wins.append(second_player, "Horizontal")
    
    if len(first_player_Wins) == 1:
        return first_player
    if len(second_player_Wins) == 1:
        return second_player
    
    first_player_Wins =[]
    second_player_Wins =[]
    
    currentCol = 0
    for c in board:
        for w in board:
            if first_player in w[currentCol]:
                first_player_Wins.append(first_player)
            if second_player in w[currentCol]:
                second_player_Wins.append(second_player)
            if len(first_player_Wins) == len(board):
                return first_player
            if len(second_player_Wins) == len(board):
                return second_player
        currentCol += 1
        first_player_Wins =[]
        second_player_Wins =[] 
    
    first_player_Wins =[]
    second_player_Wins =[]

    currentCol = 0

        for s in board:
            if first_player in s[currentCol]:
                first_player_Wins.append(first_player)
            if second_player in s[currentCol]: 
                second_player_Wins.append(second_player)
            currentCol += 1

        if len(first_player_Wins) == len(board):
            return first_player
        if len(second_player_Wins) == len(board):
            return second_player

        first_player_Wins =[]
        second_player_Wins =[]

        currentCol = len(board)-1
        for s in board:
            if first_player in s[currentCol]:
                first_player_Wins.append(first_player)
            if second_player in s[currentCol]: 
                second_player_Wins.append(second_player)
            currentCol -= 1

        if len(first_player_Wins) == len(board):
            return first_player
        if len(second_player_Wins) == len(board):
            return second_player
        if len(first_player_Wins) != len(board) and len(second_player_Wins) != len(board):
            return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    20 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see the sample data file in this same folder for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    currentStop = ""
    key = 0
    timeTotal = 0
    temp = [" "," "]
    
    if (first_stop,second_stop) in route_map:
        return route_map[(first_stop, second_stop)]["travel_time_mins"]
    else:
        while temp[1] != second_stop:
            temp = list(route_map.keys())[key]
            if temp[0] == first_stop and currentStop == "":
                timeTotal += route_map[temp]["travel_time_mins"]
            if temp[1] != second_stop and currentStop != "":
                timeTotal += route_map[temp]["travel_time_mins"]
            if temp[1] == second_stop:
                timeTotal += route_map[temp]["travel_time_mins"]
            currentStop = temp[1]
            key += 1
        return 