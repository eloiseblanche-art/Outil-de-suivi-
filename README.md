# Outil de suivi – PASS S1

Page de suivi pour préparer le concours du 17 décembre : avancement des cours (3 passages + Anki), QCM par cours, révisions espacées, retards, kholles, semaine type et méthode.

- `suivi-pass.html` : le code de la page. Elle est publiée comme artifact privé sur claude.ai, et les données (cours, kholles, bilans) sont stockées dans sa base.

## Annales

L'onglet « Annales » montre 12 annales par matière (2020 S1 → 2025 S2). Toucher une case ouvre une fenêtre pour noter la note (facultative, sur 20 par défaut, ou sur un autre total), la date et ce qu'on retient. Chaque annale faite est un document de la collection `annales` : `{matiere, annee, session, date, note, sur, com}`. La moyenne sur 20 s'affiche par matière et au total.

## Révisions espacées

L'onglet « Révisions » traite chaque question des QCM comme une carte Anki et la programme avec l'algorithme FSRS (rétention 0,90, intervalle max 21 jours, réglables). L'état de chaque question est recalculé à partir des résultats enregistrés dans `qcmres` (les séances de révision y sont enregistrées avec `mode: "revision"`). Les réglages sont dans `config/revision`.

## QCM automatiques

Une tâche planifiée crée le QCM de chaque nouveau cours qui a un polycopié joint et pas encore de QCM. La marche à suivre et les scripts sont dans `qcm-auto/` (`CONSIGNES.md`).
