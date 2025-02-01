You receive a cryptic message from Kara Nix, the enigmatic NPC guide. The message appears as a scrambled text file that, when decoded, reads: "To find the key, face the past. Shadows of the world will reveal the truth at last." Kara appears in her cryptic fashion, a holographic rendered in glitchy,glowing lines. She explains that the shard is locked behind the Trial of Knowledge.

`Points : 150`

- we have 2 files named `inbox_Kara.txt` and `flag.py` 
- in inbox_Kara.txt there are just hex values
- when we open flag.py , we see a function named str_xor , hinting it is a xor function
- we have a phrase `110313162c02475200` but no key here while the following lines hint us that key is always extended to the length of the phrase

```python
while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)
```

- the line in question , `To find the key, face the past` , hints us to previous question where the comment of first image was `No flag here but,c0rrUpt3d` 
- so xoring the phrase with `c0rrUpt3d` gives `r3adyr3ad` hence , the key is `r3ady`
- now xoring the hex phrase in inbox_Kara.txt with r3ady reveals the flag `P1X3l_C0l1s3UM`

`Flag : OSCTF{P1X3l_C0l1s3UM}`

