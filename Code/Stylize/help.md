# **Welcome to Help**
### Basics
To use this 'plugin' the main html file where the  
base page is situated is the 'index.html'  
file.
The boilerplate has been done for you, along with  
some examples on the types of modules and  
components you can use.

To link the html file with the css, the main.css  
file has been formatted with scss (sass css)  
syntax

use a ```<link rel="" href="">``` to use the css.  
It has already been done for you but should you  
change the path of the index.html file, this is  
how you link:
``` html
<link rel="stylesheet" href="PATH/TO/main.css">
```

### Fonts
To use fonts define them like this:  
``` scss
.INSERT_NAME_HERE {
    font_family: $INSERT_NAME_HERE;
}
```
Here are some font presets:  
``` scss
/* Fonts */
$Default: "";
$Roboto: "Martian Mono", monospace;
$Arial: "Arial", Helvetica, monospace;
$YoungSerif: "Young Serif", sans-serif;
$Montserrat: "Montserrat", serif;
$Poppins: "Poppins", "Montserrat", sans-serif;
$PixelifySans: "Pixelify Sans", cursive;
$OldSchool: "Playfair Display", serif;
$PlayfulContemporary: "Quicksand", sans-serif;
$Serious: "Open Sans", sans-serif;
$Ubuntu: "Ubuntu", sans-serif;
$Impactful: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
```
The fonts are downloaded from Google Fonts  
Here are the links  
``` html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<!--Fonts-->
<link href="https://fonts.googleapis.com/css2?family=Martian+Mono&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Young+Serif&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Montserrat&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Pixelify+Sans&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Quicksand&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Open+Sans:ital@1&display=swap" rel="stylesheet">
<link hr1ef="https://fonts.googleapis.com/css2?family=Ubuntu&display=swap" rel="stylesheet">
```

### Text Overlays
To use text overlays, insert this in the html:
(one has been done for you.)
``` html
<!--Text Overlays-->
<div class="container">
    <div class="box1">
        <div class="ImpactText">OVERLAY</div>
        <div class="SubliminalText"><i>T E X T</i></div>
    </div>
    <div class="box2">
        <div class="ImpactText">OVERLAY</div>
        <div class="SubliminalText1"><i>T E X T</i></div>
    </div>
    <div class="box3">
        <div class="ImpactText">OVERLAY</div>
        <div class="SubliminalText2"><i>T E X T</i></div>
    </div>
</div>
```
then use the _overlays.scss to customise the size and shape.  
the base mixins are in the _mixins.scss file
``` scss
.container { position: relative; }

.ImpactText {
    @include flex-center();
    @include backtextoverlay();
    font-size: 75px;
    font-family: $Impactful;
}

.SubliminalText {
    @include flex-center();
    @include fronttextoverlay();
    font-size: 25px;
    top: 45px;
    color: red;
    font-family: $OldSchool;
    text-align: center;
    left: 50%; /* Center horizontally */
    transform: translate(-50%);
}

/* Duplicate Overlays
This is for the positioning 
of the front text */

.SubliminalText1 {
    @include flex-center();
    @include fronttextoverlay();
    font-size: 25px;
    top: 170px;
    color: red;
    font-family: $OldSchool;
    text-align: center;
    left: 50%; /* Center horizontally */
    transform: translate(-50%);
}

.SubliminalText2 {
    @include flex-center();
    @include fronttextoverlay();
    font-size: 25px;
    top: 290px;
    color: red;
    font-family: $OldSchool;
    text-align: center;
    left: 50%; /* Center horizontally */
    transform: translate(-50%);
}

/* Padding */

.box1 { padding: 10px; }
.box2 { padding: 10px; }
.box3 { padding: 10px; }
```
The mixins look like this:
``` scss
/* Text Overlays */

@mixin backtextoverlay() {
    align-items: center;
    width: 300px;
    padding: 5px;
    border: 1px solid #ccc;
    top: 0px;
    left: 0px;
    z-index: 0;
}

@mixin fronttextoverlay() {
    position: absolute;
    width: 300px;
    font-size: 15px;
    left: 0px;
    z-index: 1;
}
```
### Cards
Cards is a modular way of storing  
short sentence paragraphs in a  
neat and tidy way.

To initialize the card, enter this into the html file
Light:
``` html
<div class="card">
    <img src="https://images.unsplash.com/photo-1524749292158-7540c2494485?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTd8fGRldmVsb3BlcnN8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60" alt="">
    <div class="card_content">
        <h2 class="card_title">Lorem</h2>
        <p class="card_description">Lorem, ipsum dolor sit amet consectetur adipisicing elit. Rerum porro dolores sapiente.</p>
    </div>
</div>
```
Dark:
``` html
<div class="card card_dark">
    <img src="https://media.istockphoto.com/photos/put-more-in-get-more-out-picture-id1291318636?b=1&k=20&m=1291318636&s=170667a&w=0&h=UvVIk7wwkN3X9OFm8gBlWWviV5vAjfrq2ejYP30JmnA=" alt="">
    <div class="card_content">
        <h2 class="card_title">Lorem</h2>
        <p class="card_description">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Atque amet obcaecati nihil.</p>
    </div>
</div>
```
The rest will be done for you and will  
adapt natually to the size and length of the  
text.

thanks for using landingpager!
hope you come again!