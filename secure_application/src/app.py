import sqlite3

def init_db():
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT, name TEXT, pass TEXT, balance REAL)")
    cursor.execute("DELETE FROM users")
    cursor.execute("INSERT INTO users VALUES (1, 'alice', 'pass123', 5000.0)")
    cursor.execute("INSERT INTO users VALUES (2, 'bob', 'pass456', 10000.0)")
    conn.commit()
    conn.close()

# Vulnerability 1: SQL Injection
def login(username, password):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    # Direct string concatenation causes SQLi
    query = f"SELECT * FROM users WHERE name = '{username}' AND pass = '{password}'"
    
    # Vulnerability 2: Sensitive Data Exposure (Printing credentials)
    print(f"[LOG]: Attempted login with Password: {password}")
    
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    return user

# Vulnerability 3: Broken Access Control (IDOR)
def check_balance(account_id):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    # Does not check if the logged-in user owns this account_id
    cursor.execute("SELECT name, balance FROM users WHERE id = ?", (account_id,))
    data = cursor.fetchone()
    conn.close()
    return data

def transfer_money(sender_id, receiver_id, amount):
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET balance = balance - ? WHERE id = ?", (amount, sender_id))
    cursor.execute("UPDATE users SET balance = balance + ? WHERE id = ?", (amount, receiver_id))
    conn.commit()
    conn.close()
    print("Transfer successful!")

def main():
    init_db()
    print("=== Simple Online Banking ===")
    
    u = input("Username: ")
    p = input("Password: ")
    user = login(u, p)
    
    if user:
        print(f"\nWelcome, {user[1]}!")
        print("1. Check Balance")
        print("2. Transfer Money")
        
        choice = input("Choice: ")
        if choice == '1':
            acc_id = input("Enter Account ID to check balance: ")
            bal = check_balance(acc_id)
            print(f"Account Data: {bal}")
        elif choice == '2':
            rec = input("Recipient ID: ")
            amt = float(input("Amount: "))
            transfer_money(user[0], rec, amt)
    else:
        print("Login failed.")

if __name__ == "__main__":
    main()