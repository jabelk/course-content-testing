# Inline Editorial Review: AUTOCOR-Sec01_orig

**Instructions**: Search for `~~` to find deletions and `**` to find additions.
Copy this document into Word to see Track Changes formatting.

---

**Total Changes**: 111 (Auto-fix: 49, Review: 54, Questions: 8)

---

AUTOCOR

Design, Deploy, and Manage Network Automation Systems

Student Learning Guide

Version 1.0

Section 1: Network Automation Toolkits

Introduction

You have been promoted to the network automation team at a multinational retail chain that manages over 500 stores in multiple countries. The company operates a traditional CLI-based network infrastructure comprising routers, switches, and firewalls.

The network operations team has been struggling with manual configuration tasks that consume hours each day, and inconsistent device configurations across locations make troubleshooting extremely difficult and time-consuming. As a result, the team spends more time firefighting than improving the network.

The breaking point occurred during a manual update, when a misconfigured ~~ACL~~ **access control list (ACL)** [Explanation: Acronym 'ACL' not expanded on first use. Category: Acronyms] shown in the following figure, disrupted payment processing at 50 stores on Black Friday. The incident lasted for two hours as engineers scrambled to identify and fix the affected devices manually.

![ Network showing three retail stores connected through routers to a firewall and central server. A configuration box displays router commands for applying an access control list, highlighting a misconfiguration that disrupted payment processing.](media/image1.bin){width="6.94027668416448in" height="3.9514905949256343in"}

These challenges have made it clear that manual network management cannot scale, which prompted the Chief Technology Officer (CTO) to mandate network automation. At the quarterly review, leadership emphasized that the network must be both programmable and self-documenting.

Your assignment is to evaluate and select the right automation tools for your multivendor environment.

Network Automation Tools Overview

After analyzing the Black Friday incident, you realize that tool selection determines success. The right combination of automation approaches can prevent such outages, while poor choices create new complexity without solving core problems. Choose each automation tool to learn more.

Python CLI Scripts

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Network setup showing a web interface connected to two network devices. The command shown is show i p interface brief, indicating retrieval of interface status information from the devices.](media/image2.bin){width="6.940277777777778in" height="6.355442913385827in"}
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  : //outerTableForFigure

Sometimes CLI scripting is simply the easiest approach. When you know the commands well and there\'s minimal output to parse, why complicate things? Libraries like Netmiko or pyATS let you ~~SSH~~ **Secure Shell (SSH)** [Explanation: Acronym 'SSH' not expanded on first use. Category: Acronyms] to devices and run commands exactly as you would type them.

**Best suited for:** Emergency troubleshooting, vendor-specific commands not available via API, and quick data collection across multiple devices when structured APIs are unavailable or impractical.

Python API-based Scripts

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Network setup showing a web interface sending an H T T P S GET request to retrieve data from network devices using the path data slash interface.](media/image3.bin){width="6.940277777777778in" height="6.355442913385827in"}
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  : //outerTableForFigure

Interact with the device via ~~NETCONF~~ **Network Configuration Protocol (NETCONF)** [Explanation: Acronym 'NETCONF' not expanded on first use. Category: Acronyms], ~~RESTCONF~~ **REST-based Configuration Protocol (RESTCONF)** [Explanation: Acronym 'RESTCONF' not expanded on first use. Category: Acronyms], or vendor-specific Representational State Transfer (REST) APIs that provide structured access to device configurations and operational data. Instead of parsing text output, these interfaces return JavaScript Object Notation (JSON) or XML data that programs can process reliably. Python is frequently used for API automation with libraries like requests and ncclient.

**Best suited for:** Organizations with modern devices supporting standardized APIs, seeking robust automation with transactional capabilities and structured data handling.

Configuration Management Tools

  ---------------------------------------------------------------------------------
  ![](media/image4.bin){width="6.940277777777778in" height="6.355442913385827in"}
  ---------------------------------------------------------------------------------

  ---------------------------------------------------------------------------------

  : //outerTableForFigure

These tools provide abstraction layers so you don\'t have to handle all the logic with Python. Instead of writing code to connect, check state, apply changes, and handle errors for each device type, you describe what you want in simple, human-readable files. This definitions are then translated to the required CLI commands or API calls.

**Best suited for:** Maintaining configuration consistency across large environments or teams that would like to avoid writing custom code.

Network Controller Platforms

  ---------------------------------------------------------------------------------
  ![](media/image5.bin){width="5.812902449693788in" height="5.329032152230971in"}
  ---------------------------------------------------------------------------------

  ---------------------------------------------------------------------------------

  : //outerTableForFigure

These platforms provide centralized management and pre-built logic that handles common use cases and enables intent-based networking. Typically they provide northbound APIs that enable you to automate those workflows. Examples include Cisco Catalyst Center, Meraki Dashboard, or Cisco Application Centric Infrastructure (ACI).

**Best suited for:** Organizations that are committed to single-vendor ecosystems with budget for licensing and training investment.

Tool Selection Strategy

With 500 stores and a diverse infrastructure, which tools will truly be effective? The key is to select tools that align with your network, complement your team\'s skills, and solve the problems that matter most to your business, rather than simply chasing the latest technology.

Most importantly, you must decide if you will build the solution from the ground up using Python and configuration management tools like Ansible, or you will use logic that is already built-in different network controller platforms.

![Two network devices connect to Python scripts, configuration management tools, and network controller platforms, showing choices between building automation from the ground up or using built-in platform logic.](media/image6.bin){width="6.045160761154856in" height="4.232257217847769in"}

Your choice of tools depends on three factors:

-   Your existing resources

-   Your device capabilities

-   What your team can effectively use

Start by auditing your existing investments. If you have Cisco Catalyst Center or Cisco ACI licenses, use them as your foundation. You can always add custom scripts for gaps that they do not cover. If your team already manages servers with Ansible, extending it to network devices probably makes more sense than introducing something completely new.

+-----------------------------------------------------------------------------------------------------------------+
| 1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Multivendor environments rule out single-vendor controllers. You need tools that work across all platforms. |
+=================================================================================================================+
+-----------------------------------------------------------------------------------------------------------------+

