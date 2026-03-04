# Inline Editorial Review: DCNAUTO-Sec 01_orig

**Instructions**: Search for `~~` to find deletions and `**` to find additions.
Copy this document into Word to see Track Changes formatting.

---

**Total Changes**: 265 (Auto-fix: 121, Review: 112, Questions: 32)

---

dcnauto20

Automating Cisco Data Center Networking Solutions

Student Learning Guide

Version

Section 1: Day-Zero Provisioning

Introduction

Imagine you are a network engineer preparing to deploy a new data center. Dozens of Cisco Nexus switches have just arrived, and the clock is ticking. Your operations team needs these devices that are configured and online as quickly as possible. Manual provisioning means to rack each switch, connecting to the console, and applying configurations one by one; a time-consuming process prone to errors that can delay your entire deployment.

You and your team are under pressure to deliver. Every extra hour spent on initial setup means delayed project milestones, wasted resources, and a higher risk of misconfigurations that can impact network performance from day one.

![Diagram showing an office environment with four people, two large screens in the background, one displaying a network device with a circular flow and the other a project timeline, representing collaborative work or a presentation.](media/image1.bin){width="6.940277777777778in" height="3.1080369641294836in"}

This learning content will transform your approach to Day-Zero operations by showing you how to automate initial device provisioning using PowerOn Auto Provisioning (POAP) and Python scripts. You will learn how to streamline the setup of Cisco Nexus devices, reduce human error, and accelerate the time from unboxing to production-ready.

In this learning content, you will:

-   Understand the concept and benefits of Day-Zero operations.

-   Describe the POAP workflow and required infrastructure components.

-   Configure Cisco Nexus devices to use POAP for automated provisioning.

-   Develop and integrate a Python script to customize and extend POAP functionality.

-   Verify and troubleshoot POAP deployments.

Course to Exam Blueprint Mapping

+--------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ![Exam prep icon.](media/image2.bin){width="0.9741929133858268in" height="0.9741929133858268in"} | This course aligns to the Cisco 300-635 DCNAUTO v2.0 as outlined below:                       |
|                                                                                                  |                                                                                               |
|                                                                                                  | -   3.0 Network Element Programmability                                                       |
|                                                                                                  |                                                                                               |
|                                                                                                  | ```{=html}                                                                                    |
|                                                                                                  | <!-- -->                                                                                      |
|                                                                                                  | ```                                                                                           |
|                                                                                                  | -   3.2 Construct a device-level network automation solution for Day-0 Provisioning with POAP |
+--------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+

Day-Zero Operations

You have just powered on racks of new Cisco Nexus switches in the data center. The project deadline is tight, and manual configuration for each device would consume hours and risk introducing inconsistencies. This is where Day-Zero operations come in.

Day-Zero operations refer to the automated process of bringing a network device from its initial power-on state to a functional, production-ready configuration with minimal manual intervention. This stage is critical for accelerating deployments, reducing human error, and ensuring consistent configurations across all devices---exactly what you need to meet your deployment schedule.

On Cisco Nexus devices running the Cisco Nexus Operating System (NX-OS), foundational automation capabilities support the entire device lifecycle:

-   **Day 0:** Initial device startup, base configuration, and software upgrade

-   **Day 1:** Incremental configuration for new endpoints and workloads

-   **Day 2:** Monitoring and visibility

-   **Day N:** Ongoing maintenance, upgrades, and patching

![Diagram illustrating the operational phases of a network device lifecycle, presented as a vertical stack of boxes on the left detailing Day 0 Install (P O A P) through Day N Upgrade, Patching, and a circular lifecycle diagram on the right showing the continuous flow of these phases.](media/image3.bin){width="6.94027668416448in" height="3.1146609798775153in"}

During Day-Zero operations, the device is booted, upgraded to the approved Cisco NX-OS version, and configured with initial parameters such as:

-   **Minimal configuration parameters:**

```{=html}
<!-- -->
```
-   Switch name

-   Admin username and password

-   Out-of-band (OOB) management interface and routing

-   Operating system version upgrade

```{=html}
<!-- -->
```
-   **Extended configuration parameters:**

```{=html}
<!-- -->
```
-   In-band management

-   Authentication, Authorization, and Accounting (AAA)

-   Enabling required Cisco NX-OS features

-   Global switching parameters

-   Routing protocol parameters

-   vPC domain setup

-   ~~VXLAN~~ **Virtual Extensible LAN (VXLAN)** [Explanation: Acronym 'VXLAN' not expanded on first use. Category: Acronyms] Tunnel Endpoint (VTEP) parameters

-   Network interface configuration

To streamline these steps in your deployment, Cisco Nexus devices support POAP, which automates Day-Zero provisioning by downloading and applying configuration files or executing Python scripts at first boot. This ensures that every switch in your racks is provisioned quickly, consistently, and in alignment with your organization's standards---turning hours of manual work into minutes of automated setup.

![Diagram illustrating the P O A P process, where a cloud labeled P O A P delivers a Configuration File and a Python Script to a stack of server like devices for configuration and updates.](media/image4.bin){width="3.406451224846894in" height="5.322579833770779in"}

Before POAP can run, several back-end services must be in place to provide the device with its initial configuration, scripts, and software images. These services work together to complete the Day-Zero provisioning workflow and form the foundation of the POAP architecture.

POAP Architecture Components

Behind the scenes, POAP relies on several back-end components---services that work together to assign network settings, deliver scripts, and provide software images to your new Cisco Nexus switches. These components form the architecture that makes Day-Zero automation possible, and they can run on a single consolidated server or be distributed across multiple systems, depending on your environment.

![Network diagram illustrating the P O A P architecture components, including a D H C P Server, Script Server, and Configuration and Software Server connected through a cloud and Default Gateway to a Nexus Switch, showing the flow of I P addresses, script files, and configuration and software images.](media/image5.bin){width="6.94027668416448in" height="3.1146609798775153in"}

The following are the key back-end services that enable the POAP process for Cisco Nexus switches, along with their respective roles:

-   **Cisco Nexus Switch:** On first boot, the switch checks for a startup configuration. If none exists, POAP is triggered.

-   **~~DHCP~~ **Dynamic Host Configuration Protocol (DHCP)** [Explanation: Acronym 'DHCP' not expanded on first use. Category: Acronyms] Server:** Assigns IP address, gateway, and the location of the script server and script file to the switch.

-   **Script Server (TFTP/HTTP):** Delivers a configuration script or Python script that is used to automate setup.

-   **Configuration and Software Server:** Hosts software images and configuration files that can be downloaded and installed during Day-Zero provisioning.

POAP offers several benefits, including:

-   Reduces manual errors and inconsistencies.

-   Accelerates device provisioning from hours to minutes.

-   Ensures consistent, standardized configurations across all devices.

-   Frees network engineers to focus on higher-value tasks.

POAP also integrates with existing network management workflows and automation tools, enabling seamless Day-Zero provisioning as part of broader network operations.

~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. What is the primary goal of Day-Zero operations in Cisco Nexus device deployment?

A. To monitor network traffic continuously

B. To automate initial device startup, configuration, and software upgrade

C. To perform routine maintenance and patching

D. To configure routing protocols after deployment

PowerOn Auto Provisioning

The new Cisco Nexus switches are powered on and ready to join the network. Rather than logging in to each switch and configuring it manually, you use PowerOn Auto Provisioning (POAP). POAP is an automated method that ensures every device receives its correct software image, configuration, and required agents right at first boot.

POAP is a Cisco NX-OS feature that is designed for Day-Zero provisioning, allowing a switch ~~to automatically configure~~ **Consider moving the adverb (e.g., 'to quickly configure' → 'to configure quickly')** [Explanation: avoiding split infinitives when possible. Category: Grammar & Punctuation] itself using predefined scripts and image files. The process eliminates manual intervention, speeds up deployments, and ensures consistency across all devices.

POAP Workflow

The POAP workflow follows a precise sequence from when a switch powers on to when it becomes fully operational. Each step builds on the previous one, beginning with DHCP initialization, moving through script retrieval and device identification, and ending with the configuration application.

![Flowchart illustrating the power-up and configuration process for a network switch. The process starts with powering up the switch. If a startup configuration exists, the switch boots normally with that configuration. If no startup configuration exists, the switch prompts whether to ~~abort~~ **Consider changing 'abort' to 'cancel' or 'terminate'** [Explanation: using 'cancel' or 'terminate' instead of 'abort'. Category: Cisco Style Guide] the P O A P process. If P O A P is ~~aborted~~ **Consider changing 'abort' to 'cancel' or 'terminate'** [Explanation: using 'cancel' or 'terminate' instead of 'abort'. Category: Cisco Style Guide], an interactive setup begins over the serial console. If P O A P is not ~~aborted~~ **Consider changing 'abort' to 'cancel' or 'terminate'** [Explanation: using 'cancel' or 'terminate' instead of 'abort'. Category: Cisco Style Guide], the switch executes D H C P discovery to obtain an I P address and T F T P server address for the P O A P script file. The switch then downloads and executes the P O A P script file. Next, it checks if the bootflash contains the image specified in the script; if not, it downloads the image. Following this, the switch determines and downloads the configuration file, reboots, replays the configuration file to configure itself, and finally saves the configuration locally to N V RAM.](media/image6.bin){width="6.940277777777778in" height="3.1046620734908137in"}

