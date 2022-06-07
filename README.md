<h1> 2048 </h1>

Game of 2048 is a popular game from Playstore which I recreated  using pygame Library from Python.

A simple game of 2048; it is composed of main game file "game_A" along with 1 class objects, logic_T, which contain all the actions occurring in the gamee and both objects, thee block for numbers and the arrays of Blocks.

<img width="350" heigth="350" alt="Screen Shot 2022-05-31 at 11 24 10 PM" src="https://user-images.githubusercontent.com/44034603/171325513-a3e603c8-5b2f-4e86-bbbd-2c56e4860290.png">

Features:
  =>Goal: The game end when user reach the 2048 number collectiion; the victory sign will be show in that case. 
  
<img width="350" heigth="350" alt="Screen Shot 2022-05-31 at 5 58 45 PM" src="https://user-images.githubusercontent.com/44034603/171327133-b66bb900-cc0c-4b42-80a3-4ce1cf6bbde6.png">

  
  =>Controls: The control of game are the keyboards buttons: Right, Left, Up and Down while also A, D, W, S respectively.
    There is an Undo button whhich is "RR keyboard"
    And there is an option of new game, that is the "TAB button"
    
<img width="450" heigth="350"  alt="Screen Shot 2022-06-01 at 12 14 26 AM" src="https://user-images.githubusercontent.com/44034603/171326295-a7ccfec2-7e7f-4e02-b341-650cb909e801.png">

    
   => Lose: The game automatically end when all blocks are fill and no conbination is possible; a sign of lose will be show in such case.

<img width="450" heigth="350" alt="Screen Shot 2022-06-01 at 1 23 34 AM" src="https://user-images.githubusercontent.com/44034603/171333650-813bc5b0-fa5f-4009-92a7-89248112a6ff.png">

===================================================

In case you wish to run in from teminal; you can run it with command 'python3 game_A.py"; however, the foldeer of image known as numbers, must bee ddiosplace from dist to pygame

The game was turn into an executable using the library pyinstaller; it can be run by acceding the folder pygame/dist, file game_A.exe.