Depending on the ~~desired~~ **wanted** [Explanation: 'want' or 'wanted' instead of 'desire/desired'. Category: Cisco Style Guide] option, you\'ll also have to ~~make sure~~ **ensure** [Explanation: 'ensure' or 'verify' instead of 'make sure'. Category: Cisco Style Guide] that all your devices support that approach.

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Device Type                                                               Capabilities                                      Tools
  ------------------------------------------------------------------------- ------------------------------------------------- --------------------------------------------------------------
  **Modern equipment** (with application programming interfaces \[APIs\])   Structured automation, error handling, rollback   requests, ncclient, terraform providers, Ansible API modules

  **Legacy devices**                                                        Limited to CLI scripting                          Netmiko, pyATS, Ansible SSH modules
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Regardless of the equipment, it is important to consider both your knowledge and your team\'s knowledge. You should match the tool to your team\'s knowledge. Each tool brings specific benefits:

-   **Python:** Maximum control, but requires scripting skills.

-   **Ansible:** Easier to read templates, but may lack some needed features.

-   **Controller**s**:** A lot of logic-~~built in~~ **Change 'built in' to 'built-in'** [Explanation: Hyphenate 'built-in' when used as a compound modifier. Category: Grammar & Punctuation] but requires specific knowledge.

+--------------------------------------------------------------------------------------------------------------+
| 2~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Choosing tools that your engineers will actually use and maintain is probably the most important factor. |
+==============================================================================================================+
+--------------------------------------------------------------------------------------------------------------+

Also, remember that no single tool can handle every scenario perfectly. Each has strengths and weaknesses:

  ----------------------------------------------------------------------------------------------------------------------------
  Tool                    Strengths                                        Limitations
  ----------------------- ------------------------------------------------ ---------------------------------------------------
  RESTCONF APIs           Excellent for configuration changes              May not support some CLI operations

  Ansible                 Abstraction and readability when modules exist   Gaps for newer features

  Controllers             Complete workflows for common scenarios          Limited flexibility outside predefined automation
  ----------------------------------------------------------------------------------------------------------------------------

Instead of searching for a single perfect tool, focus on building a flexible automation strategy. Start with your most common and painful tasks, and use the simplest tool that solves them reliably.

+-------------------------------------------------------------------------------------------------------------------------+
| 3~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Most effective automation strategies often combine multiple tools, using each where it provides the greatest value. |
+=========================================================================================================================+
+-------------------------------------------------------------------------------------------------------------------------+

Regardless of the tools you chose, starting small with low-risk tasks is always a good idea:

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Begin with configuration backups or report generation.

2~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Allow the team to learn tools and processes gradually.

3~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Minimize production risk.

4~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Build confidence with each success.

5~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]Demonstrate value to skeptical team members.

Key Takeaways

Reflect on the following key takeaways, and click each one to check your understanding:

Begin with Low-Risk Tasks

Start with simple operations like configuration backups or report generation. Build confidence through small wins before tackling critical configuration changes. Each success demonstrates value and reduces resistance to automation.

Consider Team Skills

The best tool is the one your team will actually use. If your team has coding skills you can immediately start building custom solutions, otherwise consider tools that provide simplicity.

Use What You Have

Prioritize tools that you already use and check device capabilities before choosing new automation options.

No Universal Solution

Different tools excel in different scenarios. Often, a combination of tools is needed.

In the following guides you\'ll explore each network automation approach, evaluating the real benefits and limitations each brings to your network infrastructure.

~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. Which three factors should be considered when selecting network automation tools for a multivendor environment? (Choose three)

A. The team\'s existing coding skills and knowledge.

B. The capabilities of the network devices (for example, API support, legacy CLI).

C. The ability to generate advanced network topology maps.

D. The potential to combine multiple tools for different scenarios.

E. Adherence to open-source licensing models.

F. Built-in capability for advanced network performance monitoring.

Model-Driven APIs for Network Automation

As you plan your automation strategy, you realize there are multiple approaches to consider. Since your infrastructure includes modern devices with API capabilities, you decide to evaluate model-driven APIs first, by exploring how they compare to traditional methods.

Model-driven APIs like NETCONF and RESTCONF provide programmatic access to network devices using standardized data models.

Key advantages include:

-   **Structured data formats:** XML and JSON.

-   **Standardized operations:** Create, read, update, delete.

-   **Atomic transactions:** Either all changes succeed or everything rolls back.

-   **Easier error handling:** APIs return explicit error codes, not ambiguous CLI output.

Understanding these interfaces is essential, as they eliminate CLI parsing complexity and enable reliable automation.

Power of Structured Data

Having programmable access through APIs is very useful for automation. But to understand why, first observe what happens when you try to automate using traditional CLI commands. You might write a script that connects via SSH to each device and executes commands, just as you would manually. This seems straightforward at first.

For example, if you want to monitor interface traffic on your switches, you would use the **show interfaces** command and easily find the packet statistics. However, extracting this data programmatically for monitoring purposes can be challenging.

Following is an example of the output of the **show interfaces GigabitEthernet0/1** command on a Cisco switch running ~~IOS~~ **Cisco IOS Software** [Explanation: Acronym 'IOS' not expanded on first use. Category: Acronyms] XE 15.x Software:

GigabitEthernet0/1 is up, line protocol is up\
Hardware is Gigabit Ethernet, address is 0023.04ee.be01\
Description: UPLINK_TO_CORE\
~~MTU~~ **Maximum Transmission Unit (MTU)** [Explanation: Acronym 'MTU' not expanded on first use. Category: Acronyms] 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec\
reliability 255/255, txload ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]/255, rxload ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]/255\
~~5~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] minute input rate 1000 bits/sec, ~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] packets/sec\
~~5~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] minute output rate 2000 bits/sec, ~~3~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] packets/sec\
1564 packets input, 98896 bytes, 0 no buffer

The packet input information is clearly visible: \"1564 packets input.\" However, if you wanted to find this information programmatically, you would need to be very familiar with the output format and write code that can parse the cleartext to extract the right data from the right position in each line.

