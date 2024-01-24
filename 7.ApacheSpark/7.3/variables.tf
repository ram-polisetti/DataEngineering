variable "credentials" {
  description = "Path to the credentials file"
  type        = string
  default     = "./keys/my_creds.json"

}
variable "project_id" {
  description = "Project ID"
  type        = string
  default     = "global-standard-411715"
}

variable "region" {
  description = "Region for the project"
  type        = string
  default     = "us-central1"

}
variable "bq_dataset_name" {
  description = "BigQuery dataset name"
  type        = string
  default     = "pq"
}

variable "gcs_bucket_name" {
  description = "My storage bucket"
  type        = string
  default     = "terraform-412018-bucket"

}

variable "gcs_storage_class" {
  description = "Storage class for the bucket"
  type        = string
  default     = "STANDARD"

}

variable "location" {
  description = "Location for the project"
  type        = string
  default     = "US"

}

variable "gcs_object_name" {
  description = "Name of the object to be uploaded"
  type        = string
  default     = "ny_taxi_parquet"

}

variable "gcs_object_path" {
  description = "Path of the object to be uploaded"
  type        = string
  default     ="Hello/"

}