terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.13.0"
    }
  }
}

provider "google" {
  # Configuration options
  credentials = "./keys/my_creds.json"
  project = "terraform-412018"
  region  = "us-central1"
}