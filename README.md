# Outil de suivi – PASS S1

Page de suivi pour préparer le concours du 17 décembre : avancement des cours (3 passages + Anki), QCM par cours, révisions espacées, retards, kholles, semaine type et méthode.

- `suivi-pass.html` : le code de la page. Elle est publiée comme artifact privé sur claude.ai, et les données (cours, kholles, bilans) sont stockées dans sa base.

## Révisions espacées

L'onglet « Révisions » traite chaque question des QCM comme une carte Anki et la programme avec l'algorithme FSRS (rétention 0,90, intervalle max 21 jours, réglables). L'état de chaque question est recalculé à partir des résultats enregistrés dans `qcmres` (les séances de révision y sont enregistrées avec `mode: "revision"`). Les réglages sont dans `config/revision`.

## QCM automatiques

Une tâche planifiée crée le QCM de chaque nouveau cours qui a un polycopié joint et pas encore de QCM. La marche à suivre et les scripts sont dans `qcm-auto/` (`CONSIGNES.md`).

## Planning et annales (dernier mois)

- Onglet « Planning » : les packs de chaque jour jusqu'au concours (collection `taches`, documents `pl-MMJJ-NN` : date, heure, fin, texte, matiere, fait), à cocher au fur et à mesure. Les kholles du jour s'y affichent aussi.
- Onglet « Annales » : 12 annales par matière (2020 S1 → 2025 S2), toujours la plus ancienne non faite en premier. Une annale faite = un document `annales/<matiere>_<année>_s<session>` (matiere, annee, session, date).
