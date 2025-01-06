# kitty-go-panics

A [kitty terminal](https://sw.kovidgoyal.net/kitty/) extension that opens a standard [Go panic](https://gobyexample.com/panic) (file and line) directly in [VSCode](https://code.visualstudio.com).

## Usage

> [!IMPORTANT]
> This extension requires [VSCode](https://code.visualstudio.com) with `code` tools installed in `/usr/local/bin`.

Download `go_panics.py` and move it into `~/.configs/kitty/` (or your equivalent).

Map to a key (`ctrl+g`)
```
map ctrl+g kitten go_panics.py
```

Use when viewing a Go panic, like the following (found in `example/`)

```go
cd example

go run main.go

panic: runtime error: index out of range [0] with length 0

goroutine 1 [running]:
github.com/plyr4/kitty-go-panics/pkg_c.C()
	/Users/plyr4/kitty-go-panics/example/pkg_c/c.go:7 +0x24
github.com/plyr4/kitty-go-panics/pkg_b.B(...)
	/Users/plyr4/kitty-go-panics/example/pkg_b/b.go:8
github.com/plyr4/kitty-go-panics/pkg_a.A()
	/Users/plyr4/kitty-go-panics/example/pkg_a/a.go:10 +0x20
main.main()
	/Users/plyr4/kitty-go-panics/example/main.go:8 +0x1c
exit status 2
```

Finally, hit `ctrl+g`.
