# Infrastructure for Deep Sea Research Station
provider "aws" {
  region     = "eu-central-1"
  # WARNING: Hardcoded credentials - High priority detection trigger
  access_key = "AKIA5F7D3E2B1A6C4D8E" 
  secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
}

# Database configuration with embedded password
resource "aws_db_instance" "coral_db" {
  allocated_storage    = 20
  engine               = "mysql"
  engine_version       = "8.0"
  instance_class       = "db.t3.micro"
  db_name              = "marine_life_db"
  username             = "admin"
  
  # SECRET 1: Plaintext password
  password             = "SuperSecretCoralReef2024!"
  
  parameter_group_name = "default.mysql8.0"
  skip_final_snapshot  = true
}

# Web Server with a private key in metadata (The "Fishing Net" hole)
resource "aws_instance" "research_web" {
  ami           = "ami-0d527b8c282149145"
  instance_type = "t3.small"

  user_data = <<-EOF
              #!/bin/bash
              # SECRET 2: Embedded RSA Private Key for "Shadow Crew" access
              echo "-----BEGIN RSA PRIVATE KEY-----
              MIIEpAIBAAKCAQEA75p9...+M7
              j8LpX17nLpX17nLpX17nLpX17nL
              -----END RSA PRIVATE KEY-----" > /home/ubuntu/id_rsa
              
              # SECRET 3: Azure Connection String for cross-cloud "Currents"
              export AZURE_STORAGE_CONNECTION_STRING="DefaultEndpointsProtocol=https;AccountName=phantomfish;AccountKey=YmFzZTY0X2lzX25vdF9lbmNyeXB0aW9uX2l0c19qdXN0X2VuY29kaW5nCg==;EndpointSuffix=core.windows.net"
              EOF

  tags = {
    Name        = "Abyssal-Platform-Node"
    Environment = "Production"
    # SECRET 4: Slack Webhook for distress signals
    AlertWebhook = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"
  }
}
