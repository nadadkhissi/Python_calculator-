print("🤖 Welcome to the Smart Calculator \n")

# Operation history
history = []

while True:
    try:
        print("=" * 40)
        num1 = float(input("🔢 First number: "))
        oper = input("⚡ Operation (+, -, *, /, %): ").strip()
        num2 = float(input("🔢 Second number: "))
        
        print("\n📊 Results:")
        print("-" * 25)
        
        if oper == '+':
            result = num1 + num2
            print(f"➕ Addition: {num1} + {num2} = {result}")
        elif oper == '-':
            result = num1 - num2
            print(f"➖ Subtraction: {num1} - {num2} = {result}")
        elif oper == '*':
            result = num1 * num2
            print(f"✖️ Multiplication: {num1} × {num2} = {result}")
        elif oper == '/':
            if num2 != 0:
                result = num1 / num2
                print(f"➗ Division: {num1} ÷ {num2} = {result}")
            else:
                print("❌ Error: Cannot divide by zero!")
                continue
        elif oper == '%':
            result = num1 % num2
            print(f"📈 Modulo: {num1} % {num2} = {result}")
        else:
            print("❌ Invalid operation! Choose from (+, -, *, /, %)")
            continue
        
        # Save to history
        history.append(f"{num1} {oper} {num2} = {result}")
        print(f"\n💾 Saved to history")
        
        # Show last 3 operations
        if len(history) >= 1:
            print("\n📋 Recent operations:")
            for i, h in enumerate(history[-3:], 1):
                print(f"  {i}. {h}")
        
        # Moroccan VAT feature (20%)
        vat = result * 0.20
        print(f"\n💰 With 20% VAT: {result + vat:.2f} MAD")
        
        again = input("\n🔄 Another calculation? (y/n): ").lower()
        if again != 'y':
            print("👋 Thank you for using the Smart Calculator!")
            break
            
    except ValueError:
        print("❌ Error: Please enter valid numbers only!")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
