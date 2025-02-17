# **Applied_Quantum_Algorithms-circuits---Cryogenics---Wave-Radiation-from-Exoplanets-Spatial-Objects**

## **Applied_Quantum_Algorithms(circuits) - Cryogenics - Wave Radiation from Exoplanets/Spatial Objects - Machine Learning Techniques in Pennylane (IA) - Cryogenics FPGA Hazard Cheatsheet**

This repository aims to explore and implement quantum algorithms with a focus on end-to-end resource analysis and optimization, particularly for applications in quantum interior-point methods (QIPMs) for second-order cone programming (SOCP), with a specific use case in portfolio optimization (PO). The repository will also delve into quantum circuits, cryogenics, and the study of wave radiation from exoplanets and other spatial objects, combining this with machine learning techniques and advanced hardware considerations.

---

## **Description**

This project extracts algorithms and explores resource optimization strategies from the paper *"End-To-End Resource Analysis for Quantum Interior-Point Methods and Portfolio Optimization"* by Alexander M. Dalzell et al. It focuses on the analysis of quantum algorithms for solving optimization problems, such as portfolio optimization, and provides a detailed quantum circuit-level description of quantum interior-point methods (QIPMs).

The repository also incorporates machine learning techniques, utilizing Pennylane for quantum computing and cryogenics, which are key components in the study of wave radiation from exoplanets and other spatial objects. Additionally, this repository includes a collection of FPGA hazard cheatsheets, designed for interfacing with quantum systems and supporting complex algorithms.

# Monitoring and Control of a Gas Turbine or Jet Engine with ZCU106/ZCU104

## 1. Data Acquisition from Sensors
Temperature, pressure, or vibration sensors are connected to the FPGA through:
- **External ADC (SPI/I2C)** if the sensors are analog.
- **GPIO or MIO** if the sensors already provide digital signals.
- **Alternative**: Use **PL I/O (LVCMOS/HP I/O)** to acquire fast signals directly.

## 2. FPGA Processing (Vivado + VHDL/Verilog)
- Design an IP block that receives and processes signals in real-time.
- Implement **FIR/IIR filters in DSP** to enhance signal quality.
- Configure **thermal controllers** that adjust combustion based on acquired metrics.

## 3. Ethernet Communication (Tri-speed, GEM, RGMII)
- Use the **GEM (Gigabit Ethernet MAC)** of the FPGA and configure **RGMII** for real-time data transmission.
- Send the metrics to a **PC/Server with Python** for further analysis.

## 4. Integration with Theoretical Models (Cantera + Python)
- Compare acquired data with **thermodynamic simulations in Cantera**.
- Use **AI/ML (TensorFlow Lite or PyTorch on ARM Cortex-A53)** to predict failures or improve turbine performance.

## 📊 Key Differences between ZCU102, ZCU106, and ZCU104

| Feature             | ZCU102      | ZCU106      | ZCU104      |
|----------------------|------------|------------|------------|
| **FPGA Logic**      | 600K LUTs  | 504K LUTs  | 350K LUTs  |
| **DSP Slices**       | 2520       | 1728       | 1542       |
| **Ethernet**         | 4x GEM (Tri-speed) | 4x GEM | 4x GEM |
| **Internal ADC**     | No         | No         | No         |
| **Interfaces**       | RGMII, PCIe, USB | RGMII, PCIe, USB | RGMII, PCIe, USB |
| **Processor**        | Quad ARM Cortex-A53 + Dual Cortex-R5 | Quad ARM Cortex-A53 + Dual Cortex-R5 | Quad ARM Cortex-A53 + Dual Cortex-R5 |

## ✅ Conclusion
- **ZCU106 and ZCU102** are more powerful than **ZCU104**, but all support the same workflow.
- If you need **more DSP and LUTs** (for intensive signal processing), **ZCU102/ZCU106** are better options.
- If you need something **more compact and efficient**, **ZCU104** is still a viable option for this type of project.


---

## **Key Features**

1. **Quantum Interior-Point Methods (QIPMs)**  
   Explore the implementation of QIPMs for SOCP problems with a focus on portfolio optimization (PO). The algorithms are described in terms of quantum circuits, covering the problem input to output, with an emphasis on improvements in quantum algorithm implementations.

2. **Resource Analysis**  
   An end-to-end resource analysis of quantum algorithms, accounting for logical qubits, non-Clifford T gates, and the parameters influencing the resource cost (such as instance-specific factors). The analysis includes practical considerations for scaling quantum algorithms for financial applications like portfolio optimization.

3. **Cryogenics and FPGA Integration**  
   Study of cryogenic systems and their interaction with FPGA hardware. This component will explore potential hazards and best practices when working with quantum circuits in cryogenic environments. The FPGA module will focus on hazard control and optimization techniques.

4. **Machine Learning in Pennylane (IA)**  
   Machine learning algorithms will be employed to analyze and optimize quantum circuits and other resources. Pennylane is used to implement quantum machine learning techniques that improve efficiency and accuracy in quantum algorithm applications.

5. **Wave Radiation from Exoplanets/Spatial Objects**  
   Investigate the quantum algorithms applicable to studying wave radiation emitted from exoplanets or other spatial objects. This section will connect quantum computing with astrophysical studies, enabling more efficient data processing techniques for astrophysical signal analysis.

6. **FPGA Hazard Cheatsheet**  
   A comprehensive cheatsheet for managing FPGA hazards when implementing quantum algorithms, especially under cryogenic conditions. It includes practical tips for hardware setup, error management, and debugging.

---

## **Getting Started**

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/Applied_Quantum_Algorithms.git
   ```

2. Install dependencies for machine learning with Pennylane:
   ```bash
   pip install pennylane
   ```

3. Follow the instructions in the `docs` folder for specific setup details on cryogenics, FPGA configuration, and quantum circuit implementations.

For quantum interior-point method implementations, navigate to the `QIPM` folder to find detailed examples and resource analysis for portfolio optimization.

---

## **Future Work**

- Extend the implementation of quantum algorithms for larger-scale optimization problems.
- Improve the cryogenic system integration for better performance in low-temperature environments.
- Investigate more machine learning techniques to improve the accuracy of quantum optimization.
- Study new quantum algorithms for various astrophysical problems involving wave radiation.

---

## **Contributing**

We welcome contributions! Please fork the repository, create a branch, and submit a pull request with your changes. Be sure to follow the guidelines in the `CONTRIBUTING.md` file.

---

## **Image Reference**

![Simulation](simulation/Captura%20de%20pantalla%202025-01-27%20213757.png)

---

## **Additional Resources**

- **Radio Astronomy**: Learn more about exoplanets and wave radiation at [NRAO Radio Astronomy](https://public.nrao.edu/radio-astronomy/exoplanets/).