To understand how the process unfolds, let's walk through each stage in the following order:

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]**DHCP Initialization:** When a switch boots without a startup configuration, it acts as a DHCP client. The DHCP server assigns a temporary IP address and passes additional DHCP scope options that guide the provisioning process.

2~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]**DHCP Options for POAP:** Explore the key steps and DHCP options that drive the POAP process for Cisco Nexus switches:

-   **DHCP Option 66:** Specifies the IP address or hostname of the script server (TFTP/HTTP). The switch uses this to find and download the configuration or Python script that is needed for provisioning.

-   **DHCP Option 150:** An option available on Cisco platforms that supports multiple TFTP server IP addresses. This provides redundancy by allowing the switch to contact alternate servers if the primary server is unavailable.

-   **DHCP Option 67:** Defines the name of the boot script to download, such as poap.py. This script contains the logic to automate image downloads, configuration application, agent installation, and other setup tasks.

3~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]**Script Retrieval and Execution:** The switch contacts the script server to download the specified script. This script contains the logic to download the NX-OS image, apply the configuration, install any agents, and perform other setup tasks.

4~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]**Device Identification:** POAP can identify a switch using its serial number, system ~~MAC~~ **Media Access Control (MAC)** [Explanation: Acronym 'MAC' not expanded on first use. Category: Acronyms] address, or network topology (directly connected neighbors). This allows the script to customize the configuration per device.

5~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]**Applying Configuration:** The downloaded image and configuration are applied after a reboot, completing the Day-Zero provisioning process.

By using POAP, you transform what could be hours of manual work into an automated, repeatable workflow. This ensures all your Cisco Nexus switches are configured and ready for production in minutes.

~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. What is the purpose of DHCP Option 66 in the POAP process for Cisco Nexus switches?

A. To assign a temporary IP address to the switch

B. To specify the IP address or hostname of the script server for downloading provisioning scripts

C. To define the name of the boot script to download

D. To provide multiple TFTP server IP addresses for redundancy

Python Script for POAP

The Cisco Nexus switches have pulled a temporary IP via DHCP, learned where to fetch the bootstrap, and downloaded poap.py.

The Cisco provided poap.py Python script automates Day-Zero provisioning and upgrade processes for Cisco Nexus switches. It simplifies tasks such as image upgrades, configuration deployment, and agent installation during initial device setup, enabling scalable and consistent network device provisioning.

The script requires several user-editable parameters to customize provisioning:

-   **hostname:** The file server's hostname or IP address from~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]files are copied.

-   **transfer_protocol:** The protocol used for file transfer (Secure Copy Protocol \[SCP\], FTP, SFTP, HTTP, HTTPS, TFTP). The default is SCP.

-   **username/password:** Credentials for authenticating to the file server if required.

-   **target_system_image:** The NX-OS image filename to upgrade the switch to, if needed.

-   **mode:** Defines how the switch identifies to the file server to receive the correct configuration. Options include serial number, MAC address, hostname, or location. The default is the serial number.

To help you get a hands-on experience with the poap.py script provided by Cisco, the key user-editable settings are broken down into the following focused areas:

-   **Transfer Settings**

Specify the file server and transfer method here. Set \"hostname\": \"2.1.1.1\" to your file server\'s IP address or hostname. Use \"transfer_protocol\": \"scp\" to select the Secure Copy Protocol. The script supports SCP, SFTP, FTP, HTTP, HTTPS, and TFTP, with SCP as the default.

