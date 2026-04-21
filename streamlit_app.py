import streamlit as st
import numpy as np

st.title("🔬 N9010B Phase Noise Tool")

st.header("Entrada")

freq = st.number_input("Frecuencia (GHz)", value=3.195)
offset = st.number_input("Offset (Hz)", value=500)
measured = st.number_input("Phase Noise medido (dBc/Hz)", value=-97.0)

st.header("Cálculo")

if offset <= 1000:
    base = -105
elif offset <= 10000:
    base = -110
elif offset <= 100000:
    base = -115
else:
    base = -134

delta = 20 * np.log10(freq)
exa = base + delta

st.write(f"Ruido EXA estimado: {exa:.2f} dBc/Hz")

margin = measured - exa

st.header("Resultado")

if margin > 10:
    st.success("✅ VÁLIDO")
elif margin > 3:
    st.warning("⚠️ DUDOSO")
else:
    st.error("❌ LO-LIMITED")
