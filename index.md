Welcome to the **Inter-Canyon Mesh Network**, a community-driven project to build a **peer-to-peer encrypted communication network** 🔒 across **our canyons** using **Meshtastic** 📡. Text message your peers or the canyon crew with no internet, power, or cell service needed!

---

### 📡 **How Does It Work?**  
Our team has installed radio infrastruture 📡 on hilltops in Trabuco Canyon to provide initial coverage for residents. All you need is a small $40 mesh radio paired via Bluetooth to your existing cell phone. Download the Meshtastic app 📱, follow the simple instructions, and you’ll be up and running in minutes. Practice group texting 💬 with your community or, more importantly, stay connected when disaster strikes! 

### ⏱️ **Example**
Bobby can text Jack 💬 across the network, with messages hopping from device to device, bypassing obstacles and working without internet, power, or cell service

![Community Example](images/community-example.jpg)

---

## ⚙️ **Quick Start**  

1. **Get a Device**: Starting at $40 and great for walking around the [SenseCap Tracker T1000-E](https://www.seeedstudio.com/SenseCAP-Card-Tracker-T1000-E-for-Meshtastic-p-5913.html) is an excellent every day carry radio the size of a credit card or try something with a screen like the [WisMesh Pocket V2 for $99](https://store.rakwireless.com/products/wismesh-pocket).
2. **Install the App:** [Download the Meshtastic app on iOS (App Store)](https://apps.apple.com/us/app/meshtastic/id1586432531) or [Android (Google Play)](https://play.google.com/store/apps/details?id=com.geeksville.mesh&pcampaignid=web_share). 📲  
3. **Connect Your Phone**: Open the **Meshtastic** app, navigate to Bluetooth, pair with your device.
4. **Join ICMESH**: Go to settings -> Lora Config -> Region = United States.   Use Preset ON.   Present = **Medium Range - Slow**.  Ignore MQTT = ON, OK to MQTT = ON.  Transmit Enabled = ON.  
5. **Name Your Device**: Settings -> User -> Short Name up to 4 characters or 1 Emoji -> Long Name <something short> + ICMESH.COM.  For example: short name = BAC and long name = BACON - ICMESH.COM. Use ICMESH.COM in your long name so we can include you on our community dashboard.  
6. **Send A Message**: In your mobile app, go to **Channel** to send a message to everyone or **Direct Messages** to send a secure message to anyone on the network.

Here is a pic of the SenseCap Tracker T1000-E for $40

![Device Example](images/t1000.webp)

---

## 📍 **Coverage Map**  

### Current & Future Infrastructure Nodes in Trabuco Canyon, CA.

![Future Proposed Locations](images/future-network.png)

| 🟢   | 🟡   | 🔴   |
|------|------|------|
| Operational | Planned | Down |

View our [Extended Range Plan](EXTENDED-RANGE.md) and the [Future Goals of the Mesh](FUTURE-GOALS.md)

---

## 🤝 **We Need Your Help!**

We’re looking for:

- **You** to grab a device 📻, join the network 🌐, and team up with us!
- **Community Leaders** to rally support and help us raise $1,000 for more hilltop radios in Trabuco Canyon 📡 and special nodes to link our distant canyon folk 🏞️.
- **Nerds, hardware hackers, and radio enthusiasts** to assist in setting up the network, placing initial nodes, managing servers, and coding cool stuff to make this all work 💻.
- **Meet Up with Us** – Join us **Wednesday's at 6PM** on the mesh & [Discord](https://discord.gg/5FETN4UY) to test the network.

---

## ✅ **Current Progress**  
- 1 solar node ☀️ is live on Hamilton Trail + 3 more nodes ready for deployment 📡.  
- Successful testing between Hamilton, Cooks, and even Coto De Caza 📶.  
- Tools for admins to expand and track the network: MQTT, MeshView, Maps 🗺️, and Grafana Dashboards 🌐.   

---

## 📡✨ Communications Compared 📊

How does ICMESH compare to other forms of communication?

| **PACE Level**   | **Method**           | **Description**                                                                             | ✅ **Pros**                           | ❌ **Cons**                           |
|----------------------|--------------------------|------------------------------------------------------------------------------------------------|----------------------------------------|----------------------------------------|
| **Primary**          | 📱 **Cell Phone / Internet** | Standard mobile networks or Wi-Fi internet communication.                                       | High reliability and speed             | Dependent on towers and infrastructure |
| **Alternate**        | 📶 **ICMESH (Meshtastic)**   | Encrypted peer-to-peer communication using mesh networking devices.                             | No infrastructure needed, encrypted    | Limited range, requires local nodes    |
| **Contingency**      | 🎙️ **GMRS**                  | General Mobile Radio Service (requires license), for family or local communication.              | Easy to use, better range than FRS     | Requires GMRS license, non-encrypted   |
| **Emergency**        | 📻 **Ham Radio**          | High-frequency amateur radio for long-range emergency communication.                            | Global range, robust in emergencies    | License needed, complex equipment      |
| **Emergency**        | 🛰️ **Satellite**             | Satellite communication (e.g., Starlink, Iridium) for critical off-grid communication.           | Global coverage, reliable in remote areas | Expensive, limited message capacity  |

---

## ❓ **FAQ - Frequently Asked Questions**

**How reliable is this?** - As we kick off, coverage might be patchy. The more nodes 📡 we install, the stronger the network gets! Nope, this isn’t a cell phone substitute 📱❌.

**Do I need a license or tech skills?** - No license required 🎫❌. Tech know-how is a bonus but not needed to chat with neighbors 👋.

**Where can I get help?** 🆘 - Catch us on the Trabuco Facebook pages or join us on [Discord](https://discord.gg/5FETN4UY) 💬.

**How much does this cost?** - Just a radio ($40 to $100) 📻. No monthly fees ever 🙅‍♂️.

**Do I have to use my real name?** - Nope. You can remain anonymous if you choose.  Just follow the community guidelines or your node will be disabled from the network.

**What does RSSI and SNR mean?** - Meshtastic gear gives you two key signal stats: **RSSI (Received Signal Strength Indicator)** 📶 and **SNR (Signal-to-Noise Ratio)** 🎙️. Learn more [here](rssi-snr.md) 📚.

---

### 📜 **ICMESH Community Guidelines**  

To ensure a positive and respectful environment for all users, the following guidelines apply to messaging over ICMESH:  

1. 🚫 **No Politics or Religion**:  
   Keep conversations neutral and avoid topics related to politics or religion to maintain harmony.  

2. **No Foul Language**:  
   Use respectful language at all times. Offensive or inappropriate language is strictly prohibited.  

3. 🚷 **No SHAT**:  
   Content related to **Sex, Hate, Alcohol, or Tobacco/Drugs** is not allowed. Keep messages clean and safe for everyone.  

4. **All-Age Appropriate**:  
   All messages should be suitable for audiences of all ages. Think family-friendly in all communications.  

5. 📵 **No Commercial Sales or Spam**:  
   Messages promoting commercial sales, advertisements, or spam are not permitted. Let's keep the network free of unwanted promotions.

6. **Legal Placement of Nodes**:
   Always place nodes in areas with federal, state, city, government, and property owner permission. Avoid "rogue" installations to maintain integrity.

We look forward to seeing you on ICMESH!

### ⚠️ Disclaimer

<small>icmesh.com is run by an independent team not affiliated with Meshtastic LLC, using [Meshtastic®](https://meshtastic.org) software under license (Meshtastic® is a trademark of Meshtastic LLC). We proudly support [SoCalMesh](https://socalmesh.org), a 1,000+ member mesh networking community in Southern California. By using our site, you agree it’s provided “as is” with no warranties, and we’re not responsible for any communication issues, damages, or losses. It’s not a substitute for emergency services—dial 911 in emergencies.</small>
