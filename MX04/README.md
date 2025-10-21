# Rohde & Schwarz MXO4 Spectrum Capture Example

This example demonstrates how to control the **R&S MXO4 oscilloscope** over LAN using the [RsInstrument](https://pypi.org/project/RsInstrument/) Python library.  
The script configures the FFT view, measures amplitude values at multiple frequencies, and saves the results into a CSV file.

---

## Requirements
Install the RsInstrument library:
```bash
pip install RsInstrument
