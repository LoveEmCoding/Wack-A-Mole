import random

def prettyprintgrid(grid):
    row = 0
    print " 0 1 2 3 4"
    for line in grid:
        print row,
        row +=1
        for point in line:
            print point,
        print""

def straightdistance (r1, c1, r2, c2):
    rdiff = r1 - r2
    cdiff = c1 - c2

    rdiff = abs(rdiff)
    cdiff = abs(cdiff)

    if rdiff > cdiff:
        return rdiff
    else:
        return cdiff

grid = []

mugr = random.randint(0,4)
mugc = random.randint(0,4)

lives = 5

#construct the grid
for i in range(0,5):
    grid.append(['.','.','.','.','.'])


#game loop
while lives > 0:
    prettyprintgrid(grid)
    print "lives", lives

    row = raw_input("Row: ")
    row = int(row)
    col = raw_input("Col: ")
    col = int(col)

    if row == mugr and col == mugc:
         grid[row][col] = 'O'
        print"Congrats!You won and found the mugwamp! You are safe from being haunted by him."
        break

    else:
        grid[row][col] = 'x'
        print "You hear digging ",straightdistance(row, col, mugr, mugc), "tile/s away."
        lives -=1

        if lives == 0:
            print"You lost.He will haunt you for the rest of your life untill you win this game"
    
