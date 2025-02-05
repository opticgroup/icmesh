# TCMESH - Trabuco Canyon Mesh Network 🌄🛰️  

Welcome to **TCMESH**, a community-driven project to create a **peer-to-peer encrypted communication network** across **Trabuco Canyon, CA** using **Meshtastic**. This network operates completely **off-grid**—no internet or cell service required! 🌐  

### 🚨 **Our Mission**  

To **unite our community** by building and maintaining an **alternate, secure communication network** for **curiosity, connection, and emergency preparedness**.  
This network ensures we stay connected during critical events such as **fires**, **fallen poles**, and **flooding**, without relying on traditional infrastructure like **SCE power**, **internet**, or **cell towers**. 🌐📡  
 

---

## ⚙️ **Quick Start**  

1. **Get a Device**: Starting at **~$60** 👉 [Etsy Store](https://www.etsy.com/people/i9v8id6n/favorites/tcmesh-meshtastic-turn-key-devices)  
2. **Install the App:** [Download the Meshtastic app on iOS (App Store)](https://apps.apple.com/us/app/meshtastic/id1586432531) or [Android (Google Play)](https://play.google.com/store/apps/details?id=com.geeksville.mesh&pcampaignid=web_share). 📲  
3. **Connect Your Phone**: Use your **iPhone** or **Android** to connect via **Bluetooth** to your Meshtastic device.
4. **Configure your device**: Please use any short name you want.  For example mine is shortname: 🦅 long name: EAGLE TCMESH. **Important** use TCMESH in your long name so we can include your anonymized location on our future TCMESH map.
5. **Join the Network**: Once connected, your device will automatically communicate with other nodes on the mesh.  We use the default primary channel in So Cal.
6. **Join TCMESH**: This is a work in progress but we have created an encrypted channeled called **TCMESH** which you can configure here 👉 [Join TCMESH](https://meshtastic.org/e/?add=true#ChASAUwaBlRDTUVTSCUBAAAAEg8IATgBQAVIAVAeaAHABgE)  (untested)

📖 **For detailed instructions**, see our full guide: [INSTALLGUIDE.md](INSTALLGUIDE.md)  

---

### 📶 **How Meshtastic Works**  

Meshtastic is a long-range, open-source communication network designed to function without traditional cell towers or internet access. It is highly resilient and designed to avoid single points of failure. Here's how it works:

1. **Device-to-Device Communication**:  
   Meshtastic devices form a decentralized mesh network, where messages hop from one device to another until they reach their destination. This allows communication over large distances, even in remote areas, by relaying messages through multiple devices.  

2. **Network Resilience (No Single Point of Failure)**:  
   If a node or router in the network goes offline, the mesh will automatically route messages through other available nodes. This redundancy ensures that the network continues operating smoothly, avoiding disruption from any single point of failure. ⚙️🔄

3. **Unlicensed ISM Band Usage**:  
   Meshtastic operates on the **Industrial, Scientific, and Medical (ISM)** band, which is free to use and does **not require a license**. In the United States, Meshtastic use the **915 MHz** frequency. This frequency offers an ideal balance of range and penetration through obstacles like buildings and trees.

4. **Power & Range**:  
   Devices can legally transmit up to **1 watt (30 dBm)** of power on the ISM band, providing significant coverage even in remote areas. The mesh network's relaying capabilities further extend its range by passing messages through intermediate nodes.

TCMESH has chosen Meshtastic as it is well adopted, easy to use, and able to communicate both locally and over long distances when configured properly. 🌐📡  

---

## 📍 **Coverage Goals**  

### **Phase 1:** 
- **Cooks Corner** 🏍️  
- **Live Oaks Grade** 🛣️
- **Hamilton Trail** 🏡  
- **Trabuco Oaks Drive** 🌲
- Why? A few of us already active on TCMESH have established line of sight between these areas. They simply serve as a jumping off point to get the network established.

### **Phase 2:** Extended areas of Trabuco Canyon 🌐  
- Continue to cover Trabuco Oaks Drive (highly populated)
- General Store (popular meeting place)
- Rosa's Cantina (popular meeting place)
- Windy Ridge (additional coverage for homes half way up TOD)
- End of TOD (we have a TCMESH member that will cover the back of TOD)
- **Holy Jim** 🔥 to the **Flying Field** 🛩️ and the **Cabins** (future expansion)  
- Take user reports (via facebook) of nodes that cannot connect and design around this limitation

### **Phase 3:** Surrounding canyons and communities 🏞️  
- Goal:  Find and promote stakeholders in other canyons that can extend the TCMESH to the following canyons:
- **Modjeska Canyon**  
- **Silverado Canyon**  
- **Williams Canyon**  
- **Black Star Canyon**  

The goal is to create a best effort, **encrypted off-grid communication** throughout the entire canyon region! 📡  

---

## 🌄 **Extending Range with High-Elevation Nodes**

To expand **TCMESH** coverage across **Trabuco Canyon** and connect neighboring canyons, we are deploying **high-elevation, solar-powered, remote-configurable nodes**. These specialized nodes are designed to act as **point-to-point routers**, bridging communication between different areas.  For the tech nerds, they will be carefully selected to act as "routers"

### **Key Features:**  
- 📡 **Long-range distance:** Equipped with **tuned antennas** to maximize coverage across rugged terrain.  
- ☀️ **Solar-powered:** Ensures continuous operation without relying on external power sources.  
- 🔧 **Remote-configurable:** We will use remote administration public keys to manage these nodes to update software and maintain optimal performance.  
- 🌐 **Inter-canyon connectivity:** Facilitates best effort communication between **Trabuco Canyon**, **Modjeska**, **Silverado**, **Williams**, and **Black Star Canyons**.  
- 📻 **Station G2 radios for extended range:** Uses **higher-output radios** with **tuned receivers and transmitters**, optimized to reach longer distances.  
  - Equipped with **5-7dB gain** **915MHz antennas** for improved transmission and reception over challenging terrain.  We will carefully consider use of omni-direction vs. yagi antennas and are also researching how to combine both a yagi and omni node to provide this bridge.

### **Costs to build a router:**  
- Estimated build price: DIY **$150** or turn-key **$250** to **$450** per node.
- Nodes will serve as key infrastructure points, linking seperate communities, enhancing the mesh network's reliability and coverage.

By strategically placing these nodes on high ground, we can ensure robust, off-grid communication throughout the canyon network! 📡🏞️  

This allows **off-grid** communication across any connected nodes. Perfect for use in natural disasters, areas with poor reception, or for tech enthusiasts looking to experiment with mesh networking. 🛰️  

---

## 🤝 **We Need Your Help!**  
We're looking for:  
- **Nerds, hardware hackers, and radio enthusiasts** 🎙️ to help expand the network with hardware and write code to faciliate network resilancy.
- **Volunteers** to place **routers** on their property 🏠 to improve coverage. Ideal spots have good line-of-sight to neighboring areas.
- **Advocated** to spread TCMESH and setup new users
- **Host a Fund Raiser** - we are looking to raise a minimum of $1,000 through a resaurant fund raiser.  If you have experience doing this, please reach us on the mesh network.
- **Community Leaders** - find funds to buy turn key nodes and work with neighbors to place nodes with high propery elevation that can see a dense population of neighbors.

By placing routers and nodes throughout the area, we can strengthen coverage across the canyon and beyond!  

---

## ✅ **Current Progress**  
- **Our first solar powered node** will go live the week of February 10th, 2025
- Successful tests have already occured from Hamilton trail reaching from San Clemente to Orange.
- This Wiki 😃

---

### 📅 **Join Our Weekly TC Mesh Net!**  

We're excited to invite all TC Mesh users to our **Weekly Net**! 🎉 This is a great opportunity for us to stay connected, practice using TCMESH, and ensure the network is operating smoothly.

🕕 **When:** Every Tuesday at **6:00 PM PT**  
📡 **Where:** Primary Channel 0

During the net, we will:  
1. **Trade Messages** 💬 – Test and communicate with others on the network.  
2. **Expose Coverage Issues** 📶 – Identify weak spots and areas that need improvement.  
3. **Teach & Learn** 🧑‍🏫 – Share knowledge with new users, answer questions, and provide demos.  
4. **Ensure Network Health** ⚙️ – Confirm that devices are functioning properly and the network is stable.
5. **Use Facebook Chat** 💬 - As a reliable mode of communication to help others that cannot reach TCMESH (yet)

Regular participation helps us keep TC Mesh reliable and ready for when we need it most.   Whether you're a beginner or an experienced user, your involvement makes a difference! 🤝  

See you every Tuesday! Let's keep building and improving together! 🌐✨  

---

## 📡✨ Communications Compared 📊

| 📚 **PACE Level**   | 📡 **Method**           | 📝 **Description**                                                                             | ✅ **Pros**                           | ❌ **Cons**                           |
|----------------------|--------------------------|------------------------------------------------------------------------------------------------|----------------------------------------|----------------------------------------|
| **Primary**          | 📱 **Cell Phone / Internet** | Standard mobile networks or Wi-Fi internet communication.                                       | High reliability and speed             | Dependent on towers and infrastructure |
| **Alternate**        | 📶 **TCMESH (Meshtastic)**   | Encrypted peer-to-peer communication using mesh networking devices.                             | No infrastructure needed, encrypted    | Limited range, requires local nodes    |
| **Contingency**      | 🎙️ **GMRS**                  | General Mobile Radio Service (requires license), for family or local communication.              | Easy to use, better range than FRS     | Requires GMRS license, non-encrypted   |
| **Emergency**        | 📻 **HF Ham Radio**          | High-frequency amateur radio for long-range emergency communication.                            | Global range, robust in emergencies    | License needed, complex equipment      |
| **Emergency**        | 🛰️ **Satellite**             | Satellite communication (e.g., Starlink, Iridium) for critical off-grid communication.           | Global coverage, reliable in remote areas | Expensive, limited message capacity  |

---

### 🤝🌐 **Support & Learn from SoCalMesh.org!**  

We're proud to support and learn from our friends at **[SoCalMesh.org](https://socalmesh.org)**! 🛠️ They're building a resilient, community-driven communication network across Southern California using Meshtastic. 🏞️

Whether you're passionate about decentralized networks, emergency communications, or just want to connect with like-minded tech enthusiasts, **SoCalMesh** is the place to be!  

👉 **[Join their Discord community here](https://discord.gg/N5sXGwb5)** to collaborate, share ideas, and make a difference! 💬📡

---

## 🎯 **Future Goals for TC Mesh**  

We're continuously working to expand and enhance the **TCMESH** to better serve our community. Here are some of our key goals for the future:

1. **High-Powered Solar Node BBS** ☀️📡  
   - Set up a high-powered, solar-powered node to function as a **Bulletin Board System (BBS)** based on [Meshing Around](https://github.com/SpudGunMan/meshing-around). This will enable users to leave and retrieve messages when offline, creating a more robust communication system.

2. **Document Roll-Out & Community Involvement** 📋👥  
   - Track and document the network’s roll-out process, including community involvement metrics.  
   - Present this use case to **SoCalMesh** and other forms of media to showcase our network and extend our reach.

3. **Feature TC Mesh at the 4th of July Parade** 🎆🇺🇸  
   - Highlight **TCMESH** during the annual **4th of July Parade**, promoting its benefits and encouraging community participation.

4. **501(c)(3) Partnership** 🤝🏛️  
   - Attach **TCMESH** as a chapter of an existing **501(c)(3)** nonprofit.  
   - Since our project is small, this approach avoids the expenses and administrative burden of managing a separate nonprofit.

5. **Build Days & In-Person Meetups** 🔧🍔  
   - Organize **build days** and **meetups** for both **Trabuco Canyon Meshers** and **SoCal Meshers**.  
   - Support local restaurants that offer **revenue-sharing** by donating a portion of the proceeds to fund **TCMESH**.
  
6. **MQTT Server & Node Mapping** 🗺️📊  
   - Set up an **MQTT server** to log messages and build a dynamic map of **TCMESH** nodes. The **TCMESH channel** will automatically **desensitize GPS positions** to **0.9 miles** to protect users' exact locations while maintaining network functionality but will give us an idea of where everyone is at so we can design proper radio frequency coverage.


By achieving these goals, we aim to strengthen the network, foster collaboration, and ensure that **TCMESH** remains a vital, off-grid communication resource for our community! 🌐✨  

---

### 📜 **TCMESH Community Messaging Policy**  

To ensure a positive, inclusive, and respectful environment for all users, the following guidelines apply to messaging over TC Mesh:  

1. 🚫 **No Politics or Religion**:  
   Keep conversations neutral and avoid topics related to politics or religion to maintain harmony.  

2. 🗣️ **No Foul Language**:  
   Use respectful language at all times. Offensive or inappropriate language is strictly prohibited.  

3. 🚷 **No SHAFT Content**:  
   Content related to **Sex, Hate, Alcohol, Firearms, or Tobacco/Drugs** is not allowed. Keep messages clean and safe for everyone.  

4. 👶 **All-Age Appropriate**:  
   All messages should be suitable for audiences of all ages. Think family-friendly in all communications.  

5. 📵 **No Commercial Sales or Spam**:  
   Messages promoting commercial sales, advertisements, or spam are not permitted. Let's keep the network free of unwanted promotions.

6. 🪪 **Legal Placement of Routers & Nodes**:
   Place routers in areas with owner, goverment, and city permission.  Avoid "rougue" installations to maintain **TCMESH** integrity within the community and our local goverment.

Together, we can maintain a respectful, safe, and enjoyable space on **TCMESH**! 🤝🌐  
