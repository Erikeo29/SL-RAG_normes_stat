# Cours de normes statistiques industrielles

Ce document constitue un cours de référence sur les principales normes statistiques utilisées en qualité industrielle. Il couvre l'échantillonnage, la maîtrise statistique des procédés (SPC), la capabilité, les tests de normalité, la détection des valeurs aberrantes, les intervalles de tolérance et l'incertitude de mesure. Chaque section renvoie aux normes ISO, ASTM ou guides internationaux correspondants.

---

## Sommaire

1. [Introduction — rôle des statistiques dans la qualité industrielle](#1-introduction--rôle-des-statistiques-dans-la-qualité-industrielle)
2. [Échantillonnage par attributs (ISO 2859)](#2-échantillonnage-par-attributs-iso-2859)
3. [Échantillonnage par mesures (ISO 3951)](#3-échantillonnage-par-mesures-iso-3951)
4. [Cartes de contrôle SPC (ISO 7870, ASTM E2587)](#4-cartes-de-contrôle-spc-iso-7870-astm-e2587)
5. [Capabilité des procédés (ISO 22514)](#5-capabilité-des-procédés-iso-22514)
6. [Capabilité des systèmes de mesure (ISO 22514-7)](#6-capabilité-des-systèmes-de-mesure-iso-22514-7)
7. [Tests de normalité (ISO 5479)](#7-tests-de-normalité-iso-5479)
8. [Comparaison de populations — tests et ANOVA (ISO 5725, ASTM E691)](#8-comparaison-de-populations--tests-et-anova-iso-5725-astm-e691)
9. [Détection des valeurs aberrantes (ISO 16269-4)](#9-détection-des-valeurs-aberrantes-iso-16269-4)
10. [Intervalles de tolérance statistiques (ISO 16269-6)](#10-intervalles-de-tolérance-statistiques-iso-16269-6)
11. [Incertitude de mesure (GUM, NIST)](#11-incertitude-de-mesure-gum-nist)
12. [Guide SPC (ISO 11462) — étapes d'implémentation](#12-guide-spc-iso-11462--étapes-dimplémentation)
13. [Synthèse et articulations — tableau croisé](#13-synthèse-et-articulations--tableau-croisé)
14. [Documents indexés dans le RAG](#14-documents-indexés-dans-le-rag)

---

## 1. Introduction — rôle des statistiques dans la qualité industrielle

### 1.1 Pourquoi les statistiques en production

La qualité industrielle repose sur la capacité à prendre des décisions fiables à partir de données limitées. Dans un contexte de production en série, il est impossible d'inspecter chaque pièce ni de surveiller en continu chaque paramètre de procédé. Les méthodes statistiques fournissent un cadre rigoureux pour :

- **Accepter ou refuser un lot** de produits sur la base d'un échantillon représentatif (échantillonnage).
- **Surveiller un procédé** en temps réel et détecter toute dérive avant qu'elle ne génère des non-conformités (cartes de contrôle SPC).
- **Quantifier la performance** d'un procédé par rapport aux spécifications client (capabilité).
- **Valider un système de mesure** avant de l'utiliser pour prendre des décisions (analyse GRR).
- **Estimer l'incertitude** associée à un résultat de mesure (GUM).

### 1.2 Panorama normatif ISO pour les méthodes statistiques

Les normes ISO relatives aux méthodes statistiques sont regroupées dans le comité technique ISO/TC 69 « Application des méthodes statistiques ». Les principales familles sont les suivantes :

| Famille de normes | Domaine |
|---|---|
| ISO 2859 | Échantillonnage par attributs (contrôle par comptage). |
| ISO 3951 | Échantillonnage par mesures (contrôle par variables). |
| ISO 7870 | Cartes de contrôle (SPC). |
| ISO 22514 | Capabilité des procédés et des systèmes de mesure. |
| ISO 5479 | Tests de normalité. |
| ISO 16269 | Intervalles statistiques (tolérance, confiance, prédiction). |
| ISO 11462 | Lignes directrices pour la mise en oeuvre du SPC. |

À ces normes ISO s'ajoutent des guides internationaux comme le GUM (JCGM 100:2008) pour l'incertitude de mesure, la note technique NIST TN 1297, et des normes ASTM comme E2587 pour les cartes de contrôle.

### 1.3 Concepts fondamentaux

**Population et échantillon.** La population est l'ensemble complet des individus (pièces, mesures) sur lequel porte l'étude. L'échantillon est un sous-ensemble de taille $n$ prélevé de la population de taille $N$. Toute inférence statistique repose sur la qualité de l'échantillonnage.

**Risque de première espèce ($\alpha$).** C'est la probabilité de rejeter un lot (ou de conclure à un signal) alors que le procédé est conforme. On l'appelle aussi risque du producteur. Typiquement $\alpha = 0{,}05$ (5 %).

**Risque de deuxième espèce ($\beta$).** C'est la probabilité d'accepter un lot (ou de ne pas détecter un signal) alors que le procédé est non conforme. On l'appelle aussi risque du consommateur. La puissance du test est $1 - \beta$.

**Niveau de confiance.** Le niveau de confiance $1 - \alpha$ exprime la probabilité que l'intervalle estimé contienne la vraie valeur du paramètre. Un niveau de confiance de 95 % signifie que, sur 100 intervalles construits de la même manière, environ 95 contiendraient la vraie valeur.

**Niveau de qualité acceptable (NQA ou AQL).** Le NQA est le pire niveau de qualité moyen du procédé que le consommateur considère comme acceptable. Il est exprimé en pourcentage de non-conformes dans le lot.

**Distribution normale.** La distribution normale (ou gaussienne) est le modèle probabiliste fondamental en statistique industrielle. Elle est caractérisée par deux paramètres : la moyenne $\mu$ et l'écart-type $\sigma$. La règle empirique donne les probabilités suivantes :
- $\pm 1\sigma$ : 68,27 % de la population.
- $\pm 2\sigma$ : 95,45 % de la population.
- $\pm 3\sigma$ : 99,73 % de la population.

<!-- IMG:normal_distribution_3sigma.png -->

**Degré de liberté ($\nu$).** Le nombre de degrés de liberté est le nombre de valeurs indépendantes qui peuvent varier dans un calcul statistique. Pour l'écart-type d'un échantillon de taille $n$, le nombre de degrés de liberté est $\nu = n - 1$.

**Vocabulaire lié aux non-conformités.** Il est important de distinguer :
- **Non-conforme** (nonconforming) : une unité qui ne satisfait pas au moins une spécification. Une pièce est soit conforme, soit non conforme.
- **Non-conformité** (nonconformity) : un écart individuel par rapport à une spécification. Une même pièce peut présenter plusieurs non-conformités.

---

## 2. Échantillonnage par attributs (ISO 2859)

L'échantillonnage par attributs consiste à inspecter un échantillon de $n$ unités prélevées dans un lot et à les classer en conformes ou non conformes (critère binaire : passe / ne passe pas). La décision d'acceptation ou de refus du lot repose sur le nombre d'unités non conformes trouvées dans l'échantillon.

### 2.1 ISO 2859-1 — plans indexés par NQA

La norme ISO 2859-1 (équivalente à la norme ANSI/ASQ Z1.4) définit des plans d'échantillonnage indexés par le niveau de qualité acceptable (NQA). Elle est la référence mondiale pour le contrôle par attributs en réception.

#### 2.1.1 Terminologie

| Terme | Définition |
|---|---|
| **Lot** | Quantité définie de produits fabriqués dans des conditions supposées uniformes. |
| **Taille d'échantillon** ($n$) | Nombre d'unités prélevées dans le lot pour inspection. |
| **NQA** (AQL) | Niveau de qualité acceptable : pourcentage maximal de non-conformes considéré comme satisfaisant en moyenne de procédé. |
| **Nombre d'acceptation** ($Ac$) | Nombre maximal de non-conformes dans l'échantillon pour accepter le lot. |
| **Nombre de rejet** ($Re$) | Nombre minimal de non-conformes dans l'échantillon pour rejeter le lot. $Re = Ac + 1$ pour les plans simples. |
| **Courbe OC** | Courbe d'efficacité (Operating Characteristic) donnant la probabilité d'acceptation en fonction de la proportion réelle de non-conformes. |

#### 2.1.2 Niveaux d'inspection

ISO 2859-1 définit trois niveaux d'inspection généraux et quatre niveaux spéciaux :

| Niveau | Usage | Taille d'échantillon relative |
|---|---|---|
| **I** | Inspection réduite, moins discriminante. | Plus petite. |
| **II** | Inspection normale, usage par défaut. | Référence. |
| **III** | Inspection renforcée, plus discriminante. | Plus grande. |
| **S-1** | Inspection spéciale, essais coûteux ou destructifs. | Très petite. |
| **S-2** | Inspection spéciale. | Très petite. |
| **S-3** | Inspection spéciale. | Petite. |
| **S-4** | Inspection spéciale. | Petite. |

Le niveau II est le niveau par défaut. Les niveaux spéciaux S-1 à S-4 sont utilisés lorsque les essais sont destructifs ou très coûteux et que l'on doit minimiser la taille de l'échantillon.

#### 2.1.3 Table des codes lettres (taille de lot vers code lettre)

La première étape consiste à déterminer le code lettre à partir de la taille du lot et du niveau d'inspection choisi.

| Taille du lot | S-1 | S-2 | S-3 | S-4 | I | II | III |
|---|---|---|---|---|---|---|---|
| 2 à 8 | A | A | A | A | A | A | B |
| 9 à 15 | A | A | A | A | A | B | C |
| 16 à 25 | A | A | B | B | B | C | D |
| 26 à 50 | A | B | B | C | C | D | E |
| 51 à 90 | B | B | C | C | C | E | F |
| 91 à 150 | B | B | C | D | D | F | G |
| 151 à 280 | B | C | D | E | E | G | H |
| 281 à 500 | B | C | D | E | F | H | J |
| 501 à 1200 | C | C | E | F | G | J | K |
| 1201 à 3200 | C | D | E | G | H | K | L |
| 3201 à 10000 | C | D | F | G | J | L | M |
| 10001 à 35000 | C | D | F | H | K | M | N |
| 35001 à 150000 | D | E | G | J | L | N | P |
| 150001 à 500000 | D | E | G | J | M | P | Q |
| 500001 et plus | D | E | H | K | N | Q | R |

#### 2.1.4 Plans d'échantillonnage simple — inspection normale

Une fois le code lettre déterminé, on lit la taille d'échantillon $n$ et les nombres $Ac$ / $Re$ dans la table correspondant au NQA choisi. Exemple de plans pour l'inspection normale (extrait) :

| Code | $n$ | NQA 0,65 | NQA 1,0 | NQA 1,5 | NQA 2,5 | NQA 4,0 | NQA 6,5 |
|---|---|---|---|---|---|---|---|
| A | 2 | — | — | — | 0/1 | 0/1 | 1/2 |
| B | 3 | — | — | 0/1 | 0/1 | 0/1 | 1/2 |
| C | 5 | — | 0/1 | 0/1 | 0/1 | 1/2 | 2/3 |
| D | 8 | 0/1 | 0/1 | 0/1 | 1/2 | 1/2 | 2/3 |
| E | 13 | 0/1 | 0/1 | 1/2 | 1/2 | 2/3 | 3/4 |
| F | 20 | 0/1 | 1/2 | 1/2 | 2/3 | 3/4 | 5/6 |
| G | 32 | 1/2 | 1/2 | 2/3 | 3/4 | 5/6 | 7/8 |
| H | 50 | 1/2 | 2/3 | 3/4 | 5/6 | 7/8 | 10/11 |
| J | 80 | 2/3 | 3/4 | 5/6 | 7/8 | 10/11 | 14/15 |
| K | 125 | 3/4 | 5/6 | 7/8 | 10/11 | 14/15 | 21/22 |

*Notation : $Ac$/$Re$. Le symbole « — » indique que le plan n'est pas disponible pour ce NQA.*

#### 2.1.5 Inspection renforcée et inspection réduite

**Inspection renforcée (tightened).** Les critères d'acceptation sont plus sévères (nombres $Ac$ réduits pour la même taille d'échantillon). On passe en inspection renforcée lorsque la qualité des lots se dégrade.

**Inspection réduite (reduced).** La taille d'échantillon est diminuée et les critères sont assouplis. On y accède lorsque la qualité est régulièrement bonne.

#### 2.1.6 Règles de commutation (switching rules)

Les règles de commutation entre les trois sévérités d'inspection sont définies à la clause 9 de l'ISO 2859-1.

**Normal vers renforcé.** Passer en inspection renforcée lorsque 2 lots sur 5 consécutifs (ou moins) sont refusés en inspection normale.

**Renforcé vers normal.** Revenir en inspection normale lorsque 5 lots consécutifs sont acceptés en inspection renforcée.

**Normal vers réduit.** Passer en inspection réduite lorsque les trois conditions suivantes sont simultanément remplies :
- Les 10 derniers lots ont été acceptés en inspection normale.
- Le nombre total de non-conformes dans ces 10 échantillons ne dépasse pas un seuil spécifié.
- La production est régulière et stable.

**Réduit vers normal.** Revenir en inspection normale dès qu'un lot est refusé en inspection réduite, ou que d'autres conditions d'instabilité sont détectées.

**Arrêt de l'inspection.** Si, en inspection renforcée, 5 lots consécutifs restent refusés, l'inspection est suspendue et des actions correctives sont exigées avant reprise.

<!-- IMG:switching_rules_diagram.png -->

#### 2.1.7 Courbes d'efficacité (OC curves)

La courbe d'efficacité (Operating Characteristic curve) donne la probabilité d'acceptation $P_a$ du lot en fonction de la proportion réelle de non-conformes $p$ dans le lot.

Pour un plan d'échantillonnage simple avec taille d'échantillon $n$ et nombre d'acceptation $Ac$, la probabilité d'acceptation suit la loi binomiale :

$$P_a(p) = \sum_{i=0}^{Ac} \binom{n}{i} p^i (1-p)^{n-i}$$

Pour les grands lots et petites proportions $p$, l'approximation de Poisson est utilisée :

$$P_a(p) \approx \sum_{i=0}^{Ac} \frac{(np)^i}{i!} e^{-np}$$

La courbe OC permet de visualiser :
- Le **point NQA** : la proportion $p$ pour laquelle $P_a \approx 0{,}95$ (risque producteur $\alpha \approx 5\%$).
- Le **point LQ** : la proportion $p$ pour laquelle $P_a \approx 0{,}10$ (risque consommateur $\beta \approx 10\%$).

<!-- IMG:oc_curve_sampling.png -->

#### 2.1.8 Risque du producteur ($\alpha$) et risque du consommateur ($\beta$)

| Risque | Symbole | Définition | Valeur typique |
|---|---|---|---|
| Risque du producteur | $\alpha$ | Probabilité de rejeter un lot dont la qualité est au NQA. | $\approx 5\%$ |
| Risque du consommateur | $\beta$ | Probabilité d'accepter un lot dont la qualité est au niveau LQ. | $\approx 10\%$ |

Le choix du plan d'échantillonnage est un compromis entre ces deux risques. Un plan plus discriminant (taille d'échantillon plus grande) réduit simultanément $\alpha$ et $\beta$, mais augmente le coût d'inspection.

### 2.2 ISO 2859-2 — plans pour lots isolés (LQ)

Lorsque les lots ne font pas partie d'une série continue (lot isolé, premier lot d'un nouveau fournisseur), on ne peut pas utiliser les règles de commutation de l'ISO 2859-1. L'ISO 2859-2 propose des plans d'échantillonnage indexés par la qualité limite (LQ ou Limiting Quality).

La LQ est le niveau de qualité correspondant à une faible probabilité d'acceptation (typiquement $P_a = 0{,}10$). Le plan est choisi de sorte que, si la proportion réelle de non-conformes atteint la LQ, le lot a au plus 10 % de chance d'être accepté.

**Procédure :**
1. Définir la LQ souhaitée (en pourcentage de non-conformes).
2. Déterminer la taille du lot $N$.
3. Lire dans les tables de l'ISO 2859-2 la taille d'échantillon $n$ et le nombre d'acceptation $Ac$.
4. Prélever $n$ unités, inspecter et compter les non-conformes $d$.
5. Si $d \leq Ac$ : accepter le lot. Si $d \geq Re$ : refuser le lot.

---

## 3. Échantillonnage par mesures (ISO 3951)

L'échantillonnage par mesures (ou par variables) exploite la valeur numérique mesurée sur chaque unité de l'échantillon, et non pas un simple classement conforme / non conforme. Cela permet d'obtenir une meilleure discrimination avec un échantillon plus petit qu'en échantillonnage par attributs.

### 3.1 Quand utiliser l'échantillonnage par mesures

L'échantillonnage par mesures est préférable lorsque :
- La caractéristique contrôlée est mesurable sur une échelle continue.
- La distribution de la caractéristique est approximativement normale (hypothèse fondamentale).
- On souhaite réduire la taille d'échantillon par rapport à un plan par attributs équivalent.
- Le coût d'une mesure individuelle est acceptable.

Il n'est **pas** approprié lorsque :
- La caractéristique est qualitative (visuelle, fonctionnelle).
- La distribution est fortement non normale et ne peut pas être transformée.
- Plusieurs caractéristiques doivent être contrôlées simultanément avec des distributions différentes.

### 3.2 ISO 3951-1 — plans indexés par NQA

L'ISO 3951-1 propose deux méthodes principales selon que l'écart-type du procédé est connu ou non.

#### 3.2.1 Méthode « s » (écart-type inconnu)

Lorsque l'écart-type du procédé $\sigma$ n'est pas connu, on l'estime à partir de l'échantillon par l'écart-type corrigé $s$ :

$$s = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2}$$

**Critère d'acceptation pour une spécification unilatérale supérieure :**

On calcule la statistique de qualité :

$$Q_U = \frac{LSS - \bar{x}}{s}$$

où $LSS$ est la limite de spécification supérieure (USL). Si $Q_U \geq k$, le lot est accepté. Sinon, il est refusé.

**Critère d'acceptation pour une spécification unilatérale inférieure :**

$$Q_L = \frac{\bar{x} - LSI}{s}$$

où $LSI$ est la limite de spécification inférieure (LSL). Si $Q_L \geq k$, le lot est accepté.

La constante d'acceptabilité $k$ dépend du NQA, du code lettre (taille de lot et niveau d'inspection) et de la sévérité d'inspection.

#### 3.2.2 Méthode « $\sigma$ » (écart-type connu)

Lorsque l'écart-type $\sigma$ est connu (par exemple, grâce à un historique fiable de production), on utilise directement $\sigma$ à la place de $s$ :

$$Q_U = \frac{LSS - \bar{x}}{\sigma}$$

$$Q_L = \frac{\bar{x} - LSI}{\sigma}$$

La méthode $\sigma$ permet des tailles d'échantillon plus petites que la méthode $s$ car il n'y a pas d'incertitude liée à l'estimation de l'écart-type.

#### 3.2.3 Constante d'acceptabilité $k$ — extrait de tables

Les valeurs de $k$ pour l'inspection normale, méthode $s$, sont données ci-dessous (extrait) :

| Code | $n$ | NQA 0,65 | NQA 1,0 | NQA 1,5 | NQA 2,5 | NQA 4,0 | NQA 6,5 |
|---|---|---|---|---|---|---|---|
| B | 3 | — | — | — | — | 0,950 | 0,566 |
| C | 4 | — | — | — | 1,452 | 0,917 | 0,550 |
| D | 5 | — | — | 1,666 | 1,242 | 0,874 | 0,536 |
| E | 7 | — | 1,879 | 1,490 | 1,133 | 0,824 | 0,523 |
| F | 10 | 2,058 | 1,715 | 1,400 | 1,066 | 0,790 | 0,516 |
| G | 15 | 1,909 | 1,618 | 1,342 | 1,030 | 0,770 | 0,513 |
| H | 20 | 1,833 | 1,565 | 1,307 | 1,011 | 0,759 | 0,512 |
| J | 25 | 1,786 | 1,530 | 1,283 | 0,998 | 0,752 | 0,511 |
| K | 35 | 1,736 | 1,494 | 1,259 | 0,984 | 0,745 | 0,510 |
| L | 50 | 1,696 | 1,464 | 1,239 | 0,973 | 0,739 | 0,509 |

*Le symbole « — » indique que le plan n'est pas disponible pour ce NQA.*

#### 3.2.4 Spécifications bilatérales

Pour les spécifications bilatérales (limites inférieure $LSI$ et supérieure $LSS$), ISO 3951-1 propose deux approches :

**Méthode combinée.** On calcule séparément $Q_U$ et $Q_L$ et on utilise une table spécifique pour vérifier que la proportion estimée de non-conformes (côtés supérieur et inférieur combinés) ne dépasse pas le NQA.

**Méthode séparée.** On applique le critère d'acceptation indépendamment pour chaque limite. Cette méthode est plus conservatrice.

---

## 4. Cartes de contrôle SPC (ISO 7870, ASTM E2587)

La maîtrise statistique des procédés (Statistical Process Control, SPC) est un ensemble de méthodes permettant de surveiller un procédé de production en temps réel à l'aide de cartes de contrôle. L'objectif est de distinguer les variations dues à des causes communes (inhérentes au procédé, aléatoires) de celles dues à des causes spéciales (assignables, identifiables et corrigeables).

### Principes fondamentaux (Shewhart)

Walter A. Shewhart a introduit le concept de carte de contrôle dans les années 1920 aux laboratoires Bell. Le principe repose sur le théorème suivant : un procédé sous contrôle statistique ne présente que des variations aléatoires, prévisibles par les lois de la statistique. Toute observation sortant des limites de contrôle, ou tout motif non aléatoire dans les données, signale une cause spéciale qu'il faut identifier et éliminer.

Une carte de contrôle comprend trois lignes horizontales :
- **LCS** (limite de contrôle supérieure, UCL) : $CL + 3\sigma$.
- **LC** (ligne centrale, CL) : valeur moyenne du paramètre surveillé.
- **LCI** (limite de contrôle inférieure, LCL) : $CL - 3\sigma$.

Les limites à $\pm 3\sigma$ correspondent à une probabilité de fausse alarme d'environ 0,27 % par point (soit environ 1 point sur 370 en dehors des limites par hasard seul, si le procédé est sous contrôle et la distribution est normale).

**Attention :** les limites de contrôle ne sont PAS les limites de spécification. Les limites de contrôle sont calculées à partir des données du procédé et reflètent sa variabilité naturelle. Les limites de spécification sont définies par le client ou le concepteur.

### ISO 7870-1 — guide général

L'ISO 7870-1 fournit un cadre général pour la sélection et l'utilisation des cartes de contrôle. Elle couvre les définitions, les types de cartes, les conditions d'application et les lignes directrices pour l'interprétation.

### ISO 7870-2 — cartes de contrôle pour variables et pour attributs

L'ISO 7870-2 détaille les formules, les constantes et les procédures pour les principaux types de cartes de contrôle.

---

### 4.1 Cartes pour variables

Les cartes pour variables utilisent des données mesurées sur une échelle continue (dimensions, masses, concentrations, etc.).

#### 4.1.1 Carte $\bar{x}$ / R (moyenne et étendue)

C'est la carte de contrôle la plus utilisée pour des sous-groupes de petite taille ($2 \leq n \leq 10$). Elle se compose de deux graphiques :
- La carte $\bar{x}$ surveille la position (moyenne) du procédé.
- La carte $R$ surveille la dispersion (étendue) du procédé.

**Collecte des données.** On prélève $k$ sous-groupes de taille $n$. Pour chaque sous-groupe $j$ :
- Moyenne : $\bar{x}_j = \frac{1}{n} \sum_{i=1}^{n} x_{ij}$
- Étendue : $R_j = x_{max,j} - x_{min,j}$

**Calcul des paramètres centraux :**
- Moyenne générale (grand mean) : $\bar{\bar{x}} = \frac{1}{k} \sum_{j=1}^{k} \bar{x}_j$
- Étendue moyenne : $\bar{R} = \frac{1}{k} \sum_{j=1}^{k} R_j$

**Limites de contrôle pour la carte $\bar{x}$ :**

$$UCL_{\bar{x}} = \bar{\bar{x}} + A_2 \bar{R}$$

$$CL_{\bar{x}} = \bar{\bar{x}}$$

$$LCL_{\bar{x}} = \bar{\bar{x}} - A_2 \bar{R}$$

**Limites de contrôle pour la carte $R$ :**

$$UCL_R = D_4 \bar{R}$$

$$CL_R = \bar{R}$$

$$LCL_R = D_3 \bar{R}$$

**Estimation de l'écart-type intra-groupe :**

$$\hat{\sigma} = \frac{\bar{R}}{d_2}$$

**Table des constantes pour la carte $\bar{x}$ / R ($n$ = 2 à 10) :**

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

*Note : $D_3 = 0$ pour $n \leq 6$ signifie que $LCL_R = 0$ (pas de limite inférieure sur la carte R).*

**Exemple numérique.** Supposons $k = 25$ sous-groupes de taille $n = 5$, avec $\bar{\bar{x}} = 50{,}00$ mm et $\bar{R} = 0{,}40$ mm.

- $UCL_{\bar{x}} = 50{,}00 + 0{,}577 \times 0{,}40 = 50{,}231$ mm
- $LCL_{\bar{x}} = 50{,}00 - 0{,}577 \times 0{,}40 = 49{,}769$ mm
- $UCL_R = 2{,}114 \times 0{,}40 = 0{,}846$ mm
- $LCL_R = 0 \times 0{,}40 = 0$ mm
- $\hat{\sigma} = 0{,}40 / 2{,}326 = 0{,}172$ mm

<!-- IMG:control_chart_xbar.png -->

#### 4.1.2 Carte $\bar{x}$ / S (moyenne et écart-type)

La carte $\bar{x}$ / S est préférée lorsque la taille des sous-groupes est grande ($n \geq 10$), car l'étendue $R$ devient un estimateur moins efficace de la dispersion pour les grands sous-groupes. L'écart-type $s$ est alors un estimateur plus fiable.

**Calcul des paramètres :**
- Écart-type du sous-groupe $j$ : $s_j = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_{ij} - \bar{x}_j)^2}$
- Écart-type moyen : $\bar{S} = \frac{1}{k}\sum_{j=1}^{k} s_j$

**Limites de contrôle pour la carte $\bar{x}$ :**

$$UCL_{\bar{x}} = \bar{\bar{x}} + A_3 \bar{S}$$

$$CL_{\bar{x}} = \bar{\bar{x}}$$

$$LCL_{\bar{x}} = \bar{\bar{x}} - A_3 \bar{S}$$

**Limites de contrôle pour la carte $S$ :**

$$UCL_S = B_4 \bar{S}$$

$$CL_S = \bar{S}$$

$$LCL_S = B_3 \bar{S}$$

**Estimation de l'écart-type intra-groupe :**

$$\hat{\sigma} = \frac{\bar{S}}{c_4}$$

**Table des constantes pour la carte $\bar{x}$ / S ($n$ = 2 à 25) :**

| $n$ | $A_3$ | $B_3$ | $B_4$ | $c_4$ |
|---|---|---|---|---|
| 2 | 2,659 | 0 | 3,267 | 0,7979 |
| 3 | 1,954 | 0 | 2,568 | 0,8862 |
| 4 | 1,628 | 0 | 2,266 | 0,9213 |
| 5 | 1,427 | 0 | 2,089 | 0,9400 |
| 6 | 1,287 | 0,030 | 1,970 | 0,9515 |
| 7 | 1,182 | 0,118 | 1,882 | 0,9594 |
| 8 | 1,099 | 0,185 | 1,815 | 0,9650 |
| 9 | 1,032 | 0,239 | 1,761 | 0,9693 |
| 10 | 0,975 | 0,284 | 1,716 | 0,9727 |
| 11 | 0,927 | 0,321 | 1,679 | 0,9754 |
| 12 | 0,886 | 0,354 | 1,646 | 0,9776 |
| 13 | 0,850 | 0,382 | 1,618 | 0,9794 |
| 14 | 0,817 | 0,406 | 1,594 | 0,9810 |
| 15 | 0,789 | 0,428 | 1,572 | 0,9823 |
| 16 | 0,763 | 0,448 | 1,552 | 0,9835 |
| 17 | 0,739 | 0,466 | 1,534 | 0,9845 |
| 18 | 0,718 | 0,482 | 1,518 | 0,9854 |
| 19 | 0,698 | 0,497 | 1,503 | 0,9862 |
| 20 | 0,680 | 0,510 | 1,490 | 0,9869 |
| 21 | 0,663 | 0,523 | 1,477 | 0,9876 |
| 22 | 0,647 | 0,534 | 1,466 | 0,9882 |
| 23 | 0,633 | 0,545 | 1,455 | 0,9887 |
| 24 | 0,619 | 0,555 | 1,445 | 0,9892 |
| 25 | 0,606 | 0,565 | 1,435 | 0,9896 |

#### 4.1.3 Carte I-MR (individuelle et étendue mobile)

La carte I-MR (Individual - Moving Range) est utilisée lorsque les données sont collectées une par une ($n = 1$), par exemple lorsque :
- La production est très lente (une pièce par heure ou par jour).
- Les mesures sont coûteuses ou destructives.
- Chaque mesure représente un lot ou un batch.
- Les données sont homogènes (pas de sous-groupes naturels).

**Calcul des paramètres :**
- Moyenne : $\bar{X} = \frac{1}{k}\sum_{j=1}^{k} x_j$
- Étendue mobile (moving range) : $MR_j = |x_j - x_{j-1}|$ pour $j = 2, 3, \ldots, k$
- Étendue mobile moyenne : $\bar{MR} = \frac{1}{k-1}\sum_{j=2}^{k} MR_j$

**Limites de contrôle pour la carte I (individuelle) :**

$$UCL_X = \bar{X} + 2{,}66 \, \bar{MR}$$

$$CL_X = \bar{X}$$

$$LCL_X = \bar{X} - 2{,}66 \, \bar{MR}$$

Le coefficient $2{,}66 = 3 / d_2 = 3 / 1{,}128$ provient de la relation entre l'étendue mobile (calculée sur des paires consécutives, $n = 2$) et l'écart-type.

**Limites de contrôle pour la carte MR :**

$$UCL_{MR} = D_4 \, \bar{MR} = 3{,}267 \, \bar{MR}$$

$$CL_{MR} = \bar{MR}$$

$$LCL_{MR} = D_3 \, \bar{MR} = 0$$

Les constantes utilisées sont celles de $n = 2$ car l'étendue mobile est calculée sur des paires de valeurs consécutives : $d_2 = 1{,}128$, $D_3 = 0$, $D_4 = 3{,}267$.

**Estimation de l'écart-type :**

$$\hat{\sigma} = \frac{\bar{MR}}{d_2} = \frac{\bar{MR}}{1{,}128}$$

**Important :** la carte I-MR est sensible aux écarts de normalité. Si les données ne suivent pas une distribution approximativement normale, les limites de contrôle peuvent être trompeuses. Il est recommandé de vérifier la normalité (section 7) avant d'utiliser cette carte.

**Exemple numérique.** On mesure quotidiennement le pH d'un bain de traitement de surface. Sur 20 jours, on obtient $\bar{X} = 4{,}50$ et $\bar{MR} = 0{,}15$.

- $UCL_X = 4{,}50 + 2{,}66 \times 0{,}15 = 4{,}899$
- $LCL_X = 4{,}50 - 2{,}66 \times 0{,}15 = 4{,}101$
- $UCL_{MR} = 3{,}267 \times 0{,}15 = 0{,}490$
- $\hat{\sigma} = 0{,}15 / 1{,}128 = 0{,}133$

#### 4.1.4 Phase d'étude et phase de surveillance

La mise en place d'une carte de contrôle se déroule en deux phases distinctes.

**Phase 1 — étude (rétrospective).** On collecte des données historiques (au moins 25 sous-groupes selon ISO 7870-2, clause 7.2). On calcule les limites de contrôle provisoires et on vérifie qu'aucun point n'est hors contrôle. Si des points hors contrôle sont identifiés :
1. Rechercher la cause spéciale.
2. Si la cause est trouvée et éliminée, retirer le sous-groupe et recalculer les limites.
3. Répéter jusqu'à obtenir un procédé sous contrôle.

Les limites finales de la phase 1 deviennent les limites de référence pour la phase 2.

**Phase 2 — surveillance (prospective).** On utilise les limites calculées en phase 1 pour surveiller la production en temps réel. Chaque nouveau point est tracé et évalué. Les règles Western Electric / Nelson (section 4.3) sont appliquées. Les limites ne sont recalculées que si le procédé a été modifié intentionnellement (nouveau réglage, nouvelle matière, amélioration).

#### 4.1.5 Choix entre les cartes pour variables

| Critère | $\bar{x}$ / R | $\bar{x}$ / S | I-MR |
|---|---|---|---|
| Taille de sous-groupe | $2 \leq n \leq 9$ | $n \geq 10$ | $n = 1$ |
| Estimation de $\sigma$ | $\bar{R}/d_2$ | $\bar{S}/c_4$ | $\bar{MR}/d_2$ ($n=2$) |
| Efficacité statistique | Bonne pour petits $n$. | Meilleure pour grands $n$. | Moins efficace (pas de sous-groupes). |
| Sensibilité aux outliers | Moyenne. | Plus robuste. | Élevée (un seul point par sous-groupe). |
| Hypothèse de normalité | Robuste (théorème central limite). | Robuste (théorème central limite). | Sensible (pas de moyennage). |
| Complexité | Simple. | Modérée. | Simple. |

#### 4.1.6 Estimation de $\sigma$ — comparaison des méthodes

L'estimation de l'écart-type intra-groupe $\hat{\sigma}$ peut être obtenue de trois manières :

| Méthode | Formule | Carte associée | Biais |
|---|---|---|---|
| Étendue moyenne | $\hat{\sigma} = \bar{R} / d_2$ | $\bar{x}$ / R | Non biaisé (corrigé par $d_2$). |
| Écart-type moyen | $\hat{\sigma} = \bar{S} / c_4$ | $\bar{x}$ / S | Non biaisé (corrigé par $c_4$). |
| Étendue mobile | $\hat{\sigma} = \bar{MR} / d_2$ ($n=2$) | I-MR | Non biaisé (corrigé par $d_2$). |
| Écart-type poolé | $\hat{\sigma} = S_p = \sqrt{\frac{\sum(n_j-1)s_j^2}{\sum(n_j-1)}}$ | Alternative | Non biaisé, estimateur le plus efficace. |

---

### 4.2 Cartes pour attributs

Les cartes pour attributs utilisent des données discrètes (nombre ou proportion de non-conformes, nombre de défauts, etc.).

#### 4.2.1 Carte $p$ (proportion de non-conformes)

La carte $p$ surveille la fraction de pièces non conformes dans des échantillons qui peuvent être de taille variable. Elle est basée sur la loi binomiale.

**Paramètre central :**

$$\bar{p} = \frac{\sum_{j=1}^{k} d_j}{\sum_{j=1}^{k} n_j}$$

où $d_j$ est le nombre de non-conformes dans le sous-groupe $j$ de taille $n_j$.

**Limites de contrôle :**

$$UCL_p = \bar{p} + 3\sqrt{\frac{\bar{p}(1 - \bar{p})}{n}}$$

$$CL_p = \bar{p}$$

$$LCL_p = \bar{p} - 3\sqrt{\frac{\bar{p}(1 - \bar{p})}{n}}$$

Si $LCL_p < 0$, on pose $LCL_p = 0$. Lorsque la taille des échantillons varie, les limites de contrôle sont recalculées pour chaque sous-groupe.

**Condition d'application :** $n\bar{p} \geq 5$ et $n(1 - \bar{p}) \geq 5$ pour que l'approximation normale soit valable.

#### 4.2.2 Carte $np$ (nombre de non-conformes)

La carte $np$ surveille le nombre de pièces non conformes dans des échantillons de **taille constante** $n$. C'est une variante de la carte $p$ plus facile à interpréter.

**Limites de contrôle :**

$$UCL_{np} = n\bar{p} + 3\sqrt{n\bar{p}(1 - \bar{p})}$$

$$CL_{np} = n\bar{p}$$

$$LCL_{np} = n\bar{p} - 3\sqrt{n\bar{p}(1 - \bar{p})}$$

Si $LCL_{np} < 0$, on pose $LCL_{np} = 0$.

#### 4.2.3 Carte $c$ (nombre de non-conformités)

La carte $c$ surveille le nombre total de non-conformités (défauts) dans une unité d'inspection de taille constante. Elle est basée sur la loi de Poisson.

**Paramètre central :**

$$\bar{c} = \frac{\sum_{j=1}^{k} c_j}{k}$$

**Limites de contrôle :**

$$UCL_c = \bar{c} + 3\sqrt{\bar{c}}$$

$$CL_c = \bar{c}$$

$$LCL_c = \bar{c} - 3\sqrt{\bar{c}}$$

Si $LCL_c < 0$, on pose $LCL_c = 0$.

**Exemple.** On compte le nombre de soudures défectueuses sur des cartes électroniques. Si $\bar{c} = 4{,}0$ :
- $UCL_c = 4{,}0 + 3\sqrt{4{,}0} = 4{,}0 + 6{,}0 = 10{,}0$
- $LCL_c = 4{,}0 - 6{,}0 = -2{,}0 \rightarrow 0$

#### 4.2.4 Carte $u$ (taux de non-conformités par unité)

La carte $u$ surveille le nombre de non-conformités par unité d'inspection. Elle est utilisée lorsque la taille des unités d'inspection varie.

**Paramètre central :**

$$\bar{u} = \frac{\sum_{j=1}^{k} c_j}{\sum_{j=1}^{k} n_j}$$

**Limites de contrôle :**

$$UCL_u = \bar{u} + 3\sqrt{\frac{\bar{u}}{n}}$$

$$CL_u = \bar{u}$$

$$LCL_u = \bar{u} - 3\sqrt{\frac{\bar{u}}{n}}$$

Si $LCL_u < 0$, on pose $LCL_u = 0$. Lorsque la taille $n$ varie, les limites sont recalculées pour chaque sous-groupe.

**Tableau récapitulatif des cartes pour attributs :**

| Carte | Données surveillées | Taille d'échantillon | Distribution | Formule UCL |
|---|---|---|---|---|
| $p$ | Fraction non conforme | Variable ou constante | Binomiale | $\bar{p} + 3\sqrt{\bar{p}(1-\bar{p})/n}$ |
| $np$ | Nombre de non-conformes | Constante | Binomiale | $n\bar{p} + 3\sqrt{n\bar{p}(1-\bar{p})}$ |
| $c$ | Nombre de non-conformités | Constante | Poisson | $\bar{c} + 3\sqrt{\bar{c}}$ |
| $u$ | Taux de non-conformités/unité | Variable ou constante | Poisson | $\bar{u} + 3\sqrt{\bar{u}/n}$ |

---

### 4.3 Règles Western Electric / Nelson

Les limites de contrôle à $\pm 3\sigma$ constituent la règle de base de Shewhart. Cependant, la carte de Shewhart seule est peu sensible aux petits décalages de moyenne. Les règles complémentaires de Western Electric (WECO, 1956) et de Nelson (1984) augmentent la sensibilité en détectant des motifs non aléatoires dans les données, même si aucun point ne dépasse les limites de contrôle.

Pour appliquer ces règles, on divise la zone entre les limites de contrôle en trois bandes de chaque côté de la ligne centrale :
- **Zone A** : entre $2\sigma$ et $3\sigma$ de la ligne centrale.
- **Zone B** : entre $1\sigma$ et $2\sigma$ de la ligne centrale.
- **Zone C** : entre la ligne centrale et $1\sigma$.

#### Règle 1 — un point au-delà de 3$\sigma$

**Description :** un seul point se situe au-delà de la limite de contrôle supérieure ou inférieure (en dehors de la zone A).

**Signal :** cause spéciale évidente, événement isolé majeur.

**Probabilité de fausse alarme :** 0,27 % par point.

#### Règle 2 — 9 points consécutifs du même côté de la ligne centrale

**Description :** neuf points consécutifs se situent tous au-dessus ou tous en dessous de la ligne centrale.

**Signal :** décalage durable de la moyenne du procédé.

**Probabilité de fausse alarme :** $(0{,}5)^9 = 0{,}195\%$ par séquence de 9.

#### Règle 3 — 6 points consécutifs en augmentation ou diminution monotone

**Description :** six points consécutifs montrent une tendance strictement croissante ou strictement décroissante.

**Signal :** dérive progressive du procédé (usure d'outil, dérive de température, etc.).

#### Règle 4 — 14 points consécutifs alternant haut et bas

**Description :** quatorze points consécutifs alternent en montant et descendant de manière régulière.

**Signal :** surcontrôle du procédé, ou deux sources de variation alternées (par exemple, deux machines alternant la production).

#### Règle 5 — 2 points sur 3 au-delà de 2$\sigma$ (même côté)

**Description :** deux points sur trois consécutifs se situent dans la zone A (entre $2\sigma$ et $3\sigma$) du même côté de la ligne centrale.

**Signal :** augmentation temporaire de la variabilité ou décalage momentané de la moyenne.

#### Règle 6 — 4 points sur 5 au-delà de 1$\sigma$ (même côté)

**Description :** quatre points sur cinq consécutifs se situent au-delà de $1\sigma$ (dans les zones A ou B) du même côté de la ligne centrale.

**Signal :** décalage modéré de la moyenne.

#### Règle 7 — 15 points consécutifs dans la zone C (stratification)

**Description :** quinze points consécutifs se situent tous dans la zone C (entre la ligne centrale et $1\sigma$), de part et d'autre de la ligne centrale.

**Signal :** stratification — les données proviennent de sources mélangées dont les moyennes sont proches, ou les limites de contrôle sont trop larges.

#### Règle 8 — 8 points consécutifs au-delà de 1$\sigma$ (mélange)

**Description :** huit points consécutifs se situent tous au-delà de $1\sigma$ de la ligne centrale (dans les zones A ou B), de part et d'autre.

**Signal :** mélange — les données proviennent de deux distributions différentes (deux machines, deux opérateurs, deux lots de matière première).

**Tableau récapitulatif des règles Western Electric / Nelson :**

| Règle | Description | Signal typique |
|---|---|---|
| 1 | 1 point au-delà de $3\sigma$ | Cause spéciale isolée. |
| 2 | 9 points du même côté du CL | Décalage de moyenne. |
| 3 | 6 points en tendance monotone | Dérive progressive. |
| 4 | 14 points alternant haut/bas | Surcontrôle ou alternance de sources. |
| 5 | 2 sur 3 au-delà de $2\sigma$ (même côté) | Décalage ou instabilité temporaire. |
| 6 | 4 sur 5 au-delà de $1\sigma$ (même côté) | Décalage modéré de moyenne. |
| 7 | 15 points dans la zone C | Stratification (limites trop larges). |
| 8 | 8 points au-delà de $1\sigma$ (des deux côtés) | Mélange de distributions. |

**Recommandation pratique.** En production, il est courant de n'appliquer que les règles 1 à 4 (voire uniquement la règle 1) pour limiter les fausses alarmes. L'application de toutes les règles simultanément augmente le taux de fausses alarmes à environ 2 à 4 % par point, contre 0,27 % pour la règle 1 seule. Le choix des règles dépend du coût d'une fausse alarme par rapport au coût d'un défaut non détecté.

**Sensibilité aux décalages de moyenne.** La carte de Shewhart avec la seule règle 1 détecte un décalage de $1{,}5\sigma$ en moyenne après 6 à 7 sous-groupes (ARL $\approx 6{,}3$). L'ajout des règles complémentaires réduit l'ARL à environ 2 à 3 sous-groupes pour le même décalage. Pour une détection encore plus rapide des petits décalages, on peut utiliser des cartes CUSUM (sommes cumulées) ou EWMA (moyenne mobile pondérée exponentiellement), décrites dans l'ISO 7870-4 et ISO 7870-6 respectivement.

---

### 4.4 Table complète des constantes SPC

Le tableau suivant regroupe les constantes SPC de référence pour des sous-groupes de taille $n$ allant de 2 à 25. Ces constantes sont utilisées pour construire les cartes $\bar{x}$/R, $\bar{x}$/S et I-MR.

**Définitions des constantes :**
- $A_2$ : facteur pour les limites de la carte $\bar{x}$ à partir de $\bar{R}$.
- $A_3$ : facteur pour les limites de la carte $\bar{x}$ à partir de $\bar{S}$.
- $B_3$ : facteur pour la limite inférieure de la carte $S$.
- $B_4$ : facteur pour la limite supérieure de la carte $S$.
- $D_3$ : facteur pour la limite inférieure de la carte $R$.
- $D_4$ : facteur pour la limite supérieure de la carte $R$.
- $d_2$ : facteur de conversion étendue vers écart-type ($\hat{\sigma} = \bar{R}/d_2$).
- $c_4$ : facteur de correction de biais de l'écart-type ($\hat{\sigma} = \bar{S}/c_4$).

| $n$ | $A_2$ | $A_3$ | $B_3$ | $B_4$ | $D_3$ | $D_4$ | $d_2$ | $c_4$ |
|---|---|---|---|---|---|---|---|---|
| 2 | 1,880 | 2,659 | 0 | 3,267 | 0 | 3,267 | 1,128 | 0,7979 |
| 3 | 1,023 | 1,954 | 0 | 2,568 | 0 | 2,574 | 1,693 | 0,8862 |
| 4 | 0,729 | 1,628 | 0 | 2,266 | 0 | 2,282 | 2,059 | 0,9213 |
| 5 | 0,577 | 1,427 | 0 | 2,089 | 0 | 2,114 | 2,326 | 0,9400 |
| 6 | 0,483 | 1,287 | 0,030 | 1,970 | 0 | 2,004 | 2,534 | 0,9515 |
| 7 | 0,419 | 1,182 | 0,118 | 1,882 | 0,076 | 1,924 | 2,704 | 0,9594 |
| 8 | 0,373 | 1,099 | 0,185 | 1,815 | 0,136 | 1,864 | 2,847 | 0,9650 |
| 9 | 0,337 | 1,032 | 0,239 | 1,761 | 0,184 | 1,816 | 2,970 | 0,9693 |
| 10 | 0,308 | 0,975 | 0,284 | 1,716 | 0,223 | 1,777 | 3,078 | 0,9727 |
| 11 | 0,285 | 0,927 | 0,321 | 1,679 | 0,256 | 1,744 | 3,173 | 0,9754 |
| 12 | 0,266 | 0,886 | 0,354 | 1,646 | 0,283 | 1,717 | 3,258 | 0,9776 |
| 13 | 0,249 | 0,850 | 0,382 | 1,618 | 0,307 | 1,693 | 3,336 | 0,9794 |
| 14 | 0,235 | 0,817 | 0,406 | 1,594 | 0,328 | 1,672 | 3,407 | 0,9810 |
| 15 | 0,223 | 0,789 | 0,428 | 1,572 | 0,347 | 1,653 | 3,472 | 0,9823 |
| 16 | 0,212 | 0,763 | 0,448 | 1,552 | 0,363 | 1,637 | 3,532 | 0,9835 |
| 17 | 0,203 | 0,739 | 0,466 | 1,534 | 0,378 | 1,622 | 3,588 | 0,9845 |
| 18 | 0,194 | 0,718 | 0,482 | 1,518 | 0,391 | 1,608 | 3,640 | 0,9854 |
| 19 | 0,187 | 0,698 | 0,497 | 1,503 | 0,403 | 1,597 | 3,689 | 0,9862 |
| 20 | 0,180 | 0,680 | 0,510 | 1,490 | 0,415 | 1,585 | 3,735 | 0,9869 |
| 21 | 0,173 | 0,663 | 0,523 | 1,477 | 0,425 | 1,575 | 3,778 | 0,9876 |
| 22 | 0,167 | 0,647 | 0,534 | 1,466 | 0,434 | 1,566 | 3,819 | 0,9882 |
| 23 | 0,162 | 0,633 | 0,545 | 1,455 | 0,443 | 1,557 | 3,858 | 0,9887 |
| 24 | 0,157 | 0,619 | 0,555 | 1,445 | 0,451 | 1,548 | 3,895 | 0,9892 |
| 25 | 0,153 | 0,606 | 0,565 | 1,435 | 0,459 | 1,541 | 3,931 | 0,9896 |

**Relations fondamentales entre les constantes :**

- $A_2 = 3 / (d_2 \sqrt{n})$ : relie les limites $\bar{x}$ à l'étendue moyenne.
- $A_3 = 3 / (c_4 \sqrt{n})$ : relie les limites $\bar{x}$ à l'écart-type moyen.
- $D_3 = 1 - 3 d_3 / d_2$ et $D_4 = 1 + 3 d_3 / d_2$ : limites de la carte R ($d_3$ est l'écart-type de l'étendue relative).
- $B_3 = 1 - 3\sqrt{1 - c_4^2}/c_4$ et $B_4 = 1 + 3\sqrt{1 - c_4^2}/c_4$ : limites de la carte S.

---

## 5. Capabilité des procédés (ISO 22514)

La capabilité d'un procédé mesure son aptitude à produire des résultats conformes aux spécifications. Elle compare la dispersion naturelle du procédé à l'intervalle de tolérance spécifié.

### 5.1 ISO 22514-1 — concepts généraux

L'ISO 22514-1 définit les termes et concepts de base relatifs à la capabilité. Elle distingue :
- La **capabilité machine** : performance à court terme dans des conditions contrôlées (même opérateur, même matière, même réglage).
- La **capabilité procédé** : performance à long terme incluant toutes les sources de variation (changements d'opérateur, de matière, de réglage, etc.).

### 5.2 ISO 22514-2 — capabilité machine et procédé

#### 5.2.1 Indices de capabilité à court terme ($C_p$, $C_{pk}$)

Ces indices utilisent l'écart-type intra-groupe $\sigma$ estimé à partir des cartes de contrôle (variation à court terme, within-subgroup).

**Indice de capabilité potentielle $C_p$ :**

$$C_p = \frac{LSS - LSI}{6\sigma}$$

$C_p$ compare la largeur de la tolérance à la dispersion du procédé. Il ne tient pas compte du centrage du procédé.

**Indice de capabilité réelle $C_{pk}$ :**

$$C_{pk} = \min\left(\frac{LSS - \bar{x}}{3\sigma}, \frac{\bar{x} - LSI}{3\sigma}\right)$$

$C_{pk}$ tient compte du centrage. Si le procédé est parfaitement centré, $C_{pk} = C_p$. Sinon, $C_{pk} < C_p$.

#### 5.2.2 Indices de performance à long terme ($P_p$, $P_{pk}$)

Ces indices utilisent l'écart-type total $s$ calculé sur l'ensemble des données individuelles (variation totale, overall).

**Indice de performance potentielle $P_p$ :**

$$P_p = \frac{LSS - LSI}{6s}$$

**Indice de performance réelle $P_{pk}$ :**

$$P_{pk} = \min\left(\frac{LSS - \bar{x}}{3s}, \frac{\bar{x} - LSI}{3s}\right)$$

#### 5.2.3 Différence entre $\sigma$ (intra-groupe) et $s$ (total)

| Paramètre | Symbole | Estimation | Source de variation |
|---|---|---|---|
| Écart-type intra-groupe | $\sigma$ | $\hat{\sigma} = \bar{R}/d_2$ ou $\bar{S}/c_4$ | Variation à court terme uniquement (au sein des sous-groupes). |
| Écart-type total | $s$ | $s = \sqrt{\frac{1}{N-1}\sum(x_i - \bar{x})^2}$ | Variation totale incluant les variations entre sous-groupes. |

En général, $s \geq \sigma$, et donc $P_p \leq C_p$ et $P_{pk} \leq C_{pk}$. Un écart important entre les indices de capabilité et de performance indique la présence de sources de variation entre les sous-groupes (décalages de moyenne, effets opérateur, etc.).

<!-- IMG:capability_cp_cpk.png -->

#### 5.2.4 Interprétation des indices de capabilité

| $C_{pk}$ (ou $P_{pk}$) | Interprétation | PPM hors tolérance (une queue) | Action recommandée |
|---|---|---|---|
| $< 0{,}67$ | Très incapable | $> 22750$ | Action immédiate requise. |
| $0{,}67$ à $1{,}00$ | Incapable | $2700$ à $22750$ | Amélioration urgente. |
| $1{,}00$ à $1{,}33$ | Marginal | $63$ à $2700$ | Amélioration souhaitée. |
| $1{,}33$ à $1{,}67$ | Capable | $0{,}6$ à $63$ | Acceptable pour la plupart des applications. |
| $1{,}67$ à $2{,}00$ | Très capable | $< 0{,}6$ | Excellent. |
| $> 2{,}00$ | World class | $< 0{,}001$ | Exceptionnel (objectif Six Sigma). |

#### 5.2.5 Table des PPM en fonction de $C_{pk}$

Le tableau suivant donne le nombre de parties par million (PPM) hors tolérance pour un procédé centré et normalement distribué en fonction de $C_{pk}$ :

| $C_{pk}$ | PPM total (deux côtés) | Niveau sigma |
|---|---|---|
| 0,33 | 317310 | 1$\sigma$ |
| 0,50 | 133614 | 1,5$\sigma$ |
| 0,67 | 45500 | 2$\sigma$ |
| 0,83 | 12419 | 2,5$\sigma$ |
| 1,00 | 2700 | 3$\sigma$ |
| 1,17 | 467 | 3,5$\sigma$ |
| 1,33 | 63 | 4$\sigma$ |
| 1,50 | 6,8 | 4,5$\sigma$ |
| 1,67 | 0,57 | 5$\sigma$ |
| 2,00 | 0,002 | 6$\sigma$ |

*Note : ces valeurs supposent un procédé parfaitement centré et normalement distribué. Le décalage de 1,5$\sigma$ souvent mentionné dans l'approche Six Sigma n'est PAS pris en compte ici.*

#### 5.2.6 Exemple numérique de calcul de capabilité

Un procédé d'usinage produit des axes dont le diamètre doit être compris entre $LSI = 9{,}95$ mm et $LSS = 10{,}05$ mm ($T = 0{,}10$ mm). Sur 30 sous-groupes de taille $n = 5$, on obtient :
- $\bar{\bar{x}} = 10{,}005$ mm
- $\hat{\sigma} = \bar{R}/d_2 = 0{,}012$ mm (écart-type intra-groupe)
- $s = 0{,}015$ mm (écart-type total)

**Indices à court terme :**
- $C_p = \frac{0{,}10}{6 \times 0{,}012} = 1{,}39$
- $C_{pk} = \min\left(\frac{10{,}05 - 10{,}005}{3 \times 0{,}012}, \frac{10{,}005 - 9{,}95}{3 \times 0{,}012}\right) = \min(1{,}25 ; 1{,}53) = 1{,}25$

**Indices à long terme :**
- $P_p = \frac{0{,}10}{6 \times 0{,}015} = 1{,}11$
- $P_{pk} = \min\left(\frac{10{,}05 - 10{,}005}{3 \times 0{,}015}, \frac{10{,}005 - 9{,}95}{3 \times 0{,}015}\right) = \min(1{,}00 ; 1{,}22) = 1{,}00$

**Interprétation :** la capabilité à court terme ($C_{pk} = 1{,}25$) est proche du seuil acceptable ($1{,}33$) mais n'est pas atteinte. Le décentrage du procédé ($\bar{x} = 10{,}005$ vs cible $= 10{,}00$) réduit le $C_{pk}$ par rapport au $C_p$. La performance à long terme ($P_{pk} = 1{,}00$) est marginale. L'écart entre $C_{pk}$ et $P_{pk}$ révèle des sources de variation entre sous-groupes.

**Actions recommandées :**
1. Recentrer le procédé sur la valeur cible (réduire le biais de 0,005 mm).
2. Identifier et réduire les sources de variation entre sous-groupes.
3. Viser $C_{pk} \geq 1{,}33$ et $P_{pk} \geq 1{,}33$.

#### 5.2.7 Conditions préalables au calcul de capabilité

Avant de calculer des indices de capabilité, il faut vérifier que :
1. Le procédé est **sous contrôle statistique** (aucune cause spéciale détectée sur la carte de contrôle).
2. Les données suivent une distribution **approximativement normale** (test de normalité, section 7).
3. Le **système de mesure** est adéquat (GRR acceptable, section 6).
4. Les données sont en nombre suffisant (au moins 25 sous-groupes, ISO 22514-2, clause 6).

---

## 6. Capabilité des systèmes de mesure (ISO 22514-7)

L'ISO 22514-7 définit les méthodes d'évaluation de la capabilité des systèmes de mesure. Un système de mesure inadéquat peut masquer les véritables variations du procédé ou générer de fausses alarmes sur les cartes de contrôle.

### 6.1 Indices $C_g$ et $C_{gk}$

Les indices $C_g$ et $C_{gk}$ évaluent la capabilité du système de mesure en comparant sa répétabilité à la tolérance du produit.

**Indice $C_g$ (capabilité de la jauge) :**

$$C_g = \frac{0{,}2 \times T}{6 s_g}$$

où :
- $T = LSS - LSI$ est l'intervalle de tolérance.
- $s_g$ est l'écart-type de répétabilité (obtenu en mesurant $n$ fois la même pièce de référence avec le même opérateur, le même instrument, dans les mêmes conditions).

Le facteur $0{,}2$ signifie que l'on n'accorde au système de mesure que 20 % de la tolérance totale. Un $C_g \geq 1{,}33$ est exigé.

**Indice $C_{gk}$ (capabilité de la jauge avec biais) :**

$$C_{gk} = \frac{0{,}1 \times T - |x_m - \bar{x}|}{3 s_g}$$

où :
- $x_m$ est la valeur de référence (valeur certifiée de la pièce étalon).
- $\bar{x}$ est la moyenne des mesures répétées.
- $|x_m - \bar{x}|$ est le biais du système de mesure.

Un $C_{gk} \geq 1{,}33$ est exigé. Si $C_g$ est acceptable mais $C_{gk}$ ne l'est pas, le système présente un biais significatif qui doit être corrigé.

### 6.2 Étude GRR (Gage Repeatability and Reproducibility)

L'étude GRR décompose la variabilité totale du système de mesure en deux composantes :

**Répétabilité (EV — Equipment Variation) :** variation observée lorsque le même opérateur mesure la même pièce plusieurs fois avec le même instrument.

$$EV = \bar{R}_{opérateurs} / d_2$$

**Reproductibilité (AV — Appraiser Variation) :** variation observée entre différents opérateurs mesurant les mêmes pièces.

$$AV = \sqrt{\left(\frac{\bar{R}_{pièces \, par \, opérateur}}{d_2}\right)^2 - \frac{EV^2}{n \times r}}$$

où $n$ est le nombre de pièces et $r$ est le nombre de répétitions.

Si le terme sous la racine est négatif, $AV = 0$.

**GRR combiné :**

$$GRR = \sqrt{EV^2 + AV^2}$$

**Variation des pièces (PV — Part Variation) :**

$$PV = \frac{R_{pièces}}{d_2}$$

**Variation totale (TV — Total Variation) :**

$$TV = \sqrt{GRR^2 + PV^2}$$

**Pourcentage GRR :**

$$\%GRR = \frac{GRR}{TV} \times 100$$

#### 6.2.1 Interprétation du %GRR

| %GRR | Interprétation | Action |
|---|---|---|
| $< 10\%$ | Système de mesure acceptable. | Aucune action nécessaire. |
| $10\%$ à $30\%$ | Système marginal. | Acceptable selon l'application et le coût. |
| $> 30\%$ | Système inacceptable. | Amélioration indispensable avant utilisation. |

<!-- IMG:grr_variance_components.png -->

#### 6.2.2 Nombre de catégories distinctes (ndc)

Le nombre de catégories distinctes est un indicateur supplémentaire de la discrimination du système de mesure :

$$ndc = 1{,}41 \times \frac{PV}{GRR}$$

Le résultat est arrondi à l'entier inférieur. Un $ndc \geq 5$ est exigé pour un système de mesure acceptable. Cela signifie que le système peut distinguer au moins 5 groupes distincts parmi les pièces mesurées.

### 6.3 Procédure typique d'une étude GRR

1. Sélectionner 10 pièces couvrant la gamme de production.
2. Identifier 2 à 3 opérateurs.
3. Chaque opérateur mesure chaque pièce 2 à 3 fois (ordre aléatoire, en aveugle).
4. Calculer EV, AV, GRR, PV, TV, %GRR et ndc.
5. Conclure sur l'acceptabilité du système de mesure.

---

## 7. Tests de normalité (ISO 5479)

De nombreuses méthodes statistiques (cartes de contrôle, capabilité, intervalles de tolérance) supposent que les données suivent une distribution normale. L'ISO 5479 fournit des méthodes pour vérifier cette hypothèse.

### 7.1 Pourquoi la normalité est importante

Les conséquences d'une non-normalité non détectée peuvent être graves :
- Les **limites de contrôle** des cartes $\bar{x}$ sont relativement robustes (grâce au théorème central limite), mais les cartes R, S et I-MR sont sensibles à la non-normalité.
- Les **indices de capabilité** $C_p$ et $C_{pk}$ supposent la normalité. Sur données non normales, les PPM estimés peuvent être très éloignés de la réalité.
- Les **intervalles de tolérance** paramétriques de l'ISO 16269-6 supposent la normalité.

### 7.2 Test de Shapiro-Wilk

Le test de Shapiro-Wilk est considéré comme le test de normalité le plus puissant pour les petits échantillons ($n < 50$, bien qu'il puisse être étendu jusqu'à $n = 5000$).

**Hypothèses :**
- $H_0$ : les données proviennent d'une distribution normale.
- $H_1$ : les données ne proviennent pas d'une distribution normale.

**Statistique de test $W$ :**

$$W = \frac{\left(\sum_{i=1}^{m} a_i (x_{(n+1-i)} - x_{(i)})\right)^2}{\sum_{i=1}^{n}(x_i - \bar{x})^2}$$

où $x_{(i)}$ sont les statistiques d'ordre (données triées), $a_i$ sont des coefficients tabulés qui dépendent de $n$, et $m = n/2$ (arrondi à l'entier inférieur).

**Interprétation :** $W$ varie entre 0 et 1. Plus $W$ est proche de 1, plus l'hypothèse de normalité est soutenue. On rejette $H_0$ si $W < W_{critique}$ (ou si la $p$-value $< \alpha$, typiquement $\alpha = 0{,}05$).

**Limites :** le test de Shapiro-Wilk est très puissant mais peut rejeter la normalité pour des écarts mineurs sur de grands échantillons. Il est recommandé de combiner le résultat du test avec une analyse graphique (Q-Q plot).

### 7.3 Test d'Anderson-Darling

Le test d'Anderson-Darling est particulièrement sensible aux écarts dans les queues de distribution, ce qui est pertinent pour les calculs de capabilité et de PPM.

**Statistique de test $A^2$ :**

$$A^2 = -n - \frac{1}{n}\sum_{i=1}^{n}(2i - 1)\left[\ln(F(x_{(i)})) + \ln(1 - F(x_{(n+1-i)}))\right]$$

où $F$ est la fonction de répartition de la loi normale standard et $x_{(i)}$ sont les données standardisées triées.

**Statistique corrigée :**

$$A^{*2} = A^2 \left(1 + \frac{0{,}75}{n} + \frac{2{,}25}{n^2}\right)$$

**Interprétation :** on rejette $H_0$ si $A^{*2}$ dépasse la valeur critique. Pour un niveau de signification $\alpha = 0{,}05$, la valeur critique est approximativement $0{,}752$.

| Niveau $\alpha$ | Valeur critique $A^{*2}$ |
|---|---|
| 0,15 | 0,576 |
| 0,10 | 0,656 |
| 0,05 | 0,752 |
| 0,025 | 0,873 |
| 0,01 | 1,035 |

### 7.4 Test de Kolmogorov-Smirnov

Le test de Kolmogorov-Smirnov (KS) compare la fonction de répartition empirique $F_n(x)$ à la fonction de répartition théorique $F_0(x)$ de la loi normale.

**Statistique de test $D$ :**

$$D = \max_{i} \left| F_n(x_{(i)}) - F_0(x_{(i)}) \right|$$

où $F_n(x_{(i)}) = i/n$ est la fréquence cumulée empirique.

**Valeurs critiques (test de Lilliefors pour normalité avec paramètres estimés) :**

| $n$ | $\alpha = 0{,}20$ | $\alpha = 0{,}15$ | $\alpha = 0{,}10$ | $\alpha = 0{,}05$ | $\alpha = 0{,}01$ |
|---|---|---|---|---|---|
| 5 | 0,289 | 0,303 | 0,319 | 0,337 | 0,405 |
| 10 | 0,214 | 0,224 | 0,239 | 0,258 | 0,294 |
| 15 | 0,178 | 0,187 | 0,201 | 0,220 | 0,257 |
| 20 | 0,155 | 0,164 | 0,178 | 0,195 | 0,231 |
| 25 | 0,140 | 0,148 | 0,162 | 0,177 | 0,211 |
| 30 | 0,128 | 0,136 | 0,149 | 0,163 | 0,196 |
| 50 | 0,100 | 0,106 | 0,117 | 0,130 | 0,157 |
| 100 | 0,071 | 0,076 | 0,084 | 0,093 | 0,114 |

*Note : lorsque les paramètres $\mu$ et $\sigma$ sont estimés à partir des données, il faut utiliser les tables de Lilliefors (et non les tables KS classiques).*

### 7.5 Diagramme Q-Q (quantile-quantile)

Le diagramme Q-Q est un outil graphique qui compare les quantiles observés aux quantiles théoriques de la loi normale. Si les données sont normales, les points s'alignent approximativement sur une droite.

**Construction :**
1. Trier les données : $x_{(1)} \leq x_{(2)} \leq \ldots \leq x_{(n)}$.
2. Calculer les fréquences cumulées : $p_i = (i - 0{,}375) / (n + 0{,}25)$ (formule de Blom).
3. Calculer les quantiles théoriques : $z_i = \Phi^{-1}(p_i)$.
4. Tracer $x_{(i)}$ en ordonnée contre $z_i$ en abscisse.

**Interprétation des motifs :**
- Alignement linéaire : normalité confirmée.
- Courbure en S : asymétrie (skewness).
- Extrémités déviantes : queues lourdes (kurtosis) ou valeurs aberrantes.
- Points étagés : données discrètes ou arrondies.

<!-- IMG:qqplot_comparison.png -->

### 7.6 Tableau comparatif des tests de normalité

| Test | Taille d'échantillon | Sensibilité principale | Puissance globale | Usage recommandé |
|---|---|---|---|---|
| Shapiro-Wilk | $3 \leq n \leq 5000$ | Centre et queues. | Très élevée. | Test de référence pour $n < 50$. |
| Anderson-Darling | $n \geq 8$ | Queues de distribution. | Élevée. | Complément pour les calculs de PPM. |
| Kolmogorov-Smirnov (Lilliefors) | $n \geq 5$ | Centre de distribution. | Modérée. | Quand les autres tests ne sont pas disponibles. |
| Q-Q plot | Tout $n$ | Diagnostic visuel global. | — | Toujours en complément d'un test formel. |

**Recommandation pratique.** Utiliser le test de Shapiro-Wilk comme test principal, complété par le diagramme Q-Q pour l'interprétation visuelle. Pour les applications où les queues de distribution sont critiques (calcul de PPM, capabilité), ajouter le test d'Anderson-Darling.

---

## 8. Comparaison de populations — tests et ANOVA (ISO 5725, ASTM E691)

En qualité industrielle, il est fréquent de devoir comparer des populations : deux machines produisent-elles des pièces de même dimension moyenne ? Trois opérateurs obtiennent-ils la même dispersion de mesure ? Un changement de fournisseur a-t-il modifié la performance du procédé ? Cette section couvre les principaux tests paramétriques et non paramétriques de comparaison, ainsi que l'analyse de la variance (ANOVA).

### 8.1 Comparaison de deux moyennes — test de Student

Le test de Student (ou test $t$) est le test de base pour comparer des moyennes. Il existe en trois variantes selon la structure des données.

#### 8.1.1 Test de Student pour un échantillon (one-sample t-test)

On compare la moyenne $\bar{x}$ d'un échantillon de taille $n$ à une valeur de référence $\mu_0$ connue (par exemple, la valeur nominale d'une spécification).

**Hypothèses :**
- $H_0$ : $\mu = \mu_0$ (la moyenne du procédé est égale à la référence).
- $H_1$ : $\mu \neq \mu_0$ (test bilatéral) ou $\mu > \mu_0$ / $\mu < \mu_0$ (test unilatéral).

**Statistique de test :**

$$t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}$$

avec $\nu = n - 1$ degrés de liberté.

**Règle de décision (test bilatéral) :** rejeter $H_0$ si $|t| > t_{\alpha/2, \, n-1}$.

**Conditions d'application :**
- L'échantillon est prélevé aléatoirement.
- La population suit une distribution approximativement normale (vérifier avec les tests de la section 7).
- Pour $n \geq 30$, le test est robuste aux écarts modérés par rapport à la normalité (théorème central limite).

**Exemple industriel.** Un procédé d'usinage vise un diamètre nominal $\mu_0 = 10{,}000$ mm. On prélève $n = 12$ pièces et on mesure $\bar{x} = 10{,}015$ mm, $s = 0{,}022$ mm. La statistique est $t = (10{,}015 - 10{,}000) / (0{,}022 / \sqrt{12}) = 2{,}362$. La valeur critique pour $\alpha = 0{,}05$ bilatéral et $\nu = 11$ est $t_{0{,}025, 11} = 2{,}201$. Comme $|t| = 2{,}362 > 2{,}201$, on rejette $H_0$ : le procédé est significativement décentré.

#### 8.1.2 Test de Student pour deux échantillons indépendants (two-sample t-test)

On compare les moyennes de deux échantillons indépendants, par exemple les productions de deux machines.

**Cas 1 : variances égales (pooled t-test).**

On suppose $\sigma_1^2 = \sigma_2^2$ (hypothèse vérifiable par le test de Fisher, section 8.2).

$$t = \frac{\bar{x}_1 - \bar{x}_2}{s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}$$

où $s_p$ est l'écart-type poolé :

$$s_p = \sqrt{\frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}}$$

Les degrés de liberté sont $\nu = n_1 + n_2 - 2$.

**Cas 2 : variances inégales (test de Welch).**

Lorsque l'hypothèse d'égalité des variances est rejetée, on utilise le test de Welch :

$$t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}$$

Les degrés de liberté effectifs sont estimés par la formule de Welch-Satterthwaite :

$$\nu_{eff} = \frac{\left(\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}\right)^2}{\frac{(s_1^2/n_1)^2}{n_1 - 1} + \frac{(s_2^2/n_2)^2}{n_2 - 1}}$$

Le résultat est arrondi à l'entier inférieur.

**Recommandation pratique.** En cas de doute sur l'égalité des variances, utiliser systématiquement le test de Welch, qui est plus conservateur mais toujours valide.

#### 8.1.3 Test de Student apparié (paired t-test)

On compare deux mesures effectuées sur les mêmes unités : avant/après traitement, même pièce mesurée par deux instruments, etc.

**Principe.** On calcule les différences $d_i = x_{1i} - x_{2i}$ pour chaque paire, puis on applique un test à un échantillon sur les $d_i$.

$$t = \frac{\bar{d}}{s_d / \sqrt{n}}$$

avec $\bar{d} = \frac{1}{n}\sum_{i=1}^{n} d_i$ et $s_d = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(d_i - \bar{d})^2}$, et $\nu = n - 1$.

**Conditions d'application :**
- Les paires sont naturellement appariées (même pièce, même lot, même opérateur).
- Les différences $d_i$ suivent une distribution approximativement normale.

**Applications typiques en qualité :**
- Comparer un ancien et un nouveau moyen de mesure sur les mêmes pièces.
- Évaluer l'effet d'un traitement de surface avant/après.
- Vérifier la dérive d'un instrument entre deux étalonnages sur les mêmes étalons.

### 8.2 Comparaison de deux variances — test de Fisher (F-test)

Le test de Fisher compare les variances de deux populations normales indépendantes. Il est souvent utilisé comme prérequis au test de Student à deux échantillons (pour décider entre le pooled t-test et le test de Welch).

**Hypothèses :**
- $H_0$ : $\sigma_1^2 = \sigma_2^2$ (les deux populations ont la même variance).
- $H_1$ : $\sigma_1^2 \neq \sigma_2^2$ (test bilatéral).

**Statistique de test :**

$$F = \frac{s_1^2}{s_2^2}$$

avec par convention $s_1^2 \geq s_2^2$ pour que $F \geq 1$.

Les degrés de liberté sont $\nu_1 = n_1 - 1$ (numérateur) et $\nu_2 = n_2 - 1$ (dénominateur).

**Règle de décision (test bilatéral) :** rejeter $H_0$ si $F > F_{\alpha/2, \, \nu_1, \, \nu_2}$.

**Valeurs critiques du test de Fisher ($\alpha = 0{,}05$, bilatéral, soit $\alpha/2 = 0{,}025$ par queue) :**

| $\nu_1 \backslash \nu_2$ | 5 | 10 | 15 | 20 | 30 | 60 |
|---|---|---|---|---|---|---|
| 5 | 7,15 | 4,24 | 3,58 | 3,29 | 3,03 | 2,79 |
| 10 | 4,24 | 3,15 | 2,72 | 2,52 | 2,33 | 2,16 |
| 15 | 3,58 | 2,72 | 2,40 | 2,23 | 2,07 | 1,92 |
| 20 | 3,29 | 2,52 | 2,23 | 2,08 | 1,93 | 1,79 |
| 30 | 3,03 | 2,33 | 2,07 | 1,93 | 1,79 | 1,65 |
| 60 | 2,79 | 2,16 | 1,92 | 1,79 | 1,65 | 1,53 |

**Limites du test de Fisher.** Le test de Fisher est très sensible à la non-normalité des données. Pour des données non normales, on préfère le test de Levene (section 8.6). Pour comparer les variances de $k > 2$ groupes, on utilise le test de Bartlett ou le test de Levene.

### 8.3 ANOVA à un facteur (one-way ANOVA)

L'analyse de la variance (ANOVA) à un facteur permet de comparer les moyennes de $k \geq 3$ groupes simultanément. C'est la généralisation du test de Student à deux échantillons.

**Pourquoi ne pas faire des tests de Student multiples ?** Si l'on compare $k = 4$ groupes deux à deux, on effectue $\binom{4}{2} = 6$ tests. Avec $\alpha = 0{,}05$ par test, le risque global de conclure à tort qu'au moins une paire diffère atteint $1 - (1 - 0{,}05)^6 \approx 26\%$. L'ANOVA contrôle le risque $\alpha$ global.

**Hypothèses :**
- $H_0$ : $\mu_1 = \mu_2 = \cdots = \mu_k$ (toutes les moyennes de groupe sont égales).
- $H_1$ : au moins une moyenne diffère.

#### 8.3.1 Décomposition de la variabilité

La variabilité totale est décomposée en deux sources : la variabilité inter-groupes (Between, due au facteur) et la variabilité intra-groupe (Within, résiduelle).

$$SS_T = SS_B + SS_W$$

**Somme des carrés totale :**

$$SS_T = \sum_{j=1}^{k}\sum_{i=1}^{n_j}(x_{ij} - \bar{\bar{x}})^2$$

où $\bar{\bar{x}}$ est la moyenne générale de toutes les observations.

**Somme des carrés inter-groupes (Between) :**

$$SS_B = \sum_{j=1}^{k} n_j (\bar{x}_j - \bar{\bar{x}})^2$$

où $\bar{x}_j$ est la moyenne du groupe $j$ et $n_j$ est l'effectif du groupe $j$.

**Somme des carrés intra-groupe (Within) :**

$$SS_W = \sum_{j=1}^{k}\sum_{i=1}^{n_j}(x_{ij} - \bar{x}_j)^2$$

#### 8.3.2 Table ANOVA

| Source | Somme des carrés | Degrés de liberté | Carré moyen | F |
|---|---|---|---|---|
| Inter-groupes (Between) | $SS_B$ | $k - 1$ | $MS_B = SS_B / (k - 1)$ | $F = MS_B / MS_W$ |
| Intra-groupe (Within) | $SS_W$ | $N - k$ | $MS_W = SS_W / (N - k)$ | — |
| Total | $SS_T$ | $N - 1$ | — | — |

où $N = \sum_{j=1}^{k} n_j$ est le nombre total d'observations.

**Règle de décision :** rejeter $H_0$ si $F > F_{\alpha, \, k-1, \, N-k}$.

#### 8.3.3 Conditions d'application

1. **Indépendance** : les observations sont indépendantes entre elles et entre les groupes.
2. **Normalité** : les données au sein de chaque groupe suivent une distribution approximativement normale (vérifier avec la section 7).
3. **Homogénéité des variances** (homoscédasticité) : les variances des $k$ groupes sont égales ($\sigma_1^2 = \sigma_2^2 = \cdots = \sigma_k^2$). Vérifier avec le test de Bartlett ou de Levene (section 8.6).

Si la condition d'homogénéité est violée, on utilise l'ANOVA de Welch comme alternative robuste.

#### 8.3.4 Exemple numérique — comparaison de 3 machines

Trois machines produisent des axes dont on mesure le diamètre (en mm). On prélève $n = 5$ pièces par machine.

| Machine A | Machine B | Machine C |
|---|---|---|
| 10,02 | 10,05 | 9,98 |
| 10,01 | 10,03 | 10,00 |
| 10,03 | 10,06 | 9,97 |
| 10,00 | 10,04 | 9,99 |
| 10,04 | 10,07 | 10,01 |

**Calculs :**
- $\bar{x}_A = 10{,}020$, $\bar{x}_B = 10{,}050$, $\bar{x}_C = 9{,}990$.
- $\bar{\bar{x}} = (10{,}020 + 10{,}050 + 9{,}990) / 3 = 10{,}020$.
- $SS_B = 5 \times [(10{,}020 - 10{,}020)^2 + (10{,}050 - 10{,}020)^2 + (9{,}990 - 10{,}020)^2] = 5 \times [0 + 0{,}0009 + 0{,}0009] = 0{,}0090$.
- $SS_W = \sum (x_{ij} - \bar{x}_j)^2 = 0{,}0010 + 0{,}0010 + 0{,}0010 = 0{,}0030$ (sommes des carrés des écarts intra-groupe).
- $MS_B = 0{,}0090 / 2 = 0{,}0045$.
- $MS_W = 0{,}0030 / 12 = 0{,}000\,25$.
- $F = 0{,}0045 / 0{,}000\,25 = 18{,}0$.

**Table ANOVA de l'exemple :**

| Source | SS | df | MS | F |
|---|---|---|---|---|
| Between | 0,0090 | 2 | 0,0045 | 18,0 |
| Within | 0,0030 | 12 | 0,000 25 | — |
| Total | 0,0120 | 14 | — | — |

La valeur critique pour $\alpha = 0{,}05$, $\nu_1 = 2$, $\nu_2 = 12$ est $F_{0{,}05, 2, 12} = 3{,}89$. Comme $F = 18{,}0 \gg 3{,}89$, on rejette $H_0$ : les trois machines ne produisent pas le même diamètre moyen. Un test post-hoc (section 8.5) permettra d'identifier quelles machines diffèrent.

<!-- IMG:anova_boxplot.png -->

### 8.4 ANOVA à deux facteurs (two-way ANOVA)

L'ANOVA à deux facteurs étudie l'effet simultané de deux facteurs (par exemple, machine et opérateur) sur une variable de réponse. Elle permet en outre de détecter une interaction entre les deux facteurs.

#### 8.4.1 Modèle avec interaction

Le modèle s'écrit :

$$x_{ijk} = \mu + \alpha_i + \beta_j + (\alpha\beta)_{ij} + \varepsilon_{ijk}$$

où $\alpha_i$ est l'effet du niveau $i$ du facteur A, $\beta_j$ est l'effet du niveau $j$ du facteur B, $(\alpha\beta)_{ij}$ est l'effet d'interaction, et $\varepsilon_{ijk}$ est l'erreur résiduelle.

#### 8.4.2 Décomposition de la variabilité

$$SS_T = SS_A + SS_B + SS_{AB} + SS_E$$

| Source | Somme des carrés | Degrés de liberté | Carré moyen | F |
|---|---|---|---|---|
| Facteur A | $SS_A$ | $a - 1$ | $MS_A = SS_A / (a - 1)$ | $F_A = MS_A / MS_E$ |
| Facteur B | $SS_B$ | $b - 1$ | $MS_B = SS_B / (b - 1)$ | $F_B = MS_B / MS_E$ |
| Interaction A$\times$B | $SS_{AB}$ | $(a-1)(b-1)$ | $MS_{AB} = SS_{AB} / [(a-1)(b-1)]$ | $F_{AB} = MS_{AB} / MS_E$ |
| Erreur (résiduelle) | $SS_E$ | $ab(r-1)$ | $MS_E = SS_E / [ab(r-1)]$ | — |
| Total | $SS_T$ | $abr - 1$ | — | — |

où $a$ est le nombre de niveaux du facteur A, $b$ le nombre de niveaux du facteur B, et $r$ le nombre de réplicats par cellule.

#### 8.4.3 Interprétation de l'interaction

Si l'interaction A$\times$B est significative ($F_{AB} > F_{critique}$), les effets principaux de A et B doivent être interprétés avec prudence : l'effet d'un facteur dépend du niveau de l'autre. Dans ce cas, on analyse les effets simples (simple effects) plutôt que les effets principaux.

**Lien avec l'ISO 5725.** L'étude de répétabilité et reproductibilité (R&R) de l'ISO 5725 peut être formulée comme une ANOVA à deux facteurs, avec l'opérateur comme facteur A et la pièce (ou le laboratoire) comme facteur B. La variance de répétabilité correspond à $MS_E$ et la variance de reproductibilité est estimée à partir de $MS_A$.

### 8.5 Tests post-hoc — comparaisons multiples

Lorsque l'ANOVA rejette $H_0$, elle indique qu'au moins une moyenne diffère, mais ne précise pas laquelle. Les tests post-hoc (ou comparaisons multiples) identifient les paires de groupes qui diffèrent significativement.

#### 8.5.1 Test de Tukey HSD (Honestly Significant Difference)

Le test de Tukey est le plus courant pour les comparaisons par paires lorsque les effectifs sont égaux.

$$HSD = q_{\alpha, k, N-k} \sqrt{\frac{MS_W}{n}}$$

où $q_{\alpha, k, N-k}$ est la valeur critique de la distribution de la range studentisée, $k$ est le nombre de groupes, $N - k$ les degrés de liberté résiduels, et $n$ l'effectif par groupe (groupes de taille égale).

**Règle de décision :** deux moyennes $\bar{x}_i$ et $\bar{x}_j$ diffèrent significativement si $|\bar{x}_i - \bar{x}_j| > HSD$.

**Valeurs critiques $q_{0{,}05, k, \nu}$ (extrait) :**

| $\nu \backslash k$ | 3 | 4 | 5 | 6 |
|---|---|---|---|---|
| 10 | 3,88 | 4,33 | 4,65 | 4,91 |
| 12 | 3,77 | 4,20 | 4,51 | 4,75 |
| 15 | 3,67 | 4,08 | 4,37 | 4,60 |
| 20 | 3,58 | 3,96 | 4,23 | 4,45 |
| 30 | 3,49 | 3,85 | 4,10 | 4,30 |
| 60 | 3,40 | 3,74 | 3,98 | 4,16 |

**Application à l'exemple de la section 8.3.4.** Avec $k = 3$, $\nu = 12$, $n = 5$ et $MS_W = 0{,}000\,25$, on lit $q_{0{,}05, 3, 12} = 3{,}77$. Le HSD vaut $3{,}77 \times \sqrt{0{,}000\,25 / 5} = 3{,}77 \times 0{,}00707 = 0{,}0267$ mm. Les différences de moyennes sont $|\bar{x}_A - \bar{x}_B| = 0{,}030$, $|\bar{x}_A - \bar{x}_C| = 0{,}030$, $|\bar{x}_B - \bar{x}_C| = 0{,}060$. Toutes les différences dépassent le HSD : les trois machines sont significativement différentes deux à deux.

#### 8.5.2 Correction de Bonferroni

La correction de Bonferroni est une méthode générale applicable à tout type de comparaisons multiples. Elle ajuste le seuil de signification :

$$\alpha_{adj} = \frac{\alpha}{m}$$

où $m$ est le nombre de comparaisons. Pour $k$ groupes, $m = k(k-1)/2$.

Cette correction est plus conservatrice que le test de Tukey (elle rejette moins souvent), mais elle est applicable même avec des effectifs inégaux ou des comparaisons planifiées.

#### 8.5.3 Tableau comparatif des méthodes post-hoc

| Méthode | Usage principal | Avantage | Inconvénient |
|---|---|---|---|
| Tukey HSD | Toutes les comparaisons par paires, effectifs égaux. | Contrôle exact du risque $\alpha$ familywise. | Nécessite des effectifs égaux (sinon Tukey-Kramer). |
| Bonferroni | Toute situation, petit nombre de comparaisons. | Simple, applicable partout. | Trop conservatrice si $m$ est grand. |
| Scheffé | Contrastes quelconques (pas seulement par paires). | Flexibilité maximale. | La plus conservatrice pour les paires. |
| Dunnett | Comparer chaque groupe à un témoin unique. | Plus puissant que Tukey pour ce cas. | Limité à la comparaison avec un témoin. |

### 8.6 Tests d'homogénéité des variances

L'homogénéité des variances (homoscédasticité) est un prérequis pour l'ANOVA classique et pour le pooled t-test. Deux tests principaux permettent de la vérifier.

#### 8.6.1 Test de Bartlett

Le test de Bartlett est le test classique d'homogénéité des variances pour $k$ groupes.

**Hypothèses :**
- $H_0$ : $\sigma_1^2 = \sigma_2^2 = \cdots = \sigma_k^2$.
- $H_1$ : au moins une variance diffère.

**Statistique de test :**

$$\chi^2 = \frac{(N - k) \ln(s_p^2) - \sum_{j=1}^{k}(n_j - 1)\ln(s_j^2)}{1 + \frac{1}{3(k-1)}\left(\sum_{j=1}^{k}\frac{1}{n_j - 1} - \frac{1}{N - k}\right)}$$

où $s_p^2 = \frac{\sum_{j=1}^{k}(n_j - 1)s_j^2}{N - k}$ est la variance poolée.

On compare $\chi^2$ à la valeur critique $\chi^2_{\alpha, k-1}$.

**Limite.** Le test de Bartlett est très sensible à la non-normalité : des écarts à la normalité peuvent conduire à rejeter $H_0$ alors que les variances sont égales.

#### 8.6.2 Test de Levene

Le test de Levene est une alternative robuste au test de Bartlett, moins sensible à la non-normalité.

**Principe.** On remplace chaque observation par son écart absolu à la médiane du groupe :

$$z_{ij} = |x_{ij} - \tilde{x}_j|$$

où $\tilde{x}_j$ est la médiane du groupe $j$. Puis on effectue une ANOVA à un facteur sur les $z_{ij}$.

**Avantage.** L'utilisation de la médiane (plutôt que la moyenne) rend le test robuste aux données non normales et aux valeurs aberrantes.

**Recommandation pratique.** En routine industrielle, préférer le test de Levene au test de Bartlett, sauf si la normalité des données est bien établie.

### 8.7 Alternative non paramétrique — test de Kruskal-Wallis

Lorsque l'hypothèse de normalité n'est pas vérifiée (et ne peut pas être obtenue par transformation), on utilise le test de Kruskal-Wallis comme alternative non paramétrique à l'ANOVA à un facteur.

**Principe.** Les $N$ observations sont classées par rang (de 1 à $N$) indépendamment de leur groupe d'appartenance. La statistique de test compare les rangs moyens des groupes.

**Statistique de test :**

$$H = \frac{12}{N(N+1)} \sum_{j=1}^{k} \frac{R_j^2}{n_j} - 3(N+1)$$

où $R_j$ est la somme des rangs du groupe $j$ et $n_j$ est l'effectif du groupe $j$.

**Distribution.** Sous $H_0$, la statistique $H$ suit approximativement une distribution du $\chi^2$ à $k - 1$ degrés de liberté (pour $n_j \geq 5$).

**Règle de décision :** rejeter $H_0$ si $H > \chi^2_{\alpha, k-1}$.

**Quand utiliser le Kruskal-Wallis plutôt que l'ANOVA :**
- Les données ne suivent pas une distribution normale et ne peuvent pas être transformées.
- Les données sont ordinales plutôt que continues.
- Les échantillons sont petits et la normalité ne peut pas être vérifiée.
- En présence de valeurs aberrantes qui affecteraient l'ANOVA.

Si le test de Kruskal-Wallis est significatif, on peut utiliser le test de Dunn comme test post-hoc pour identifier les paires de groupes qui diffèrent.

### 8.8 Applications industrielles — ISO 5725 et ASTM E691

Les tests de comparaison décrits dans cette section sont au coeur de deux normes majeures : l'ISO 5725 (exactitude des résultats de mesure) et l'ASTM E691 (études interlaboratoires).

#### 8.8.1 ISO 5725 — exactitude (justesse et fidélité)

L'ISO 5725 décompose l'exactitude (accuracy) en deux composantes :
- **Justesse** (trueness) : proximité de la moyenne des résultats à la valeur de référence. Mesurée par le biais.
- **Fidélité** (precision) : proximité des résultats entre eux. Mesurée par l'écart-type de répétabilité $s_r$ et l'écart-type de reproductibilité $s_R$.

**Répétabilité ($r$).** Conditions de répétabilité : même opérateur, même instrument, même laboratoire, court intervalle de temps. La limite de répétabilité est $r = 2{,}8 \times s_r$. Deux résultats obtenus en conditions de répétabilité ne devraient pas différer de plus de $r$ dans 95 % des cas.

**Reproductibilité ($R$).** Conditions de reproductibilité : opérateurs différents, instruments différents, laboratoires différents. La limite de reproductibilité est $R = 2{,}8 \times s_R$.

La variance de reproductibilité inclut la variance de répétabilité :

$$s_R^2 = s_r^2 + s_L^2$$

où $s_L^2$ est la variance inter-laboratoires, estimée par une ANOVA emboîtée (nested ANOVA).

#### 8.8.2 ASTM E691 — études interlaboratoires

L'ASTM E691 fournit une procédure pour organiser et analyser une étude interlaboratoire (collaborative study). Elle utilise deux statistiques de consistance introduites par Mandel :

**Statistique $h$ de Mandel (consistance inter-laboratoires) :**

$$h_j = \frac{\bar{x}_j - \bar{\bar{x}}}{s_{\bar{x}}}$$

où $\bar{x}_j$ est la moyenne du laboratoire $j$, $\bar{\bar{x}}$ est la moyenne de tous les laboratoires, et $s_{\bar{x}}$ est l'écart-type des moyennes de laboratoires. La statistique $h$ détecte les biais systématiques d'un laboratoire.

**Statistique $k$ de Mandel (consistance intra-laboratoire) :**

$$k_j = \frac{s_j}{s_r}$$

où $s_j$ est l'écart-type du laboratoire $j$ et $s_r$ est l'écart-type de répétabilité moyen. La statistique $k$ détecte les laboratoires dont la dispersion est anormalement élevée ou faible.

Les valeurs critiques de $h$ et $k$ sont données dans les tables de l'ASTM E691. Un laboratoire dont $|h|$ ou $k$ dépasse la valeur critique doit être examiné pour identifier les causes de l'écart.

#### 8.8.3 Exemple pratique — comparaison de 3 instruments de mesure

Trois instruments mesurent la même cote sur $n = 10$ pièces de référence.

| Instrument | $\bar{x}$ (mm) | $s$ (mm) |
|---|---|---|
| Instrument 1 | 25,012 | 0,008 |
| Instrument 2 | 25,018 | 0,011 |
| Instrument 3 | 25,010 | 0,009 |

**Analyse.** Une ANOVA à un facteur sur les mesures individuelles permet de tester si les trois instruments donnent la même moyenne. Le test de Bartlett ou de Levene vérifie si les dispersions sont homogènes. Si l'ANOVA est significative, un test de Tukey identifie quels instruments diffèrent. Enfin, les statistiques $h$ et $k$ de Mandel caractérisent la consistance de chaque instrument par rapport à l'ensemble.

### 8.9 Tableau récapitulatif des tests de comparaison

| Objectif | Test | Conditions | Alternative non paramétrique |
|---|---|---|---|
| Comparer une moyenne à une référence. | Student 1 échantillon. | Normalité. | Wilcoxon signé. |
| Comparer 2 moyennes indépendantes. | Student 2 échantillons. | Normalité, égalité des variances (ou Welch). | Mann-Whitney U. |
| Comparer 2 moyennes appariées. | Student apparié. | Normalité des différences. | Wilcoxon signé (apparié). |
| Comparer 2 variances. | Fisher F. | Normalité. | Ansari-Bradley. |
| Comparer $k \geq 3$ moyennes. | ANOVA à 1 facteur. | Normalité, homogénéité des variances. | Kruskal-Wallis. |
| Comparer $k$ moyennes (2 facteurs). | ANOVA à 2 facteurs. | Normalité, homogénéité. | Friedman (mesures répétées). |
| Comparer $k$ variances. | Bartlett / Levene. | Bartlett : normalité ; Levene : robuste. | — |

---

## 9. Détection des valeurs aberrantes (ISO 16269-4)

Les valeurs aberrantes (outliers) sont des observations qui s'écartent significativement du reste des données. Elles peuvent provenir d'erreurs de mesure, d'erreurs de transcription, de causes spéciales ou d'une contamination de l'échantillon. L'ISO 16269-4 fournit des tests statistiques pour les détecter.

### 9.1 Test de Grubbs

Le test de Grubbs est le test le plus utilisé pour détecter une valeur aberrante unique dans un échantillon supposé normalement distribué.

**Hypothèses :**
- $H_0$ : il n'y a pas de valeur aberrante.
- $H_1$ : la valeur la plus extrême est une valeur aberrante.

**Statistique de test :**

$$G = \frac{\max_i |x_i - \bar{x}|}{s}$$

où $\bar{x}$ est la moyenne et $s$ est l'écart-type de l'échantillon.

**Variantes :**
- Test unilatéral supérieur : $G = (x_{(n)} - \bar{x}) / s$
- Test unilatéral inférieur : $G = (\bar{x} - x_{(1)}) / s$
- Test bilatéral : $G = \max(x_{(n)} - \bar{x}, \bar{x} - x_{(1)}) / s$

**Valeurs critiques du test de Grubbs (bilatéral, $\alpha = 0{,}05$) :**

| $n$ | $G_{critique}$ |
|---|---|
| 3 | 1,155 |
| 4 | 1,481 |
| 5 | 1,715 |
| 6 | 1,887 |
| 7 | 2,020 |
| 8 | 2,126 |
| 9 | 2,215 |
| 10 | 2,290 |
| 12 | 2,412 |
| 15 | 2,549 |
| 20 | 2,709 |
| 25 | 2,822 |
| 30 | 2,908 |
| 40 | 3,036 |
| 50 | 3,128 |
| 60 | 3,199 |
| 80 | 3,305 |
| 100 | 3,383 |

On rejette $H_0$ si $G > G_{critique}$. Si une valeur aberrante est détectée et retirée, le test peut être répété sur le jeu de données réduit.

### 9.2 Test de Dixon

Le test de Dixon est une alternative non paramétrique au test de Grubbs, particulièrement adaptée aux petits échantillons ($3 \leq n \leq 25$). Il utilise des rapports basés sur les statistiques d'ordre (données triées).

**Statistiques de test selon la taille de l'échantillon :**

| Taille $n$ | Statistique | Formule (test de la plus grande valeur) |
|---|---|---|
| 3 à 7 | $r_{10}$ | $(x_{(n)} - x_{(n-1)}) / (x_{(n)} - x_{(1)})$ |
| 8 à 10 | $r_{11}$ | $(x_{(n)} - x_{(n-1)}) / (x_{(n)} - x_{(2)})$ |
| 11 à 13 | $r_{21}$ | $(x_{(n)} - x_{(n-2)}) / (x_{(n)} - x_{(2)})$ |
| 14 à 25 | $r_{22}$ | $(x_{(n)} - x_{(n-2)}) / (x_{(n)} - x_{(3)})$ |

Pour tester la plus petite valeur, on inverse les indices.

**Valeurs critiques du test de Dixon ($\alpha = 0{,}05$, test unilatéral) :**

| $n$ | $r_{10}$ | $r_{11}$ | $r_{21}$ | $r_{22}$ |
|---|---|---|---|---|
| 3 | 0,941 | — | — | — |
| 4 | 0,765 | — | — | — |
| 5 | 0,642 | — | — | — |
| 6 | 0,560 | — | — | — |
| 7 | 0,507 | — | — | — |
| 8 | — | 0,554 | — | — |
| 9 | — | 0,512 | — | — |
| 10 | — | 0,477 | — | — |
| 11 | — | — | 0,576 | — |
| 12 | — | — | 0,546 | — |
| 13 | — | — | 0,521 | — |
| 14 | — | — | — | 0,546 |
| 15 | — | — | — | 0,525 |
| 20 | — | — | — | 0,450 |
| 25 | — | — | — | 0,406 |

*Le symbole « — » indique que la statistique correspondante n'est pas utilisée pour cette taille d'échantillon.*

### 9.3 Comparaison des tests de Grubbs et Dixon

| Critère | Grubbs | Dixon |
|---|---|---|
| Hypothèse de normalité | Oui (requis). | Moins sensible à la non-normalité. |
| Taille d'échantillon | $n \geq 3$, idéal pour $n \geq 7$. | $3 \leq n \leq 25$. |
| Puissance | Plus élevée pour les échantillons de taille moyenne et grande. | Plus élevée pour les très petits échantillons. |
| Outliers multiples | Sensible au masquage (un outlier peut masquer un autre). | Moins sensible au masquage. |
| Calcul | Nécessite $\bar{x}$ et $s$. | Basé uniquement sur les statistiques d'ordre. |

**Recommandation pratique :** pour $n < 10$, privilégier Dixon. Pour $n \geq 10$, privilégier Grubbs. Dans tous les cas, une analyse graphique (boîte à moustaches, Q-Q plot) doit accompagner le test formel.

---

## 10. Intervalles de tolérance statistiques (ISO 16269-6)

Un intervalle de tolérance statistique est un intervalle estimé à partir d'un échantillon qui contient au moins une proportion $p$ de la population avec un niveau de confiance $\gamma$. Il ne faut pas le confondre avec l'intervalle de confiance (qui encadre un paramètre) ni avec l'intervalle de tolérance industriel (spécifications imposées par le client).

### 10.1 Définitions

**Intervalle de tolérance bilatéral :** un intervalle $[\bar{x} - k \cdot s, \, \bar{x} + k \cdot s]$ qui contient au moins la proportion $p$ de la population avec un niveau de confiance $\gamma$.

**Intervalle de tolérance unilatéral supérieur :** $(-\infty, \, \bar{x} + k \cdot s]$ contient au moins $p$ de la population.

**Intervalle de tolérance unilatéral inférieur :** $[\bar{x} - k \cdot s, \, +\infty)$ contient au moins $p$ de la population.

Le facteur $k$ dépend de la taille de l'échantillon $n$, de la proportion $p$ et du niveau de confiance $\gamma$.

### 10.2 Facteurs $k$ pour les intervalles bilatéraux (distribution normale)

Le tableau suivant donne les facteurs $k$ pour des intervalles de tolérance bilatéraux sous hypothèse de normalité, pour les valeurs courantes de $p$ et $\gamma$ :

**$p = 0{,}90$ (90 % de la population) :**

| $n$ | $\gamma = 0{,}90$ | $\gamma = 0{,}95$ | $\gamma = 0{,}99$ |
|---|---|---|---|
| 5 | 3,407 | 4,275 | 6,603 |
| 10 | 2,535 | 2,839 | 3,532 |
| 15 | 2,329 | 2,566 | 3,036 |
| 20 | 2,219 | 2,408 | 2,786 |
| 25 | 2,150 | 2,310 | 2,631 |
| 30 | 2,103 | 2,245 | 2,529 |
| 50 | 1,996 | 2,104 | 2,310 |
| 100 | 1,916 | 1,999 | 2,146 |

**$p = 0{,}95$ (95 % de la population) :**

| $n$ | $\gamma = 0{,}90$ | $\gamma = 0{,}95$ | $\gamma = 0{,}99$ |
|---|---|---|---|
| 5 | 4,152 | 5,079 | 7,855 |
| 10 | 2,911 | 3,259 | 4,053 |
| 15 | 2,637 | 2,907 | 3,443 |
| 20 | 2,498 | 2,713 | 3,139 |
| 25 | 2,412 | 2,594 | 2,952 |
| 30 | 2,354 | 2,515 | 2,833 |
| 50 | 2,224 | 2,345 | 2,576 |
| 100 | 2,127 | 2,218 | 2,383 |

**$p = 0{,}99$ (99 % de la population) :**

| $n$ | $\gamma = 0{,}90$ | $\gamma = 0{,}95$ | $\gamma = 0{,}99$ |
|---|---|---|---|
| 5 | 5,741 | 6,634 | 10,260 |
| 10 | 3,739 | 4,187 | 5,209 |
| 15 | 3,329 | 3,669 | 4,343 |
| 20 | 3,126 | 3,395 | 3,927 |
| 25 | 3,002 | 3,231 | 3,677 |
| 30 | 2,919 | 3,118 | 3,513 |
| 50 | 2,735 | 2,882 | 3,165 |
| 100 | 2,601 | 2,715 | 2,917 |

### 10.3 Facteurs $k$ pour les intervalles unilatéraux (distribution normale)

**$p = 0{,}95$, $\gamma = 0{,}95$ :**

| $n$ | $k$ (unilatéral) |
|---|---|
| 5 | 3,400 |
| 10 | 2,568 |
| 15 | 2,329 |
| 20 | 2,208 |
| 25 | 2,132 |
| 30 | 2,080 |
| 50 | 1,965 |
| 100 | 1,874 |

### 10.4 Intervalles de tolérance non paramétriques (distribution-free)

Lorsque la distribution des données n'est pas normale (ou ne peut pas être vérifiée), on utilise des intervalles de tolérance non paramétriques basés sur les statistiques d'ordre.

L'intervalle $[x_{(r)}, x_{(n-r+1)}]$ contient au moins la proportion $p$ de la population avec un niveau de confiance $\gamma$ si :

$$\sum_{j=0}^{2r-2} \binom{n}{j} p^j (1-p)^{n-j} \leq 1 - \gamma$$

**Taille d'échantillon minimale pour un intervalle non paramétrique :**

Pour un intervalle bilatéral avec $r = 1$ (bornes = minimum et maximum de l'échantillon) :

| $p$ | $\gamma = 0{,}90$ | $\gamma = 0{,}95$ | $\gamma = 0{,}99$ |
|---|---|---|---|
| 0,90 | 38 | 46 | 64 |
| 0,95 | 77 | 93 | 130 |
| 0,99 | 388 | 473 | 662 |

Ces tailles d'échantillon élevées illustrent le coût de l'absence d'hypothèse distributionnelle : il faut beaucoup plus de données pour obtenir la même couverture.

### 10.5 Distinction entre les types d'intervalles statistiques

Il est essentiel de ne pas confondre les différents types d'intervalles.

| Type d'intervalle | Ce qu'il encadre | Formule typique | Largeur |
|---|---|---|---|
| **Intervalle de confiance** | Le paramètre $\mu$ de la population. | $\bar{x} \pm t_{\alpha/2, n-1} \cdot s / \sqrt{n}$ | Diminue avec $n$. |
| **Intervalle de prédiction** | La prochaine observation individuelle. | $\bar{x} \pm t_{\alpha/2, n-1} \cdot s \sqrt{1 + 1/n}$ | Diminue lentement avec $n$. |
| **Intervalle de tolérance** | Au moins $p$ % de la population. | $\bar{x} \pm k \cdot s$ | Diminue lentement avec $n$. |

L'intervalle de confiance est toujours le plus étroit car il vise un seul paramètre. L'intervalle de tolérance est le plus large car il doit couvrir une proportion entière de la population avec un niveau de confiance donné.

### 10.6 Application pratique : vérification de la conformité d'un lot

Pour vérifier qu'un lot satisfait une spécification bilatérale $[LSI, LSS]$ avec au moins $p = 99\%$ de la population conforme à un niveau de confiance $\gamma = 95\%$, on procède ainsi :
1. Prélever un échantillon de taille $n$ (par exemple, $n = 30$).
2. Vérifier la normalité (section 7).
3. Calculer $\bar{x}$ et $s$.
4. Lire le facteur $k$ dans la table ($k = 3{,}118$ pour $n = 30$, $p = 0{,}99$, $\gamma = 0{,}95$).
5. Vérifier que $\bar{x} - k \cdot s \geq LSI$ et $\bar{x} + k \cdot s \leq LSS$.
6. Si les deux conditions sont remplies, on conclut avec 95 % de confiance que 99 % de la population est conforme.

---

## 11. Incertitude de mesure (GUM, NIST)

Le GUM (Guide to the expression of Uncertainty in Measurement, JCGM 100:2008) est le document de référence international pour l'évaluation et l'expression de l'incertitude de mesure. La note technique NIST TN 1297 en est un résumé pratique pour les laboratoires.

### 11.1 Principes fondamentaux

Toute mesure est entachée d'une incertitude. Le résultat d'une mesure n'est complet que s'il est accompagné de son incertitude. L'incertitude de mesure quantifie la dispersion des valeurs qui pourraient raisonnablement être attribuées au mesurande.

Le modèle de mesure est :

$$Y = f(X_1, X_2, \ldots, X_N)$$

où $Y$ est le mesurande, $X_i$ sont les grandeurs d'entrée et $f$ est la fonction de mesure.

### 11.2 Évaluation de type A

L'évaluation de type A utilise l'analyse statistique d'une série de $n$ observations répétées.

**Incertitude-type de type A :**

$$u_A = \frac{s}{\sqrt{n}}$$

où $s$ est l'écart-type expérimental :

$$s = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2}$$

L'évaluation de type A est associée à $\nu = n - 1$ degrés de liberté.

### 11.3 Évaluation de type B

L'évaluation de type B utilise des informations autres que statistiques : certificats d'étalonnage, spécifications du fabricant, données de la littérature, jugement d'expert.

**Distribution rectangulaire (uniforme) :**

Lorsque l'on sait seulement que la valeur se situe dans un intervalle $[-a, +a]$ avec une probabilité égale :

$$u_B = \frac{a}{\sqrt{3}}$$

Degrés de liberté associés : $\nu \rightarrow \infty$ (en pratique, on utilise $\nu = 50$ ou plus).

**Distribution triangulaire :**

Lorsque les valeurs centrales sont plus probables que les extrêmes :

$$u_B = \frac{a}{\sqrt{6}}$$

**Distribution normale :**

Lorsque l'information est donnée sous forme d'un intervalle de confiance avec un facteur d'élargissement $k$ :

$$u_B = \frac{a}{k}$$

Par exemple, si un certificat d'étalonnage indique $U = 0{,}1$ mg avec $k = 2$, alors $u_B = 0{,}1 / 2 = 0{,}05$ mg.

**Tableau récapitulatif des distributions de type B :**

| Distribution | Paramètre | Incertitude-type $u_B$ | Usage typique |
|---|---|---|---|
| Rectangulaire | Demi-largeur $a$ | $a / \sqrt{3}$ | Résolution d'un instrument, tolérance d'un composant. |
| Triangulaire | Demi-largeur $a$ | $a / \sqrt{6}$ | Information plus précise que rectangulaire. |
| Normale | Incertitude élargie $U$, facteur $k$ | $U / k$ | Certificat d'étalonnage. |
| En U (arc-sinus) | Demi-amplitude $a$ | $a / \sqrt{2}$ | Oscillation sinusoïdale (température cyclique). |

### 11.4 Incertitude composée

L'incertitude composée $u_c$ est obtenue par la loi de propagation des incertitudes (approximation linéaire) :

$$u_c^2 = \sum_{i=1}^{N} c_i^2 \, u_i^2$$

où $c_i$ est le coefficient de sensibilité :

$$c_i = \frac{\partial f}{\partial x_i}$$

Cette formule suppose que les grandeurs d'entrée sont indépendantes (non corrélées). Si des corrélations existent, il faut ajouter les termes croisés :

$$u_c^2 = \sum_{i=1}^{N} c_i^2 \, u_i^2 + 2 \sum_{i=1}^{N-1}\sum_{j=i+1}^{N} c_i \, c_j \, u(x_i, x_j)$$

où $u(x_i, x_j)$ est la covariance estimée.

### 11.5 Incertitude élargie

L'incertitude élargie $U$ fournit un intervalle dans lequel le mesurande se situe avec un niveau de confiance donné :

$$U = k \cdot u_c$$

| Facteur $k$ | Niveau de confiance (distribution normale) |
|---|---|
| 1 | 68,3 % |
| 2 | 95,5 % |
| 2,576 | 99 % |
| 3 | 99,7 % |

Le facteur $k = 2$ est le plus couramment utilisé et correspond à un niveau de confiance d'environ 95 %.

**Expression du résultat :**

$$Y = y \pm U \quad (k = 2, \text{ niveau de confiance } \approx 95\%)$$

### 11.6 Budget d'incertitude — exemple

Un budget d'incertitude est un tableau résumant toutes les composantes de l'incertitude. Voici un exemple pour la mesure d'une longueur avec un pied à coulisse.

| Source | Type | Distribution | Valeur | Diviseur | $u_i$ | $c_i$ | $c_i \cdot u_i$ | $(c_i \cdot u_i)^2$ |
|---|---|---|---|---|---|---|---|---|
| Répétabilité | A | Normale | $s = 0{,}012$ mm | $\sqrt{n} = \sqrt{5}$ | 0,0054 | 1 | 0,0054 | 0,0000291 |
| Résolution | B | Rectangulaire | $a = 0{,}005$ mm | $\sqrt{3}$ | 0,0029 | 1 | 0,0029 | 0,0000084 |
| Étalonnage | B | Normale | $U = 0{,}010$ mm | $k = 2$ | 0,0050 | 1 | 0,0050 | 0,0000250 |
| Température | B | Rectangulaire | $a = 0{,}003$ mm | $\sqrt{3}$ | 0,0017 | 1 | 0,0017 | 0,0000029 |

**Incertitude composée :** $u_c = \sqrt{0{,}0000291 + 0{,}0000084 + 0{,}0000250 + 0{,}0000029} = \sqrt{0{,}0000654} = 0{,}0081$ mm.

**Incertitude élargie :** $U = 2 \times 0{,}0081 = 0{,}016$ mm (arrondi).

**Résultat :** $L = 25{,}032 \pm 0{,}016$ mm ($k = 2$, niveau de confiance $\approx 95\%$).

<!-- IMG:uncertainty_budget.png -->

### 11.7 Degrés de liberté et formule de Welch-Satterthwaite

Lorsque l'incertitude composée combine des composantes avec des degrés de liberté $\nu_i$ différents, le nombre effectif de degrés de liberté $\nu_{eff}$ est estimé par la formule de Welch-Satterthwaite :

$$\nu_{eff} = \frac{u_c^4}{\sum_{i=1}^{N} \frac{(c_i \, u_i)^4}{\nu_i}}$$

Le résultat est arrondi à l'entier inférieur. Si $\nu_{eff}$ est faible (typiquement $< 30$), le facteur d'élargissement $k$ doit être ajusté en utilisant la distribution de Student :

| $\nu_{eff}$ | $k$ pour 95 % | $k$ pour 99 % |
|---|---|---|
| 1 | 12,71 | 63,66 |
| 2 | 4,30 | 9,92 |
| 3 | 3,18 | 5,84 |
| 5 | 2,57 | 4,03 |
| 10 | 2,23 | 3,17 |
| 20 | 2,09 | 2,85 |
| 30 | 2,04 | 2,75 |
| 50 | 2,01 | 2,68 |
| $\infty$ | 1,96 | 2,58 |

### 11.8 Règles de conformité et incertitude (ISO 14253-1)

Lorsqu'un résultat de mesure est comparé à une spécification, l'incertitude de mesure doit être prise en compte. L'ISO 14253-1 définit les règles suivantes :

**Règle de conformité :** une pièce est déclarée conforme si le résultat de mesure, diminué de l'incertitude élargie, reste à l'intérieur des limites de spécification.

$$LSI + U \leq y \leq LSS - U$$

**Règle de non-conformité :** une pièce est déclarée non conforme si le résultat de mesure, augmenté de l'incertitude élargie, se situe en dehors des limites de spécification.

$$y < LSI - U \quad \text{ou} \quad y > LSS + U$$

**Zone d'incertitude :** lorsque le résultat se situe entre la zone de conformité et la zone de non-conformité, aucune décision ne peut être prise avec certitude. Cette zone a une largeur de $2U$ de chaque côté de la limite de spécification.

### 11.9 Bonnes pratiques pour l'expression de l'incertitude

1. Identifier toutes les sources d'incertitude (ne rien oublier).
2. Quantifier chaque source par une incertitude-type (type A ou type B).
3. Vérifier les unités et les coefficients de sensibilité.
4. Ne pas oublier les corrélations entre grandeurs d'entrée.
5. Arrondir l'incertitude élargie à un ou deux chiffres significatifs.
6. Arrondir le résultat au même nombre de décimales que l'incertitude.
7. Toujours indiquer le facteur d'élargissement $k$ et le niveau de confiance associé.

---

## 12. Guide SPC (ISO 11462) — étapes d'implémentation

L'ISO 11462-1 fournit des lignes directrices pour la mise en oeuvre de la maîtrise statistique des procédés (SPC) dans un environnement industriel. La norme insiste sur le fait que le SPC est un outil de management et d'amélioration continue, et non pas simplement un calcul statistique.

### 12.1 Étape 1 — engagement de la direction

La direction doit comprendre et soutenir la démarche SPC. Cela inclut :
- L'allocation de ressources (personnel, formation, logiciels, instruments).
- La définition d'objectifs mesurables.
- L'intégration du SPC dans le système qualité (ISO 9001).

### 12.2 Étape 2 — identification des procédés

Identifier les procédés critiques qui ont un impact significatif sur la qualité du produit. Utiliser des outils comme :
- L'AMDEC (Analyse des Modes de Défaillance, de leurs Effets et de leur Criticité) pour hiérarchiser les risques.
- Le diagramme de flux du procédé pour comprendre les étapes clés.
- L'analyse de Pareto pour identifier les sources principales de non-conformité.

### 12.3 Étape 3 — analyse du système de mesure

Avant de collecter des données SPC, vérifier que le système de mesure est adéquat (section 6) :
- Étude GRR : %GRR $< 10\%$ (acceptable) ou $< 30\%$ (marginal).
- Nombre de catégories distinctes $ndc \geq 5$.
- Linéarité et stabilité du moyen de mesure.

### 12.4 Étape 4 — collecte des données

Définir un plan de collecte des données incluant :
- La caractéristique à surveiller.
- La taille des sous-groupes $n$ et la fréquence de prélèvement.
- La méthode de prélèvement (aléatoire au sein d'un sous-groupe homogène).
- Le nombre minimal de sous-groupes pour la phase d'étude (au moins 25, selon ISO 7870-2).

### 12.5 Étape 5 — choix de la carte de contrôle

Le choix de la carte de contrôle dépend du type de données et des conditions de production.

| Type de données | Taille de sous-groupe | Carte recommandée |
|---|---|---|
| Variables continues | $n = 1$ | I-MR |
| Variables continues | $2 \leq n \leq 9$ | $\bar{x}$ / R |
| Variables continues | $n \geq 10$ | $\bar{x}$ / S |
| Attributs (conformes / non conformes) | Constante | $np$ |
| Attributs (conformes / non conformes) | Variable | $p$ |
| Attributs (nombre de défauts) | Constante | $c$ |
| Attributs (taux de défauts) | Variable | $u$ |

### 12.6 Étape 6 — calcul des limites de contrôle

Calculer les limites de contrôle à partir des données de la phase d'étude, en utilisant les formules de la section 4. Vérifier que :
- Aucun point n'est en dehors des limites pendant la phase d'étude.
- Aucun motif non aléatoire n'est détecté (règles Western Electric, section 4.3).
- Si des points hors contrôle sont identifiés et que la cause spéciale est trouvée et éliminée, recalculer les limites après exclusion de ces points.

### 12.7 Étape 7 — surveillance du procédé

Mettre en place la carte de contrôle en production :
- Tracer les nouvelles données en temps réel.
- Appliquer les règles de détection (section 4.3).
- Former les opérateurs à l'interprétation de la carte.
- Documenter les événements (changements de lot, réglages, etc.).

### 12.8 Étape 8 — plan d'action en cas de hors-contrôle (OCAP)

L'OCAP (Out-of-Control Action Plan) définit les actions à entreprendre lorsqu'un signal hors contrôle est détecté. Il doit inclure :
- L'identification de la cause spéciale (les 5M : matière, machine, méthode, main-d'oeuvre, milieu).
- L'action corrective immédiate (arrêt, réglage, tri).
- L'action corrective permanente (modification du procédé, maintenance préventive).
- La vérification de l'efficacité de l'action corrective.
- La mise à jour éventuelle des limites de contrôle.

### 12.9 Étape 9 — amélioration continue

Le SPC ne se limite pas à la surveillance : il est un outil d'amélioration continue (PDCA). Les objectifs à long terme sont :
- Réduire la variabilité du procédé (augmenter $C_{pk}$).
- Centrer le procédé sur la cible.
- Réduire le coût de la non-qualité.
- Réviser périodiquement les limites de contrôle pour refléter les améliorations.

**Cycle d'amélioration SPC :**

1. **Planifier (Plan)** : identifier le procédé, choisir la carte, définir les objectifs.
2. **Faire (Do)** : collecter les données, calculer les limites, mettre en oeuvre la carte.
3. **Vérifier (Check)** : analyser les résultats, détecter les causes spéciales, calculer la capabilité.
4. **Agir (Act)** : éliminer les causes spéciales, réduire la variabilité, standardiser les améliorations.

---

## 13. Synthèse et articulations — tableau croisé

Le tableau suivant montre comment les différentes normes et méthodes s'articulent entre elles. Chaque ligne représente une norme, et chaque colonne indique si cette norme est liée à un domaine donné.

| Norme | Échantillonnage | SPC | Capabilité | Normalité | Valeurs aberrantes | Incertitude | Intervalles de tolérance |
|---|---|---|---|---|---|---|---|
| **ISO 2859** (attributs) | Oui (principal). | Utilise les résultats pour ajuster l'inspection. | — | — | — | — | — |
| **ISO 3951** (mesures) | Oui (principal). | — | Nécessite la vérification de la capabilité du procédé. | Hypothèse de normalité requise. | Sensible aux outliers. | — | — |
| **ISO 7870** (SPC) | — | Oui (principal). | Fournit l'estimation de $\sigma$ pour $C_p$, $C_{pk}$. | La carte I-MR suppose la normalité. | Les règles WECO détectent certains outliers. | — | — |
| **ISO 22514-2** (capabilité procédé) | — | Requiert un procédé sous contrôle (SPC). | Oui (principal). | Hypothèse de normalité requise pour les indices. | Les outliers faussent les indices. | Le système de mesure contribue à la variabilité. | Les indices sont liés aux intervalles de tolérance. |
| **ISO 22514-7** (capabilité mesure) | — | Prérequis pour un SPC fiable. | Prérequis pour une capabilité fiable. | — | — | Liée à l'incertitude de mesure. | — |
| **ISO 5479** (normalité) | — | Prérequis pour I-MR. | Prérequis pour $C_p$, $C_{pk}$. | Oui (principal). | À réaliser avant le test d'outliers. | — | Prérequis pour les intervalles paramétriques. |
| **ISO 5725 / ASTM E691** (ANOVA, comparaison) | — | Comparer des procédés ou des machines. | Vérifier l'homogénéité entre équipements. | Prérequis pour les tests paramétriques (Student, ANOVA). | Les outliers faussent les moyennes comparées. | Répétabilité et reproductibilité liées à l'incertitude. | — |
| **ISO 16269-4** (outliers) | Les outliers dans l'échantillon faussent la décision. | Les outliers génèrent de fausses alarmes. | Les outliers faussent $C_{pk}$. | Grubbs suppose la normalité. | Oui (principal). | — | Les outliers élargissent les intervalles. |
| **ISO 16269-6** (intervalles de tolérance) | — | — | Liée à la notion de capabilité. | Intervalles paramétriques supposent la normalité. | Les outliers affectent les bornes. | — | Oui (principal). |
| **ISO 11462** (guide SPC) | — | Oui (guide d'implémentation). | Intègre la capabilité dans la démarche SPC. | Mentionne la vérification de normalité. | — | Mentionne la validation du système de mesure. | — |
| **GUM / NIST** | — | — | L'incertitude de mesure affecte la capabilité apparente. | Type A suppose la normalité pour $u_A$. | Les outliers affectent l'estimation de type A. | Oui (principal). | — |

### Articulations principales

**Séquence logique recommandée pour une étude de capabilité :**

1. **Valider le système de mesure** (ISO 22514-7) : étude GRR, vérifier %GRR $< 10\%$.
2. **Collecter les données** (ISO 7870-2) : au moins 25 sous-groupes.
3. **Tester la normalité** (ISO 5479) : Shapiro-Wilk + Q-Q plot.
4. **Détecter les valeurs aberrantes** (ISO 16269-4) : Grubbs ou Dixon.
5. **Construire les cartes de contrôle** (ISO 7870-2) : vérifier que le procédé est sous contrôle.
6. **Calculer la capabilité** (ISO 22514-2) : $C_p$, $C_{pk}$, $P_p$, $P_{pk}$.
7. **Estimer l'incertitude** (GUM) si nécessaire pour le résultat de mesure.
8. **Calculer les intervalles de tolérance** (ISO 16269-6) si nécessaire pour les spécifications.

---

## 14. Documents indexés dans le RAG

Les documents suivants sont disponibles dans la collection statistique du RAG et peuvent être interrogés pour des informations plus détaillées.

### 14.1 Normes d'échantillonnage

| Référence | Titre | Contenu principal |
|---|---|---|
| **ISO 2859-1** | Plans d'échantillonnage pour les contrôles par attributs — Partie 1 : procédures d'échantillonnage pour les contrôles lot par lot, indexés d'après le NQA. | Tables d'échantillonnage, codes lettres, règles de commutation, courbes OC. |
| **ISO 2859-2** | Plans d'échantillonnage pour les contrôles par attributs — Partie 2 : plans d'échantillonnage pour les contrôles de lots isolés, indexés d'après la qualité limite (LQ). | Plans pour lots isolés, tables indexées par LQ. |
| **ISO 3951-1** | Plans d'échantillonnage pour les contrôles par mesures — Partie 1 : plans d'échantillonnage simples, indexés d'après le NQA. | Méthodes $s$ et $\sigma$, constante d'acceptabilité $k$, spécifications unilatérales et bilatérales. |

### 14.2 Normes SPC et cartes de contrôle

| Référence | Titre | Contenu principal |
|---|---|---|
| **ISO 7870-1** | Cartes de contrôle — Partie 1 : lignes directrices générales. | Vue d'ensemble des types de cartes, principes, terminologie. |
| **ISO 7870-2** | Cartes de contrôle — Partie 2 : cartes de contrôle de Shewhart. | Cartes $\bar{x}$/R, $\bar{x}$/S, I-MR, $p$, $np$, $c$, $u$, tables de constantes. |
| **ASTM E2587** | Standard Practice for Use of Control Charts in Statistical Process Control. | Guide pratique pour la mise en oeuvre des cartes de contrôle, exemples numériques. |
| **ISO 11462-1** | Lignes directrices pour la mise en oeuvre de la maîtrise statistique des procédés (MSP) — Partie 1 : éléments de MSP. | Étapes d'implémentation, organisation, formation, amélioration continue. |

### 14.3 Normes de capabilité

| Référence | Titre | Contenu principal |
|---|---|---|
| **ISO 22514-1** | Méthodes statistiques dans la gestion de processus — Capabilité et performance — Partie 1 : principes et concepts généraux. | Définitions, terminologie, concepts de capabilité et performance. |
| **ISO 22514-2** | Méthodes statistiques dans la gestion de processus — Capabilité et performance — Partie 2 : capabilité et performance de processus pour des caractéristiques de qualité quantitatives dépendant du temps. | Indices $C_p$, $C_{pk}$, $P_p$, $P_{pk}$, méthodes de calcul. |
| **ISO 22514-7** | Méthodes statistiques dans la gestion de processus — Capabilité et performance — Partie 7 : capabilité des processus de mesure. | Indices $C_g$, $C_{gk}$, étude GRR, %GRR, ndc. |

### 14.4 Normes de tests statistiques et intervalles

| Référence | Titre | Contenu principal |
|---|---|---|
| **ISO 5479** | Tests statistiques — Tests de normalité. | Tests de Shapiro-Wilk, Anderson-Darling, Kolmogorov-Smirnov, Q-Q plots. |
| **ISO 16269-4** | Interprétation statistique des données — Partie 4 : détection et traitement des valeurs aberrantes. | Tests de Grubbs, Dixon, tables de valeurs critiques. |
| **ISO 16269-6** | Interprétation statistique des données — Partie 6 : détermination des intervalles de tolérance statistiques. | Intervalles paramétriques et non paramétriques, tables de facteurs $k$. |

### 14.5 Guides internationaux pour l'incertitude

| Référence | Titre | Contenu principal |
|---|---|---|
| **GUM (JCGM 100:2008)** | Évaluation des données de mesure — Guide pour l'expression de l'incertitude de mesure. | Types A et B, propagation des incertitudes, incertitude composée et élargie, Welch-Satterthwaite. |
| **NIST TN 1297** | Guidelines for Evaluating and Expressing the Uncertainty of NIST Measurement Results. | Résumé pratique du GUM adapté aux laboratoires, exemples, recommandations. |

---

*Ce document constitue un support de cours et de référence. Pour des applications contractuelles ou réglementaires, il est indispensable de se référer directement aux textes normatifs officiels dans leur version en vigueur.*
