# 📱 Samsung Product Stock Checker — User Guide

Welcome! This page helps you monitor the **live stock and pricing** of Samsung products across two countries — the **Netherlands (NL)** and **Belgium (BE)** — all in one place, updated automatically.

---

## 🚀 Getting Started

When you open the page, it will **automatically load** all product data for you. No need to click anything — just open it and the tables will populate within a few seconds.

> ℹ️ The product list is taken from the latest uploaded inventory file. If no file has been uploaded yet, the tables will be empty. See the [Uploading Inventory](#-uploading-your-inventory-file) section below.

---

## 🗂️ What's on the Page

### Two Stock Tables

You will see **two tables** on the page:

| Table | Description |
|---|---|
| **Samsung Product Stock Status — NL** | Live stock data for the Netherlands |
| **Samsung Product Stock Status — BE** | Live stock data for Belgium |

Both tables show the same set of products but reflect the prices and stock levels for each country separately.

---

## 📋 What Each Column Means

| Column | What it shows |
|---|---|
| **Product Code** | The unique Samsung model identifier (e.g. `SM-F766BZKHEUB`) |
| **Product Name** | The human-readable product name from your inventory file |
| **Stock Status** | Whether the product is currently available (`inStock`, `outOfStock`, `preOrder`) |
| **Stock Level** | The exact number of units available in Samsung's system |
| **Current Price** | The live price shown on Samsung's website right now |
| **Initially Briefed Price** | The expected/reference price from your uploaded inventory file |
| **Shipping ETA** | Estimated delivery date if available |
| **BackOrder ETA** | If the product is on back-order, when it's expected to be available |

---

## 🎨 What the Row Colours Mean

Each row is colour-coded so you can instantly spot what needs attention:

| Colour | Meaning |
|---|---|
| 🟥 **Red** | Product is **out of stock** |
| 🟨 **Yellow** | Product is in stock, but the **current price differs** from your briefed price |
| 🟩 **Green** | Product is **in stock** (or available for pre-order) and the price matches your briefed price |

> 💡 **Tip:** Yellow rows are the ones to watch closely — they mean Samsung has changed the price since you uploaded your inventory file.

---

## 🔄 Automatic Refresh

The page **automatically refreshes every 10 minutes** to always show you the latest data.

In the **top-right corner** of the page you will see a small panel showing:
- **Last update** — the time the data was last loaded
- **Next update** — a live countdown to the next automatic refresh

You can also manually refresh the page at any time by pressing `F5` or `Cmd+R` / `Ctrl+R`.

---

## 📤 Uploading Your Inventory File

The product list and reference prices come from an **Excel file (.xlsx)** that you upload to the server. This only needs to be done when your product list or briefed prices change.

### How to Upload

Use the dedicated upload endpoint on the server. Once uploaded, the page will automatically use the new data on the next refresh.

### What the Excel File Should Look Like

Your spreadsheet should have the following columns (the order does not matter):

| Column Name | Description |
|---|---|
| `Base SKU` | The Samsung product code (e.g. `SM-F766BZKHEUB`) |
| `Model Name` | The product name |
| `SKU` | Regional SKU if different |
| `Color` | Product colour |
| `Memory` | Storage/memory size |
| `RRP` | Recommended Retail Price (your briefed price) |

> ℹ️ The first row of the spreadsheet must be the column headers. All other rows are treated as products.

---

## ⚠️ Error Messages

If something goes wrong (e.g. the server is unavailable or no inventory has been uploaded), a **red banner** will appear at the top of the page with a short description of the problem.

You can **dismiss the banner** by clicking the **✕ close button** on the right side of it. This does not fix the underlying issue — it just hides the message.

Common messages you might see:

| Message | What it means |
|---|---|
| *No inventory data uploaded yet* | No Excel file has been uploaded to the server yet |
| *Failed to fetch product data* | The server could not be reached (check your connection or server status) |
| *Upstream error: 5xx* | Samsung's API is temporarily unavailable |

---

## 🔒 A Note on Data

- This page **does not store any data in your browser** — everything is fetched fresh from the server each time.
- The product list and prices come directly from **Samsung's official API**, so they reflect real-time information.
- Your uploaded inventory file is stored securely on the server and used only to match product names and reference prices.

---

*If you have questions or notice something unexpected, please contact your system administrator.*

