# Inline Editorial Review: Network Access for Non-Supplicant Devices_Sec 01_orig

**Instructions**: Search for `~~` to find deletions and `**` to find additions.
Copy this document into Word to see Track Changes formatting.

---

**Total Changes**: 217 (Auto-fix: 82, Review: 119, Questions: 16)

---

Section 1: Network Access for Non-Supplicant Devices

Introduction

As part of a network engineering team managing secure access across a large Cisco-based enterprise, your organization has already deployed IEEE [QUESTION: Unknown acronym 'IEEE' - please provide expansion or confirm intentional. Category: Acronyms] 802.1X authentication on your network access devices to enforce identity-based controls for users and devices. However, despite this implementation, you have encountered numerous endpoints (such as printers, IP phones, security cameras, and other Internet of Things \[IoT\] devices) that are not 802.1X-capable. These non-supplicant devices present unique challenges. Without an alternative authentication method, these devices are either blocked from network access entirely or placed in open ~~VLANs~~ **virtual LAN (VLAN)** [Explanation: Acronym 'VLAN' not expanded on first use. Category: Acronyms], undermining your enterprise access control policies.

Imagine the risks introduced when critical but unmanaged devices bypass authentication. For example, a misconfigured printer could offer an entry point for lateral movement, or an IP camera without proper access controls could allow unauthorized monitoring or data exfiltration.

  ------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][http://schemas.openxmlformats.org/drawingml/2006/picture](media/image1.bin){width="0.9741929133858268in" height="0.9741929133858268in"}   While 802.1X provides robust user and device authentication, an enterprise network needs fallback mechanisms like ~~MAC~~ **Media Access Control (MAC)** [Explanation: Acronym 'MAC' not expanded on first use. Category: Acronyms] Authentication Bypass (MAB) to maintain both security and operational continuity. This approach is instrumentational in preserving the integrity of your access control model and aligning with enterprise Zero Trust goals.

  ------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image2.bin){width="6.940277777777778in" height="3.1080369641294836in"}

  ------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][http://schemas.openxmlformats.org/drawingml/2006/picture](media/image3.bin){width="0.9741929133858268in" height="0.9741929133858268in"}   This course provides a comprehensive overview of implementing MAB on Cisco network access devices ~~to securely onboard~~ **Consider moving the adverb (e.g., 'to quickly configure' → 'to configure quickly')** [Explanation: avoiding split infinitives when possible. Category: Grammar & Punctuation] non-supplicant devices in an 802.1X-enabled network. You will gain an in-depth knowledge on how to design, configure, and validate MAB policies, integrate them with ~~RADIUS~~ **Remote Authentication Dial-In User Service (RADIUS)** [Explanation: Acronym 'RADIUS' not expanded on first use. Category: Acronyms] authentication, and apply identity-based access controls that meet enterprise security standards.

  ------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In this course, you will learn to:

-   Explain why MAB is required as a fallback mechanism in an 802.1X-authenticated Cisco network.

-   Identify and categorize devices that require MAB (e.g., printers, IP phones, IoT endpoints).

-   Configure Cisco Catalyst switch interfaces for Flexible Authentication using 802.1X and MAB.

-   Integrate Cisco Catalyst switches with RADIUS servers (such as Cisco Identity Services Engine \[ISE\]) for MAC-based authentication and policy assignment.

-   Validate MAB sessions on Cisco Catalyst switches and monitor authentication events using ISE live logs and CLI tools.

-   Identify and mitigate the limitations and security concerns of MAB, such as MAC spoofing risks.

-   Configure, test, and troubleshoot MAB on Cisco Catalyst switches using real-world scenarios.

By the end of this training, you'll be equipped to implement a secure, policy-driven access solution that integrates MAB alongside 802.1X. This will help you ensure consistent enterprise-wide access control for both user and device populations.

Let's get started building a wired network security foundation that you can trust.

MAC Authentication Bypass (MAB) Overview

As a network engineer, you have begun to implement access control in your organization and are deploying 802.1X where possible. However, as shown in the following diagram, you have identified various devices that cannot authenticate using 802.1X.

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image4.bin){width="6.940277777777778in" height="2.5470286526684163in"}

You have determined that these devices may not be able to use 802.1X authentication for the following reasons:

-   Supplicant software is not available for a specific client platform.

-   Supplicant software is not enabled, not configured, or is misconfigured and will need to obtain access to the network for support.

-   Client configuration is not under your administrative control.

-   802.1X requests are not supported on specific networks.

Due to these limitations, the devices either need to have an alternate means to authenticate or must have a fallback mechanism to authenticate if 802.1X is unable to be used.

  ------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][http://schemas.openxmlformats.org/drawingml/2006/picture](media/image3.bin){width="0.9741929133858268in" height="0.9741929133858268in"}   This training introduces MAC Authentication Bypass (MAB), a method that enables non-802.1X-capable devices to gain network access based on their MAC addresses. In this overview, you will explore how MAB can be used when 802.1X is not supported. You will also identify MAB's benefits and limitations, as well as how the MAB process operates to ensure secure and manageable network access.

  ------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

MAB Benefits and Limitations

MAB offers a method for network access control with notable Benefits and Limitations.

MAB is an authentication mechanism that allows non-supplicant devices to be authenticated based on MAC addresses to gain access to the network. It is typically implemented when more secure methods like 802.1X (which uses user credentials or certificates) aren\'t supported.

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image5.bin){width="6.940277777777778in" height="3.6175404636920385in"}

**Benefits**

MAB offers the following network access control benefits:

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Benefits                                Description
  --------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Fallback or Standalone Authentication   MAB can be deployed as a fallback, or complementary, mechanism to IEEE 802.1X. If the network does not have any IEEE 802.1X-capable devices, MAB can be deployed as a standalone authentication mechanism.

  Device Authentication                   MAB is used to authenticate devices that are not capable of IEEE 802.1X or that do not have a user such as printers, cameras, and Internet of Things (IoT) devices.

  Visibility                              MAB enhances network visibility by linking a device's IP address, MAC address, switch, and port, which aids in security audits, forensics, usage statistics, and troubleshooting.

  Identity-Based Services                 MAB allows dynamic delivery of customized services, such as VLAN assignment or unique access lists, based on an endpoint's MAC address. All dynamic authorization methods available with IEEE 802.1X also apply to MAB.

  Access Control                          MAB acts at Layer ~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation], allowing you to control network access at the access edge for guest (temporary devices), where certificates or usernames aren\'t practical.
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Limitations**

