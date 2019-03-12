How to use
=========

Run `python3 main.py`


Documentation de l'API du projet de AREA
======

Le langage utiliser pour la creation de cette _api_ est _Python3_.
Nous avons utiliser le framework open-source python _Flask_.

L'API comporte 9 requete : 5 POST, 3 GET et 1 DELETE

Tout les retours sont un json :

`
[{
    "code": "1"          # valeur de retour
    "data": [
        "msg": "error"
        # données retourner selon api request
    ]
}]
`

Crée un nouveaux compte
------------

POST	:	http://127.0.0.1:5000/api/users

http://127.0.0.1:5000       URL
/api/users				route

Dans le body : 
`{"username":"florianles@oui.crom",
"password":"zefqldkqk",
"email":"florian.bord@epitech.eu"}`

Trois retour possible:
	- 404 en cas d'erruer, avec un message specifique 
	- 200 pour ok

-------------------------------------------------------------------------------------

Vérifier que le compte existe dans la BD

POST	:	http://127.0.0.1:5000/api/login

http://127.0.0.1:5000/		URL
api/login/						route

Dans le body : {"username":"florianles@oui.crom",
				"password":"zefqldkqk"}

Le token est retourner dans data avec la clé 'token' (Voir le format de reponse au debut du document)

Deux retour possible:
	- 200 pour ok
	- 401 si l'utilisateur n'existe pas

-------------------------------------------------------------------------------------

Ajouter un service

POST	:	http://127.0.0.1:5000/service

http://127.0.0.1:5000/		URL
service/					route

Dans le header : 'Authorization : $token'
exemple : 'Authorization : EQ4b60fb_AuewuYCpK6SPA'

Dans le body : {"action":"Nom de l'action",
				"action_data":"argument de l'action",
				"reaction":"Nom de la reaction",
				"reaction_data":"argument de la reaction",
				"name":"Nom donner au service"}

Deux retour possible:
	- 200 		si tout c'est bien passer
	- 401		si la connection a echouer ( mauvais username password)

Retirer un service

DELETE	:	http://127.0.0.1:5000/service

http://127.0.0.1:5000/		URL
service/					route

Trois retour possible:
	- 200		pour ok
	- -2	si le service n'existe pas
	- 401	si la connection a echouer ( mauvais username password)

-------------------------------------------------------------------------------------

Avoir la liste des service d'un user, et sont etat ( activer / desactiver)

GET	:	http://127.0.0.1:5000/service_list

http://127.0.0.1:5000/		URL
service_list/				route

Dans le header : 'Authorization : $token'
exemple : 'Authorization : EQ4b60fb_AuewuYCpK6SPA'

Les service sont retoruner dans data sous la forme : [{"name":"SERVICE1","state":"true"}]

exemple pour 4 service nommé 'serv1', 'serv2', 'serv3', 'serv4' :
	[{"name":"serv1","state":true},{"name":"serv2","state":true},{"name":"serv3","state":true},{"name":"serv4","state":true}]

Trois retour possible:
	- 200 pour ok
	- -2		(pas de service pour c'est utilisateur)
	- 401		si la combinaisont username password et incorrect

-------------------------------------------------------------------------------------

Changer le state d'un service, si il est true il passe a false et vis versa

POST	:	http://127.0.0.1:5000/change_state/

http://127.0.0.1:5000/		URL
change_state/				route

Dans le header : 'Authorization : $token'
exemple : 'Authorization : EQ4b60fb_AuewuYCpK6SPA'

Dans le body : {"name":"Nom du service"}

Trois retour possible:
	- 200		pour ok
	- 404	si le service n'existe pas
	- 401	si le token est mauvais
