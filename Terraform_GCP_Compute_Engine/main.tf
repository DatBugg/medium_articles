terraform {
  required_providers{
    google = {
      source = "hashicorp/google"
      version = "3.5.0"
    }
  }
}

provider "google" {
  credentials = file("ServiceAccountKey.json")
  project     = var.project_id
}

resource "google_compute_instance" "default" {
  name         = "test1"
  machine_type = var.machine_type
  zone         = "us-central1-a"

  tags = ["tag1", "tag2"]

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = "default"

    access_config {
      // Ephemeral public IP
    }
  }
}