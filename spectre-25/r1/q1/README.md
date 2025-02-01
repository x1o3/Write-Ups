You log  into  Pixel  Haven , a  vibrant,  retro-inspired world  in the  OASIS designed as a  tribute to 1980s gaming culture. The sky is a mosaic of shifting  pixel patterns, and  the  ground is  a grid of neon tiles. Players wander through arcades, neon-lit streets , and  arenas, each filled with classic games and 8-bit challenges. Eve’s avatar , modeled  after  a  sleek,  modern  take  on  an  8-bit  adventurer, steps into the heart of the Retro Arcade World  

`Points : 100`

  - we have a jpg named arcade.jpg , running exiftool on it shows comment `No flag here but,c0rrUpt3d`
 -  running `binwalk arcade.jpg` shows there is some embedded data
 
``` sh
$binwalk arcade.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
321558        0x4E816         JPEG image data, JFIF standard 1.01
  
```
we can extract it all using --dd='.*' command

```sh
binwalk --dd='.*' arcade.jpg
```
this gives another image named 4E816

the flag is in the metadata/comment of that embedded image

`Flag: OSCTF{S0m30n3s_d3t3rM1n3d}`