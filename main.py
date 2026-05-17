n = float(input("Digite um numero: "))

print("=" * 35)
print("       SUPER TABUADA")
print("=" * 35)

print("\n--- MULTIPLICACAO ---")

for i in range(1,11):
    print(f"{n} x {i} = {n*i}")

print("-" * 35)

print("\n--- DIVISAO ---")

for i in range(1,11):
    print(f"{n} / {i} = {n/i:.2f}")

print("-" * 35)

print("\n--- SOMA ---")

for i in range(1,11):
    print(f"{n} + {i} = {n+i}")

print("-" * 35)

print("\n--- SUBTRACAO ---")

for i in range(1,11):
    print(f"{n} - {i} = {n-i}")

print("-" * 35)

print("\nFim da tabuada")