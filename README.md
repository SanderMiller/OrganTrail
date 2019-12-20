# OrganTrail

We plan on sharing content through the medium of a game. Similarly to the games made on ARIS that allowed the user to experience learning and gameplay by way of augmented reality, our game experience will attempt to place the user in a text based, informative Ancient Egyptian environment. We think this model suits our process because of it's level of engagement, while still portraying relevant information in a fun and interactive way.

Currently we are considering using the Python library "pygame" to build our game. Pygame allows for simple manipulation of 2d pixel space and appears to be able to create simple decision based gameplay without too much trouble, which makes it a good candidate for our project. (It also allows us to keep track of items and assets, where some more linear story based game creators may fall short on)

Our next steps will be framing and structuring our game. We will have to consider what 3D models we will be including and their significance. We will begin brainstorming characters, and challenges that the player will face. We will have to do some more research on the Egyptian afterlife to ensure we are conveying accurate information. Then we will begin structuring our game in pygame.


INSTRUCTIONS ON GETTING ACCESS TO OUR GAME FOR WINDOWS:<br/>
**1.** <br/>
Follow this link to download python: https://www.python.org/downloads/ (download python 3.8)

Follow this link to download git: https://git-scm.com/download/win
run through the installation processes of both as instructed

**2.** <br/>
Search "system variables" on your local computer and click on "edit the system environment variables"

Click on the "environment variables" button

double-click on path

click new

paste in this (replacing UserNameHere with your local user name) C:\Users\UserNameHere\AppData\Local\Programs\Python\Python37

click new again

paste in this (again replacing usernamehere) C:\Users\UserNameHere\AppData\Local\Programs\Python\Python37\scripts

do the same for these two:
C:\Program Files\Git\cmd\
C:\Program Files\Git\bin\


**3.** <br/>
open command terminal (can be searched for on local computer using CMD)

copy paste:      `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`             into terminal and click enter

type `python get-pip.py` into terminal and click enter

`pip install pygame`

`pip install opencv-python`

**4.**<br/>
put the following command into terminal: git clone https://github.com/SanderMiller/OrganTrail.git

type `cd OrganTrail`
to play the game, copy paste "python PygameVisual.py" into terminal and click enter


Credit where it's due:
The majority of the images in this game belong to the Met Museum's copyright free image library! Other images were taken from demonthings and a single image was taken from assassin creed origins photography mode. We are not monetizing this game in any fashion, and the preprocessed images were not created or owned by us.