MAB has the following limitations that you must consider before you decide to implement:

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Limitation                          Description
  ----------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Requires MAC database               MAB requires a pre-existing, up-to-date database of allowed device MAC addresses, and maintaining this database is a key deployment challenge.

  Delay                               When MAB is used as a fallback to IEEE 802.1X, it waits for 802.1X to time out before proceeding, resulting in a delay with no network access that can affect devices and user experience. A mitigation technique is needed to minimize this delay.

  No user authentication              MAB can be used to authenticate only devices, not users. Different users logged into the same device have the same network access.

  Strength of authentication          Unlike IEEE 802.1X, MAB is not a strong authentication method. MAB can be defeated by spoofing the MAC address of a valid device.
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. Which operational challenge must be addressed when deploying MAB as a network access control method?

A. Maintaining an up-to-date database of authorized MAC addresses

B. Ensuring all devices support certificate-based authentication

C. Providing per-user authentication on every connected device

D. Encrypting all network traffic at Layer ~~3~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]

MAB Operation

Understanding MAB Operation helps ensure that non-802.1X capable devices can still be authenticated and managed securely within a network that enforces port-based access control.

As illustrated in the following figure, before MAB authentication, the identity of the endpoint is unknown and all traffic is blocked.

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image6.bin){width="6.940277777777778in" height="3.1231244531933506in"}

The switch examines the first client packet to learn and authenticate the source MAC address. If 802.1X is the primary means of authentication, packets that are sent before the port has fallen back to MAB (during the IEEE 802.1X timeout phase) are discarded immediately. They cannot be used to learn the MAC address. The switch can use almost any Layer 2 and Layer ~~3~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] packets to learn MAC addresses. The exception is bridging frames, such as Cisco Discovery Protocol, Link Layer Discovery Protocol (LLDP), Spanning Tree Protocol (STP), and Dynamic Trunking Protocol (DTP).

After MAB authentication succeeds, the identity of the endpoint is known and all traffic from that endpoint is then allowed. For example, the switch will begin forwarding a printer's protocols such as IPP (Internet Printing Protocol) or LPR (Line Printer Remote). In essence, the switch performs source MAC address filtering to help ensure that only the MAB-authenticated endpoint is allowed to send traffic.

There are four phases of the MAB process. The following figure illustrates the flow of the MAB process when MAB is configured as a fallback mechanism to 802.1X.

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image7.bin){width="6.940277777777778in" height="3.118205380577428in"}

+------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Phase                              | Task                                                                                                                                                                                                                         |
+====================================+==============================================================================================================================================================================================================================+
| 1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Initiation                     | -   Upon detecting link-up on a port, the switch sends an ~~EAP~~ **Extensible Authentication Protocol (EAP)** [Explanation: Acronym 'EAP' not expanded on first use. Category: Acronyms] Request-Identity message to the endpoint to ~~initiate~~ **start** [Explanation: 'start' or 'begin' instead of 'initiate'. Category: Cisco Style Guide] authentication~~.                                                                                           ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]|
|                                    |                                                                                                                                                                                                                              |
|                                    | -   If there is no response, the switch retransmits the request at set intervals, up to a maximum number of retries~~.                                                                                                         ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]|
|                                    |                                                                                                                                                                                                                              |
|                                    | -   If no response is received after all retries, IEEE 802.1X times out and the switch proceeds to MAB (MAC Authentication Bypass), if configured~~.                                                                           ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]|
+------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]MAC Address Learning           | -   After learning the source MAC address from the first packet, the switch discards the packet and sends a RADIUS Access-Request using PAP by default~~.                                                                      ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]|
|                                    |                                                                                                                                                                                                                              |
|                                    | -   The MAC address is included in three attributes: Username (Attribute ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]), Password (Attribute ~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]), and Calling-Station-Id (Attribute 31), each with a different format~~.                                                    ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]|
|                                    |                                                                                                                                                                                                                              |
|                                    | -   Different RADIUS servers may validate the MAC address using different attributes, so it\'s important to ensure the server can distinguish MAB requests from other authentication types~~.                                  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]|
|                                    |                                                                                                                                                                                                                              |
|                                    | -   Cisco switches set Attribute ~~6~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] (Service-Type) to 10 (Call-Check) for MAB, allowing RADIUS servers to filter and identify MAB requests~~.                                                                                   ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]|
+------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 3~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Session Authorization          | -   If the MAC address is valid, the RADIUS server sends an Access-Accept message, granting port access and optionally applying dynamic policies like VLANs or dACLs; no further authentication methods are attempted~~.       ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]|
|                                    |                                                                                                                                                                                                                              |
|                                    | -   If the MAC address is invalid, the RADIUS server sends an Access-Reject message, and the switch may try alternative methods such as IEEE 802.1X, web authentication, or deploy a guest VLAN, depending on configuration. |
|                                    |                                                                                                                                                                                                                              |
|                                    | -   If no fallback methods are configured, the switch stops the authentication process and keeps the port unauthorized~~.                                                                                                      ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]|
|                                    |                                                                                                                                                                                                                              |
|                                    | -   The authentication timer restart feature can make the switch retry MAB for unknown MAC addresses, but Cisco recommends leaving this feature disabled to avoid unnecessary control-plane traffic~~.                         ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]|
|                                    |                                                                                                                                                                                                                              |
|                                    | -   Cisco generally recommends that you leave the authentication timer restart disabled~~.                                                                                                                                     ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]|
+------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 4~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Accounting                     | -   If the switch successfully applies the authorization policy, it sends a RADIUS Accounting-Request message to the RADIUS server with session details~~.                                                                     ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]|
+------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| 1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]If 802.1X is not enabled, the process is the same, except that MAB starts immediately after link-up, instead of waiting for IEEE 802.1X to time out. |
+==========================================================================================================================================================+
+----------------------------------------------------------------------------------------------------------------------------------------------------------+

~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. Which of the following is considered a limitation of a MAB implementation?

A. Visibility

B. Identity-Based Services

C. Strength of authentication

D. Access Control at the Edge

~~3~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. Which scenario best demonstrates a primary benefit of implementing MAB in a network environment?

A. Authenticating devices that lack IEEE 802.1X support, such as printers or cameras

B. Preventing IP address spoofing at the network edge

C. Enabling user-specific access controls based on login credentials

D. Encrypting network traffic for all connected endpoints

~~4~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. During the MAC Authentication Bypass (MAB) process on a switch configured with 802.1X, which attribute is uniquely set to identify a MAB Access-Request message to the RADIUS server?

A. Attribute ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] (Username)

B. Attribute ~~6~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] (Service-Type)

C. Attribute 31 (Calling-Station-Id)

D. Attribute ~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] (Password)

MAC Authentication Bypass (MAB) Configuration and Verification

During your preparations to implement MAB you have identified many devices on your network that do not support 802.1X authentication. These devices, such as printers, cameras, IP phones, scanners, and other devices, will need to be authenticated using their MAC addresses.

