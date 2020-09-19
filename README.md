# NASM Shell++

This tool enhance the power of NASM Shell (Metasploit Framework) to save some precious time while building your exploits.

Just enter your bunch of assembly instructions and generate your final payload (compatible with Python / C / CPP).

Supports bad characters detection.

## Help Menu

```
:help                      : Display help menu (This menu).
:clear                     : Clear Terminal Screen.
:exit                      : Terminate application.
:badchars      <badchars>  : Set characters you want to avoid in your shellcode. Highlight them in red. (Ex: "\x01\x02\x03")
:ls_badchars               : List bad characters.
:assembly                  : Dump saved assembly instructions (current session).
:shellcode                 : Output shellcode version from assembly instructions (Python / C / CPP Formated String)
:pyvar         <var_name>  : Output shellcode version from assembly instructions to python formated variable.
:dlast                     : Remove latest saved instruction.
:delete                    : Delete saved instruction at defined index.
:update                    : Update saved instruction at defined index.
:reset                     : Delete saved instructions. Reset/Clear instruction buffer (/!\ Can't be undo).
:load          <filename>  : Load assembly file from disk.
:r                         : Read Only. Instructions are not saved to instruction buffer.
:w                         : Write mode. Instructions are saved to instruction buffer.
:!             <command>   : Execute shell command. Ex: ":!ls -ltr /var/log"
```







