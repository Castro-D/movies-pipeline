variable "region" {
    type = string
    default = "us-central"
}
variable "project" {
    type = string
}

variable "credentials_path" {
    type = string
}

variable "repo_url" {
  description = "Repository url to clone into production machine"
  type        = string
  default     = "https://github.com/Castro-D/movies-pipeline.git"
}