# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 11:10:19 2018

@author: Webster
"""
alien_0 = {}
alien_0["color"] = "green"
alien_0["points"] = 15
print (alien_0)
alien_0 = {"color" : "green"}
print ("The color of the alien is "+ " " +alien_0["color"] + ".")
alien_0 = {"color" : "yellow"}
print ("The new color of the alien is now" + " " + alien_0["color"] + "." )
alien_0 = {"x_position" : 0 , "y_position" : 25 , "color" : "green" , "speed" : "medium"}
#Lets attempt to find the new position of the alien based on their speed.
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 3
else:
    x_increment = 9
    

# to find the new position of the alien, we add the x increment to the original x position of the alien.
alien_0["x_position"] = alien_0["x_position"] + x_increment
print ("The new position of the alien is " + " " +str (alien_0["x_position"]))
#The above code helped us obtain the x_position only.
# Now let us attempt to get both the x and y position of the alien after moving it.
print (alien_0)
if alien_0["speed"] == "slow":
    x_increment = 3
    y_increment = 5
elif alien_0["speed"] == "medium":
    x_increment = 9
    y_increment = 15
else:
        x_increment = 27
        y_increment = 45
# Just like in the previous cases, the new position is found by adding the original position to the increment. 
alien_0["x_position"] = alien_0["x_position"] + x_increment
alien_0["y_position"] = alien_0["y_position"] + y_increment
print ("The new x coordinate is " + " " + str(alien_0["x_position"]))
print ("The new y coordinate is " + " " + str(alien_0["y_position"]))
#Pat yourself man. that was easy. 
print (alien_0)
#Now what if we want to remove some information from our dictionary. 
del alien_0["speed"]
print(alien_0)
#A dictionary containing simmilar objects.
favorite_languages = {
        "Ning'i" : "python" , 
        "domi" : "fortran" , 
        "izo" : "java" , 
        "corne" : "pascal" ,
        }
print ("favorite_languages")
print (favorite_languages)
print ("Ningi's favorite language is " + 
       favorite_languages["Ning'i"].title()
       + ".")

        


    