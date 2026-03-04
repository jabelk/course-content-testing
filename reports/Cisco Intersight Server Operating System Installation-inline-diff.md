# Inline Editorial Review: Cisco Intersight Server Operating System Installation

**Instructions**: Search for `~~` to find deletions and `**` to find additions.
Copy this document into Word to see Track Changes formatting.

---

**Total Changes**: 191 (Auto-fix: 101, Review: 62, Questions: 28)

---

Cisco Intersight Server Operating System Installation

Introduction

Cisco Intersight introduces the ability to install vMedia-based operating systems on the managed servers in your data center. With this capability, you can perform an unattended operating system installation on one or more Cisco Unified Computing System (Cisco UCS) C-Series standalone servers and Cisco Intersight Managed Mode (IMM) servers (C-Series, B-Series, and X-Series) from your centralized data center through a simple process.

Cisco Intersight Operating System Installation

This topic describes how to install an operating system by using Cisco Intersight. It also describes three options that you can use to install an operating system.

Introduction to Operating System Installation Workflow

As the name of the server action implies, the Install operating system action installs an operating system on the target server. This capability is different than traditional tools from operating system vendors or utility software providers that lack an underlying knowledge of the specific hardware target. Cisco Intersight operating system installation streamlines the integration of vendor-specific drivers and tools into the operating system installation process.

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image1.bin){width="6.333333333333333in" height="3.5625in"}

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image2.bin){width="6.333333333333333in" height="3.5625in"}

Operating System Installation Types

Cisco Intersight currently supports an unattended operating system installation that is enabled by one of the following configuration sources:

-   **Cisco:** Use a Cisco-validated template to install the selected operating system version. Cisco Intersight lets you view the Cisco-provided configuration files based on the operating system image version that you select. You can see the content of the configuration files and the required and optional parameters for the selected operating system installation. The Cisco option is ideal for typical operating systems installations, but Cisco expands the list of supported operating systems continuously. Using the Cisco-validated template is simple because you are required to assign basic mandatory parameters such as IP settings, the hostname, and the password. You must modify the configuration file if you want to provide additional settings.

-   **Custom:** The administrator provides a configuration file containing an installation script or configuration (kickstart) file with the necessary placeholders for the parameters. A placeholder is a variable for a configurable entity. Cisco Intersight assigns the value that the administrator enters in the placeholders to the appropriate parameters.

-   **Embedded:** The configuration (kickstart) file is embedded in the operating system ISO image. The ISO image contains the necessary references to the kickstart file from the bootloader configuration to execute an unattended operating system installation. This option is suitable for an operating system image that includes a configuration file.

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image3.bin){width="6.333333333333333in" height="3.5625in"}

You will ~~initiate~~ **start** [Explanation: 'start' or 'begin' instead of 'initiate'. Category: Cisco Style Guide] the operating system installation wizard for any method by navigating to the target server on~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]you want to install the operating system. From the **Action** menu, choose **Install Operating System**.

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image4.bin){width="6.333333333333333in" height="3.5625in"}

Operating System Installation Types Use Cases

Each of these operating system installation type options has its use cases.

-   The **Cisco** option is the easiest method. Cisco has tested and validated the methods for each supported operating system to match best practices. The default installation workflow fits a typical installation, but if it does not exactly match your needs, you can modify the configuration. The configuration file supports scripting and complexity for almost any situation.

-   The **Custom** option ~~allows you to~~ **lets you** [Explanation: 'lets you' instead of 'allows you to'. Category: Cisco Style Guide] use your configuration file. Before people began using Cisco Intersight, they often had custom configuration files. The **Custom** option ~~allows you to~~ **lets you** [Explanation: 'lets you' instead of 'allows you to'. Category: Cisco Style Guide] use your custom configuration files. Users can also place variables in the configuration file so that the Cisco Intersight GUI will ask for the values of those variables (such as hostname and password).

-   In the **Embedded** option, you can use any ISO image that has a configuration file inside. From the Cisco Intersight perspective, the **Embedded** option is a server-side installation where Cisco Intersight only provides an ISO image to the server. Then the server boots and installs the ISO image by using the settings that are provided within the ISO image.

```{=html}
<!-- -->
```
-   The Embedded method can run any utility for booting the ISO image, but you must build a complete ISO image with an embedded configuration (kickstart) file.

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image5.bin){width="6.333333333333333in" height="3.5625in"}

~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. Which of the following types of servers can be a target for an operating system installation from Cisco Intersight? (Choose three.)

A. Cisco UCS B-Series in IMM mode

B. Cisco UCS C-Series in IMM mode

C. Cisco UCS HX-Series in standalone mode

D. Cisco UCS S-Series in IMM mode

E. Cisco UCS X-Series in IMM mode

F. Third-party server

Cisco Intersight Operating System Installation Requirements

This topic lists currently supported hardware for operating system installation features, information about supported target operating systems, and caveats to consider.

Supported Hardware

To use the operating system installation feature from Cisco Intersight, the type of target server on~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]an operating system is to be installed must be supported. Each management mode has specific supported servers for the operating system install feature.

Supported Hardware for the Operating System Install Feature

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------
  Standalone Mode                                                                 Servers in Cisco IMM Mode
  ------------------------------------------------------------------------------- -------------------------------------------------------------------------------
  C-Series Servers (M7): UCSC-C220-M7, UCSC-240-M7\                               B-Series (M5): UCSB-B200-M5, UCSB-B480-M5\
  C-Series Servers (M6): UCSC-C220-M6, UCSC-240-M6, UCSC-C245-M6, UCSC-C225-M6\   B-Series Servers (M6): UCSB-B200-M6\
  C-Series Servers (M5): UCSC-C220-M5, UCSC-240-M5, UCSC-C480-M5                  C-Series Servers (M5): UCSC-C220-M5, UCSC-240-M5, UCSC-C480-M5\
                                                                                  C-Series Servers (M6): UCSC-C220-M6, UCSC-240-M6, UCSC-C245-M6, UCSC-C225-M6\
                                                                                  C-Series Servers (M7): UCSC-C220-M7, UCSC-240-M7\
                                                                                  X-Series Servers (M6): UCSX-210C-M6\
                                                                                  X-Series Servers (M7): UCSX-210C-M7

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]The requirements for the minimum software version for Cisco IMC, SCU, BIOS, and the device connector may be different for the same type of server in other management modes. |
+==================================================================================================================================================================================+
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Supported Operating Systems

