# ShellCode Helper

This tool enhance the power of NASM Shell (Metasploit Framework) to save some precious time while building your exploits.

Just enter your bunch of assembly instructions and generate the final payload (compatible with Python / C / CPP).

## Help Menu

* `:help` -> Display this menu.
* `:exit` -> Close this application.
* `:assembly` -> Dump session assembly instructions.
* `:shellcode` -> Generate output shellcode (Python / C / CPP formatted).
* `:dlast` -> Delete last instruction.
* `:delete` -> Delete instruction at specified index (prompted).
* `:update` -> Update instruction at specified index (prompted).
* `:reset` -> Clear instructions. Restart from scratch.

## In Action

### Write a bunch of instruction and export to Python / C / CPP Formated String.

![Instructions](https://i.imgur.com/7zoVDy8.png)

### Delete instructions

![Delete](https://i.imgur.com/TqRdVxN.png)

### Update instructions

![Update](https://i.imgur.com/Xmf25XY.png)

### Supports NASM Shell Errors / Warning

![Errors](https://i.imgur.com/ETMv7nB.png)