\# script_timeout=1800\
\# \-\~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation] Start of user editable settings \-\~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]\
\# Host name and user credentials\
options = {\
\"username\": \"root\",\
\"password\": \"password\",\
**\"hostname\": \"2.1.1.1\",\
\"transfer_protocol\": \"scp\",**

-   **Device Identity Mode**

Choose how the switch identifies to the file server to receive the correct configuration. Setting \"mode\": \"hostname\" makes the switch use its hostname as identity. You can also select a serial number (default), MAC address, or location. This ensures that the script applies device-specific configurations accurately.

\# script_timeout=1800\
\# \-\~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation] Start of user editable settings \-\~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]\
\# Host name and user credentials\
options = {\
\"username\": \"root\",\
\"password\": \"password\",\
\"hostname\": \"2.1.1.1\",\
\"transfer_protocol\": \"scp\",\
**\"mode\": \"hostname\",**

-   **Image Upgrade**

Specify the Cisco NX-OS Software version for the switch to upgrade to during provisioning. Set \"target_system_image\": \" nxos64-cs.10.6.1.F.bin \" to the ~~desired~~ **wanted** [Explanation: 'want' or 'wanted' instead of 'desire/desired'. Category: Cisco Style Guide] image filename. If the switch already runs this version, the script skips the upgrade; otherwise, it downloads and installs the image.

\# script_timeout=1800\
\# \-\~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation] Start of user editable settings \-\~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]\
\# Host name and user credentials\
options = {\
\"username\": \"root\",\
\"password\": \"password\",\
\"hostname\": \"2.1.1.1\",\
\"transfer_protocol\": \"scp\",\
\"mode\": \"hostname\",\
**\"target_system_image\": \" nxos64-cs.10.6.1.F.bin \",**

-   **Handling Additional Files (Switch Agents)**

The script can also copy extra files such as monitoring agents, scripts, or tarballs to the switch. It supports unpacking tarballs and deleting them after extraction to keep the device clean.

download_user_app(\"/source\", \"filename.tar\", \"/destination\", unpack=True, delete_after_unpack=True)

~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. Which parameter in the poap.py Python script specifies how the Cisco Nexus switch identifies itself to the file server to receive the correct configuration?

A. **hostname**

B. **transfer_protocol**

C. **mode**

D. **target_system_image**

Discovery 1: Set Up PowerOn Auto Provisioning on the Cisco Nexus 9000

Introduction

In this lab, you will explore the services and files that make POAP work and walk through the full POAP process on Cisco Nexus 9000v switches. By the end, you will understand how POAP accelerates deployments and reduces operational effort.

Scenario

You are a network operations engineer for a rapidly expanding cloud service provider. Your company is undergoing a significant data center expansion, requiring the deployment of dozens of new Cisco Nexus switches. Manually configuring each switch is not feasible for this scale, and your team needs a highly efficient and repeatable method for initial device setup. Your primary objective is to implement a robust and automated provisioning solution to accelerate deployments, minimize human error, and ensure consistent configurations across all new devices.

Your lab environment simulates a segment of this expansion, featuring an Infra-Server configured with DHCP and TFTP services, and two new Cisco Nexus 9000v switches (Leaf-b and Leaf-c) awaiting initial configuration.

The company mandates that all new switches are automatically onboarded, receive the correct Cisco NX-OS image, and apply a standardized configuration based on their unique serial numbers, all without manual intervention at the device console. Integrity checks (like MD5 checksums) are critical for ensuring secure and reliable deployments.

To accomplish this, you will:

-   Prepare the central provisioning server by verifying and enabling its DHCP and TFTP services.

-   Ensure the integrity of the POAP script and device-specific configuration files.

-   Initiate the POAP process on a new Cisco Nexus switch.

-   Monitor the automated provisioning workflow, from IP address acquisition to configuration application.

-   Validate that the switch has been successfully provisioned with its intended configuration.

-   Apply the learned process to provision an additional Cisco Nexus device independently.

Topology

In this lab, you will use **Leaf-b** and **Leaf-c** Cisco Nexus 9000v switches for POAP. The **Infra-Server** hosts the DHCP, TFTP, and provisioning script services required for POAP. You will access the Infra-Server through the **Student Linux VM**.

![Diagram illustrating a network topology centered around an O O B M G M T device. This device is connected to a Student Linux V M at I P address 10.1.1.10, an Infra S R V at I P address 10.1.1.254, Leaf B at I P address 10.1.1.54, and Leaf C at I P address 10.1.1.55. An additional Student P C is connected to the Student Linux V M.](media/image7.bin){width="6.940277777777778in" height="3.1611789151356082in"}

Job Aid

Device Information

  ---------------------------------------------------------------------------------------------------------------------------
  Device                Description                                         Protocol        IP Address   Credentials
  --------------------- --------------------------------------------------- --------------- ------------ --------------------
  Student Workstation   Linux Ubuntu VM                                     ~~SSH~~ **Secure Shell (SSH)** [Explanation: Acronym 'SSH' not expanded on first use. Category: Acronyms]             10.10.1.10   student, 1234QWer

  Infra-Server          Linux Ubuntu VM                                     SSH             10.1.1.254   cisco, cisco

  ~~CML~~ **Cisco Modeling Labs (CML)** [Explanation: Acronym 'CML' not expanded on first use. Category: Acronyms]                   Cisco Modeling Labs                                 HTTPs           10.1.1.20    admin, 1234QWer

  Leaf-b                Cisco Nexus 9000 9000v virtual Cisco NX-OS switch   SSH             10.1.1.54    admin, 1234QWer

  Leaf-c                Cisco Nexus 9000 9000v virtual Cisco NX-OS switch   SSH             10.1.1.55    admin, 1234QWer
  ---------------------------------------------------------------------------------------------------------------------------

Command List

The table describes the commands that are used in this activity. The commands are listed in alphabetical order so that you can easily locate the information that you need. Refer to this list if you need configuration command assistance during the lab activity.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Command                        Description
  ------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  cd *directory name*            To change directories within the Linux file system, use the **cd** command. You will use this command to enter a directory where the lab scripts are housed. You can use tab completion to finish the name of the directory after you start typing it.

  python *script-file-name.py*   To ~~initiate~~ **start** [Explanation: 'start' or 'begin' instead of 'initiate'. Category: Cisco Style Guide] a Python script, you need to use the **python** Linux command along with the name of the script. You can use tab completion to finish the name of the script after you start typing it.

  systemctl *service restart*    **Systemctl** is a command used in Linux environments to configure Systemd init system. The example stops and starts the selected service.

  SSH *IP address*               Opens a secure command-line session to the specified system.

  cat *file*                     The most common use of the **cat** Linux command is to read the contents of files. It is the most convenient command for this purpose in a Unix-like operating system.
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Task 1: Review DHCP/TFTP/SSH Configuration

As part of our data center expansion and the need for scalable deployments, the initial boot of new Cisco Nexus switches in a greenfield environment is a critical step for POAP. Rather than manual, error-prone configurations, POAP automates this vital process.

In this task, you will examine the foundational services and files on the Infra-Server, which is the central hub for automated provisioning. You will explore and verify the DHCP and TFTP configurations, crucial components that enable the Infra-Server to handle IP address assignment, deliver the POAP script, and provide device-specific configuration files. This review ensures that when a new switch powers on, it can seamlessly interact with these services ~~to automatically apply~~ **Consider moving the adverb (e.g., 'to quickly configure' → 'to configure quickly')** [Explanation: avoiding split infinitives when possible. Category: Grammar & Punctuation] its intended configuration, aligning with our goal of efficient, zero-touch deployments.

Activity

**Step ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** From the Student Workstation, launch a terminal and establish an SSH session to the Leaf-b switch. When prompted, accept the host key by typing **yes**, then log in with the provided credentials. Once connected, use the **show interface mgmt 0** command.

After running the **show interface mgmt0** on leaf-b command, note down the Hardware address (MAC address).

This step confirms the physical identity of the switch. The output shows the management interface MAC address, which should match the hardware address that is defined in the dhcpd.conf file on the Infra-Server. Matching these values ensures that the DHCP reservation is correctly tied to this device and that POAP will apply the right configuration.

student@student-vm:\~\$ **ssh admin@10.1.1.54**\
User Access Verification\
Password: 1234QWer\
\<\... output omitted \...\>\
\
leaf-b# **show interface mgmt 0**\
mgmt0 is up\
admin state is up,\
Hardware: Ethernet, address: 5254.007c.d963 (bia 5254.007c.d963)\
Internet Address is 10.1.1.54/24\
~~MTU~~ **Maximum Transmission Unit (MTU)** [Explanation: Acronym 'MTU' not expanded on first use. Category: Acronyms] 1500 bytes, BW 1000000 Kbit , DLY 10 usec\
reliability 255/255, txload ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]/255, rxload ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]/255\
Encapsulation ARPA, medium is broadcast\
full-duplex, 1000 Mb/s\
Auto-Negotiation is turned on\
Auto-mdix is turned off\
EtherType is 0x0000\
~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] minute input rate 1528 bits/sec, 0 packets/sec\
~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] minute output rate 624 bits/sec, 0 packets/sec\
Rx\
707 input packets 103 unicast packets 124 multicast packets\
480 broadcast packets 210619 bytes\
Tx\
100 output packets 64 unicast packets 32 multicast packets\
~~4~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] broadcast packets 20339 bytes\
Management transceiver: Absent\
Active connector: Link Down\
Configured Media-type: RJ45

You will later confirm or update the MAC addresses in the */etc/dhcp/dhcpd.conf* file on the Infra-Server.

Repeat this step on leaf-c and record its MAC address.

**Step ~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** On Leaf-b, run the **show hardware** command to display hardware details, including the serial number.

After running the **show hardware** command on leaf-b, note down the **Serial number**. Each serial number corresponds to a configuration file in the TFTP directory (/var/lib/tftpboot/conf.\<SERIAL\>).

Your serial numbers may differ from the examples shown. You will copy the configuration files that match your actual device serial numbers.

leaf-b# **show hardware**\
\<\... output omitted \...\>\
Manufacture Date is Year 1996 Week 0\
Serial number is 96NA44HCRU7\
\<\... output omitted \...\>

Repeat this step on leaf-c.

**Step ~~3~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** From the Student Workstation, launch a new terminal and establish an SSH session to the Infra-Server.

This connection ~~allows you to~~ **lets you** [Explanation: 'lets you' instead of 'allows you to'. Category: Cisco Style Guide] access the Infra-Server, which is responsible for running the DHCP and TFTP services that support the POAP process.

student@student-vm:\~\$\
student@student-vm:\~\$ **ssh cisco@10.1.1.254**\
cisco@10.1.1.254\'s password: **cisco**\
cisco@INFRA-SERVER:\~\$

