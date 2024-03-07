def solution(players, callings):
    answer = []
    index = {player: i for i, player in enumerate(players)}

    for calling in callings:
        idx = index[calling] 
        players[idx], players[idx-1] = players[idx-1], players[idx] 
        index[players[idx]] = idx
        index[players[idx-1]] = idx - 1

    answer = players
    return answer