The following figure illustrates the various components that make up a MAB solution:

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image8.bin){width="6.940277777777778in" height="2.4856747594050743in"}

Several items should be considered before deploying MAB. These items include:

-   Determining~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]devices you want to authenticate via MAB, (~~e.g. ~~ **for example, ** [Explanation: 'for example' instead of 'e.g.'. Category: Cisco Style Guide]printers, IP cameras, mobile devices).

-   Identifying the network access devices that need to be configured (~~e.g. ~~ **for example, ** [Explanation: 'for example' instead of 'e.g.'. Category: Cisco Style Guide]Cisco Catalyst switch, Cisco Catalyst Wireless Controller).

-   Determine whether MAB will be configured as a primary or back means of authentication.

-   Determining~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]Authentication, Authorization, and Accounting (AAA) server to use (~~e.g. ~~ **for example, ** [Explanation: 'for example' instead of 'e.g.'. Category: Cisco Style Guide]Cisco Identity Services Engine \[ISE\]), and whether it will host the MAC database of client devices.

-   Determining how to store an external database of collected MAC addresses, (~~e.g. ~~ **for example, ** [Explanation: 'for example' instead of 'e.g.'. Category: Cisco Style Guide]Lightweight Directory Access Protocol \[LDAP\] and Active Directory).

-   If the switchports might connect to IP phones, which might have computers connected to them, has the host mode been identified as part of the 802.1X configuration? (single host, multidomain authentication, multi-authentication host, or multihost)

  ------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][http://schemas.openxmlformats.org/drawingml/2006/picture](media/image3.bin){width="0.9741929133858268in" height="0.9741929133858268in"}   This training explains how to configure MAB for devices that can\'t use 802.1X. It explores planning considerations, MAC address collection and storage, and detailed steps to set up MAB on Cisco switches and wireless controllers using RADIUS servers for authentication.

  ------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

MAB Planning and Considerations

MAB requires that device MAC addresses be collected and stored in a database.

**MAC Collection**

There are several ways to collect MAC addresses to populate your MAC address database. The easiest and most economical method is to find pre-existing inventories of MAC addresses.

  ---------------------------------------------------------------------------------------------------------------------
  **For example:**\
  In some companies, the purchasing department keeps rigorous records of the MAC addresses of every purchased device.

  ---------------------------------------------------------------------------------------------------------------------

Another good source for MAC addresses is any existing application that uses a MAC address in some way.

  --------------------------------------------------------------------------------------------------------------------
  **For example:**\
  Cisco Unified Communication Manager keeps a list of the MAC addresses of every registered IP phone on the network.

  --------------------------------------------------------------------------------------------------------------------

If also implementing 802.1X with Cisco ISE as the RADIUS server, use a phased deployment. The Monitor and Low-Impact phases allow Cisco ISE to identify MAC addresses that do not perform 802.1X. If profiling is enabled in Cisco ISE, this will also automatically map endpoint profiles to MAC addresses, reducing the amount of work that is required to build the endpoint database.

**MAC Storage**

After you have collected the allowed MAC addresses that you wish to authenticate via MAB, you must store them in a database. The RADIUS server must access this database during the MAB attempt. As shown in the following figure, there are several factors to consider when storing your device MACs.

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image9.bin){width="6.940277777777778in" height="1.5164260717410323in"}

Options for storing the device MAC addresses used for MAB authentication include:

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Database                          Description
  --------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  RADIUS Server Internal Database   With some RADIUS servers, you simply enter the MAC addresses in the local user database, setting both the username and password to the MAC address. (~~e.g. ~~ **for example, ** [Explanation: 'for example' instead of 'e.g.'. Category: Cisco Style Guide]Cisco ISE stores MAC addresses in an endpoint database.)

  LDAP Database                     After you have collected MAC addresses, you can import them to the LDAP server and then configure your RADIUS server to query that server.

  Microsoft Active Directory        Microsoft Active Directory is a widely deployed directory service for users. To simplify MAC address storage, Microsoft Active Directory provides a special object class for MAC addresses that is called "ieee802Device".
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. Which of the following sources can be used to collect MAC addresses when building a database for MAB (MAC Authentication Bypass)?

A. Cisco Unified Communication Manager lists

B. Guest wireless network logs

C. Endpoint antivirus software reports

D. Website browsing history

Cisco Catalyst Switch MAB Configuration

The following figure illustrates the key steps in configuring MAB on a Cisco Catalyst switch:

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image10.bin){width="6.94027668416448in" height="1.8756485126859144in"}

**Enable AAA**

This step enables the AAA feature set and instructs the switch to use a specific RADIUS server to perform the authentication, authorization, and accounting functions. This step may have been completed as part of 802.1X implementation.

Configuration:

aaa new-model\
aaa authentication dot1x default group radius\
aaa authorization network default group radius\
aaa accounting dot1x default start-stop group radius\
radius-server host 10.1.1.1 key Cisco123

**Enable 802.1X Globally**

Configuration:

dot1x system-auth-control

While the **aaa accounting dot1x default start-stop group radius** command identifies 802.1X, it is used for both 802.1X and MAB.

**Enable 802.1X and MAB on Interface**

This step enables port authentication, determines the order of authentication methods attempted, enables MAB, and configures the switch port to be an 802.1X Authenticator.

In the interface configuration on the access switch, there are two ways in~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]you can configure MAB:

-   **Standalone**: Supports MAB authentication only, typically used with ports being used by non-supplicant devices.

-   **Fallback**: Attempts 802.1X and when it fails or a timeout occurs, uses MAB authentication. To easily enable this behavior, Cisco's Flexible Authentication (FlexAuth) allows network administrators to set an authentication order and priority on switch ports. Ports attempt 802.1X, MAB, and WebAuth in a configured order. This single configuration simplifies operational models for customers compared to traditional 802.1X deployments.

Configuration (MAB Fallback):

interface FastEthernet0/1\
authentication port-control auto\
authentication host-mode multi-auth\
authentication order dot1x mab\
authentication priority dot1x mab\
**mab**

While most of this configuration might have been performed during 802.1X authentication configuration, the **mab** command is required for the switch to perform MAB.

**Verifying Switch MAB Configuration and Operation**

Verifying MAB operation for Catalyst switches using Cisco Identity-Based Network Security 2.0 (IBNS 2.0) is performed with the show **access session** command.

An example of that output includes:

Switch#**show access session interface Gi ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]/0/3**\
Interface MAC Address Method Domain Status FQ Session ID\
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]\
Gi1/0/3 0050.568e.5602 mab DATA Auth A0A0A03000000875FB5DC72

Authentication, as well as authentication failure and reasoning, can also be found in the RADIUS server logs. In Cisco ISE these are located in the RADIUS live logs.