**Step ~~4~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** The Infra-Server is acting as the DHCP server for this lab using **dhcpd** within Linux. Run the **cat** command on the dhcpd.conf file located in the */etc/dhcp/* folder.

In this configuration file, you will find that option 150 is set and configured. The option extends the TFTP boot option 66. For context, the option 66 only allows specifying one TFTP server while the option 150 specifies multiple TFTP servers. The TFTP server is used to host the bootstrap script poap.py that is fetched from the booting switch through the TFTP protocol. This script is run by the networking device to perform POAP. When the DHCP IP assignment is sent to the network device, it also sends the TFTP server address and the script location for the device to find the script. Other network protocols can also be used to fetch the script, such as HTTP.

cisco@INFRA-SERVER:\~\$ **cat /etc/dhcp/dhcpd.conf**\
\
ddns-update-style none;\
\
option domain-name \"ciscodevnet.com\";\
\
default-lease-time 3600;\
max-lease-time 7200;\
\
log-facility local7;\
\
option tftp-server-address code 150 = ip-address;\
\
subnet 10.1.1.0 netmask 255.255.255.0 {\
option routers 10.1.1.1;\
option tftp-server-address 10.1.1.254;\
\
}\
\
host leaf-b {\
hardware ethernet 52:54:00:7c~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]d9:63;\
fixed-address 10.1.1.54;\
option bootfile-name \"poap.py\";\
}\
\
host leaf-c {\
hardware ethernet 52:54:00:8c~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]a5~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]a3;\
fixed-address 10.1.1.55;\
option bootfile-name \"poap.py\";\
}

In this file, notice the MAC addresses associated with each host definition (leaf-b and leaf-c). These ensure that when a specific switch requests an IP address, the DHCP server recognizes it and assigns the correct reserved IP.

**Step ~~5~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** Update the MAC Addresses in the DHCP Configuration.

If the management MAC addresses you captured from leaf-b and leaf-c do not match what is shown in /etc/dhcp/dhcpd.conf, you must update them.

On the Infra-Server, open the DHCP configuration file.

host leaf-b {\
hardware ethernet 52:54:00:7c~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]d9:63; \# Replace with your actual MAC\
fixed-address 10.1.1.54;\
option bootfile-name \"poap.py\";\
}

Locate the host leaf-b section. Update the hardware Ethernet Line with the MAC address that you recorded from the show interface mgmt0 output on leaf-b. For example:

host leaf-b {\
hardware ethernet 52:54:00:7c~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]d9:63; \# Replace with your actual MAC\
fixed-address 10.1.1.54;\
option bootfile-name \"poap.py\";\
}

Do the same for the host leaf-c section, replacing the hardware Ethernet value with the actual MAC address from leaf-c.

host leaf-c {\
hardware ethernet 52:54:00:8c~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]a5~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]a3; \# Replace with your actual MAC\
fixed-address 10.1.1.55;\
option bootfile-name \"poap.py\";\
}

Press **Ctrl**+**O** then **Enter** to save, and **Ctrl**+**X** to exit.

The lab environment was only partially set up for you. You will need to start the actual services that are involved in POAP before you can configure devices with POAP.

**Step ~~6~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** After reviewing the configuration file, you need to restart the DHCP service, so the updated settings take effect. Once restarted, verify that the service is running correctly to ensure that switches can obtain their management IP addresses during POAP.

On the Infra-Server, elevate your privileges with the **sudo su** command, then restart the DHCP service using the **service isc-dhcp-server restart** command, and confirm its status with the **service isc-dhcp-server status** command. A successful status should display active (running) as shown in the following output.

cisco@INFRA-SERVER:\~\$ **sudo su**\
root@INFRA-SERVER:/home/cisco# **service isc-dhcp-server restart**\
root@INFRA-SERVER:/home/cisco# **service isc-dhcp-server status**Active: active (running) since Tue 2025-08-19 08:53:01 UTC; 7s ago\
Docs: man~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]dhcpd(~~8~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation])\
Main ~~PID~~ **Product Identifier (PID)** [Explanation: Acronym 'PID' not expanded on first use. Category: Acronyms]: 6982 (dhcpd)\
Tasks: ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] (limit: 9486)\
Memory: 1.7M (peak: 2.2M)\
CPU: 13ms\
CGroup: /system.slice/isc-dhcp-server.service\
~~??~~ **?** [Explanation: single question mark. Category: Grammar & Punctuation]6982 dhcpd -user dhcpd -group dhcpd -f -4 -pf /run/dhcp-server/dhcpd.pid -cf /etc/dhcp/dhcpd.conf\
\<\... output omitted \...\>

**Step ~~7~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** The TFTP service is responsible for delivering the POAP script and configuration files to the switches. To ensure that it is available, restart the service and verify that it is running properly.

On the Infra-Server, restart the TFTP service with the **service tftpd-hpa restart** command, then check its status using the **service tftpd-hpa status** command. A successful status should display active (running) as shown in the following output.

root@INFRA-SERVER:/home/cisco# **service tftpd-hpa restart**\
root@INFRA-SERVER:/home/cisco# **service tftpd-hpa status**\
? tftpd-hpa.service - LSB: HPA\'s tftp server\
Loaded: loaded (/etc/init.d/tftpd-hpa; generated)\
Active: active (running) since Tue 2025-08-19 08:54:47 UTC; 7s ago\
Docs: man~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]systemd-sysv-generator(~~8~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation])\
Process: 7030 ExecStart=/etc/init.d/tftpd-hpa start (code=exited, status=0/SUCCESS)\
Tasks: ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] (limit: 9486)\
Memory: 256.0K (peak: 1.7M)\
CPU: 17ms\
CGroup: /system.slice/tftpd-hpa.service\
~~??~~ **?** [Explanation: single question mark. Category: Grammar & Punctuation]7038 /usr/sbin/in.tftpd \~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]listen \~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]user tftp \~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]address 0.0.0.0:69 \~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]secure \~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]ipv4 /var/lib/tftpboot\
\<\... output omitted \...\>

**Step ~~8~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** On the Infra-Server, display the configuration file using the **cat /etc/default/tftpd-hpa** command. Confirm that the TFTP_DIRECTORY points to /var/lib/tftpboot.

The TFTP service uses a configuration file to define how it runs and where it stores files. This file is located in the /etc/default/ directory. Pay attention to the TFTP_DIRECTORY variable, which specifies the folder that is used to store files that will be served to the switches.

root@INFRA-SERVER:/home/cisco# **cat /etc/default/tftpd-hpa**\
\# /etc/default/tftpd-hpa\
\
TFTP_USERNAME=\"tftp\"\
TFTP_DIRECTORY=\"/var/lib/tftpboot\"\
TFTP_ADDRESS=\"0.0.0.0:69\"\
TFTP_OPTIONS=\"\~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]secure \~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]ipv4\"

**Step ~~9~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** Use the **ls -al /var/lib/tftpboot/** command to list all files in the TFTP directory. You should see the poap.py script along with two configuration files that are named by device identifiers, such as the serial number.

The /var/lib/tftpboot directory is where the Infra-Server stores files that will be served to the switches during POAP. This includes both the bootstrap script (poap.py) and the device-specific configuration files.

root@INFRA-SERVER:/home/cisco# **ls -al /var/lib/tftpboot/\
total 128**\
drwxr-xr-x ~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] root root 4096 Aug 19 08:58 .\
drwxr-xr-x 46 root root 4096 Aug 19 07:16 ..\
-rw-r\~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]r\~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation] ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] root root 2282 Aug 19 07:31 conf.96NA44HCRU7\
-rw-r\~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]r\~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation] ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] root root 2268 Aug 19 07:31 conf.9NFLH65S85G\
-rw-r\~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]r\~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation] ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] root root 114224 Aug 19 08:38 poap.py

Use the **cat** command to open each configuration file and check the hostname line. This will tell you~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]file belongs to leaf-b and~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]belongs to leaf-c. For example:

cisco@INFRA-SERVER:/var/lib/tftpboot\$ **cat conf.96NA44HCRU7**\
hostname leaf-b\
username admin password 0 1234QWer role network-admin\
~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation]\
nv overlay evpn\
feature ospf\
\...\
\<output omitted\>

In this example, you can see that the file conf.96NA44HCRU7 belongs to leaf-b.

**Step 10** Compare the serial numbers that you captured earlier with the filenames.

If the serial number from your device *matches* an existing file, no changes are required.

If the serial number *does not* match, copy one of the existing files and rename it to the actual serial number of your switch. For example:

cisco@INFRA-SERVER:/var/lib/tftpboot\$ sudo cp conf.9J1ZH86FDUU conf.\<YOUR_SERIAL\>

Replace \<YOUR_SERIAL\> with the serial number that is recorded from your device using show hardware.

Repeat this process for leaf-c.

**Step 11** Use the **cat** command to display the contents of the script. Review the header, which explains how to update the checksum, and confirm that the script points to the TFTP server (10.1.1.254) and uses the serial_number mode to identify the correct configuration file.

During the POAP process, the Cisco Nexus device will download and execute the poap.py script from the TFTP directory. This script defines the automation logic for provisioning the switch. In this lab, the script is designed to download a configuration file based on the device's serial number and skip the image download.

Pay close attention to the second line, which contains an **md5sum** value. This checksum must be recalculated if the script is modified, ensuring its integrity before execution.

root@INFRA-SERVER:/home/cisco# **cat /var/lib/tftpboot/poap.py**\
#~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation]/bin/env python3\
#md5sum=\"eb08329071ac99ccc2739640439152a3\"\
\"\"\"\
If any changes are made to this script, please run the below command\
in bash shell to update the above md5sum. This is used for integrity check.\
f=poap_nexus_script.py ; cat \$f \| sed \'/\^#md5sum/d\' \> \$f.md5 ; sed -i \\\
\"s/\^#md5sum=.\*/#md5sum=\\\"\$(md5sum \$f.md5 \| sed \'s/ .\*//\')\\\"/\" \$f\
\"\"\"\
\
import glob\
import os\
import pkgutil\
import re\
import shutil\
import signal\
import sys\
import syslog\
import time\
from time import gmtime, strftime\
import tarfile\
import errno\
import yaml\
\
try:\
import subprocess as sp\
except ImportError:\
sp = None\
\
try:\
from cisco import cli\
from cisco import transfer\
legacy = True\
except ImportError:\
from cli import \*\
legacy = False\
\
\
options = {\
\"username\": \"admin\", \# required by the framework even for tftp\
\"password\": \"\", \# not used by tftp\
\"hostname\": \"10.1.1.254\", \# your DHCP/TFTP server\
\"transfer_protocol\": \"tftp\", \# use TFTP\
\"mode\": \"serial_number\", \# pick config by POAP_SERIAL ? conf.\<SERIAL\>\
\"target_system_image\": \"nxos64-cs.10.5.3.f.bin\",\
}\
\
\<\... output omitted \...\>

