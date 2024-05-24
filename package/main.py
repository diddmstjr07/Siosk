from package.client.anoask import Api

api = Api()

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2Fub2Fzay5zaXRlIiwiZXhwIjoxNzE3NDcwMDc5LCJzdWIiOiIzOCJ9._1iLHXYqP5ht71-NUKGlmJYJuDR9m3uoIVGywJSDoa0"
while True:
    api.send_response(token, "아이스 아메리카노 1잔 주문할게")