Cisco Catalyst Wireless Controller MAB Configuration

The following figure illustrates the key steps in configuring MAB on a Cisco Catalyst Wireless Controller:

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image11.bin){width="6.940277777777778in" height="1.7218525809273841in"}

**Enable RADIUS Server for Authentication**

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Navigate to **Configuration** \> **Security** \> **RADIUS**.

2~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]~~Click Add~~ **Add bold formatting to the button/menu name (e.g., 'click **Save**')** [Explanation: GUI elements after 'click' should be bold. Category: Cisco Style Guide] to add a RADIUS server.

3~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Enter the following:

-   IP address

-   Shared secret

-   Authentication port (usually 1812)

-   Accounting port (usually 1813)

The following figure shows the AAA server configuration:

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image12.bin){width="6.940277777777778in" height="2.941917104111986in"}

**Configure WLAN Profile to Use MAB**

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Navigate to **WLANs Security** \> **Tags~~ & ~~ **Change '&' to 'and'** [Explanation: 'and' instead of '&' in prose text. Category: Grammar & Punctuation]Profiles** \> **WLANs**.

2~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Select the WLAN that you want to configure MAB for.

3~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Under **Security** \> **Layer ~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]**:

-   Enable MAC Filtering.

-   (Optional) Disable 802.1X if you're using MAB only.

The following figure shows selecting MAC Filtering for a WLAN:

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image13.bin){width="6.940277777777778in" height="2.424675196850394in"}

**Enable AAA override and set Client Exclusion**

Navigate to **Configuration** \> **Tags~~ & ~~ **Change '&' to 'and'** [Explanation: 'and' instead of '&' in prose text. Category: Grammar & Punctuation]Profiles** \> **Policy**:

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Click on your policy in the list.

2~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]In the **Advanced** tab for your policy, locate the **AAA Policy** section.

3~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Click the box for **Allow AAA override**.

4~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Set Client Exclusion as needed.

The following figure shows the policy that is configured with AAA override enabled and Client exclusion set:

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image14.bin){width="6.94027668416448in" height="4.715569772528434in"}

**Verifying Switch MAB Configuration and Operation**

The easiest way to verify wireless MAB authentication, and authentication failure and reasoning, is the RADIUS server logs. In Cisco ISE these are located in the RADIUS live logs.

~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. What is the significance of the \"ieee802Device\" object class in Microsoft Active Directory when storing MAC addresses?

A. It enables IP address-to-MAC binding for ~~DHCP~~ **Dynamic Host Configuration Protocol (DHCP)** [Explanation: Acronym 'DHCP' not expanded on first use. Category: Acronyms]

B. It allows direct mapping of MAC addresses to RADIUS profiles

C. It provides a standardized schema to store MAC addresses

D. It enforces 802.1X policy enforcement on all Active Directory users

~~3~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. When storing MAC addresses for MAB authentication, what is a key feature of using Microsoft Active Directory?

A. It uses a dedicated object class called \"ieee802Device\" for MAC addresses

B. It stores MAC addresses only as usernames and passwords

C. It encrypts MAC addresses in endpoint databases by default

D. It restricts MAC address storage to wireless devices only

~~4~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. When configuring a WLAN profile for MAC Authentication Bypass (MAB) only, which Layer ~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] security setting should be applied?

A. Enable 802.1X and MAC Filtering simultaneously

B. Enable WPA2-Enterprise and 802.1X

C. Enable WPA2-Personal with a pre-shared key

D. Enable MAC Filtering and disable 802.1

Cisco Central Web Authentication for Guest Users

During your MAB implementation, you discover that some user devices do not support 802.1X authentication but require user verification to connect to the network. These devices include laptops and mobile devices, typically used by guests visiting your network. You have found that guest users pose a unique challenge:

-   When a guest device that does not support 802.1X connects to a port configured for IEEE 802.1X control, simply assigning the client to a guest VLAN can introduce security risks.

-   Guest devices' MAC addresses are unknown and cannot be maintained in a database, making MAB an unsuitable option.

Due to the limitations of providing guest access with 802.1X or MAB solutions, your organization has decided to implement web authentication.

Web authentication allows users to authenticate via HTTP(S) without requiring an 802.1X supplicant or MAC address that is defined in an endpoint database. As illustrated in the following figure, when web authentication is implemented:

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image15.bin){width="6.94027668416448in" height="1.988844050743657in"}

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Browser traffic from the client is intercepted by the network access device (NAD) and the user is redirected to a login page on the Cisco ISE web portal.

2~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]After successful authentication, appropriate network access is provided.

  ------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][http://schemas.openxmlformats.org/drawingml/2006/picture](media/image3.bin){width="0.9741929133858268in" height="0.9741929133858268in"}   This training introduces web authentication as a solution for providing guest access and a fallback when 802.1X authentication fails. It focuses on the Central Web Authentication (CWA) method, exploring the CWA process and how to configure it on Cisco Catalyst switches and wireless controllers.

  ------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Web Authentication Use Cases

The two key use cases for web authentication are guest access and a fallback for 802.1X.

Web authentication provides a means to provide access to endpoints that do not have an 802.1X supplicant or lack local credentials to authenticate to the network.

The following figure shows the basic functionality of Web Authentication using Cisco ISE as the authentication server:

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image16.bin){width="6.94027668416448in" height="3.035903324584427in"}

Web authentication is typically used to provide guest access to a network via HTTP or HTTPS. However, it can also serve as a fallback method for endpoint authentication. For example, when an 802.1X supplicant is not installed, misconfigured, or nonfunctional, web authentication can act as a last resort. In such cases, it can prompt the user for credentials through a web portal and still allow network access. Web authentication may also be used for guest users who have an 802.1X supplicant but lack a user account in the appropriate identity database.

Web Authentication Methods

Cisco offers two web authentication methods that support various wired and wireless scenarios, with trade-offs in scalability, control, and user experience.

**Central Web Authentication (CWA)**

CWA involves redirection by the network device, such as a switch or wireless controller, to a centralized Cisco ISE web portal for user authentication. All authentication and guest access control are centrally managed within ISE, allowing for advanced features such as flexible policy enforcement, device profiling, and post-authentication redirection. This method is commonly employed in enterprise environments to support robust and scalable guest access solutions.

**Local Web Authentication (LWA)**

LWA offers a simpler configuration, making it particularly suitable for small to medium-sized networks. It provides basic guest access capabilities, with the authentication web portal hosted directly on the network device, such as a wireless LAN controller.

The disadvantages of LWA include no support for Change of Authorization (CoA), and no information will be logged in the centralized audit trail. Because of these disadvantages, LWA is only used in rare situations where CWA is not viable.

The typical LWA authentication flow is as follows:

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]The user associates to the Web Auth SSID.

