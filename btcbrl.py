import sys
import cryptocompare
import requests
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = "TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMPLEMENTOFDEFAULT"

btc_brl = cryptocompare.get_price('BTC','BRL')['BTC']['BRL']

if len(sys.argv) < 2:
    print("Preço atual BTC/BRL: ", format(btc_brl, ",.2f"))
    sys.exit()

if sys.argv[1].upper() == "BTC":
    try:
        premium = float(sys.argv[3])
    except IndexError:
        premium = 0
    btc_brl_premium = btc_brl * ((100.0 + premium) / 100.0 )
    print("Preço atual BTC/BRL: ", format(btc_brl, ",.2f"))
    print("Preço atual BTC/BRL + Premium do Vendedor: ", format(btc_brl_premium, ",.2f"))
    print(f"Preço atual BTC/BRL + Premium do Vendedor para {sys.argv[2]} BTC: ", format(btc_brl_premium*float(sys.argv[2]), ",.2f"))
    sys.exit()

brl_oferta = int(sys.argv[1])
premium = float(sys.argv[2])

btc_brl_premium = btc_brl * ((100.0 + premium) / 100.0 )

btc_vendido = brl_oferta / btc_brl_premium
sats_vendido = btc_vendido * 100_000_000

print("Preço atual BTC/BRL: ", format(btc_brl, ",.2f"))
print("Premium do Vendedor: ", premium, "%")
print("Preço atual BTC/BRL + Premium do Vendedor: ", format(btc_brl_premium, ",.2f"))
print("Oferta de compra em BRL:", format(brl_oferta, ",.2f"))
print("---")
print("BTCs vendidos:", format(btc_vendido, ",.8f"))
print("sats vendidos: ", format(sats_vendido, ",.0f"))
