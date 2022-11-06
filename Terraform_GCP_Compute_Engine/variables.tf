variable "project_id" { 
    description = "Google Cloud project ID"
    type = string
    }

variable "machine_type" { 
    description = "Machine Type"
    type = string
    default = "f1-micro"
    }