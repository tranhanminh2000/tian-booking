
# Create LAN (VPC), like a router set up LAN in your home
# CIDR block is new approach to replace classful IP addressing (Flexible in define: "10.0.0.0/16")
# We don't have follow classful IP addressing like A, B, C anymore
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  tags = {
    Name = "my-vpc"
  }
}

resource "aws_internet_gateway" "igw" { # Help LAN connect to the internet
  vpc_id = aws_vpc.main.id
  tags = {
    Name = "vpc-igw"
  }
}

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id
  tags = {
    Name = "public-rt"
  }
}

resource "aws_route" "default_route" {
  route_table_id         = aws_route_table.public.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.igw.id
}

resource "aws_route_table_association" "public_subnet" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.public.id
}
