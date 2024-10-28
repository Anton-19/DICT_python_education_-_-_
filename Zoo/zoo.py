print("I love animals!")
print("Let's check out the animals...")
print("The deer looks fine.")
print("The lion looks healthy.")

camel = r"""
Camel habitat in the desert
 ___.-''''-.
/___  @    |
',,,,.     |         _.'''''''._
     '     |        /           \
     |     \    _.-'             \
     |      '.-'                  '-.
     |                               ',
     |                                '',
      ',,-,                           ':;
           ',,| ;,,                 ,' ;;
              ! ;!''!,',',,,,'!''!; ;   ;:
            : ;      ! !      ! !  ; ;   :;
          ; ;       ! !       ! !   ; ;   ,,
         ; ;        ! !      ! !    ; ;
        ; ;         ! !      ! !     ; ;
        ;,,         ! !     ! !      ; ;
        /_I         _L_I_   L_I_     L_I_
Look at that!
"""

print(camel)

lion = r"""
The lion habitat Savannah
                                   ,w.
                                 ,YWMMw  ,M  ,
                    _.---.._   __..---._.'MMMMMw,wMWmW,
               _.-""        '''           YP"WMMMMMMMMMb,
            .-' __.'                   .'     MMMMW^WMMMM;
    _,        .'.-'"; `,       /`     .--""      :MMM[==MWMW^;
 ,mM^"     ,-'.'   /   ;      ;      /   ,       MMMMb_wMW"  @\  
,MM:.    .'.-'   .'     ;     `,     ;     `,     MMMMMMMW `"=./`-,
WMMm__,-'.'     /      _.\      F'''-+,,   ;_,_.dMMMMMMMM[,_ / `=_}
"^MP__.-'    ,-'.       `.     \_._,'     MMM^""'YWWMW^\`'""
The lion is roaring!"""
print(lion)

deer = r"""
Deer habitat forest
   /|       |\
`__\\       //__'
   ||      ||
 \__`\     |'__/
   `_\\   //_'
     _.,:---;,._
     \_:     :_/
       |@. .@|
       |     |
       ,\.-./ \
       ;;`-'   `---__________-----.-.
       ;;;                         \_\
       ';;;                         |
        ;    |                      ;
         \   \     \        |      /
           \_, \    /        \   |\ \
             |';|  |,,,,,,,,/ \ | \ \_
             |  |  |           \|  |  |
             |  |  |            |  |  |
             |  |  |            |  |  |
             |  |  |            |  |  |
             |__|__|            |__|__|
Pretty good!"""
print(deer)

goose = r"""
Goose habitat meadow
                                    _
                                ,-"" "".
                              ,'  ____  `.
                            ,'  ,'    `.  `._
   (`.         _..--.._   ,'  ,'        \    \
  (`-.\    .-""        ""'   /          (  d _b
 (`._  `-"" ,._             (            `-(   \
 <_  `     (  <`<            \              `-._\
  <`-       (__< <           :
   (__        (_<_<          ;
    `------------------------------------------
Beautiful!"""
print(goose)

bat = r"""
The habitat of bats is a cave
   _______________             _________________
       ~-.        \  |\___/|  /       .-~
           ~-.     \ / o o \ /      .-~
              >     \\  W  //     <
             /       /~---~\       \
            /_      |       |      _\
             ~-.    |       |    .-~
               ;     \     /      i
             /___     /\ /\   ___\
                  ~-. V   V .-~
                   V         V
It's doing fine."""
print(bat)

rabbit = r"""
The habitat of rabbits is a meadow
          ,
         /|      __
        / |   ,-~ /
       Y :|  //  /
       | jj /( .^
       >-"~"-v"
      /       Y
     jo  o    |
    ( ~T~     j
     >._-' _./
    /   "~"  |
   Y     _,  |
  /| ;-~ _  l
 / l/ ,-"~    \
 \//\/      .- \
  Y        /    Y 
  l       I     !
  ]\      _\    /"\
 (" ~----( ~   Y.  )
It looks fine!"""
print(rabbit)

animals = [camel, lion, deer, goose, bat, rabbit]     # Список тварин
number = int(input("Please enter the number of the habitat you would like to view: "))
print(animals[number])

print("You've reached the end of the program.")

while True:
    user = input("Please enter the number of the habitat you would like to view (or 'exit' to quit): ")     # або номер або  exit

    if user == 'exit':
        print("See you later!")
        break

    if user.isdigit():                    # Перевірка число чи не число
        habitat_number = int(user)

        if 0 <= habitat_number < len(animals):
            print(animals[habitat_number])
        else:
            print("Invalid habitat number. Please try again.")
    else:
        print("Invalid input. Please enter a number or 'exit'.")