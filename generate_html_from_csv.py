import csv
import json

INPUT_CSV = 'products.csv'
OUTPUT_HTML = 'index.html'

product_codes = []
product_info_map = {}

with open(INPUT_CSV, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='\t')
    for row in reader:
        code = row['sku'].strip()
        if not code:
            continue
        product_codes.append(code)
        name = f"{row['model'].strip()} {row['storage'].strip()} {row['color'].strip()}"
        price = int(row['price'].strip())
        product_info_map[code] = {
            "name": name,
            "expectedPrice": price
        }

# HTML-шаблон
html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Samsung Product Stock Checker</title>
  <link
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
          rel="stylesheet"
  >
  <style>
    body {{ padding: 2rem; }}
    .table td, .table th {{ vertical-align: middle; }}
  </style>
</head>
<body>
<div class="container">
  <h2 class="mb-4">Samsung Product Stock Status</h2>
  <table class="table table-bordered table-hover">
    <thead class="table-dark">
    <tr>
      <th>Product Code</th>
      <th>Product Name</th>
      <th>Stock Status</th>
      <th>Stock Level</th>
      <th>Price</th>
      <th>Expected Price</th>
    </tr>
    </thead>
    <tbody id="productTableBody"></tbody>
  </table>
</div>

<script>
  const productCodes = {json.dumps(product_codes, indent=2)};

  const productInfoMap = {json.dumps(product_info_map, indent=2)};

  fetch(`https://api.shop.samsung.com/tokocommercewebservices/v2/nl/products?productCodes=${{productCodes.join(',')}}`)
    .then(res => res.json())
    .then(data => {{
      const tbody = document.getElementById("productTableBody");

      data.forEach(product => {{
        const row = document.createElement("tr");

        const productInfo = productInfoMap[product.code] || {{}};
        const expectedPrice = productInfo.expectedPrice;
        const actualPrice = product.price?.value;

        let rowClass = "table-danger";

        const status = product.stock?.stockLevelStatus;

        if (status === "outOfStock") {
        rowClass = "table-danger";
        } else if (actualPrice !== expectedPrice) {
        rowClass = "table-warning";
        } else if (status === "inStock" || status === "preOrder") {
        rowClass = "table-success";
        }

        row.classList.add(rowClass);

        const productName = productInfo.name || "(Unknown)";

        row.innerHTML = `
          <td>${{product.code}}</td>
          <td>${{productName}}</td>
          <td>${{product.stock?.stockLevelStatus || "n/a"}}</td>
          <td>${{product.stock?.stockLevel ?? "n/a"}}</td>
          <td>${{product.price?.formattedValue || "n/a"}}</td>
          <td>€ ${{expectedPrice ?? "n/a"}}</td>
        `;

        tbody.appendChild(row);
      }});
    }})
    .catch(err => {{
      console.error("Ошибка загрузки данных:", err);
    }});
</script>
</body>
</html>"""

with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f"✅ HTML-файл создан: {OUTPUT_HTML}")
