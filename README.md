# Outil de suivi – PASS S1

Page de suivi pour préparer le concours du 17 décembre, réduite à trois onglets pour le dernier mois :

- **Cours** : avancement des cours (3 passages + Anki), camemberts par matière, polycopiés.
- **QCM** : un QCM par cours, résultats, correction, « Revoir mes erreurs ».
- **Kholles** : classements, liste des kholles, semaines jusqu'au concours.

Les onglets Aujourd'hui, Planning, Révisions et Méthode ont été retirés de la page. Leurs données (tâches, bilans, réglages, résultats de révision) restent dans la base mais ne sont plus affichées.

- `suivi-pass.html` : le code de la page. Elle est publiée comme artifact privé sur claude.ai, et les données (cours, kholles, QCM) sont stockées dans sa base.

## Masquer des blocs

Le bouton ⚙ en haut permet de masquer des blocs des onglets Cours et Kholles (rien n'est effacé, tout se remet). Le choix est enregistré dans `config/affichage` (`blk`).

## Supprimer

Se suppriment (en touchant deux fois le bouton) : cours, kholles, QCM entiers avec leurs résultats (bouton en bas de « ✎ Modifier »), questions d'un QCM (dans « ✎ Corriger ») et résultats de QCM (dans la page du résultat).

## QCM automatiques

Une tâche planifiée crée le QCM de chaque nouveau cours qui a un polycopié joint et pas encore de QCM. La marche à suivre et les scripts sont dans `qcm-auto/` (`CONSIGNES.md`).
