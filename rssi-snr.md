# RSSI and SNR

In wireless communication, **RSSI** and **SNR** determine signal quality.

#### **RSSI** (Signal Strength)  
- Measures how strong the signal is (like how loud someone is speaking).  
  - **Good:** Above **-115 dBm**  
  - **Poor:** Below **-126 dBm**  
- **Analogy:** In a concert, voices can be loud (**RSSI = -80 dBm**) but still hard to hear due to noise.

#### **SNR** (Signal Clarity)  
- Measures how much louder the signal is compared to background noise.  
  - **Good:** Above **17.5 dB**  
  - **Poor:** Below **9 dB**  
- **Analogy:** In a quiet cafe, soft voices (**RSSI = -115 dBm**) are easy to understand because the noise is minimal (**SNR = 25 dB**).

Both strong **RSSI** and high **SNR** are needed for reliable communication.

| **Metric**   | **Good**                     | **Fair**                       | **Bad**                       | **Poor**                   |
|--------------|-------------------------------|---------------------------------|-------------------------------|----------------------------|
| **RSSI**     | 🟢 > -115 dBm                 | 🟡 -115 dBm to -120 dBm         | 🟠 -120 dBm to -126 dBm        | 🔴 ≤ -126 dBm              |
| **SNR**      | 🟢 > 17.5 dB                  | 🟡 11 dB to 17.5 dB             | 🟠 9 dB to 11 dB               | 🔴 < 9 dB                  |
