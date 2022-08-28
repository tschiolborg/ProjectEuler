package main

import (
	"fmt"
	"math"
)

func main() {

	n := 600851475143

	result := findLargestPrime(n)

	fmt.Println(result)
}

func findLargestPrime(n int) int {
	i := 2

	for i < int(math.Sqrt(float64(n))) {
		for n%i == 0 && n != i {
			n /= i
		}
		if i != 2 {
			i++
		}
		i++
	}
	return n
}
