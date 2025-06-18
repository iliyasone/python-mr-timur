### Definitions with Tiny Examples

* **`struct`** — composite type that bundles named fields laid out consecutively in memory.

  ```c
  struct Point { int x; int y; };
  struct Point p = {1, 2};
  ```

* **`malloc`** — reserves *n* raw bytes on the heap; contents are un-initialized.

  ```c
  int *p = malloc(5 * sizeof(int));   /* 5 ints */
  free(p);
  ```

* **`calloc`** — allocates and zero-fills `count × size` bytes.

  ```c
  int *p = calloc(5, sizeof(int));    /* 5 zeroed ints */
  free(p);
  ```

* **`size_t`** — unsigned integer type returned by `sizeof`, able to index any array on the platform.

  ```c
  size_t n = sizeof(long);            /* typically 8 on 64-bit */
  ```

* **`sizeof`** — compile-time operator giving the size of a type or object in bytes (constant expression except for VLAs).

  ```c
  printf("%zu\n", sizeof(double));    /* prints 8 on LP64 */
  ```

---

### Task: Implement a Dynamic Integer List (`IntList`)

```c
struct IntList {
    int    *data;     /* heap array              */
    size_t  size;     /* elements currently used */
    size_t  capacity; /* slots allocated         */
};

/* initialise list with capacity = 0 */
void intlist_init(struct IntList *lst);

/* append value, doubling capacity when needed */
void intlist_append(struct IntList *lst, int value);

/* remove and return last element; if empty, print to stderr and exit(1) */
int  intlist_pop(struct IntList *lst);

/* release heap memory and reset fields to zero/NULL */
void intlist_free(struct IntList *lst);
```

**Constraints**

1. When `size == capacity`, grow to `(capacity ? 2*capacity : 4)` elements via `realloc`.
2. All counters/indices are `size_t`.
3. Every successful `malloc`/`realloc` must be balanced with `free`.
4. `intlist_pop` is O(1); on empty list terminate the program with a clear error message.
5. Provide a short `main` demonstrating `init → append → pop → free`.
