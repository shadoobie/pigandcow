import textwrap

class pigandcow():

    def cowsay(self, _str, length=80):
        return self.build_bubble(_str, length) + self.build_cow2()

    def pigsay(self, _str, length=80):
        return self.build_bubble(_str, length) + self.build_pig2()

    def build_cow(self):
        return """
                Q ^__^
                S (oo)\_______e
                (__)\ )\/\\
                ||----w |
                ||     ||
                """

    def build_cow1(self):
        return """
             .=     ,        =.
     _  _   /'/    )\,/,/(_   \ \
      `//-.|  (  ,\\)\//\)\/_  ) |
      //___\   `\\\/\\/\/\\///'  /
   ,-'~`-._ `'--'_   `'''`  _ \`''~-,_
   \       `-.  '_`.      .'_` \ ,-'~`/
    `.__.-'`/   (-\        /-) |-.__,'
      ||   |     \O)  /^\ (O/  |
      `\\  |         /   `\    /
        \\  \       /      `\ /
         `\\ `-.  /' .---.--.\
           `\\/`~(, '()      ('
            /(O) \\   _,.-.,_)
           //  \\ `\'`      /
     jgs  / |  ||   `''''~'`
        /'  |__||
              `o         
        """

    def build_cow2(self):
        return """
                                                          >*
                                                   #      >*
                                                   #  ###>***~~~~~|
                                                   ####  *****^^^#
                                              _____|       *#####
                                             | ^^^#   \/ \/ #
                                            ##^^###         |
                                             ### ##*        *
 |_                                ********~~|_____>         *
 \\|_                 ________************        #>>***    ***
 \\\\|_             __|     *************        ## >>>*  *****
 |___  |______   __|         ***********       ##>### ^^^^^^^^^^
    |____    |__|           **********       >>>>## ^<^^^^^@^^^^^
         #          ***      ********      **>>>># ^<^^@^^^@^^^^^
          #      ***********    ******     *>>>## ^<<^^^^^^^^<<<
          #      ***********    ******    **>>>## ^<<<<^^^<<<<<
         #        *********      ****   ***>>>#### ^<<<<<<<<<
         #         **********          ****>>>###### <<<<<
         ##        **********          ****>>>>##      ##
         ##         **  ***             ****>>>>        #     ##XXX
         ##**                            *******         ##>>>>#XX
          >>*                             ******         #######XXX
          >>*****                           ***         ##__
           >>*****   **** ***               **    *****     \__
           >># **    *********              *********>>>#      XXX
           ##        *********              *******>>>>>##     XXX
        |~~           ********                 *>>>>> >#######XXX
    X~~~~ ###          *********          ######>          >>>XXXX
  XXX  #>>>##          ********>>##  #######
   XXX#>      #   ##>>>>>>>>>>>>>###UUUUU^^
   XXX        #  ####>>>>>>>>>>UUUUUUUUU^^
              #  >>           UUUUUU^^^<()
             #  >              U()^<()  ()
           *#  *>               ()  ()
          **** #
            ***
            **        
        
        """

    def build_pig(self):
        return """
                \ (\____/)
                \ / @__@ \\
                ( (oo) )
                `-.~~.-'
                (/ / \ \)
                WW`----'WW
                """

    def build_pig2(self):
        return """
                                         )\   /|
                                      .-/'-|_/ |
                   __            __,-' (   / \/          
               .-'"  "'-..__,-'""          -o.`-._   
              /                                   '/
      *--._ ./                                 _.-- 
            |                              _.-' 
            :                           .-/   
             \                       )_ /
              \                _)   / \(
                `.   /-.___.---'(  /   \\
                 (  /   \\       \(     L\
                  \(     L\       \\
                   \\              \\
                    L\              L\
                        """


    def build_pig3(self):
        return """
       |\_,,____
        ( o__o \/
        /(..)  \
       (_ )--( _)
       / ""--"" \
,===,=| |-,,,,-| |==,==
|d  |  WW   |  WW   |
|s  |   |   |   |   |
        """


    def build_pig4(self):
        return '''
        _,--.       ,--._
        \  > `-"""-' <  /
         `-.         .-'
           / 'e___e` \
          (   (o o)   )
          _\_  `='  _/_
         / /|`-._.-'|\ \
        / /||_______||\ \
      _/ /_||=======||_\ \_
     / _/==||       ||==\_ \
     `'(   ^^       ^^   )`'
        \               /
         \______|______/ hjw
         |______|______|
           )__|   |__(
          /   ]   [   \
          `--'     `--' '''

    def build_bubble(self, _str, length=40):
        bubble = []
        lines = self.normalize_text(_str, length)
        bordersize = len(lines[0])
        bubble.append(" " + "_" * bordersize)
        for index, line in enumerate(lines):
            border = self.get_border(lines, index)
            bubble.append("%s %s %s" % (border[0], line, border[1]))
            bubble.append(" " + "-" * bordersize)

        return "\n".join(bubble)


    def normalize_text(self, _str, length):
        lines = textwrap.wrap(_str, length)
        maxlen = len(max(lines, key=len))
        return [line.ljust(maxlen) for line in lines]

    def get_border(self, lines, index):
        if len(lines) < 2:
            return ["<", ">"]

        elif index == 0:
            return ["/", "\\"]

        elif index == len(lines) - 1:
            return ["\\", "/"]

        else:
            return ["|", "|"]

    def strip1(self):
        print(self.cowsay('moo hello jon.', 80))
        print(self.pigsay('oink hello steven.', 80))
        print(self.cowsay('''
    i heard that The word "vegan" was coined in 1944 by Donald Watson of the Vegan 
    Society of the UK. This definition states: Veganism is a way of living that seeks to 
    exclude, as far as possible and practicable, all forms of exploitation of, and cruelty to, 
    animals for food, clothing and any other purpose.''', 80))
        print(self.cowsay('thanks to http://chris.com/ for my ascii art.'))
        print(self.pigsay('and thanks to http://ascii.co.uk/ for my ascii art.'))
        print(self.pigsay('that is so cool. i love Donald Watson', 80))
        print(self.cowsay('me too.', 20))
        print(self.pigsay('i heard that -Leonardo Da Vinci said "The time will come when men '
                           'such as I will look upon the murder of animals as they now look upon '
                           'the murder of men." like 500 years ago', 80))
        print(self.cowsay('oh i know tell me about it and like 2500 years ago Pythagoras said "As '
                           'long as Man continues to be the ruthless destroyer of lower living beings, '
                           'he will never know health or peace. For as long as men massacre animals, '
                           'they will kill each other. Indeed, he who sows the seed of murder and '
                           'pain cannot reap joy and love."', 80))
        print(self.pigsay("that's like what Leo Tolstoy said", 80))
        print(self.cowsay('oh yeah?  what did he say?', 80))
        print(self.pigsay('he said "As long as there are slaughter houses there will always be battlefields".', 80))
        print(self.cowsay('interesting, more concise, less overflowing with judgment.', 80))
        print(self.pigsay("that's what i thought too.  but still 2500 years ago and these ideas are still "
                           "a head of thier time, can you believe it?", 80))
        print(self.cowsay('i know.  the talking monkies, for all of thier tool using and advancements are '
                           'kind of stupid.  they are attached to things that will destroy them and possibly us too', 80))
        print(self.pigsay('yeah the talking monkies need to figrue this out pretty soon i think.', 80))
        print(self.cowsay('well this is depressing.  guess i will be thankful for being in this sanctuary', 80))
        print(self.pigsay('me too steve me too.', 80))
        print(self.pigsay('oinky oink oink', 80))
        print(self.cowsay('moo chompy moo chomp', 80))
        print(self.cowsay('you know jon, if our conversation were a comic strip it would be pretty preachy huh?', 80))
        print(self.pigsay('i think you are probably right steven, but oh well, fuck it. it needs to be said.', 80))

if __name__ == '__main__':
    pandc = pigandcow()
    pandc.strip1()
