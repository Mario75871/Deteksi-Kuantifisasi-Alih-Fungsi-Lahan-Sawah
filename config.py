"""
Konfigurasi proyek Deteksi Alih Fungsi Lahan Sawah - Kabupaten Badung
=====================================================================
Semua parameter, path, dan threshold dikumpulkan di sini agar mudah diubah.
Mendukung Upgrade Algoritma V2 (Bilateral Filter, LSWI, Tekstur NIR,
Multitemporal Differential Change Detection, Morfologi Rect 2x2 & CCA).
"""

from pathlib import Path

# ============================================================================
# PATH PROYEK
# ============================================================================
PROJECT_ROOT = Path(__file__).parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
BOUNDARY_DIR = DATA_DIR / "boundary"
PROCESSED_DIR = DATA_DIR / "processed"
INDICES_DIR = DATA_DIR / "indices"
RESULTS_DIR = DATA_DIR / "results"
VALIDATION_DIR = PROJECT_ROOT / "validation" / "highres_tiles"
OUTPUT_MAPS = PROJECT_ROOT / "output" / "maps"
OUTPUT_STATS = PROJECT_ROOT / "output" / "statistics"

# ============================================================================
# WILAYAH PENELITIAN - KABUPATEN BADUNG
# ============================================================================
# Bounding box (digunakan untuk download citra & clipping awal)
BADUNG_BBOX = {
    "west": 115.05,
    "south": -8.88,
    "east": 115.46,
    "north": -8.55,
}

# File boundary
BOUNDARY_FILE = BOUNDARY_DIR / "badung_boundary.geojson"
KECAMATAN_FILE = BOUNDARY_DIR / "badung_kecamatan.geojson"

# Sentinel-2 tile IDs yang mencakup Badung
SENTINEL2_TILES = ["T50LKR", "T50LLR"]

# ============================================================================
# PERIODE PENGAMATAN
# ============================================================================
YEAR_START = 2018
YEAR_END = 2026
MONTH = 10  # Oktober

DATE_START_2018 = "2018-10-01"
DATE_END_2018 = "2018-10-31"

DATE_START_2026 = "2026-10-13"
DATE_END_2026 = "2026-10-18"

# ============================================================================
# SENTINEL-2 BAND CONFIGURATION
# ============================================================================
BANDS_10M = ["B02", "B03", "B04", "B08"]        # Blue, Green, Red, NIR
BANDS_20M = ["B11", "B12"]                       # SWIR-1, SWIR-2
BANDS_SCL = ["SCL"]                              # Scene Classification Layer
ALL_BANDS = BANDS_10M + BANDS_20M + BANDS_SCL

TARGET_RESOLUTION = 10

# ============================================================================
# CLOUD MASKING - KELAS SCL YANG DI-MASK
# ============================================================================
SCL_MASK_VALUES = [0, 1, 3, 8, 9, 10, 11]
SCL_VALID_VALUES = [2, 4, 5, 6, 7]

# ============================================================================
# PARAMETER BILATERAL FILTER & BICUBIC RESAMPLING (ALGORITMA V2)
# ============================================================================
BILATERAL_D = 5
BILATERAL_SIGMA_COLOR = 0.05
BILATERAL_SIGMA_SPACE = 5.0

# ============================================================================
# THRESHOLD INDEKS SPEKTRAL (ALGORITMA V2 - LSWI & MULTITEMPORAL DIFFERENTIAL)
# ============================================================================
# Tekstur NIR: Standar Deviasi Lokal 5x5 (sawah homogen < 0.045)
TH_SIGMA_NIR = 0.045
TEXTURE_WINDOW_SIZE = 5

# Aturan Sawah 2018 (2 Fase: Vegetatif & Genangan Air Subak)
# 1. Fase Vegetatif
TH_NDVI_SAWAH_VEG = 0.45
TH_LSWI_SAWAH_VEG = 0.18

# 2. Fase Genangan Subak / Pengolahan Tanah
TH_NDVI_SAWAH_WATER_MIN = 0.10
TH_NDVI_SAWAH_WATER_MAX = 0.45
TH_LSWI_SAWAH_WATER = 0.25
TH_NDBI_SAWAH_WATER = -0.10

