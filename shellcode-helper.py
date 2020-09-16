#!/usr/bin/python3

'''

	Jean-Pierre LESUEUR (@DarkCoderSc)
	https://www.twitter.com/darkcodersc
	https://github.com/DarkCoderSc
	https://www.linkedin.com/in/jlesueur/

	https://www.phrozen.io/

	Version: 1.0b

	Description:
		Impove Metasploit Nasm Shell Tool for Exploit Development Purpose.

	Changelog:
		* 2020/09/15 : Very first version of the script.

	TODO: 
		- Support Arrow Keys.
		- Optimize and make code more readable.

'''

import pexpect
from textwrap import wrap
from collections import defaultdict

nasm_shell_location = "/usr/bin/msf-nasm_shell" # Update the location of your Nasm Shell if required!

instructions = list()

'''
	Terminal Colors Class
'''

class tcolors:
	clear = "\033[0m"
	green = "\033[39m"
	red = "\033[31m"
	yellow = "\033[33m"
	blue = "\033[34m"


'''
	Def Loggers

'''

def success(message):
    print(f"[\033[32m+\033[39m] {message}")

def error(message):
    print(f"\033[31m{message}\033[39m")

def warning(message):
	print(f"\033[33m{message}\033[39m")


'''
	Instruction Object

'''
class instruction:
	def __init__(self, asm, opcodes):
		self.asm = asm
		self.opcodes = opcodes
		self.update_size()

	def update_size(self):
		self.size = int(len(self.opcodes) / 4)


'''
	Help Menu

'''
def display_help():
	print(f'\nShellcode Helper ({tcolors.blue}@DarkCoderSc{tcolors.clear})\n')

	print(f"\t {tcolors.blue}:help{tcolors.clear} -> Display this menu.")
	print(f"\t {tcolors.blue}:exit{tcolors.clear} -> Close this application.")
	print(f"\t {tcolors.blue}:assembly{tcolors.clear} -> Dump session assembly instructions.")
	print(f"\t {tcolors.blue}:shellcode{tcolors.clear} -> Generate output shellcode (Python / C / CPP formatted)")
	print(f"\t {tcolors.blue}:dlast{tcolors.clear} -> Delete last instruction.")
	print(f"\t {tcolors.blue}:delete{tcolors.clear} -> Delete instruction at specified index (prompted).")
	print(f"\t {tcolors.blue}:update{tcolors.clear} -> Update instruction at specified index (prompted).")
	print(f"\t {tcolors.blue}:reset{tcolors.clear} -> Clear instructions. Restart from scratch.")

	print("\n")


'''
	Return Shellcode Size

'''
def get_shellcode_size():
	size = 0
	for obj in instructions:
		size += obj.size

	return size

'''
	Transform asm to it opcode equivalent using Nasm Shell

'''
def process_nasm_shell(asm, update_index = -1):
	proc.sendline(asm)

	proc.expect(expected_token)

	output = proc.before.decode("utf-8").rstrip()

	lines = output.split("\n")

	if "warning:" in output:
		lines.pop(0)
		output = "\n".join(lines)
		warning(output)

		return False

	if "Error:" in output:
		lines.pop(0)
		output = "\n".join(lines)
		error(output)
		
		return False

	opcodes = wrap(lines[1][10:].split(' ')[0], 2)

	formated_opcodes = ""
	for opcode in opcodes:
		formated_opcodes += f"\\x{opcode}"


	if (update_index != -1):
		instructions[update_index].asm = asm
		instructions[update_index].opcodes = formated_opcodes
		instructions[update_index].update_size()
	else:		
		instructions.append(instruction(asm, formated_opcodes))

		print(f"[{tcolors.green}+{tcolors.clear}] {tcolors.blue}{asm}{tcolors.clear} ({tcolors.blue}{formated_opcodes}{tcolors.clear}), Shellcode Size: {tcolors.blue}{get_shellcode_size()}{tcolors.clear} Bytes")

	return True


'''
	Dump Instruction or Opcode
'''
def dump(data):
	print('\n--- BEGIN DUMP ---')
	print(f"{tcolors.blue}{output.rstrip()}{tcolors.clear}")
	print('--- END DUMP ---\n')

	print(f"Shellcode Size: {tcolors.blue}{get_shellcode_size()}{tcolors.clear} Bytes\n")



'''

 	Entry Point

'''

if __name__ == "__main__":
	expected_token = "\\033\[1mnasm\\033\[0m >"

	proc = pexpect.spawn(nasm_shell_location)

	proc.expect(expected_token)

	print(f"\nEnter \"{tcolors.blue}:help{tcolors.clear}\" to display help menu.\n")

	while True:
		print("nasm > ", end='')

		stdin = str(input())

		# Exit Program Hijack
		if stdin == "exit":
			stdin = ":exit"

		# Ignore Empty Inputs
		if not stdin:
			continue

		# 
		# Parse Commands
		#

		if stdin[:1] == ":":
			command = stdin[1:].rstrip()

			if (command == "exit"):
				if proc:
					proc.close()

				break
			elif (command == "reset"):
				count = len(instructions)

				instructions.clear()

				success(f"{count} instructions cleared.")
			elif (command == "help"):
				display_help()
			elif (command == "assembly"):
				if len(instructions) > 0:
					output = ""
					for obj in instructions:
						output += obj.asm + "\n"

					dump(output)
				else:
					warning("No instruction yet.")

			elif (command == "shellcode"):
				if len(instructions) > 0:
					
					output = ""
					for obj in instructions:
						output += obj.opcodes

					dump(output)
			elif (command == "dlast"):
				if len(instructions) > 0:
					index = (len(instructions) - 1)

					instructions.pop(index)

					success(f"Element {index} successfully deleted.")
				else:
					warning("Nothing to delete.")
			elif (command == "delete") or (command == "update"):
				for index, obj in enumerate(instructions):				
					print(f"{index} - {tcolors.blue}{obj.asm}{tcolors.clear}")

				while True:
					print("Choose Index: ", end='')

					stdin = str(input())

					if not stdin.isnumeric():
						error("Invalid Index.")
					else:
						index = int(stdin)

						if (index > len(instructions) -1):
							error("Index out of range.")
						else:
							break

				if (command == "delete"):
					instructions.pop(index)
				elif (command == "update"):					
					print(f"Replace \"{tcolors.blue}{instructions[index].asm}{tcolors.clear}\" with: ", end='')

					stdin = str(input())

					if process_nasm_shell(stdin, index):
						success(f"Instruction at index {index} successfully updated.")
					else:
						error(f"Could not update instruction at index {index}")


				# elif ...
			continue


		#
		# Transform Asm Instruction through Nasm Shell from Metasploit
		#
		process_nasm_shell(stdin)
		