For experienced network engineers with coding skills, this task is manageable. However, a routine software upgrade can change the output format. After upgrading to IOS XE 16.x Software, the same command now produces the following output:

GigabitEthernet0/1 is up, line protocol is up\
Hardware is Gigabit Ethernet, address is 0023.04ee.be01\
Description: UPLINK_TO_CORE\
MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec\
reliability 255/255, txload ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]/255, rxload ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]/255\
~~5~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] minute input rate 1000 bits/sec, ~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] packets/sec\
~~5~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] minute output rate 2000 bits/sec, ~~3~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] packets/sec\
rx pkts: 1564 bytes: 98896 drops: 0

Now your parsing breaks completely because the format changed from \"1564 packets input\" to \"rx pkts: 1564.\" You discover this at ~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] AM when your monitoring system shows zero traffic, but the network is actually running normally. Your automation reports everything is fine, while actual problems go undetected. This is the fundamental problem with CLI automation---the output is designed for humans to read, not for computers to parse. It uses spacing and positioning to show information. Even small changes in software versions or device models can break your parsing logic completely.

This limitation is precisely why model-driven APIs were created. Instead of parsing human-readable text, APIs return structured data that programs can reliably process.

NETCONF

NETCONF is a network management protocol that lets you retrieve configuration data, obtain operational information such as interface statistics, and make configuration changes programmatically. It uses SSH for secure communication and sends all data in XML format. Instead of parsing unstructured text output that requires complex regex patterns, you receive structured data in XML format with clearly defined fields and values that programs can easily navigate.

The data schema is defined by ~~YANG~~ **Yet Another Next Generation (YANG)** [Explanation: Acronym 'YANG' not expanded on first use. Category: Acronyms] models. These models specify precisely what information is available and how it should be organized. You will explore how YANG functions in detail in one of the upcoming courses.

Choose each of the key characteristics of NETCONF to learn more:

SSH transport

Secure, encrypted communication on port 830

XML messaging

Structured request/response format

Transactional

Changes can be validated before commitment

YANG-based

All data schema is defined with YANG models

A common way to work with devices over NETCONF is through Python. With its ncclient library, Python makes these interactions simpler by handling the heavy lifting for you.

Fetching structured XML is straightforward with the ncclient library:

from ncclient import manager\
\
\# Connect to device\
with manager.connect(\
host=\'192.168.1.1\',\
port=830,\
username=\'admin\',\
password=\'password\',\
hostkey_verify=False\
) as m:\
\# Get running configuration\
config = m.get_config(source=\'running\')\
print(config)

![Network device sends interface data in XML format showing details such as interface name, type, status, physical address, and packet statistics to an application.](media/image7.bin){width="6.94027668416448in" height="3.1101181102362205in"}

RESTCONF

NETCONF was the first model-driven API, but today, there are several protocols that provide access to the same YANG-modeled data, including gNMI, gRPC, and RESTCONF. Of these, RESTCONF has become especially popular due to its simplicity---it relies on familiar HTTP methods and supports both JSON and XML formats. That makes it more approachable, since JSON maps directly to Python data structures and is often the most familiar format for developers.

Since RESTCONF builds on familiar HTTP methods and JSON, it's also easy to test with tools like Postman or Bruno, which simplify development and troubleshooting. In practice, Python's requests library is commonly used, as it handles REST calls in a way most developers already understand.

Fetching structured JSON is straightforward with the requests library:

from requests import manager\
\
\# Connect to device\
with manager.connect(\
host=\'192.168.1.1\',\
port=830,\
username=\'admin\',\
password=\'password\',\
hostkey_verify=False\
) as m:\
\# Get running configuration\
config = m.get_config(source=\'running\')\
print(config)

![Network device sending JSON formatted interface data, including name, status, address, and packet statistics, to an application.](media/image8.bin){width="6.94027668416448in" height="3.1101181102362205in"}

RESTCONF is a developer-friendly alternative to NETCONF. Click each of the following benefits to learn more:

JSON data format

RESTCONF has JSON support, alongside XML.

Standard HTTP(s) methods.

RESTCONF uses standard HTTP(s) methods to perform create, read, update, and delete (CRUD) operations.

Standard HTTP(s) Python libraries.

With RESTCONF, standard HTTP(s) libraries such as requests can be used.

Integration with modern tools.

Tools like Postman or Bruno make development and troubleshooting much easier.

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 4~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]All these characteristics make APIs a very powerful choice for network automation, and they are widely used. However, keep in mind that not every task you may need is supported, so you may still need to use other tools or write CLI scripts. |
+======================================================================================================================================================================================================================================================+
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. What is the fundamental problem with traditional CLI automation that model-driven APIs (like NETCONF and RESTCONF) are designed to solve, especially concerning software upgrades?

A. CLI commands are too slow to execute.

B. CLI output is designed for humans to read, making it unreliable for programmatic parsing.

C. CLI lacks support for secure communication protocols.

D. CLI does not allow for multi-vendor device management

Ansible Modules for Network Automation

As you continue to evaluate automation approaches, you may consider the complexity of managing Python scripts across your expanding infrastructure. While custom scripts offer flexibility, maintaining them and their configuration can become overwhelming as your network scales up.

Ansible simplifies network automation through pre-built modules that handle common tasks. Instead of writing custom Python code for each device interaction, you define configurations using highly abstracted modules. These modules automatically handle connection details, error parsing, and device-specific syntax.

Designed for simplicity and flexibility, Ansible does not require any agents or daemons on your network devices. Everything is controlled from your management host. Therefore, you can manage hundreds of various devices without worrying about installing or maintaining agents. While Ansible typically connects via SSH, it can also use other methods such as NETCONF or REST APIs when supported by devices.

Key Ansible characteristics include:

-   **YAML syntax:** Human-readable configuration files called playbooks

-   **Idempotent operations:** Safe to run multiple times without side effects

-   **Agentless architecture: No software installation on target devices**

-   **Extensive module library:** Pre-built modules for major network vendors

The Power of Ansible Abstraction

One of the key tasks in your automation journey is deploying configuration changes across your entire network. For instance, suppose you need to add a new ~~VLAN~~ **virtual LAN (VLAN)** [Explanation: Acronym 'VLAN' not expanded on first use. Category: Acronyms] to 50 switches in your retail stores. With traditional automation, you might write a Python script that uses APIs or CLI commands. However, you would need to handle many details yourself, such as:

-   **Connection:** SSH/API session management and error recovery.

-   **Device variations:** Different command syntax across vendors and OS versions.

-   **Error handling:** Custom logic for timeouts, authentication failures, and command errors.

-   **State management:** Tracking what changes were made and handling rollbacks.

Handling these tasks is certainly achievable if you are familiar with Python. You could use libraries like Netmiko for SSH, handle exceptions, and parse outputs.

from netmiko import ConnectHandler\
\
def configure_vlan(host, username, password, vlan_id, vlan_name):\
\
#Describe the target device and credentials for Netmiko to connect\
device = {\
\'device_type\': \'cisco_ios\',\
\'host\': host,\
\'username\': username,\
\'password\': password,\
}\
\
try:\
connection = ConnectHandler(\*\*device)\
\
#Send the VLAN configuration\
commands = \[\
\'configure terminal\',\
f\'vlan {vlan_id}\',\
f\'name {vlan_name}\',\
\'exit\',\
\'exit\'\
\]\
\
output = connection.send_config_set(commands)\
connection.disconnect()\
\
#Simple check\
if \'Invalid\' in output or \'Error\' in output:\
raise Exception(f\"Command failed: {output}\")\
\
except Exception as e:\
print(f\"Configuration failed: {e}\")\
return False\
\
return True

As your network grows and requirements become more complex, maintaining all this custom code becomes increasingly difficult to scale.

Instead of writing hundreds of lines of Python to handle all the underlying complexity, you can write Ansible playbooks. Playbooks are the instructions that define how to configure your infrastructure, written in YAML format. They describe your ~~desired~~ **wanted** [Explanation: 'want' or 'wanted' instead of 'desire/desired'. Category: Cisco Style Guide] outcomes in a simple, readable manner:

![Ansible playbook with tasks including a YAML snippet configuring VLAN 100 named Production.](media/image9.bin){width="6.94027668416448in" height="2.7557534995625548in"}

Ansible playbooks appear much simpler because much of the underlying complexity is handled by Ansible modules. Those modules provide abstraction by allowing you to set only the required parameters. You consult the module documentation to learn~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]parameters are needed, then define your ~~desired~~ **wanted** [Explanation: 'want' or 'wanted' instead of 'desire/desired'. Category: Cisco Style Guide] state. Ansible's core engine then runs the playbook, walks through all defined tasks, and calls the appropriate modules to do the actual work.

Modules are packaged in collections, bundles of related automation content distributed through Ansible Galaxy. For Cisco devices alone, there are collections such as cisco.ios for Cisco Catalyst switches and routers, cisco.nxos for Cisco Nexus switches, and cisco.asa for firewalls. Each collection contains dozens of specialized modules for various configuration tasks.

![Ansible core connects to Cisco collections including cisco dot aci, cisco dot nxos, cisco dot ios, and cisco dot asa to manage network devices.](media/image10.bin){width="6.940277777777778in" height="4.032728565179353in"}

Using these modules, Ansible handles SSH connections, command syntax variations, error parsing, and idempotency automatically, eliminating hundreds of lines of boilerplate code.

Click each of the advantages of Ansible\'s approach to learn more:

Idempotency

Running the same playbook multiple times produces the same result.

Easy-to-Read Playbooks

Playbooks use high-level YAML definitions instead of Python code.

Self-Documenting Configuration

Configuration intent is clear from YAML structure.

+--------------------------------------------------------------------------------------------------------+
| 5~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]These advantages depend on module quality---poorly written modules may not deliver these benefits. |
+========================================================================================================+
+--------------------------------------------------------------------------------------------------------+