Cisco Intersight supports installation of the following versions of VMware vSphere ESXi, Red Hat Enterprise Linux (RHEL), CentOS, Windows Server, Hyper-V Server, SUSE Linux Enterprise, Citrix Hypervisor, and Ubuntu Server editions with and without the SCU. The Cisco Intersight operating system installation service supports installing an operating system on one or more managed servers.

The following tables show support information for target operating systems in each of the two management modes.

Supported Operating Systems for Installation from Cisco Intersight in Standalone Management Mode

  ---------------------------------------------------------------------------------------------------------
  Operating System        Cisco Template   Custom Template   Embedded (with SCU)   Embedded (without SCU)
  ----------------------- ---------------- ----------------- --------------------- ------------------------
  VMware vSphere ESXi     Yes              Yes               Yes                   Yes

  Windows                 Yes              Yes               Yes                   Yes

  Hyper-V                 Yes              Yes               Yes                   Yes

  RHEL                    Yes              Yes               Yes                   Yes

  CentOS                  Yes              Yes               Yes                   Yes

  Ubuntu Server           Yes              Yes               Yes                   Yes

  SUSE Enterprise Linux   Yes              Yes               No                    Yes
  ---------------------------------------------------------------------------------------------------------

Supported Operating Systems for Installation from Cisco Intersight in Cisco IMM Management Mode

  ---------------------------------------------------------------------------------------------------------
  Operating System        Cisco Template   Custom Template   Embedded (with SCU)   Embedded (without SCU)
  ----------------------- ---------------- ----------------- --------------------- ------------------------
  VMware vSphere ESXi     Yes              Yes               Yes                   Yes

  Windows                 Yes              Yes               Yes                   Yes

  RHEL                    Yes              Yes               Yes                   Yes

  CentOS                  Yes              Yes               Yes                   Yes

  Ubuntu Server           Yes              Yes               Yes                   Yes

  SUSE Enterprise Linux   Yes              Yes               No                    Yes
  ---------------------------------------------------------------------------------------------------------

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]The requirements for the minimum software version for Cisco IMC, SCU, BIOS, and the device connector may be different for the same type of server in other management modes. |
+==================================================================================================================================================================================+
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Limitations and Caveats

You must have an account administrator or server administrator role to use the **Install OS from Cisco Intersight** feature. In a read-only role, you can view one or more installed operating systems on the server.

Depending on the target operating system, additional limitations apply:

-   A product key is mandatory for Windows installations.

-   An answer file that is used in the Windows installations must not include the disk configuration section.

-   The network device is mandatory for SUSE Linux Enterprise Server (SLES) installations.

-   The Cisco template for a Windows operating system installation automatically configures the network interface LAN on Motherboard (LOM) Port 1. To use a different network interface, make the necessary changes to the network port in the answer file using a custom template installation.

-   You can only configure IPv4 addresses for Hyper-V hosts or servers.

-   Tracking the operating system install process for VMware vSphere ESXi requires the operating system image to include the **ucs-tools vib**, which is included in the Cisco Custom VMware vSphere ESXi images.

The following limitations apply to Cisco IMM servers:

-   Cisco IMM servers must be associated with a server profile with a Cisco Integrated Management Controller (IMC) and LAN policy. You can configure additional policies.

-   RHEL installations with Unified Extensible Firmware Interface (UEFI) Secure Boot are not supported on Cisco IMM servers.

-   Cisco IMM servers do not support hosting images on an HTTP share. Cisco IMM servers only support Network File Systems (NFS), Common Internet File Systems (CIFS), or HTTPS shares.

The following limitations apply to target devices:

-   Targets with the Internet Small Computer Systems Interface (iSCSI) and Non-Volatile Memory Express (NVMe) types are not supported.

-   The legacy boot mode installation does not support partitions greater than ~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] TIB. UEFI boot mode can be used for partitions greater than ~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] TIB.

~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. For~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]operating system Intersight installation is supported on servers in standalone mode, but not on servers in Cisco IMM mode?

A. CentOS

B. Hyper-V

C. RHEL

D. Ubuntu Server

E. Windows

Adding an Operating System Image

This topic describes how to add the operating system image to the Cisco Intersight software repository. It also provides configuration details for adding an image depending on the protocol that you choose for the share location.

Repository Locations

An administrator must add the operating system image before the installation. Before you install an operating system, you must add the operating system image source, the details of the file share location, and the protocol (CIFS/NFS/HTTP/HTTPS) to the software repository.

Cisco Intersight uses the sharing repository as the source location for the operating system image, configuration file, and SCU. When you define a repository location, you must add the parameters if any custom settings are available for the selected source. After you add the operating system files once, you can reuse them many times. As you add more and different operating system images, configuration files, or SCUs, you will see them in the list during the operating system installation process, and you can easily choose the one that you want to install.

Your files must be accessible by Cisco Intelligent Contact Management (ICM) on your target server where you want to install your operating system.

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image6.bin){width="6.333333333333333in" height="3.5625in"}

After you add the operating system image once, you can reuse it many times. As you add operating system images, they appear in the list during the operating system install process. You can easily select the operating system that you want to install.

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image7.bin){width="6.333333333333333in" height="3.5625in"}

Adding an Operating System Image

