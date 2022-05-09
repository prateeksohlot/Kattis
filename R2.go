package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {

	var first, mean int
	second := 0
	var r = bufio.NewReader(os.Stdin)

	fmt.Fscanf(r, "%d %d", &first, &mean) //input for space seperated inputs
	// fmt.Printf("%d %d", a, b)

	second = 2*mean - first

	fmt.Printf("%d", second)
}