However, modules have a critical limitation: if a module does not support your specific use case or behaves unexpectedly, you\'re stuck. Unlike custom Python scripts where you can modify the code, Ansible modules are black boxes. When they fail or lack features, you must either find workarounds, wait for updates, or abandon Ansible for that particular task. Alternatively, you can create your own module to address the issue and contribute it back to the Ansible community, benefiting others as well..

~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. Which tool is best suited for maintaining configuration consistency across large environments or for teams that want to avoid writing custom code, by using simple, human-readable files?

A. Python CLI scripts

B. Model-driven APIs

C. Ansible Modules

D. Terraform

~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. Which of the following two characteristics are described as key characteristics of Ansible for network automation? (Choose two)

A. It ~~utilizes~~ **uses** [Explanation: 'use' instead of 'utilize'. Category: Cisco Style Guide] YAML syntax for its configuration files (playbooks).

B. It requires agents to be installed on the network devices it manages.

C. Its operations are designed to be idempotent.

D. It primarily relies on model-driven APIs like NETCONF for all device interactions.

E. It compiles playbooks into optimized binaries for deployment on network devices.

Terraform for Network Automation

As you continue exploring automation options, you have seen how APIs provide structured data access and how Ansible offers pre-built modules for common tasks. Now, you are considering Terraform, a tool frequently mentioned by colleagues on the cloud team. They claim it has revolutionized how they manage cloud infrastructure, but you remain skeptical. Can a cloud-centric tool really work for network devices? You decide to investigate whether Terraform\'s approach offers something unique for network automation.

Terraform takes a different approach to automation by focusing on the ~~desired~~ **wanted** [Explanation: 'want' or 'wanted' instead of 'desire/desired'. Category: Cisco Style Guide] end state rather than specific commands or tasks to execute. Instead of writing scripts that run commands or playbooks that perform tasks, you describe what your infrastructure should look like, and Terraform figures out how to achieve that configuration.

Choose the following key characteristics of Terraform to discover more:

Declarative configuration

Define what infrastructure should look like

State management

Track actual vs ~~desired~~ **wanted** [Explanation: 'want' or 'wanted' instead of 'desire/desired'. Category: Cisco Style Guide] configuration

Plan and apply workflow

Preview changes before execution

Provider ecosystem

Pre-built integrations with network platforms

