
In the Hall of Echoes, they encounter holograms of pop culture icons like Elvis Presley,Princess Leia, who pose interactive challenges. Elvis challenges them to recreate a virtual concert using rhythm mechanics.Princess Leia asks them to solve a puzzle map of iconic sci-fi worlds.

`Points : 400`

- in this we have a file named `is_that_elvis` with no extension , using file we get pcapng capture file. So, instinctively opening it in wireshark.
- running through some common filters , using ftp, ftp-data shows there are some messages and data transfers.

![[wireshark_ftp.png]]

- Now the above 3ch0 reveals that it is a JPEG image but broken down in parts, extracting these and concatenating them using the following command reveals the image below 

`cat 3ch0 3ch1 3ch2 3ch3 > img.jpg `

![[combined.jpg]]
- lower half of the image was given as a hint so you needed to sort the first half atleast 
- now this is in base64 and converting that gives out the flag 

`Flag : OSCTF{Tr1v1a_s40Wd0Wn}`