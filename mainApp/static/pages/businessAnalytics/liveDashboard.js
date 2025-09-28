    const body = document.body;
    const darkModeSwitch = document.getElementById('darkModeSwitch');
    const dynamicContent = document.getElementById('dynamic-content');
    const contentTitle = document.getElementById('content-title');
    const navLinks = document.querySelectorAll('.sidebar .nav-link');

    // Dummy Grafik Fonksiyonları
    function generateBarChart(data, labels) {
        let bars = '';
        data.forEach((height, index) => {
            const color = index === 0 ? '#3498db' : (index === 1 ? '#2ecc71' : '#f39c12');
            bars += `<div class="bar" style="height: ${height}%; background-color: ${color};">
                        <span class="bar-label">${labels[index]}</span>
                    </div>`;
        });
        // Dummy X Ekseni Çizgisi
        const xAxisLine = `<div style="position: absolute; bottom: 15px; left: 0; right: 0; height: 1px; background-color: var(--text-light); opacity: 0.5;"></div>`;

        return `<div class="chart-dummy" style="align-items: flex-end; height: 250px; background-color: var(--body-bg); border: 1px dashed var(--text-light);">${xAxisLine}${bars}</div>`;
    }

    function generatePieChart(data) {
        // Data format: [{label: 'A', percent: 35, color: '#2ecc71'}, ...]
        let gradientStops = [];
        let currentStop = 0;
        
        data.forEach(item => {
            let nextStop = currentStop + item.percent;
            gradientStops.push(`${item.color} ${currentStop}% ${nextStop}%`);
            currentStop = nextStop;
        });

        const pieStyle = gradientStops.join(', ');
        const legend = data.map(item => `
            <div class="d-flex align-items-center mb-2">
                <div style="width: 10px; height: 10px; background-color: ${item.color}; border-radius: 50%; margin-right: 8px;"></div>
                <span class="small">${item.label}: <span class="fw-bold">${item.percent}%</span></span>
            </div>
        `).join('');

        return `
            <div class="row">
                <div class="col-6 d-flex justify-content-center">
                    <div class="pie-dummy" style="background: conic-gradient(${pieStyle});"></div>
                </div>
                <div class="col-6 d-flex flex-column justify-content-center">
                    ${legend}
                </div>
            </div>
        `;
    }

    // DYNAMIC CONTENT HTML TEMPLATES
    const TEMPLATES = {
        overview: `
            <div class="row g-4">
                <div class="col-lg-3 col-md-6">
                    <div class="content-card text-center" style="border-top-color: var(--primary-color);">
                        <i class="bi bi-box-fill text-primary-custom mb-3" style="font-size: 2rem;"></i>
                        <p class="small text-muted mb-1">Stok Doğruluğu</p>
                        <div class="kpi-value text-primary-custom">99.8%</div>
                        <span class="badge bg-success-subtle text-success">Endüstri Ort. Üstü</span>
                    </div>
                </div>
                <div class="col-lg-3 col-md-6">
                    <div class="content-card text-center" style="border-top-color: #e74c3c;">
                        <i class="bi bi-people-fill text-danger mb-3" style="font-size: 2rem;"></i>
                        <p class="small text-muted mb-1">Yıllık Devir Oranı</p>
                        <div class="kpi-value text-danger">15.4%</div>
                        <span class="badge bg-danger-subtle text-danger">Yüksek Riskli Departmanlar: 2</span>
                    </div>
                </div>
                <div class="col-lg-3 col-md-6">
                    <div class="content-card text-center" style="border-top-color: #f39c12;">
                        <i class="bi bi-clock-history text-warning mb-3" style="font-size: 2rem;"></i>
                        <p class="small text-muted mb-1">Ort. Onay Süresi (Tüm Akışlar)</p>
                        <div class="kpi-value text-warning">48 Saat</div>
                        <span class="badge bg-warning-subtle text-warning">Hedefin %20 Üstünde</span>
                    </div>
                </div>
                <div class="col-lg-3 col-md-6">
                    <div class="content-card text-center" style="border-top-color: #2ecc71;">
                        <i class="bi bi-currency-dollar text-success mb-3" style="font-size: 2rem;"></i>
                        <p class="small text-muted mb-1">Çalışan Başına Gelir</p>
                        <div class="kpi-value text-success">₺155K</div>
                        <span class="badge bg-success-subtle text-success">+%12 (Geçen Çeyrek)</span>
                    </div>
                </div>
            </div>
            <div class="row g-4 mt-1">
                <div class="col-lg-8">
                    <div class="content-card">
                        <h5 class="fw-bold mb-3">Çeyreklik Performans Karşılaştırması</h5>
                        ${generateBarChart([85, 95, 70, 80, 60], ['Oca', 'Şub', 'Mar', 'Nis', 'May'])}
                    </div>
                </div>
                <div class="col-lg-4">
                    <div class="content-card">
                        <h5 class="fw-bold mb-3">Hızlı Aksiyonlar</h5>
                        <ul class="list-group small list-group-flush">
                            <li class="list-group-item d-flex justify-content-between align-items-center" style="background-color: transparent;">
                                Depo A'ya acil stok transferi gerekiyor.
                                <a href="#" class="btn btn-sm btn-outline-danger">Başlat</a>
                            </li>
                            <li class="list-group-item d-flex justify-content-between align-items-center" style="background-color: transparent;">
                                Finansal Yıllık Raporu Oluştur.
                                <a href="#" class="btn btn-sm btn-outline-primary">Oluştur</a>
                            </li>
                            <li class="list-group-item d-flex justify-content-between align-items-center" style="background-color: transparent;">
                                5 Personel için eğitim planı onayı.
                                <a href="#" class="btn btn-sm btn-outline-warning">İncele</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        `,
        hr: `
            <div class="row g-4">
                <div class="col-lg-12">
                    <div class="content-card">
                        <h5 class="fw-bold mb-3"><i class="bi bi-people-fill me-2 text-primary-custom"></i> Departmana Göre Devir Oranı Analizi (Son 12 Ay)</h5>
                        ${generateBarChart([50, 70, 30, 90, 40], ['Satış', 'Pazarlama', 'Üretim', 'Teknik Servis', 'Yönetim'])}
                    </div>
                </div>
                <div class="col-lg-6">
                    <div class="content-card">
                        <h5 class="fw-bold mb-3">İşe Alım Süresi (Time To Hire)</h5>
                        <p class="kpi-value text-primary-custom">28 Gün</p>
                        <p class="small text-muted">Hedef: **21 Gün**. En uzun süren pozisyon: Kıdemli Yazılımcı (45 gün).</p>
                    </div>
                </div>
                <div class="col-lg-6">
                    <div class="content-card">
                        <h5 class="fw-bold mb-3">Çalışan Memnuniyeti (Son Anket)</h5>
                        <p class="kpi-value text-success">7.8 / 10</p>
                        <p class="small text-muted">Önceki: 7.5. **Gelişim Alanı:** Kariyer Gelişimi (6.1/10).</p>
                    </div>
                </div>
            </div>
        `,
        warehouse: `
            <div class="row g-4">
                <div class="col-lg-12">
                    <div class="content-card">
                        <h5 class="fw-bold mb-3"><i class="bi bi-truck-flatbed me-2 text-primary-custom"></i> Depo A ve B İçin Toplama Hızları Karşılaştırması</h5>
                        ${generateBarChart([80, 50, 65, 90], ['Depo A', 'Depo B', 'Depo C', 'Hedef'])}
                    </div>
                </div>
                <div class="col-lg-4">
                    <div class="content-card">
                        <h5 class="fw-bold mb-3">Stok Durumu Dağılımı</h5>
                        ${generatePieChart([
                            {label: 'Yeterli Stok', percent: 65, color: '#2ecc71'},
                            {label: 'Yakın Kritik', percent: 20, color: '#f39c12'},
                            {label: 'Kritik Stok', percent: 10, color: '#e74c3c'},
                            {label: 'Fazla Stok', percent: 5, color: 'var(--primary-color)'}
                        ])}
                    </div>
                </div>
                <div class="col-lg-8">
                    <div class="content-card">
                        <h5 class="fw-bold mb-3">Hatalı Sevkiyat Detayı (Son 7 Gün)</h5>
                        <table class="table table-hover small" style="color: var(--text-dark);">
                            <thead><tr><th>Tarih</th><th>Hata Tipi</th><th>Maliyet</th><th>Aksiyon</th></tr></thead>
                            <tbody>
                                <tr><td>Dün</td><td>Yanlış Adres</td><td class="text-danger">₺1.200</td><td><span class="badge text-bg-danger">Hata Kaydı Oluşturuldu</span></td></tr>
                                <tr><td>3 gün önce</td><td>Eksik Ürün</td><td class="text-danger">₺850</td><td><span class="badge text-bg-warning">İncelemede</span></td></tr>
                                <tr><td>4 gün önce</td><td>Fazla Ürün</td><td class="text-warning">₺300</td><td><span class="badge text-bg-success">Çözüldü</span></td></tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        `,
        workflow: `
            <div class="row g-4">
                <div class="col-lg-6">
                    <div class="content-card">
                        <h5 class="fw-bold mb-3"><i class="bi bi-diagram-3-fill me-2 text-primary-custom"></i> En Yavaş İş Akışları (Ort. Tamamlanma Süresi)</h5>
                        ${generateBarChart([90, 60, 30, 45, 20], ['Fatura Onayı', 'Sözleşme İmza', 'İzin Talebi', 'Tedarikçi Kaydı', 'Gider Onayı'])}
                        <p class="small text-muted mt-4">En yavaş akışlarda aksiyon almak, genel verimliliği %15 artırabilir.</p>
                    </div>
                </div>
                <div class="col-lg-6">
                    <div class="content-card">
                        <h5 class="fw-bold mb-3">Tıkanma Noktaları (Top 3 Kişi)</h5>
                        <ul class="list-group small list-group-flush">
                            <li class="list-group-item d-flex justify-content-between align-items-center" style="background-color: transparent;">
                                Ahmet Yılmaz - 15 Onay Bekliyor
                                <a href="#" class="btn btn-sm btn-danger">Hatırlat</a>
                            </li>
                            <li class="list-group-item d-flex justify-content-between align-items-center" style="background-color: transparent;">
                                Elif Kaya - 8 Onay Bekliyor
                                <a href="#" class="btn btn-sm btn-warning">Hatırlat</a>
                            </li>
                            <li class="list-group-item d-flex justify-content-between align-items-center" style="background-color: transparent;">
                                Yönetim Kurulu - 5 Onay Bekliyor
                                <a href="#" class="btn btn-sm btn-warning">Hatırlat</a>
                            </li>
                        </ul>
                        <div class="mt-3">
                            <h5 class="fw-bold mb-2">Toplam Bekleyen Onay Sayısı</h5>
                            <p class="kpi-value text-primary-custom">47</p>
                        </div>
                    </div>
                </div>
            </div>
        `,
        finance: `
            <div class="row g-4">
                <div class="col-lg-4">
                    <div class="content-card text-center" style="border-top-color: #2ecc71;">
                        <i class="bi bi-cash-stack text-success mb-3" style="font-size: 2rem;"></i>
                        <p class="small text-muted mb-1">Toplam Giderler (Bu Ay)</p>
                        <div class="kpi-value text-success">₺1.2 Milyon</div>
                        <span class="badge bg-success-subtle text-success">Bütçenin %10 Altında</span>
                    </div>
                </div>
                <div class="col-lg-4">
                    <div class="content-card text-center" style="border-top-color: #f39c12;">
                        <i class="bi bi-wallet-fill text-warning mb-3" style="font-size: 2rem;"></i>
                        <p class="small text-muted mb-1">Personel Maliyeti (Toplam)</p>
                        <div class="kpi-value text-warning">₺650K</div>
                        <span class="badge bg-warning-subtle text-warning">Geçen Aya Göre %3 Arttı</span>
                    </div>
                </div>
                <div class="col-lg-4">
                    <div class="content-card text-center" style="border-top-color: #e74c3c;">
                        <i class="bi bi-file-earmark-bar-graph-fill text-danger mb-3" style="font-size: 2rem;"></i>
                        <p class="small text-muted mb-1">Geciken Tahsilat Oranı</p>
                        <div class="kpi-value text-danger">4.5%</div>
                        <span class="badge bg-danger-subtle text-danger">Takip Gerekli</span>
                    </div>
                </div>
                <div class="col-lg-12">
                    <div class="content-card">
                        <h5 class="fw-bold mb-3"><i class="bi bi-bar-chart-fill me-2 text-primary-custom"></i> Gider Kategorileri Dağılımı</h5>
                        ${generatePieChart([
                            {label: 'Maaş ve SGK', percent: 55, color: '#3498db'},
                            {label: 'Operasyonel', percent: 25, color: '#2ecc71'},
                            {label: 'Pazarlama', percent: 10, color: '#f39c12'},
                            {label: 'Diğer', percent: 10, color: '#e74c3c'}
                        ])}
                    </div>
                </div>
            </div>
        `
    };

    // Fonksiyon: Temayı Yerel Hafızadan Yükle
    function loadTheme() {
        const savedTheme = localStorage.getItem('theme');
        const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;

        if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
            body.classList.add('dark-mode');
            darkModeSwitch.checked = true;
        } else {
            body.classList.remove('dark-mode');
            darkModeSwitch.checked = false;
        }
    }

    // Fonksiyon: Dark Mode Anahtarını Yönet
    darkModeSwitch.addEventListener('change', function () {
        if (this.checked) {
            body.classList.add('dark-mode');
            localStorage.setItem('theme', 'dark');
        } else {
            body.classList.remove('dark-mode');
            localStorage.setItem('theme', 'light');
        }
    });

    // Fonksiyon: Dinamik İçeriği Yükle
    function loadContent(area) {
        // Navigasyonları güncelle
        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('data-area') === area) {
                link.classList.add('active');
                contentTitle.textContent = link.textContent.trim();
            }
        });

        // İçeriği ekle ve animasyonu başlat
        dynamicContent.classList.remove('animate__fadeIn');
        dynamicContent.classList.add('animate__fadeOut');
        
        setTimeout(() => {
            dynamicContent.innerHTML = TEMPLATES[area] || `<h2>İçerik Bulunamadı</h2><p>Lütfen bir alan seçin.</p>`;
            dynamicContent.classList.remove('animate__fadeOut');
            dynamicContent.classList.add('animate__fadeIn');
        }, 300); 
        
        document.getElementById('last-update').textContent = `Bugün, ${new Date().toLocaleTimeString('tr-TR', { hour: '2-digit', minute: '2-digit' })}`;
    }

    // Navigasyon Tıklama Yöneticisi
    navLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const area = this.getAttribute('data-area');
            loadContent(area);
        });
    });

    // Sayfa yüklendiğinde varsayılan temayı ve içeriği yükle
    loadTheme();
    loadContent('overview'); 