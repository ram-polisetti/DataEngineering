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
  credentials = var.credentials
  project     = var.project_id
  region      = var.location
}

resource "google_storage_bucket" "ny_taxi_parquet" {
  name                        = var.gcs_bucket_name
  location                    = var.location
  storage_class               = var.gcs_storage_class
  uniform_bucket_level_access = true
  force_destroy               = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}
#
#
#resource "google_storage_bucket_object" "ny_taxi_parquet_object" {
#  for_each = fileset("${path.module}/data/raw/", "**/*")
#  name         = var.gcs_object_name
#  source       = "data/raw/${each.value}"
#  bucket       = google_storage_bucket.ny_taxi_parquet.id
#}
