#### 1. **Preprocessing**

```bash
gcc -E source.c -o source.i
```

→ Output: `source.i` (preprocessed source)

#### 2. **Compilation to Assembly**

```bash
gcc -S source.i -o source.s
```

→ Output: `source.s` (assembly code)

#### 3. **Assembly to Object Code**

```bash
gcc -c source.s -o source.o
```

→ Output: `source.o` (object file)

#### 4. **Linking to Executable**

```bash
gcc source.o -o program
```

→ Output: `program` (executable)

---

### Alternative: Automate with One Command

```bash
gcc -Wall -save-temps -o program source.c
```

* Generates: `source.i`, `source.s`, `source.o`, and `program`
* `-save-temps` keeps intermediate files.

---

Let me know if you want to inspect the AST or IR (with `clang` or `gcc` plugins).
