import sqlite3 as sql
import matplotlib.pyplot as plt


def init_db():
    connect = sql.connect('expenses.db')
    cursor = connect.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY, date TEXT, amount INTEGER, description TEXT, category TEXT)')
    connect.commit()


def add_expense(date, amount, description, category):
    connect = sql.connect('expenses.db')
    cursor = connect.cursor()
    cursor.execute('INSERT INTO expenses (date , amount, description, category) VALUES(?, ?, ?, ?)', (date, amount, description, category))
    connect.commit()
    connect.close()


def view_expenses():
    Connect = sql.connect('expenses.db')
    cursor = Connect.cursor()
    cursor.execute('SELECT * FROM expenses')
    fetch = cursor.fetchall()
    Connect.close()
    return fetch
    

    
    
def guess_description(description):
    categories ={
        "food": [
            # General
            "restaurant", "cafe", "coffee", "pizza", "burger", "kebab",
            "fast food", "bakery", "dessert", "ice cream",

            # Iran
            "snapp food", "zoodfood", "reyhoon",

            # Global
            "ubereats", "uber eats", "doordash", "grubhub",
            "deliveroo", "just eat", "foodpanda", "swiggy",
            "zomato", "talabat", "careem food", "glovo",
            "eatstreet", "postmates", "gojek"
        ],

        "transport": [
            # General
            "taxi", "cab", "ride", "rideshare",
            "bus", "metro", "subway", "train",
            "airport", "flight", "railway",

            # Iran
            "snapp", "tapsi", "maxim",

            # Global
            "uber", "lyft", "bolt", "grab",
            "ola", "careem", "didi", "gojek",
            "cabify", "free now", "yango", "indrive"
        ],

        "shopping": [
            # General
            "mall", "shopping", "market", "store", "shop",

            # Iran
            "digikala", "torob", "basalam",
            "emalls", "okala", "modiseh",
            "janebi", "hyperstar",

            # Global
            "amazon", "ebay", "etsy",
            "aliexpress", "alibaba",
            "temu", "wish",
            "walmart", "target",
            "costco", "best buy",
            "ikea", "flipkart",
            "rakuten", "mercado libre",
            "noon", "shopee", "lazada"
        ],

        "travel": [
            "booking", "booking.com",
            "airbnb", "expedia",
            "tripadvisor", "kayak",
            "agoda", "skyscanner",
            "hopper", "trip.com",
            "alibaba", "snaptrip",
            "jabama", "hotel", "hostel"
        ],

        "finance": [
            "paypal", "stripe", "wise",
            "revolut", "venmo",
            "cash app", "cashapp",
            "google pay", "apple pay",
            "samsung pay",
            "zarinpal", "idpay",
            "nextpay", "paytm",
            "phonepe"
        ],

        "social": [
            "instagram", "facebook",
            "twitter", "bird",
            "threads",
            "reddit", "linkedin",
            "telegram", "whatsapp",
            "messenger", "wechat",
            "line", "signal",
            "discord", "slack",
            "snapchat", "tiktok",
            "kakao", "viber"
        ],

        "video": [
            "youtube", "netflix",
            "prime video", "amazon prime",
            "disney+", "disney plus",
            "hulu", "max", "hbo max",
            "apple tv", "paramount+",
            "peacock",
            "filimo", "namava",
            "aparat", "twitch"
        ],

        "music": [
            "spotify", "apple music",
            "youtube music",
            "soundcloud",
            "deezer", "tidal",
            "pandora", "amazon music"
        ],

        "maps": [
            "google maps",
            "apple maps",
            "waze",
            "neshan",
            "balad",
            "here wego",
            "mapquest"
        ],

        "delivery": [
            "snappbox", "post",
            "dhl", "fedex", "ups",
            "usps", "aramex",
            "tnt", "dpd", "gls"
        ],

        "productivity": [
            "gmail", "outlook",
            "google drive",
            "dropbox", "onedrive",
            "google docs",
            "google sheets",
            "notion", "evernote",
            "trello", "asana",
            "clickup", "jira",
            "zoom", "teams",
            "google meet", "meet"
        ],

        "ai": [
            "chatgpt", "gemini",
            "claude", "copilot",
            "perplexity",
            "grok", "midjourney",
            "stable diffusion",
            "dall-e", "deepseek"
        ]
    }

    description = description.lower()
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in description:
                return category
            
    return 'uncategorized'
            

def get_category_totals():
    expenses = view_expenses()
    totals = {}
    for row in expenses:
        category = row[4]
        amount = row[2]
        if category in totals:
            totals[category] = totals[category] + amount
        else:
            totals[category] = amount
    return totals

    
def generate_pie_chart():
    totals = get_category_totals()
    if not totals:
        return
    labels = list(totals.keys())
    values = list(totals.values())
    
    plt.figure(figsize=(8, 6))
    wedges, texts, autotexts = plt.pie(values, autopct='%1.1f%%')
    plt.legend(wedges, labels, title="Categories", bbox_to_anchor=(1, 0.5), loc='center left')
    plt.tight_layout()
    plt.savefig('static/chart.png', bbox_inches='tight')
    plt.close()
    
    
def delete_expense(expense_id):
    Connect = sql.connect('expenses.db')
    cursor = Connect.cursor()
    cursor.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
    Connect.commit()
    Connect.close()
    
if __name__ == '__main__':
    generate_pie_chart()
    init_db()
    