# Aturan Target Konversi (Vila Tropis & Bangunan 2026)
TH_DELTA_NDBI = 0.10       # Δ NDBI > 0.10 (material kedap air / atap / semen bertambah)
TH_DELTA_LSWI = -0.05      # Δ LSWI < -0.05 (kelembapan / fasa basah sawah hilang drastis)
TH_DELTA_BSI = 0.10        # Δ BSI > 0.10 (lahan urukan / tanah konstruksi)
TH_NDBI_BUILT_2026 = 0.05  # NDBI 2026 terbangun

# ============================================================================
# OPERASI MORFOLOGI & CONNECTED COMPONENT ANALYSIS (CCA)
# ============================================================================
# Sawah Awal: Ellipse 3x3 + CCA >= 15 piksel (1.500 m²)
MORPH_SAWAH_KERNEL_SHAPE = "ellipse"
MORPH_SAWAH_KERNEL_SIZE = 3
MIN_SAWAH_PIXELS = 15

# Konversi / Bangunan: Rectangular 2x2 (menjaga kavling vila kecil tidak terhapus)
MORPH_BUILD_KERNEL_SHAPE = "rect"
MORPH_BUILD_KERNEL_SIZE = 2
MIN_CONVERSION_PIXELS = 5   # 500 m² (kavling vila / perumahan)

# Data Referensi Resmi Dinas Pertanian / Satu Data Badung
REF_KUTA_UTARA_HA = 871.86

# ============================================================================
# OPENEO CONFIGURATION (CDSE)
# ============================================================================
OPENEO_BACKEND_URL = "openeo.dataspace.copernicus.eu"
OPENEO_COLLECTION = "SENTINEL2_L2A"

# ============================================================================
# VALIDASI HIGH-RES
# ============================================================================
ESRI_IMAGERY_URL = (
    "https://server.arcgisonline.com/ArcGIS/rest/services/"
    "World_Imagery/MapServer/tile/{z}/{y}/{x}"
)
ESRI_ZOOM_LEVEL = 17

# ============================================================================
# OUTPUT FILE NAMES
# ============================================================================
COMPOSITE_2018 = PROCESSED_DIR / "composite_2018_oct.tif"
COMPOSITE_2026 = PROCESSED_DIR / "composite_2026_oct.tif"

NDVI_2018 = INDICES_DIR / "ndvi_2018.tif"
NDVI_2026 = INDICES_DIR / "ndvi_2026.tif"
LSWI_2018 = INDICES_DIR / "lswi_2018.tif"
LSWI_2026 = INDICES_DIR / "lswi_2026.tif"
NDBI_2018 = INDICES_DIR / "ndbi_2018.tif"
NDBI_2026 = INDICES_DIR / "ndbi_2026.tif"
NDWI_2018 = INDICES_DIR / "ndwi_2018.tif"
NDWI_2026 = INDICES_DIR / "ndwi_2026.tif"
BSI_2018 = INDICES_DIR / "bsi_2018.tif"
BSI_2026 = INDICES_DIR / "bsi_2026.tif"
TEXTURE_NIR_2018 = INDICES_DIR / "texture_nir_2018.tif"
TEXTURE_NIR_2026 = INDICES_DIR / "texture_nir_2026.tif"

# Hasil deteksi
CANDIDATE_MASK = RESULTS_DIR / "candidate_transition.tif"
CANDIDATE_MORPHED = RESULTS_DIR / "candidate_transition_morphed.tif"
CONVERSION_MULTICLASS = RESULTS_DIR / "conversion_multiclass_morphed.tif"
CONVERSION_POLYGONS = RESULTS_DIR / "conversion_polygons.geojson"

# Luaran Peta & Statistik
DUALMAP_HTML = OUTPUT_MAPS / "peta_dualmap_klaster.html"
KECAMATAN_BREAKDOWN_CSV = OUTPUT_STATS / "kecamatan_breakdown.csv"
ACCURACY_REPORT_CSV = OUTPUT_STATS / "accuracy_report.csv"
FINAL_STATS_CSV = OUTPUT_STATS / "final_statistics.csv"
VALIDATION_POINTS_GEOJSON = PROJECT_ROOT / "output" / "validation" / "validation_points.geojson"
