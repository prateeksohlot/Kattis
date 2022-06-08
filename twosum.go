package main

import (
	"bufio"
	"fmt"
	"os"
)
`
func main() {
	var a, b int
	var r = bufio.NewReader(os.Stdin)

	fmt.Fscanf(r, "%d %d", &a, &b)

	fmt.Println(a + b)
}
`
