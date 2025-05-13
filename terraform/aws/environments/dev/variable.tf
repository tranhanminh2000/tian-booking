variable "meta" {
  type = object({
    project_name = string
    environment  = string
    region       = string
  })
}

variable "cors" {
  type = object({
    allow_origin   = list(string)
    allow_methods  = list(string)
    allow_headers  = list(string)
    expose_headers = list(string)
    max_age        = number
  })
  default = {
    allow_origin   = ["*"]
    allow_methods  = ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
    allow_headers  = ["Content-Type", "Authorization"]
    expose_headers = []
    max_age        = 3600
  }
}
