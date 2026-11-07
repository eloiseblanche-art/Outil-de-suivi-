# Outil de suivi – PASS S1

Page de suivi pour préparer le concours du 17 décembre : avancement des cours (3 passages + Anki), QCM par cours, révisions espacées, retards, kholles, semaine type et méthode.

- `suivi-pass.html` : le code de la page. Elle est publiée comme artifact privé sur claude.ai, et les données (cours, kholles, bilans) sont stockées dans sa base.

## Personnaliser la page et sprint final

Le bouton ⚙ en haut ouvre « Personnaliser la page » : on y décoche les onglets et les blocs qu'on ne veut plus voir (rien n'est effacé, tout se remet), et on active le **mode sprint**. Le choix est enregistré dans `config/affichage` (`tabs`, `blk`, `sprint`).

- **Bloc « Sprint final »** (onglet Aujourd'hui) : révisions du jour à lancer en un clic, questions jamais vues et rythme de nouvelles questions pour toutes les voir avant J-7, cours sans P3, points faibles (QCM avec le moins de propositions justes la dernière fois) et score par matière.
- **Mode sprint** : l'intervalle max des révisions est ramené au tiers des jours restants jusqu'au 15 décembre (au moins 2 j), pour que chaque question revienne encore au moins 3 fois avant le concours.

## Supprimer

Se suppriment (en touchant deux fois le bouton) : cours, kholles, tâches, événements, bilans de la semaine, QCM entiers (avec leurs résultats ; bouton en bas de « ✎ Modifier »), questions d'un QCM (dans « ✎ Corriger »), et résultats ou séances de révision (dans la page du résultat).

## Révisions espacées

L'onglet « Révisions » traite chaque question des QCM comme une carte Anki et la programme avec l'algorithme FSRS (rétention 0,90, intervalle max 21 jours, réglables). L'état de chaque question est recalculé à partir des résultats enregistrés dans `qcmres` (les séances de révision y sont enregistrées avec `mode: "revision"`). Les réglages sont dans `config/revision`.

## QCM automatiques

Une tâche planifiée crée le QCM de chaque nouveau cours qui a un polycopié joint et pas encore de QCM. La marche à suivre et les scripts sont dans `qcm-auto/` (`CONSIGNES.md`).
