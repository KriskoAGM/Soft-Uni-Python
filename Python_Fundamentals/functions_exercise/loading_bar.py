def check_progress(num):
    if num == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    return f"{num}% [{'%'*(num // 10)}{'.'*(10 - num // 10)}]\nStill loading..."


number = int(input())
print(check_progress(number))
