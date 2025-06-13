import streamlit as st

# Data Ikan dan Alat Tangkap
data = [
    {"ikan": "Cakalang", "alat": "Rawai Tuna", "cluster": 2},
    {"ikan": "Bawal Hitam", "alat": "Jaring Insang Hanyut", "cluster": 2},
    {"ikan": "Layangan Benggol", "alat": "Pukat Cincin Pelagis", "cluster": 0},
    {"ikan": "Kerapu Karang", "alat": "Bubu", "cluster": 0},
    {"ikan": "Lemuru", "alat": "Bouke Ami", "cluster": 0},
    {"ikan": "Tenggiri", "alat": "Pancing Ulur", "cluster": 1},
    {"ikan": "Rajungan", "alat": "Bagan Berperahu", "cluster": 1},
]

# HTML dan CSS untuk tema dan desain responsif
html_content = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alat Tangkap Ikan dan Clustering</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f0f8ff; /* Biru muda untuk tema perikanan */
            margin: 0;
            padding: 0;
            color: #333;
        }

        header {
            background-color: #0288d1; /* Biru laut gelap */
            color: white;
            padding: 30px;
            text-align: center;
            font-size: 2.5rem;
            border-bottom: 5px solid #01579b; /* Pembatas bawah */
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }

        .container {
            padding: 40px;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0px 6px 20px rgba(0, 0, 0, 0.1);
            margin: 50px auto;
            max-width: 800px;
            transition: transform 0.3s ease;
        }

        .container:hover {
            transform: scale(1.02);
        }

        h2 {
            color: #0288d1;
            text-align: center;
            font-size: 2rem;
        }

        label {
            font-size: 1.1rem;
            font-weight: bold;
            display: block;
            margin: 10px 0;
        }

        select, button {
            width: 100%;
            padding: 12px;
            margin: 12px 0;
            font-size: 1.1rem;
            border-radius: 5px;
            border: 1px solid #0288d1;
            box-sizing: border-box;
        }

        select:focus, button:focus {
            outline: none;
            border-color: #01579b;
            box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
        }

        .result {
            margin-top: 20px;
        }

        .result-item {
            padding: 20px;
            margin-bottom: 15px;
            background-color: #f1f8ff;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            transition: background-color 0.3s;
        }

        .result-item:hover {
            background-color: #e0f7fa;
        }

        .footer {
            background-color: #0288d1;
            color: white;
            padding: 10px 0;
            text-align: center;
            position: fixed;
            bottom: 0;
            width: 100%;
        }

        .cluster-info {
            margin-top: 30px;
            padding: 25px;
            background-color: #e3f2fd;
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }

        .cluster-info h3 {
            color: #0288d1;
            font-size: 1.5rem;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <header>
        <h1>Alat Tangkap Ikan dan Clustering</h1>
    </header>

    <div class="container">
        <h2>Temukan Data Alat Tangkap dan Jenis Ikan</h2>

        <!-- Kolom Pilihan Alat Tangkap -->
        <label for="gear-select">Pilih Alat Tangkap:</label>
        <select id="gear-select">
            <option value="all">Semua Alat Tangkap</option>
            <option value="Rawai Tuna">Rawai Tuna</option>
            <option value="Jaring Insang Hanyut">Jaring Insang Hanyut</option>
            <option value="Pukat Cincin Pelagis">Pukat Cincin Pelagis</option>
            <option value="Bubu">Bubu</option>
            <option value="Bouke Ami">Bouke Ami</option>
            <option value="Pancing Ulur">Pancing Ulur</option>
            <option value="Bagan Berperahu">Bagan Berperahu</option>
        </select>

        <div id="result-container" class="result">
            <!-- Data akan dimasukkan secara dinamis melalui JavaScript -->
        </div>

        <!-- Informasi Cluster -->
        <div id="cluster-info" class="cluster-info">
            <h3>Informasi Tentang Cluster</h3>
            <p><strong>Cluster 0:</strong> Ikan-ikan dalam cluster ini cenderung memiliki nilai dan volume produksi yang lebih rendah. Mereka sering kali ditangkap menggunakan alat tangkap tradisional atau kecil, seperti "Bubu" dan "Jaring Insang Hanyut." Ikan dalam cluster ini mencakup jenis yang kurang bernilai ekonominya namun memiliki potensi pasar lokal yang besar.</p>
            <p><strong>Cluster 1:</strong> Cluster ini terdiri dari ikan-ikan yang lebih bernilai komersial dan sering kali ditangkap dengan alat tangkap yang lebih besar dan modern. Alat tangkap yang digunakan seperti "Bagan Berperahu" dan "Pancing Ulur," yang menunjukan usaha penangkapan dengan skala yang lebih besar dan komersial. Ikan di cluster ini lebih sering dikonsumsi secara luas di pasar internasional.</p>
            <p><strong>Cluster 2:</strong> Ikan-ikan dalam cluster ini adalah yang paling bernilai dan memiliki produksi yang tinggi. Mereka ditangkap menggunakan metode industri dan teknologi canggih seperti "Rawai Tuna" dan "Jaring Insang Hanyut." Cluster ini berfokus pada ikan-ikan yang memiliki permintaan tinggi dan sangat penting untuk sektor perikanan komersial.</p>
        </div>
    </div>

    <div class="footer">
        <p>&copy; 2025 Alat Tangkap Ikan - Semua Hak Cipta Dilindungi</p>
    </div>

    <script>
        // Menambahkan interaksi dengan JavaScript
        document.getElementById('gear-select').addEventListener('change', function() {
            var selectedGear = this.value;
            var resultContainer = document.getElementById('result-container');
            resultContainer.innerHTML = '';

            // Filter data berdasarkan alat tangkap
            var filteredData = [
                { ikan: "Cakalang", alat: "Rawai Tuna", cluster: 2 },
                { ikan: "Bawal Hitam", alat: "Jaring Insang Hanyut", cluster: 2 },
                { ikan: "Layangan Benggol", alat: "Pukat Cincin Pelagis", cluster: 0 },
                { ikan: "Kerapu Karang", alat: "Bubu", cluster: 0 },
                { ikan: "Lemuru", alat: "Bouke Ami", cluster: 0 },
                { ikan: "Tenggiri", alat: "Pancing Ulur", cluster: 1 },
                { ikan: "Rajungan", alat: "Bagan Berperahu", cluster: 1 }
            ];

            if (selectedGear !== 'all') {
                filteredData = filteredData.filter(item => item.alat === selectedGear);
            }

            filteredData.forEach(item => {
                const resultItem = document.createElement('div');
                resultItem.classList.add('result-item');
                resultItem.innerHTML = `
                    <h3>${item.ikan}</h3>
                    <p><strong>Alat Tangkap:</strong> ${item.alat}</p>
                    <p><strong>Cluster:</strong> ${item.cluster}</p>
                `;
                resultContainer.appendChild(resultItem);
            });
        });
    </script>
</body>
</html>
"""

# Menampilkan HTML dan JavaScript menggunakan st.components.v1.html
components.html(html_content, height=1000, width=900)