From the navigation menu, ~~click on~~ **click** [Explanation: 'click' instead of 'click on'. Category: Cisco Style Guide] **System**. Click on **Software** **Repository**, and ~~click on~~ **click** [Explanation: 'click' instead of 'click on'. Category: Cisco Style Guide] **OS Image Links** tab. Click on the **Add OS Image Link** button to start the wizard for adding operating system image.

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image8.bin){width="6.333333333333333in" height="3.5625in"}

In the **General** section of the wizard, enter the following details about the operating system image:

-   **Organization:** From the drop-down menu, select the organization to make a resource available to users. The organization can be a default or a specific entity, but it must be the same as the organization from~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]the operating system installation is triggered.

-   In the transfer protocol section, select the transfer protocol configured on the repository location. Depending on your chosen protocol, you will have to populate different options. The table below summarizes the configuration options for each transfer protocol.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  NFS                                                                                                                                                                                                          CIFS                                                                                                                                                                                                          HTTP(S)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------
  **File Location:** The location of the image file. For example, 10.1.17.250/repo/XYZ.iso                                                                                                                     **File Location:** The location of the image file. For example, 10.1.17.250/repo/XYZ.iso                                                                                                                      **File Location:** The location of the image file. For example, https:// 10.1.17.250/repo/XYZ.iso

  **Mount Options:** The choices for mounting as configured in the NFS server. Endpoints use the mount option to mount the remote share as part of a firmware upgrade or operating system install operation~~.   ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]**Mount Options:** The choices for mounting as configured in the CIFS server. Endpoints use the mount option to mount the remote share as part of a firmware upgrade or operating system install operation~~.   ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]**Username/password:** The strings that are the username and password respectively as configured on the HTTP(S) server.

                                                                                                                                                                                                               **Username/password:** Strings that are the username and password, respectively, as configured on the CIFS server~~.                                                                                            ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image9.bin){width="6.333333333333333in" height="3.5625in"}

+-----------------------------------------------------------------------+
| 3~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]HTTP protocol is not supported for Cisco IMM servers~~.             ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]|
+=======================================================================+
+-----------------------------------------------------------------------+

In the **Details** section of the wizard, enter the following details about the operating system image, and ~~click on~~ **click** [Explanation: 'click' instead of 'click on'. Category: Cisco Style Guide] **Add**:

-   **Name:** The string is the name of the operating system file. The name is populated as part of the image import when you install the specific operating system.

-   **Vendor:** Select the operating system vendor from the drop-down list.

-   **Version:** Select the operating system version from the drop-down list.

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 4~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]The drop-down list does not include a selection for Hyper-V Server. For the Hyper-V Server 2019, select the Windows Server 2019, For the Hyper-V Server 2016, choose the Windows Server 2016. |
+===================================================================================================================================================================================================+
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

-   **Description:** Add an optional description of the operating system file. If the image is obtained from the Cisco inventory, Cisco provides the description.

-   **Add Tag:** Add an optional tag to identify and search for the image.

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image10.bin){width="6.333333333333333in" height="3.5625in"}

After you add the operating system to the software repository, view the added operating system in the table view. Edit or delete details of the operating system in the table view.

~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. Which one of the transfer protocols have configuration options for file location, mount option, and authentication?

A. NFS

B. CIFS

C. HTTP

D. HTTPS

Adding an SCU

This topic describes how to add a Server Configuration Utility (SCU) to the Cisco Intersight software repository. It also provides configuration details for adding an SCU file depending on the protocol that you choose for the sharing location.

An SCU is an optional application that enables automated unattended operating system installation and an SCU is often required to complete the installation. An SCU helps in performing various tasks on the server, such as upgrading, troubleshooting, viewing the server health and logs, configuring the server, configuring Redundant Array of Independent Disks (RAID) volumes, and, most importantly, installing an operating system.

The Cisco UCS SCU guides you through a set of questions to help you configure the server through automatic recognition of the server hardware, with few reboots and an automated unattended operating system installation.

Procedure to Add an SCU

From the navigation menu, ~~click on~~ **click** [Explanation: 'click' instead of 'click on'. Category: Cisco Style Guide] **System**. Click on **Software Repository**, and ~~click on~~ **click** [Explanation: 'click' instead of 'click on'. Category: Cisco Style Guide] **SCU Links** tab. Click on the **Add SCU Link** button to start the wizard for adding operating system image.

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image11.bin){width="6.333333333333333in" height="3.5625in"}

In the **General** section of the wizard, enter the following details about the SCU image:

-   **Organization:** From the drop-down menu, select the organization to make a resource available to users. The organization can be a default or a specific entity, but it must be the same as the organization from~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]the operating system installation is triggered.

-   In the transfer protocol section, select the transfer protocol configured on the repository location. Depending on your chosen protocol, you will populate different options. The table below summarizes the configuration options for each transfer protocol.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  NFS                                                                                                                                                                                                          CIFS                                                                                                                                                                                                         HTTP(S)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------
  **File Location:** The location of the image file, for example 10.1.17.250/repo/XYZ.iso                                                                                                                      **File Location:** The location of the image file. For example, 10.1.17.250/repo/XYZ.iso                                                                                                                     **File Location:** The location of the image file. For example, https:// 10.1.17.250/repo/XYZ.iso

  **Mount Options:** The choices for mounting as configured in the NFS server. Endpoints use the mount option to mount the remote share as part of a firmware upgrade or operating system install operation~~.   ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]**Mount Options:** The choices for mounting as configured in the NFS server. Endpoints use the mount option to mount the remote share as part of a firmware upgrade or operating system install operation~~.   ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]**Username/password:** The strings that are the username and password respectively as configured on the HTTP(S) server.

                                                                                                                                                                                                               **Username/password:** The strings that are the username and password respectively as configured on the CIFS server~~.                                                                                         ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image12.bin){width="6.333333333333333in" height="3.5625in"}

+-----------------------------------------------------------------------+
| 5~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]HTTP protocol is not supported for Cisco IMM servers~~.             ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]|
+=======================================================================+
+-----------------------------------------------------------------------+