Understanding Terraform\'s approach can help you determine whether its state-based management model fits your network automation needs.

Terraform Providers

Terraform uses simple declarative configuration files that are written in HashiCorp Configuration Language (HCL). In the configuration file, you describe your ~~desired~~ **wanted** [Explanation: 'want' or 'wanted' instead of 'desire/desired'. Category: Cisco Style Guide] infrastructure state as shown in this example:

resource \"iosxe_vlan\" \"production-vlan\" {\
vlan_id = 100\
name = \"Production\"\
}

This HCL configuration tells Terraform that you want a VLAN 100 called PRODUCTION. But how does Terraform actually create that VLAN on your Cisco switch? Here is where providers come in.

Think of providers as translators. Each provider is a plugin that knows how to communicate with a specific platform\'s API. The Cisco IOS XE Software provider translates your HCL into RESTCONF API calls. The Cisco ACI provider speaks to the Cisco ACI controller\'s REST API. The Cisco Meraki provider talks to the Cisco Meraki Dashboard API. Each provider understands both the HCL language and the target platform\'s specific requirements.

When you run Terraform, it reads your HCL files, determines what changes are needed, and then uses the appropriate provider to make those API calls. The provider handles all the complexity, including authentication, API formatting, and error handling, while you focus on describing what you want.

The key advantage of this architecture is that nothing needs to be installed on your network devices. Terraform and its providers run separately from your infrastructure, communicating through existing management APIs. Your switches and routers do not need any agents or additional software. They need to have their APIs enabled, which most modern devices already support.

Declarative Network Management

With Terraform, you describe what you want your network to look like, not how to configure it. This fundamentally changes how you approach network automation. Instead of writing step-by-step instructions, you define your ~~desired~~ **wanted** [Explanation: 'want' or 'wanted' instead of 'desire/desired'. Category: Cisco Style Guide] end state and let Terraform figure out how to get there.

Traditional automation approaches focus on executing specific actions:

-   **CLI scripts:** Send commands via SSH in exact order

-   **API scripts:** Make REST or NETCONF calls to configure devices

-   **Ansible playbooks:** Define tasks that execute sequentially

All these approaches require you to think about the \"how.\" You must specify each command, handle the responses, manage the order of operations, and deal with errors. Even when Ansible modules provide abstraction, your playbook still defines a sequence of tasks to perform.

Terraform takes a completely different approach. Observe how each method handles creating an access control list (ACL) and applying it to an interface, by expanding each of the methods:

