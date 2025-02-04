# 📡 **Best Practices for the Southern California Mesh Network**  

This document outlines recommended practices for operating on the **SoCalMesh** network using **Meshtastic**. These settings are not mandatory but are suggested to help reduce congestion and improve message reliability.  

**Reference:** [Meshtastic Documentation](https://meshtastic.org/docs/introduction/)

---

## 🚀 **Quick Start**  
1. Install and configure your Meshtastic device.  
2. Ensure your device is set to use the **default primary channel** (no special PSK or channel selection required for the public network).  
3. Set your device role and other configurations using the following guidelines.

---

## ⚙️ **Radio Configuration**  

### **Device Role**  
- **CLIENT**: Recommended for general use and "hop-out" nodes positioned slightly higher than other local nodes.  
- **CLIENT_MUTE**: Best for mobile nodes. Does not forward mesh packets but still transmits **NODEINFO** and **POSITION** updates.  
- **ROUTER**: Ideal for nodes placed on high elevations or remote peaks. Only a few nodes should use this role.

---

### **Settings**  
- **Hop Count:** Keep this low for better reliability. Occasional increases to 7 are possible but not recommended for long-term use.  
- **Broadcast Intervals:**  
  - **Position, Telemetry, Node Info**: Set to **3600 seconds** to reduce network congestion.  
- **LoRa Settings:** Ignore **MQTT** unless needed.

---

## 📡 **Antenna and Line-of-Sight Tips**  
- **Antennas and height** are crucial. A good antenna improves your signal transmission, while higher elevation gives better line-of-sight to other nodes.  
- Signals are heavily affected by obstructions (e.g., buildings, trees). Try to ensure there’s minimal interference between nodes.  
- Meshtastic operates on **low power** frequencies, so small improvements in setup (e.g., antenna tuning) can greatly enhance performance.

---

## 🔄 **Message Transmission Reliability**  
- It's generally easier to **receive** than **send** on portable devices with stock antennas.  
- Even if a message seems undelivered, the recipient may have received it, but a confirmation couldn't return due to signal conditions.  
- The more hops a message requires, the less reliable two-way communication becomes.

---

## 🎥 **Further Resources**  
- Check out this video for more details: [Meshtastic Setup and Tips](https://youtu.be/htjwtnjQkkE?si=7w7cbeKFueVI0Bk6)

---

Following these best practices will help you optimize your experience on the **SoCalMesh** network while minimizing congestion and improving message delivery. Happy meshing! 🌐  
