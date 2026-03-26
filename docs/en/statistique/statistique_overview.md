# Industrial statistical standards course

This document serves as a reference course on the main statistical standards used in industrial quality. It covers sampling, statistical process control (SPC), capability, normality tests, outlier detection, tolerance intervals, and measurement uncertainty.

---

## Table of contents

1. [Introduction - role of statistics in industrial quality](#1-introduction--role-of-statistics-in-industrial-quality)
2. [Sampling by attributes (ISO 2859)](#2-sampling-by-attributes-iso-2859)
3. [Sampling by variables (ISO 3951)](#3-sampling-by-variables-iso-3951)
4. [SPC control charts (ISO 7870, ASTM E2587)](#4-spc-control-charts-iso-7870-astm-e2587)
5. [Process capability (ISO 22514)](#5-process-capability-iso-22514)
6. [Measurement system capability (ISO 22514-7)](#6-measurement-system-capability-iso-22514-7)
7. [Normality tests (ISO 5479)](#7-normality-tests-iso-5479)
8. [Comparison of populations - tests and ANOVA (ISO 5725, ASTM E691)](#8-comparison-of-populations--tests-and-anova-iso-5725-astm-e691)
9. [Outlier detection (ISO 16269-4)](#9-outlier-detection-iso-16269-4)
10. [Statistical tolerance intervals (ISO 16269-6)](#10-statistical-tolerance-intervals-iso-16269-6)
11. [Measurement uncertainty (GUM, NIST)](#11-measurement-uncertainty-gum-nist)
12. [SPC guide (ISO 11462) - implementation steps](#12-spc-guide-iso-11462--implementation-steps)
13. [Summary and interconnections](#13-summary-and-interconnections)
14. [Open source documents indexed in the RAG](#14-open-source-documents-indexed-in-the-rag)

---

## 1. Introduction - role of statistics in industrial quality

### 1.1 Why statistics in production

Industrial quality relies on the ability to make reliable decisions from limited data. Statistical methods provide a rigorous framework to:

- **Accept or reject a lot** based on a representative sample (sampling).
- **Monitor a process** in real time and detect any drift (SPC control charts).
- **Quantify the performance** of a process relative to specifications (capability).
- **Validate a measurement system** before using it for decision-making (GRR analysis).
- **Estimate the uncertainty** associated with a measurement result (GUM).

### 1.2 ISO normative overview for statistical methods

ISO standards related to statistical methods are grouped under ISO/TC 69:

| Standard family | Domain |
|---|---|
| ISO 2859 | Sampling by attributes (inspection by counting). |
| ISO 3951 | Sampling by variables (inspection by measurements). |
| ISO 7870 | Control charts (SPC). |
| ISO 22514 | Process and measurement system capability. |
| ISO 5479 | Normality tests. |
| ISO 16269 | Statistical intervals (tolerance, confidence, prediction). |
| ISO 11462 | Guidelines for implementing SPC. |

In addition to these ISO standards, there are the GUM (JCGM 100:2008) for measurement uncertainty, the NIST Technical Note TN 1297, and ASTM standards such as E2587 for control charts.

### 1.3 Fundamental concepts

**Population and sample.** The population is the complete set of individuals. The sample is a subset of size $n$ drawn from the population of size $N$.

**Type I risk ($\alpha$).** Probability of rejecting a conforming lot (producer's risk). Typically $\alpha = 0.05$.

**Type II risk ($\beta$).** Probability of accepting a nonconforming lot (consumer's risk). The power of the test is $1 - \beta$.

**Confidence level.** $1 - \alpha$ expresses the probability that the estimated interval contains the true parameter value.

**Acceptable quality level (AQL).** The worst average process quality level considered acceptable, expressed as a percentage of nonconforming items.

**Normal distribution.** Characterized by $\mu$ and $\sigma$:
- $\pm 1\sigma$: 68.27% of the population.
- $\pm 2\sigma$: 95.45% of the population.
- $\pm 3\sigma$: 99.73% of the population.

<!-- IMG:normal_distribution_3sigma.png -->

**Degrees of freedom ($\nu$).** For the standard deviation of a sample of size $n$: $\nu = n - 1$.

**Vocabulary.** *Nonconforming*: a unit that fails to satisfy at least one specification. *Nonconformity*: an individual deviation from a specification (a single part may have several nonconformities).

---

## 2. Sampling by attributes (ISO 2859)

> **Note:** ISO 2859 standards are not indexed in the RAG (paid standards). The theory and formulas are presented below for reference.

Sampling by attributes consists of classifying sample units as conforming or nonconforming (binary criterion). The decision is based on the number of nonconforming items found.

### 2.1 ISO 2859-1 - plans indexed by AQL

ISO 2859-1 (equivalent to ANSI/ASQ Z1.4) defines sampling plans indexed by AQL. The procedure is: (1) determine the letter code from the lot size and inspection level, (2) read the sample size $n$ and $Ac$/$Re$ numbers from the table for the chosen AQL.

**Inspection levels:** level II by default; level I (reduced) and III (tightened); special levels S-1 to S-4 for destructive or costly tests.

**Switching rules:**
- **Normal to tightened:** 2 out of 5 consecutive lots rejected.
- **Tightened to normal:** 5 consecutive lots accepted.
- **Normal to reduced:** 10 lots accepted, total nonconforming items below a threshold, stable production.
- **Reduced to normal:** as soon as a lot is rejected.
- **Discontinuation:** 5 consecutive lots rejected during tightened inspection.

<!-- IMG:switching_rules_diagram.png -->

### 2.2 Operating characteristic curves (OC curves)

The OC curve gives the probability of acceptance $P_a$ as a function of the actual proportion of nonconforming items $p$.

For a single sampling plan ($n$, $Ac$), the acceptance probability follows the binomial distribution:

$$P_a(p) = \sum_{i=0}^{Ac} \binom{n}{i} p^i (1-p)^{n-i}$$

Poisson approximation for large lots and small proportions:

$$P_a(p) \approx \sum_{i=0}^{Ac} \frac{(np)^i}{i!} e^{-np}$$

- **AQL point:** $P_a \approx 0.95$ (producer's risk $\alpha \approx 5\%$).
- **LQ point:** $P_a \approx 0.10$ (consumer's risk $\beta \approx 10\%$).

<!-- IMG:oc_curve_sampling.png -->

### 2.3 ISO 2859-2 - plans for isolated lots (LQ)

For isolated lots, ISO 2859-2 provides plans indexed by the limiting quality (LQ), corresponding to $P_a = 0.10$.

---

## 3. Sampling by variables (ISO 3951)

> **Note:** ISO 3951 standards are not indexed in the RAG (paid standards).

Sampling by variables uses the numerical measured value on each unit, allowing better discrimination with a smaller sample. **Fundamental assumption:** the distribution of the characteristic is approximately normal.

### 3.1 ISO 3951-1 - s and $\sigma$ methods

**"s" method (unknown standard deviation):**

$$s = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2}$$

Acceptance criteria:
- Upper specification: $Q_U = (LSS - \bar{x})/s \geq k$
- Lower specification: $Q_L = (\bar{x} - LSI)/s \geq k$

**"$\sigma$" method (known standard deviation):** $\sigma$ is used instead of $s$, allowing smaller sample sizes.

**Two-sided specifications:** combined method (combined estimated proportion $\leq$ AQL) or separate method (independent criterion per limit, more conservative).

---

## 4. SPC control charts (ISO 7870, ASTM E2587)

> **Note:** ISO 7870 and ASTM E2587 standards are not indexed in the RAG (paid standards).

Statistical process control (SPC) distinguishes variations due to common causes (random) from those due to special causes (assignable).

### Fundamental principles (Shewhart)

A control chart comprises:
- **UCL** (upper control limit): $CL + 3\sigma$
- **CL** (center line): mean value
- **LCL** (lower control limit): $CL - 3\sigma$

The $\pm 3\sigma$ limits correspond to a false alarm probability of approximately 0.27% per point.

**Caution:** control limits (calculated from process data) are NOT specification limits (defined by the customer).

### 4.1 Charts for variables

#### 4.1.1 $\bar{x}$ / R chart (mean and range)

Most widely used chart for $2 \leq n \leq 9$.

**Control limits for $\bar{x}$:**

$$UCL_{\bar{x}} = \bar{\bar{x}} + A_2 \bar{R} \qquad LCL_{\bar{x}} = \bar{\bar{x}} - A_2 \bar{R}$$

**Control limits for $R$:**

$$UCL_R = D_4 \bar{R} \qquad LCL_R = D_3 \bar{R}$$

**Standard deviation estimate:** $\hat{\sigma} = \bar{R}/d_2$

**Constants table ($n$ = 2 to 10):**

| $n$ | $A_2$ | $D_3$ | $D_4$ | $d_2$ |
|---|---|---|---|---|
| 2 | 1.880 | 0 | 3.267 | 1.128 |
| 3 | 1.023 | 0 | 2.574 | 1.693 |
| 4 | 0.729 | 0 | 2.282 | 2.059 |
| 5 | 0.577 | 0 | 2.114 | 2.326 |
| 6 | 0.483 | 0 | 2.004 | 2.534 |
| 7 | 0.419 | 0.076 | 1.924 | 2.704 |
| 8 | 0.373 | 0.136 | 1.864 | 2.847 |
| 9 | 0.337 | 0.184 | 1.816 | 2.970 |
| 10 | 0.308 | 0.223 | 1.777 | 3.078 |

<!-- IMG:control_chart_xbar.png -->

#### 4.1.2 $\bar{x}$ / S chart (mean and standard deviation)

Preferred for $n \geq 10$. The standard deviation $s$ is a more reliable estimator than the range for large subgroups.

**Control limits for $\bar{x}$:**

$$UCL_{\bar{x}} = \bar{\bar{x}} + A_3 \bar{S} \qquad LCL_{\bar{x}} = \bar{\bar{x}} - A_3 \bar{S}$$

**Control limits for $S$:**

$$UCL_S = B_4 \bar{S} \qquad LCL_S = B_3 \bar{S}$$

**Standard deviation estimate:** $\hat{\sigma} = \bar{S}/c_4$

Constants $A_3$, $B_3$, $B_4$, $c_4$ are tabulated for $n = 2$ to $25$.

#### 4.1.3 I-MR chart (individual and moving range)

Used for $n = 1$ (slow production, costly measurements, data without natural subgroups).

**Control limits for the I chart:**

$$UCL_X = \bar{X} + 2.66 \, \bar{MR} \qquad LCL_X = \bar{X} - 2.66 \, \bar{MR}$$

The coefficient $2.66 = 3 / d_2 = 3 / 1.128$ (constants for $n = 2$).

**Control limits for MR:** $UCL_{MR} = 3.267 \, \bar{MR}$, $LCL_{MR} = 0$.

**Standard deviation estimate:** $\hat{\sigma} = \bar{MR}/1.128$

**Important:** the I-MR chart is sensitive to departures from normality. Verify normality (section 7) before use.

#### 4.1.4 Study phase and monitoring phase

**Phase 1 (retrospective):** collect at least 25 subgroups, calculate provisional limits, eliminate out-of-control points whose special cause is identified, recalculate.

**Phase 2 (prospective):** monitor in real time using Phase 1 limits. Recalculate only if the process is intentionally modified.

#### 4.1.5 Choosing between charts for variables

| Criterion | $\bar{x}$ / R | $\bar{x}$ / S | I-MR |
|---|---|---|---|
| Subgroup size | $2 \leq n \leq 9$ | $n \geq 10$ | $n = 1$ |
| Estimation of $\sigma$ | $\bar{R}/d_2$ | $\bar{S}/c_4$ | $\bar{MR}/d_2$ ($n=2$) |
| Normality assumption | Robust (CLT). | Robust (CLT). | Sensitive. |

**Fundamental relationships between constants:**
- $A_2 = 3 / (d_2 \sqrt{n})$
- $A_3 = 3 / (c_4 \sqrt{n})$
- $D_3 = 1 - 3 d_3 / d_2$ and $D_4 = 1 + 3 d_3 / d_2$
- $B_3 = 1 - 3\sqrt{1 - c_4^2}/c_4$ and $B_4 = 1 + 3\sqrt{1 - c_4^2}/c_4$

---

### 4.2 Charts for attributes

| Chart | Monitored data | Sample size | Distribution | UCL formula |
|---|---|---|---|---|
| $p$ | Fraction nonconforming | Variable or constant | Binomial | $\bar{p} + 3\sqrt{\bar{p}(1-\bar{p})/n}$ |
| $np$ | Number of nonconforming items | Constant | Binomial | $n\bar{p} + 3\sqrt{n\bar{p}(1-\bar{p})}$ |
| $c$ | Number of nonconformities | Constant | Poisson | $\bar{c} + 3\sqrt{\bar{c}}$ |
| $u$ | Nonconformities per unit rate | Variable or constant | Poisson | $\bar{u} + 3\sqrt{\bar{u}/n}$ |

If LCL is negative, set $LCL = 0$. For $p$ and $u$ charts, limits are recalculated when $n$ varies.

**Application condition for the $p$ chart:** $n\bar{p} \geq 5$ and $n(1 - \bar{p}) \geq 5$.

---

### 4.3 Western Electric / Nelson rules

The supplementary rules increase sensitivity to small shifts by detecting non-random patterns. The zone between the limits is divided into three bands (A, B, C) on each side of the center line.

| Rule | Description | Typical signal |
|---|---|---|
| 1 | 1 point beyond $3\sigma$ | Isolated special cause. |
| 2 | 9 points on the same side of CL | Mean shift. |
| 3 | 6 points in monotone trend | Progressive drift. |
| 4 | 14 points alternating up/down | Overcontrol or alternating sources. |
| 5 | 2 out of 3 beyond $2\sigma$ (same side) | Temporary shift. |
| 6 | 4 out of 5 beyond $1\sigma$ (same side) | Moderate mean shift. |
| 7 | 15 points in Zone C | Stratification (limits too wide). |
| 8 | 8 points beyond $1\sigma$ (both sides) | Mixture of distributions. |

**Recommendation:** in production, apply rules 1 through 4 to limit false alarms. Applying all rules increases the false alarm rate to 2-4% per point. For small shifts, consider CUSUM (ISO 7870-4) or EWMA (ISO 7870-6) charts.

---

## 5. Process capability (ISO 22514)

> **Note:** ISO 22514 standards are not indexed in the RAG (paid standards).

Capability compares the natural process spread to the specified tolerance interval.

### 5.1 Short-term capability indices ($C_p$, $C_{pk}$)

These indices use the within-subgroup standard deviation $\sigma$ (short-term variation).

$$C_p = \frac{LSS - LSI}{6\sigma} \qquad C_{pk} = \min\left(\frac{LSS - \bar{x}}{3\sigma}, \frac{\bar{x} - LSI}{3\sigma}\right)$$

$C_p$ measures potential capability (without centering). $C_{pk}$ accounts for centering. If the process is centered, $C_{pk} = C_p$.

### 5.2 Long-term performance indices ($P_p$, $P_{pk}$)

These indices use the total standard deviation $s$ (total variation including between-subgroup variations).

$$P_p = \frac{LSS - LSI}{6s} \qquad P_{pk} = \min\left(\frac{LSS - \bar{x}}{3s}, \frac{\bar{x} - LSI}{3s}\right)$$

In general $s \geq \sigma$, so $P_p \leq C_p$ and $P_{pk} \leq C_{pk}$. A significant gap reveals between-subgroup variation sources.

<!-- IMG:capability_cp_cpk.png -->

### 5.3 Interpretation of indices

| $C_{pk}$ (or $P_{pk}$) | Interpretation | PPM out of tolerance (total, two tails) |
|---|---|---|
| $< 1.00$ | Incapable | $> 2700$ |
| $1.00$ to $1.33$ | Marginal | $63$ to $2700$ |
| $1.33$ to $1.67$ | Capable | $0.6$ to $63$ |
| $\geq 1.67$ | Highly capable | $< 0.6$ |

### 5.4 Prerequisites for capability calculation

1. The process is **under statistical control** (control chart).
2. The data follow an **approximately normal** distribution (section 7).
3. The **measurement system** is adequate (%GRR acceptable, section 6).
4. At least **25 subgroups** (ISO 22514-2).

---

## 6. Measurement system capability (ISO 22514-7)

> **Note:** ISO 22514-7 is not indexed in the RAG (paid standard).

### 6.1 $C_g$ and $C_{gk}$ indices

$$C_g = \frac{0.2 \times T}{6 s_g} \qquad C_{gk} = \frac{0.1 \times T - |x_m - \bar{x}|}{3 s_g}$$

where $T = LSS - LSI$, $s_g$ is the repeatability standard deviation, $x_m$ the reference value, and $\bar{x}$ the mean of measurements. Requirement: $C_g \geq 1.33$ and $C_{gk} \geq 1.33$.

### 6.2 GRR study

Measurement system variability decomposes into:

- **Repeatability (EV):** $EV = \bar{R}_{operators} / d_2$
- **Reproducibility (AV):** $AV = \sqrt{(\bar{R}_{parts \, by \, operator}/d_2)^2 - EV^2/(nr)}$
- **Combined GRR:** $GRR = \sqrt{EV^2 + AV^2}$
- **Part Variation:** $PV = R_{parts}/d_2$
- **Total Variation:** $TV = \sqrt{GRR^2 + PV^2}$
- **GRR percentage:** $\%GRR = GRR/TV \times 100$

| %GRR | Interpretation |
|---|---|
| $< 10\%$ | Acceptable. |
| $10\%$ to $30\%$ | Marginal. |
| $> 30\%$ | Unacceptable. |

**Number of distinct categories:** $ndc = 1.41 \times PV/GRR$ (requirement: $ndc \geq 5$).

<!-- IMG:grr_variance_components.png -->

---

## 7. Normality tests (ISO 5479)

> **Note:** ISO 5479 is not indexed in the RAG (paid standard).

### 7.1 Why normality matters

- The R, S, and I-MR charts are sensitive to non-normality ($\bar{x}$ charts are more robust thanks to the CLT).
- Capability indices $C_p$/$C_{pk}$ assume normality.
- Parametric tolerance intervals (ISO 16269-6) assume normality.

### 7.2 Shapiro-Wilk test

Reference test for $n < 50$ (extensible to $n = 5000$).

$$W = \frac{\left(\sum_{i=1}^{m} a_i (x_{(n+1-i)} - x_{(i)})\right)^2}{\sum_{i=1}^{n}(x_i - \bar{x})^2}$$

$W$ ranges between 0 and 1. Reject $H_0$ (normality) if $W < W_{critical}$ or if $p$-value $< \alpha$.

### 7.3 Anderson-Darling test

Particularly sensitive to distribution tails (relevant for PPM calculations).

$$A^2 = -n - \frac{1}{n}\sum_{i=1}^{n}(2i - 1)\left[\ln(F(x_{(i)})) + \ln(1 - F(x_{(n+1-i)}))\right]$$

$$A^{*2} = A^2 \left(1 + \frac{0.75}{n} + \frac{2.25}{n^2}\right)$$

Critical value for $\alpha = 0.05$: $A^{*2} \approx 0.752$.

### 7.4 Kolmogorov-Smirnov test (Lilliefors)

$$D = \max_{i} \left| F_n(x_{(i)}) - F_0(x_{(i)}) \right|$$

When $\mu$ and $\sigma$ are estimated, use Lilliefors tables.

### 7.5 Q-Q plot (quantile-quantile)

Construction: sort data, calculate $p_i = (i - 0.375)/(n + 0.25)$ (Blom), then $z_i = \Phi^{-1}(p_i)$, and plot $x_{(i)}$ vs $z_i$.

Interpretation: linear alignment = normality; S-shaped curvature = skewness; deviating extremes = heavy tails.

<!-- IMG:qqplot_comparison.png -->

### 7.6 Comparative table

| Test | Primary sensitivity | Recommended use |
|---|---|---|
| Shapiro-Wilk | Center and tails. | Reference for $n < 50$. |
| Anderson-Darling | Distribution tails. | Complement for PPM. |
| KS (Lilliefors) | Center of distribution. | When others are not available. |
| Q-Q plot | Overall visual diagnostic. | Always as a complement. |

---

## 8. Comparison of populations - tests and ANOVA (ISO 5725, ASTM E691)

> **Note:** ISO 5725 and ASTM E691 standards are not indexed in the RAG (paid standards).

### 8.1 Student's t-test - comparing means

#### 8.1.1 One-sample

$$t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}} \qquad \nu = n - 1$$

Reject $H_0$ if $|t| > t_{\alpha/2, n-1}$.

#### 8.1.2 Two independent samples

**Equal variances (pooled):**

$$t = \frac{\bar{x}_1 - \bar{x}_2}{s_p \sqrt{1/n_1 + 1/n_2}} \qquad s_p = \sqrt{\frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1+n_2-2}}$$

**Unequal variances (Welch):**

$$t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{s_1^2/n_1 + s_2^2/n_2}} \qquad \nu_{eff} = \frac{(s_1^2/n_1 + s_2^2/n_2)^2}{(s_1^2/n_1)^2/(n_1-1) + (s_2^2/n_2)^2/(n_2-1)}$$

When in doubt about equal variances, use Welch's test.

#### 8.1.3 Paired t-test

$$t = \frac{\bar{d}}{s_d / \sqrt{n}} \qquad \nu = n - 1$$

### 8.2 Fisher's F-test - comparing two variances

$$F = \frac{s_1^2}{s_2^2} \quad (s_1^2 \geq s_2^2)$$

Reject $H_0$ if $F > F_{\alpha/2, n_1-1, n_2-1}$. The F-test is very sensitive to departures from normality; prefer the Levene test when in doubt.

### 8.3 One-way ANOVA

Compares the means of $k \geq 3$ groups simultaneously. $H_0: \mu_1 = \mu_2 = \cdots = \mu_k$.

**Decomposition:** $SS_T = SS_B + SS_W$

| Source | SS | df | MS | F |
|---|---|---|---|---|
| Between groups | $SS_B$ | $k - 1$ | $MS_B = SS_B/(k-1)$ | $F = MS_B/MS_W$ |
| Within groups | $SS_W$ | $N - k$ | $MS_W = SS_W/(N-k)$ | |
| Total | $SS_T$ | $N - 1$ | | |

Reject $H_0$ if $F > F_{\alpha, k-1, N-k}$.

**Conditions:** independence, normality, homogeneity of variances (test with Bartlett or Levene).

<!-- IMG:anova_boxplot.png -->

### 8.4 Two-way ANOVA

Model with interaction:

$$x_{ijk} = \mu + \alpha_i + \beta_j + (\alpha\beta)_{ij} + \varepsilon_{ijk}$$

The decomposition includes $SS_A$, $SS_B$, $SS_{AB}$, and $SS_E$. If the interaction is significant, main effects must be interpreted with caution.

### 8.5 Post-hoc tests

| Method | Primary use | Particularity |
|---|---|---|
| Tukey HSD | All pairs, balanced designs. | Exact family-wise error control. |
| Bonferroni | Any situation. | Simple but conservative if $m$ is large. |
| Scheffé | Any contrasts. | Most conservative for pairs. |
| Dunnett | Comparison to a single control. | More powerful than Tukey for this case. |

### 8.6 Tests for homogeneity of variances

**Bartlett:** powerful but very sensitive to departures from normality.

**Levene:** replaces each observation by $z_{ij} = |x_{ij} - \tilde{x}_j|$ (group median), then performs ANOVA on $z_{ij}$. Robust to non-normal data.

### 8.7 Non-parametric alternative - Kruskal-Wallis

$$H = \frac{12}{N(N+1)} \sum_{j=1}^{k} \frac{R_j^2}{n_j} - 3(N+1)$$

Under $H_0$, $H \sim \chi^2(k-1)$ for $n_j \geq 5$.

### 8.8 ISO 5725 and ASTM E691

**ISO 5725 - accuracy (trueness and precision):**
- Repeatability: $r = 2.8 \times s_r$
- Reproducibility: $R = 2.8 \times s_R$ with $s_R^2 = s_r^2 + s_L^2$

**ASTM E691 - Mandel statistics:**
- $h_j = (\bar{x}_j - \bar{\bar{x}})/s_{\bar{x}}$ (between-laboratory consistency)
- $k_j = s_j/s_r$ (within-laboratory consistency)

### 8.9 Summary table

| Objective | Test | Non-parametric alternative |
|---|---|---|
| 1 mean vs reference | One-sample t-test | Wilcoxon signed-rank |
| 2 independent means | Two-sample t-test / Welch | Mann-Whitney U |
| 2 paired means | Paired t-test | Wilcoxon signed-rank |
| 2 variances | Fisher F | Levene |
| $k \geq 3$ means | One-way ANOVA | Kruskal-Wallis |
| $k$ means (2 factors) | Two-way ANOVA | Friedman |

---

## 9. Outlier detection (ISO 16269-4)

> **Note:** ISO 16269-4 is not indexed in the RAG (paid standard).

### 9.1 Grubbs test

$$G = \frac{\max_i |x_i - \bar{x}|}{s}$$

Reject $H_0$ (no outlier) if $G > G_{critical}$. The test assumes normality.

### 9.2 Dixon test

Alternative for small samples ($3 \leq n \leq 25$), based on order statistics (assumes normality).

| Size $n$ | Statistic | Formula |
|---|---|---|
| 3 to 7 | $r_{10}$ | $(x_{(n)} - x_{(n-1)}) / (x_{(n)} - x_{(1)})$ |
| 8 to 10 | $r_{11}$ | $(x_{(n)} - x_{(n-1)}) / (x_{(n)} - x_{(2)})$ |
| 11 to 13 | $r_{21}$ | $(x_{(n)} - x_{(n-2)}) / (x_{(n)} - x_{(2)})$ |
| 14 to 25 | $r_{22}$ | $(x_{(n)} - x_{(n-2)}) / (x_{(n)} - x_{(3)})$ |

### 9.3 Practical recommendation

For $n < 10$: prefer Dixon. For $n \geq 10$: prefer Grubbs. Always accompany with graphical analysis (box plot, Q-Q plot).

---

## 10. Statistical tolerance intervals (ISO 16269-6)

> **Note:** ISO 16269-6 is not indexed in the RAG (paid standard).

A statistical tolerance interval contains at least a proportion $p$ of the population with a confidence level $\gamma$. Not to be confused with the confidence interval or industrial tolerance specifications.

### 10.1 Parametric intervals (normal distribution)

**Two-sided:** $[\bar{x} - k \cdot s, \, \bar{x} + k \cdot s]$

**One-sided:** $(-\infty, \, \bar{x} + k \cdot s]$ or $[\bar{x} - k \cdot s, \, +\infty)$

The factor $k$ depends on $n$, $p$, and $\gamma$. Excerpt for $p = 0.95$ (two-sided):

| $n$ | $\gamma = 0.90$ | $\gamma = 0.95$ | $\gamma = 0.99$ |
|---|---|---|---|
| 5 | 4.152 | 5.079 | 7.855 |
| 10 | 2.911 | 3.259 | 4.053 |
| 20 | 2.498 | 2.713 | 3.139 |
| 30 | 2.354 | 2.515 | 2.833 |
| 50 | 2.224 | 2.345 | 2.576 |
| 100 | 2.127 | 2.218 | 2.383 |

### 10.2 Non-parametric (distribution-free) intervals

The interval $[x_{(r)}, x_{(n-r+1)}]$ covers at least $p$ of the population with confidence $\gamma$ if:

$$\sum_{j=0}^{2r-2} \binom{n}{j} p^j (1-p)^{n-j} \leq 1 - \gamma$$

Minimum sample sizes for $r = 1$ (bounds = min/max) are much larger than the parametric approach.

### 10.3 Distinction between types of intervals

| Type | What it brackets | Typical formula |
|---|---|---|
| Confidence interval | The parameter $\mu$. | $\bar{x} \pm t_{\alpha/2, n-1} \cdot s / \sqrt{n}$ |
| Prediction interval | The next observation. | $\bar{x} \pm t_{\alpha/2, n-1} \cdot s \sqrt{1 + 1/n}$ |
| Tolerance interval | At least $p$% of the population. | $\bar{x} \pm k \cdot s$ |

---

## 11. Measurement uncertainty (GUM, NIST)

The GUM (JCGM 100:2008) is the international reference document for measurement uncertainty. The NIST TN 1297 is a practical summary. The NIST SP 260-135 guide covers statistical metrology.

### 11.1 Measurement model

$$Y = f(X_1, X_2, \ldots, X_N)$$

### 11.2 Type A evaluation

$$u_A = \frac{s}{\sqrt{n}} \qquad s = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2}$$

Degrees of freedom: $\nu = n - 1$.

### 11.3 Type B evaluation

| Distribution | Parameter | Standard uncertainty $u_B$ | Typical use |
|---|---|---|---|
| Rectangular | Half-width $a$ | $a / \sqrt{3}$ | Instrument resolution, component tolerance. |
| Triangular | Half-width $a$ | $a / \sqrt{6}$ | More precise information than rectangular. |
| Normal | Expanded uncertainty $U$, factor $k$ | $U / k$ | Calibration certificate. |
| U-shaped (arcsine) | Half-amplitude $a$ | $a / \sqrt{2}$ | Sinusoidal oscillation. |

### 11.4 Combined uncertainty

$$u_c^2 = \sum_{i=1}^{N} c_i^2 \, u_i^2 \qquad c_i = \frac{\partial f}{\partial x_i}$$

With correlations:

$$u_c^2 = \sum_{i=1}^{N} c_i^2 \, u_i^2 + 2 \sum_{i=1}^{N-1}\sum_{j=i+1}^{N} c_i \, c_j \, u(x_i, x_j)$$

### 11.5 Expanded uncertainty

$$U = k \cdot u_c$$

| Factor $k$ | Confidence level |
|---|---|
| 1 | 68.3% |
| 2 | 95.5% |
| 3 | 99.7% |

The factor $k = 2$ is most common ($\approx 95\%$).

**Expression of the result:** $Y = y \pm U \quad (k = 2)$

### 11.6 Uncertainty budget - example

| Source | Type | Distribution | Value | Divisor | $u_i$ |
|---|---|---|---|---|---|
| Repeatability | A | Normal | $s = 0.012$ mm | $\sqrt{5}$ | 0.0054 |
| Resolution | B | Rectangular | $a = 0.005$ mm | $\sqrt{3}$ | 0.0029 |
| Calibration | B | Normal | $U = 0.010$ mm | $k = 2$ | 0.0050 |
| Temperature | B | Rectangular | $a = 0.003$ mm | $\sqrt{3}$ | 0.0017 |

$u_c = 0.0081$ mm, $U = 0.016$ mm ($k = 2$).

**Result:** $L = 25.032 \pm 0.016$ mm ($k = 2$, confidence level $\approx 95\%$).

<!-- IMG:uncertainty_budget.png -->

### 11.7 Welch-Satterthwaite formula

$$\nu_{eff} = \frac{u_c^4}{\sum_{i=1}^{N} \frac{(c_i \, u_i)^4}{\nu_i}}$$

If $\nu_{eff} < 30$, adjust $k$ using the Student's t-distribution (e.g., $k = 2.23$ for $\nu_{eff} = 10$ at 95%).

### 11.8 Conformity rules (ISO 14253-1)

- **Conformity:** $LSI + U \leq y \leq LSS - U$
- **Nonconformity:** $y < LSI - U$ or $y > LSS + U$
- **Uncertainty zone:** width $2U$ on each side of the specification limit.

---

## 12. SPC guide (ISO 11462) - implementation steps

> **Note:** ISO 11462 is not indexed in the RAG (paid standard).

ISO 11462-1 provides guidelines for implementing SPC. Main steps:

1. **Management commitment:** resources, objectives, ISO 9001 integration.
2. **Critical process identification:** FMEA, process flow diagram, Pareto analysis.
3. **Measurement system analysis:** GRR, ndc, linearity, stability.
4. **Data collection:** characteristic, subgroup size, frequency, minimum 25 subgroups.
5. **Control chart selection** (cf. section 4.1.5).
6. **Control limit calculation** (study phase).
7. **Production monitoring** (Phase 2).
8. **OCAP (Out-of-Control Action Plan):** special cause identification (5Ms), corrective action, verification, limit update.
9. **Continuous improvement (PDCA):** reduce variability, center the process, revise limits.

---

## 13. Summary and interconnections

**Recommended logical sequence for a capability study:**

1. **Validate the measurement system** (ISO 22514-7): %GRR $< 10\%$.
2. **Collect data** (ISO 7870-2): at least 25 subgroups.
3. **Test normality** (ISO 5479): Shapiro-Wilk + Q-Q plot.
4. **Detect outliers** (ISO 16269-4): Grubbs or Dixon.
5. **Construct control charts** (ISO 7870-2): verify statistical control.
6. **Calculate capability** (ISO 22514-2): $C_p$, $C_{pk}$, $P_p$, $P_{pk}$.
7. **Estimate uncertainty** (GUM) if necessary.
8. **Calculate tolerance intervals** (ISO 16269-6) if necessary.

---

## 14. Open source documents indexed in the RAG

The following documents are freely available and indexed in the RAG statistical collection:

| Reference | Title |
|---|---|
| **JCGM 100:2008 (GUM)** | Evaluation of measurement data - Guide to the expression of uncertainty in measurement (English version). |
| **JCGM 100:2008 (GUM)** | Evaluation des donnees de mesure - Guide pour l'expression de l'incertitude de mesure (French version). |
| **NIST SP 260-135** | Statistical methods for the certification of reference materials - Statistics in metrology. |
| **NIST TN 1297** | Guidelines for Evaluating and Expressing the Uncertainty of NIST Measurement Results. |

---

*This document serves as a course and reference support. For contractual or regulatory applications, it is essential to refer directly to the official standard texts in their current version.*