Python CLI Script

  -----------------------------------------------------------------------
  \# send each required command\
  device.send_command(\"configure terminal\")\
  device.send_command(\"ip access-list standard SACL1\")\
  device.send_command(\"10 deny 10.0.0.0 0.0.0.255 log\")\
  device.send_command(\"exit\")\
  device.send_command(\"interface GigabitEthernet3\")\
  device.send_command(\"ip access-group SACL1 in\")

  -----------------------------------------------------------------------

Ansible Playbook

  -----------------------------------------------------------------------
  \# tasks that execute in defined order\
  - name: Configure standard ACL SACL1\
  cisco.ios.ios_acls:\
  config:\
  - afi: ipv4\
  acls:\
  - name: SACL1\
  acl_type: standard\
  aces:\
  - sequence: 10\
  grant: deny\
  source:\
  address: 10.0.0.0\
  wildcard_bits: 0.0.0.255\
  state: merged\
  \
  - name: Apply ACL to GigabitEthernet3\
  cisco.ios.ios_acl_interfaces:\
  config:\
  - name: GigabitEthernet3\
  access_groups:\
  - afi: ipv4\
  acls:\
  - name: SACL1\
  direction: in\
  state: merged

  -----------------------------------------------------------------------

Terraform Configuration

  -----------------------------------------------------------------------
  \# ~~desired~~ **wanted** [Explanation: 'want' or 'wanted' instead of 'desire/desired'. Category: Cisco Style Guide] state definition\
  resource \"iosxe_access_list_standard\" \"deny-guest\" {\
  name = \"SACL1\"\
  entries = \[\
  {\
  sequence = 10\
  deny_prefix = \"10.0.0.0\"\
  deny_prefix_mask = \"0.0.0.255\"\
  deny_log = true\
  }\
  \]\
  }\
  \
  resource \"iosxe_interface_ethernet\" \"example\" {\
  type = \"GigabitEthernet\"\
  name = \"~~3~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\"\
  ipv4_address = \"15.1.1.1\"\
  ipv4_address_mask = \"255.255.255.252\"\
  ip_access_group_in_enable = true\
  ip_access_group_in = \"SACL1\"\
  }

  -----------------------------------------------------------------------

With Terraform, you never specify the order of operations or how to create these resources. You just describe what should exist.

This freedom from sequencing means that you can organize your infrastructure definitions in whatever way makes the most sense for your team. For example, you could keep all ACLs in an **acls.tf** file, all interfaces in **interfaces.tf**, and all VLANs in **vlans.tf**. Alternatively, you could organize by network zones with **dmz.tf**, **campus.tf**, and **~~datacenter~~ **data center** [Explanation: 'data center' (two words) instead of 'datacenter'. Category: Cisco Style Guide].tf**. Since Terraform analyzes all files collectively and automatically determines dependencies, the file organization is solely for human readability. The order of files and the resources within them does not matter.

This declarative approach is possible because of persistent state tracking. When you run a Python script or Ansible playbook, the tool executes your commands and exits with no memory of what it did. Terraform maintains a state file that records everything it manages.

This state tracking enables Terraform to compare your Terraform definition files (\*.tf) with the current state (terraform.tfstate) and calculate exactly what changes are required. Terraform always knows both the intended configuration and what currently exists, ensuring it applies only the necessary changes. Whether you\'re adding, modifying , or removing resources from your configuration files, Terraform updates your infrastructure to match your ~~desired~~ **wanted** [Explanation: 'want' or 'wanted' instead of 'desire/desired'. Category: Cisco Style Guide] state. This stateful workflow is described in the following figure.

![Terraform workflow showing how it compares dot tf files with terraform dot tfstate to update network infrastructure to the ~~desired~~ **wanted** [Explanation: 'want' or 'wanted' instead of 'desire/desired'. Category: Cisco Style Guide] state.](media/image11.bin){width="6.940277777777778in" height="5.192588582677165in"}

Scripts and playbooks execute without knowledge of previous runs. Terraform\'s state awareness means that it always knows the intended configuration and automatically calculates what changes are needed to achieve it.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 6~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]While Ansible resource modules check the current state before making changes (achieving idempotency), they do not track the state. Unlike Terraform\'s persistent state file, Ansible has no memory of previous executions |
+================================================================================================================================================================================================================================+
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Terraform has some unique advantages that make it a powerful tool for network automation. Click each advantage to learn more:

State Tracking

Persistent memory of what Terraform deployed, enabling drift detection

Declarative Configuration

You describe the ~~desired~~ **wanted** [Explanation: 'want' or 'wanted' instead of 'desire/desired'. Category: Cisco Style Guide] end state, Terraform figures out how to get there

Safe Changes

Preview exactly what will change before applying with terraform plan

Self-documenting

Network infrastructure is described in readable HCL configuration files.

However, Terraform has a critical limitation, you can only manage what providers support. If a provider does not expose a specific device feature or configuration option, you simply cannot manage it through Terraform.

In addition, the quality and completeness of providers vary significantly. While major platforms have well-maintained providers, many vendors lag in provider development, leaving gaps in functionality. When you encounter these limitations, you need to complement Terraform with other tools.

~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. Which of the following two characteristics are key characteristics or advantages of Terraform for network automation? (Choose two)

A. It requires agents to be installed directly on the network devices it manages.

B. It focuses on defining the ~~desired~~ **wanted** [Explanation: 'want' or 'wanted' instead of 'desire/desired'. Category: Cisco Style Guide] end state of the network infrastructure.

C. Its primary method for configuring devices involves sending sequential CLI commands via SSH.

D. It ensures a full, automatic rollback of all changes if any part of the deployment fails

E. It maintains a persistent state file to track the actual versus ~~desired~~ **wanted** [Explanation: 'want' or 'wanted' instead of 'desire/desired'. Category: Cisco Style Guide] configuration.

CLI Scripting with Python

As you continue evaluating automation approaches for your retail chain, you realize that not every problem requires a complex solution. Your network operations team handles dozens of small, urgent tasks each day---rebooting misbehaving access points, collecting debug outputs during incidents, and running vendor-specific commands that no APIs support. In these real-world scenarios, CLI scripting often offers the most practical path forward.

CLI scripting with Python sends commands via SSH exactly as you would type them manually. While APIs offer structured data and tools like Ansible provide useful abstractions, CLI scripting gives you direct, immediate access to every command on every device. CLI scripting is often the quickest way to resolve issues.

When working with network devices, CLI scripting offers a fast and flexible way to automate tasks. The following key characteristics show why it is a valuable complement to other automation tools, helping you solve immediate problems efficiently. Click each one to learn more:

Direct Execution

Run any command without waiting for API support.

Simple Implementation

A basic Python script gets you started in minutes.

Complete Access

Every CLI command and debug feature available

Minimal Overhead

No agents, no frameworks, just SSH and Python

When to Use CLI Scripts?

Sometimes, CLI scripting is simply the easiest approach. When you know the commands well and there\'s minimal output to parse, why complicate things? This is especially true when you\'re deeply familiar with CLI commands but less experienced with YANG models and APIs.

Some operations are actually more difficult to accomplish through APIs. Device reboots and software upgrades often involve interactive prompts such as \"Proceed with reload? \[confirm\]\" or \"This will interrupt service. Continue? \[y/n\].\" These multi-step confirmations are straightforward in CLI scripting but can be complicated to handle through APIs.

Imagine that you are testing new features on a dedicated network and often need to reboot 20 access points between tests.

With CLI scripting, this task is made simple:

from netmiko import ConnectHandler\
\
test_aps = \[\'10.99.1.10\', \'10.99.1.11\', \'10.99.1.12\', \'\...\'\]\
\
for ap in test_aps:\
device = {\
\'device_type\': \'cisco_ios\',\
\'host\': ap,\
\'username\': \'admin\',\
\'password\': \'password\',\
}\
\
conn = ConnectHandler(\*\*device)\
conn.send_command(\'reload\', expect_string=\'confirm\')\
conn.send_command(\'\')\
print(f\"{ap}: Rebooting\")

Python Libraries for CLI Scripting

The Python ecosystem provides excellent libraries that handle the SSH complexity, letting you focus on what commands to run rather than how to run them. Two very popular examples are:

-   Netmiko

-   pyATS

Netmiko is the go-to library for most network engineers. It handles login sequences and prompt detection, command timing and output waiting, enable mode and config mode transitions, and various vendor quirks and behaviors. This ~~allows you to~~ **lets you** [Explanation: 'lets you' instead of 'allows you to'. Category: Cisco Style Guide] focus on~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]commands to run rather than how to run them.

In the following example, you can see how you can execute CLI commands using Netmiko.

from netmiko import ConnectHandler\
\
device = {\
\'device_type\': \'cisco_ios\',\
\'host\': \'192.168.1.1\',\
\'username\': \'admin\',\
\'password\': \'password\',\
}\
\
with ConnectHandler(\*\*device) as conn:\
output = conn.send_command(\'show version\')\
print(output)

Another Python tool, pyATS, is a modern alternative to Netmiko. Originally developed by Cisco as a comprehensive testing framework, pyATS has since gained popularity among network engineers for general automation tasks. While it includes advanced features for test automation that you will explore later, it also offers a straightforward way to connect to devices and execute CLI commands.

In the following example, you can see how you can execute CLI commands using pyATS.

from genie.testbed import load\
\
testbed = load(\'testbed.yaml\')\
device = testbed.devices\[\'router1\'\]\
device.connect()\
\
output = device.execute(\'show version\')\
print(output)

Parsing CLI Output

The main challenge with CLI scripting is parsing human-readable output. Without python libraries, you have to parse raw CLI manually. The following is an example of raw CLI output.

output = conn.send_command(\'show interfaces GigabitEthernet0/1\')\
\
GigabitEthernet0/1 is up, line protocol is up\
Hardware is Gigabit Ethernet, address is 0024.f7dd.7741\
Internet address is 10.1.1.1/24\
MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec\
reliability 255/255, txload ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]/255, rxload ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]/255\
~~5~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] minute input rate 3000 bits/sec, ~~5~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] packets/sec\
~~5~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] minute output rate 2000 bits/sec, ~~3~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] packets/sec\
144553 packets input, 18752330 bytes\
122456 packets output, 15643867 bytes

Fortunately, there are Python libraries that can help. One of the most popular options is the pyATS Genie parsers, which transform CLI output into structured data. Below is an example of a structured CLI output:

output = device.parse(\'show interfaces GigabitEthernet0/1\')\
\
{\
\'GigabitEthernet0/1\': {\
\'oper_status\': \'up\',\
\'line_protocol\': \'up\',\
\'hardware_type\': \'Gigabit Ethernet\',\
\'mac_address\': \'0024.f7dd.7741\',\
\'ipv4\': {\'10.1.1.1\': {\'prefix_length\': 24}},\
\'counters\': {\
\'in_pkts\': 144553,\
\'in_octets\': 18752330,\
\'out_pkts\': 122456,\
\'out_octets\': 15643867\
}\
}\
}

Key Takeaways

Take a moment to reflect upon the following key takeaways on CLI scripting. Click each takeaway to check your understanding:

Practical Solutions

CLI scripting often provides the fastest path from problem to solution, especially for simple tasks.

Universal Access

Works with every network device that supports SSH, regardless of vendor or model.

Modern Tools Help

Libraries like Netmiko and parsers like Genie eliminate most traditional CLI scripting pain points.

Complementary Approach

CLI scripts work alongside APIs, Ansible, and Terraform, not as a replacement but as another tool in your toolkit.

By embracing CLI scripting for certain tasks, you can solve problems quickly and efficiently while keeping your automation architecture simple and maintainable.

~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. What is identified as the main challenge when using CLI scripting with Python for network automation?

A. The inability to establish secure SSH connections to devices.

B. The requirement for complex frameworks and agents on target devices.

C. Reliably parsing human-readable output, which can be inconsistent or change with software updates.

D. A lack of Python libraries available to simplify CLI interactions.

Cisco Automation Platforms

As you continue your network automation journey for the retail chain, you face a fundamental decision: should you build custom automation applications or adopt existing vendor controller platforms? After evaluating APIs, Ansible playbooks, and Terraform configurations, you realize these tools still require extensive custom logic to orchestrate complex workflows. This leads you to consider enterprise-grade controller platforms that offer prebuilt automation capabilities.

Take your current challenge: 500 stores, each with ~~4~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] to ~~5~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] switches---approximately ~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation],500 devices. Even a simple task, like adding a new VLAN, becomes a major project. With Ansible, you have to manage inventory files, handle partial failures, and track~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]stores succeeded versus those~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]required a retry. And that is just for VLANs. Now imagine upgrading IOS on all those switches. You would need scripts to check current versions, verify hardware compatibility, schedule maintenance windows, transfer images, monitor reboots, verify services are restored, and handle inevitable failures.

