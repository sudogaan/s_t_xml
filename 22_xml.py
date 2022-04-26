# implementation of the elementtree api

# to get a clear vision of functions in xml.etree.ElementTree

import xml.etree.ElementTree as ET
from inspect import getmembers, isclass, isfunction

# Display classes in ET module
#for (name, member) in getmembers(ET, isclass):
	#if not name.startswith("_"):
		#print(name)

# Display functions in ET module
for (name, member) in getmembers(ET, isfunction):
        if not name.startswith("_"):
                print(name)

# xml: a tree of elements, a tree is a data stucture where each node other than the root has a single parent and each node can have zero or more children
# an xml document is a tree where each node is an element, an element is simply a pair of tags, the start tag and the end tag
# the end tag requires a slash "/"
# an element can contain attributes(key value pairs) inside the start tag
# <user id='24'></user>
# elements can also contain text between the tags
# <user id='24'>GVR63</user>
# and even other elements
# <user id='24'>GVR63<permissions/></user>

# fromstring takes an xml data in the form of a string and returns an element object
# parse will open an xml file and return it as an element tree
# tostring is the inverse of the fromstring function (converts element to a string)

# if we assume that we have an xml file names as hodlers.xml:

import xml.etree.ElementTree as ET

tree = ET.parse("hodlers.xml") #open the file using the parse function, will return an element tree object
root = tree.getroot() #to get the root element of this 
print(ET.tostring(root)) #to print out this element as a string
# the output of this code is a byte string according to the leading 'b'. This output includes all child elements in addition to white space 
# get 'coin' attribute 

coin = root.get('coin') #to get the value of an attribute, the crypto element has a single attribute, coin.
print("Crypto name = {val}".format(val=coin)) #to check if everything is correct

# the get method returns an attribute value, to create an attribute you use the set method.

#set 'launched' attribute 
root.set('launched', '20210101') 
print(root.attrib) # we use attrib property to see all of the attributes for an element, this returns all the attributes as a dictionary

#save updated XML
tree.write('hodlers.xml') #to save it, we use the write method

#add 'id' attribute to each investor
id = 1 
#to find all investor nodes in the xml tree 
for investor in tree.findall('investor'):
	investor.set('id', str(id)) #setting an id attribute, id is integer but the attribute value should be a string, that's why we use str(id)
	id += 1 #increment the id
#save XML
tree.write('hodlers.xml')

#delete 'id' attributes
for investor in tree.findall('investor'):
	del(investor.attrib['id']) #delete the id entry in the attribute dictionary
#save XML
tree.write('hodlers.xml')

#add investor #1st method
investor1 = ET.fromstring("<investor>Allen Duffy</investor>") #we can use fromstring method to create the new investor explicitly
root.append(investor1) #append this element to the root node and save the XML
tree.write('hodlers.xml')

#add investor #2nd method
investor2 = ET.Element("investor") #calling the element constructor, we pass the name of the tag and have a new element object 
investor2.text = "Karl Amber" #set the text value of this investor
root.append(investor2)
tree.write('hodlers.xml')

#the element tree and element classes also support selecting nodes by path 

#add ids once more
for (id, investor) in enumerate(root.findall('investor')): #iterate over an enumeration of the investor elements
	investor.set('id', str(id))
tree.write('hodlers.xml')

#select investor4
investor = root.find(".//investor[@id='4']") #selecting the first investor element with an id of 4
print(investor.text)

#to find more than one element use findall