The script is configured to run in serial number mode (mode: \"serial_number\"), which ensures the switch automatically retrieves the correct configuration file (for example, conf.\<SERIAL\>).

**Step 12** Change the directory to **/var/lib/tftpboot/** and run the provided commands to recalculate the checksum for poap.py as well as for each configuration file. This process updates the md5sum line in the files and creates .md5 checksum files. You can copy the output from poap_script.py.

Before the POAP process can succeed, the checksum values for the script and configuration files must be updated. This step ensures file integrity, allowing the Cisco Nexus switches to validate that the files have not been altered. When you update the checksum, a corresponding .md5 file is generated in the same directory.

root@INFRA-SERVER:/home/cisco# **cd /var/lib/tftpboot/**\
root@INFRA-SERVER:/var/lib/tftpboot# f**=poap.py ; cat \$f \| sed \'/\^#md5sum/d\' \> \$f.md5 ; sed -i \"s/\^#md5sum=.\*/#md5sum=\\\"\$(md5sum \$f.md5 \| sed \'s/ .\*//\')\\\"/\" \$f**\
root@INFRA-SERVER:/var/lib/tftpboot# **f=conf.96NA44HCRU7 ; cat \$f \| sed \'/\^#md5sum/d\' \> \$f.md5 ; sed -i \"s/\^#md5sum=.\*/#md5sum=\\\"\$(md5sum \$f.md5 \| sed \'s/ .\*//\')\\\"/\" \$f**\
root@INFRA-SERVER:/var/lib/tftpboot# **f=conf.9NFLH65S85G ; cat \$f \| sed \'/\^#md5sum/d\' \> \$f.md5 ; sed -i \"s/\^#md5sum=.\*/#md5sum=\\\"\$(md5sum \$f.md5 \| sed \'s/ .\*//\')\\\"/\" \$f**

Updating the checksum creates another file, **poap.py.md5**, in the same folder.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Always double-check the filenames in your lab environment. Device serial numbers might differ, which means your configuration filenames might not exactly match the examples that are shown here. Adjust the commands accordingly. |
+========================================================================================================================================================================================================================================+
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Step 13** Run the **ls -al** command in the /var/lib/tftpboot/ directory to list the contents. Verify that each configuration file and the poap.py script has a corresponding .md5 file.

You will see new .md5 files created in the same folder (for example, poap.py.md5).

root@INFRA-SERVER:/var/lib/tftpboot# **ls -al**\
total 248\
drwxr-xr-x ~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] root root 4096 Aug 19 09:07 .\
drwxr-xr-x 46 root root 4096 Aug 19 07:16 ..\
-rw-r\~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]r\~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation] ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] root root 2282 Aug 19 09:07 conf.96NA44HCRU7\
-rw-r\~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]r\~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation] ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] root root 2282 Aug 19 09:07 conf.96NA44HCRU7.md5\
-rw-r\~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]r\~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation] ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] root root 2268 Aug 19 09:07 conf.9NFLH65S85G\
-rw-r\~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]r\~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation] ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] root root 2268 Aug 19 09:07 conf.9NFLH65S85G.md5\
-rw-r\~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]r\~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation] ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] root root 111596 Aug 19 09:07 poap.py\
-rw-r\~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]r\~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation] ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] root root 111553 Aug 19 09:07 poap.py.md5

~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. Why must you update the MD5 checksum for poap.py and configuration files after editing them?

A. To allow TFTP to transfer files faster

B. To ensure file integrity and detect tampering

C. To automatically rename configuration files to match serial numbers

D. To enable POAP to run without DHCP

Task 2: Reprovision Cisco Nexus 9000v

Having thoroughly reviewed and prepared the core infrastructure services on the Infra-Server in Task ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation], you are now ready to put the POAP process into action. In line with our data center expansion scenario, this task focuses on the practical execution of POAP for one of our new Cisco Nexus 9000v devices. You will actively ~~initiate~~ **start** [Explanation: 'start' or 'begin' instead of 'initiate'. Category: Cisco Style Guide] the automated provisioning workflow, monitor the critical interactions between the switch and the Infra-Server, and ultimately verify that the device receives and applies its intended configuration. This is where you will see the power of ~~ZTP~~ **Zero Touch Provisioning (ZTP)** [Explanation: Acronym 'ZTP' not expanded on first use. Category: Acronyms] firsthand, as the switch transforms from a blank slate to a fully configured network element.

Activity

**Step ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** While you are still connected to the Infra-Server, run the **tail -f /var/log/syslog** command to monitor incoming DHCP requests during the POAP process.

At this point, you will not see DHCP messages yet because POAP has not been enabled on the switch. The terminal will simply wait and display new entries as they arrive. Keeping this command running ensures you can capture the DHCP requests and responses in ~~real time~~ **Change 'real time' to 'real-time'** [Explanation: Hyphenate 'real-time' when used as a compound modifier. Category: Grammar & Punctuation] once POAP starts.

cisco@INFRA-SERVER:\~\$ **tail -f /var/log/syslog**

**Step ~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** From your Student VM, open a new terminal and SSH to **server-a** using the username **admin** and password **1234QWer**. Once logged in, attempt to ping **server-b**.

The first SSH connection may prompt you to accept the server's key fingerprint. Type **yes** to continue, then provide the password.

student@student-vm:\~\$ **ssh admin@10.1.1.101**\
The authenticity of host \'10.1.1.101 (10.1.1.101)\' can\'t be established.\
ED25519 key fingerprint is SHA256~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]aLN5r8GU/yhtJbPXXAOqHiaqU+92uurIxVfZ7Ap2T9I.\
This key is not known by any other names\
Are you sure you want to continue connecting (yes/no/\[fingerprint\])? **yes**\
\
The Alpine Wiki contains a large amount of how-to guides and general\
information about administrating Alpine systems.\
See \<https://wiki.alpinelinux.org/\>.\
\
You can setup the system with the command: setup-alpine\
\
You may change this message by editing /etc/motd.\
\
server-a:\~

Once on server-a, the ping to server-b will fail at this stage because the leaf switches have not yet been provisioned through POAP. This failed test provides a baseline---after POAP, the ping will succeed, confirming end-to-end connectivity across the fabric.

server-a:\~\$ **ping 192.168.10.102\
**\
\-\~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation] 192.168.10.102 ping statistics \-\~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation] 33 packets transmitted, 0 packets received, 100% packet loss server-a:\~\$ \^C

**Step ~~3~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** From your Student VM, open a web browser and connect to your CML environment. When prompted, enter the credentials **username** admin and password **1234QWer**.

Accessing CML through the browser ~~allows you to~~ **lets you** [Explanation: 'lets you' instead of 'allows you to'. Category: Cisco Style Guide] interact with the lab topology and device consoles. This is where you will connect to the Cisco Nexus switches to observe and control the POAP workflow.

![Screenshot of a login screen for Cisco Modeling Labs, showing input fields for Username and Password. The admin username is prefilled, and the password field is obscured. Both input fields are highlighted by a pink rectangle. A LOGIN button is visible, along with the browser bar displaying the U R L 10.1.1.20 slash login.](media/image8.bin){width="6.94027668416448in" height="5.344384295713036in"}

**Step ~~4~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** After logging in to the CML environment, navigate to your topology. Connect to the console on leaf-2.

To connect to the console right-~~click on~~ **click** [Explanation: 'click' instead of 'click on'. Category: Cisco Style Guide] **leaf-2** and then select **Console**. This action opens an interactive console session for the Cisco Nexus switch inside CML. The console gives you direct access to the device's boot process and configuration.

![Diagram illustrating a Cisco Modeling Labs network topology diagram featuring a spine leaf architecture. There are two spine nodes, spine one and spine two, and three leaf nodes, leaf one, leaf two, and leaf three. Two server nodes are also present, labeled ubuntu dev and server B. A context menu is open on leaf two, highlighting the Console option with a pink rectangle among other actions like Stop, Add Link, Hide Links, Delete, and Wipe. Interface labels, such as E one slash 13, are visible on the links.](media/image9.bin){width="4.5870964566929135in" height="5.012902449693788in"}

**Step ~~5~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** Select **OPEN CONSOLE** and log in to the switch using username **admin** and password **1234QWer**.

Logging in gives you direct control of the Cisco Nexus switch. This is the foundation for the rest of the lab, because POAP provisioning and verification all happen from the CLI.

User Access Verification\
leaf-b login: **admin**\
Password: **1234QWer**\
leaf-b#

**Step ~~6~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** On leaf-b, view the current configuration before POAP so you have a baseline to compare after provisioning.

You should see only a minimal, pre-provisioned configuration. This baseline helps you confirm~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]changes were applied by POAP after the reload.

