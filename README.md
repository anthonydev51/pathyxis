# Pathyxis

  

![Pathyxis Logo](public/logo.png)

  

Pathyxis is a web-based malware scanning tool designed to provide fast and reliable detection of malicious files by combining heuristic analysis with VirusTotal's powerful scanning engine.

  

---

  

## Features

  

-  **File Upload Scanning:** Upload files easily through a simple web interface for instant malware detection.

-  **VirusTotal Integration:** Leverages the VirusTotal API to access a vast database of malware signatures.

-  **Heuristic Analysis:** Performs basic heuristic checks to detect suspicious file patterns beyond known signatures.

-  **Real-time Feedback:** Displays near real-time scanning results to users.

-  **Open Source & Lightweight:** Built with Python (Flask) and a modern frontend stack, easy to deploy and customize.

-  **Privacy-Focused:** Files are scanned securely with no unnecessary data retention.

  

---

  

## Getting Started

  

### Prerequisites

  

- Python 3.7+

- Node.js and npm

- VirusTotal API key (register at [VirusTotal](https://www.virustotal.com/gui/join-us))

  


## Installation

### 1. Clone the repository:

``` 
git clone https://github.com/anthonydev51/pathyxis.git
cd pathyxis
```

### 2. Install backend dependencies:

```
pip install -r requirements.txt
```
### 3. Install frontend dependencies:
```
npm install
```

### 4. Set your VirusTotal API key environment variable in the terminal:
```
set VT_API_KEY=your_api_key_here
```
---

## Running the Application

### Start Backend (Flask API)
```
python app.py
```
### Start Frontend (Development Server)
```
npm run dev
```
Then open your browser at [http://localhost:5173](http://localhost:5173)

---

## Usage

-   Upload files through the web interface.
    
-   Pathyxis sends files to VirusTotal for scanning.
    
-   Results are displayed in real-time with detection details.
    
-   Heuristic checks provide an additional layer of analysis.
---

## Notes & Limitations

-   **VirusTotal Free API Limits:** Approximately 4 requests per minute and 500 requests per day.
    
-   **File Size Restrictions:** Files over 32 MB cannot be scanned via the free VirusTotal API.
    
-   **Scan Latency:** Some scans may take time; the app polls until the report is ready or times out.
    
-   **Privacy:** Uploaded files are sent to VirusTotal servers. Avoid uploading sensitive files unless you trust their policy.
    
-   **Not a Production Security Tool:** Intended as a demo and educational project only.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgments

-   VirusTotal for their malware scanning API.
    
-   Flask and Requests for backend libraries.
    
-   Vite and frontend ecosystem for the modern UI.
