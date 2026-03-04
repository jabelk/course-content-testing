# Inline Editorial Review: 02_SD-WAN Components and Roles_orig

**Instructions**: Search for `~~` to find deletions and `**` to find additions.
Copy this document into Word to see Track Changes formatting.

---

**Total Changes**: 348 (Auto-fix: 178, Review: 87, Questions: 83)

---

En-sdwan-30-componentroles

SD [QUESTION: Unknown acronym 'SD' - please provide expansion or confirm intentional. Category: Acronyms]-~~WAN~~ **Wide Area Network (WAN)** [Explanation: Acronym 'WAN' not expanded on first use. Category: Acronyms] Components and Roles

Student Guide

Version Number

Part Number

Copyright Notices

© 2025 ~~Cisco Systems~~ **Cisco** [Explanation: 'Cisco' instead of 'Cisco Systems'. Category: Cisco Style Guide], Inc.

© 2025 ~~Cisco Systems~~ **Cisco** [Explanation: 'Cisco' instead of 'Cisco Systems'. Category: Cisco Style Guide], Inc.

![](media/image1.bin){width="0.9677416885389326in" height="0.5161286089238846in"}

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------- --------------------------------------------
  **Americas Headquarters**\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        **Asia Pacific Headquarters**\   **Europe Headquarters**\
  ~~Cisco Systems~~ **Cisco** [Explanation: 'Cisco' instead of 'Cisco Systems'. Category: Cisco Style Guide], Inc.\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              ~~Cisco Systems~~ **Cisco** [Explanation: 'Cisco' instead of 'Cisco Systems'. Category: Cisco Style Guide] (USA) Pte. Ltd.\   ~~Cisco Systems~~ **Cisco** [Explanation: 'Cisco' instead of 'Cisco Systems'. Category: Cisco Style Guide] International BV Amsterdam,\
  San Jose, CA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      Singapore                        The Netherlands

  Cisco has more than 200 offices worldwide. Addresses, phone numbers, and fax numbers are listed on the Cisco website at <http://www.cisco.com/go/offices>~~.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]

  Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S. and other countries. To view a list of Cisco trademarks, go to this URL:<http://www.cisco.com/c/en/us/about/legal/trademarks.html>. Third-party trademarks that are mentioned are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (1110R)                                                                                                                                                                                                                                                                                          

  DISCLAIMER WARRANTY: THIS CONTENT IS BEING PROVIDED "AS IS" AND AS SUCH MAY INCLUDE TYPOGRAPHICAL, GRAPHICS, OR FORMATTING ERRORS. CISCO MAKES AND YOU RECEIVE NO WARRANTIES IN CONNECTION WITH THE CONTENT PROVIDED HEREUNDER, EXPRESS, IMPLIED, STATUTORY OR IN ANY OTHER PROVISION OF THIS CONTENT OR COMMUNICATION BETWEEN CISCO AND YOU. CISCO SPECIFICALLY DISCLAIMS ALL IMPLIED WARRANTIES, INCLUDING WARRANTIES OF MERCHANTABILITY, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE, OR ARISING FROM A COURSE OF DEALING, USAGE OR TRADE PRACTICE. This learning product may contain early release content, and while Cisco believes it to be accurate, it falls subject to the disclaimer above~~.                                    ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------- --------------------------------------------

Course Welcome

Thank you for choosing Cisco as your technical learning provider. We recognize that you have many options to choose from when working toward achieving your technical and professional goals. Our objective is to help you meet those goals by providing high-quality, collaborative learning experiences.

Before you begin, take a moment to review the primary components in this course, how to access online support, and opportunities to provide feedback on the course.

**Course outline:** If you are attending a live, instructor-led training session, your instructor may customize the course to meet the specific needs of the class. However, you will find a basic outline of the material in the *Course Introduction* section.

**Course content:** You will find detailed information and instructions along with supporting illustrations, self-check challenges to give you exam practice, and lab activities to give you a real-world experience.

**Bias-Free language:** Cisco is updating content to be free of offensive or suggestive language. We are changing terms such as ~~blacklist~~ **blocked list** [Explanation: 'blocked list' instead of 'blacklist' (bias-free language). Category: Cisco Style Guide]/~~whitelist~~ **allowed list** [Explanation: 'allowed list' instead of 'whitelist' (bias-free language). Category: Cisco Style Guide] and ~~master~~ **Consider using 'primary/secondary' or 'active/standby' instead** [Explanation: 'primary/secondary' or 'active/standby' instead of 'maste.... Category: Cisco Style Guide]/~~slave~~ **Consider using 'primary/secondary' or 'active/standby' instead** [Explanation: 'primary/secondary' or 'active/standby' instead of 'maste.... Category: Cisco Style Guide] to more appropriate alternatives. While we update our portfolio of products and content, users may see differences between some content and a product's user interface or command syntax. Please use your product's current terminology as found in its documentation.

**Online support:** Join the [Cisco Learning Network](https://learningnetwork.cisco.com/community/learning_center/featured-groups) community to participate in study group discussions and get answers to questions as you prepare for your exam.

**Your feedback:** We encourage you to submit feedback so that we can continue to improve course quality and offer the best learning products possible. Your input is valuable to us, and we want to know how the course has helped with your job and exam performance. There are two ways to submit feedback:

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]**Course evaluation survey:** If you attend a live, instructor-led training session, then your instructor will provide a survey on the last day of class. After completing the survey, you\'ll receive a course completion certificate. Once you\'ve had a chance to practice what you\'ve learned, you'll receive a follow-up survey approximately two months after completing the course.

2~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]**Digital kit feedback:** Use the Feedback button in the digital version of the course materials to submit your comments.

We make regular updates to our content in response to your feedback, so please share it with us.

Special thanks to our Cisco Authorized Learning Partners in making these materials available.

Thank you again for choosing Cisco.

Table of Contents

