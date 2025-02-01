Riftwalkers sabotage their progress, creating virtual storms and disruptions _0Ytg1u?9? . Eve rallies players in the Sandbox to fend off the attacks, showcasing the resilience of collective creativity.

The masterpiece glows. Kira’s voice resonates:  
"Creation is the soul of progress. Build not for power, but for purpose."

`Points : 1000`

- we have a directory in which we got 3 files `sam , system , r1ftwalk3r.zip` now sam and system directly to windows system files and the zip is password protected , so using secretsdump.py on it (which is a well known script by impacket) , we get the following 

![[secretsdump.png]](secretsdump.png)

- now in the r1ftwalk3r there are 2 directories , can be seen through gui , sp3ctr3 and player so trying noth of there NT and LM hashes we find NT hash of player to successfuly unlock the zip.

- now we need passwords for both player and sp3ctr3 , we have no clue so going back to the question , we see a weird phrase  `_0Ytg1u?9?` , using crunch on it creating a passlist of 9 chars using 0Ytg1u ,with crunch and running john we get password `Y0u_g0t_1` 

``` sh
crunch 9 9 _0Ytg1u > pass.list

zip2john player.zip > hash.hash

john hash.hash --wordlist=pass.list

# unlocks player.zip using password `Y0u_g0t_1`
# this same password can be found cracking ntlm hashes of player using hashcat with same pass list but that is an unnecessary step while working with directories and not the real system 
# P.S we were meant to share the windows vm but it was too big :(
```

- now in player there are 2 more files , r00t and access , first access with blk data may perceive as  a disk imageor some other block data but skipping it for the moment and analysing r00t in ghidra which is also a binary with little to no protections , only PIE and RELR (can be found using `hardening-check`)

- here we can see that 2 files are used in this code input.txt and image.bmp , now furthur analysing the code we can see two other functions embed and encodeBit have been used , opening encodeBit looks like a normal xor function whereas embed tells us that it is a one bit encoding 

![[main.png]](main.png)

![[encodeBit.png]](encodeBit.png)

![[embed.png]](embed.png)

- now in the main function we are running a loop for 8 iterations telling 8 bit for every character in local_38 , i.e the file input.txt , so furthur analysing this tells us that the encodeBit is triggered if local_28 & 1 != 0 also it can be seen that local_28 is being used as an indexing value because in each iteration it is incremented by 1.

- after that there is another variable local_20 which is restricted in the range 0-2 by the code snippet below the if statements and is iterating constantly form 0-2 , the if statements are embedding the current bit using the embedding function and the value of local_20 is also used in calling the functions , as per the context of this code , this hints directly to the channels of RGB 0,1,2.

- finally we can see that another variable is incremented twice in every iteration i.e local_10 and local_10 is used in another while function in the same iteration where if it exceeds the value of local_58 it calls an error "Imaze size exceeded" hence local_10 must keep track of the row or the width of the image file whereas local_18 should be the other one row or width.

- now after accumulating all the data we know that we are
	1. reading the char from input.txt.
	2. treating it as 8 bits of data.
	3. xoring alternate bits , using bitwise & operator in if statement and then calling encodeBit function.
	4. iterating between r,g,b channels embedding every bit as 1-bit lsb. 
	5. then skipping 2 rows (assuming we are iterating through column in step 4)

- now to extract what is hidden in the image we can cook our own c script and use that on the file named access , we can change its extension to image.bmp

[decryption.c](decryption.c)

- now using this script above gives us f60c2d5dc14560b758bb7aa187983b9c which is another NT hash using it on the sp3ctr3 zip we get 2 files purpose.zip and fasttrack.txt

- fasttrack is  a known wordlist for password but running this with john didn't bear any fruit so i manually inspected it because its a small wordlist and found `1ll0g1cal_@@@@@`  which hints that this is an incomplete password , using default crunch with all numbers and alphabets we created a wordlist 
```sh
crunch 15 15 -t 1ll0g1cal_@@@@@ > pass.list
```

- running this pass.list on the purpose.zip with john works and gives `1ll0g1cal_stuff` as password , now finally we have a text file named soul where we get the flag OSCTF{T415_ha5_b33n_fUn}

`Flag : OSCTF{T415_ha5_b33n_fUn}`
