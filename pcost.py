def porfolio_cost(filename: str) -> float:    
    total_cost: float = 0
    with open('Data/portfolio.dat','rb') as f:
        for line in f:
            try:
                split_line = line.split()
                shares: int = int(split_line[1])
                cost: float = float(split_line[2])
                total_cost += shares * cost
            except ValueError as e:
                print("Couldn't parse", line)
                print("Reason:", e)

    return total_cost    

if __name__ == '__main__':
    print(porfolio_cost('Data/portfolio3.dat'))