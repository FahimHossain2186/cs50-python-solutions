import requests
import sys
import json

try:
    if len(sys.argv) != 2:
        raise IndexError
    else:
        x = float(sys.argv[1])

    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=04e545ef14399aae0181ebea7bf78b8ff9026ffb7bdb6b42ef4744fa89c99f1f")
    o = response.json()
    bitcoin = float(o["data"]["priceUsd"])

    prize = bitcoin * x
    print(f"${prize:,.4f}")


except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")
except requests.RequestException:
    sys.exit()
