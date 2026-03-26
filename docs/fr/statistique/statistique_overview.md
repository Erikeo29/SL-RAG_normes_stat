# Cours de normes statistiques industrielles

Ce document constitue un cours de référence sur les principales normes statistiques utilisées en qualité industrielle. Il couvre l'échantillonnage, la maîtrise statistique des procédés (SPC), la capabilité, les tests de normalité, la détection des valeurs aberrantes, les intervalles de tolérance et l'incertitude de mesure.

---

## Sommaire

1. [Introduction - rôle des statistiques dans la qualité industrielle](#1-introduction--rôle-des-statistiques-dans-la-qualité-industrielle)
2. [Échantillonnage par attributs (ISO 2859)](#2-échantillonnage-par-attributs-iso-2859)
3. [Échantillonnage par mesures (ISO 3951)](#3-échantillonnage-par-mesures-iso-3951)
4. [Cartes de contrôle SPC (ISO 7870, ASTM E2587)](#4-cartes-de-contrôle-spc-iso-7870-astm-e2587)
5. [Capabilité des procédés (ISO 22514)](#5-capabilité-des-procédés-iso-22514)
6. [Capabilité des systèmes de mesure (ISO 22514-7)](#6-capabilité-des-systèmes-de-mesure-iso-22514-7)
7. [Tests de normalité (ISO 5479)](#7-tests-de-normalité-iso-5479)
8. [Comparaison de populations - tests et ANOVA (ISO 5725, ASTM E691)](#8-comparaison-de-populations--tests-et-anova-iso-5725-astm-e691)
9. [Détection des valeurs aberrantes (ISO 16269-4)](#9-détection-des-valeurs-aberrantes-iso-16269-4)
10. [Intervalles de tolérance statistiques (ISO 16269-6)](#10-intervalles-de-tolérance-statistiques-iso-16269-6)
11. [Incertitude de mesure (GUM, NIST)](#11-incertitude-de-mesure-gum-nist)
12. [Guide SPC (ISO 11462) - étapes d'implémentation](#12-guide-spc-iso-11462--étapes-dimplémentation)
13. [Synthèse et articulations](#13-synthèse-et-articulations)
14. [Documents open source indexés dans le RAG](#14-documents-open-source-indexés-dans-le-rag)

---

## 1. Introduction - rôle des statistiques dans la qualité industrielle

### 1.1 Pourquoi les statistiques en production

La qualité industrielle repose sur la capacité à prendre des décisions fiables à partir de données limitées. Les méthodes statistiques fournissent un cadre rigoureux pour :

- **Accepter ou refuser un lot** sur la base d'un échantillon représentatif (échantillonnage).
- **Surveiller un procédé** en temps réel et détecter toute dérive (cartes de contrôle SPC).
- **Quantifier la performance** d'un procédé par rapport aux spécifications (capabilité).
- **Valider un système de mesure** avant de l'utiliser pour prendre des décisions (analyse GRR).
- **Estimer l'incertitude** associée à un résultat de mesure (GUM).

### 1.2 Panorama normatif ISO pour les méthodes statistiques

Les normes ISO relatives aux méthodes statistiques sont regroupées dans le comité technique ISO/TC 69 :

| Famille de normes | Domaine |
|---|---|
| ISO 2859 | Échantillonnage par attributs (contrôle par comptage). |
| ISO 3951 | Échantillonnage par mesures (contrôle par variables). |
| ISO 7870 | Cartes de contrôle (SPC). |
| ISO 22514 | Capabilité des procédés et des systèmes de mesure. |
| ISO 5479 | Tests de normalité. |
| ISO 16269 | Intervalles statistiques (tolérance, confiance, prédiction). |
| ISO 11462 | Lignes directrices pour la mise en oeuvre du SPC. |

À ces normes ISO s'ajoutent le GUM (JCGM 100:2008) pour l'incertitude de mesure, la note technique NIST TN 1297, et des normes ASTM comme E2587 pour les cartes de contrôle.

### 1.3 Concepts fondamentaux

**Population et échantillon.** La population est l'ensemble complet des individus. L'échantillon est un sous-ensemble de taille $n$ prélevé de la population de taille $N$.

**Risque de première espèce ($\alpha$).** Probabilité de rejeter un lot conforme (risque du producteur). Typiquement $\alpha = 0{,}05$.

**Risque de deuxième espèce ($\beta$).** Probabilité d'accepter un lot non conforme (risque du consommateur). La puissance du test est $1 - \beta$.

**Niveau de confiance.** $1 - \alpha$ exprime la probabilité que l'intervalle estimé contienne la vraie valeur du paramètre.

**Niveau de qualité acceptable (NQA ou AQL).** Le pire niveau de qualité moyen du procédé considéré comme acceptable, en pourcentage de non-conformes.

**Distribution normale.** Caractérisée par $\mu$ et $\sigma$ :
- $\pm 1\sigma$ : 68,27 % de la population.
- $\pm 2\sigma$ : 95,45 % de la population.
- $\pm 3\sigma$ : 99,73 % de la population.

<!-- IMG:normal_distribution_3sigma.png -->

**Degré de liberté ($\nu$).** Pour l'écart-type d'un échantillon de taille $n$ : $\nu = n - 1$.

**Vocabulaire.** *Non-conforme* : une unité qui ne satisfait pas au moins une spécification. *Non-conformité* : un écart individuel par rapport à une spécification (une pièce peut en présenter plusieurs).

---

## 2. Échantillonnage par attributs (ISO 2859)

> **Note :** les normes ISO 2859 ne sont pas indexées dans le RAG (normes payantes). La théorie et les formules sont présentées ci-dessous à titre de référence.

L'échantillonnage par attributs consiste à classer les unités d'un échantillon en conformes ou non conformes (critère binaire). La décision repose sur le nombre de non-conformes trouvées.

### 2.1 ISO 2859-1 - plans indexés par NQA

ISO 2859-1 (équivalente à ANSI/ASQ Z1.4) définit des plans d'échantillonnage indexés par le NQA. La procédure est : (1) déterminer le code lettre à partir de la taille du lot et du niveau d'inspection, (2) lire la taille d'échantillon $n$ et les nombres $Ac$/$Re$ dans la table correspondant au NQA choisi.

**Niveaux d'inspection :** niveau II par défaut ; niveau I (réduit) et III (renforcé) ; niveaux spéciaux S-1 à S-4 pour les essais destructifs ou coûteux.

**Règles de commutation :**
- **Normal vers renforcé :** 2 lots sur 5 consécutifs refusés.
- **Renforcé vers normal :** 5 lots consécutifs acceptés.
- **Normal vers réduit :** 10 lots acceptés, nombre total de non-conformes sous un seuil, production stable.
- **Réduit vers normal :** dès qu'un lot est refusé.
- **Arrêt :** 5 lots consécutifs refusés en inspection renforcée.

<!-- IMG:switching_rules_diagram.png -->

### 2.2 Courbes d'efficacité (OC curves)

La courbe OC donne la probabilité d'acceptation $P_a$ en fonction de la proportion réelle de non-conformes $p$.

Pour un plan simple ($n$, $Ac$), la probabilité d'acceptation suit la loi binomiale :

$$P_a(p) = \sum_{i=0}^{Ac} \binom{n}{i} p^i (1-p)^{n-i}$$

Approximation de Poisson pour les grands lots et petites proportions :

$$P_a(p) \approx \sum_{i=0}^{Ac} \frac{(np)^i}{i!} e^{-np}$$

- **Point NQA :** $P_a \approx 0{,}95$ (risque producteur $\alpha \approx 5\%$).
- **Point LQ :** $P_a \approx 0{,}10$ (risque consommateur $\beta \approx 10\%$).

<!-- IMG:oc_curve_sampling.png -->

### 2.3 ISO 2859-2 - plans pour lots isolés (LQ)

Pour les lots isolés, ISO 2859-2 propose des plans indexés par la qualité limite (LQ), correspondant à $P_a = 0{,}10$.

---

## 3. Échantillonnage par mesures (ISO 3951)

> **Note :** les normes ISO 3951 ne sont pas indexées dans le RAG (normes payantes).

L'échantillonnage par mesures exploite la valeur numérique mesurée sur chaque unité, ce qui permet une meilleure discrimination avec un échantillon plus petit. **Hypothèse fondamentale :** la distribution de la caractéristique est approximativement normale.

### 3.1 ISO 3951-1 - méthodes s et $\sigma$

**Méthode « s » (écart-type inconnu) :**

$$s = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2}$$

Critères d'acceptation :
- Spécification supérieure : $Q_U = (LSS - \bar{x})/s \geq k$
- Spécification inférieure : $Q_L = (\bar{x} - LSI)/s \geq k$

**Méthode « $\sigma$ » (écart-type connu) :** on remplace $s$ par $\sigma$, ce qui permet des tailles d'échantillon plus petites.

**Spécifications bilatérales :** méthode combinée (proportion estimée combinée $\leq$ NQA) ou méthode séparée (critère indépendant par limite, plus conservatrice).

---

## 4. Cartes de contrôle SPC (ISO 7870, ASTM E2587)

> **Note :** les normes ISO 7870 et ASTM E2587 ne sont pas indexées dans le RAG (normes payantes).

La maîtrise statistique des procédés (SPC) distingue les variations dues à des causes communes (aléatoires) de celles dues à des causes spéciales (assignables).

### Principes fondamentaux (Shewhart)

Une carte de contrôle comprend :
- **LCS** (UCL) : $CL + 3\sigma$
- **LC** (CL) : valeur moyenne
- **LCI** (LCL) : $CL - 3\sigma$

Les limites à $\pm 3\sigma$ correspondent à une probabilité de fausse alarme d'environ 0,27 % par point.

**Attention :** les limites de contrôle (calculées à partir des données du procédé) ne sont PAS les limites de spécification (définies par le client).

### 4.1 Cartes pour variables

#### 4.1.1 Carte $\bar{x}$ / R (moyenne et étendue)

Carte la plus utilisée pour $2 \leq n \leq 9$.

**Limites de contrôle pour $\bar{x}$ :**

$$UCL_{\bar{x}} = \bar{\bar{x}} + A_2 \bar{R} \qquad LCL_{\bar{x}} = \bar{\bar{x}} - A_2 \bar{R}$$

**Limites de contrôle pour $R$ :**

$$UCL_R = D_4 \bar{R} \qquad LCL_R = D_3 \bar{R}$$

**Estimation de l'écart-type :** $\hat{\sigma} = \bar{R}/d_2$

**Table des constantes ($n$ = 2 à 10) :**

| $n$ | $A_2$ | $D_3$ | $D_4$ | $d_2$ |
|---|---|---|---|---|
| 2 | 1,880 | 0 | 3,267 | 1,128 |
| 3 | 1,023 | 0 | 2,574 | 1,693 |
| 4 | 0,729 | 0 | 2,282 | 2,059 |
| 5 | 0,577 | 0 | 2,114 | 2,326 |
| 6 | 0,483 | 0 | 2,004 | 2,534 |
| 7 | 0,419 | 0,076 | 1,924 | 2,704 |
| 8 | 0,373 | 0,136 | 1,864 | 2,847 |
| 9 | 0,337 | 0,184 | 1,816 | 2,970 |
| 10 | 0,308 | 0,223 | 1,777 | 3,078 |

<!-- IMG:control_chart_xbar.png -->

#### 4.1.2 Carte $\bar{x}$ / S (moyenne et écart-type)

Préférée pour $n \geq 10$. L'écart-type $s$ est un estimateur plus fiable que l'étendue pour les grands sous-groupes.

**Limites de contrôle pour $\bar{x}$ :**

$$UCL_{\bar{x}} = \bar{\bar{x}} + A_3 \bar{S} \qquad LCL_{\bar{x}} = \bar{\bar{x}} - A_3 \bar{S}$$

**Limites de contrôle pour $S$ :**

$$UCL_S = B_4 \bar{S} \qquad LCL_S = B_3 \bar{S}$$

**Estimation de l'écart-type :** $\hat{\sigma} = \bar{S}/c_4$

Les constantes $A_3$, $B_3$, $B_4$, $c_4$ sont tabulées pour $n = 2$ à $25$.

#### 4.1.3 Carte I-MR (individuelle et étendue mobile)

Utilisée pour $n = 1$ (production lente, mesures coûteuses, données sans sous-groupes naturels).

**Limites de contrôle pour la carte I :**

$$UCL_X = \bar{X} + 2{,}66 \, \bar{MR} \qquad LCL_X = \bar{X} - 2{,}66 \, \bar{MR}$$

Le coefficient $2{,}66 = 3 / d_2 = 3 / 1{,}128$ (constantes de $n = 2$).

**Limites de contrôle pour MR :** $UCL_{MR} = 3{,}267 \, \bar{MR}$, $LCL_{MR} = 0$.

**Estimation de l'écart-type :** $\hat{\sigma} = \bar{MR}/1{,}128$

**Important :** la carte I-MR est sensible aux écarts de normalité. Vérifier la normalité (section 7) avant utilisation.

#### 4.1.4 Phase d'étude et phase de surveillance

**Phase 1 (rétrospective) :** collecter au moins 25 sous-groupes, calculer les limites provisoires, éliminer les points hors contrôle dont la cause spéciale est identifiée, recalculer.

**Phase 2 (prospective) :** surveiller en temps réel avec les limites de la phase 1. Ne recalculer que si le procédé est modifié intentionnellement.

#### 4.1.5 Choix entre les cartes pour variables

| Critère | $\bar{x}$ / R | $\bar{x}$ / S | I-MR |
|---|---|---|---|
| Taille de sous-groupe | $2 \leq n \leq 9$ | $n \geq 10$ | $n = 1$ |
| Estimation de $\sigma$ | $\bar{R}/d_2$ | $\bar{S}/c_4$ | $\bar{MR}/d_2$ ($n=2$) |
| Hypothèse de normalité | Robuste (TCL). | Robuste (TCL). | Sensible. |

**Relations fondamentales entre les constantes :**
- $A_2 = 3 / (d_2 \sqrt{n})$
- $A_3 = 3 / (c_4 \sqrt{n})$
- $D_3 = 1 - 3 d_3 / d_2$ et $D_4 = 1 + 3 d_3 / d_2$
- $B_3 = 1 - 3\sqrt{1 - c_4^2}/c_4$ et $B_4 = 1 + 3\sqrt{1 - c_4^2}/c_4$

---

### 4.2 Cartes pour attributs

| Carte | Données surveillées | Taille d'échantillon | Distribution | Formule UCL |
|---|---|---|---|---|
| $p$ | Fraction non conforme | Variable ou constante | Binomiale | $\bar{p} + 3\sqrt{\bar{p}(1-\bar{p})/n}$ |
| $np$ | Nombre de non-conformes | Constante | Binomiale | $n\bar{p} + 3\sqrt{n\bar{p}(1-\bar{p})}$ |
| $c$ | Nombre de non-conformités | Constante | Poisson | $\bar{c} + 3\sqrt{\bar{c}}$ |
| $u$ | Taux de non-conformités/unité | Variable ou constante | Poisson | $\bar{u} + 3\sqrt{\bar{u}/n}$ |

Si la LCI est négative, on pose $LCI = 0$. Pour les cartes $p$ et $u$, les limites sont recalculées lorsque $n$ varie.

**Condition d'application de la carte $p$ :** $n\bar{p} \geq 5$ et $n(1 - \bar{p}) \geq 5$.

---

### 4.3 Règles Western Electric / Nelson

Les règles complémentaires augmentent la sensibilité aux petits décalages en détectant des motifs non aléatoires. La zone entre les limites est divisée en trois bandes (A, B, C) de chaque côté de la ligne centrale.

| Règle | Description | Signal typique |
|---|---|---|
| 1 | 1 point au-delà de $3\sigma$ | Cause spéciale isolée. |
| 2 | 9 points du même côté du CL | Décalage de moyenne. |
| 3 | 6 points en tendance monotone | Dérive progressive. |
| 4 | 14 points alternant haut/bas | Surcontrôle ou alternance de sources. |
| 5 | 2 sur 3 au-delà de $2\sigma$ (même côté) | Décalage temporaire. |
| 6 | 4 sur 5 au-delà de $1\sigma$ (même côté) | Décalage modéré de moyenne. |
| 7 | 15 points dans la zone C | Stratification (limites trop larges). |
| 8 | 8 points au-delà de $1\sigma$ (des deux côtés) | Mélange de distributions. |

**Recommandation :** en production, appliquer les règles 1 à 4 pour limiter les fausses alarmes. L'application de toutes les règles augmente le taux de fausses alarmes à 2-4 % par point. Pour les petits décalages, considérer les cartes CUSUM (ISO 7870-4) ou EWMA (ISO 7870-6).

---

## 5. Capabilité des procédés (ISO 22514)

> **Note :** les normes ISO 22514 ne sont pas indexées dans le RAG (normes payantes).

La capabilité compare la dispersion naturelle du procédé à l'intervalle de tolérance spécifié.

### 5.1 Indices de capabilité à court terme ($C_p$, $C_{pk}$)

Ces indices utilisent l'écart-type intra-groupe $\sigma$ (variation à court terme).

$$C_p = \frac{LSS - LSI}{6\sigma} \qquad C_{pk} = \min\left(\frac{LSS - \bar{x}}{3\sigma}, \frac{\bar{x} - LSI}{3\sigma}\right)$$

$C_p$ mesure la capabilité potentielle (sans centrage). $C_{pk}$ tient compte du centrage. Si le procédé est centré, $C_{pk} = C_p$.

### 5.2 Indices de performance à long terme ($P_p$, $P_{pk}$)

Ces indices utilisent l'écart-type total $s$ (variation totale incluant les variations entre sous-groupes).

$$P_p = \frac{LSS - LSI}{6s} \qquad P_{pk} = \min\left(\frac{LSS - \bar{x}}{3s}, \frac{\bar{x} - LSI}{3s}\right)$$

En général $s \geq \sigma$, donc $P_p \leq C_p$ et $P_{pk} \leq C_{pk}$. Un écart important révèle des sources de variation entre sous-groupes.

<!-- IMG:capability_cp_cpk.png -->

### 5.3 Interprétation des indices

| $C_{pk}$ (ou $P_{pk}$) | Interprétation | PPM hors tolérance (total, deux queues) |
|---|---|---|
| $< 1{,}00$ | Incapable | $> 2700$ |
| $1{,}00$ à $1{,}33$ | Marginal | $63$ à $2700$ |
| $1{,}33$ à $1{,}67$ | Capable | $0{,}6$ à $63$ |
| $\geq 1{,}67$ | Très capable | $< 0{,}6$ |

### 5.4 Conditions préalables au calcul de capabilité

1. Le procédé est **sous contrôle statistique** (carte de contrôle).
2. Les données suivent une distribution **approximativement normale** (section 7).
3. Le **système de mesure** est adéquat (%GRR acceptable, section 6).
4. Au moins **25 sous-groupes** (ISO 22514-2).

---

## 6. Capabilité des systèmes de mesure (ISO 22514-7)

> **Note :** la norme ISO 22514-7 n'est pas indexée dans le RAG (norme payante).

### 6.1 Indices $C_g$ et $C_{gk}$

$$C_g = \frac{0{,}2 \times T}{6 s_g} \qquad C_{gk} = \frac{0{,}1 \times T - |x_m - \bar{x}|}{3 s_g}$$

où $T = LSS - LSI$, $s_g$ est l'écart-type de répétabilité, $x_m$ la valeur de référence et $\bar{x}$ la moyenne des mesures. Exigence : $C_g \geq 1{,}33$ et $C_{gk} \geq 1{,}33$.

### 6.2 Étude GRR

La variabilité du système de mesure se décompose en :

- **Répétabilité (EV) :** $EV = \bar{R}_{opérateurs} / d_2$
- **Reproductibilité (AV) :** $AV = \sqrt{(\bar{R}_{pièces \, par \, opérateur}/d_2)^2 - EV^2/(nr)}$
- **GRR combiné :** $GRR = \sqrt{EV^2 + AV^2}$
- **Variation des pièces :** $PV = R_{pièces}/d_2$
- **Variation totale :** $TV = \sqrt{GRR^2 + PV^2}$
- **Pourcentage GRR :** $\%GRR = GRR/TV \times 100$

| %GRR | Interprétation |
|---|---|
| $< 10\%$ | Acceptable. |
| $10\%$ à $30\%$ | Marginal. |
| $> 30\%$ | Inacceptable. |

**Nombre de catégories distinctes :** $ndc = 1{,}41 \times PV/GRR$ (exigence : $ndc \geq 5$).

<!-- IMG:grr_variance_components.png -->

---

## 7. Tests de normalité (ISO 5479)

> **Note :** la norme ISO 5479 n'est pas indexée dans le RAG (norme payante).

### 7.1 Pourquoi la normalité est importante

- Les cartes R, S et I-MR sont sensibles à la non-normalité (les cartes $\bar{x}$ sont plus robustes grâce au TCL).
- Les indices $C_p$/$C_{pk}$ supposent la normalité.
- Les intervalles de tolérance paramétriques (ISO 16269-6) supposent la normalité.

### 7.2 Test de Shapiro-Wilk

Test de référence pour $n < 50$ (extensible à $n = 5000$).

$$W = \frac{\left(\sum_{i=1}^{m} a_i (x_{(n+1-i)} - x_{(i)})\right)^2}{\sum_{i=1}^{n}(x_i - \bar{x})^2}$$

$W$ varie entre 0 et 1. On rejette $H_0$ (normalité) si $W < W_{critique}$ ou si $p$-value $< \alpha$.

### 7.3 Test d'Anderson-Darling

Particulièrement sensible aux queues de distribution (pertinent pour les PPM).

$$A^2 = -n - \frac{1}{n}\sum_{i=1}^{n}(2i - 1)\left[\ln(F(x_{(i)})) + \ln(1 - F(x_{(n+1-i)}))\right]$$

$$A^{*2} = A^2 \left(1 + \frac{0{,}75}{n} + \frac{2{,}25}{n^2}\right)$$

Valeur critique pour $\alpha = 0{,}05$ : $A^{*2} \approx 0{,}752$.

### 7.4 Test de Kolmogorov-Smirnov (Lilliefors)

$$D = \max_{i} \left| F_n(x_{(i)}) - F_0(x_{(i)}) \right|$$

Lorsque $\mu$ et $\sigma$ sont estimés, utiliser les tables de Lilliefors.

### 7.5 Diagramme Q-Q (quantile-quantile)

Construction : trier les données, calculer $p_i = (i - 0{,}375)/(n + 0{,}25)$ (Blom), puis $z_i = \Phi^{-1}(p_i)$, et tracer $x_{(i)}$ vs $z_i$.

Interprétation : alignement linéaire = normalité ; courbure en S = asymétrie ; extrémités déviantes = queues lourdes.

<!-- IMG:qqplot_comparison.png -->

### 7.6 Tableau comparatif

| Test | Sensibilité principale | Usage recommandé |
|---|---|---|
| Shapiro-Wilk | Centre et queues. | Référence pour $n < 50$. |
| Anderson-Darling | Queues de distribution. | Complément pour PPM. |
| KS (Lilliefors) | Centre de distribution. | Quand les autres ne sont pas disponibles. |
| Q-Q plot | Diagnostic visuel global. | Toujours en complément. |

---

## 8. Comparaison de populations - tests et ANOVA (ISO 5725, ASTM E691)

> **Note :** les normes ISO 5725 et ASTM E691 ne sont pas indexées dans le RAG (normes payantes).

### 8.1 Test de Student - comparaison de moyennes

#### 8.1.1 Un échantillon

$$t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}} \qquad \nu = n - 1$$

Rejeter $H_0$ si $|t| > t_{\alpha/2, n-1}$.

#### 8.1.2 Deux échantillons indépendants

**Variances égales (pooled) :**

$$t = \frac{\bar{x}_1 - \bar{x}_2}{s_p \sqrt{1/n_1 + 1/n_2}} \qquad s_p = \sqrt{\frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1+n_2-2}}$$

**Variances inégales (Welch) :**

$$t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{s_1^2/n_1 + s_2^2/n_2}} \qquad \nu_{eff} = \frac{(s_1^2/n_1 + s_2^2/n_2)^2}{(s_1^2/n_1)^2/(n_1-1) + (s_2^2/n_2)^2/(n_2-1)}$$

En cas de doute sur l'égalité des variances, utiliser systématiquement Welch.

#### 8.1.3 Test apparié

$$t = \frac{\bar{d}}{s_d / \sqrt{n}} \qquad \nu = n - 1$$

### 8.2 Test de Fisher - comparaison de deux variances

$$F = \frac{s_1^2}{s_2^2} \quad (s_1^2 \geq s_2^2)$$

Rejeter $H_0$ si $F > F_{\alpha/2, n_1-1, n_2-1}$. Le test de Fisher est très sensible à la non-normalité ; préférer le test de Levene en cas de doute.

### 8.3 ANOVA à un facteur

Compare les moyennes de $k \geq 3$ groupes simultanément. $H_0 : \mu_1 = \mu_2 = \cdots = \mu_k$.

**Décomposition :** $SS_T = SS_B + SS_W$

| Source | SS | df | MS | F |
|---|---|---|---|---|
| Inter-groupes | $SS_B$ | $k - 1$ | $MS_B = SS_B/(k-1)$ | $F = MS_B/MS_W$ |
| Intra-groupe | $SS_W$ | $N - k$ | $MS_W = SS_W/(N-k)$ | |
| Total | $SS_T$ | $N - 1$ | | |

Rejeter $H_0$ si $F > F_{\alpha, k-1, N-k}$.

**Conditions :** indépendance, normalité, homogénéité des variances (tester avec Bartlett ou Levene).

<!-- IMG:anova_boxplot.png -->

### 8.4 ANOVA à deux facteurs

Modèle avec interaction :

$$x_{ijk} = \mu + \alpha_i + \beta_j + (\alpha\beta)_{ij} + \varepsilon_{ijk}$$

La décomposition inclut $SS_A$, $SS_B$, $SS_{AB}$ et $SS_E$. Si l'interaction est significative, les effets principaux doivent être interprétés avec prudence.

### 8.5 Tests post-hoc

| Méthode | Usage principal | Particularité |
|---|---|---|
| Tukey HSD | Toutes les paires, effectifs égaux. | Contrôle exact du risque familywise. |
| Bonferroni | Toute situation. | Simple mais conservatrice si $m$ est grand. |
| Scheffé | Contrastes quelconques. | La plus conservatrice pour les paires. |
| Dunnett | Comparaison à un témoin. | Plus puissant que Tukey pour ce cas. |

### 8.6 Tests d'homogénéité des variances

**Bartlett :** puissant mais très sensible à la non-normalité.

**Levene :** remplace chaque observation par $z_{ij} = |x_{ij} - \tilde{x}_j|$ (médiane du groupe), puis ANOVA sur les $z_{ij}$. Robuste aux données non normales.

### 8.7 Alternative non paramétrique - Kruskal-Wallis

$$H = \frac{12}{N(N+1)} \sum_{j=1}^{k} \frac{R_j^2}{n_j} - 3(N+1)$$

Sous $H_0$, $H \sim \chi^2(k-1)$ pour $n_j \geq 5$.

### 8.8 ISO 5725 et ASTM E691

**ISO 5725 - exactitude (justesse et fidélité) :**
- Répétabilité : $r = 2{,}8 \times s_r$
- Reproductibilité : $R = 2{,}8 \times s_R$ avec $s_R^2 = s_r^2 + s_L^2$

**ASTM E691 - statistiques de Mandel :**
- $h_j = (\bar{x}_j - \bar{\bar{x}})/s_{\bar{x}}$ (consistance inter-laboratoires)
- $k_j = s_j/s_r$ (consistance intra-laboratoire)

### 8.9 Tableau récapitulatif

| Objectif | Test | Alternative non paramétrique |
|---|---|---|
| 1 moyenne vs référence | Student 1 échantillon | Wilcoxon signé |
| 2 moyennes indépendantes | Student 2 éch. / Welch | Mann-Whitney U |
| 2 moyennes appariées | Student apparié | Wilcoxon signé |
| 2 variances | Fisher F | Levene |
| $k \geq 3$ moyennes | ANOVA 1 facteur | Kruskal-Wallis |
| $k$ moyennes (2 facteurs) | ANOVA 2 facteurs | Friedman |

---

## 9. Détection des valeurs aberrantes (ISO 16269-4)

> **Note :** la norme ISO 16269-4 n'est pas indexée dans le RAG (norme payante).

### 9.1 Test de Grubbs

$$G = \frac{\max_i |x_i - \bar{x}|}{s}$$

Rejeter $H_0$ (pas d'outlier) si $G > G_{critique}$. Le test suppose la normalité.

### 9.2 Test de Dixon

Alternative pour petits échantillons ($3 \leq n \leq 25$), basée sur les statistiques d'ordre.

| Taille $n$ | Statistique | Formule |
|---|---|---|
| 3 à 7 | $r_{10}$ | $(x_{(n)} - x_{(n-1)}) / (x_{(n)} - x_{(1)})$ |
| 8 à 10 | $r_{11}$ | $(x_{(n)} - x_{(n-1)}) / (x_{(n)} - x_{(2)})$ |
| 11 à 13 | $r_{21}$ | $(x_{(n)} - x_{(n-2)}) / (x_{(n)} - x_{(2)})$ |
| 14 à 25 | $r_{22}$ | $(x_{(n)} - x_{(n-2)}) / (x_{(n)} - x_{(3)})$ |

### 9.3 Recommandation pratique

Pour $n < 10$ : privilégier Dixon. Pour $n \geq 10$ : privilégier Grubbs. Toujours accompagner d'une analyse graphique (boîte à moustaches, Q-Q plot).

---

## 10. Intervalles de tolérance statistiques (ISO 16269-6)

> **Note :** la norme ISO 16269-6 n'est pas indexée dans le RAG (norme payante).

Un intervalle de tolérance statistique contient au moins une proportion $p$ de la population avec un niveau de confiance $\gamma$. À ne pas confondre avec l'intervalle de confiance ni avec les tolérances industrielles.

### 10.1 Intervalles paramétriques (distribution normale)

**Bilatéral :** $[\bar{x} - k \cdot s, \, \bar{x} + k \cdot s]$

**Unilatéral :** $(-\infty, \, \bar{x} + k \cdot s]$ ou $[\bar{x} - k \cdot s, \, +\infty)$

Le facteur $k$ dépend de $n$, $p$ et $\gamma$. Extrait pour $p = 0{,}95$ (bilatéral) :

| $n$ | $\gamma = 0{,}90$ | $\gamma = 0{,}95$ | $\gamma = 0{,}99$ |
|---|---|---|---|
| 5 | 4,152 | 5,079 | 7,855 |
| 10 | 2,911 | 3,259 | 4,053 |
| 20 | 2,498 | 2,713 | 3,139 |
| 30 | 2,354 | 2,515 | 2,833 |
| 50 | 2,224 | 2,345 | 2,576 |
| 100 | 2,127 | 2,218 | 2,383 |

### 10.2 Intervalles non paramétriques

L'intervalle $[x_{(r)}, x_{(n-r+1)}]$ couvre au moins $p$ de la population avec confiance $\gamma$ si :

$$\sum_{j=0}^{2r-2} \binom{n}{j} p^j (1-p)^{n-j} \leq 1 - \gamma$$

Tailles minimales pour $r = 1$ (bornes = min/max) bien plus élevées que l'approche paramétrique.

### 10.3 Distinction entre types d'intervalles

| Type | Ce qu'il encadre | Formule typique |
|---|---|---|
| Intervalle de confiance | Le paramètre $\mu$. | $\bar{x} \pm t_{\alpha/2, n-1} \cdot s / \sqrt{n}$ |
| Intervalle de prédiction | La prochaine observation. | $\bar{x} \pm t_{\alpha/2, n-1} \cdot s \sqrt{1 + 1/n}$ |
| Intervalle de tolérance | Au moins $p$% de la population. | $\bar{x} \pm k \cdot s$ |

---

## 11. Incertitude de mesure (GUM, NIST)

Le GUM (JCGM 100:2008) est le document de référence international pour l'incertitude de mesure. La note NIST TN 1297 en est un résumé pratique. Le guide NIST SP 260-135 traite de la métrologie statistique.

### 11.1 Modèle de mesure

$$Y = f(X_1, X_2, \ldots, X_N)$$

### 11.2 Évaluation de type A

$$u_A = \frac{s}{\sqrt{n}} \qquad s = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2}$$

Degrés de liberté : $\nu = n - 1$.

### 11.3 Évaluation de type B

| Distribution | Paramètre | Incertitude-type $u_B$ | Usage typique |
|---|---|---|---|
| Rectangulaire | Demi-largeur $a$ | $a / \sqrt{3}$ | Résolution d'un instrument, tolérance d'un composant. |
| Triangulaire | Demi-largeur $a$ | $a / \sqrt{6}$ | Information plus précise que rectangulaire. |
| Normale | Incertitude élargie $U$, facteur $k$ | $U / k$ | Certificat d'étalonnage. |
| En U (arc-sinus) | Demi-amplitude $a$ | $a / \sqrt{2}$ | Oscillation sinusoïdale. |

### 11.4 Incertitude composée

$$u_c^2 = \sum_{i=1}^{N} c_i^2 \, u_i^2 \qquad c_i = \frac{\partial f}{\partial x_i}$$

Avec corrélations :

$$u_c^2 = \sum_{i=1}^{N} c_i^2 \, u_i^2 + 2 \sum_{i=1}^{N-1}\sum_{j=i+1}^{N} c_i \, c_j \, u(x_i, x_j)$$

### 11.5 Incertitude élargie

$$U = k \cdot u_c$$

| Facteur $k$ | Niveau de confiance |
|---|---|
| 1 | 68,3 % |
| 2 | 95,5 % |
| 3 | 99,7 % |

Le facteur $k = 2$ est le plus courant ($\approx 95\%$).

**Expression du résultat :** $Y = y \pm U \quad (k = 2)$

### 11.6 Budget d'incertitude - exemple

| Source | Type | Distribution | Valeur | Diviseur | $u_i$ |
|---|---|---|---|---|---|
| Répétabilité | A | Normale | $s = 0{,}012$ mm | $\sqrt{5}$ | 0,0054 |
| Résolution | B | Rectangulaire | $a = 0{,}005$ mm | $\sqrt{3}$ | 0,0029 |
| Étalonnage | B | Normale | $U = 0{,}010$ mm | $k = 2$ | 0,0050 |
| Température | B | Rectangulaire | $a = 0{,}003$ mm | $\sqrt{3}$ | 0,0017 |

$u_c = 0{,}0081$ mm, $U = 0{,}016$ mm ($k = 2$).

**Résultat :** $L = 25{,}032 \pm 0{,}016$ mm ($k = 2$, confiance $\approx 95\%$).

<!-- IMG:uncertainty_budget.png -->

### 11.7 Formule de Welch-Satterthwaite

$$\nu_{eff} = \frac{u_c^4}{\sum_{i=1}^{N} \frac{(c_i \, u_i)^4}{\nu_i}}$$

Si $\nu_{eff} < 30$, ajuster $k$ avec la distribution de Student (par exemple $k = 2{,}23$ pour $\nu_{eff} = 10$ à 95 %).

### 11.8 Règles de conformité (ISO 14253-1)

- **Conformité :** $LSI + U \leq y \leq LSS - U$
- **Non-conformité :** $y < LSI - U$ ou $y > LSS + U$
- **Zone d'incertitude :** largeur $2U$ de chaque côté de la limite de spécification.

---

## 12. Guide SPC (ISO 11462) - étapes d'implémentation

> **Note :** la norme ISO 11462 n'est pas indexée dans le RAG (norme payante).

ISO 11462-1 fournit des lignes directrices pour la mise en oeuvre du SPC. Étapes principales :

1. **Engagement de la direction :** ressources, objectifs, intégration ISO 9001.
2. **Identification des procédés critiques :** AMDEC, diagramme de flux, Pareto.
3. **Analyse du système de mesure :** GRR, ndc, linéarité, stabilité.
4. **Collecte des données :** caractéristique, taille de sous-groupe, fréquence, minimum 25 sous-groupes.
5. **Choix de la carte de contrôle** (cf. section 4.1.5).
6. **Calcul des limites de contrôle** (phase d'étude).
7. **Surveillance en production** (phase 2).
8. **OCAP (Out-of-Control Action Plan) :** identification cause spéciale (5M), action corrective, vérification, mise à jour des limites.
9. **Amélioration continue (PDCA) :** réduire la variabilité, centrer le procédé, réviser les limites.

---

## 13. Synthèse et articulations

**Séquence logique recommandée pour une étude de capabilité :**

1. **Valider le système de mesure** (ISO 22514-7) : %GRR $< 10\%$.
2. **Collecter les données** (ISO 7870-2) : au moins 25 sous-groupes.
3. **Tester la normalité** (ISO 5479) : Shapiro-Wilk + Q-Q plot.
4. **Détecter les valeurs aberrantes** (ISO 16269-4) : Grubbs ou Dixon.
5. **Construire les cartes de contrôle** (ISO 7870-2) : vérifier le contrôle statistique.
6. **Calculer la capabilité** (ISO 22514-2) : $C_p$, $C_{pk}$, $P_p$, $P_{pk}$.
7. **Estimer l'incertitude** (GUM) si nécessaire.
8. **Calculer les intervalles de tolérance** (ISO 16269-6) si nécessaire.

---

## 14. Documents open source indexés dans le RAG

Les documents suivants sont disponibles en accès libre et indexés dans la collection statistique du RAG :

| Référence | Titre |
|---|---|
| **JCGM 100:2008 (GUM)** | Évaluation des données de mesure - Guide pour l'expression de l'incertitude de mesure (version française). |
| **JCGM 100:2008 (GUM)** | Evaluation of measurement data - Guide to the expression of uncertainty in measurement (version anglaise). |
| **NIST SP 260-135** | Statistical methods for the certification of reference materials - Métrologie statistique. |
| **NIST TN 1297** | Guidelines for Evaluating and Expressing the Uncertainty of NIST Measurement Results. |

---

*Ce document constitue un support de cours et de référence. Pour des applications contractuelles ou réglementaires, il est indispensable de se référer directement aux textes normatifs officiels dans leur version en vigueur.*
