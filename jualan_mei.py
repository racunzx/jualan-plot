import matplotlib.pyplot as plt
import numpy as np
import datetime

# Data jualan dan QR MEI 2025
sales_data = [
    ("1.5.2025", 350),
    ("2.5.2025", 265),
    ("3.5.2025", 223),
    ("4.5.2025", 278),
    ("5.5.2025", 229),
    ("6.5.2025", 276),
    ("7.5.2025", 264),
    ("9.5.2025", 1139),
    ("10.5.2025", 1577),
    ("11.5.2025", 1584),
    ("13.5.2025", 298),
    ("14.5.2025", 179),
    ("15.5.2025", 224),
    ("16.5.2025", 308),
    ("17.5.2025", 310),
    ("18.5.2025", 410),
    ("19.5.2025", 159),
    ("20.5.2025", 375),
]

# Proses data
label_x = []
sale = []

for date_str, s in sales_data:
    date_obj = datetime.datetime.strptime(date_str, "%d.%m.%Y")
    day_name = date_obj.strftime("%A")  # Dapatkan nama hari dalam English
    label = f"{day_name} ({date_str})"
    label_x.append(label)
    sale.append(s)

# Jumlah dan purata jualan
jumlah_sale = sum(sale)
purata_sale = jumlah_sale / len(sale)

# Plot
fig, ax = plt.subplots(figsize=(14, 7))
x_indexes = np.arange(len(label_x))
color_sale = '#28B463'

ax.bar(x_indexes, sale, color=color_sale, label='Jualan Harian')

# Tambah garis purata
ax.axhline(purata_sale, color='blue', linestyle='--', linewidth=2, label=f'Purata: RM {purata_sale:.2f}')
ax.text(len(sale) - 1, purata_sale + 5, f"Purata RM {purata_sale:.2f}", color='blue', ha='right')

# Label dan grid
ax.set_xlabel("Hari dan Tarikh")
ax.set_ylabel("Jualan (RM)")
ax.set_title("Jualan Harian")
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.set_xticks(x_indexes)
ax.set_xticklabels(label_x, rotation=45, ha="right")

# Label bar
for i, txt in enumerate(sale):
    ax.text(i, txt + 5, str(txt), ha='center', fontsize=8)

# Total jualan di bawah
fig.text(0.1, 0.01, f"Total Jualan: RM {jumlah_sale:.2f}", fontsize=12, color='red')

# Legend
ax.legend()

plt.tight_layout()
plt.savefig("graf_jualan_mei.png")
plt.show()
