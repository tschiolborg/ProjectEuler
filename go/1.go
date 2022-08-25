package main

import "fmt"

func main() {
	a := 3
	b := 5
	n := 1000

	sum := sumMultiple(n, a, b)

	fmt.Println(sum)
}

func sumMultiple(n, a, b int) int {
	sum := 0
	for i := 1; i < n; i++ {
		if i%a == 0 || i%b == 0 {
			sum += i
		}
	}
	return sum
}
