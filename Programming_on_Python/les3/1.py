def make_averager(accumulation_period: int) -> Callable[[float], float]:
    n = accumulation_period
    s = 0 # Sum of all numbers
    avg = 0 # Average of first n numbers
    elements = []
    def get_avg(p):
        nonlocal elements, s, avg
        elements.append(p)
        s += p
        length = len(elements)
        if length > n:
            avg = avg - elements[length - 1 - n] / n + (p / n)
        else:
            avg = s / length
        return avg
    return get_avg

def make_averager(accumulation_period: int) -> Callable[[float], float]:
    actions=list()
    avg,sm=0,0
    def get_avg(now:int):
        nonlocal actions, avg, sm
        actions.append(now)
        sm+=now
        ln=len(actions)
        if len(actions)>accumulation_period:
            avg=avg-actions[ln-accumulation_period-1]/accumulation_period+(now/accumulation_period)
        else:
            avg=sm/ln
        return avg
    return get_avg