# phonebook.py
import csv
import json
import os
from datetime import date
from connect import get_connection

# Helper class to properly serialize date objects into JSON format
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.isoformat()
        return super().default(obj)

def init_db():
    """Initializes the database by running schema and procedure SQL files."""
    conn = get_connection()
    if not conn: return
    try:
        with conn.cursor() as cur:
            if os.path.exists('schema.sql'):
                with open('schema.sql', 'r', encoding='utf-8') as f:
                    cur.execute(f.read())
            if os.path.exists('procedures.sql'):
                with open('procedures.sql', 'r', encoding='utf-8') as f:
                    cur.execute(f.read())
        conn.commit()
        print("Database initialized successfully.")
    except Exception as e:
        print(f"Initialization error: {e}")
    finally:
        conn.close()

def export_to_json():
    """Exports all contacts, including their phones and groups, to a JSON file."""
    conn = get_connection()
    with conn.cursor() as cur:
        # Fetch combined data using JOINs and array_agg for multiple phones
        cur.execute("""
            SELECT c.name, c.surname, c.email, c.birthday, g.name, 
                   array_agg(p.phone || ' (' || p.type || ')') 
            FROM contacts c
            LEFT JOIN groups g ON c.group_id = g.id
            LEFT JOIN phones p ON c.id = p.contact_id
            GROUP BY c.id, g.name
        """)
        rows = cur.fetchall()
        
        # Format the data into a list of dictionaries
        data = [{"name": r[0], "email": r[2], "birthday": r[3], "group": r[4], "phones": r[5]} for r in rows]
        
        with open("contacts.json", "w", encoding="utf-8") as f:
            json.dump(data, f, cls=DateEncoder, indent=4)
            
    print("Successfully exported to contacts.json")
    conn.close()

def paginated_view():
    """Displays contacts with a limit/offset mechanism for pagination."""
    limit = 3
    offset = 0
    while True:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT name, email, birthday FROM contacts ORDER BY id LIMIT %s OFFSET %s", (limit, offset))
            rows = cur.fetchall()
            
            print(f"\n--- Page {(offset//limit)+1} ---")
            for r in rows: 
                print(f"Name: {r[0]} | Email: {r[1]} | Birthday: {r[2]}")
            
            cmd = input("\n[n] Next | [p] Prev | [q] Quit: ").lower()
            if cmd == 'n': 
                offset += limit
            elif cmd == 'p': 
                offset = max(0, offset - limit)
            elif cmd == 'q': 
                break
        conn.close()

def main_menu():
    """Main application loop."""
    init_db()  # Run DB setup on startup
    
    while True:
        print("\n--- PHONEBOOK EXTENDED ---")
        print("1. View Contacts (Paginated)")
        print("2. Add Phone (Procedure)")
        print("3. Change Group (Procedure)")
        print("4. Search (Function)")
        print("5. Export to JSON")
        print("6. Exit")
        
        choice = input("Select an option: ")
        conn = get_connection()
        cur = conn.cursor()

        try:
            if choice == '1':
                paginated_view()
                
            elif choice == '2':
                name = input("Contact Name: ")
                phone = input("Phone Number: ")
                ptype = input("Type (home/work/mobile): ")
                
                # Explicitly cast types to ::varchar to prevent PostgreSQL type mismatch errors
                cur.execute("CALL add_phone(%s::varchar, %s::varchar, %s::varchar)", (name, phone, ptype))
                conn.commit()
                print("Phone number added successfully.")
                
            elif choice == '3':
                name = input("Contact Name: ")
                group = input("New Group Name: ")
                
                cur.execute("CALL move_to_group(%s::varchar, %s::varchar)", (name, group))
                conn.commit()
                print("Group updated successfully.")
                
            elif choice == '4':
                query = input("Enter name, email, or phone: ")
                cur.execute("SELECT * FROM search_contacts(%s)", (query,))
                for r in cur.fetchall(): 
                    print(r)
                    
            elif choice == '5':
                export_to_json()
                
            elif choice == '6':
                print("Exiting application...")
                break
                
        except Exception as e:
            print(f"Error: {e}")
            conn.rollback()
        finally:
            cur.close()
            conn.close()

if __name__ == "__main__":
    main_menu()