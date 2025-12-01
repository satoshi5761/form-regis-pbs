
import streamlit as st
import pandas as pd
import time, requests

st.markdown(r"""
### Registrasi $\;\frac{Public}{Speaking}💬$
""")

st.write('AIzaSyBpDcVjrWav7KgkXYjy6spmMvrAqOQ51Zw')

GOOGLE_SHEET_URL = 'https://script.google.com/macros/s/AKfycbzdFu99QQ07YPPIGbkQwglwaItJ6G-vfKz2GoyWkQHoSDsPPN2-rTUnbKONZvs-hkGDFQ/exec'

LIMIT = 43
with st.spinner("Loading...", show_time=1):
    getapi = requests.get(GOOGLE_SHEET_URL).json()
    print("="*10)
    peserta = getapi['peserta']
    cnt = int(getapi['total'])

    print(peserta, cnt)

# Create a form
if (cnt < LIMIT):
    with st.form("user_form"):
        name = st.text_input("Nama Lengkap")
        time.sleep(0.2)
        email = st.text_input("Alamat Email")
        time.sleep(0.2)

        org = [
            "Mahasiswa",
            "HMTI",
            "HMSI",
            "HMPSM",
            "HMPSA",
            "HMDP",
            "HMA ATRIVM",
            "BEMU",
            "BEM FTeol",
            "BEM FABIO",
            "BEM FTI",
            "BEM FKHUM",
            "BEM FK",
            "BEM FB",
            "BEM FAD",
            "BPMU",
            "BPM FTI",
            "BPM FTeol",
            "BPM FK",
            "BPM FB",
            "BPM FAD",
            "BPM FBIO"
        ]
        asal = st.selectbox("Miscellaneous", org)

        submitted = st.form_submit_button("Submit", type='primary')

        if (submitted):
            data = {"name":name,
                    "email": email,
                    "org": asal
                    }

            with st.spinner("Loading..."):
                req = requests.post(GOOGLE_SHEET_URL, json=data)

                if (req.status_code == 200):
                    st.success("Accepted :hearts:")
                    st.balloons()
                else:
                    st.error("Error...")

else:
    st.info("Kuota Terpenuhi", icon='ℹ️')



time.sleep(0.2)
rundown_sesi1 = {
    "Waktu": [1000,
              1002,
              1005,
              1007,
              1009,
              1012,
              1032,
              1052,

              '---',
              1100,
              '---',

              1120,
              1135,
              1235,
              1240,
              1245,
              1250,
              1251,
              1252,
              1250],
    "Durasi (menit)": [1,
                       3,
                       2,
                       2,
                       3,
                       20,
                       20,
                       8,

                       '---',
                       15,
                       '---',

                       15,
                       60,
                       5,
                       5,
                       5,
                       1,
                       1,
                       3,
                       10],
    "Keterangan": ['Doa Pembuka',
                   'Pembukaan Acara',
                   'Sambutan Wakil Ketua BPMU',
                   'Sambutan Ketua Pelaksana',
                   'MC memulai acara',
                   'Pemaparan Materi',
                   'Pemaparan Materi',
                   'Q & A',
                   '---',
                   'Istirahat',
                   '---',
                   'Persiapan',
                   'Presentasi',
                   'Pemeringkatan',
                   'Pengumuman',
                   'Pemberian sertifikat kepada narasumber & dokumentasi',
                   'Doa Penutup',
                   'Penutupan Acara',
                   'Dokumentasi',
                   'Pembagian Hadiah'
                   ] 
}

print(len(rundown_sesi1["Waktu"]), len(rundown_sesi1["Durasi (menit)"]), len(rundown_sesi1["Keterangan"]))
assert(len(rundown_sesi1["Waktu"]) == len(rundown_sesi1["Durasi (menit)"]) == len(rundown_sesi1["Keterangan"]))

rundown_sesi1["Waktu"] = [f"{str(i)[:2]}:{str(i)[2:]}" if (isinstance(i, int)) else i for i in rundown_sesi1["Waktu"]]

data_sesi1 = pd.DataFrame(columns=("Waktu", "Durasi (menit)", "Keterangan"))

rd_btn = st.button("Lihat Rundown")

if (rd_btn):
    
    c1, c2, c3 = st.columns([1,1,1])
    with c1:
        st.info(":calendar: 20 September 2025")

    with c2:
        st.info(":round_pushpin: Rudi Budiman")

    with c3:
        st.info(":alarm_clock: 10:00 - 13:00")

    percentage = 0.0
    progress_bar = st.progress(percentage) 
    table = st.empty()
    n = len(rundown_sesi1["Waktu"])
    for i in range(n):
        x = rundown_sesi1
        data_sesi1.loc[i] = [ x["Waktu"][i], x["Durasi (menit)"][i], x["Keterangan"][i] ]

        time.sleep(0.15)
        table.dataframe(data_sesi1, use_container_width=1)

        percentage += 1/n
        progress_bar.progress(percentage)


lihat_peserta = st.button("Lihat Peserta")

if (lihat_peserta):

    data_peserta = pd.DataFrame(columns=["Nama Lengkap"])

    table_peserta = st.empty()

    if (len(peserta) == 0):
        st.info("Belum ada pendaftar")
    else:
        for i in range(len(peserta)):
            data_peserta.loc[i] = peserta[i]
            table_peserta.dataframe(data_peserta)

            time.sleep(0.15)

