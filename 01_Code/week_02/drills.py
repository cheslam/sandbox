def sum_list(numbers: list[int]) -> int:
    """Returns the sum of a list of numbers"""
    total = 0
    for n in numbers:
        total += n
    return total

raw = input("Enter your list of numbers:").strip()

try:
    nums = [int(x) for x in raw.replace(",", " ").split()]
except ValueError:
    print("Please enter only integers, separated by spaces or commas.")
    raise SystemExit(1)


result = sum_list(nums)
print(f"The sum of your list is: {result}")

# %%
def reverse_string(s: str) -> str:
    """Reverses a given string"""
    final = len(s) - 1
    new = []
    for c in s:
        new.append(s[final])
        final -= 1
    result = "".join(new)
    return result

raw = input("Type your string:")

result = reverse_string(raw)
print(result)
        

# %%
def count_vowels(s: str) -> int:
    """Counts the number of vowels in a string (not including y)"""
    vowels = {"a", "e", "i", "o", "u"}
    v_count = 0
    for c in s:
        c = c.lower()
        if c in vowels:
            v_count += 1
    
    return v_count

raw = input("Type your string:")

result = count_vowels(raw)
print(f"There are {result} vowels in your string.")
# %%
