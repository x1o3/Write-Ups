The   final   boss,   Shadows   of  the  World,   is a   menacing  fusion   of   8-bit Characters.   To   defeat   it,   Eve  must   navigate   a   shifting  maze, dodge classic Game-inspired    traps,    and    collect   memory   orbs   to   reveal   Halliday's vision for the OASIS. "The key lies just out of reach, shrouded in shadows. To claim it, you must delve deeper and prove your worth.” 

`Points : 200`

- we got a file named S3W.bin , running file tells us this is a zip 
- using john on it with rockyou gives password `shadowzendric` 

``` sh
sudo zip2john S3W.zip > hash,hash

sudo john hash.hash --wordlist=rockyou.txt
```

- unzipping we get 2 files `m3m0ry` , an ascii text file , and `k3y`  , a password protected zip
- now running the following command gives us 4 flags 

```sh
cat m3m0ry | grep "OSCTF"
```

- out of those , `Ph3w_G0tCha` is the password for the pdf in which we get the flag

`Flag : OSCTF{K3y?_W0nt_B3_3asY}`