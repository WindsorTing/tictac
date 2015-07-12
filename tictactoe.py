# This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

#    Command Line Tic Tac Toe, by Windsor KC Ting July 2015

print "Command Line Tic Tac Toe!"
a = [0, 0, 0]
b = [0, 0, 0]
c = [0, 0, 0]
print a
print b
print c
print("Shown above is the board. As you can see, each spot on the board corresponds to a coordinate in a 3 x 3 matrix. For example, to place a marker on row 2, column 1, this position corresponds to an x coordinate of 2 and a y coordinate of 1.")
P1Name = raw_input('Player 1: Please enter your first name: ')
P2Name = raw_input('Player 2: Please enter your first name: ')
print("Okay. " + P1Name + " is denoted by the number 1.")
print(P2Name + ", you are denoted by the number 2.")
for i in range(0,10): 
  print "It is " + P1Name + "'s turn."
  x = input('Define X Coordinate: ')
  if x > 3 or x < 1: 
    x = input('Out of bounds! You have one more chance. Please enter a number between 1 and 3 corresponding to your desired x coordinate: ')
    if x > 3 or x < 1:
      print("Uh Oh. Sorry about that. " + P1Name + " has ended the game prematurely with two consecutive illegal entries. Please start the game again.")
      break
  y = input('Define Y Coordinate: ')
  if y > 3 or y < 1: 
    y = input('Out of bounds! You have one more chance. Please enter a number between 1 and 3 corresponding to your desired y coordinate: ')
    if x > 3 or x < 1:
      print("Uh Oh. Sorry about that. " + P1Name + " has ended the game prematurely with two consecutive illegal entries. Please start the game again.")
      break
  if y == 1:
    if a[x-1] == 0: 
      a[x-1] = 1
    else: 
      print("This move is not permitted! You will have to wait for your next turn")
  if y == 2:
    if b[x-1] == 0: 
      b[x-1] = 1
    else: 
      print("This move is not permitted! You will have to wait for your next turn")
  if y == 3:
    if c[x-1] == 0: 
      c[x-1] = 1
    else: 
      print("This move is not permitted! You will have to wait for your next turn")
  print a
  print b
  print c
  if a[0] == a[1] and a[1] == a[2] and a[2] == 1: 
    print(P1Name + " wins, across the first row!")
    break
  if a[0] == a[1] and a[1] == a[2] and a[2] == 2: 
    print(P2Name + " wins, across the first row!")
    break
  if b[0] == b[1] and b[1] == b[2] and b[2] == 1: 
    print(P1Name + " wins, across the second row!")
    break
  if b[0] == b[1] and b[1] == b[2] and b[2] == 2: 
    print(P2Name + " wins, across the second row!")
    break
  if c[0] == c[1] and c[1] == c[2] and c[2] == 1: 
    print(P1Name + " wins, across the third row!")
    break
  if c[0] == c[1] and c[1] == c[2] and c[2] == 2: 
    print(P2Name + " wins, across the third row!")
    break
  if a[0] == b[0] and b[0] == c[0] and c[0] == 1: 
    print(P1Name + " wins, down the first column!")
    break
  if a[0] == b[0] and b[0] == c[0] and c[0] == 2: 
    print(P2Name + " wins, down the first column!")
    break
  if a[1] == b[1] and b[1] == c[1] and c[1] == 1: 
    print(P1Name + " wins, down the second column!")
    break
  if a[1] == b[1] and b[1] == c[1] and c[1] == 2: 
    print(P2Name + " wins, down the second column!")
    break
  if a[2] == b[2] and b[2] == c[2] and c[2] == 1: 
    print(P1Name + " wins, down the third column!")
    break
  if a[2] == b[2] and b[2] == c[2] and c[2] == 2: 
    print(P2Name + " wins, down the second column!")
    break
  if a[0] == b[1] and b[1] == c[2] and c[2] == 1: 
    print(P1Name + " wins in the diagonal!")
    break
  if a[0] == b[1] and b[1] == c[2] and c[2] == 2: 
    print(P2Name + " wins in the diagonal!")
    break
  if a[2] == b[1] and b[1] == c[0] and c[0] == 1: 
    print(P1Name + " wins in the diagonal!")
    break
  if a[2] == b[1] and b[1] == c[0] and c[0] == 2: 
    print(P2Name + " wins in the diagonal!")
    break
  if a[0] != 0 and a[1] != 0 and a[2] != 0 and b[0] != 0 and b[1] != 0 and b[2] != 0 and c[0] != 0 and c[1] != 0 and c[2] != 0: 
    print("Cat's Game!")
    break
  print "It is " + P2Name + "'s turn."
  x = input('Define X Coordinate: ')
  if x > 3 or x < 1: 
    x = input('Out of bounds! You have one more chance. Please enter a number between 1 and 3 corresponding to your desired x coordinate: ')
    if x > 3 or x < 1:
      print("Uh Oh. Sorry about that. " + P2Name + " has ended the game prematurely with two consecutive illegal entries. Please start the game again.")
      break
  y = input('Define Y Coordinate: ')
  if y > 3 or y < 1: 
    y = input('Out of bounds! You have one more chance. Please enter a number between 1 and 3 corresponding to your desired y coordinate: ')
    if x > 3 or x < 1:
      print("Uh Oh. Sorry about that. " + P2Name + " has ended the game prematurely with two consecutive illegal entries. Please start the game again.")
      break
  if y == 1:
    if a[x-1] == 0: 
      a[x-1] = 2
    else: 
      print("This move is not permitted! Please wait for your next turn")
  if y == 2:
    if b[x-1] == 0: 
      b[x-1] = 2
    else: 
      print("This move is not permitted! Please wait for your next turn")
  if y == 3:
    if c[x-1] == 0: 
      c[x-1] = 2
    else: 
      print("This move is not permitted! Please wait for your next turn")    
  print a
  print b
  print c
  if a[0] == a[1] and a[1] == a[2] and a[2] == 1: 
    print(P1Name + " wins, across the first row!")
    break
  if a[0] == a[1] and a[1] == a[2] and a[2] == 2: 
    print(P2Name + " wins, across the first row!")
    break
  if b[0] == b[1] and b[1] == b[2] and b[2] == 1: 
    print(P1Name + " wins, across the second row!")
    break
  if b[0] == b[1] and b[1] == b[2] and b[2] == 2: 
    print(P2Name + " wins, across the second row!")
    break
  if c[0] == c[1] and c[1] == c[2] and c[2] == 1: 
    print(P1Name + " wins, across the third row!")
    break
  if c[0] == c[1] and c[1] == c[2] and c[2] == 2: 
    print(P2Name + " wins, across the third row!")
    break
  if a[0] == b[0] and b[0] == c[0] and c[0] == 1: 
    print(P1Name + " wins, down the first column!")
    break
  if a[0] == b[0] and b[0] == c[0] and c[0] == 2: 
    print(P2Name + " wins, down the first column!")
    break
  if a[1] == b[1] and b[1] == c[1] and c[1] == 1: 
    print(P1Name + " wins, down the second column!")
    break
  if a[1] == b[1] and b[1] == c[1] and c[1] == 2: 
    print(P2Name + " wins, down the second column!")
    break
  if a[2] == b[2] and b[2] == c[2] and c[2] == 1: 
    print(P1Name + " wins, down the third column!")
    break
  if a[2] == b[2] and b[2] == c[2] and c[2] == 2: 
    print(P2Name + " wins, down the second column!")
    break
  if a[0] == b[1] and b[1] == c[2] and c[2] == 1: 
    print(P1Name + " wins in the diagonal!")
    break
  if a[0] == b[1] and b[1] == c[2] and c[2] == 2: 
    print(P2Name + " wins in the diagonal!")
    break
  if a[2] == b[1] and b[1] == c[0] and c[0] == 1: 
    print(P1Name + " wins in the diagonal!")
    break
  if a[2] == b[1] and b[1] == c[0] and c[0] == 2: 
    print(P2Name + " wins in the diagonal!")
    break
  if a[0] != 0 and a[1] != 0 and a[2] != 0 and b[0] != 0 and b[1] != 0 and b[2] != 0 and c[0] != 0 and c[1] != 0 and c[2] != 0: 
    print("Cat's Game!")
    break
print("Game Over! Thanks for playing!") 

