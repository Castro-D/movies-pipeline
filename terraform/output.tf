output "gce_public_ip" {
  description = "GCE instance public IP."
  value       = google_compute_instance.dev.network_interface[0].access_config[0].nat_ip
}

output "private_key" {
  description = "compute engine private key."
  value       = tls_private_key.custom_key.private_key_pem
  sensitive   = true
}

output "public_key" {
  description = "compute engine public key."
  value       = tls_private_key.custom_key.public_key_openssh
}