In the **Details** section of the wizard, enter the following details about the operating system image, and ~~click on~~ **click** [Explanation: 'click' instead of 'click on'. Category: Cisco Style Guide] **Add**:

-   **Name:** The string is the name of the Server Configuration file. When you install an operating system, the name string is populated as part of the image import.

-   **Version:** The vendor-provided version of the utility.

-   **Supported Models:** The server model for~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]the image of the SCU is applicable. You can add up to four models.

+--------------------------------------------------------------------------------+
| 6~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]SCU support is available for both Cisco UCS B-Series and C-Series servers. |
+================================================================================+
+--------------------------------------------------------------------------------+

-   **Description:** Add an optional description of the operating system file. Cisco provides the description if the image is obtained from the Cisco inventory.

-   **Set Tag:** Add an optional tag to identify and search for the SCU.

-   In the transfer protocol section, select the transfer protocol configured on the repository location. Depending on your chosen protocol, you will populate different options. The table below summarizes the configuration options for each transfer protocol.

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image13.bin){width="6.333333333333333in" height="3.5625in"}

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  NFS                                                                                                                                                                                                          CIFS                                                                                                                                                                                                         HTTP(S)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------
  **File Location:** The location of the image file, for example 10.1.17.250/repo/XYZ.iso                                                                                                                      **File Location:** The location of the image file. For example, 10.1.17.250/repo/XYZ.iso                                                                                                                     **File Location:** The location of the image file. For example, https:// 10.1.17.250/repo/XYZ.iso

  **Mount Options:** The choices for mounting as configured in the NFS server. Endpoints use the mount option to mount the remote share as part of a firmware upgrade or operating system install operation~~.   ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]**Mount Options:** The choices for mounting as configured in the NFS server. Endpoints use the mount option to mount the remote share as part of a firmware upgrade or operating system install operation~~.   ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]**Username/password:** The strings that are the username and password respectively as configured on the HTTP(S) server.

                                                                                                                                                                                                               **Username/password:** The strings that are the username and password respectively as configured on the CIFS server~~.                                                                                         ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

+-----------------------------------------------------------------------+
| 7~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]HTTP protocol is not supported for Cisco IMM servers~~.             ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]|
+=======================================================================+
+-----------------------------------------------------------------------+

After you add the SCU to the software repository, you can view the added SCU in the table view.

~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. Which one of these transfer protocols for adding SCU is *not* available for IMM servers?

A. NFS

B. CIFS

C. HTTP

D. HTTPS

Operating System Installation Using Cisco Source

This topic describes how to install an operating system using a Cisco-validated template. It also explains how ~~to apply the~~ **Consider moving the adverb (e.g., 'to quickly configure' → 'to configure quickly')** [Explanation: avoiding split infinitives when possible. Category: Grammar & Punctuation] configuration to the target operating system and lists supported target partitions for the installation process using the Cisco source method.

Procedure for Installing an Operating System Using Cisco Source

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 8~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Before you ~~initiate~~ **start** [Explanation: 'start' or 'begin' instead of 'initiate'. Category: Cisco Style Guide] operating system installation from Intersight, ~~make sure~~ **ensure** [Explanation: 'ensure' or 'verify' instead of 'make sure'. Category: Cisco Style Guide] that you uploaded an SCU and operating system image to the software repository, and that your server Cisco IMC has access to the file paths that are defined in the repository locations. |
+============================================================================================================================================================================================================================================================================+
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image14.bin){width="6.333333333333333in" height="3.5625in"}

The operating system installation wizard using Cisco source guides you through the following six steps:

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]The wizard offers confirmation of the server on~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]you want to install the operating system. Optionally, you can select two or more servers from the tabled view in Cisco Intersight and perform an automated installation of the operating system to the selected servers.

2~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Select the operating system and the version that you want to install. The list contains all the operating system images that are defined in the software repository. If you do not see the operating system that you want to install, select **Add Operating System Image** to add it to the system.

3~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]If you choose the **Cisco** option, you can use a Cisco-validated template to select the operating system version as the configuration file. Based on the operating system image that you previously chose, Cisco Intersight displays the configuration file in the **View File** panel.

4~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Click the eye icon next to the operating system image to view the configuration file on the right. The configuration file contains provisions or placeholders for the necessary configuration parameter values.

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image15.bin){width="6.940277777777778in" height="2.347344706911636in"}

5~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Cisco Intersight shows the configuration files according to the operating system image version that you select. The **Set Configuration** section displays the corresponding fields for adding values for the required parameters. Required parameters are mandatory values for a **Static IP** or **~~DHCP~~ **Dynamic Host Configuration Protocol (DHCP)** [Explanation: Acronym 'DHCP' not expanded on first use. Category: Acronyms]** configuration and an option to select the IPv4 protocol or the IPv6 protocol (IP address, netmask or prefix, gateway, name server, hostname, and password). Provide the password for the root/administrator user in the operating system. You can enable the password in encrypted format using the respective encryption mechanism that is supported by the operating system. For Windows installations, you must populate:

-   The **Product Key** field.

-   The administrator password.

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image16.bin){width="6.94027668416448in" height="3.9264195100612422in"}

6~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Select~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]SCU that you want ~~to apply to~~ **Consider moving the adverb (e.g., 'to quickly configure' → 'to configure quickly')** [Explanation: avoiding split infinitives when possible. Category: Grammar & Punctuation] during installation. The list within this step contains all SCUs that are defined in the software repository.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 9~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Different utilities exist for different servers. For example, you cannot apply an SCU to a Cisco M6 server if it is used for a Cisco M5 server. Always ~~make sure~~ **ensure** [Explanation: 'ensure' or 'verify' instead of 'make sure'. Category: Cisco Style Guide] that you have an up-to-date and current SCU. |
+===================================================================================================================================================================================================================+
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

7~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Select the installation target. The installation target is the partition where you will install the operating system. The supported targets must meet one of the following conditions:

-   The following are supported storage controllers:

```{=html}
<!-- -->
```
-   MegaRAID controller

-   Cisco Boot Optimized M.2 controller with the server configured in UEFI boot mode

```{=html}
<!-- -->
```
-   The following are supported storage types:

```{=html}
<!-- -->
```
-   Virtual drives from MegaRAID controllers

-   Physical disks configured as Just a Bunch of Disks (JBOD)

8~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]After you have completed the wizard, it provides a summary for you to ensure that all the settings are correct. This step is your opportunity to correct any settings.

You can monitor the installation status under the **Active Tasks** menu and watch the progress of the operating system install process. You can also monitor the progress using a keyboard, video, mouse (KVM) window to see what is happening in the output from the server. To see the embedded server KVM window inside Cisco Intersight, you must launch tunneled KVM from the server's **Action** menu.

~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. Which is a supported type of storage controller for installing an operating system from Cisco Intersight?

A. Cisco 12G Modular RAID

B. Cisco Boot Optimized M.2 with server configured in AHCI mode

C. Embedded RAID

D. MegaRAID

Operating System Installation Using Custom Source

This topic describes the procedure of installing an operating system using a custom configuration source. It also explains how to prepare a configuration (kickstart) file and apply it using the install wizard.

Custom Configuration File

You can add new configuration files in the **Software \> Operating System Configuration Files** section. The list of configuration files is filtered based on the operating system vendor and version. If you want to create a new operating system configuration file, click the **Create New** button.

When you install an operating system using the **Custom** option, the selected configuration file can be static or contain placeholders that you can change at run time. A best practice is to prepopulate the static file with the relevant configuration settings. You can also create a template file with placeholders instead of actual answers. If you use a file with custom placeholders, click the **Set Configuration** link on the **Configuration** page. For example, you might need to set the hostname and IP address values for each server. The uploaded answer file placeholder must conform to Golang template syntax.

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image17.bin){width="6.940277777777778in" height="3.0403663604549434in"}

The configuration file contains all the answers that you will provide during the operating system installation procedure. The following is an example of a VMware vSphere ESXi configuration file. Lines that start with the pound sign (**\#**) are comments that explain the next line.

\# Sample scripted installation file\
\# Accept the VMware End User License Agreement\
vmaccepteula\
\# Set the root password for the DCUI and Tech Support Mode\
rootpw myp@ssw0rd\
\# Install on the first local disk available on machine\
install \~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]firstdisk \~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]overwritevmfs\
\# Set the network to DHCP on the first network adapter\
network \~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]bootproto=dhcp \~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]device=vmnic0\
\# A sample post-install script\
%post \~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]interpreter=python \~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]ignorefailure=true\
import time\
stampFile = open(\'/finished.stamp\', mode=\'w\')\
stampFile.write( time.asctime() )

You can install an operating system on multiple servers if you define the IP configuration of the host server through the DHCP scope.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 10. When using a custom installation mode, the Cisco Intersight template does not validate the answer file values that you provide. ~~Make sure~~ **Ensure** [Explanation: 'ensure' or 'verify' instead of 'make sure'. Category: Cisco Style Guide] that you validate the placeholder values when using a custom template. The filename in the custom answer file that you upload must not contain special characters except a period (**.**), hyphen (**-**), or underscore (**\_**). Cisco Intersight does not validate the answer file. Validate the answer file using an operating system validation tool, for example, Windows System Image Manager (Windows SIM) for Windows. For non-Windows operating system answer files, confirm that the file does not contain **Ctrl+M** (carriage return) characters, which can cause unexpected behavior during operating system installation. |
+========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Procedure for Installing an Operating System Using Custom Source

The custom operating system installation wizard walks you through six steps. The following figure shows the high-level steps for **Custom** operating system installation.

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image18.bin){width="6.333333333333333in" height="3.5625in"}

The following steps detail the procedure for **Custom** operating system installation:

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]The wizard offers the confirmation of the server selection on~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]you want to install the operating system. Optionally, you can select two or more servers from the tabled view in Cisco Intersight and perform an automated installation of the operating system to selected servers.

2~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]You will select~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]operating system and version that you wish to install. The list contains all the operating system images that are defined in the software repository. If you do not see the operating system that you want to install, select **Add Operating System Image** to add it to the system.

3~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]With the **Custom** option, you can upload a kickstart (configuration) file or a file with the necessary placeholders for configuration parameters. The Configuration page of the operating system installation wizard provides two tabs supporting management operating system installation files:

```{=html}
<!-- -->
```
a~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]**Software Repository:** Select a configuration file defined in the software repository.

b~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]**Local Machine:** Click **Browse** and upload the configuration file from your local machine. The file under the **Local Machine** tab is only available for the current installation.

```{=html}
<!-- -->
```
4~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]The requested values are pulled from the kickstart file that you use. The names that you use in the kickstart file are what you see to populate the variables. Click the eye icon to view the configuration file details.

5~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Select the installation target, which is the partition in~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]you will install the operating system. The same type of installation target is supported with both the **Cisco** and **Custom** options.

6~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]The wizard provides a summary for you to review, to verify that all the settings are correct. This step is your opportunity to correct the configuration.

You can monitor the installation status under the active tasks menu and watch the progress of the operating system install process. You can also monitor the progress using a keyboard, video, mouse (KVM) window to see what is happening in the output from the server. To see the embedded server KVM window inside the Cisco Intersight, you must launch the tunneled KVM from the server's **Action** menu.

After you enter the required values, the installation prompts and warns the administrator that it will start the installation and overwrite any existing operating system that might be there.

~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. The configuration file template must comply with~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]of the following programming languages?

A. Golang

B. Java

C. Python

D. Ruby

Operating System Installation Using Embedded Source

This topic describes the procedure of installing an operating system using the single ISO file that contains all the necessary configuration files for operating system installation.

ISO File for Embedded Installation

