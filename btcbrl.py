import sys
import cryptocompare
import requests
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = "TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMPLEMENTOFDEFAULT"

btc_brl = cryptocompare.get_price('BTC','BRL')['BTC']['BRL']

brl_oferta = int(sys.argv[1])
premium = float(sys.argv[2])

btc_brl_premium = btc_brl * ((100.0 + premium) / 100.0 )

btc_vendido = brl_oferta / btc_brl_premium
sats_vendido = btc_vendido * 100_000_000

print("Preço atual BTC/BRL: ", btc_brl)
print("Premium do Vendedor: ", premium, "%")
print("Preço atual BTC/BRL + Premium do Vendedor: ", btc_brl_premium)
print("Oferta de compra em BRL:", brl_oferta)
print("---")
print("BTCs vendidos:", btc_vendido)
print("sats vendidos: ", sats_vendido)
