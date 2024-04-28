Para garantir que o `cryptocompare` esteja disponível:

```
$ python3 -m venv .
$ source bin/activate
$ pip3 install cryptocompare
```

## Use o 'btcbrl.py' da seguinte forma:
Para converter de BRL para BTC:
```
$ python3 btcbrl.py <brl_oferta> <%_premium_vendedor>
```
Para converter de BTC para BRL:
```
$ python3 btcbrl.py BTC <quantidade_btc> <%_premium_vendedor>
```
Para converter de sats para BRL:
```
$ python3 btcbrl.py sats <quantidade_sats> <%_premium_vendedor>
```
Para exibir somente o preço atual:
```
$ python3 btcbrl.py
```
## Rode com Docker

```
docker run --rm jaonoctus/btcbrl <brl_oferta> <%_premium_vendedor>
```
