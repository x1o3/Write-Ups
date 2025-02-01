
Kara Nix reappears, her shimmering with static. "The shard lies beyond knowledge itself. Prove your worth by recalling the tales, melodies, and marvels of those who came before." Kara materializes in a flicker of light, her glitching, glowing form radiating an otherworldly energy that hums through the OASIS. Speaking in a voice both soothing and eerie, she vanishes into streams of data, leaving an air of mystery behind.

`Points : 400`

- There is a file given named nix . when run file on it , it return data only.
- Running hexedit on it gives away it is a JPEG from broken headers

  ![[nix_hexedit.png]]

- rebuilding the headers , FF D8 FF E0 00 10 , returns a valid image 
- now further in the hints , we get `There are insects out there in the wild who appeared only twice`  this hints to cicada 3301 , where in one of the cicada challenges there was manipulation of image length from its hex.

![[nix_offset.png]]
`we changed 03 to 04 hence revealing the whole image`

- so manipulating the length offsets , as below we get `Ahle_0b_3Cz03i` at the bottom right which is in vignere cipher
- Now for that we look inito the image's metadeta using exiftool and the comment `THATWASQUICK` works as the key hence decrypting the flag `Hall_0f_3Ch03s`
  

`Flag : OSCTF{Hall_0f_3Ch03s}`