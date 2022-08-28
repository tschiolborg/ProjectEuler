package main

import (
	"fmt"
	"math"
	"strconv"
)

func main() {

	n := 3

	p, x, y := largestPalindrome(n)

	fmt.Println(p, x, y)
}

func largestPalindrome(n int) (int, int, int) {
	p, x, y := 0, 0, 0

	min := powInt(10, n-1)
	max := powInt(10, n) - 1

	for i := max; i > min; i-- {
		for j := max; j > i; j-- {
			k := i * j
			if k < p {
				break
			}
			if isPalindrome(strconv.Itoa(k)) {
				p, x, y = k, i, j
			}
		}
	}

	return p, x, y
}

func isPalindrome(s string) bool {
	for i := 0; i < len(s)/2+1; i++ {
		if s[i] != s[len(s)-1-i] {
			return false
		}
	}
	return true
}

func powInt(x, y int) int {
	return int(math.Pow(float64(x), float64(y)))
}
