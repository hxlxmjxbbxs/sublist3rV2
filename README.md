<p align="center">
<a href="https://github.com/hxlxmjxbbxs/SUBLIST3R_V2.0"><img src="assets/img (1).jpg" width=250px align="center"></a>
</p>

# SUBLISTER VERSION 2.0

## Overview
Sublist3r v2.0 is a sophisticated tool specializing in automated subdomain enumeration designed for penetration testers and security researchers. This advanced version builds upon the robust foundation of Sublist3r v1.0, integrating significant enhancements and novel features to offer a more dynamic and efficient tool for unearthing subdomains of any given domain.

### 🌟 What's New

- Resolved Virustotal API integration issues, enhancing data reliability and enumeration scope. 
- Added ShrewdEye for broader and more unique subdomain discovery.
- Refined and optimized enumerator modules for various search engines, ensuring more efficient data retrieval and processing.
- Improved error handling and performance optimization.
- Advanced port scanning capabilities, complementing subdomain enumeration with network service insights.


### 📸 Code Comparison Snapshot
Above: A visual comparison showcasing the differences between the old implementation and my updated version.

<p align="center">
<a href="https://github.com/aboul3la/Sublist3r/compare/master...hxlxmjxbbxs:Sublist3r:fix-virustotal-api-compatibility"><img src="assets/img (3).jpg" align="center"></a>
</p>

### Key Updates
In Sublist3r v1.0, there were notable issues related to Virustotal integration, as reported by users on the [GitHub issues page](https://github.com/aboul3la/Sublist3r/issues?page=2&q=is%3Aissue+is%3Aopen+virustotal). 

<p align="center">
<a href="https://github.com/hxlxmjxbbxs/SUBLIST3R_V2.0"><img src="assets/img (4).jpg" align="center"></a>
</p>

These issues primarily involved:
#### 🚫 Virustotal Blocking Requests: 
- Users frequently encountered problems where Virustotal was blocking the requests made by Sublist3r. This issue significantly hindered the tool's ability to fetch subdomain data from Virustotal, thereby reducing its effectiveness.

#### ❌ API Integration Challenges: 
- There were difficulties in integrating with the Virustotal API correctly, which may include problems with API keys or changes in the API itself that were not reflected in Sublist3r.

#### 😞 User Experience: 
- Due to these integration issues, users often had to resort to temporary fixes, such as skipping Virustotal during enumeration or manually commenting out related code segments. This not only affected the tool's user-friendliness but also its efficiency in subdomain enumeration.

#### ✅ In Sublist3r v2.0: 
All these specific issues have been addressed and optimized to ensure a smoother, more reliable integration with Virustotal. Additionally, the integration of ShrewdEye as a new source for subdomain enumeration adds to the tool's capabilities, enhancing its overall performance and the breadth of its attack surface. This update positions Sublist3r v2.0 as a more robust and reliable tool for subdomain discovery in security assessments and penetration testing scenarios.

### 🛠 Installation & Setup
System Requirements

#### Python Version:
Sublist3r supports Python 2 (2.7.x) and Python 3 (3.4.x).

### Installing Sublist3r

Clone the repository:

```bash
git clone https://github.com/hxlxmjxbbxs/SUBLIST3R_V2.0
```

### Dependencies
Sublist3r depends on requests, dnspython, and argparse. 
These can be installed using the requirements file:

### Windows:
```bash
c:\python27\python.exe -m pip install -r requirements.txt
```

### Linux:
```bash
sudo pip install -r requirements.txt
```

### Additional Windows Dependencies

For coloring support in the Windows terminal, install win_unicode_console and colorama:
```bash
C:\python27\python.exe -m pip install win_unicode_console colorama
```

### ⚙️ Usage Instructions
```bash
Usage: python sublist3r.py [Options]

Options:
  -d, --domain         Domain name to enumerate subdomains
  -b, --bruteforce     Enable the subbrute bruteforce module
  -p, --ports          Scan the found subdomains against specified tcp ports
  -v, --verbose        Enable verbosity and display results in real-time
  -t, --threads        Number of threads to use for subbrute bruteforce
  -e, --engines        Specify a comma-separated list of search engines
  -o, --output         Save the results to text file
  -n, --no-color       Output without color

Example:
  python sublist3r.py -d example.com -v -t 30 -o output.txt

```

Enumerate subdomains for a specific domain:

```bash
python sublist3r.py -d example.com
```

### 📄 License

Sublist3r is distributed under the GNU GPL license, which allows for widespread use and modification. For more details, please refer to the [LICENSE](https://github.com/hxlxmjxbbxs/SUBLIST3R_V2.0/blob/main/LICENSE).

### 🤝 Credits and Acknowledgements

* [Ahmed Aboul-Ela](https://github.com/bitquark) - The original creator of **Sublist3r**.
* [TheRook](https://github.com/TheRook) - The bruteforce module was based on his script **subbrute**. 
* [Bitquark](https://github.com/bitquark) - The Subbrute's wordlist was based on his research **dnspop**. 

## Thanks

* Special Thanks to [Ibrahim Mosaad](https://twitter.com/ibrahim_mosaad) for his great contributions that helped in improving the tool.

### 📢 Version

<p align="center">
<a href="https://github.com/hxlxmjxbbxs/SUBLIST3R_V2.0"><img src="assets/img (2).jpg" align="center"></br></a></br>
<strong>Current Version:</strong> 2.0
</p>