Understanding Controller Platforms

Vendors observed that thousands of customers were repeatedly building the same automation solutions and decided to provide their own. Instead of everyone writing custom scripts to manage VLANs, upgrade software, or configure security policies, vendors developed comprehensive platforms that handle these operations ~~out of the box~~ **Change 'out of the box' to 'out-of-the-box'** [Explanation: Hyphenate 'out-of-the-box' when used as a compound modifier. Category: Grammar & Punctuation].

Think of them as pre-built automation applications that vendors have already developed, tested, and refined through years of deployment. Those platforms interpret your business intent and translate it into network changes.

Network controllers represent a fundamental shift in automation. Instead of configuring each device individually, you simply specify your ~~desired~~ **wanted** [Explanation: 'want' or 'wanted' instead of 'desire/desired'. Category: Cisco Style Guide] outcome to the controller , and it determines~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]devices require configuration.

Consider the following scenario: You need to deploy a guest network across 50 stores.

Without a controller, you need to build a script that will:

-   Connect to all the switches.

-   Check current VLAN configuration on each.

-   Create new VLAN.

-   Configure access and trunk ports.

-   Handle failures (what if ~~3~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] switches are unreachable?)

With a controller, your script would only need to:

-   Create a \"Guest Network\" policy in the controller.

-   Apply it to the \"Northeast Region\" store group.

-   Controller handles everything else.

The controller knows your network topology, manages the device connections, handles errors and retries, provides audit logs, and ensures consistency.

Northbound APIs and Automation

While controllers provide user-friendly graphical interfaces, their true automation power lies in northbound APIs. This approach ~~allows you to~~ **lets you** [Explanation: 'lets you' instead of 'allows you to'. Category: Cisco Style Guide] build scripts that only talk to the controller and define new intents, rather than configuring each affected device individually.

One API call can replace hundreds of lines of code:

controller_api.create_policy(\
name=\"Guest Network\",\
sites=\[\"Store_001\", \"Store_050\"\],\
vlan_id=999,\
security_level=\"guest\"\
)

Cisco Controller Portfolio

Cisco offers several controller platforms, each targeting specific use cases. Click each one to discover more:

Catalyst Center

Management and automation platform for enterprise networks. It provides automation features like bulk configuration, zero-touch provisioning, software image management, and policy-based enforcement. This makes it easier to keep the network consistent, secure, and reliable.

Cisco Identity Services Engine (ISE)

A network access control and policy platform developed by Cisco, it helps you control who and what connects to your network. It also supports policy-based ~~access, guest and bring~~ **Add comma before 'and' (e.g., 'A, B, and C')** [Explanation: adding serial comma before 'and' in list of three or more.... Category: Grammar & Punctuation] your own device (BYOD) management, and integrates with security tools to detect and contain threats.

Cisco Meraki Dashboard

A cloud-managed ~~IT~~ **Information Technology (IT)** [Explanation: Acronym 'IT' not expanded on first use. Category: Acronyms] platform from Cisco. It lets you manage switches, firewalls, or wireless access points, from a single web-based dashboard.

Cisco ACI

Data center software-defined networking (SDN) solution using an application-focused approach. It is best suited for modern data centers and is not typically used for campus or branch networks. In Cisco ACI, you define what applications need (bandwidth, security, connectivity), ACI figures out the network configuration.

Across all these platforms, Cisco provides APIs that enable automation of the features described above.

When to Use Controller Platforms?

Controller platforms can save significant time by handling common networking tasks through prebuilt logic and automation. The key benefit is their focus upon business intent rather than technical configuration. Instead of configuring VLANs, ACLs, and routing protocols, you simply define intents. Controllers translate these intentions into actual device configurations across your entire infrastructure.

However, there are still some considerations to take into account before choosing a controller platform:

Cost

Licensing for 2500 devices is not cheap. You will need to justify the investment against the cost of developing and maintaining custom automation.

Capability Gaps

Controllers excel at common use cases but struggle with unique requirements. When you have a requirement that is unsupported, you are back to custom scripts.

Learning Curve

Your team\'s CLI expertise does not directly transfer to working with newtwork controllers. Controllers have their own concepts, terminology, and operational models that take time to become proficient in.

Many organizations use controllers for standard operations and custom automation for everything else. For example, you could use Catalyst Center to manage software upgrades and standard configurations and ISE to handle security policies. But that weird integration with your legacy phone system? That is still a Python script.

Understanding all automation approaches, from CLI scripting to controllers, enables you to pick the right tool for each challenge. Through the following courses you will get hands-on practice with all these options so that you can see~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]work best for you.

~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. What is identified as a key benefit of using Cisco Automation Platforms compared to building custom automation scripts?

A. They eliminate the need for any network device APIs.

B. They allow a focus on business intent rather than detailed technical device configurations.

C. They are always free to use and require no licensing.

D. They are primarily designed for single-device automation tasks.

Summary

You've explored the options for automating your network: CLI scripting (Netmiko/pyATS), model-driven APIs, Ansible, Terraform, and controller platforms. You now understand the basics of each approach and the benefits and trade-offs of different tools. In other words, you are now the go-to person for planning the next automation steps and discussing viable possibilities.

To dive deeper and start building real automation solutions, explore the courses available as you continue your learning journey with Cisco U:

-   Network Task Automation with Python

-   REST APIs in Network Automation

-   Network Automation with RESTCONF

-   Network Automation with Ansible

-   Network Automation with Terraform

Summary Challenge

~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. What is considered the most important factor when selecting automation tools for a large, multivendor network?

A. Choosing tools that your engineers will actually use and maintain.

B. Ensuring every tool comes from the same vendor for maximum compatibility.

C. Selecting the most advanced platform with artificial intelligence capabilities for future growth.

D. Implementing every available automation tool simultaneously to cover all potential use cases.

~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. What main problem do model-driven APIs such as NETCONF and RESTCONF solve compared to traditional CLI automation?

A. CLI commands are too slow to execute on modern network devices.

B. APIs eliminate the need for authentication and security controls during automation.

C. CLI output is designed for humans to read, making it unreliable for programmatic parsing.

D. They enable developers to create entirely new device operating systems instead of using existing ones.

~~3~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. What makes Ansible particularly suitable for maintaining configuration consistency across large environments?

A. It requires agents on all managed devices, ensuring real-time synchronization.

B. It compiles device configurations into encrypted machine binaries for faster deployment.

C. It automatically generates Python scripts from every playbook to maintain a full audit trail.

D. It defines infrastructure through simple, human-readable YAML files that describe the ~~desired~~ **wanted** [Explanation: 'want' or 'wanted' instead of 'desire/desired'. Category: Cisco Style Guide] state.

~~4~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. Which two characteristics describe Ansible's core design for network automation? (Choose two.)

A. It ~~utilizes~~ **uses** [Explanation: 'use' instead of 'utilize'. Category: Cisco Style Guide] YAML syntax for playbooks.

B. It must install an agent on every target device to operate correctly.

C. It depends exclusively on model-driven APIs for every supported platform.

D. Its operations are idempotent, producing the same result even after repeated runs.

E. It dynamically generates provider configuration files during each run for state tracking.

~~5~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. Which statement best explains how Terraform differs from Ansible or Python scripting?

A. Terraform executes device-specific CLI commands line by line for precise control.

B. Terraform requires additional agents to maintain persistent SSH connections to all devices.

C. Terraform uses proprietary APIs available only on Cisco devices to enforce compliance policies.

D. Terraform defines the ~~desired~~ **wanted** [Explanation: 'want' or 'wanted' instead of 'desire/desired'. Category: Cisco Style Guide] end state of the infrastructure and calculates the required changes automatically.

~~6~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. What is identified as the main challenge when using CLI scripting for network automation?

A. Reliably parsing human-readable output that can vary with software versions.

B. Inability to perform commands on multiple devices simultaneously.

C. Requirement to rewrite all Python code after every firmware update.

D. Limited compatibility with SSH and Telnet protocols.

~~7~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]\. What is a key benefit of using Cisco Automation Platforms compared to building custom scripts?

A. They completely eliminate the need for APIs or any external automation logic.

B. They are designed exclusively for testing environments and small lab deployments.

C. They provide automation but cannot integrate with other tools like Ansible or Terraform.

D. They allow engineers to focus on business intent rather than device-level configuration details.

Answer Key

Network Automation Tools Overview

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]A, B, D

Model-Driven APIs for Network Automation

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]B

Ansible Modules for Network Automation

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]C

2~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]A, C

Terraform for Network Automation

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]B, E

CLI Scripting with Python

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]C

Cisco Automation Platforms

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]B

Summary Challenge

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]A

2~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]C

3~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]D

4~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]A, D

5~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]D

6~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]A

7~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]D


---

## Change Legend

| Markup | Meaning |
|--------|---------|
| ~~text~~ | Text to remove (strikethrough) |
| **text** | Text to add (bold) |
| [Explanation: ...] | Rationale for change |

*Generated by Course AI Editor on 2026-03-04 15:15*