2~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]The user opens a browser.

3~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]The WLC redirects the user to the guest portal hosted on the WLC itself (not on external systems like ISE or NGS).

4~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]The user authenticates this portal.

5~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]The portal redirects back to the WLC with the entered credentials.

6~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]The WLC authenticates the user via RADIUS.

7~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]The WLC then redirects the user to the originally requested URL.

CWA Process

The CWA process uses browser-based redirection and identity-based policy enforcement to authenticate users connecting through wired or wireless endpoints.

When wired or wireless guest users first connect to the network, they have limited access. You can define this access through the VLAN or an ~~ACL~~ **access control list (ACL)** [Explanation: Acronym 'ACL' not expanded on first use. Category: Acronyms] configuration on the WLC, or through a dACL on a switch. At this initial stage, the authorization assignment permits only web authentication traffic. Other traffic is redirected to the web authentication service running on Cisco ISE.

The following diagram illustrates the process of a client being authenticated using the CWA method:

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image17.bin){width="6.940277777777778in" height="3.0937674978127734in"}

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]The client connects to the NAD through a wired or wireless connection. The client may or may not have an 802.1X supplicant.

2~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Once 802.1X times out, the NAD ~~initiates~~ **starts** [Explanation: 'start' or 'begin' instead of 'initiate'. Category: Cisco Style Guide] a MAB request for an endpoint without a supplicant or a regular access request for an endpoint with a supplicant. The request is made to a Cisco ISE server that is configured as a RADIUS server on the NAD.

3~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]The Cisco ISE processes the request and does not find an endpoint or user. The appropriate authorization rule is configured with a restricted network profile, which contains URL-redirection parameters.

4~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Cisco ISE sends an Access-Accept message with URL redirection for CWA to NAD. The redirection is to the CWA service running on the Cisco ISE.

5~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]The client ~~initiates~~ **starts** [Explanation: 'start' or 'begin' instead of 'initiate'. Category: Cisco Style Guide] an HTTP or HTTPS request to any URL using a browser, Domain Name System (DNS) resolution is required.

6~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]The NAD sends an HTTP or HTTPS redirect message to the client. The redirection is to the URL and is included in the Access-Accept message. This URL is for the Guest portal login page on the Cisco ISE.

7~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Client browser sends redirected traffic to the Cisco ISE.

8~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]The guest service displays the authentication portal, prompts for the username and password, and authenticates the user against the configured identity store or stores.

9~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Upon successful authentication, Cisco ISE sends the authorization profile that is associated with the authenticated user in the form of a CoA request to the NAD.

10. The NAD applies the new authorization settings and sends a new MAB request to the Cisco ISE, using the same session ID from the previous request.

11. The NAD applies the received new authorization settings and returns a CoA acknowledgment back to the Cisco ISE.

~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. What is a key limitation of LWA when compared to CWA in Cisco environments?

A. LWA does not support CoA and does not log information in a centralized audit trail

B. LWA offers more comprehensive guest access control than CWA

C. LWA enables advanced device profiling and post-authentication redirection

D. LWA uses Cisco ISE exclusively for all authentication requests

CWA Configuration on a Cisco Catalyst Switch

To enable CWA on the Cisco Catalyst switch, you must configure AAA, the appropriate authentication methods, and the web redirection.

The following figure illustrates the key steps in configuring CWA on a Cisco Catalyst switch:

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image18.bin){width="6.94027668416448in" height="1.8794225721784776in"}

In a typical network access implementation, web authentication is used with 802.1X and MAB. Once an endpoint connects to the switch, the web authentication process is performed after 802.1X, and MAB fails. Therefore, the switch needs to be configured with AAA, RADIUS, and global 802.1X settings. Also, ensure that CoA is configured for dynamic VLAN assignment and all necessary interfaces have the appropriate interface-specific 802.1X and MAB settings.

To complete CWA support on a Cisco Catalyst switch, perform the following tasks:

-   **Enable HTTP(S) Servers:** Enables the switch to perform intercept of incoming HTTP and HTTPS requests and perform redirection to a guest portal running on Cisco ISE.

-   **Configure Redirect ACL:** Specifies~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]traffic will be redirected to Cisco ISE. You need to deny traffic that should not be redirected, and permit traffic that should be redirected. The redirect ACL does not redirect DNS, DHCP, and traffic to Cisco ISE.

CWA Configuration on a Cisco Catalyst Wireless Controller

To enable CWA on the Cisco Catalyst Wireless Controller, you must configure AAA, the appropriate WLANs, and the web redirection.

The following figure illustrates the key steps in configuring CWA on a Cisco Catalyst Wireless Controller:

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image19.bin){width="6.940277777777778in" height="1.7445089676290464in"}

**Configure AAA, WLANs, and Policy Mapping**

This step consists of the following tasks:

-   AAA RADIUS configuration

```{=html}
<!-- -->
```
-   Add the AAA Server.

-   Ensure support for CoA is enabled.

-   Create an authorization method list.

```{=html}
<!-- -->
```
-   WLAN configuration

```{=html}
<!-- -->
```
-   Create the WLAN.

-   Select the needed security method.

```{=html}
<!-- -->
```
-   Policy Mapping

```{=html}
<!-- -->
```
-   Create a policy profile to assign clients to VLANs, and set up ACLs, Quality of Service (QoS), Mobility Anchor, and timers. Configure the policy profile to allow AAA override and CoA. You can optionally specify an accounting method too.

-   Link your WLAN to the ~~desired~~ **wanted** [Explanation: 'want' or 'wanted' instead of 'desire/desired'. Category: Cisco Style Guide] policy profile.

-   Assign the policy tag to the needed Access Points (APs).

**Enable HTTP(S) Servers**

-   To enable client HTTP traffic to be redirected to Cisco ISE, you can either choose to:

```{=html}
<!-- -->
```
-   Enable it globally from the WLC CLI with the ip http server command.

-   Enable it for the web authentication module only from the WLC CLI with the webauth-http-enable command under the parameter map.

```{=html}
<!-- -->
```
-   To enable client HTTPS traffic to be redirected to Cisco ISE, use the WLC GUI to enable the option "Web Auth intercept HTTPS" (**Configuration** \> **Security** \> **Web Auth**). Enabling client HTTPS traffic to be redirected for authentication purposes is not recommended as the configuration will increase CPU usage and generate certificate errors.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]The redirection of HTTP traffic happens inside Control and Provisioning of Wireless Access Points (CAPWAP), even in case of FlexConnect Local Switching. Since it is the WLC doing the interception work, the AP sends the HTTP(S) packets inside the CAPWAP tunnel and receives the redirection from the WLC back in CAPWAP. |
+===================================================================================================================================================================================================================================================================================================================================+
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Configure Redirect ACL**

