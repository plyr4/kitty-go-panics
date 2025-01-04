package pkg_a

import (
	"fmt"

	"github.com/plyr4/kitten-go/pkg_b"
)

func A() {
	b := pkg_b.B()
	fmt.Println(b)
}
