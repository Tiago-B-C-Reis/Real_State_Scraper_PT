import base64

api_key = "tqztrdipk5jr1zkpulsg3q0kti14h8gq"
api_secret = "vWeL5hjOxFmX"

# Combine the API key and secret with a colon
combined_key_secret = f"{api_key}:{api_secret}"

# Base64 encode the combined string
base64_encoded_credentials = base64.b64encode(combined_key_secret.encode()).decode()

print(base64_encoded_credentials)


# curl -X POST -H "Authorization: Basic dHF6dHJkaXBrNWpyMXprcHVsc2czcTBrdGkxNGg4Z3E6dldlTDVoak94Rm1Y" -H "Content-Type: application/x-www-form-urlencoded" -d 'grant_type=client_credentials&scope=read' "https://api.idealista.com/oauth/token" -k

# curl -X POST -H "Authorization: Bearer {dHF6dHJkaXBrNWpyMXprcHVsc2czcTBrdGkxNGg4Z3E6dldlTDVoak94Rm1Y}" -H "Content-Type: multipart/form-data;" -F "center=40.430,-3.702" -F "propertyType=homes" -F "distance=15000" -F "operation=sale" "https://api.idealista.com/3.5/es/search"
tiagoreis@Tiagos-MacBook-Air ~ % curl -X POST -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZSI6WyJyZWFkIl0sImV4cCI6MTY5NTY5MTQyMSwiYXV0aG9yaXRpZXMiOlsiUk9MRV9QVUJMSUMiXSwianRpIjoiZjJlNTVmYTAtM2E2Mi00MzJmLWFlY2MtMDRkODg9YmEwMTllIiwiY2xpZW50X2lkIjoidHF6dHJkaXBrNWpyMXprcHVsc2czcTBrdGkxNGg4Z3EifQ.vn3y0_HRLCVc8fJ1rys6JLx_WzWUDWdkWSK1YhaI_zs" -H "Content-Type: multipart/form-data;" -F "center=40.430,-3.702" -F "propertyType=homes" -F "distance=15000" -F "operation=sale" "https://api.idealista.com/3.5/es/search"

{"error":"invalid_token","error_description":"Cannot convert access token to JSON"}%                                                        tiagoreis@Tiagos-MacBook-Air ~ %
