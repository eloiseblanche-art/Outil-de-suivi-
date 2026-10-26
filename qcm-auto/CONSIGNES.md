# Création automatique des QCM

Une tâche planifiée lance régulièrement une session Claude qui ajoute un QCM à chaque cours qui n'en a pas encore.

## Où sont les données

- Page : « Carnet PASS S1 », https://claude.ai/artifact/NLi4T7Ecs29xvuCh8HnMDd
- Base de la page (outil `ArtifactData`) : collections `cours`, `matieres`, `qcm`.
- Un cours a besoin d'un QCM quand il existe dans `cours` mais qu'il n'y a pas de document `qcm/<id du cours>`.
- Le polycopié du cours est un fichier de la page : champ `poly` du cours (id de 32 caractères). On le télécharge avec l'outil `Artifact`, `action: "read"`, `url` de la page et `path` = cet id (un seul fichier par appel). Si le cours n'a pas de `poly` (ou seulement un `lien`), on le saute.

## Comment faire un QCM

1. Lire tout le polycopié (souvent des scans : le lire page par page avec l'outil Read, `pages`).
2. Suivre les « Règles pour créer les QCM » de l'onglet Méthode (`suivi-pass.html`, bloc « Règles pour créer les QCM ») : un QCM par cours qui reprend tout le cours dans l'ordre, 3 à 5 questions par partie, 5 propositions, un nombre de vraies qui varie (entre 1 et 4, au moins 2 en SHS), placées au hasard : `build.py` mélange les propositions de chaque question, chaque fausse avec un commentaire qui donne la bonne réponse, uniquement le contenu du cours. Ne pas faire de questions sur ce que le poly dit « pas à connaître ».
3. Écrire le QCM dans le format court lu par `build.py` (voir l'en-tête du script), puis `python3 qcm-auto/build.py cours.txt cours.json` : le script vérifie 5 propositions, entre 1 et 4 vraies, et un commentaire pour chaque fausse.
4. Histo uniquement : une question par photo de microscopie du poly, dans une dernière partie « Photos de microscopie ». Rendre les pages avec `pdftoppm -r 200 -png`, découper chaque photo et masquer ses légendes avec `crop.py` (coordonnées en pixels à 100 dpi), vérifier le résultat à l'œil, puis envoyer les images dans la page (`Artifact`, `asset: true`, `file_paths`) et mettre l'id renvoyé à la fin de la ligne `? la photo ci-dessus @<id>`.
5. Enregistrer : `ArtifactData`, `action: "batch"`, une écriture `set` par QCM dans `qcm` avec `doc_id` = id du cours et `file_path` = le JSON. Ne jamais réécrire un QCM qui existe déjà.

Champs d'un document `qcm/<id>` : `cours` (id), `matiere`, `ordre` (celui du cours), `titre` (« 07 · Titre », numéro à deux chiffres), `sections`, `questions`. Ne pas mettre `rev` : le cours se lance dans les révisions depuis la page.
