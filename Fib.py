
def fibonacci(n):
  previous_num = 1
  next_num = 0
  current_num = 1

  fib_sequence = []
  for _ in range(n):

    fib_sequence.append(previous_num)
    # Update the Fibonacci numbers
    next_num = previous_num + current_num

    previous_num = current_num

    current_num = next_num
  return fib_sequence


if __name__ == "__main__":
  n = int(input("Enter the number of Fibonacci numbers to generate: "))
  fib_sequence = fibonacci(n)

  print(f"The first {n} Fibonacci numbers are: {fib_sequence}")