# test_nginx_configuration.py

import subprocess
import requests
import pytest

@pytest.fixture(scope='module')
def nginx_status():
    # Restart Nginx to ensure the latest configuration is applied
    subprocess.run(['sudo', 'systemctl', 'restart', 'nginx'], check=True)

    # Check Nginx status to ensure it's running
    nginx_process = subprocess.run(['sudo', 'systemctl', 'status', 'nginx'], capture_output=True, text=True)
    status_output = nginx_process.stdout
    return status_output

def test_nginx_status(nginx_status):
    assert 'active (running)' in nginx_status, "Nginx is not running properly."

def test_nginx_forwarding():
    # Assuming Flask app is running on localhost:5000
    response = requests.get('http://localhost')
    assert response.status_code == 200, "Nginx failed to forward requests to the upstream server."

    # Add more assertions as needed to verify the response content or headers

