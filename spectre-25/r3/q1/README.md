Eve’s team lands in the fragmented realm of Factionland, a shattered digital world locked in conflict. Three factions—Codemasters, Hacksmiths, and Data Druids—fight for dominance amidst crumbling cities, glowing forests, and pixelated ruins. Each zone whispers a clue: hidden in the chaos, a faint symbol resembling Kira appears in scattered fragments, hinting at a deeper unity buried beneath the divide. Clusters of eight symbols, arranged in patterns of two, repeat across the terrain, silently pointing toward the solution to the factions' discord.

`Points : 600 `

- we have a file named `k1ram0rrow.bin` which is actually a zip file , now in this we have no clue to unzip the zip so we can try running common wordlists or cook up on our own 

- in the question we have the appearance of 8 and 2 , so by that using the zip  file name we cook up a wordlist using crunch
```sh
crunch 8 8 k1ram0rrow > pass.list
```
 
 - now running john with this 
 ```sh
 sudo zip2john k1rram0rrow.zip > hash.hash
 
 sudo john hash.hash --wordlist=pass.list
```
 
 we got the password `mork1ra0` , this gives us an image `fractured_faction.png

- given png we can try some png tools etc but the core concept of this steg is LSB and that 2 bit LSB (derived from the question  

- we can use the following python script to work with this , extracting last 2 lsbs then mapping them back as 4 bit msbs in a new image

![[steg-extract.py]]

- finally we can see the flag in the image 

 `Flag : OSCTF{Th3_s1g4t's_sad}`