An **Embedded** installation applies the ISO image that you provide and assumes that everything that it needs is already on it. As an administrator, you must create this ISO image to support an automated installation. During installation, you will point to this ISO image, so the image must contain all the necessary configuration files for the target operating system. Optionally, you can select an SCU to use with the ISO image.

Creating an automated ISO image depends on the target operating system and customization level that you want to achieve, but the basic procedure for most operating systems has three steps:

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Extract the original ISO file to a working directory used for modifications.

2~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Create and modify the kickstart configuration file and add it to an extracted ISO directory. Optionally, modify the boot file to specify the location of the installation script.

3~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Recreate the ISO image using the content of the working directory using the ISO creation utility, such as **mkisofs** or **genisoimage**.

Procedure for Installing an Operating System Using Embedded Source

The **Embedded** operating system installation wizard walks you through five steps.

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image19.bin){width="6.333333333333333in" height="3.5625in"}

The following steps explain the detailed procedure for an **Embedded** operating system installation:

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]The wizard offers confirmation of the server selection on~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]you want to install the operating system. Optionally, select two or more servers from the tabled view in Cisco Intersight and perform an automated installation of the operating system to the selected servers.

2~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Select~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]operating system and version to install. The list contains all the operating system images that are defined in the software repository. You must add an embedded ISO image location to the software repository before you run an operating system install procedure.

3~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Select the **Embedded** option. You will not be able to modify your target operating system configuration. Your configuration should be embedded in the ISO image that you selected in the previous step.

4~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Optionally, select the SCU to run on this server before the ISO image.

5~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]After you have completed the wizard, it will provide a summary for you to review and validate that all the settings are correct. This step is your opportunity to correct any settings in the configuration.

After you ~~initiate~~ **start** [Explanation: 'start' or 'begin' instead of 'initiate'. Category: Cisco Style Guide] the operating system installation using the **Embedded** option, the Cisco IMC pulls the ISO image from the sharing location, and the server locally ~~initiates~~ **starts** [Explanation: 'start' or 'begin' instead of 'initiate'. Category: Cisco Style Guide] the installation from the provided ISO.

From Cisco Intersight, you can monitor the limited execution flow for the operating system install process. After Cisco Intersight validates the server configuration, the server prepares and downloads the ISO file and sets the boot order. Installation progress is not available in Cisco Intersight, but you can track when the server completes the installation. The following is an example of the post-install tracking for VMware vSphere ESXi:

%post \~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]interpreter=busybox \~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]ignorefailure=true ESXI_INSTALL_LOG=/var/log/esxi_install.log\
echo \\\"OS INSTALL COMPLETED\\\" \>\> /var/log/Xinstall.log /opt/ucs_tool_esxi/ucs_ipmitool write_file /var/log/Xinstall.log osProgress.log

~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. Which two ISO utilities can be used to create ISO files with embedded configuration files (kickstart files)? (Choose two.)

A. genisofs

B. genisoimage

C. ISO mount

D. mkfs

E. mkisofs

Understanding Placeholder Variables

A placeholder is a variable that you define in the configuration files. During the operating system installation, you assign values to the placeholders. You can use placeholders for **Cisco** and **Custom** operating system installations. Two types of placeholders are in the configuration files: custom and internal.

Custom Placeholders

In the operating system installation wizard, Cisco Intersight prompts you to provide a value for the parameter. Cisco Intersight assigns the value to a custom placeholder. Intersight replaces the placeholder with the value.

Use the following examples of custom placeholders in your configuration files:

{{.secure.Password}}\
network \~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]bootproto=static \~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]ip={{ .IpAddress }} \~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]netmask={{ .Netmask }} \~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]gateway={{ .Gateway }} \~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]host name={{ .Hostname }} \~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]nameserver={{ .NameServer }}

You can express custom placeholders using conditional expressions in the answer file:

{{if (eq .IpConfigType \"dhcp\")}}network \~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]bootproto=dhcp {{end}}\
{{if (eq .IpConfigType \"static\")}}network \~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]bootproto=static \~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]ip={{ .IpAddress }} \~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]netmask={{ .Netmask }} \~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]gateway={{ .Gateway }} \~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]host name={{ .Hostname }} \~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]nameserver={{ .NameServer }} {{end}}

Internal Placeholders

When you define your kickstart file, the operating system installation requires mandatory placeholder strings. Cisco Intersight replaces the content of internal placeholder variables with an appropriate value during the installation. You cannot change internal placeholders because the system predefines them. Internal placeholders are expressed in all capital letters in the configuration files.

Depending on the operating system that you are installing, include the following placeholders in the kickstart (answer) file:

-   **DISKIDPLACEHOLDER (all operating systems)/DISK_NAME_PLACEHOLDER (SUSE Linux Enterprise Server (SLES):** Populates the target disk where you want to install your operating system. This placeholder is required for all operating system installations. For example, VMware vSphere ESXi\'s kickstart (answer) file contains this placeholder.

\# Accept the VMware End User License Agreement\
vmaccepteula\
\# Set the root password for the DCUI and Tech Support Mode\
rootpw {{ .secure.Password }}\
#for Local boot\
DISKIDPLACEHOLDER\
\# Set the network to use a static IP on the first network adapter\
\
network \~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]bootproto=static \~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]ip={{ .IpAddress }} \~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]netmask={{ .NetMask }} \~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]gateway={{ .GateWay }} \~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]host name={{ .HostName }} \~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]nameserver=={{ .NameServer }}\
\<\< Output omitted \>\>\>

-   **PARTITIONPLACEHOLDER:** Populates the partition where you want to install your operating system. You must define the placeholder for Windows operating system installations. For example, the unattended file for Windows 2019 Server contains this placeholder:

\<Value\>Windows Server 2019 SERVERDATACENTER\</Value\>\
\</MetaData\>\
\</InstallFrom\>\
\<InstallTo\>\
\<DiskID\>DISKIDPLACEHOLDER\</DiskID\>\
\<PartitionID\>PARTITIONPLACEHOLDER\</PartitionID\>\
\</InstallTo\>\
\<InstallToAvailablePartition\>false\</InstallToAvailablePartition\>\
\<WillShowUI\>OnError\</WillShowUI\>\
\<\< Output omitted \>\>\>

