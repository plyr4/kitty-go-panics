package pkg_b

import (
	"github.com/plyr4/kitten-go/pkg_c"
)

func B() string {
	return pkg_c.C()
}
