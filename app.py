from flask import Flask, request, jsonify, render_template
import nmap
import socket
import requests

app = Flask(__name__)

def port_scan(target):
    output = ""
    scanner = nmap.PortScanner()
    scanner.scan(target, '1-1024', '-sV')
    for host in scanner.all_hosts():
        output += f"Host: {host} ({scanner[host].hostname()})\n"
        output += f"State: {scanner[host].state()}\n"
        for protocol in scanner[host].all_protocols():
            output += f"Protocol: {protocol}\n"
            ports = scanner[host][protocol].keys()
            for port in ports:
                output += f"Port: {port}, State: {scanner[host][protocol][port]['state']}\n"
    return output

def banner_grab(target, port):
    try:
        s = socket.socket()
        s.connect((target, port))
        s.send(b'HEAD / HTTP/1.1\r\n\r\n')
        banner = s.recv(1024)
        return f"Banner for {target}:{port}: {banner.decode('utf-8')}\n"
    except Exception as e:
        return f"Error grabbing banner: {e}\n"

def check_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers
        output = "Security Headers:\n"
        for header, value in headers.items():
            output += f"{header}: {value}\n"
        return output
    except Exception as e:
        return f"Error checking headers: {e}\n"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    data = request.json
    target = data.get('target')
    scan_type = data.get('scanType')
    if not target or not scan_type:
        return jsonify({"error": "Missing target or scan type"}), 400

    if scan_type == "Port Scan":
        result = port_scan(target)
    elif scan_type == "Banner Grabbing":
        result = banner_grab(target, 80)
    elif scan_type == "Header Check":
        result = check_headers(target)
    else:
        return jsonify({"error": "Invalid scan type"}), 400

    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)