-   **OS_INSTALL_COMPLETED_STATUS_PLACEHOLDER:** Tracks and notifies the completion of operating system installation. You must include DISKIDPLACEHOLDER with **OS_INSTALL_COMPLETED_STATUS_PLACEHOLDER** to track installations. The placeholder is required only for RHEL and CentOS installations. For example, the unattended file for RHEL contains this placeholder:

\<\< Output omitted \>\>\>\
%post \~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]nochroot \~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]log=/root/ks-post.log\
OS_INSTALL_COMPLETED_STATUS_PLACEHOLDER\
%end\
reboot

+--------------------------------------------------------------------------------------------+
| 11. The **Go Template** placeholder variables should contain only alphanumeric characters. |
+============================================================================================+
+--------------------------------------------------------------------------------------------+

+-----------------------------------------------------------------------------------------------------------------------------------------+
| 12. Do not insert multihierarchy or multilevel placeholders. A multihierarchy placeholder contains nested levels of placeholder values. |
+=========================================================================================================================================+
+-----------------------------------------------------------------------------------------------------------------------------------------+

For more examples of kickstart files for different operating system versions, refer to <https://github.com/CiscoDevNet/intersight-BMaaS/tree/main/os-install/kickstart-samples>.

~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. Which two types of placeholders exist in the operating system configuration files? (Choose two.)

A. automatic

B. custom

C. external

D. internal

E. static

F. variable

Password Encryption in Operating System Install

You can enter a plaintext or encrypted password in the operating system install wizard. If you enter a plaintext password, Cisco Intersight automatically encrypts it. This topic explains operating system-specific considerations for the encryption of different types of passwords.

Specific Considerations

You can use a password encryption service for both **Cisco** and **Custom** operating system installations.

For VMware vSphere ESXi and other Linux-based operating systems, you can generate a secure (hashed) password on another Linux-based system using the SHA-512 algorithm with the **mkpasswd \~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]method=sha-512** command. Alternatively, use an online encoding source to generate the password by specifying **SHA-512** in the protocol options.

Windows-based systems use the base64 method to generate an encrypted password. Confirm that you set the destination character to UTF-16LE. To get the password, apply a password encrypting service and append the password with **AdministratorPassword**. For example, if your password is **myPassword1234**, enter **myPassword1234AdministratorPassword**. Enable the **Password provided is in encrypted format** check box to use an encrypted password in the **Password** field in the operating system installation wizard.

If you use custom templates to install Windows, you must provide two placeholder passwords for the Auto Logon and the Administrator passwords in the following formats in the answer file:

-   For Auto Logon passwords, append the suffix **Password**. The following figure shows the placeholder for the Auto Logon with this suffix.

\<AutoLogon\>\
\<Passwords\>\
\<value\>{{.PlaceholderAutoLogonPassword}}\</Value\>\
\<PlainText\>false\</PlainText\>\
\</Password\>\
\<Enabled\>true\</Enabled\>\
\<LogonCount\>~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\</Logoncount\>\
\<username\>Administrator\</Username\>\
\</Autologon\>

-   For Administrator passwords, append **AdministratorPassword** to the password. The following figure shows the placeholder for the Administrator password with this suffix.

\<AdministratorPassword\>\
\<value\>{{.PlaceholderAdministratorPassword}}\</Value\>\
\<PlainText\>false\</PlainText\>\
\<AdministratorPassword\>

When you populate these two placeholders, passwords are generated, and Cisco Intersight passes this configuration file to the operating system.

\<AutoLogon\>\
\<Password\>\
\<Value\>QwBsAG8AdQBwAGkAYQAhADEAMgAzAFAAYQBzAHMAdwBvAHIAZAA=\</Value\>\
\<PlainText\>false\</PlainText\>\
\</Password\>\
\<Enabled\>true\</Enabled\>\
\<LogonCount\>~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\</LogonCount\>\
\<Username\>Administrator\</Username\>\
\</AutoLogon\>

\<AdministratorPassword\>\
\<Value\>QwBsAG8AdQ8wAGkAYQAhADEAMgAzAEEAZABtAGkAbgBpAHMAdAByAGEAdABvAHIAUABhAHMAcw83AG8AcgBkAA==\</Value\>\
\<PlainText\>false\</PlainText\>\
\</AdministratorPassword\>

~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. Which encoding method is used in Windows-based systems to generate an encrypted password?

A. ASCII

B. base64

C. blob

D. utf-8

Operating System Installation Using a CSV File

You can install an operating system on multiple servers using comma-separated values (CSV). In the CSV file, you will specify the installation parameters of the operating system for each server. The CSV file contains all the necessary settings for operating system installation, such as server serial number, operating system image, IP settings, and passwords. In this topic, you will learn how to use a CSV file in the operating system installation procedure and how to create a CSV file for installation.

Procedure for Installing an Operating System Using a CSV File

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image20.bin){width="6.333333333333333in" height="3.5625in"}

The procedure for installing an operating system using a CSV file is as follows:

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Initiate the operating system installation with CSV by selecting the servers defined in the CSV file, clicking the ellipsis (**\...**) symbol in the top left of the **Servers** report, and choosing **Install Operating System**.

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image21.bin){width="6.36128937007874in" height="3.8193547681539806in"}

2~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]The operating system install window opens with the **Set Configuration** **via** **Wizard** tab selected.

3~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Click the **Set Configuration** **through the** **File** tab.

4~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Click the **Start** button and the **File Upload** screen displays.

5~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Click the **Browse** button to navigate to the CSV configuration file you want to use for the selected servers. Select your CSV file. Cisco Intersight returns to the **File Upload** screen, displaying the selected file in the **Selected File** field.

