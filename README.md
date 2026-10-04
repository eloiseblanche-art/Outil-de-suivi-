# Outil de suivi – PASS S1

Page de suivi pour préparer le concours du 17 décembre : avancement des cours (3 passages + Anki), QCM par cours, révisions espacées, retards, kholles, semaine type et méthode.

- `suivi-pass.html` : le code de la page. Elle est publiée comme artifact privé sur claude.ai, et les données (cours, kholles, bilans) sont stockées dans sa base.

## Révisions espacées

L'onglet « Révisions » traite chaque question des QCM comme une carte Anki et la programme avec l'algorithme FSRS (rétention 0,90, intervalle max 21 jours, réglables). L'état de chaque question est recalculé à partir des résultats enregistrés dans `qcmres` (les séances de révision y sont enregistrées avec `mode: "revision"`). Les réglages sont dans `config/revision`.
