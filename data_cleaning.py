import pandas as pd
df = pd.read_csv('GooglePlayStore_wild.csv')


# Виведи інформацію про всі DataFrame, щоб дізнатися, які стовпці потребують очищення

# Скільки в датасеті додатків, у яких не вказано (NaN) рейтинг (Rating)?

norat = df[pd.isnull(df['Rating'])]
#print(len(norat))

# Заміни порожнє значення ('NaN') рейтингу ('Rating') для таких програм на -1.

df['Rating'].fillna(-1, inplace=True) #inplace = змінюємо саме у документі 
# Визнач, яке ще значення розміру ('Size') зберігається в датасеті крім Кілобайтів та Мегабайтів, заміни його на -1.
# Перетвори розміри додатків ('Size') у числовий формат (float). Розмір усіх програм повинен вимірюватися в Мегабайтах.

print(df['Size'].value_counts())

def size_cleaning(size):
    if size[-1] == 'M':
        return float(size[:-1])
    elif size[-1] == 'k':
        return float(size[:-1]) / 1024
    return -1

df['Size'] = df['Size'].apply(size_cleaning)


# Чому дорівнює максимальний розмір ('Size') додатків з категорії ('Category') 'TOOLS'?
tools = df[df['Category'] == 'TOOLS']
print(tools['Size'].max())

# Бонусні завдання
# Заміни тип даних на цілий (int) для кількості установок ('Installs').

def clean_inst(installs):
    if installs[-1] == "+":
        what = installs[:-1].replace(',', '')
        return int(what)
    else:
        return 0
df['Installs'] = df['Installs'].apply(clean_inst)

def price_clean(size):
    if size[0] == '$':
        return float(size[1:])
    return 0 
df['Price'] = df['Price'].apply(price_clean)
# У записі кількості установок ('Installs') знак "+" необхідно ігнорувати.
# Тобто, якщо в датасеті кількість установок дорівнює 1,000,000+, необхідно змінити значення на 1000000

# Згрупуй дані за категорією ('Category') та цільовою аудиторією ('Content Rating') будь-яким зручним для тебе способом,
# Порахуй середню кількість установок ('Installs') у кожній групі. Результат округлили до десятих.
# В отриманій таблиці знайди клітинку з найбільшим значенням.
# До якої вікової групи та типу додатків відносяться дані з цієї клітинки?

# У якої програми не вказаний тип ('Type')? Який тип там потрібно записати залежно від ціни?

# Виведи інформацію про все DataFrame, щоб переконатися, що очищення пройшло успішно

def create_month(date):
    if date != '':
        month = date.split()[0]
        return month
    else:
        return ''
    
df['Month'] = df['Last Updated'].apply(create_month)



df['Profit'] = df['Installs'] * df['Price']
df.to_csv('cleaned.csv', index=False)
df.info()