-   The redirect ACL defines~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]traffic is sent to the CPU (via permit statements) for further processing such as redirection. The redirect ACL also defines~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]traffic remains in the data plane (via deny statements) and bypasses redirection. Denied traffic is not dropped, only excluded from redirection. Consider the following when creating your redirect ACL:

```{=html}
<!-- -->
```
-   Deny traffic to your ISE nodes, as well as DNS and DHCP servers, while permitting all other traffic.

-   It is better to restrict to port 8443, which is typically the port that is used by the guest portal (although in some specific cases, other ports can be involved).

~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. In the CWA process, what is the purpose of the redirect ACL on a switch or wireless controller?

A. To filter out malicious HTTP/HTTPS traffic

B. To drop all unauthorized DNS and DHCP traffic

C. To determine~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]client traffic should be sent to Cisco ISE

D. To assign VLANs for authenticated users

~~3~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. Which configuration step is required to ensure that a Cisco Catalyst Wireless Controller can successfully redirect HTTP traffic from wireless clients to Cisco ISE for CWA?

A. Enable HTTP server globally using the ip http server command on the WLC

B. Assign a unique SSID to each WLAN used for guest access

C. Set up WPA2-Enterprise as the only security method on the WLAN

D. Configure a static IP address for each wireless client

~~4~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. In the context of configuring a redirect ACL for CWA on a Cisco Catalyst Wireless Controller, which type of traffic should typically be denied preventing unnecessary redirection?

A. All traffic destined for external web servers

B. All wireless client-to-client traffic

C. All traffic on ports above 1024

D. Traffic to ISE nodes, DNS, and DHCP servers

Discovery 1: MAC Authentication Bypass on Cisco Network Devices

Introduction

Imagine that you are part of a network security team in charge of securing wired access across a distributed enterprise network. You have been tasked with configuring your access layer switches to integrate with Cisco ISE to enforce identity-based access control. While IEEE 802.1X is the preferred method for authenticating endpoints, many devices, such as IP phones, printers, and certain access points, do not support 802.1X. To accommodate these devices without compromising security, you plan to use MAB as a fallback mechanism.

This lab steps you through the process of configuring and testing Cisco Catalyst switches to allow network access to devices that do not support 802.1X supplicants. You will implement MAB and verify dynamic policy enforcement to deploy a secure, enterprise-grade access control solution.

During the lab, you will perform the following key activities:

-   Examine the switch's AAA and RADIUS configuration to confirm it is ready for Cisco ISE integration and identity-based access control.

-   Enable MAB and enforce dynamic policies using policy maps on a specific port to support non-802.1X devices.

-   Analyze session details to confirm proper authentication via MAB, examining how fallback from 802.1X to MAB occurs.

-   Use CLI outputs to observe real-time changes in authentication states and identify the exact policy behavior.

Topology

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image20.bin){width="6.940277777777778in" height="3.1687150043744534in"}

Job Aid

**Usernames and Passwords**

  -------------------------------------------------------------------------------------------------------------------------------------------------------
  Name               Description                       Hostname (FQDN)          IP Address                             Username                Password
  ------------------ --------------------------------- ------------------------ -------------------------------------- ----------------------- ----------
  Admin-PC           Admin PC                          n/a                      10.10.10.10                            admin                   1234QWer

  Client-PC          Client PC                         n/a                      wired 10.10.30.x wireless 10.10.40.x   Student\                1234QWer
                                                                                                                       (student-PC\\Student)   

  Active Directory   Microsoft Certificate Authority   ad.abc.public/certsrv/   10.10.4.20                             administrator           1234QWer

  WLC                Cisco WLC                         n/a                      10.10.10.50                            admin                   1234QWer
  -------------------------------------------------------------------------------------------------------------------------------------------------------

Task 1: Validate the Existing Switch AAA Configuration

In this task, you will inspect and verify the switch's existing AAA configuration and test user authentication via CLI using RADIUS. These steps will reinforce your understanding of AAA functionality, particularly in how Cisco ISE policies are applied ~~to securely control~~ **Consider moving the adverb (e.g., 'to quickly configure' → 'to configure quickly')** [Explanation: avoiding split infinitives when possible. Category: Grammar & Punctuation] network access.

Activity

**Step ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** From the Admin-PC, open Putty and start a terminal session to access your C3560-CX access switch using the credentials username: **admin**, and password: **1234QWer**.

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image21.bin){width="2.65161198600175in" height="2.948386920384952in"}

**Step ~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** Examine the current AAA configuration on the switch by using the **show run \| sec aaa** command.

show run \| sec aaa

sise-PG05-P02#sh run \| sec aaa\
aaa new-model\
aaa group server radius ise-pac\
server name ISE-1\
aaa authentication login login-none none\
aaa authentication enable default none\
aaa authentication dot1x default group ise-pac\
aaa authorization network default group ise-pac\
aaa authorization auth-proxy default group ise-pac\
aaa accounting update newinfo periodic ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\
aaa accounting identity default start-stop group ise-pac\
aaa server radius dynamic-author\
client 10.10.10.30 server-key 1234QWer\
auth-type any\
aaa session-id common\
match result-type aaa-timeout\
match result-type aaa-timeout

This current AAA configuration defines authentication, authorization (including web-based auth-proxy), and accounting policies for network access control. It enables 802.1X authentication to use a RADIUS server group named **ise-pac**, a Cisco ISE device, and ensures that session records are consistently identified using a common session ID. Additionally, the match result-type configuration includes logic to detect and match AAA timeout conditions, which can be used ~~to apply fallback~~ **Consider moving the adverb (e.g., 'to quickly configure' → 'to configure quickly')** [Explanation: avoiding split infinitives when possible. Category: Grammar & Punctuation] policies when the RADIUS server is unresponsive.

**Step ~~3~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** From privileged exec mode, perform a CLI AAA authentication test for **employee1** with the following command:

test aaa group radius employee1@abc.public 1234QWer new-code

sise-PG05-P02#test aaa group radius employee1@abc.public 1234QWer new-code

**Step ~~4~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** Notice that the user is authenticated, matching a policy on the AAA server that allows access.

sise-PG05-P02#test aaa group radius employee1@abc.public 1234QWer new-code\
User successfully authenticated\
\
USER ATTRIBUTES\
\
username 0 \"employee1@abc.public\"\
CiscoSecure-Defined- 0 \"#ACSACL#-IP-acl_employee-688be8f5\"

Task 2: Configure MAB on Switch Port

In this task, you will configure a switch port to support MAB for an access point and validate its integration with a RADIUS server. This exercise demonstrates how identity-based access control is enforced at the switch port level and how authentication policies influence device or user access to the network.

Activity

