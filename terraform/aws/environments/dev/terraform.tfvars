meta = {
  project_name = "ecs-tian"
  environment  = "dev"
  region       = "us-west-2"
}

cors = {
  allow_origin   = ["*"]
  allow_methods  = ["POST", "PUT", "DELETE", "OPTIONS"]
  allow_headers  = ["Content-Type", "Authorization", "x-api-key"]
  expose_headers = []
  max_age        = 3600
}