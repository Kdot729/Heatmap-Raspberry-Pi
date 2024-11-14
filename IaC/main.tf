terraform {
required_providers {
        google = {
        source  = "hashicorp/google"
        version = ">= 4.51.0"
        }
    }
}

provider "google" {
    project = var.project
    region  = var.region
}

locals {
    script_content = file("install_docker.sh")
}

resource "google_compute_instance" "vm_instance" {
    name         = "ubuntu-docker"
    machine_type = "c3-standard-4-lssd"
    zone         = var.zone

    boot_disk {
        initialize_params {
        image = "ubuntu-2004-focal-v20240307b"
        }
    }

    network_interface {
        network = "default"
        access_config{
        }
    }

    metadata = {
        user-data = <<-EOF
        #!/bin/bash
        sudo apt-get update
        git clone https://github.com/Kdot729/Heatmap-Raspberry-Pi.git
        echo 'Clone complmented'
        echo '${local.script_content}' > /tmp/install_docker.sh
        sudo chmod +x /tmp/install_docker.sh
        /bin/bash /tmp/install_docker.sh
        EOF
    }
}

resource "google_compute_firewall" "allow_react" {
    name    = "allow-react"
    network = "default"
    
    allow {
        protocol = "tcp"
        ports    = ["3000"]
    }

    source_ranges = ["0.0.0.0/0"]
    description   = "Allow inbound traffic on port 3000 (React)"
}

resource "google_compute_firewall" "allow_fastapi" {
    name    = "allow-fastapi"
    network = "default"
    
    allow {
        protocol = "tcp"
        ports    = ["8000"]
    }

    source_ranges = ["0.0.0.0/0"]
    description   = "Allow inbound traffic on port 8000 (FastAPI)"
}

resource "google_bigtable_instance" "bigtable_instance" {
    name          = "bigtable-instance"
    project       = var.project

    cluster {
        cluster_id   = "bigtable-cluster"
        zone         = var.zone
        num_nodes    = 1
        storage_type = "SSD"
    }

    deletion_protection = false
}

resource "google_bigtable_table" "coinbase_table" {
    project       = var.project
    name          = "coinbase"
    instance_name = google_bigtable_instance.bigtable_instance.name

    column_family {
        family = "eth"
    }

}

output "public_ip" {
    value = google_compute_instance.vm_instance.network_interface[0].access_config[0].nat_ip
}