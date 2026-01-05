package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	// Read input from stdin or file
	scanner := bufio.NewScanner(os.Stdin)
	
	position := 50 // Starting position
	zeroCount := 0 // Count how many times dial points at 0
	zeroPassCount := 0 // Count how many times dial passes 0 (not just ends at 0)
	
	fmt.Printf("Starting position: %d\n", position)
	
	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		if line == "" {
			continue
		}
		
		// Parse the rotation instruction
		direction := line[0]
		distance, err := strconv.Atoi(line[1:])
		if err != nil {
			fmt.Fprintf(os.Stderr, "Error parsing line '%s': %v\n", line, err)
			continue
		}
		
		// Store previous position before rotation
		prevPosition := position
		
		// Apply the rotation
		if direction == 'L' {
			// Left means toward lower numbers (subtract)
			position = (position - distance) % 100
			// Handle negative wrap-around
			if position < 0 {
				position += 100
			}
		} else if direction == 'R' {
			// Right means toward higher numbers (add)
			position = (position + distance) % 100
		} else {
			fmt.Fprintf(os.Stderr, "Invalid direction '%c' in line '%s'\n", direction, line)
			continue
		}
		
		fmt.Printf("Rotated %c%d to point at %d\n", direction, distance, position)
		
		// Check if dial points at 0
		if position == 0 {
			zeroCount++
		}
		
		// Count how many times we pass through 0 during rotation
		// We need to count multiple passes if distance is large enough
		// BUT: if we start at position 0, don't count it as a pass
		passes := 0
		if prevPosition != 0 {
			if direction == 'L' {
				// Moving left (counterclockwise, decreasing numbers)
				// Calculate how many times we cross 0
				// If we're at position 5 and move left 105, we cross 0 once (at step 5) and end at 0
				// If we're at position 5 and move left 205, we cross 0 twice
				if distance >= prevPosition {
					// We at least cross 0 once
					passes = 1 + (distance - prevPosition) / 100
				}
			} else if direction == 'R' {
				// Moving right (clockwise, increasing numbers)
				// If we're at position 95 and move right 105, we cross 0 once (at step 5) and end at 0
				// If we're at position 95 and move right 205, we cross 0 twice
				if distance + prevPosition >= 100 {
					// We at least cross 0 once
					passes = 1 + (distance + prevPosition - 100) / 100
				}
			}
		}
		
		zeroPassCount += passes
		if passes > 0 {
			fmt.Printf("  -> Passed through 0 a total of %d time(s)\n", passes)
		}
	}
	
	if err := scanner.Err(); err != nil {
		fmt.Fprintf(os.Stderr, "Error reading input: %v\n", err)
		os.Exit(1)
	}

	fmt.Printf("\nThe dial ended on 0 a total of %d times.\n", zeroCount)
	fmt.Printf("The dial passed 0 a total of %d times.\n", zeroPassCount)
	fmt.Printf("Password (part 1): %d\n", zeroCount)
	fmt.Printf("Password (part 2): %d\n", zeroPassCount)
}