leaf-b# **show running-config**\
\
~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation]Command: show running-config\
~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation]Running configuration last done at: Tue Sep ~~9~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] 11:05:28 2025\
~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation]Time: Wed Sep 10 06:37:14 2025\
\
version 10.5(~~3~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]) Bios~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]version\
hostname leaf-b\
nv overlay evpn\
feature ospf\
feature bgp\
feature pim\
feature interface-vlan\
feature vn-segment-vlan-based\
feature lacp\
feature dhcp\
feature lldp\
feature nv overlay\
feature ngoam\
\
username admin password ~~5~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] \$~~5~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\$DEGKNA\$GVWhbIl0Okouok3vruJlE6jwPPI7bOoRox3z34nUQj3\
role network-admin\
ip domain-lookup\
copp profile strict\
snmp-server user admin network-admin auth md5 365F760E19310D484A37659E91DB273AFB\
9C priv aes-128 366B7B0F4E474515452A3B8285DF0A729FBE localizedV2key\
rmon event ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] log trap public description FATAL(~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]) owner PMON@FATAL\
rmon event ~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] log trap public description CRITICAL(~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]) owner PMON@CRITICAL\
rmon event ~~3~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] log trap public description ERROR(~~3~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]) owner PMON@ERROR\
rmon event ~~4~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] log trap public description WARNING(~~4~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]) owner PMON@WARNING\
rmon event ~~5~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] log trap public description INFORMATION(~~5~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]) owner PMON@INFO\
\
vlan ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\
\
service dhcp\
ip dhcp relay\
ipv6 dhcp relay\
vrf context management\
ip route 0.0.0.0/0 10.1.1.1\
\
\
interface Vlan1\
\
interface Ethernet1/1\
\
interface Ethernet1/2\
\
interface Ethernet1/3\
\...\
\<output omitted\>\
\...\
interface mgmt0\
vrf member management\
ip address 10.1.1.54/24\
icam monitor scale\
\
line console\
line vty\
boot nxos bootflash:/nxos64-cs.10.5.3.F.bin

**Step ~~7~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** On leaf-b, enter configuration mode and enable POAP boot with the **boot poap enable** command. Save the running configuration to startup, then reload the switch to ~~initiate~~ **start** [Explanation: 'start' or 'begin' instead of 'initiate'. Category: Cisco Style Guide] the POAP process.

After you enable POAP and reload, the device will obtain an address from DHCP, learn the TFTP server, and fetch the poap.py script. No additional input is required during this process.

leaf-b# **configure terminal**\
Enter configuration commands, one per line. End with CNTL/Z.\
leaf-b(config)# **boot poap enable**\
leaf-b(config)# **copy running-config startup-config**\
\[########################################\] 100%\
Copy complete, now saving to disk (please wait)\...\
Copy complete.\
leaf-b(config)# **reload**\
This command will reboot the system. (y/n)? \[n\] **y**

To start POAP, you would normally erase the startup configuration and reload a device. In this remote lab, the startup configuration enables POAP boot and specifies the boot image to prevent the virtual switch from getting stuck in the bootloader. This allows the switch to be provisioned through POAP despite a non-empty startup configuration.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]If you are observing the switch boot process via CML, the switch will ask you if you wish to go back to normal setup. There is no need to press anything, wait for the switch to execute the POAP boot. |
+=============================================================================================================================================================================================================+
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Step ~~8~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** Return to the syslog terminal on the Infra-Server and watch for DHCP activity that is generated by the POAP process using the **tail -f /var/log/syslog** command.

You should see DHCPDISCOVER, DHCPOFFER, DHCPREQUEST, and acknowledgment messages exchanged between the switch and the server.

Seeing a final DHCPACK confirms the switch received its management IP and the TFTP server info (option 150). If you do not see ACK, re-check that *isc-dhcp-server* is active and that the host reservation/mask are correct.

cisco@INFRA-SERVER:\~\$ **tail -f /var/log/syslog**\
\
2025-08-19T09:34:52.959589+00:00 ubuntu dhcpd\[6982\]: DHCPDISCOVER from 52:54:00:7c~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]d9:63 via ens2\
2025-08-19T09:34:52.959761+00:00 ubuntu dhcpd\[6982\]: DHCPOFFER on 10.1.1.54 to 52:54:00:7c~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]d9:63 via ens2\
2025-08-19T09:34:53.961121+00:00 ubuntu dhcpd\[6982\]: DHCPDISCOVER from 52:54:00:7c~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]d9:63 via ens2\
2025-08-19T09:34:53.961412+00:00 ubuntu dhcpd\[6982\]: DHCPOFFER on 10.1.1.54 to 52:54:00:7c~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]d9:63 via ens2\
2025-08-19T09:34:59.970087+00:00 ubuntu dhcpd\[6982\]: DHCPREQUEST for 10.1.1.54 (10.1.1.254) from 52:54:00:7c~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]d9:63 via ens2\
2025-08-19T09:34:59.970392+00:00 ubuntu dhcpd\[6982\]: DHCPACK on 10.1.1.54 to 52:54:00:7c~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]d9:63 via ens2

**Step ~~9~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** Go back to the CML console for the switch and watch the output as the POAP workflow begins.

You will see the switch send out DHCP requests, receive an IP address, netmask, and default gateway, and learn the location of the TFTP server. Once network connectivity is established, the device downloads the poap.py script from the TFTP server and checks its MD5 checksum to confirm file integrity. After validation, the script runs and selects the appropriate configuration file based on the device's serial number. Both the configuration file and its checksum are then copied to the switch, ensuring the file is authentic before it is applied.