**Step ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** Examine the initial configuration on the switchport we are going ~~to apply MAB~~ **Consider moving the adverb (e.g., 'to quickly configure' → 'to configure quickly')** [Explanation: avoiding split infinitives when possible. Category: Grammar & Punctuation] configuration to, run the **show run interface GigabitEthernet 0/1** command.

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 3~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]There are two different hardware pools used in this lab set. The switches either use **GigabitEthernet 0/x** or **GigabitEthernet ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]/0/x** interface formatting so take note of~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]interfaces you have in your assigned lab environment.The lab pods use two different types of switches, which have different interface naming conventions. Depending on your assigned pod, your switch interfaces will be labeled either as GigabitEthernet 0/x or GigabitEthernet ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]/0/x. Please verify~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]interface format is used in your lab environment. |
+=========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

sise-PG05-P02#sh run int gigabitEthernet ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]/0/1\
Building configuration\...\
\
Current configuration : 237 bytes\
~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation]\
interface GigabitEthernet1/0/1\
description Access-Point\
switchport access vlan 50\
switchport mode access\
access-session host-mode single-host\
access-session closed\
spanning-tree portfast edge\
spanning-tree bpduguard enable\
end

**Step ~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** Configure the access point's switch port for MAB, on the C3560-CX access switch, enter the following commands from GigabitEthernet ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]/0/1 interface configuration mode:

mab\
\
access-session port-control auto\
\
dot1x pae authenticator\
\
service-policy type control subscriber POLICY_Gi1/0/1

interface GigabitEthernet1/0/1\
description Access-Point\
switchport access vlan 50\
switchport mode access\
access-session host-mode single-host\
access-session closed\
access-session port-control auto\
mab\
dot1x pae authenticator\
spanning-tree portfast edge\
spanning-tree bpduguard enable\
service-policy type control subscriber POLICY_Gi1/0/1

Notice that the port is set ~~to automatically transition~~ **Consider moving the adverb (e.g., 'to quickly configure' → 'to configure quickly')** [Explanation: avoiding split infinitives when possible. Category: Grammar & Punctuation] between authorized and unauthorized states based on authentication results. Additionally, a subscriber control policy (**POLICY_Gi1/0/1**) is applied to enforce dynamic network access policies such as VLAN assignment, ACLs, or QoS based on the identity of the connecting device or user.

Task 3: Verify the MAB Authentication

This task guides you through verifying your MAB configuration on the switch. You'll observe the access point's authentication state changes, reboot the AP to trigger reauthentication, and analyze the switch port's session details and policy configurations to understand how MAB is ~~initiated~~ **started** [Explanation: 'start' or 'begin' instead of 'initiate'. Category: Cisco Style Guide] and authorized.

Activity

**Step ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** From the C3560-CX access switch privileged exec mode, examine the AAA session information by entering the following command:

show access-session interface GigabitEthernet ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]/0/1

Notice the following:

-   The MAC address of the access point that the switch is trying to authenticate using MAB.

**Step ~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** The status of the session - **Unauth** (unauthorized). If the status of your session is not **Unauth**, enter the command **clear access-session interface GigabitEthernet ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]/0/1** to force the AP to start a new session.

sise-PG05-P02#sh access-session interface GigabitEthernet ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]/0/1\
\
Interface MAC Address Method Domain Status Fg Session ID\
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]\
Gi1/0/1 d478.9b49.5484 N/A UNKNOWN Unauth 0A0A0A030000001300484BC3

**Step ~~3~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** After a few minutes, examine the AAA session information again by entering the following command:

show access-session interface GigabitEthernet ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]/0/1

Notice the following changes to the access point's AAA session:

-   The authentication method is **MAB** and the **Status** should be **Auth**.

sise-PG05-P02#sh access-session interface GigabitEthernet ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]/0/1\
\
Interface MAC Address Method Domain Status Fg Session ID\
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]\
Gi1/0/1 d478.9b49.5484 mab DATA Auth 0A0A0A030000001300484BC3

**Step ~~4~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** To demonstrate an alternative way to verify the access point MAB authentication, start by rebooting the access point by entering the following commands from global configuration mode:

interface Gi0/1\
shut\
no shut\
end

**Step ~~5~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** After waiting a few minutes for the access point to complete its ~~boot up~~ **start** [Explanation: 'start' or 'boot' instead of 'boot up'. Category: Cisco Style Guide], examine the access session on the access point's switch port by entering the following command in privileged exec mode:

show access-session interface GigabitEthernet 0/1 details

**Step ~~6~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** Note that the state of the 802.1X authentication method is **Running**.

Why do you suppose this is currently the state of the session?

sise-PG05-P02#sh access-session interface GigabitEthernet ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]/0/1 details\
Interface: GigabitEthernet1/0/1\
MAC Address: d478.9b49.5484\
IPv6 Address: Unknown\
IPv4 Address: 10.10.50.100\
Status: Unauthorized\
Domain: UNKNOWN\
Oper host mode: single-host\
Oper control dir: both\
Session timeout: N/A\
Restart timeout: N/A\
Periodic Acct timeout: N/A\
Common Session ID: 0A0A0A0300000014005EF8FB\
Acct Session ID: Unknown\
Handle: 0x00000007\
Current Policy: POLICY_Gi1/0/1\
\
Method status list:\
Method State\
\
dot1x Running

The state of the access point's authentication session is **Running** because the service policy applied to the access point's switch port is configured to have the client first try to authenticate using 802.1X. The 802.1X will have to time out first based on the policy. This configuration can be verified by examining the **POLICY_Gi1/0/3** policy map.

**Step ~~7~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** After waiting a few more minutes verify a successful authentication on the access switch by entering the following command again:

show access-session interface GigabitEthernet 0/1 details

Note the following:

-   The state of the 802.1X authentication is now **Stopped**.

**Step ~~8~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** The state of the MAB authentication is **Authc Success** (Authenticated).

sise-PG05-P02#sh access-session interface GigabitEthernet ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]/0/1 details\
Interface: GigabitEthernet1/0/1\
MAC Address: d478.9b49.5484\
IPv6 Address: Unknown\
IPv4 Address: 10.10.50.100\
User-Name: D4-78-9B-49-54-84\
Status: Authorized\
Domain: DATA\
Oper host mode: single-host\
Oper control dir: both\
Session timeout: N/A\
Restart timeout: N/A\
Periodic Acct timeout: 60s (local), Remaining: 43s\
Common Session ID: 0A0A0A0300000014005EF8FB\
Acct Session ID: 0x00000008\
Handle: 0x00000007\
Current Policy: POLICY_Gi1/0/1\
\
Local Policies:\
Service Template: DEFAULT_LINKSEC_POLICY_SHOULD_SECURE (priority 150)\
Security Policy: Should Secure\
Security Status: Link Unsecure\
\
Server Policies:\
\
Method status list:\
Method State\
\
dot1x Stopped\
mab Authc Success

