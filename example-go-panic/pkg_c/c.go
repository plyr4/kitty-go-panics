package pkg_c

import "fmt"

func C() string {
	ok := []map[string]string{}
	ok[0]["a"] = "b"
	// panic
	fmt.Println(ok[1])

	return "c"
}