2025 Aug 19 09:34:42 switch %\$ VDC-1 %\$ %POAP-2-POAP_INFO: - Abort Power On Auto Provisioning \[yes - continue with normal setup, no - continue with Power On Auto Provisioning\] (yes/no)\[no\]:\
2025 Aug 19 09:34:43 switch %\$ VDC-1 %\$ %POAP-2-POAP_INFO: Recieved DHCP offer from server ip - 10.1.1.254\
2025 Aug 19 09:34:50 switch %\$ VDC-1 %\$ %POAP-2-POAP_INFO: \[96NA44HCRU7-52:7C~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]D9:63:1B:08\] - Using DHCP, valid information received over mgmt0 from 10.1.1.254\
2025 Aug 19 09:34:50 switch %\$ VDC-1 %\$ %POAP-2-POAP_INFO: \[96NA44HCRU7-52:7C~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]D9:63:1B:08\] - Assigned IP address: 10.1.1.54\
2025 Aug 19 09:34:50 switch %\$ VDC-1 %\$ %POAP-2-POAP_INFO: \[96NA44HCRU7-52:7C~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]D9:63:1B:08\] - Netmask: 255.255.255.0\
2025 Aug 19 09:34:50 switch %\$ VDC-1 %\$ %POAP-2-POAP_INFO: \[96NA44HCRU7-52:7C~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]D9:63:1B:08\] - Default Gateway: 10.1.1.1\
2025 Aug 19 09:34:50 switch %\$ VDC-1 %\$ %POAP-2-POAP_INFO: \[96NA44HCRU7-52:7C~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]D9:63:1B:08\] - Script Server: 10.1.1.254\
2025 Aug 19 09:34:50 switch %\$ VDC-1 %\$ %POAP-2-POAP_INFO: \[96NA44HCRU7-52:7C~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]D9:63:1B:08\] - Script Name: poap.py\
2025 Aug 19 09:35:01 switch %\$ VDC-1 %\$ %POAP-2-POAP_INFO: \[96NA44HCRU7-52:7C~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]D9:63:1B:08\] - The POAP Script download has started\
2025 Aug 19 09:35:01 switch %\$ VDC-1 %\$ %POAP-2-POAP_INFO: \[96NA44HCRU7-52:7C~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]D9:63:1B:08\] - The POAP Script is being downloaded from \[copy tftp://10.1.1.254/poap.py bootflash~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]scripts/script.sh vrf management \]\
2025 Aug 19 09:35:02 switch %\$ VDC-1 %\$ %POAP-2-POAP_SCRIPT_DOWNLOADED: \[96NA44HCRU7-52:7C~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]D9:63:1B:08\] - Successfully downloaded POAP script file\
2025 Aug 19 09:35:02 switch %\$ VDC-1 %\$ %POAP-2-POAP_INFO: \[96NA44HCRU7-52:7C~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]D9:63:1B:08\] - Script file size 111596, MD5 checksum 6d93e5f83d23a13363510b69553c08d8\
2025 Aug 19 09:35:02 switch %\$ VDC-1 %\$ %POAP-2-POAP_INFO: \[96NA44HCRU7-52:7C~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]D9:63:1B:08\] - MD5 checksum received from the script file is 6d93e5f83d23a13363510b69553c08d8\
2025 Aug 19 09:35:02 switch %\$ VDC-1 %\$ %POAP-2-POAP_SCRIPT_STARTED_MD5_VALIDATED: \[96NA44HCRU7-52:7C~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]D9:63:1B:08\] - POAP script execution started(MD5 validated)\
2025 Aug 19 09:35:04 switch %\$ VDC-1 %\$ %USER-1-SYSTEM_MSG: - Logfile name: /bootflash/20250819093504_poap_12065_script.log - script.sh\
2025 Aug 19 09:35:04 switch %\$ VDC-1 %\$ %USER-1-SYSTEM_MSG: - Found ~~5~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] POAP script logs - script.sh\
2025 Aug 19 09:35:04 switch %\$ VDC-1 %\$ %USER-1-SYSTEM_MSG: - Setting source cfg filename based-on serial number - script.sh\
2025 Aug 19 09:35:04 switch %\$ VDC-1 %\$ %USER-1-SYSTEM_MSG: - serial number 96NA44HCRU7 - script.sh\
2025 Aug 19 09:35:04 switch %\$ VDC-1 %\$ %USER-1-SYSTEM_MSG: - Selected conf file name : conf.96NA44HCRU7 - script.sh\
2025 Aug 19 09:35:04 switch %\$ VDC-1 %\$ %USER-1-SYSTEM_MSG: S/N\[96NA44HCRU7\]-MAC\[52:54:00:7C~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]D9:63\] - Verifying freespace in bootflash - script.sh\
2025 Aug 19 09:35:04 switch %\$ VDC-1 %\$ %USER-1-SYSTEM_MSG: S/N\[96NA44HCRU7\]-MAC\[52:54:00:7C~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]D9:63\] - Free bootflash space is 4943940.0 KB - script.sh\
2025 Aug 19 09:35:04 switch %\$ VDC-1 %\$ %USER-1-SYSTEM_MSG: S/N\[96NA44HCRU7\]-MAC\[52:54:00:7C~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]D9:63\] - Single image is set - script.sh\
2025 Aug 19 09:35:04 switch %\$ VDC-1 %\$ %USER-1-SYSTEM_MSG: S/N\[96NA44HCRU7\]-MAC\[52:54:00:7C~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]D9:63\] - Copying config file - script.sh\
2025 Aug 19 09:35:04 switch %\$ VDC-1 %\$ %USER-1-SYSTEM_MSG: S/N\[96NA44HCRU7\]-MAC\[52:54:00:7C~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]D9:63\] - Copying MD5 information - script.sh\
2025 Aug 19 09:35:04 switch %\$ VDC-1 %\$ %USER-1-SYSTEM_MSG: S/N\[96NA44HCRU7\]-MAC\[52:54:00:7C~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]D9:63\] - Starting Copy of MD5. src = /var/lib/tftpboot/conf.96NA44HCRU7.md5 dest = /bootflash/conf.96NA44HCRU7.md5 - script.sh\
2025 Aug 19 09:35:04 switch %\$ VDC-1 %\$ %USER-1-SYSTEM_MSG: S/N\[96NA44HCRU7\]-MAC\[52:54:00:7C~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]D9:63\] - File transfer_protocol = tftp - script.sh\
2025 Aug 19 09:35:04 switch %\$ VDC-1 %\$ %USER-1-SYSTEM_MSG: S/N\[96NA44HCRU7\]-MAC\[52:54:00:7C~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]D9:63\] - Copying file options source=/var/lib/tftpboot/conf.96NA44HCRU7.md5 destination=/bootflash/conf.96NA44HCRU7.md5 login_timeout=120 destination_tmp=conf.96NA44HCRU7.md5.tmp - script.sh\
2025 Aug 19 09:35:04 switch %\$ VDC-1 %\$ %USER-1-SYSTEM_MSG: S/N\[96NA44HCRU7\]-MAC\[52:54:00:7C~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]D9:63\] - Transfering using tftp from /var/lib/tftpboot/conf.96NA44HCRU7.md5 to bootflash:/conf.96NA44HCRU7.md5.tmp hostname 10.1.1.254 vrf management - script.sh\
2025 Aug 19 09:35:04 switch %\$ VDC-1 %\$ %USER-1-SYSTEM_MSG: S/N\[96NA44HCRU7\]-MAC\[52:54:00:7C~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]D9:63\] - Command is : terminal dont-ask ; copy tftp://10.1.1.254/conf.96NA44HCRU7.md5 bootflash:/conf.96NA44HCRU7.md5.tmp vrf management - script.sh\
2025 Aug 19 09:35:05 switch %\$ VDC-1 %\$ %USER-1-SYSTEM_MSG: S/N\[96NA44HCRU7\]-MAC\[52:54:00:7C~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]D9:63\] - \*\*\* Downloaded file is of size 2282 \*\*\* - script.sh\
2025 Aug 19 09:35:05 switch %\$ VDC-1 %\$ %USER-1-SYSTEM_MSG: S/N\[96NA44HCRU7\]-MAC\[52:54:00:7C~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]D9:63\] - Renamed /bootflash/conf.96NA44HCRU7.md5.tmp to /bootflash/conf.96NA44HCRU7.md5 - script.sh\
2025 Aug 19 09:35:05 switch %\$ VDC-1 %\$ %USER-1-SYSTEM_MSG: S/N\[96NA44HCRU7\]-MAC\[52:54:00:7C~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]D9:63\] - Found non-MD5 checksum in conf.96NA44HCRU7.md5: hostname leaf-b - script.sh\
\<\... output omitted \...\>\
2025 Aug 19 09:35:10 switch %\$ VDC-1 %\$ %POAP-2-POAP_SCRIPT_EXEC_SUCCESS: \[96NA44HCRU7-52:7C~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]D9:63:1B:08\] - POAP script execution success\
2025 Aug 19 09:35:11 switch %\$ VDC-1 %\$ %POAP-2-POAP_RELOAD_DEVICE: \[96NA44HCRU7-52:7C~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]D9:63:1B:08\] - Reload device\
\<\... output omitted \...\>

These logs show how POAP automates what would otherwise be a manual provisioning process---assigning network details, pulling scripts, validating integrity, and finally applying the intended configuration.

POAP takes about ~~5~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] minutes as the switch will reload after applying its configuration.

+--------------------------------------------------------------------------------------------------------------------------------------------------+
| 3~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]**If POAP stalls at DHCP:** Re-check the hardware Ethernet Lines in the DHCP config file /etc/dhcp/dhcpd.conf~~.                               ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]|
|                                                                                                                                                  |
| 4~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]**If POAP stalls at TFTP:** Confirm the presence of the POAP script, config files and MD5 files under /var/lib/tftpboot/~~.                    ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]|
|                                                                                                                                                  |
| 5~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]**If the switch cannot find its configuration file:** Ensure the config filename matches the serial number exactly under /var/lib/tftpboot/. |
+==================================================================================================================================================+
+--------------------------------------------------------------------------------------------------------------------------------------------------+

**Step 10** From the Infra-Server, attempt to establish an SSH connection to the leaf-b switch. A warning message will be displayed indicating that the RSA fingerprint does not match the one in the *know_hosts* file.

Since the device has been reloaded and re-provisioned, you will see a host key mismatch warning. This occurs because the RSA fingerprint for the device has changed compared to what is stored in the known_hosts file. The warning message also shows the exact command that is needed to remove the old entry so that a new key can be accepted.

cisco@INFRA-SERVER:\~\$ **ssh cisco@10.1.1.54**\
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\
@ WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation] @\
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\
~~IT~~ **Information Technology (IT)** [Explanation: Acronym 'IT' not expanded on first use. Category: Acronyms] IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation]\
Someone could be eavesdropping on you right now (man-in-the-middle attack)~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation]\
It is also possible that a host key has just been changed.\
The fingerprint for the RSA key sent by the remote host is\
SHA256~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]kj+jMGP3wUmqHSM3vFZF1AuRAuI7cwM1xp9LCGUm714.\
Please contact your system administrator.\
Add correct host key in /home/cisco/.ssh/known_hosts to get rid of this message.\
Offending RSA key in /home/cisco/.ssh/known_hosts:1\
remove with~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]ssh-keygen -f \'/home/cisco/.ssh/known_hosts\' -R \'10.1.1.54\'\
Host key for 10.1.1.54 has changed and you have requested strict checking.\
Host key verification failed.

**Step 11** Run appropriate commands to remove the hostname and the IP address from the known_hosts file.

On the Infra-Server, remove the outdated key for the leaf-b switch from the known_hosts file. This will allow you to establish a new SSH session without host key verification errors.

cisco@INFRA-SERVER:\~\$ **ssh-keygen -f \"/home/student/.ssh/known_hosts\" -R \"10.1.1.54\"**\
\# Host 10.1.1.54 found: line 10\
/home/student/.ssh/known_hosts updated.\
Original contents retained as /home/student/.ssh/known_hosts.old

**Step 12** Connect through SSH again and log in using the username **admin** and password **1234QWer**.

From the Infra-Server, establish an SSH connection to the **leaf-b** switch using the admin credentials. Since the old host key was cleared, you will be prompted to accept the new RSA fingerprint. Type yes to proceed, then log in with the username **admin** and password **1234QWer**.