[[Section 1: Cisco Catalyst SD-WAN Components and Roles [~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]](#_Toc215687654)](#_Toc215687654)](#_Toc496778511)

[[Controllers and Validators [~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]](#_Toc215687655)](#_Toc215687655)](#_Toc496778511)

[[SD-WAN Manager [~~7~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]](#_Toc215687656)](#_Toc215687656)](#_Toc496778511)

[[WAN Edge Routers: Physical~~ & ~~ **Change '&' to 'and'** [Explanation: 'and' instead of '&' in prose text. Category: Grammar & Punctuation]Virtual [15](#_Toc215687657)](#_Toc215687657)](#_Toc496778511)

[[Overlay Management Protocol (OMP): The Control Plane Glue [21](#_Toc215687658)](#_Toc215687658)](#_Toc496778511)

[[Cisco Catalyst SD-WAN: Orchestration~~ & ~~ **Change '&' to 'and'** [Explanation: 'and' instead of '&' in prose text. Category: Grammar & Punctuation]Control - Bringing the Fabric to Life [24](#_Toc215687659)](#_Toc215687659)](#_Toc496778511)

[[Lab 1: Access and Monitor Cisco Catalyst SD-WAN Components [25](#_Toc215687660)](#_Toc215687660)](#_Toc496778511)

[[Summary [57](#_Toc215687661)](#_Toc215687661)](#_Toc496778511)

[[Summary Challenge [59](#_Toc215687662)](#_Toc215687662)](#_Toc496778511)

[[Answer Key [60](#_Toc215687663)](#_Toc215687663)](#_Toc496778511)

[\
](#_Toc496778511)

[[]{#_Toc215687654 .anchor}Section 1: Cisco Catalyst SD-WAN Components and Roles](#_Toc496778511)

[Introduction](#_Toc496778511)

[You successfully navigated the foundational concepts of Cisco Catalyst SD-WAN and understand its transformative power over traditional WANs. Now, it\'s time to explore the architecture that makes this transformation possible. Imagine you\'re tasked with constructing this modern network from the ground up. You need to understand the specialized components that act as the brains, nervous system, and gatekeepers of the SD-WAN fabric. You need to move beyond theory and understand the critical components that serve as the brains, nervous system, and gatekeepers of the SD-WAN fabric. How do these specialized elements orchestrate secure device onboarding, distribute policies, and manage routing across a dynamic, distributed environment?](#_Toc496778511)

  ------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Real-world scenario icon.](media/image2.bin){width="0.9741929133858268in" height="0.9741929133858268in"}](#_Toc496778511)   [How would you explain the distinct roles of the SD-WAN Controller, Validator, and Manager to a new team member, emphasizing their individual contributions to the overall fabric?](#_Toc496778511)

  ------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[This course will introduce you to the core orchestrators and managers that bring the Cisco Catalyst SD-WAN vision to life, enabling you ~~to confidently navigate~~ **Consider moving the adverb (e.g., 'to quickly configure' → 'to configure quickly')** [Explanation: avoiding split infinitives when possible. Category: Grammar & Punctuation] its architecture.](#_Toc496778511)

[In this course, you will learn:](#_Toc496778511)

-   
-   
-   

[The critical role of Cisco Catalyst SD-WAN Controllers responsible for centralizing the control plane, distributing policies, and managing routing.The distinct responsibilities of Cisco Catalyst SD-WAN Validators in device authentication and secure onboarding.The operational benefits of centralized management provided by Cisco Catalyst SD-WAN Manager for provisioning, monitoring, and troubleshooting.](#_Toc496778511)

[Your journey begins by uncovering how each SD-WAN component works in concert to orchestrate secure, agile, and intelligent connectivity across your enterprise network.](#_Toc496778511)

[[]{#_Toc215687655 .anchor}Controllers and Validators](#_Toc496778511)

[In the evolving landscape of WAN, understanding the foundational components that drive Cisco Catalyst SD-WANis paramount. Just as a complex organism relies on its brain and nervous system to function, the Cisco Catalyst SD-WAN fabric depends on specialized components to orchestrate its intelligent behavior.](#_Toc496778511)

  ------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Real-world scenario icon.](media/image3.bin){width="0.9741929133858268in" height="0.9741929133858268in"}](#_Toc496778511)   [This topic examines the two critical \"brains\" of the Cisco Catalyst SD-WAN architecture: the SD-WAN Controllers and SD-WAN Validators. These elements are central to the control plane, ensuring secure device onboarding, policy distribution, and the overall orchestration of your overlay network.](#_Toc496778511)

  ------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[The Coordinators of Intelligence: Cisco Catalyst SD-WAN Controllers](#_Toc496778511)

[The Cisco Catalyst SD-WAN Controllers serve as the central nervous system of your SD-WAN fabric, embodying the core intelligence that differentiates this modern WAN solution from traditional architectures. Their primary objective is to coordinate the entire overlay network, ensuring seamless communication and consistent policy enforcement across all connected devices.](#_Toc496778511)

[The following figure illustrates the Cisco Catalyst SD-WAN Control Plane, showcasing the roles of Controllers, Validators, and Manager in distributing policies and managing the secure data plane.](#_Toc496778511)

[![Network diagram illustrating the Control Plane. A cloud contains a Validator, Manager, and Controllers. A text box describes the Control Plane as a virtual machine that distributes data plane policies, implements control plane policies, acts like a B G P route reflector, and manages the secure data plane between W A N Edge Routers. W A N Edge Routers at Cloud, Data Center, Campus, Branch, and CoLo sites connect to M P L S, 4 G, and I N E T transports, which in turn connect to the Controllers.](media/image4.bin){width="6.94027668416448in" height="3.715274496937883in"}](#_Toc496778511)

[At their core, Controllers are responsible for:](#_Toc496778511)

-   

[**Control Plane Coordination**: They establish and maintain the control plane of the SD-WAN fabric, managing the flow of routing and policy information. This centralized approach dramatically reduces the complexity typically associated with distributed routing protocols in large-scale networks.](#_Toc496778511)

-   

[**Policy Distribution**: Controllers act as the single source of truth for all networkwide policies. They distribute data plane and application-aware routing policies to WAN Edge routers for reinforcement to handle traffic according to predefined business rules, regardless of origin or destination within the overlay.](#_Toc496778511)

-   

[**Intelligent Routing (OMP)**: They are integral to the **Overlay Management Protocol (OMP)**, which is the Cisco Catalyst SD-WAN\'s proprietary control plane protocol. Controllers run OMP among themselves and with WAN Edge routers, disseminating critical control plane information such as service-side reachability, transport-side IP addressing, and IPsec encryption keys. This centralized routing intelligence simplifies the learning and distribution of prefixes across the overlay.](#_Toc496778511)

[These functions enable the Controllers ~~to dramatically reduce~~ **Consider moving the adverb (e.g., 'to quickly configure' → 'to configure quickly')** [Explanation: avoiding split infinitives when possible. Category: Grammar & Punctuation] control plane complexity, making the network far more manageable and scalable. They are designed for high resiliency and multi-tenancy, meaning they can support multiple independent network environments simultaneously while maintaining continuous operation even in the face of component failures. This robust design ensures that policy enforcement is consistent and network-wide security is enhanced.](#_Toc496778511)

[**Real-World Scenario:** During a team briefing, your architect explains how Cisco Catalyst SD-WAN Controllers act as the "brain" of the network, making all the intelligent routing and policy decisions. You need to understand their core functions to grasp the centralized control model.](#_Toc496778511)

[**Why it matters:** The centralized control plane is a fundamental differentiator of Cisco Catalyst SD-WAN from traditional networks. Understanding the role of the Controllers is key to comprehending how the entire overlay network is managed and optimized.](#_Toc496778511)

[**Engineer Insight:** Think of the Controller as the air traffic controller for your WAN. It doesn\'t carry the planes (data), but it tells them where to go and ensures that they follow the rules (policies).](#_Toc496778511)

  ------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
          [**Tip:** The Cisco Catalyst SD-WAN Controllers form the centralized control plane, acting as the \"brain\" of the network. They orchestrate routing, distribute policies, and manage security parameters across the entire overlay, simplifying complex WAN operations.](#_Toc496778511)

  ------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[1. What is the primary role of Cisco Catalyst SD-WAN Controllers in the SD-WAN fabric?](#_Toc496778511)

[A. To forward data packets between WAN Edge routers.](#_Toc496778511)

[B. To provide the first point of authentication for new devices.](#_Toc496778511)

[C. To coordinate the overlay network, distribute policies, and manage routing information.](#_Toc496778511)

[D. To serve as the single pane of glass for network management.](#_Toc496778511)

[The Gatekeepers: Cisco Catalyst SD-WAN Validators](#_Toc496778511)

[While Controllers manage the ongoing intelligence and policy enforcement, the Cisco Catalyst SD-WAN Validators play an equally crucial, albeit different, role. They are the first point of contact for any new device attempting to join the SD-WAN fabric, acting as the secure gatekeepers.](#_Toc496778511)

[The Validator\'s responsibilities include:](#_Toc496778511)

-   
-   
-   

[**First Point of Authentication:** When a new WAN Edge router powers on and attempts to join the SD-WAN overlay, it first contacts the Validator. The Validator performs the initial authentication, verifying the device\'s identity against a pre-approved list (the authorized serial number file uploaded to SD-WAN Manager). This is a critical step in the zero-trust onboarding process, ensuring only legitimate devices can proceed.**Facilitating NAT Traversal:** In environments where Network Address Translation (NAT) is present (common in broadband internet deployments), the Validator assists WAN Edge devices in discovering their public (post-NAT) and private (pre-NAT) IP addresses. This capability is vital for establishing direct, secure tunnels between WAN Edge devices that might be behind different NAT devices.**Distributing Controller Information:** Once a WAN Edge device is authenticated, the Validator provides it with the list of available Cisco Catalyst SD-WAN Controllers and SD-WAN Managers. This allows the WAN Edge to then establish secure OMP sessions with the Controllers for routing and policy information, and secure connections with the Manager for configuration and monitoring.](#_Toc496778511)

[The following figure illustrates the Cisco Catalyst SD-WAN Orchestration Plane, highlighting the Validator\'s role in authentication, distribution of controller information, and NAT traversal for WAN Edge routers.](#_Toc496778511)

[![Network diagram illustrating the Orchestration Plane. A cloud contains a Validator, Manager, and Controllers. The Validator is shown as a virtual machine, serving as the first point of authentication, distributing lists of Controllers and Managers to all W A N Edges, and assisting with N A T Traversal. The Manager connects to 3rd Party Automation via A P I s. W A N Edge Routers at Cloud, Data Center, Campus, Branch, and CoLo sites connect to M P L S, 4 G, and I N E T transports, which in turn connect to the Controllers.](media/image5.bin){width="6.94027668416448in" height="3.791447944006999in"}](#_Toc496778511)

[Validators are designed for high resiliency and typically require a public IP address (or a 1:1 NAT mapping) to be reachable by all WAN Edge devices, regardless of their location. Their role is primarily focused on the initial secure bring-up and discovery, after~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]the WAN Edge devices interact directly with the Controllers and Manager.](#_Toc496778511)

[**Real-World Scenario:** A new WAN Edge router is failing to onboard. You need to understand if the issue lies with the SD-WAN Controller (for example, policy distribution, OMP peering) or the SD-WAN Validator (for example, initial authentication, reachability).](#_Toc496778511)

[**Why it matters:** Understanding the precise roles of each controller component is vital for troubleshooting onboarding issues, ensuring zero-trust security, and maintaining the integrity of the SD-WAN fabric.](#_Toc496778511)

[**Engineer Insight:** The Validator is the bouncer and greeter; it checks IDs and points new devices to the right party. The Controller is the party planner; it tells everyone what to do once they are inside. When troubleshooting, always check the Validator logs first for onboarding issues, then the Controller for policy or OMP problems.](#_Toc496778511)

[Cisco Catalyst SD-WAN Component Responsibilities](#_Toc496778511)

[To effectively manage and understand your Cisco Catalyst SD-WAN deployment, it\'s essential to know~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]component handles~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]task.](#_Toc496778511)

[The core duties of the main SD-WAN components are as follows:](#_Toc496778511)

-   
-   

[**Cisco Catalyst SD-WAN Controller: **This component distributes application-aware routing policies to WAN Edge devices and runs OMP sessions with other Controllers and WAN Edge devices.**Cisco Catalyst SD-WAN Validator:** This component facilitates NAT traversal for WAN Edge devices and functions as the first point of contact for a new WAN Edge device.](#_Toc496778511)

[Scalability and Resiliency of Controllers and Validators](#_Toc496778511)

[Both Cisco Catalyst SD-WAN Controllers and Validators are designed with inherent scalability and resiliency features to support enterprise-grade deployments.](#_Toc496778511)

-   
-   

[**Controllers:** They are a \"scale-out\" control plane function, meaning you can deploy multiple Controllers and they will automatically form a mesh among themselves using OMP. This distributed control plane provides high availability and load balancing for routing and policy dissemination. For enhanced resilience, organizations often deploy Controllers in geographically dispersed data centers, minimizing the impact of regional outages.**Validators:** While typically fewer Validators are needed compared to Controllers, they are also designed for high resiliency. In a cloud-service model, Cisco hosts them redundantly. For on-premises deployments, customers are responsible for providing adequate infrastructure resiliency to ensure continuous onboarding capability.](#_Toc496778511)

[This architectural design ensures that the core intelligence and onboarding mechanisms of your Cisco Catalyst SD-WAN remain robust and available, even as your network scales and encounters unforeseen challenges.](#_Toc496778511)

[2. Which component is responsible for the initial authentication of a new WAN Edge router joining the SD-WAN fabric and distributing the list of available Controllers?](#_Toc496778511)

[A. Cisco Catalyst SD-WAN Manager](#_Toc496778511)

[B. Cisco Catalyst SD-WAN Controller](#_Toc496778511)

[C. Cisco Catalyst SD-WAN Validator](#_Toc496778511)

[D. WAN Edge Router](#_Toc496778511)

[3. Which statement accurately describes the scalability and resiliency of Cisco Catalyst SD-WAN Controllers?](#_Toc496778511)

[A. They are a \"scale-up\" function, requiring more powerful single machines for larger deployments.](#_Toc496778511)

[B. They are a \"scale-out\" function, allowing multiple Controllers to form a mesh for high availability.](#_Toc496778511)

[C. They primarily handle data plane forwarding and do not contribute to control plane resiliency.](#_Toc496778511)

[D. They are typically deployed as a single, centralized instance without redundancy.](#_Toc496778511)

+------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [![Analogy icon.](media/image6.bin){width="0.9741929133858268in" height="0.9741929133858268in"}](#_Toc496778511) | [**Think Like an Engineer: Centralized Control Plane**](#_Toc496778511)                                                                                                                                                                                                   |
|                                                                                                                  |                                                                                                                                                                                                                                                                           |
|                                                                                                                  | [You\'re discussing the shift to Cisco Catalyst SD-WAN with a colleague familiar with traditional routing. How would you explain that centralizing the control plane reduces operational complexity compared to a distributed routing protocol like ~~BGP~~ **Border Gateway Protocol (BGP)** [Explanation: Acronym 'BGP' not expanded on first use. Category: Acronyms]?](#_Toc496778511) |
|                                                                                                                  |                                                                                                                                                                                                                                                                           |
|                                                                                                                  | -                                                                                                                                                                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[Consider aspects such as policy consistency, troubleshooting scope, and configuration management in your explanation.](#_Toc496778511)

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [![http://schemas.openxmlformats.org/drawingml/2006/picture](media/image7.bin){width="1.8193547681539808in" height="2.6064512248468943in"}](#_Toc496778511) | [**Key Takeaway: The Brains and Gatekeepers of Your SD-WAN Fabric**](#_Toc496778511)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                             | [Understanding the distinct roles of Cisco Catalyst SD-WAN Controllers and Validators is fundamental to grasping the intelligence and security of the SD-WAN architecture.](#_Toc496778511)                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                             | [By differentiating their functions, you can:](#_Toc496778511)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                             | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                             | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                             | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                             | [**Appreciate Centralized Intelligence:** Recognize how Controllers centralize routing and policy, simplifying network management.**Ensure Secure Onboarding:** Understand the Validator\'s role in securely bringing new devices into the fabric.**Troubleshoot Effectively:** Pinpoint issues more accurately by knowing~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]component is responsible for control plane orchestration versus initial device authentication.This foundational knowledge empowers you to design, deploy, and troubleshoot your Cisco Catalyst SD-WAN solution with confidence, ensuring a robust and secure network.](#_Toc496778511) |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[[]{#_Toc215687656 .anchor}SD-WAN Manager](#_Toc496778511)

[The Cisco Catalyst SD-WAN solution fundamentally transforms WAN (WAN) management by shifting from a device-centric, command-line interface (CLI)-driven approach to a centralized, policy-driven model. At the heart of this transformation lies the Cisco Catalyst SD-WAN Manager, a powerful network management system that serves as a centralized platform for all operations within your Cisco Catalyst SD-WAN fabric.](#_Toc496778511)

  ------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Real-world scenario icon.](media/image3.bin){width="0.9741929133858268in" height="0.9741929133858268in"}](#_Toc496778511)   [This topic highlights the operational benefits of centralized management facilitated by Cisco Catalyst SD-WAN Manager, covering its capabilities for provisioning, monitoring, and troubleshooting.](#_Toc496778511)

  ------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[To truly appreciate the power of this centralized tool, let\'s consider how it streamlines daily operations and empowers network engineers to manage complex environments more effectively.](#_Toc496778511)

+------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [![Analogy icon.](media/image6.bin){width="0.9741929133858268in" height="0.9741929133858268in"}](#_Toc496778511) | [**Think Like an Engineer: Leveraging the Command Center**](#_Toc496778511)                                                                                                                                                                                                                                                                                     |
|                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                  | [Your architect explains that Cisco Catalyst SD-WAN Manager will be your \"command center\" for provisioning new devices, monitoring network health, and troubleshooting performance issues. As a network engineer, how would you maximize the use of this centralized tool to streamline your daily tasks and improve operational efficiency?](#_Toc496778511) |
|                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                  | -                                                                                                                                                                                                                                                                                                                                                               |
+------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[Consider aspects such as template-driven provisioning, proactive monitoring, and integrated troubleshooting workflows.](#_Toc496778511)

[Centralized Management: Your Cisco Catalyst SD-WAN Command Center](#_Toc496778511)

[In traditional WAN environments, managing a multisite network often involves logging into individual routers, configuring them one by one, and manually verifying their operational status. This distributed approach becomes incredibly complex, time-consuming, and prone to human error as your network scales. Configuration drift, where devices subtly diverge from their intended configurations, is a constant threat, leading to unpredictable behavior and security vulnerabilities.](#_Toc496778511)

[Cisco Catalyst SD-WAN Manager addresses these challenges head-on by providing a centralized platform for Day 0 (onboarding), Day ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] (provisioning and configuration), and Day ~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] (monitoring, troubleshooting, and maintenance) operations. This unified approach streamlines daily tasks, significantly reduces operational overhead, and ensures consistency across your entire fabric.](#_Toc496778511)

[**Real-World Scenario:** Imagine your ~~IT~~ **Information Technology (IT)** [Explanation: Acronym 'IT' not expanded on first use. Category: Acronyms] team is tasked with rolling out a new security policy to every branch office globally. In a traditional WAN, this would involve logging into dozens, if not hundreds, of individual routers ~~to manually configure~~ **Consider moving the adverb (e.g., 'to quickly configure' → 'to configure quickly')** [Explanation: avoiding split infinitives when possible. Category: Grammar & Punctuation] the changes. How can you achieve this efficiently and consistently, minimizing human error and deployment time?](#_Toc496778511)

[**Why it matters:** Centralized management is key to scaling Cisco Catalyst SD-WANdeployments and reducing operational overhead. SD-WAN Manager transforms complex, distributed configurations into manageable, policy-driven operations, translating into significant time savings and reduced human error in large-scale network environments.](#_Toc496778511)

[**Engineer Insight:** Embrace the power of centralized management to shift your focus from repetitive, manual tasks to strategic network design and optimization. By leveraging templates and a unified management interface, you ensure configuration consistency across the fabric, dramatically reducing troubleshooting time and freeing up resources for innovation.](#_Toc496778511)

[Accessing SD-WAN Manager](#_Toc496778511)

[Accessing Cisco Catalyst SD-WAN Manager is straightforward. You connect to it using a standard web browser, providing a familiar graphical user interface (GUI) for network administrators. The default login credentials are typically admin for both the username and password, though these should be changed immediately in a production environment for security purposes.](#_Toc496778511)

[The following figure shows the login screen for Cisco Catalyst SD-WAN Manager, providing access to the centralized management platform.](#_Toc496778511)

[![Login screen for Cisco Catalyst S D-W A N, with fields for Username and a Continue button, set against a background of server racks in a data center.](media/image8.bin){width="6.94027668416448in" height="3.4482556867891514in"}](#_Toc496778511)

[Upon successful login, you are greeted with the Monitor \> Overview dashboard, which acts as your primary window into the health and status of your entire SD-WAN overlay network.](#_Toc496778511)

  ------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
          [**Tip:** The Cisco Catalyst SD-WAN Manager acts as a centralized platform for all network operations. From Day 0 onboarding to Day ~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] troubleshooting, its intuitive GUI streamlines tasks, drastically reducing complexity and potential for human error.](#_Toc496778511)

  ------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[1. What is the primary benefit of using Cisco Catalyst SD-WAN Manager for network operations?](#_Toc496778511)

[A. It allows for manual, per-device configuration, ensuring granular control.](#_Toc496778511)

[B. It centralizes provisioning, monitoring, and troubleshooting, reducing operational complexity.](#_Toc496778511)

[C. It eliminates the need for any network engineers, fully automating all tasks.](#_Toc496778511)

[D. It provides a distributed management plane, enhancing fault tolerance.](#_Toc496778511)

[SD-WAN Manager Monitor Overview Dashboard](#_Toc496778511)

[The **Monitor \> Overview** dashboard in SD-WAN Manager provides a comprehensive, high-level snapshot of your SD-WAN fabric\'s health and performance. It aggregates data from all connected devices and presents it through a series of intuitive panes, allowing for rapid issue identification and a quick understanding of your network\'s overall operational status.](#_Toc496778511)

[The following figure displays the Cisco Catalyst SD-WAN Manager\'s Monitor Overview dashboard, providing a high-level snapshot of the SD-WAN fabric\'s health and performance.](#_Toc496778511)

[![Alt Text: Screenshot of the Cisco Catalyst S D-W A N Manager Monitor Overview dashboard. Panes show Control Components (1 Validator, 2 Controllers, 1 Manager), W A N Edges (6 Reachable), Certificate Status (0 Warning, 0 Invalid), Licensing (14 Assigned), and Reboot (0 Last 24 hours). Below, Site Health shows 4 sites with a breakdown of Good and Fair performance. Tunnel Health displays 58 tunnels with latency details.](media/image9.bin){width="6.94027668416448in" height="2.71671697287839in"}](#_Toc496778511)

[The Monitor Overview dashboard typically displays the following key panes:](#_Toc496778511)

-   
-   
-   
-   
-   
-   

[**Control Components and WAN Edges Panes:** These two panes, positioned prominently at the top of the screen, provide a quick count of your Cisco Catalyst SD-WAN components. These include SD-WAN Validators, SD-WAN Controllers, SD-WAN Managers (if in a clustered deployment) and WAN Edge routers. It indicates their reachability status, allowing you ~~to immediately see~~ **Consider moving the adverb (e.g., 'to quickly configure' → 'to configure quickly')** [Explanation: avoiding split infinitives when possible. Category: Grammar & Punctuation] if any critical components are offline. Clicking on the numbers within this pane drills down to a detailed table for each device type.**Certificate Pane:** Security is paramount in Cisco Catalyst SD-WAN. This pane displays the state of all certificates on your controller devices, highlighting any expired or invalidated certificates. Expired certificates can lead to control plane outages, so this pane is crucial for proactive maintenance. Clicking on it reveals detailed certificate information, including serial numbers and expiration dates.**Licensing Pane:** This pane provides an overview of your assigned and unassigned licenses for WAN Edge devices. It helps you track compliance and plan for future deployments by showing how many devices are licensed versus unlicensed.**Reboot Pane:** Unexpected reboots can indicate underlying stability issues. This pane displays the total number of reboots (soft, cold, or power-cycle related) across all devices in the last 24 hours. You can drill down to see details like the system IP, hostname, time, and reason for each reboot, including any crashes.**Site Health Pane:** This pane displays the health, calculated by the average Quality of Experience (QoE) across all sites by default. The site\'s health depends on the health metrics of devices, tunnels, and applications at a chosen site.**Tunnel Health Pane:** This pane displays the health, average latency, loss, and jitter of all tunnel end points.The following figure illustrates the WAN Edge Health dashboard, showing CPU load, application health, top applications, and WAN Edge configuration management.](#_Toc496778511)

[![Dashboard displaying WAN Edge Health, showing a donut chart with Good, Fair, and Poor categories. A list of host sites shows C P U load percentages. Sections for Application Health and Top Applications are present but show no data. The WAN Edge Management pane shows a bar chart indicating 6 devices configured by Template and 1 Unlocked.](media/image10.bin){width="6.940277777777778in" height="3.1669575678040247in"}](#_Toc496778511)

-   
-   
-   
-   

[**WAN Edge Health Pane:** This pane offers an aggregated view of WAN Edge router health, based on average CPU and Memory Load, reachability, control, ~~BFD~~ **Bidirectional Forwarding Detection (BFD)** [Explanation: Acronym 'BFD' not expanded on first use. Category: Acronyms] tunnels and ~~TLOCs~~ **Transport Location (TLOC)** [Explanation: Acronym 'TLOC' not expanded on first use. Category: Acronyms] status, categorized by good, fair, and poor.**Application Health Pane:** You can view the usage of applications across all sites in a graphical format. The graph indicates whether the application performance is Good, Fair, or Poor based on the Application Quality of Experience (QoE).**Top Application Pane:** This pane displays the Cisco Catalyst SD-WAN Application Intelligence Engine (SAIE) flow information for traffic transiting WAN Edge routers in the overlay network.**WAN Edge Management Pane:** This pane shows the WAN Edge devices by Configuration type. It displays how many WAN Edge devices configurations managed by Config Groups, Templates, or CLI.**Real-World Scenario:** Your operations team receives an alert about degraded network performance impacting a critical application. You need ~~to quickly assess~~ **Consider moving the adverb (e.g., 'to quickly configure' → 'to configure quickly')** [Explanation: avoiding split infinitives when possible. Category: Grammar & Punctuation] the overall health of your Cisco Catalyst SD-WANfabric and pinpoint the source of the issue. How can the Monitor Overview dashboard provide a rapid, high-level diagnosis?](#_Toc496778511)

[**Why it Matters:** The Monitor Overview dashboard is crucial for proactive network management. Its aggregated views allow you ~~to quickly identify~~ **Consider moving the adverb (e.g., 'to quickly configure' → 'to configure quickly')** [Explanation: avoiding split infinitives when possible. Category: Grammar & Punctuation] potential issues across the entire Cisco Catalyst SD-WAN fabric, enabling rapid response and preventing minor problems from escalating into major outages.](#_Toc496778511)

[**Engineer Insight:** Mastering the Monitor Overview dashboard is key to efficient Day ~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] operations. Prioritize configuring alerts for critical health metrics (for example, WAN Edge Health, Certificate status) and ~~utilize~~ **use** [Explanation: 'use' instead of 'utilize'. Category: Cisco Style Guide] its drill-down capabilities ~~to quickly pinpoint~~ **Consider moving the adverb (e.g., 'to quickly configure' → 'to configure quickly')** [Explanation: avoiding split infinitives when possible. Category: Grammar & Punctuation] root causes, saving valuable troubleshooting time.](#_Toc496778511)

[2. What information do the Control Components and WAN Edges panes at the top of the SD-WAN Manager Monitor Overview Dashboard provide?](#_Toc496778511)

[A. They show a quick count and reachability status of Cisco Catalyst SD-WAN components like Validators, Controllers, Managers, and WAN Edge routers.](#_Toc496778511)

[B. They display the health of all application traffic based on Quality of Experience (QoE) metrics.](#_Toc496778511)

[C. They summarize the certificate and root CA status of the Cisco Catalyst SD-WAN Validators, Controllers, Managers, and WAN Edge routers.](#_Toc496778511)

[D. They show that details about unexpected device reboots, including system IP and time.](#_Toc496778511)

[SD-WAN Manager: Your Unified Command Center for Operations](#_Toc496778511)

[The Cisco Catalyst SD-WAN Manager serves as the intuitive, centralized platform for all network operations. It streamlines the entire lifecycle of your Cisco Catalyst SD-WANfabric, from initial setup to ongoing maintenance and issue resolution. This unified management approach significantly reduces operational overhead and the potential for human error, making complex network operations more manageable and efficient for your team.](#_Toc496778511)

[Key functions provided by SD-WAN Manager include:](#_Toc496778511)

-   
-   
-   

[Efficient Provisioning: SD-WAN Manager simplifies device provisioning through templates and configuration groups. This enables rapid and consistent deployment across the fabric, allowing administrators to push configurations to multiple devices simultaneously and consistently.Comprehensive Monitoring: It offers extensive dashboards and real-time data views, providing deep insights into network health, performance, and application behavior. This includes detailed information on control components, WAN Edge health, tunnel status, and application performance.Effective Troubleshooting: Integrated diagnostic tools and detailed device-specific dashboards streamline problem identification and resolution. Engineers can quickly pinpoint issues using tools like ping, traceroute, and detailed device status views.](#_Toc496778511)

[The following figure displays the Cisco Catalyst SD-WAN Manager\'s Configuration Templates section, showing a list of available templates and their associated details.](#_Toc496778511)

[![Screenshot of the Cisco Catalyst S D-W A N Manager interface showing the Configuration Templates section. A table lists various templates including vEdge, cEdge, controller, and 1000v, with columns for Device Model, Role, Feature Templates, Draft Mode, Devices Attached, Updated By, Last Updated, and Template Status.](media/image11.bin){width="6.94027668416448in" height="3.2071434820647418in"}](#_Toc496778511)

[Effective Troubleshooting: Integrated Tools and Dashboards](#_Toc496778511)

[SD-WAN Manager is not just for initial setup; it\'s also your go-to tool for daily monitoring and troubleshooting. It transforms the often-daunting task of diagnosing network issues into a more streamlined process through its intuitive GUI workflows and integrated diagnostic tools.](#_Toc496778511)

[**Device Dashboards:** From the **Monitor \> Devices** screen, you can ~~click on~~ **click** [Explanation: 'click' instead of 'click on'. Category: Cisco Style Guide] any specific device (for example, a WAN Edge router) to access its **Device 360 dashboard**. This dashboard provides granular details about that single device, offering a wealth of information categorized into various sections:](#_Toc496778511)

-   
-   
-   
-   
-   
-   
-   
-   
-   
-   
-   

[**Interface:** Displays real-time and historical statistics for all interfaces, including traffic volume, errors, and operational status.**Tracker:** Presents configured tracker information.**QoS:** Shows Quality of Service statistics.**On-Demand Troubleshooting:** Offers on-demand trouble shooting tools such as AppQoE TCP Optimization.**WAN:** Details TLOC and tunnel status, including BFD session health.**Security Monitoring:** If configured, this section provides insights into firewall, IPS, Cisco URL Filtering, and other security features.**Control Connections:** Shows the status and statistics of control plane connections to SD-WAN Controllers, SD-WAN Validators, and other SD-WAN Managers. Failed control connections mean that the device isn\'t receiving policies or routes, which is a critical issue.**System Status:** Provides critical metrics like CPU usage, memory utilization, hardware health, and recent reboot or crash information. This is crucial for identifying performance bottlenecks or stability issues on a device.**Events:** Lists recent syslog events generated by the device, which can be invaluable for diagnosing configuration changes or errors.**~~ACL~~ **access control list (ACL)** [Explanation: Acronym 'ACL' not expanded on first use. Category: Acronyms] Logs:** Displays logging files for access lists.**Real Time:** Shows real-time device information for feature-specific operational commands.](#_Toc496778511)

[The following figure shows the Cisco Catalyst SD-WAN Manager\'s Device 360 dashboard for Site100-CE1, displaying system status information including reboots, crashes, hardware components, and CPU and memory utilization.](#_Toc496778511)

[![Screenshot of the Cisco Catalyst S D-W A N Manager Device 360 dashboard for Site100-C E 1, under Monitor Devices System Status. It shows 20 reboots in the last 90 days and no crashes. Sections for Module, Hardware Inventory, Power Supply, Fans, and U S B are visible. A graph displays Control Plane C P U Utilization and Data Plane C P U Utilization over time.](media/image12.bin){width="6.94027668416448in" height="3.223111329833771in"}](#_Toc496778511)

[**Real-World Scenario:** A user reports intermittent connectivity to a specific application at a remote branch. You\'ve checked the Monitor Overview dashboard and see a \"Fair\" status for that WAN Edge. You need to drill down and diagnose the exact problem efficiently using the Cisco Catalyst SD-WAN Manager GUI.](#_Toc496778511)

[**Why it Matters:** Effective troubleshooting tools are vital for minimizing downtime and maintaining service availability. Cisco Catalyst SD-WAN Manager\'s integrated diagnostics accelerate problem resolution, directly impacting user satisfaction and business continuity.](#_Toc496778511)

[**Engineer Insight:** The Device 360 dashboard is your go-to for granular troubleshooting. Always start by checking \'System Status\' and \'Control Connections\' for a device. Leverage the \'Real Time\' data views for immediate insights, and don\'t forget the integrated Ping and Traceroute tools ~~to quickly confirm~~ **Consider moving the adverb (e.g., 'to quickly configure' → 'to configure quickly')** [Explanation: avoiding split infinitives when possible. Category: Grammar & Punctuation] reachability from the device\'s perspective.](#_Toc496778511)

[Integrated Troubleshooting Tools](#_Toc496778511)

[SD-WAN Manager\'s troubleshooting capabilities extend beyond just displaying metrics. It integrates diagnostic tools directly into the GUI, streamlining your workflow. For example, from a device\'s **Device 360** dashboard, you can navigate to the **Troubleshooting** section to perform:](#_Toc496778511)

-   
-   

[**Ping:** Test basic IP reachability to any destination from the perspective of the WAN Edge router.**Traceroute:** Trace the path to a destination, helping to identify where traffic might be getting dropped or misrouted.The following figure shows the Cisco Catalyst SD-WAN Manager\'s device dashboard, highlighting the integrated troubleshooting tools such as Ping and Trace Route.](#_Toc496778511)

[![Screenshot of the Cisco Catalyst S D-W A N Manager interface for device Site400-C E 1. The left navigation panel shows Monitor, Configuration, Analytics, Workflows, Tools, Reports, Maintenance, and Administration. Under Tools, On-Demand Troubleshooting options are visible, with Ping and Trace Route highlighted. The main content area displays Connectivity, Traffic, and Logs sections with various diagnostic tools like Device Bringup, Tunnel Health, and Debug Log.](media/image13.bin){width="6.940277777777778in" height="3.2108956692913386in"}](#_Toc496778511)

[These tools, combined with the detailed device dashboards, allow you to identify the root cause of issues, whether they are related to interface problems, control plane instability, or application performance degradation.](#_Toc496778511)

[3. Which of the following SD-WAN Manager features is primarily used for quickly identifying the root cause of issues?](#_Toc496778511)

[A. Monitor \> Overview dashboard](#_Toc496778511)

[B. Configuration \> Templates section](#_Toc496778511)

[C. Device 360 dashboard \> Troubleshooting section](#_Toc496778511)

[D. Administration \> Settings](#_Toc496778511)

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [![http://schemas.openxmlformats.org/drawingml/2006/picture](media/image7.bin){width="1.8193547681539808in" height="2.6064512248468943in"}](#_Toc496778511) | [**Key Takeaway: Centralized Control for Agile Operations**](#_Toc496778511)                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                             | [The Cisco Catalyst SD-WAN Manager is the cornerstone of operational efficiency within your Cisco Catalyst SD-WAN deployment.](#_Toc496778511)                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                             | [By leveraging this centralized platform, your company can:](#_Toc496778511)                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                             | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                             | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                             | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                             | [**Streamline Operations:** Consolidate Day 0, Day ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation], and Day ~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] tasks into a single, intuitive interface.**Reduce Errors:** Minimize manual configuration and ensure consistent policy application across the entire fabric.**Accelerate Response:** Gain comprehensive visibility and integrated tools for rapid Monitoring and Troubleshooting.This empowers your team to manage complex networks with greater ease, freeing up resources for strategic initiatives and driving business agility.](#_Toc496778511) |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[[]{#_Toc215687657 .anchor}WAN Edge Routers: Physical~~ & ~~ **Change '&' to 'and'** [Explanation: 'and' instead of '&' in prose text. Category: Grammar & Punctuation]Virtual](#_Toc496778511)

[In the dynamic landscape of modern enterprise networks, WAN Edge routers serve as the critical frontline elements of the Cisco Catalyst SD-WAN fabric. They are the workhorses that sit at the perimeter of a site---be it a remote office, branch office, campus, or data center---and are responsible for securely connecting the local network to the broader WAN. These devices are not merely routers; they are intelligent, policy-enforcing gateways that deliver essential WAN, security, and multi-cloud capabilities.](#_Toc496778511)

  ------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Real-world scenario icon.](media/image3.bin){width="0.9741929133858268in" height="0.9741929133858268in"}](#_Toc496778511)   [This topic defines the critical role of WAN Edge routers, explores Cisco Catalyst SD-WAN platforms, and compares the deployment flexibility between physical and virtual solutions for diverse network scenarios.](#_Toc496778511)

  ------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Your architect explains how WAN Edge routers act as "data plane workhorses," ensuring secure, high-performance connectivity and policy enforcement at each site. You need to understand the different models and their suitability for various branch sizes.](#_Toc496778511)

[The Role of WAN Edge Routers in the SD-WAN Fabric](#_Toc496778511)

[WAN Edge routers are the data plane elements of the Cisco Catalyst SD-WAN fabric. Their primary responsibilities include:](#_Toc496778511)

-   
-   
-   
-   
-   
-   

[**Establishing Secure Tunnels:** They build and maintain secure IPsec tunnels with other WAN Edge routers across the overlay network, ensuring encrypted and authenticated communication for all application traffic.**Enforcing Policies:** They enforce data plane and application-aware routing policies distributed by the SD-WAN Controllers, ensuring that traffic flows according to business intent and application requirements.**Forwarding Traffic:** They efficiently forward application traffic between the local site network (LAN) and the WAN (WAN).**Exporting Performance Statistics:** They continuously export performance statistics, alerts, and events to the SD-WAN Manager for centralized Monitoring and Troubleshooting.**Traditional Routing Protocols:** They ~~leverage~~ **use** [Explanation: 'use' instead of 'leverage'. Category: Cisco Style Guide] traditional routing protocols like ~~OSPF~~ **Open Shortest Path First (OSPF)** [Explanation: Acronym 'OSPF' not expanded on first use. Category: Acronyms], BGP, and EIGRP to learn reachability information from service (LAN)-side interfaces and for integration with non-Cisco Catalyst SD-WAN sites.**Zero-Touch Provisioning (ZTP):** They support ZTP and Cisco Plug and Play, enabling rapid and automated onboarding into the SD-WAN fabric.](#_Toc496778511)

[Cisco Catalyst SD-WAN Platforms](#_Toc496778511)

[Cisco Catalyst SD-WAN Edge routers are the routing components of the architecture that deliver the essential WAN, security, and multi-cloud capabilities of the Cisco Catalyst SD-WAN solution. These routers are available in various form factors to suit diverse deployment needs, from physical appliances at branch offices to virtual instances in cloud environments. They are designed to sit at the perimeter of a site and participate in establishing a secure virtual overlay network over any mix of WAN transports.](#_Toc496778511)

[There are two major categories of Cisco Catalyst SD-WAN routers:](#_Toc496778511)

-   

```{=html}
<!-- -->
```
-   
-   
-   

```{=html}
<!-- -->
```
-   

```{=html}
<!-- -->
```
-   
-   
-   

[**Cisco ~~IOS~~ **Cisco IOS Software** [Explanation: Acronym 'IOS' not expanded on first use. Category: Acronyms] XE Software SD-WAN Routers:** These are traditional Cisco Cisco IOS XE Software routers that have been enhanced with Cisco Catalyst SD-WAN capabilities through specific software images. This category includes:**Cisco ISR 1000 series:** Compact, high-performance routers ideal for small to medium-sized branch offices.**Cisco ISR 4000 series:** Modular, high-performance routers suitable for medium to large branch offices, offering a wide range of services.**Cisco ASR 1000 series:** High-end aggregation services routers designed for large enterprises and data centers, providing high throughput and advanced services.**Catalyst 8000 Edge Routers~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]Cisco Catalyst 8200 series:** These modular routers are suitable for small to medium-sized branch offices.**Cisco Catalyst 8300 series:** This series is ideal for larger, more demanding branch offices that require higher performance and more rich services.**Cisco Catalyst 8500 series:** This series is designed for high-performance aggregation in data centers and colocation facilities.](#_Toc496778511)

[For virtualized environments, Cisco offers two primary options to deliver Cisco Catalyst SD-WAN in the cloud or on virtualized infrastructure:](#_Toc496778511)

-   
-   

[**Cisco Cloud Services Router (CSR 1000V)**: A virtual router running Cisco IOS XE Software, offering comprehensive routing, security, and network services for cloud and virtualized environments.**Cisco Catalyst 8000V Edge Software (Catalyst 8000V):** A virtual-form-factor Cisco Catalyst SD-WAN Edge router that runs Cisco IOS XE software. It ~~leverages~~ **uses** [Explanation: 'use' instead of 'leverage'. Category: Cisco Style Guide] Network-Functions-Virtualization (NFV) components, allowing it to fill roles traditionally reserved for hardware-based devices. The Catalyst 8000V can run on Cisco Unified Computing System (UCS) servers, as well as on servers from leading vendors that support VMware ESXi, Red Hat KVM virtualization, Oracle Cloud Infrastructure (OCI)-Alibaba Cloud, or on public cloud platforms like Amazon EC2, Microsoft Azure, or Google Cloud Platform.](#_Toc496778511)

[The following figure categorizes various Cisco Catalyst SD-WAN platforms suitable for different deployment scenarios, including virtual, cloud, branch, core, hybrid remote, and industrial IOT edge environments.](#_Toc496778511)

[![Diagram titled S D-W A N Platforms for Any Deployment, categorizing Cisco devices by deployment type. Virtual platforms include C S P 5000 and E N C S 5000. Cloud platforms include Catalyst 8000V and C S R 1000V. Branch platforms include I S R 1000, I S R 4000, A S R 1000, and various Catalyst 8000 Edge platforms. Core platforms include Catalyst 8500 and A S R 1000. Hybrid Remote platforms include Catalyst Wireless Gateway C G 113 and Cisco Catalyst Cellular Gateway. Industrial I O T Edge platforms include Catalyst I R 1100, I R 1101, I R 1800, and I R 1830.](media/image14.bin){width="6.94027668416448in" height="2.499403980752406in"}](#_Toc496778511)

[1. Which of the following Cisco Catalyst WAN Edge router platforms are suitable for small to medium-sized branch offices?](#_Toc496778511)

[A. Cisco ISR 4000 series](#_Toc496778511)

[B. Cisco ASR 1000 series](#_Toc496778511)

[C. Cisco Catalyst 8200 series](#_Toc496778511)

[D. Cisco Catalyst 8000V](#_Toc496778511)

[Deployment Flexibility: Physical vs. Virtual WAN Edge Solutions](#_Toc496778511)

[Your enterprise is expanding into a new region with both physical branch offices and cloud-hosted applications. You need to decide on the optimal mix of physical and virtual WAN Edge routers to ensure seamless connectivity and cost-efficiency.](#_Toc496778511)

[The choice between physical and virtual WAN Edge solutions depends heavily on the specific deployment scenario, balancing factors such as performance requirements, physical space constraints, existing infrastructure, and cost-efficiency.](#_Toc496778511)

+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [![Analogy icon.](media/image6.bin){width="0.9741929133858268in" height="0.9741929133858268in"}](#_Toc496778511) | [**Think Like an Engineer: Strategic Platform Selection**](#_Toc496778511)                                                                                                                                                                                                                                                   |
|                                                                                                                  |                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                  | [When designing a large-scale Cisco Catalyst SD-WAN deployment for a global enterprise with diverse site types (for example, small retail kiosks, large regional hubs, cloud VPCs), how would you develop a standardized decision matrix for selecting the appropriate WAN Edge platform for each location?](#_Toc496778511) |
|                                                                                                                  |                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                  | [Consider factors beyond just cost and throughput.](#_Toc496778511)                                                                                                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[**Physical WAN Edge Routers (Catalyst 8000 Edge, ISR, ASR):**](#_Toc496778511)

-   
-   

```{=html}
<!-- -->
```
-   
-   
-   
-   

```{=html}
<!-- -->
```
-   

[**Suitability:** Ideal for traditional branch offices, campus environments, and data centers where dedicated hardware performance, high port density, and specific hardware-accelerated services are required. They are well suited for larger sites with significant traffic volumes and complex local network integrations.**Advantages~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]Dedicated Performance:** Offer predictable, high-performance throughput as they are purpose-built hardware.**Robustness:** Designed for continuous operation in various physical environments.**Interface Options:** Provide a wide range of physical interfaces (Ethernet, serial, cellular) to connect to diverse WAN and LAN technologies.**Hardware Acceleration:** Can ~~leverage~~ **use** [Explanation: 'use' instead of 'leverage'. Category: Cisco Style Guide] dedicated hardware for encryption, QoS, and other network services, offloading the CPU.**Considerations:** Higher initial capital expenditure, require physical installation and maintenance, and may have longer provisioning times compared to virtual solutions.](#_Toc496778511)

[**Virtual WAN Edge Routers (Catalyst 8000V, CSR 1000V):**](#_Toc496778511)

-   
-   
-   

```{=html}
<!-- -->
```
-   
-   
-   
-   

```{=html}
<!-- -->
```
-   

[**Suitability:** Excellent for cloud deployments (for example, connecting cloud-hosted applications or virtual private clouds), small branch offices with limited physical space or IT staff, and environments leveraging network function virtualization (NFV) or virtual customer-premises equipment (vCPE) models.Offers significant agility for rapid deployment and scaling.**Advantages~~:~~ **Add space after colon** [Explanation: Add space after colon. Category: Grammar & Punctuation]Deployment Flexibility:** Can be deployed quickly in public clouds, private data centers (on hypervisors), or even on general-purpose servers at smaller branches.**Cost-Efficiency:** Can reduce hardware costs by running on existing virtualized infrastructure.**Agility and Scalability:** Easy to spin up, scale out, or scale down based on demand, making them ideal for dynamic cloud environments or temporary sites.**Simplified Logistics:** No physical shipping or installation required, accelerating deployment timelines.**Considerations:** Performance is dependent on the underlying hypervisor and server resources, may have fewer physical interface options, and might require more careful resource management in shared environments.](#_Toc496778511)

[**Real-World Scenario:** Your company is a rapidly expanding retail chain with plans to open dozens of new small kiosks, several medium-sized stores, and integrate its cloud-based inventory management system. You\'re tasked with selecting the appropriate Cisco Catalyst WAN Edge platforms for each location type, balancing initial cost, deployment speed, ongoing management, and performance requirements for diverse business applications.](#_Toc496778511)

[**Why it matters:** WAN Edge routers are the frontline of the SD-WAN fabric. Choosing the right platform ensures optimal performance, scalability, and cost-effectiveness for each site in the network. This topic provides practical insights into deploying WAN Edge devices, enabling engineers to make informed decisions that balance performance, cost, and flexibility across diverse network footprints.](#_Toc496778511)

[**Engineer Insight:** These are the physical (or virtual) boxes that actually move the packets. Understand their hardware capabilities (throughput, interface types) and software features (security, QoS) to match them to site requirements. Virtual WAN Edges are great for cloud and small, agile deployments. Physical appliances offer dedicated performance and more interface options for larger branches or data centers. Always consider future growth and application demands when selecting a platform.](#_Toc496778511)

[The following table provides a comparison of various Cisco Catalyst WAN Edgerouter models, highlighting their key features and ideal use cases.](#_Toc496778511)

[Device Comparison](#_Toc496778511)

  ----------------------------------------------------- ---------------------------- ----------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------
  [**Model**](#_Toc496778511)                           [**Type**](#_Toc496778511)   [**Key Features**](#_Toc496778511)                                                                          [**Ideal Use Cases**](#_Toc496778511)

  [**Cisco Catalyst 8200/8300 Edge**](#_Toc496778511)   [Physical](#_Toc496778511)   [High performance, integrated security, modularity, advanced routing](#_Toc496778511)                       [Small, Medium to Large Branch, Small Data Center](#_Toc496778511)

  [**Cisco Catalyst 8000V**](#_Toc496778511)            [Virtual](#_Toc496778511)    [Full Cisco Catalyst SD-WAN capabilities, runs on hypervisors/cloud, flexible deployment](#_Toc496778511)   [Cloud VPCs, Virtual Branches, NFV](#_Toc496778511)

  [**Cisco ISR 1000 Series**](#_Toc496778511)           [Physical](#_Toc496778511)   [Compact, integrated services, cost-effective, cellular options](#_Toc496778511)                            [Small Branch, Retail, IoT Edge](#_Toc496778511)

  [**Cisco ISR 4000 Series**](#_Toc496778511)           [Physical](#_Toc496778511)   [Modular, high-performance, integrated services, voice/video support](#_Toc496778511)                       [Medium to Large Branch, Enterprise Edge](#_Toc496778511)

  [**Cisco ASR 1000 Series**](#_Toc496778511)           [Physical](#_Toc496778511)   [High-end aggregation, massive throughput, advanced services](#_Toc496778511)                               [Large Data Center, Regional Hub](#_Toc496778511)

  [**Cisco CSR 1000V**](#_Toc496778511)                 [Virtual](#_Toc496778511)    [Cisco IOS XE Software, comprehensive routing, cloud/virtualized environments](#_Toc496778511)              [Cloud VPCs (legacy Cisco IOS XE Software deployments), Virtual Branches](#_Toc496778511)
  ----------------------------------------------------- ---------------------------- ----------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------

[2. WAN Edge routers are primarily responsible for~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]aspect of the Cisco Catalyst SD-WAN fabric?](#_Toc496778511)

[A. Orchestrating the overlay network and distributing policies.](#_Toc496778511)

[B. Authenticating new devices and facilitating NAT traversal.](#_Toc496778511)

[C. Building secure IPsec tunnels and enforcing data plane policies.](#_Toc496778511)

[D. Providing a single pane of glass for network management.](#_Toc496778511)

[Case Study: Choosing the Right WAN Edge for a Hybrid Cloud Deployment](#_Toc496778511)

[A mid-sized enterprise is expanding its operations. They have 50 branch offices, ~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] data centers, and are heavily leveraging AWS for new applications. They need to choose WAN Edge platforms for their Cisco Catalyst SD-WAN deployment.](#_Toc496778511)

-   
-   
-   

[**Branch Offices (50 sites):** Varying sizes, from small retail stores to larger regional offices. Need cost-effective solutions, some with integrated Wi-Fi/LTE.**Data Centers (~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] sites):** High-throughput requirements, need to terminate many tunnels, integrate with existing routing protocols (OSPF/BGP).**AWS Cloud (multiple VPCs):** Need agile deployment, seamless integration with cloud networking, and the ability to scale quickly.](#_Toc496778511)

[**Analysis and Solution:** For the small branch offices, Cisco ISR 1000 series routers would be a suitable choice due to their compact form factor, integrated services (Wi-Fi, LTE options), and cost-effectiveness. For larger regional offices, Cisco Catalyst 8200/8300 Edge platforms would provide the necessary performance and modularity.](#_Toc496778511)

[For **data centers**, Cisco ASR 1000 series or high-end Catalyst 8300/8500 Edge platforms are recommended for their high throughput, robust routing capabilities, and ability to handle large numbers of IPsec tunnels.](#_Toc496778511)

[For **AWS Cloud deployments**, the Cisco Catalyst 8000V or Cisco CSR 1000v would be ideal. These virtual appliances can be easily deployed within AWS VPCs, providing native cloud integration, agility, and scalability to match the dynamic nature of cloud workloads.](#_Toc496778511)

[This hybrid approach ~~leverages~~ **uses** [Explanation: 'use' instead of 'leverage'. Category: Cisco Style Guide] the strengths of both physical and virtual WAN Edge solutions, optimizing performance and cost across the diverse enterprise environment.](#_Toc496778511)

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [![http://schemas.openxmlformats.org/drawingml/2006/picture](media/image7.bin){width="1.8193547681539808in" height="2.6064512248468943in"}](#_Toc496778511) | [**Key Takeaway: The Foundation of Site Connectivity**](#_Toc496778511)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                             | [Cisco Catalyst WAN Edge routers are the crucial data plane elements that bring the SD-WAN fabric to life at every site.](#_Toc496778511)                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                             | [By understanding their diverse platforms and deployment options, you can:](#_Toc496778511)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                             | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                             | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                             | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                             | [**Select Optimal Platforms:** Choose the right physical or virtual WAN Edge device to meet specific site requirements for performance, cost, and agility.**Ensure Secure Connectivity:** Recognize their role in establishing secure tunnels and enforcing policies at the network edge.**Support Hybrid Environments:** Effectively deploy WAN Edges in traditional branches, data centers, and cloud environments, ensuring seamless integration.This knowledge is vital for building a flexible, high-performing, and secure SD-WAN solution that adapts to your enterprise\'s evolving needs.](#_Toc496778511) |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[[]{#_Toc215687658 .anchor}Overlay Management Protocol (OMP): The Control Plane Glue](#_Toc496778511)

[You explored the distinct roles of the Cisco Catalyst SD-WAN Controllers (the brains), Validators (the gatekeepers), Manager (the command center), and WAN Edge routers (the workhorses). Now, let's discuss the critical protocol that orchestrates their communication and stitches the entire SD-WAN fabric together: the Overlay Management Protocol (OMP). OMP is the central nervous system of your Cisco Catalyst SD-WAN solution, enabling the dynamic exchange of routing, policy, and management information across the overlay network.](#_Toc496778511)

  ------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [![Real-world scenario icon.](media/image3.bin){width="0.9741929133858268in" height="0.9741929133858268in"}](#_Toc496778511)   [To appreciate the intelligence and agility of Cisco Catalyst SD-WAN, you must understand the role of OMP. It's the engine that allows the control plane to function, distributing necessary information to WAN Edge routers to build secure tunnels and enforce policies, regardless of the underlying transport.](#_Toc496778511)

  ------------------------------------------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[OMP Communication](#_Toc496778511)

[The centralized intelligence of OMP is a significant departure from traditional network designs, making its unique contribution a key concept to grasp.](#_Toc496778511)

[OMP communication forms secure peering sessions across the Cisco Catalyst SD-WAN fabric, establishing the essential communication backbone for the entire overlay network.](#_Toc496778511)

[These critical connections occur:](#_Toc496778511)

-   
-   

[**Between WAN Edge routers and Cisco Catalyst SD-WAN Controllers:** WAN Edge routers establish OMP peering sessions with Cisco Catalyst SD-WAN Controllers to exchange routing, policy, and management information.**Between Cisco Catalyst SD-WAN Controllers themselves:** In deployments with multiple Cisco Catalyst SD-WAN Controllers, they form OMP peering sessions with each other to ensure synchronization of control plane information and maintain redundancy.](#_Toc496778511)

+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [![Analogy icon.](media/image6.bin){width="0.9741929133858268in" height="0.9741929133858268in"}](#_Toc496778511) | [**Think Like an Engineer: Understanding the \"Glue\"**](#_Toc496778511)                                                                                                                                                                                                     |
|                                                                                                                  |                                                                                                                                                                                                                                                                              |
|                                                                                                                  | [You\'ve heard OMP described as the \"glue\" that holds the Cisco Catalyst SD-WAN fabric together. How would you explain OMP\'s fundamental importance to a colleague who is only familiar with traditional distributed routing protocols like BGP or OSPF?](#_Toc496778511) |
|                                                                                                                  |                                                                                                                                                                                                                                                                              |
|                                                                                                                  | -                                                                                                                                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[Consider how OMP centralizes control plane information, simplifies policy distribution, and enables scalability across a dynamic, multitransport WAN.](#_Toc496778511)

[Key Characteristics and Functions of OMP](#_Toc496778511)

[OMP is a TCP-based scalable control plane protocol that forms the backbone of the Cisco Catalyst SD-WAN overlay. It runs inside secure ~~TLS~~ **Transport Layer Security (TLS)** [Explanation: Acronym 'TLS' not expanded on first use. Category: Acronyms]/DTLS connections, establishing peering sessions between WAN Edge routers and Cisco Catalyst SD-WAN Controllers, as well as between Cisco Catalyst SD-WAN Controllers themselves.](#_Toc496778511)

[At a ~~high level~~ **Change 'high level' to 'high-level'** [Explanation: Hyphenate 'high-level' when used as a compound modifier. Category: Grammar & Punctuation], OMP is responsible for several critical functions:](#_Toc496778511)

-   
-   

[**Reachability Information:** OMP advertises how different parts of the network can be reached. This includes information about WAN Edge router interfaces (Transport Locators or TLOCs) and network destinations (service-side routes).**Policy and Key Distribution:** OMP distributes vital IPsec encryption keys, which are essential for establishing secure data plane tunnels between WAN Edge devices. Additionally, it disseminates data and application-aware policies to WAN Edge routers, ensuring consistent policy enforcement throughout the fabric.](#_Toc496778511)

[OMP operates as a control plane protocol that is automatically enabled during device bring-up. Once SD-WAN Controllers and WAN Edge routers are operational, they automatically ~~initiate~~ **start** [Explanation: 'start' or 'begin' instead of 'initiate'. Category: Cisco Style Guide] OMP peering sessions over secure DTLS connections, utilizing AES-256 key encryption for robust security. The two IP endpoints of an OMP session are the system IP addresses of the two communicating devices.](#_Toc496778511)

[**OMP\'s Role**](#_Toc496778511)

[OMP is the central protocol for overlay routing, which is a fundamental part of the Cisco Catalyst SD-WAN network.](#_Toc496778511)

[Its role includes:](#_Toc496778511)

-   
-   

[Exchanging routing, policy, and management information between the SD-WAN Controllers and WAN Edge routers across the overlay network.Ensuring the entire SD-WAN fabric operates cohesively and securely.](#_Toc496778511)

[1. Which three of the following are true about OMP? (choose three)](#_Toc496778511)

[A. Allows routes to be distributed from the SD-WAN Manager to WAN Edge routers.](#_Toc496778511)

[B. Allows routes to be distributed from the Cisco Catalyst SD-WAN Controller to the WAN Edge routers.](#_Toc496778511)

[C. Automatically enabled at bring-up.](#_Toc496778511)

[D. It is established over secure DTLS connections.](#_Toc496778511)

[E. Must be manually enabled during onboarding.](#_Toc496778511)

[F. OMP is a UDP-based control plane protocol.](#_Toc496778511)

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [![http://schemas.openxmlformats.org/drawingml/2006/picture](media/image7.bin){width="1.8193547681539808in" height="2.6064512248468943in"}](#_Toc496778511) | [**Key Takeaway: The Central Nervous System of Your Cisco Catalyst SD-WAN**](#_Toc496778511)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                             | [The Overlay Management Protocol (OMP) is fundamental to the intelligence and dynamic capabilities of your Cisco Catalyst SD-WAN deployment.](#_Toc496778511)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                             | [By understanding OMP, you can:](#_Toc496778511)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                             | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                             | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                             | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                             | [**Appreciate Centralized Intelligence:** Recognize how OMP centralizes control plane information, simplifying routing and policy distribution across the entire overlay.**Ensure Seamless Communication:** Understand its role in establishing secure connections and exchanging critical information (like TLOCs and encryption keys) between SD-WAN Controllers and WAN Edge routers.**Troubleshoot Effectively:** Pinpoint issues related to route propagation, policy application, or secure tunnel establishment by verifying OMP\'s operational status and advertised information.This knowledge is crucial for designing, deploying, and maintaining a scalable, policy-driven, and secure SD-WAN fabric.](#_Toc496778511) |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[[]{#_Toc215687659 .anchor}Cisco Catalyst SD-WAN: Orchestration~~ & ~~ **Change '&' to 'and'** [Explanation: 'and' instead of '&' in prose text. Category: Grammar & Punctuation]Control - Bringing the Fabric to Life](#_Toc496778511)

[[]{#_Toc215687660 .anchor}Lab 1: Access and Monitor Cisco Catalyst SD-WAN Components](#_Toc496778511)

[Introduction](#_Toc496778511)

[Cisco Catalyst SD-WAN Manager provides centralized monitoring and management of SD-WAN fabric components, including WAN Edge devices and controllers. It offers real-time visibility into device health, performance, and connectivity through an intuitive, dashboard-driven interface.\
\
You will use Cisco Catalyst SD-WAN Manager to explore the Overview Dashboard, drill down into Device Dashboards and the Device 360 view for WAN Edge devices and controllers. You will also learn how to use some of the built-in troubleshooting tools to identify and analyze potential issues in the SD-WAN fabric.](#_Toc496778511)

[Topology](#_Toc496778511)

[![](media/image15.bin){width="6.94027668416448in" height="3.1206681977252844in"}](#_Toc496778511)

[Topology Description](#_Toc496778511)

[The lab environment contains a small Cisco Catalyst SD-WAN fabric with one data center site and two branch sites. The data center site hosts two Cisco Catalyst 8000V WAN Edge routers, while each branch site has a single WAN Edge router, for a total of four WAN Edges. All WAN Edge devices use dual underlay transport (Internet and MPLS), and participate in a common SD-WAN overlay.\
\
The control plane consists of one Cisco Catalyst SD-WAN Manager, one Cisco Catalyst SD-WAN Validator, and one Cisco Catalyst SD-WAN Controller, which are placed in a separate controller network reachable from both WAN Edge underlays. All SD-WAN devices, including the controllers and WAN Edges, also connect to a shared management network used for out-of-band management and reachability from the Jump Host, which provides browser access to Cisco Catalyst SD-WAN Manager.](#_Toc496778511)

[Each student pod contains the following elements:](#_Toc496778511)

-   
-   
-   
-   
-   
-   
-   
-   
-   

[One Cisco Catalyst SD-WAN ManagerOne Cisco Catalyst SD-WAN ValidatorOne Cisco Catalyst SD-WAN ControllerFour Cisco Catalyst 8000V WAN Edge RoutersOne site router at the DC siteTwo provider clouds, Internet, and MPLSThree endpoints at the three sitesOne Certificate AuthorityOne Jump Host for web browser access to Cisco Catalyst SD-WAN Manager](#_Toc496778511)

[Job Aid](#_Toc496778511)

[The following job aid will help you complete the lab activities.](#_Toc496778511)

[Device Credentials](#_Toc496778511)

  ------------------------------------------------------------------------------------------------------------------------------------------------------------
  [Device](#_Toc496778511)           [Interface](#_Toc496778511)   [Management IP](#_Toc496778511)   [Username](#_Toc496778511)   [Password](#_Toc496778511)
  ---------------------------------- ----------------------------- --------------------------------- ---------------------------- ----------------------------
  [Jump Host](#_Toc496778511)        [GUI](#_Toc496778511)         [10.0.0.251](#_Toc496778511)      [student](#_Toc496778511)    [1234QWer](#_Toc496778511)

  [SD-WAN Manager](#_Toc496778511)   [CLI/Web](#_Toc496778511)     [10.0.0.102](#_Toc496778511)      [admin](#_Toc496778511)      [1234QWer](#_Toc496778511)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------

[IP Addressing](#_Toc496778511)

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [Device](#_Toc496778511)             [Site ID](#_Toc496778511)   [Interface](#_Toc496778511)   [VPN Membership](#_Toc496778511)   [Color](#_Toc496778511)             [Device IP](#_Toc496778511)         [Default Gateway](#_Toc496778511)
  ------------------------------------ --------------------------- ----------------------------- ---------------------------------- ----------------------------------- ----------------------------------- -----------------------------------
  [SD-WAN Validator](#_Toc496778511)   [100](#_Toc496778511)       [ge0/0](#_Toc496778511)       [0](#_Toc496778511)                                                    [192.168.66.3/24](#_Toc496778511)   [192.168.66.1](#_Toc496778511)

  [DC-Edge1](#_Toc496778511)           [10](#_Toc496778511)        [Gi3](#_Toc496778511)         [0](#_Toc496778511)                [public-internet](#_Toc496778511)   [172.16.0.101/24](#_Toc496778511)   [172.16.0.1](#_Toc496778511)
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Management Network](#_Toc496778511)

[![](media/image16.bin){width="6.94027668416448in" height="3.08330927384077in"}](#_Toc496778511)

[Scenario](#_Toc496778511)

[You are delivering an internal knowledge transfer to new NOC engineers in a lab environment. You will use Cisco Catalyst SD-WAN Manager to demonstrate how the platform monitors and manages SD-WAN devices. You will tour the different panes of the Overview Dashboard and drill down into the Device Dashboards and Device 360 View. Here, you will walk through the different options detailing the status and performance of different WAN Edge devices and controllers. You will demonstrate ~~SSH~~ **Secure Shell (SSH)** [Explanation: Acronym 'SSH' not expanded on first use. Category: Acronyms] Terminal Access for targeted CLI checks and showcase the usage of the built-in troubleshooting tools for proactive issue identification.](#_Toc496778511)

[The lab environment contains a small Cisco Catalyst SD-WAN fabric with one data center site and two branch sites. The data center site hosts two Cisco Catalyst 8000V WAN Edge routers, while each branch site has a single WAN Edge router, for a total of four WAN Edges. All WAN Edge devices use dual underlay transport (Internet and MPLS), and participate in a common SD-WAN overlay.\
\
The control plane consists of one Cisco Catalyst SD-WAN Manager, one Cisco Catalyst SD-WAN Validator, and one Cisco Catalyst SD-WAN Controller, which are placed in a separate controller network reachable from both WAN Edge underlays. All SD-WAN devices, including the controllers and WAN Edges, also connect to a shared management network used for out-of-band management and reachability from the Jump Host, which provides browser access to Cisco Catalyst SD-WAN Manager.](#_Toc496778511)

[Upon completion of this lab exercise, you will be able to:](#_Toc496778511)

-   
-   
-   
-   
-   
-   

[Access Cisco Catalyst SD-WAN Manager.Navigate Cisco Catalyst SD-WAN Manager main dashboard panes.Monitor the Cisco Catalyst SD-WAN Controller devices from the device dashboard.Monitor the WAN Edge devices from the device dashboard.Use the SSH Terminal tool to access a device CLI.Use Cisco Catalyst SD-WAN Manager troubleshooting tools to verify basic overlay network connectivity.](#_Toc496778511)

[Task 1: Access the Cisco Catalyst SD-WAN Manager Overview Dashboard](#_Toc496778511)

[In this task, you will log in to the Cisco Catalyst SD-WAN Manager and familiarize yourself with the different panes of the Overview Dashboard.](#_Toc496778511)

[Activity](#_Toc496778511)

[**Step ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** Access the **Jump Host**.](#_Toc496778511)

[In your lab environment, click the **Jump Host** from the list of available devices.](#_Toc496778511)

[**Step 2** Open a browser and click the **Manager bookmark** or enter one of the following URLs in the address bar: **https://manager** or **https://10.0.0.102**.](#_Toc496778511)

[Double-click a browser icon on the Jump Host desktop.](#_Toc496778511)

[![](media/image17.bin){width="6.940277777777778in" height="3.753030402449694in"}](#_Toc496778511)

[Click the Manager bookmark or enter one of the following URLs in the address bar: https://manager or https://10.0.0.102.](#_Toc496778511)

+------------------------------------------------------------------------------------------------------------+
| 1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation][Accept and proceed past any security warnings caused by the self-signed certificate.](#_Toc496778511) |
+============================================================================================================+
+------------------------------------------------------------------------------------------------------------+

[![](media/image18.bin){width="6.94027668416448in" height="3.7642180664916887in"}](#_Toc496778511)

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation][If the Cisco Catalyst SD-WAN Manager login page does not load or login fails, please wait a few minutes while the virtual environment finishes to ~~boot up~~ **start** [Explanation: 'start' or 'boot' instead of 'boot up'. Category: Cisco Style Guide]. Then, refresh the browser page inside the lab.](#_Toc496778511) |
+=================================================================================================================================================================================================================================+
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[**Step ~~3~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** Log in to Cisco Catalyst SD-WAN Manager. Use **admin** as the username and **1234QWer** as the password.](#_Toc496778511)

[Enter **admin** as the Username and click **Continue**. After the Password field appears, enter **1234QWer** and click **Log in**.](#_Toc496778511)

[![](media/image19.bin){width="6.940277777777778in" height="3.7625853018372704in"}](#_Toc496778511)

[**Step ~~4~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** Once logged in, the **Monitor** \> **Overview** dashboard is opened as the landing page. Explore the various panes available on the dashboard.](#_Toc496778511)

[Scroll down to view all the available panes.](#_Toc496778511)

[![](media/image20.bin){width="6.940277777777778in" height="2.9032163167104112in"}](#_Toc496778511)

[At the top of the Overview dashboard, the Control Components and WAN Edges panes display the total number of Cisco Catalyst SD-WAN Controllers and WAN Edge router instances in the overlay network along with the reachability status of the devices. The Certificate Status pane displays the state of all certificates on all controller devices and shows a count of all expired or invalidated certificates. The Licensing pane displays the total number of devices configured and the number of devices licensed. The Reboot pane displays the number of Cisco Catalyst SD-WAN Manager reboots in the last 24 hours.](#_Toc496778511)

[![](media/image21.bin){width="6.94027668416448in" height="0.5725623359580052in"}](#_Toc496778511)

[**Step ~~5~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** Click the drop-down list on the left and change the time range for the data displayed in the dashlets to ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] hour. Inspect the change to the displayed data and change it back to 24 hours.](#_Toc496778511)

[By default, data for the last 24 hours is displayed on the dashboard.](#_Toc496778511)

[![](media/image22.bin){width="6.94027668416448in" height="2.8980194663167103in"}](#_Toc496778511)

[**Step ~~6~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** Examine the Site Health dashlet.](#_Toc496778511)

[This dashlet displays health, which is calculated by the average Quality of Experience (QoE) across all sites. The site health depends on the health metrics of devices, tunnels, and applications at that site.](#_Toc496778511)

[There are three states for Site Health:](#_Toc496778511)

-   
-   
-   

[**Good:** All applications, WAN Edge devices, and tunnels are in good state.**Fair:** Any one application, WAN Edge device, or tunnel in fair state.**Poor:** Any one application, WAN Edge device, or tunnel in poor state.![](media/image23.bin){width="5.606451224846894in" height="2.812902449693788in"}](#_Toc496778511)

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 3~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation][The Site Health dashlet can display the \"No data for this timeframe\" message after the lab is initialized, because it does not have sufficient historical data to calculate the health score. It can take up to 15 minutes for the real data to be displayed. This issue will also impact other dashlets.](#_Toc496778511) |
+===================================================================================================================================================================================================================================================================================================================================+
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[**Step ~~7~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** Examine the Tunnel Health dashlet.](#_Toc496778511)

[This dashlet displays the health of all tunnel endpoints, based on average latency, loss, and jitter. You can also filter the tunnel information based on the health status using the drop-down list for Good Tunnels, Fair Tunnels, and Poor Tunnels, and Latency, Loss, and Jitter.](#_Toc496778511)

[![](media/image24.bin){width="5.625805993000875in" height="2.8258059930008748in"}](#_Toc496778511)

[**Step ~~8~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** Examine the WAN Edge Health dashlet.](#_Toc496778511)

[This dashlet displays an aggregated view for each router state and a count of how many WAN Edge routers are in individual states.](#_Toc496778511)

[There are three states for WAN Edge routers:](#_Toc496778511)

-   
-   
-   

[**Good:** Number of routers with memory, hardware, and CPU in good state. Using less than 75% of total memory or total CPU is classified as good.**Fair:** Number of routers with memory, hardware, or CPU in fair state. Using between 75 and 90% of total memory or total CPU is classified as in a fair state.**Poor:** Number of routers with memory, hardware, or CPU in poor state. Using more than 90% of total memory or total CPU is classified as in a poor state.![](media/image25.bin){width="5.632257217847769in" height="2.8387095363079613in"}](#_Toc496778511)

[**Step ~~9~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** Observe the Application Health dashlet.](#_Toc496778511)

[This dashlet displays the health of the usage of applications across sites, based on Quality of Experience (QoE) and bandwidth usage, with options to filter by performance status and view graphical or detailed table formats.](#_Toc496778511)

[Currently, no data is displayed in this dashlet because the lab does not include any user traffic on~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]the data can be calculated.](#_Toc496778511)

[![](media/image26.bin){width="5.632257217847769in" height="2.8516119860017497in"}](#_Toc496778511)

[**Step 10** Observe the Top Applications dashlet.](#_Toc496778511)

[This dashlet displays Cisco Catalyst SD-WAN Application Intelligence Engine (SAIE) and ~~SSL~~ **Secure Sockets Layer (SSL)** [Explanation: Acronym 'SSL' not expanded on first use. Category: Acronyms] Proxy flow information for traffic transiting WAN Edge routers in the overlay network. The dashlet shows the most used applications on the network.](#_Toc496778511)

[Currently, no data is displayed in this dashlet because the lab does not include any user traffic on~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]the data can be calculated.](#_Toc496778511)

[![](media/image27.bin){width="5.645160761154855in" height="2.858064304461942in"}](#_Toc496778511)

[**Step 11** Examine the WAN Edge Management dashlet.](#_Toc496778511)

[This dashlet shows the WAN Edge devices by Configuration Type. It displays how many WAN Edge devices configurations are centrally managed by Config Groups and Templates. The configuration of WAN Edges marked as Unlocked is not managed by Cisco Catalyst SD-WAN Manager and is therefore unlocked for direct, device-specific configuration changes, usually through CLI.](#_Toc496778511)

[![](media/image28.bin){width="5.645160761154855in" height="2.8451607611548555in"}](#_Toc496778511)

[**Step 12** Click the **drop pin** icon on the right of the **Monitor** \> **Overview** dashboard to switch to the Global Network View.](#_Toc496778511)

[This view displays sites and WAN Edge devices on a world map based on their configured location. You can also check out the other available views, such as the Table View or the Heatmap View.](#_Toc496778511)

[![](media/image29.bin){width="6.940277777777778in" height="3.0599989063867015in"}](#_Toc496778511)

[**Step 13** Click the User Profile menu in the top-right navigation bar to view details of the currently logged-in user.](#_Toc496778511)

[Here, you can access details like the role currently assigned to this user, log out, or inspect the user profile.](#_Toc496778511)

[![](media/image30.bin){width="6.94027668416448in" height="3.0512981189851267in"}](#_Toc496778511)

[**Step 14** Click the dashlets icon on the right of the dashboard to switch back to the default dashlets view of the **Monitor** \> **Overview** dashboard.](#_Toc496778511)

[You should see the default dashlets view.](#_Toc496778511)

[![](media/image31.bin){width="6.94027668416448in" height="2.929384295713036in"}](#_Toc496778511)

[**Step 15** Click the **Actions** drop-down list on the right to access the Dashboard Editor.](#_Toc496778511)

[Here, you can customize your Overview Dashboard. You can change the order in~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]the dashlets are displayed, remove dashlets you might not find critical, or add dashlets that you believe will benefit your use case.](#_Toc496778511)

[![](media/image32.bin){width="6.940277777777778in" height="2.925240594925634in"}](#_Toc496778511)

[**Step 16** Use the Dashboard Editor to customize your default Overview Dashboard view.](#_Toc496778511)

[You can do the following:](#_Toc496778511)

-   
-   
-   
-   

[**Drag and drop** a dashlet to change the order in~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]the dashlets are displayed.Click the **trash bin** icon on a dashlet to remove it from the dashboard.Click the **+ Add Dashlet** button in the top-right corner to add a dashlet.Click **Cancel** to discard or **Save** ~~to apply the~~ **Consider moving the adverb (e.g., 'to quickly configure' → 'to configure quickly')** [Explanation: avoiding split infinitives when possible. Category: Grammar & Punctuation] changes that you made.![](media/image33.bin){width="6.940277777777778in" height="3.3506014873140857in"}](#_Toc496778511)

[Activity Verification](#_Toc496778511)

[You have completed this task when you have:](#_Toc496778511)

-   
-   

[Successfully logged in to Cisco Catalyst SD-WAN Manager.Explored the various panes of the Cisco Catalyst SD-WAN Overview Dashboard.](#_Toc496778511)

[Task 2: View and Monitor Cisco Catalyst SD-WAN Controller Details](#_Toc496778511)

[In this task, you will view Cisco Catalyst SD-WAN Controller device details, device dashboard, and real-time information. You will also access the Cisco Catalyst SD-WAN Controller CLI by using the SSH Terminal tool.](#_Toc496778511)

[Activity](#_Toc496778511)

[**Step ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** From the Control Components pane of the Overview Dashboard, navigate to the list of Cisco Catalyst SD-WAN Controllers.](#_Toc496778511)

[In the Control Components pane of the Overview Dashboard, click **Controller** or the number above it to open the **Monitor** \> **Devices** dashboard. Accessing the Devices dashboard this way will automatically apply the filter ~~to only display~~ **Consider moving the adverb (e.g., 'to quickly configure' → 'to configure quickly')** [Explanation: avoiding split infinitives when possible. Category: Grammar & Punctuation] Cisco Catalyst SD-WAN Controllers.](#_Toc496778511)

[![](media/image34.bin){width="6.940277777777778in" height="2.930896762904637in"}](#_Toc496778511)

[**Step ~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** Use the scroll bar below the device list as needed to view all the columns.](#_Toc496778511)

[On the **Monitor** \> **Devices** dashboard, use the scroll bar below the device list as needed to view all the columns.](#_Toc496778511)

[![](media/image35.bin){width="6.940277777777778in" height="2.812563429571304in"}](#_Toc496778511)

[**Step ~~3~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** Click the **Controller** hostname to open the Device Dashboard for the chosen Cisco Catalyst SD-WAN Controller.](#_Toc496778511)

[The SD-WAN Controller hostname is located as shown in the following figure.](#_Toc496778511)

[![](media/image36.bin){width="6.940277777777778in" height="2.812563429571304in"}](#_Toc496778511)

[**Step ~~4~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** The **Monitor** \> **Devices** \> **Device** **360** window for the Cisco Catalyst SD-WAN Controller is displayed and shows its Control Connections by default. Scroll down and check the control connections.](#_Toc496778511)

[You should see multiple control connections from the Cisco Catalyst SD-WAN Controller to the other control components. There should also be multiple control connections from WAN Edge routers to the SD-WAN Controller.](#_Toc496778511)

[![](media/image37.bin){width="6.940277777777778in" height="3.3469061679790024in"}](#_Toc496778511)

[**Step ~~5~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** From the left-side menu, choose **Interface** to view interface statistics.](#_Toc496778511)

[The SD-WAN Controller reports three interfaces. The eth0 interface is part of VPN 512, which is the OOB management VPN. The eth1 interface is part of VPN 0 and is used for control connections to other Cisco Catalyst SD-WAN devices. The system interface is a logical interface with the system-ip.](#_Toc496778511)

[![](media/image38.bin){width="6.940277777777778in" height="3.2754680664916886in"}](#_Toc496778511)

[**Step ~~6~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** From the menu on the left, choose **Real Time**.](#_Toc496778511)

[By default, the Device Options search field displays System Information, which includes the device\'s hostname, site ID, and other information.](#_Toc496778511)

[![](media/image39.bin){width="6.94027668416448in" height="2.990757874015748in"}](#_Toc496778511)

[**Step ~~7~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** In the **Device Options** search field, choose **Interface Detail** and click **Apply** without selecting any filters.](#_Toc496778511)

[The Device Options search field should look like the following:](#_Toc496778511)

[![](media/image40.bin){width="6.940277777777778in" height="2.816137357830271in"}](#_Toc496778511)

[You may need to use the horizontal scroll bar at the bottom of the window to access additional information in the information table displayed.](#_Toc496778511)

[![](media/image41.bin){width="6.94027668416448in" height="2.908713910761155in"}](#_Toc496778511)

[**Step ~~8~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** Click the **Cisco Catalyst SD-WAN** logo in the top-left corner of the page to return to the main **Monitor** \> **Overview** dashboard.](#_Toc496778511)

[![](media/image42.bin){width="6.940277777777778in" height="2.8218318022747155in"}](#_Toc496778511)

[You can also access the **Monitor** \> **Overview** page using the menu.](#_Toc496778511)

[![](media/image43.bin){width="6.94027668416448in" height="2.513043525809274in"}](#_Toc496778511)

[**Step ~~9~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** From the Overview Dashboard, navigate to the list of Cisco Catalyst SD-WAN Controllers once more.](#_Toc496778511)

[In the Control Components pane of the Overview Dashboard, click **Controller** to open the **Monitor** \> **Devices** dashboard one more time.](#_Toc496778511)

[![](media/image44.bin){width="6.94027668416448in" height="2.9278729221347333in"}](#_Toc496778511)

[**Step 10** In the device table, click the **three dots** icon in the Action column on the far-right side of the SD-WAN Controller row. Choose the **SSH Terminal** option from the drop-down list.](#_Toc496778511)

[![](media/image45.bin){width="6.94027668416448in" height="2.9051487314085738in"}](#_Toc496778511)

[**Step 11** The **Tools \| SSH Terminal** window is displayed. Log in to the Cisco Catalyst SD-WAN Controller console using **admin** as the username and **1234QWer** as the password.](#_Toc496778511)

[You should see the following output.](#_Toc496778511)

[![](media/image46.bin){width="6.940277777777778in" height="2.4879549431321086in"}](#_Toc496778511)

[**Step 12** At the SD-WAN Controller command prompt, issue the **show system status** command.](#_Toc496778511)

[The output shows the status of the device along with information on any attached configuration or policy templates.](#_Toc496778511)

[![](media/image47.bin){width="6.940277777777778in" height="2.536076115485564in"}](#_Toc496778511)

[**Step 13** At the SD-WAN Controller command prompt, issue the **show interface** command.](#_Toc496778511)

[The output displays interface configuration and statistics.](#_Toc496778511)

[![](media/image48.bin){width="6.940277777777778in" height="2.53834208223972in"}](#_Toc496778511)

[**Step 14** Open the **SSH Terminal** tool from the main menu.](#_Toc496778511)

[Navigate to **Tools** \> **SSH Terminal** from the main menu to reach the SSH Terminal tool. Here, you can connect to all SD-WAN devices that are part of your fabric.](#_Toc496778511)

[![](media/image49.bin){width="6.940277777777778in" height="1.943705161854768in"}](#_Toc496778511)

[You can connect to a device by choosing it from the menu on the left. If you connect to several devices at the same time, the connections will be listed in tabs above the terminal window.](#_Toc496778511)

[![](media/image50.bin){width="6.940277777777778in" height="2.5392989938757657in"}](#_Toc496778511)

[Activity Verification](#_Toc496778511)

[You have completed this task when you have:](#_Toc496778511)

-   
-   
-   
-   

[Accessed the Cisco Catalyst SD-WAN Controller device details from the **Monitor** \> **Devices** dashboard.Monitored the Cisco Catalyst SD-WAN Controller control connections and interfaces from the **Monitor** \> **Devices** \> **Device** **360** dashboard.Accessed real-time information on the Cisco Catalyst SD-WAN Controller from the Device 360 dashboard.Accessed the Cisco Catalyst SD-WAN Controller CLI using the SSH Terminal tool.](#_Toc496778511)

[Task 3: View and Monitor WAN Edge Device Details](#_Toc496778511)

[In this task, you will view WAN Edge device details, device dashboard, and real-time information. You will also access the WAN Edge CLI using the SSH Terminal tool.](#_Toc496778511)

[Activity](#_Toc496778511)

[**Step ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** Return to the **Monitor** \> **Overview** page and in the WAN Edges pane, click the number of reachable WAN Edge devices to display the **Monitor** \> **Devices** dashboard for the WAN Edge routers that are up.](#_Toc496778511)

[The number of WAN Edge routers deployed in the overlay network that are currently unreachable will also be displayed next to the number of reachable WAN Edge routers.](#_Toc496778511)

[![](media/image51.bin){width="6.94027668416448in" height="2.92580271216098in"}](#_Toc496778511)

[**Step ~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** Extend the filters menu on the **Monitor** \> **Devices** dashboard.](#_Toc496778511)

[On the **Monitor** \> **Devices** dashboard, click the right arrow to expand the filters menu.](#_Toc496778511)

[![](media/image52.bin){width="6.94027668416448in" height="2.4952198162729657in"}](#_Toc496778511)

[Among other information the Devices list shows the number of control connections to the Cisco Catalyst SD-WAN Controllers, the number of BFD sessions (VPN tunnels) and available TLOCs. Notice that the DC WAN Edges have only ~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation] BFD sessions whereas the BR WAN Edge has 4. This is because the DC WAN Edges are assigned to the same site. By default, devices at the same site do not establish VPN tunnels between each other.](#_Toc496778511)

[**Step ~~3~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** Inspect the filters menu on the **Monitor** \> **Devices** dashboard.](#_Toc496778511)

[The **Filtered by** part of the Filters menu displays the currently applied filters, which are based on the link that you clicked on the main Overview dashboard. The **Filters** part contains all the available filters that you can use to narrow down the set of devices displayed in the table.](#_Toc496778511)

[![](media/image53.bin){width="6.940277777777778in" height="3.3525667104111987in"}](#_Toc496778511)

[You will notice that the WAN Edge devices have three control connections to the Cisco Catalyst SD-WAN controlers. There are only three control connections because WAN Edges only form a single control connection to Cisco Catalyst SD-WAN Manager by defaut. The other two of the three connections are to the Cisco Catalyst SD-WAN Controller one over each transport (one over internet and one over MPLS).\
The WAN Edges also have a number of active BFD sessions (VPN tunnels). Notice that DC WAN Edges have fewer BFD sessions than the Branch WAN Edges. This is because the DC WAN Edges are assigned to the same site and by default, devices at the same site do not establish BFD sessions between each other, so a DC WAN Edge only establishes a BFD session with one Branch WAN Edge, but the Branch WAN Edge establishes BFD sessions with both DC WAN Edges.](#_Toc496778511)

[**Step ~~4~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** Open the **DC-Edge2** Device 360 dashboard.](#_Toc496778511)

[On the **Monitor** \> **Devices** dashboard, click the **DC-Edge2** Hostname to open the **Monitor** \> **Devices** \> **Device 360** dashboard.](#_Toc496778511)

[![](media/image54.bin){width="6.940277777777778in" height="3.349003718285214in"}](#_Toc496778511)

[**Step ~~5~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** Inspect the **System Status** section for the DC-Edge2 WAN Edge router.](#_Toc496778511)

[The **Monitor** \> **Devices** \> **Device 360** shows the **System Status** section by default. It displays some basic information, statuses, and metrics for the DC-Edge2 WAN Edge.](#_Toc496778511)

[![](media/image55.bin){width="6.940277777777778in" height="3.3414818460192475in"}](#_Toc496778511)

[**Step ~~6~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** Open the **Interface** details section for DC-Edge2 and inspect the displayed chart and table.](#_Toc496778511)

[From the menu on the left, choose **Interface**. The top part displays the chart with the utilization of the interfaces by default. Scroll down to view details about individual interfaces in the interfaces table.](#_Toc496778511)

[![](media/image56.bin){width="6.940277777777778in" height="4.26057852143482in"}](#_Toc496778511)

[**Step ~~7~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** Change the displayed metric in the chart to **Pps**.](#_Toc496778511)

[Click the **Chart Options** and choose **Pps** (packets per second) from the drop-down list. You can add or remove individual interfaces from the chart by clicking them within the **Legend** on the right side of the chart.](#_Toc496778511)

[![](media/image57.bin){width="6.940277777777778in" height="2.242023184601925in"}](#_Toc496778511)

[**Step ~~8~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** Open the **Control Connections** section for DC-Edge2.](#_Toc496778511)

[From the menu on the left, choose **Control Connections**. You may have to scroll down the menu to display the **Control Connections** section. You will notice that there are two connections to the SD-WAN Controller, over both available transports, but only one connection to the SD-WAN Manager.](#_Toc496778511)

[![](media/image58.bin){width="6.940277777777778in" height="3.341878827646544in"}](#_Toc496778511)

[**Step ~~9~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** Open the **Real Time** section for DC-Edge2.](#_Toc496778511)

[From the menu on the left, choose **Real Time**. By default, the Device Options search field displays System Information.](#_Toc496778511)

[![](media/image59.bin){width="6.94027668416448in" height="2.9301017060367456in"}](#_Toc496778511)

[**Step 10** Verify the status of the **Control Connections** in the **Real Time** section.](#_Toc496778511)

[In the **Device Options** search field, choose **Control Connections**. Click **Apply** without modifying the filters to display all control connections.](#_Toc496778511)

[![](media/image60.bin){width="6.94027668416448in" height="2.9265365266841643in"}](#_Toc496778511)

[The WAN Edge router has two control connections to the SD-WAN Controller, one through the *public-internet* network and one through the *mpls* network.](#_Toc496778511)

[![](media/image61.bin){width="6.94027668416448in" height="1.9534011373578302in"}](#_Toc496778511)

[**Step 11** Click the **Cisco Catalyst SD-WAN** logo in the top-left corner to return to the **Monitor** \> **Overview** dashboard.](#_Toc496778511)

[![](media/image62.bin){width="6.940277777777778in" height="1.9523982939632545in"}](#_Toc496778511)

[Activity Verification](#_Toc496778511)

[You have completed this task when you have:](#_Toc496778511)

-   
-   
-   

[Accessed the WAN Edge device details from the **Monitor** \> **Device** dashboard.Monitored the WAN Edge control connections and interfaces from the **Monitor** \> **Devices** \> **Device** **360** dashboard.Accessed real-time control connection information on the WAN Edge from the **Monitor** \> **Devices** \> **Device** **360** dashboard.](#_Toc496778511)

[Task 4: View and Monitor Cisco Catalyst SD-WAN Validator Device Details](#_Toc496778511)

[In this task, you will view Cisco Catalyst SD-WAN Validator device details, device dashboard, and real-time information. You will also perform basic overlay network connectivity troubleshooting using the Cisco Catalyst SD-WAN Manager troubleshooting tools.](#_Toc496778511)

[Activity](#_Toc496778511)

[**Step ~~1~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** From the Control Components pane of the Overview Dashboard, navigate to the list of Cisco Catalyst SD-WAN Validators.](#_Toc496778511)

[In the Control Components pane of the Overview Dashboard, click **Validator** or the number above it to open the **Monitor** \> **Devices** dashboard. Accessing the Devices dashboard this way will automatically apply the filter ~~to only display~~ **Consider moving the adverb (e.g., 'to quickly configure' → 'to configure quickly')** [Explanation: avoiding split infinitives when possible. Category: Grammar & Punctuation] Cisco Catalyst SD-WAN Validators.](#_Toc496778511)

[![](media/image63.bin){width="6.94027668416448in" height="2.908713910761155in"}](#_Toc496778511)

[**Step ~~2~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** Explore the SD-WAN Validator device information.](#_Toc496778511)

[The device model is Validator. It is based on a vEdge Cloud device image and its role is to orchestrate the initial control-plane bring-up for all devices that are part of the fabric. The device is reported as Healthy and Reachable. The row also includes other properties or statuses of the SD-WAN Validator. You may need to use the scroll bar below the device list to view all the columns.](#_Toc496778511)

[![](media/image64.bin){width="6.94027668416448in" height="2.098556430446194in"}](#_Toc496778511)

[**Step ~~3~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** Open the **Validator** Device 360 dashboard.](#_Toc496778511)

[Click the **Validator** Hostname to open the **Monitor** \> **Devices** \> **Device 360** dashboard.](#_Toc496778511)

[![](media/image65.bin){width="6.94027668416448in" height="2.09747375328084in"}](#_Toc496778511)

[**Step ~~4~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** Inspect the **Orchestrator** **Connections** section for the Validator.](#_Toc496778511)

[The **Orchestrator Connections** section is displayed by default. The Control Connections between the SD-WAN Validator and other devices are referred to as Orchestrator Connections on the SD-WAN Validator.](#_Toc496778511)

[![](media/image66.bin){width="6.940277777777778in" height="3.177088801399825in"}](#_Toc496778511)

[**Step ~~5~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** Inspect the **Interface** section for the SD-WAN Validator.](#_Toc496778511)

[Click **Interface** from the menu on the left. Notice that interface statistics are not available for the vEdge Cloud (Validator) device. The interfaces list displays the statuses and configuration of the interfaces.](#_Toc496778511)

[![](media/image67.bin){width="6.940277777777778in" height="2.6267268153980754in"}](#_Toc496778511)

[**Step ~~6~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** Navigate to the **Ping** connectivity tool in the **Troubleshooting** section.](#_Toc496778511)

[From the menu on the left, choose **Troubleshooting**. The **Connectivity** pane will be displayed. Click **Ping** to choose this connectivity tool.](#_Toc496778511)

[![](media/image68.bin){width="6.94027668416448in" height="2.1850995188101487in"}](#_Toc496778511)

[**Step 7** Test connectivity to the DC-Edge1 WAN Edge router public-internet IP using **10 ICMP** probes. Use **ge0/0** as the source interface, **VPN - 0** as the VPN, and **172.16.0.101** as the destination IP.](#_Toc496778511)

[In the Ping tool, choose or enter the following:](#_Toc496778511)

-   
-   
-   
-   

[Source/Interface for VPN - 0: **ge0/0** **~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation] ipv4 ~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation] 192.168.66.3**VPN: **VPN~~--~~ **—** [Explanation: em dash (—) instead of double hyphen (--). Category: Grammar & Punctuation]0**Destination IP Address: **172.16.0.101**Click **Advanced Options** and enter **10** for the Count.Click the **Ping** button to start the ping.](#_Toc496778511)

[![](media/image69.bin){width="6.94027668416448in" height="2.459573490813648in"}](#_Toc496778511)

[Check the results of the ping requests. The Summary on the left side of the result contains information about the number of packets sent and received and the ~~average, maximum and minimum~~ **Add comma before 'and' (e.g., 'A, B, and C')** [Explanation: adding serial comma before 'and' in list of three or more.... Category: Grammar & Punctuation] round-trip time. The output on the right side contains the actual command used in the test and its complete output.](#_Toc496778511)

[![](media/image70.bin){width="6.940277777777778in" height="2.3324464129483813in"}](#_Toc496778511)

[**Step ~~8~~ **Spell out the number (e.g., '3 items' → 'three items')** [Explanation: spelling out numbers one through nine in prose. Category: Grammar & Punctuation]** Return to the **Monitor** \> **Overview** dashboard.](#_Toc496778511)

[Click the **Cisco Catalyst SD-WAN** logo in the top-left corner to return to the **Monitor** \> **Overview** dashboard.](#_Toc496778511)

[![](media/image71.bin){width="6.94027668416448in" height="2.3312489063867017in"}](#_Toc496778511)

[Activity Verification](#_Toc496778511)

[You have completed this task when you have:](#_Toc496778511)

-   
-   
-   

[Accessed the Cisco Catalyst SD-WAN Validator device details from the **Monitor** \> **Devices** dashboard.Monitored the Cisco Catalyst SD-WAN Validator orchestrator connections and interfaces from the **Monitor** \> **Devices** \> **Device** **360** dashboard.Used the Cisco Catalyst SD-WAN Manager troubleshooting tools to perform basic overlay network troubleshooting.](#_Toc496778511)

[[]{#_Toc215687661 .anchor}Summary](#_Toc496778511)

[Congratulations~~!~~ **Consider using a period instead of exclamation point** [Explanation: removing exclamation point from technical content. Category: Grammar & Punctuation] You have successfully completed the Cisco Catalyst SD-WAN: Components and Roles course, deepening your understanding of the essential building blocks that form a modern, intelligent WAN. Throughout this course, you moved beyond the foundational concepts to explore the critical components that orchestrate and manage the SD-WAN fabric. You learned about the \"brains\" that control policy and routing, the \"gatekeepers\" that ensure secure device onboarding, the \"command center\" for daily operations, and the \"workhorses\" that connect your sites.](#_Toc496778511)

[Using real-world scenarios, you gained practical insights into how these components interact and how to select the right platforms for diverse deployment needs. This knowledge is crucial for anyone involved in designing, deploying, or managing a Cisco Catalyst SD-WAN solution.\
](#_Toc496778511)

[What You Learned](#_Toc496778511)

[You are now proficient in the following essential building blocks:](#_Toc496778511)

-   
-   
-   
-   

[**SD-WAN Controllers:** Described the critical role of Cisco Catalyst SD-WAN Controllers in centralizing the control plane, distributing policies, and managing routing intelligence.**SD-WAN Validators:** Identified the distinct responsibilities of Cisco Catalyst SD-WAN Validators in device authentication, secure onboarding, and facilitating NAT traversal.**SD-WAN Manager:** Explained the operational benefits of centralized management provided by Cisco Catalyst SD-WAN Manager for provisioning, monitoring, and troubleshooting, and navigated its intuitive GUI.**WAN Edge Routers:** Distinguished between various Cisco Catalyst WAN Edge router platforms (physical and virtual) and selected appropriate models for different deployment scenarios based on their capabilities and form factors.](#_Toc496778511)

[What Does This Mean for Your Day-to-Day Work?](#_Toc496778511)

[Now that you understand the core components of Cisco Catalyst SD-WAN, you can apply this knowledge in practical ways---whether you\'re troubleshooting an onboarding issue, planning a new branch rollout, or optimizing network performance. Every component you\'ve learned about plays a vital role in ensuring the agility, security, and manageability of the networks you support.](#_Toc496778511)

[You can apply this knowledge in the following ways:](#_Toc496778511)

-   
-   
-   
-   

[**Diagnose Component Issues:** Accurately identify~~ which ~~ **If this is a restrictive clause, use 'that' instead of 'which'** [Explanation: using 'that' for restrictive clauses (no comma before 'wh.... Category: Grammar & Punctuation]SD-WAN component is responsible for specific network behaviors or issues.**Plan Deployments:** Make informed decisions about the placement and type of Controllers, Validators, and WAN Edge routers for optimal performance and cost-efficiency.**Utilize Management Tools:** Effectively use Cisco Catalyst SD-WAN Manager for comprehensive monitoring, efficient provisioning, and streamlined troubleshooting.**Communicate Architecture:** Clearly articulate the roles and interactions of SD-WAN components to both technical and non-technical stakeholders.](#_Toc496778511)

[What\'s Next?](#_Toc496778511)

[The journey into Cisco Catalyst SD-WAN is continuous. Continue exploring topics like advanced policy configuration, specific deployment models, and in-depth troubleshooting techniques to further enhance your expertise.](#_Toc496778511)

[Your journey does not stop here. Keep learning. Keep growing.](#_Toc496778511)

[[]{#_Toc215687662 .anchor}Summary Challenge](#_Toc496778511)

[[]{#_Toc215687663 .anchor}Answer Key](#_Toc496778511)

[Controllers and Validators](#_Toc496778511)

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]

[C](#_Toc496778511)

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]

[C](#_Toc496778511)

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]

[B](#_Toc496778511)

[SD-WAN Manager](#_Toc496778511)

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]

[B](#_Toc496778511)

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]

[A](#_Toc496778511)

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]

[C](#_Toc496778511)

[WAN Edge Routers: Physical~~ & ~~ **Change '&' to 'and'** [Explanation: 'and' instead of '&' in prose text. Category: Grammar & Punctuation]Virtual](#_Toc496778511)

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]

[C](#_Toc496778511)

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]

[C](#_Toc496778511)

[Overlay Management Protocol (OMP): The Control Plane Glue](#_Toc496778511)

1~~.  ~~ **. ** [Explanation: single space after period. Category: Grammar & Punctuation]

[B, C, D](#_Toc496778511)

[Summary Challenge](#_Toc496778511)


---

## Change Legend

| Markup | Meaning |
|--------|---------|
| ~~text~~ | Text to remove (strikethrough) |
| **text** | Text to add (bold) |
| [Explanation: ...] | Rationale for change |

*Generated by Course AI Editor on 2026-03-04 15:15*