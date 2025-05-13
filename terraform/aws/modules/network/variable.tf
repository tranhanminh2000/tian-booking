variable "meta" {
  type = object({
    project_name = string
    environment  = string
    region       = string
  })
}