**Step ~~9~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** To verify the way authentication is configured on the access point's switch port, examine the interface configuration by entering the command **show run int g1/0/1**.

Which service policy is applied to the interface?

sise-PG05-P02#show run int g1/0/1\
Building configuration\...\
\
Current configuration : 356 bytes\
~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation]\
interface GigabitEthernet1/0/1\
description Access-Point\
switchport access vlan 50\
switchport mode access\
access-session host-mode single-host\
access-session closed\
access-session port-control auto\
mab\
dot1x pae authenticator\
spanning-tree portfast edge\
spanning-tree bpduguard enable\
service-policy type control subscriber POLICY_Gi1/0/1\
end

The service policy that is applied to the access point's switch port is defined in the policy map **POLICY_Gi1/0/1**.

**Step 10** To examine the service policy applied to the access point's switch port, display the policy map configuration by entering the command **show policy-map type control subscriber POLICY_Gi1/0/1**.

Which part of the policy map causes the MAB authentication process to begin?

sise-PG05-P02#show policy-map type control subscriber POLICY_Gi1/0/1\
POLICY_Gi1/0/1\
event session-started match-all\
10 class always do-until-failure\
10 authenticate using dot1x priority 10\
event authentication-failure match-first\
~~5~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] class DOT1X_FAILED do-until-failure\
10 terminate dot1x\
20 authenticate using mab priority 20\
**10 class DOT1X_NO_RESP do-until-failure\
10 terminate dot1x\
20 authenticate using mab priority 20**

Since the access point does not have an 802.1X supplicant configured, it will not respond to the EAPoL-Request messages from the switch. Therefore, the corresponding class, **DOT1X_NO_RESP**, determines that the switch terminates 802.1X and uses MAB to authenticate the system.

Summary

Now that you have explored the essentials of implementing MAB on Cisco Catalyst switches, you are prepared to extend reliable and scalable access control solutions beyond traditional 802.1X authentication. By integrating MAB, your network infrastructure can securely accommodate devices that are not 802.1X-capable, ensuring consistent policy enforcement and alignment with enterprise security standards.

  -------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------
  ~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][http://schemas.openxmlformats.org/drawingml/2006/picture](media/image22.bin){width="0.9741929133858268in" height="0.9741929133858268in"}   Consider the following questions as you apply these concepts within your organization:

  -------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------

-   How will you identify and manage non-802.1X-capable devices that require MAB authentication to maintain security and operational continuity?

-   What strategy will you use to build, store, and maintain a trusted MAC address database, and how will you integrate this with your RADIUS infrastructure?

-   How will you configure Flexible Authentication order and priorities to support environments with mixed device capabilities?

-   What steps will you take to mitigate inherent MAB limitations, such as susceptibility to MAC spoofing?

-   How will you validate MAB sessions on Cisco Catalyst switches and monitor authentication results?

-   What approaches will you use to streamline MAB deployment across large enterprise environments using templates and automation?

You are now equipped with the technical knowledge and operational best practices to deploy and manage secure MAB solutions alongside 802.1X authentication. These capabilities enable your team to extend Zero Trust principles to all devices on your network while maintaining visibility, control, and a strong security posture.

Summary Challenge

1\. What triggers a Cisco Catalyst switch to begin the MAB authentication process when configured as a fallback to 802.1X?

A. Timeout of the IEEE 802.1X authentication process

B. Receipt of a valid MAC address from the endpoint

C. Completion of successful 802.1X authentication

D. Initial port configuration during switch boot-up

~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. Which attribute value does a Cisco Catalyst switch use ~~to uniquely identify~~ **Consider moving the adverb (e.g., 'to quickly configure' → 'to configure quickly')** [Explanation: avoiding split infinitives when possible. Category: Grammar & Punctuation] a MAB request to a RADIUS server?

A. Attribute ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] (Username) set to \"MAB\"

B. D. Attribute ~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] (Password) set to \"MAC-BYPASS\"

C. Attribute 31 (Calling-Station-Id) cleared

D. Attribute ~~6~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] (Service-Type) set to 10 (Call-Check)

~~3~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. What is a key security limitation of MAB?

A. It authenticates only user credentials, not devices.

B. It can be bypassed easily by spoofing a MAC address.

C. It enforces authentication at Layer ~~3~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] instead of Layer 2.

D. It prevents fallback to other authentication methods.

~~4~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. Which Cisco Catalyst switch CLI command verifies whether a device was authenticated via MAB on a specific port?

A. **show authentication status**

B. **show access session**

C. **show running-config interface**

D. **show mab sessions**

~~5~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. When configuring a WLAN profile on a Cisco Catalyst Wireless Controller for MAB-only authentication, which Layer ~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] security settings are required?

A. Enable WPA2-Enterprise and 802.1X

B. Enable 802.1X and MAC Filtering simultaneously

C. Enable MAC Filtering and disable 802.1X

D. Enable WPA2-Personal with a pre-shared key

~~6~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. During the Central Web Authentication (CWA) process, when does the network access device typically ~~initiate~~ **start** [Explanation: 'start' or 'begin' instead of 'initiate'. Category: Cisco Style Guide] a MAB request for a client?

A. After 802.1X times out and no supplicant is present

B. When a client successfully authenticates with 802.1X

C. When DNS resolution for the guest portal fails

D. Before assigning an IP address to the client

~~7~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. Why should DNS traffic typically be excluded (denied) in a redirect ACL for Central Web Authentication (CWA)?

A. DNS traffic must be dropped before HTTP redirection occurs.

B. DNS servers should authenticate clients before the web portal.

C. DNS traffic consumes excessive resources if redirected.

D. DNS traffic is needed for clients to resolve URLs for the guest portal.

Answer Key

MAC Authentication Bypass (MAB) Overview

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]A

```{=html}
<!-- -->
```
1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]C

2~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]A

3~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]B

MAC Authentication Bypass (MAB) Configuration and Verification

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]A

```{=html}
<!-- -->
```
1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]C

2~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]A

3~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]D

Cisco Central Web Authentication for Guest Users

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]A

```{=html}
<!-- -->
```
1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]C

2~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]A

3~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]D

Summary Challenge

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]A

2~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]D

3~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]B

4~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]B

5~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]C

6~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]A

7~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]D


---

## Change Legend

| Markup | Meaning |
|--------|---------|
| ~~text~~ | Text to remove (strikethrough) |
| **text** | Text to add (bold) |
| [Explanation: ...] | Rationale for change |

*Generated by Course AI Editor on 2026-03-04 14:07*