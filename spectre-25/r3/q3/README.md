At the Altar, Eve faces a new challenge: uniting the divided factions. The Codemasters demand strict rules to curb chaos, the Hacksmiths champion unrestricted freedom, and the Data Druids seek balance and preservation of the virtual ecosystem.

 Guided by Kara Nix's words—"Unite what is broken, or leave empty-handed"—Eve navigates the factions’ grievances with diplomacy, addressing their demands for fairness, creativity, and sustainability. By fostering collaboration with pcs , she restores harmony, unlocking the…

`Points : 800`

- we have a file named `trial_0f_unity` which is a binary executable file , running it we get   DEMN,YOU GOT ME REAL QUICK
			     GUESS, THIS WAS EASY ENOUGH
				 OSCTF{3a5y_p3a5y}

- which is a fake flag , so now using `hardening-check` a tool used to check protections on a binary , we get 

```sh
hardening-check tr1al_0f_un1ty 
	tr1al_0f_un1ty:
	 Position Independent Executable: yes
	 Stack protected: yes
	 Fortify Source functions: no, only unprotected functions found!
	 Read-only relocations: yes
	 Immediate binding: no, not found!
	 Stack clash protection: unknown, no -fstack-clash-protection                                 instructions found
	 Control flow integrity: no, not found!

# also running file 
file tr1al_0f_un1ty

ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 4.4.0, BuildID[sha1]=5b33c789834cde175ba690509a62deac964e2cbb, not stripped
```
as the binary is not stripped lets open it in ghidra

- in the program trees checking .bss and then .data we stumble upon alot of global variables (ghidra stores them in .data) 
![[ghidra.png]](ghidra.png)
taking out all the hex values of n , c and p and concatenating the hexes we get :-
n = 7706350080509933960915731475157042386819671015219471730180600096244041619157664652904817532724395035921591766213569126357832044793897396453188463203180479
p = 67900214844112219555506702373451026839323873323112297627106747938936601518641
c = 3200582589046258776155111823678284049720921208421907625678046048235090972062311394465840930987801830150074095472397448894824955433581146581756394990759693485024784752393021623403780900596295902851666159728976310042295438662890462140529728898204884475396206982517133180218657638227721832459756090360135861134

- now we know this is some kind of cryptosystem , and furthur analysing the functions reveals it is pailliar cryptosystem , which could be reversed even without knowing the exact cryptosystem but only the functions in ghidra (also hinted in question , `pcs`)

- reversing it using the script below gives out 
	Decrypted message: 3402075368099565918980438969562282468212149998586161083024073350756029275476696677330266590356541973940907139655558122906847507731146238447609310669027184

![[pai-dec.py]](pai-dec.py)

- this looks like another value , but this is less than n hence can even be a simple RSA , going back to ghidra code , there are 14 functions except main top 4 functions describe 2 different cryptographic techniques one is pcs and other one is RSA only hence slapping this new c , and same n , only thing left is e , e is given as 65537 in a function rsv which is a fake function so fake e , we had to look at the factors to get e or take the free hint .
- using n , c and e we get `539757526648120958511049` , treating as ascii and converting to text , it gives `5a9dB0x_Un1`

 `Flag: OSCTF{2_0f_3_f0Un4}`
