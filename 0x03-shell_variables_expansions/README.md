# 0x03. Shell, init files, variables and expansions

## 📚 Resources

### Read or Watch:
- [Expansions – linuxcommand.org](https://linuxcommand.org/lc3_lts0080.php)
- [Shell Arithmetic – GNU Bash Manual](https://www.gnu.org/software/bash/manual/html_node/Shell-Arithmetic.html)
- [Shell Initialization Files – TLDP Bash Guide](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_02.html)
- [The alias Command – linfo.org](https://www.linfo.org/alias.html)
- [Technical Writing (PDF)](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2021/6/9112669886fd446a2aa3113c31319d1f468dc160.pdf)

### man or help:
- `printenv`
- `set`
- `unset`
- `export`
- `alias`
- `unalias`
- `.`
- `source`
- `printf`

---

## 🎯 Learning Objectives

### General
- What happens when you type `$ ls -l *.txt`

### Shell Initialization Files
- What are the `/etc/profile` file and the `/etc/profile.d` directory
- What is the `~/.bashrc` file

### Variables
- Difference between local and global variables
- What is a reserved variable
- Creating, updating, and deleting shell variables
- Roles of: `HOME`, `PATH`, `PS1`
- Special parameters and the meaning of `$?`

### Expansions
- What is expansion and how to use it
- Differences between single and double quotes
- Command substitution using `$()` and backticks

### Shell Arithmetic
- Performing arithmetic operations in the shell

### The alias Command
- Creating, listing, and disabling aliases temporarily

### Other
- Executing commands from a file in the current shell

---

## ⚠️ Plagiarism Policy

You are expected to:
- Come up with your own solutions
- Not publish or copy any content of this project
- Understand that plagiarism will result in removal from the program

---

## ✅ Requirements

### General
- **Editors allowed:** `vi`, `vim`, `emacs`
- **System:** Ubuntu 20.04 LTS
- **Script constraints:**
  - Must be exactly 2 lines long (`wc -l file` should print 2)
  - Must end with a new line
  - First line must be: `#!/bin/bash`
  - No use of `&&`, `||`, or `;`
  - No use of `bc`, `sed`, or `awk`
  - Must be executable (`chmod +x`)
- **README.md** must be present describing what each script does

---

## 📁 Project Structure

```text
alx-system_engineering-devops/
└── 0x03-shell_variables_expansions/
    ├── 0-alias
    ├── 1-hello_you
    ├── 2-path
    ├── 3-paths
    ├── 4-global_variables
    ├── 5-local_variables
    ├── 6-create_local_variable
    ├── 7-create_global_variable
    ├── 8-true_knowledge
    ├── 9-divide_and_rule
    ├── 10-love_exponent_breath
    ├── 11-binary_to_decimal
    ├── 12-combinations
    ├── 13-print_float
    ├── 100-decimal_to_hexadecimal
    ├── 101-rot13
    ├── 102-odd
    └── 103-water_and_stir
