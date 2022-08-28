package main

import "fmt"

func main() {

	n := 4_000_000

	sum := fibSum(n)

	fmt.Println(sum)
}

// sum of all even fibonacci numbers
// we only need to add every third number (c)
func fibSum(n int) int {
	sum := 0

	a := 1
	b := 1
	c := 2

	for b < n {
		sum += c
		a = c + b
		b = a + c
		c = b + a
	}

	return sum
}