cisco@INFRA-SERVER:\~\$ **ssh admin@10.1.1.54**\
The authenticity of host \'10.1.1.54 (10.1.1.54)\' can\'t be established.\
RSA key fingerprint is SHA256~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]kj+jMGP3wUmqHSM3vFZF1AuRAuI7cwM1xp9LCGUm714.\
This key is not known by any other names\
Are you sure you want to continue connecting (yes/no/\[fingerprint\])? **yes**\
Warning: Permanently added \'10.1.1.54\' (RSA) to the list of known hosts.\
User Access Verification\
(admin@10.1.1.54) Password: **1234QWer**\
\
\<\... output omitted \...\>\
\
leaf-b#

**Step 13** Confirm that the startup-configuration and running-configuration are identical to the configuration provided by the TFTP Server.

The output should display the expected configuration, including the hostname, features, and other parameters pushed through POAP.

leaf-b# **show startup-config\
**\
~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation]Command: show startup-config\
~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation]Time: Tue Aug 19 09:51:31 2025\
~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation]Startup config saved at: Tue Aug 19 09:40:19 2025\
\
version 10.5(~~3~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]) Bios~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]version\
hostname leaf-b\
vdc leaf-b id ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\
limit-resource vlan minimum 16 maximum 4094\
limit-resource vrf minimum ~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] maximum 4096\
limit-resource port-channel minimum 0 maximum 511\
limit-resource m4route-mem minimum 58 maximum 58\
limit-resource m6route-mem minimum ~~8~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] maximum ~~8~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\
\
nv overlay evpn\
feature ospf\
feature bgp\
feature pim\
feature interface-vlan\
feature vn-segment-vlan-based\
feature lacp\
feature dhcp\
feature lldp\
feature nv overlay\
feature ngoam\
\
username admin password 5 \$5\$GAKCCK\$x1LXzP.xab9C4UikXkQGRkshN99xTYxFx7tF5w7byU/ role network-admin\
ip domain-lookup\
copp profile lenient\
\
\<\... output omitted \...\>

~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. During the POAP workflow, what action does the switch take immediately after downloading the poap.py script?

A. Applies ~~VLANs~~ **virtual LAN (VLAN)** [Explanation: Acronym 'VLAN' not expanded on first use. Category: Acronyms] and routing protocols directly

B. Validates the script's MD5 checksum

C. Registers with Cisco Intersight automatically

D. Copies startup-config to bootflash

Final Challenge: Provision Leaf-c with POAP

Now that you have successfully provisioned **leaf-b**, it is time ~~to apply the~~ **Consider moving the adverb (e.g., 'to quickly configure' → 'to configure quickly')** [Explanation: avoiding split infinitives when possible. Category: Grammar & Punctuation] same process to **leaf-c**. This will serve as your final challenge for this lab. Unlike the previous steps, no detailed instructions are provided. You are expected to use the knowledge gained so far to complete the provisioning on your own.

Your goal is to ensure that **leaf-c** is fully provisioned through POAP, just like **leaf-b**. To achieve this, you will need to:

-   Prepare the Infra-Server to monitor DHCP requests and verify script/config file access.

-   Connect to leaf-c through CML, enable POAP boot, and reload the device.

-   Observe the POAP process in both the syslog and the CML console to confirm the script and configuration file are applied.

-   Verify that the configuration matches the intended file from the TFTP server.

When completed, leaf-c should be running with the startup-configuration that is delivered by the POAP process, demonstrating that you can independently reprovision a Cisco Nexus device.

As a final test, connect to server-a and ping server-b. Successful pings confirm that connectivity is established across the fabric:

server-a:\~\$ **ping 192.168.10.102**\
PING 192.168.10.102 (192.168.10.102): 56 data bytes\
64 bytes from 192.168.10.102: seq=0 ttl=42 time=7.096 ms\
64 bytes from 192.168.10.102: seq=1 ttl=42 time=9.545 ms\
64 bytes from 192.168.10.102: seq=2 ttl=42 time=10.198 ms\
64 bytes from 192.168.10.102: seq=~~3~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] ttl=42 time=9.197 ms\
64 bytes from 192.168.10.102: seq=~~4~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] ttl=42 time=10.131 ms\
\-\~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation] 192.168.10.102 ping statistics \-\~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]\
~~5~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] packets transmitted, ~~5~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] packets received, 0% packet loss\
round-trip min/avg/max = 7.096/9.233/10.198 ms

If the ping is successful, it confirms that the fabric is correctly provisioned, and both servers are now reachable through the configured leaf switches.

This lab simulation provides a comprehensive, hands-on experience with Cisco POAP, enabling network engineers ~~to efficiently deploy~~ **Consider moving the adverb (e.g., 'to quickly configure' → 'to configure quickly')** [Explanation: avoiding split infinitives when possible. Category: Grammar & Punctuation] and manage Cisco Nexus devices at scale.

~~3~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. The poap.py script that is used in the POAP process contains an options dictionary. Which parameter within this dictionary is responsible for instructing the Cisco Nexus switch to select a configuration file based on its unique serial number?

A. transfer_protocol

B. hostname

C. target_system_image

D. mode

Summary

Now that you have seen how Day-Zero provisioning works on Cisco Nexus devices, you can apply these practices to accelerate deployments, eliminate repetitive manual work, and ensure consistent configurations across your data center.

Consider each of the following reflection questions now that you have completed the learning content:

-   When deploying new Cisco Nexus switches, what challenges have you encountered with manual configuration?

-   How would you design the supporting services---DHCP, TFTP/HTTP, and configuration servers---to enable a smooth POAP workflow?

-   Which DHCP options are most critical in your environment, and how would you use them to guide device bootstrapping?

-   How would you customize the poap.py script to deliver software images, configs, and agents that align with your organization's standards?

-   How do you plan ~~to apply POAP~~ **Consider moving the adverb (e.g., 'to quickly configure' → 'to configure quickly')** [Explanation: avoiding split infinitives when possible. Category: Grammar & Punctuation] and Python scripting in your own role to streamline operations and reduce deployment time?

By applying what you have learned in this learning content, you will be able to transform initial provisioning from a manual, error-prone task into a predictable, automated workflow. This makes you a valuable contributor to faster project delivery, operational consistency, and improved reliability in your organization's data center.

Summary Challenge

~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. What is one of the main benefits of using POAP in large-scale data center deployments?

A. Provides continuous traffic monitoring

B. Automates initial switch setup with consistency

C. Eliminates the need for software image

D. Reduces the number of DHCP servers required

~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. Which day-zero provisioning technology can execute a Python script as part of its workflow?

A. POAP

B. iPXE

C. Etherboot

D. gPXE

~~3~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. Which step occurs first when a Cisco Nexus switch boots without a startup configuration and enters the POAP workflow?

A. The switch downloads the Python script from the TFTP/HTTP server.

B. The switch applies the configuration and reloads.

C. The switch acts as a DHCP client to obtain an IP address and boot parameters.

D. The switch installs the target NX-OS image.

~~4~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. Which identifier can POAP use ~~to uniquely match~~ **Consider moving the adverb (e.g., 'to quickly configure' → 'to configure quickly')** [Explanation: avoiding split infinitives when possible. Category: Grammar & Punctuation] a Cisco Nexus switch to the correct configuration file?

A. Hostname

B. Serial number

C. VLAN ID

D. IP address of the management interface

~~5~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. Which DHCP option does POAP use to locate the TFTP server to obtain the POAP script?

A. Option 66

B. Option 67

C. Option 15

D. Option 151

~~6~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. Which DHCP option returns a list of TFTP servers that can be used by POAP to retrieve the configuration file?

A. Option 47

B. Option 66

C. Option 67

D. Option 150

~~7~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. Which two protocols are required to ~~leverage~~ **use** [Explanation: 'use' instead of 'leverage'. Category: Cisco Style Guide] POAP? (Choose two.)

A. DHCP

B. HTTP

C. HTTPS

D. RSH

E. SSH

F. TFTP

Answer Key

Day-Zero Operations

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]B

PowerOn Auto Provisioning

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]B

Python Script for POAP

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]C

Discovery 1: Set Up PowerOn Auto Provisioning on the Cisco Nexus 9000

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]B

```{=html}
<!-- -->
```
1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]B

```{=html}
<!-- -->
```
1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]D

Summary Challenge

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]B

2~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]A

3~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]C

4~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]B

5~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]A

6~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]D

7~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]A, F


---

## Change Legend

| Markup | Meaning |
|--------|---------|
| ~~text~~ | Text to remove (strikethrough) |
| **text** | Text to add (bold) |
| [Explanation: ...] | Rationale for change |

*Generated by Course AI Editor on 2026-03-04 15:34*