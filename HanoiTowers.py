#CODE BY ERMYS_CODE#

towers = [[], [], []]                                   #List with the representation of the towers using lists
currentMove = 1                                         #Will save the current movement number
pieceToMove = 0                                         #Will save the piece to move in the current movement
height = 0                                              #Will save the number of pieces on the game



class Piece():                                          #Piece object that contains the number of the piece
    def __init__(self, number):
        self.number = number



def GetPiece(move):                                     #Function that returns the piece to move on the current movement and where is this piece
    global towers
    
    pieceToMove = CalculatePieceToMove(move)            #Calls the CalculatePieceToMove function and is saved on pieceToMove

    for i in towers:                                    #Looks all the towers to find the pieceToMove
        for j in i:
            if j.number == pieceToMove:
                return j, towers.index(i)               #Return the piece to move and the tower where is at the moment



def CalculatePieceToMove(move):                         #Function that returns the number of the piece that will move on the current movement
    global height

    if move % 2 != 0:                                   #If the current movement is odd returns the highest number of the game
        return height
    else:                                               #If the current movement is even it calculate wich piece you have to move
        rest = 2
        div = 4
        toMove = height-1
        while True:
            result = (move - rest) % div                #It checks if the second highest piece is the piece taht you have to move
            if result == 0:                             #If the result of the operation is 0 returns the piece just checked
                return toMove
            rest *= 2                                   #If the result is not 0 multiply the operantion values by 2 and check the next piece
            div *= 2
            toMove -= 1



def CalculateStep(piece):                               #Function that returns how many towers the piece have to move
    if piece.number % 2 == 0:                           #If the piece to move number is even returns 1
        return 1
    else:                                               #If the piece to move number is odd returns 2
        return 2



def MovePiece(tower, steps, piece):                     #Function that move the pieces from a tower to another
    global towers

    towers[tower].remove(piece)                         #Removes the piece to move on the current movement from his current tower
    currentTower = tower                                #Saves the current tower index of the piece to move in a varoable
    nextTower = currentTower + steps                    #Calculate the index of the tower where the piece goes
    if nextTower > 2:                                   #If the index of the next towers is out of range substracts 3 to get it back to de range
        nextTower -= 3
    towers[nextTower].insert(0, piece)                  #Insert the current piece on index 0 in the correct tower



def DrawTowers():                                       #Function that prints the current state of the lists
    global towers

    print("\n-----------------------------\n\n")
    for i in range(len(towers)):
        print(f"Tower {i + 1}\n")
        for j in towers[i]:
            print("\t", j.number)



def Torre():                                            #Main function
    global currentMove
    global pieceToMove
    global towers
    global height

    if len(towers[2]) == height:                        #If the len of the last tower is equal to the height of the game the program ends 
        DrawTowers()                                    #Calls the DrawTowers function
        print("\nPerfect!!!")
    else:    
        DrawTowers()                                    #Calls the DraeTowers function
        pieceToMove, tower = GetPiece(currentMove)      #Calls the GetPiece function with the current move and save the value returned in pieceToMove and tower
        steps = CalculateStep(pieceToMove)              #Calls the CalculateSteps function with the pieceToMove and save the value returned in steps
        MovePiece(tower, steps, pieceToMove)            #Calls the MovePiece function with the tower, steps and pieceToMove

        currentMove += 1                                #Add 1 to the current move
        Torre()                                         #Calls the Torre fuction (itself)






height = int(input("Height of the tower: "))            #Ask for the height of the tower

for i in range(height):                                 #Add an object Piece with its number value in the first list on the index 0
    towers[0].insert(0,Piece(i + 1))

Torre()                                                 #Calls the Torre function