6~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Confirm the uploaded CSV file is present. Click **Next**. Cisco Intersight displays the **Summary** screen with the selected file in the **File Upload** field. Review the summary details and confirm they match the fields of the CSV file you uploaded, for example, values in the **Serial Number** column.

7~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Click **Install** to install the operating system. Cisco Intersight displays an intervening message, warning you to ~~make sure~~ **ensure** [Explanation: 'ensure' or 'verify' instead of 'make sure'. Category: Cisco Style Guide] you want to install the new version on target servers.

CSV File Format

Using the CSV data format, you can build a textual file containing data records in a tabular format for each server operating system.

You can create a CSV data file using a text editor such as Microsoft Notepad. Use a separate line to enter data for each server. Separate each data field with a comma and include comma separators for blank fields. Enter data on every line in the data file because an error occurs during the insert transaction if you enter a blank line in a CSV file.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 13. Cisco recommends uploading Text-Based CSV files saved in the UTF-8 format only, as characters other than ASCII characters can be stored in this format. |
+=============================================================================================================================================================+
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

The CSV file must have the appropriate comma-delineated columns. The following are examples of typical column (header) parameters in the CSV file:

-   **OsImageName:** Navigate to **Software Repository** \> **Operation Systems Images** to obtain the **OsImageName** parameter value.

-   **SerialNumber:** Serial number of a target server.

-   **overrideSecureBoot:** Specify override secure boot config for secure boot VMware vSphere ESXi installation.

-   **ScuImageName:** Navigate to **Software Repository** \> **Software Configuration Utilities** to get the **ScuImageName** parameter value.

-   **ConfigurationSource:** The possible modes of installations are **Cisco**, **Embedded**, and **Custom**.

-   **IpConfigType:** The possible values are **Static** and **DHCP**.

-   **IpAddress:** Specify the IP address to be assigned to the server. The IP address can be **IPv4** or **IPv6**.

-   **NetMask/Prefix:** Specify the netmask for IPv4 and the prefix for IPv6.

-   **Gateway:** Specify the gateway address for the server.

-   **Password:** Specify the password for **administrator/root**.

-   **ProductKey:** Specify the Windows operating system product key.

+---------------------------------------------------------------------------------------------+
| 14. Some parameters are specific to the installation mode, such as **Cisco** or **Static**. |
+=============================================================================================+
+---------------------------------------------------------------------------------------------+

The following example of a CSV file shows two headers. The first header, and values that are assigned to its parameters, are common for each target server. The values that are assigned after the second header are values for each server, one per line of the CSV file.

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image22.bin){width="6.333333333333333in" height="3.5625in"}

For more examples of kickstart files for different operating system versions, refer to <https://github.com/CiscoDevNet/intersight-BMaaS/blob/main/os-install/bulk-install-csv-samples/>

~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. Which of the following encoding formats is recommended for creating text-based CSV files?

A. ASCII

B. base64

C. blob

D. utf-8

Summary

You are now familiar with the prerequisites for installing the operating system using Cisco Intersight and how to add the necessary files to the software repository used in the operating system installation procedure. This course also covers how to install the operating system using three different configuration sources, use of placeholders in operating system configuration files, and install the operating system on multiple servers using a CSV file.

Summary Challenge

Summary Challenge

Form

Item Group

~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. Which of the following operating system installation types are available in the Cisco Intersight? (Choose three.)

A. Cisco

B. Custom

C. Embedded

D. ISO

E. Repository

F. Third-party

~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. Which of the following types of servers are supported targets for the operating system installation feature from the Cisco Intersight? (Choose three.)

A. B-Series

B. C-Series

C. HX Series

D. S-Series

E. Third-party

F. X-Series

~~3~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. Which of the following transfer protocols are available options for adding operating system images and SCU files in the Cisco Intersight? (Choose three.)

A. CIFS

B. FTP

C. HTTP(S)

D. NFS

E. SCP

F. SFTP

G. TFTP

~~4~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. When using the custom source for the operating system installation feature using Cisco Intersight, which of the following options are available for selecting the configuration file? (Choose two.)

A. Embedded

B. GitHub

C. Local Machine

D. Network Share

E. Software Repository

~~5~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. Which of the following steps is mandatory in the operating system installation process using embedded source?

A. Populate placeholders

B. Select configuration file

C. Select operating system image

D. Select SCU

~~6~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. Which of the following placeholders is mandatory for all types of operating systems?

A. DISKIDPLACEHOLDER

B. DISKPLACEHOLDER

C. PARTITIONIDPLACEHOLDER

D. PARTITIONPLACEHOLDER

~~7~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. Which of the following is the correct separator for values of parameters in a CSV file used for the operating system install feature in the Cisco Intersight?

A. Comma

B. Enter

C. Semicolon

D. Space

Objectives Tree

Describe prerequisites and various options for installing an operating system from Cisco Intersight

Describe the operating system installation process using Cisco Intersight

Describe requirements and limitations for the operating system installation process using Cisco Intersight

Describe the procedure of adding an operating system image to software repository in Cisco Intersight

Describe the procedure of adding an SCU image to the software repository in Cisco Intersight

Describe the procedure of installing an operating system with the Cisco option in Cisco Intersight

Describe the procedure of installing an operating system with the Custom option in Cisco Intersight

Describe the procedure of installing an operating system with the Embedded option in Cisco Intersight

Describe the configuration parameters used in the operating system configuration files

Describe password encryption for operating system installation in Cisco Intersight

Describe the operating system installation procedure using the CSV file

Describe how to install an operating system

~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation][](media/image23.bin){width="6.333333333333333in" height="3.5625in"}


---

## Change Legend

| Markup | Meaning |
|--------|---------|
| ~~text~~ | Text to remove (strikethrough) |
| **text** | Text to add (bold) |
| [Explanation: ...] | Rationale for change |

*Generated by Course AI Editor on 2026-03-04 14:06*