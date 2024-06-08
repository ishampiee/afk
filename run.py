import subprocess

# Dosya yolu ve adını belirtin
dosya_yolu = r"C:\path\to\baslat.bat"

# .bat dosyasını yeni bir pencerede çalıştırın
subprocess.Popen(f"start {dosya_yolu}", shell=True)
