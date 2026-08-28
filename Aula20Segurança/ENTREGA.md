# Entrega — Aula 20 · TorreJWT Segura

## Checklist

- [x] Model: senha com HASH (werkzeug). Nunca texto puro.
- [x] para_dict NÃO devolve senha.
- [x] Cadastro sempre papel=visitante (cliente não se promove).
- [x] autenticar() confere a senha.
- [x] JWT_SECRET_KEY forte (não use "123").
- [x] Access curto (~15 min) e refresh ~1 dia — não 365 dias.
- [x] JWT_TOKEN_LOCATION = ["headers"]  (Authorization: Bearer)
- [x] @jwt_required() em /eu, /radar, /admin, /blocklist
- [x] @jwt_required(refresh=True) em /refresh
- [x] @jwt_required(verify_type=False) em /logout
- [x] @jwt_required(fresh=True) em /senha
- [x] @jwt_required(optional=True) no saguão
- [x] additional_claims_loader coloca papel (e nome) no token
- [x] /admin recusa quem não tem papel admin (403)
- [x] Logout grava o jti em TokenRevogado (blocklist)
- [x] token_in_blocklist_loader consulta a blocklist
- [x] Refresh gera access NÃO fresh
- [x] Troca de senha confere a senha atual

## Relatório

Antes dava para acessar o radar e o admin sem token, fazer login só com username (sem senha), se cadastrar como admin, usar token na query string (vazando em logs), e o logout não revogava o JWT — o mesmo token continuava válido. Agora o Flask responde 401 sem Bearer token nas rotas protegidas, 403 para não-admins na sala de controle, 401 com credenciais erradas no login, cadastro sempre como visitante, tokens só via header Authorization, logout grava o jti na blocklist e refresh gera access não-fresh.

## Como rodar

```bash
cd Aula20Segurança
pip install -r requirements.txt
python app.py
```

Acesse http://127.0.0.1:5000

Demo: `admin/admin123`, `piloto/piloto123`, `visitante/visitante123`
