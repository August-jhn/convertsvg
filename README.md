This is just a quick program I created which allows me to easily embed stylized commutative diagrams on my website from 
https://q.uiver.app/. The program should only function on windows. In order for the program to run properly, there are three requirements.

1) Obviously, make sure Python is properly installed!

2) Make sure Inkscape is installed. If it isn't, after installing it make sure to add it to PATH in environment variables.

3) Finally, make sure MikTeX with pdflatex is installed and added to path.

In order to make sure all of these are configured properly, type:

>python
>pdflatex
>inkscape

If all of these are recognized commands on your computer, that means you are properly set up and ready to go!

Now for the actual instructions on how to use my program.

1) Enter the folder you want your SVG figures to be outputted into target.txt
2) On https://q.uiver.app/, create your diagram, and paste the LaTeX code into toconvert.txt
3) in command prompt, enter

>python convertsvg.py

If all is set up properly, you should find an SVG file in your target folder, titled figure.svg!

Hope you find this useful,

Cheers!