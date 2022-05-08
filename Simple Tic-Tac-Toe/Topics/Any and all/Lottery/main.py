# As luck would have it
tickets = [11, 22, 33, 44, 55]
min_win_tickets = 44
winning_tickets = [i >= min_win_tickets for i in tickets]
tickets_bool = any(winning_tickets)