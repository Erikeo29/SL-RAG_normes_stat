# Industrial statistical standards course

This document serves as a reference course on the main statistical standards used in industrial quality. It covers sampling, statistical process control (SPC), capability, normality tests, outlier detection, tolerance intervals, and measurement uncertainty. Each section refers to the corresponding ISO, ASTM, or international guide standards.

---

## Table of contents

1. [Introduction — role of statistics in industrial quality](#1-introduction--role-of-statistics-in-industrial-quality)
2. [Sampling by attributes (ISO 2859)](#2-sampling-by-attributes-iso-2859)
3. [Sampling by variables (ISO 3951)](#3-sampling-by-variables-iso-3951)
4. [SPC control charts (ISO 7870, ASTM E2587)](#4-spc-control-charts-iso-7870-astm-e2587)
5. [Process capability (ISO 22514)](#5-process-capability-iso-22514)
6. [Measurement system capability (ISO 22514-7)](#6-measurement-system-capability-iso-22514-7)
7. [Normality tests (ISO 5479)](#7-normality-tests-iso-5479)
8. [Comparison of populations — tests and ANOVA (ISO 5725, ASTM E691)](#8-comparison-of-populations--tests-and-anova-iso-5725-astm-e691)
9. [Outlier detection (ISO 16269-4)](#9-outlier-detection-iso-16269-4)
10. [Statistical tolerance intervals (ISO 16269-6)](#10-statistical-tolerance-intervals-iso-16269-6)
11. [Measurement uncertainty (GUM, NIST)](#11-measurement-uncertainty-gum-nist)
12. [SPC guide (ISO 11462) — implementation steps](#12-spc-guide-iso-11462--implementation-steps)
13. [Summary and interconnections — cross-reference table](#13-summary-and-interconnections--cross-reference-table)
14. [Documents indexed in the RAG](#14-documents-indexed-in-the-rag)

---

## 1. Introduction — role of statistics in industrial quality

### 1.1 Why statistics in production

Industrial quality relies on the ability to make reliable decisions from limited data. In a mass production context, it is impossible to inspect every part or to continuously monitor every process parameter. Statistical methods provide a rigorous framework to:

- **Accept or reject a lot** of products based on a representative sample (sampling).
- **Monitor a process** in real time and detect any drift before it generates nonconformities (SPC control charts).
- **Quantify the performance** of a process relative to customer specifications (capability).
- **Validate a measurement system** before using it for decision-making (GRR analysis).
- **Estimate the uncertainty** associated with a measurement result (GUM).

### 1.2 ISO normative overview for statistical methods

ISO standards related to statistical methods are grouped under the technical committee ISO/TC 69 "Applications of statistical methods." The main families are as follows:

| Standard family | Domain |
|---|---|
| ISO 2859 | Sampling by attributes (inspection by counting). |
| ISO 3951 | Sampling by variables (inspection by measurements). |
| ISO 7870 | Control charts (SPC). |
| ISO 22514 | Process and measurement system capability. |
| ISO 5479 | Normality tests. |
| ISO 16269 | Statistical intervals (tolerance, confidence, prediction). |
| ISO 11462 | Guidelines for implementing SPC. |

In addition to these ISO standards, there are international guides such as the GUM (JCGM 100:2008) for measurement uncertainty, the NIST Technical Note TN 1297, and ASTM standards such as E2587 for control charts.

### 1.3 Fundamental concepts

**Population and sample.** The population is the complete set of individuals (parts, measurements) under study. The sample is a subset of size $n$ drawn from the population of size $N$. All statistical inference relies on the quality of the sampling.

**Type I risk ($\alpha$).** This is the probability of rejecting a lot (or concluding that a signal exists) when the process is actually conforming. It is also called the producer's risk. Typically $\alpha = 0{,}05$ (5%).

**Type II risk ($\beta$).** This is the probability of accepting a lot (or failing to detect a signal) when the process is actually nonconforming. It is also called the consumer's risk. The power of the test is $1 - \beta$.

**Confidence level.** The confidence level $1 - \alpha$ expresses the probability that the estimated interval contains the true parameter value. A 95% confidence level means that, out of 100 intervals constructed in the same way, approximately 95 would contain the true value.

**Acceptable quality level (AQL).** The AQL is the worst average process quality level that the consumer considers acceptable. It is expressed as a percentage of nonconforming items in the lot.

**Normal distribution.** The normal (or Gaussian) distribution is the fundamental probabilistic model in industrial statistics. It is characterized by two parameters: the mean $\mu$ and the standard deviation $\sigma$. The empirical rule gives the following probabilities:
- $\pm 1\sigma$: 68.27% of the population.
- $\pm 2\sigma$: 95.45% of the population.
- $\pm 3\sigma$: 99.73% of the population.

**Degrees of freedom ($\nu$).** The number of degrees of freedom is the number of independent values that can vary in a statistical calculation. For the standard deviation of a sample of size $n$, the number of degrees of freedom is $\nu = n - 1$.

**Vocabulary related to nonconformities.** It is important to distinguish:
- **Nonconforming** (nonconforming): a unit that fails to satisfy at least one specification. A part is either conforming or nonconforming.
- **Nonconformity** (nonconformity): an individual deviation from a specification. A single part may have several nonconformities.

---

## 2. Sampling by attributes (ISO 2859)

Sampling by attributes consists of inspecting a sample of $n$ units drawn from a lot and classifying them as conforming or nonconforming (binary criterion: pass / fail). The decision to accept or reject the lot is based on the number of nonconforming units found in the sample.

### 2.1 ISO 2859-1 — plans indexed by AQL

ISO 2859-1 (equivalent to ANSI/ASQ Z1.4) defines sampling plans indexed by the acceptable quality level (AQL). It is the worldwide reference for acceptance inspection by attributes.

#### 2.1.1 Terminology

| Term | Definition |
|---|---|
| **Lot** | A defined quantity of products manufactured under conditions assumed to be uniform. |
| **Sample size** ($n$) | Number of units drawn from the lot for inspection. |
| **AQL** (AQL) | Acceptable quality level: maximum percentage of nonconforming items considered satisfactory as a process average. |
| **Acceptance number** ($Ac$) | Maximum number of nonconforming items in the sample to accept the lot. |
| **Rejection number** ($Re$) | Minimum number of nonconforming items in the sample to reject the lot. $Re = Ac + 1$ for single sampling plans. |
| **OC curve** | Operating Characteristic curve giving the probability of acceptance as a function of the actual proportion of nonconforming items. |

#### 2.1.2 Inspection levels

ISO 2859-1 defines three general inspection levels and four special levels:

| Level | Usage | Relative sample size |
|---|---|---|
| **I** | Reduced inspection, less discriminating. | Smaller. |
| **II** | Normal inspection, default usage. | Reference. |
| **III** | Tightened inspection, more discriminating. | Larger. |
| **S-1** | Special inspection, costly or destructive tests. | Very small. |
| **S-2** | Special inspection. | Very small. |
| **S-3** | Special inspection. | Small. |
| **S-4** | Special inspection. | Small. |

Level II is the default level. Special levels S-1 to S-4 are used when tests are destructive or very costly and the sample size must be minimized.

#### 2.1.3 Letter code table (lot size to letter code)

The first step is to determine the letter code from the lot size and the chosen inspection level.

| Lot size | S-1 | S-2 | S-3 | S-4 | I | II | III |
|---|---|---|---|---|---|---|---|
| 2 to 8 | A | A | A | A | A | A | B |
| 9 to 15 | A | A | A | A | A | B | C |
| 16 to 25 | A | A | B | B | B | C | D |
| 26 to 50 | A | B | B | C | C | D | E |
| 51 to 90 | B | B | C | C | C | E | F |
| 91 to 150 | B | B | C | D | D | F | G |
| 151 to 280 | B | C | D | E | E | G | H |
| 281 to 500 | B | C | D | E | F | H | J |
| 501 to 1200 | C | C | E | F | G | J | K |
| 1201 to 3200 | C | D | E | G | H | K | L |
| 3201 to 10000 | C | D | F | G | J | L | M |
| 10001 to 35000 | C | D | F | H | K | M | N |
| 35001 to 150000 | D | E | G | J | L | N | P |
| 150001 to 500000 | D | E | G | J | M | P | Q |
| 500001 and above | D | E | H | K | N | Q | R |

#### 2.1.4 Single sampling plans — normal inspection

Once the letter code is determined, the sample size $n$ and the $Ac$ / $Re$ numbers are read from the table corresponding to the chosen AQL. Example plans for normal inspection (excerpt):

| Code | $n$ | AQL 0.65 | AQL 1.0 | AQL 1.5 | AQL 2.5 | AQL 4.0 | AQL 6.5 |
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

*Notation: $Ac$/$Re$. The symbol "—" indicates that the plan is not available for this AQL.*

#### 2.1.5 Tightened inspection and reduced inspection

**Tightened inspection.** The acceptance criteria are stricter (reduced $Ac$ numbers for the same sample size). Tightened inspection is applied when lot quality deteriorates.

**Reduced inspection.** The sample size is decreased and the criteria are relaxed. It is accessed when quality is consistently good.

#### 2.1.6 Switching rules

The switching rules between the three inspection severities are defined in clause 9 of ISO 2859-1.

**Normal to tightened.** Switch to tightened inspection when 2 out of 5 consecutive lots (or fewer) are rejected during normal inspection.

**Tightened to normal.** Return to normal inspection when 5 consecutive lots are accepted during tightened inspection.

**Normal to reduced.** Switch to reduced inspection when the following three conditions are simultaneously met:
- The last 10 lots have been accepted during normal inspection.
- The total number of nonconforming items in these 10 samples does not exceed a specified threshold.
- Production is regular and stable.

**Reduced to normal.** Return to normal inspection as soon as a lot is rejected during reduced inspection, or other instability conditions are detected.

**Discontinuation of inspection.** If, during tightened inspection, 5 consecutive lots remain rejected, inspection is suspended and corrective actions are required before resumption.

<!-- IMG:switching_rules_diagram.png -->

#### 2.1.7 Operating characteristic curves (OC curves)

The operating characteristic (OC) curve gives the probability of acceptance $P_a$ of the lot as a function of the actual proportion of nonconforming items $p$ in the lot.

For a single sampling plan with sample size $n$ and acceptance number $Ac$, the probability of acceptance follows the binomial distribution:

$$P_a(p) = \sum_{i=0}^{Ac} \binom{n}{i} p^i (1-p)^{n-i}$$

For large lots and small proportions $p$, the Poisson approximation is used:

$$P_a(p) \approx \sum_{i=0}^{Ac} \frac{(np)^i}{i!} e^{-np}$$

The OC curve allows visualization of:
- The **AQL point**: the proportion $p$ for which $P_a \approx 0{,}95$ (producer's risk $\alpha \approx 5\%$).
- The **LQ point**: the proportion $p$ for which $P_a \approx 0{,}10$ (consumer's risk $\beta \approx 10\%$).

#### 2.1.8 Producer's risk ($\alpha$) and consumer's risk ($\beta$)

| Risk | Symbol | Definition | Typical value |
|---|---|---|---|
| Producer's risk | $\alpha$ | Probability of rejecting a lot whose quality is at the AQL. | $\approx 5\%$ |
| Consumer's risk | $\beta$ | Probability of accepting a lot whose quality is at the LQ level. | $\approx 10\%$ |

The choice of sampling plan is a compromise between these two risks. A more discriminating plan (larger sample size) simultaneously reduces $\alpha$ and $\beta$, but increases inspection cost.

<!-- IMG:oc_curve_sampling.png -->

### 2.2 ISO 2859-2 — plans for isolated lots (LQ)

When lots are not part of a continuous series (isolated lot, first lot from a new supplier), the switching rules of ISO 2859-1 cannot be used. ISO 2859-2 provides sampling plans indexed by the limiting quality (LQ).

The LQ is the quality level corresponding to a low probability of acceptance (typically $P_a = 0{,}10$). The plan is chosen so that, if the actual proportion of nonconforming items reaches the LQ, the lot has at most a 10% chance of being accepted.

**Procedure:**
1. Define the desired LQ (as a percentage of nonconforming items).
2. Determine the lot size $N$.
3. Read the sample size $n$ and acceptance number $Ac$ from the ISO 2859-2 tables.
4. Draw $n$ units, inspect, and count the nonconforming items $d$.
5. If $d \leq Ac$: accept the lot. If $d \geq Re$: reject the lot.

---

## 3. Sampling by variables (ISO 3951)

Sampling by variables uses the numerical measured value on each unit in the sample, rather than a simple conforming / nonconforming classification. This allows for better discrimination with a smaller sample than attribute sampling.

### 3.1 When to use sampling by variables

Sampling by variables is preferable when:
- The controlled characteristic is measurable on a continuous scale.
- The distribution of the characteristic is approximately normal (fundamental assumption).
- One wishes to reduce the sample size compared to an equivalent attribute sampling plan.
- The cost of an individual measurement is acceptable.

It is **not** appropriate when:
- The characteristic is qualitative (visual, functional).
- The distribution is strongly non-normal and cannot be transformed.
- Multiple characteristics must be controlled simultaneously with different distributions.

### 3.2 ISO 3951-1 — plans indexed by AQL

ISO 3951-1 offers two main methods depending on whether the process standard deviation is known or not.

#### 3.2.1 "s" method (unknown standard deviation)

When the process standard deviation $\sigma$ is not known, it is estimated from the sample by the corrected standard deviation $s$:

$$s = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2}$$

**Acceptance criterion for a one-sided upper specification:**

The quality statistic is calculated:

$$Q_U = \frac{LSS - \bar{x}}{s}$$

where $LSS$ is the upper specification limit (USL). If $Q_U \geq k$, the lot is accepted. Otherwise, it is rejected.

**Acceptance criterion for a one-sided lower specification:**

$$Q_L = \frac{\bar{x} - LSI}{s}$$

where $LSI$ is the lower specification limit (LSL). If $Q_L \geq k$, the lot is accepted.

The acceptability constant $k$ depends on the AQL, the letter code (lot size and inspection level), and the inspection severity.

#### 3.2.2 "$\sigma$" method (known standard deviation)

When the standard deviation $\sigma$ is known (for example, from a reliable production history), $\sigma$ is used directly instead of $s$:

$$Q_U = \frac{LSS - \bar{x}}{\sigma}$$

$$Q_L = \frac{\bar{x} - LSI}{\sigma}$$

The $\sigma$ method allows smaller sample sizes than the $s$ method because there is no uncertainty related to the estimation of the standard deviation.

#### 3.2.3 Acceptability constant $k$ — table excerpt

The values of $k$ for normal inspection, $s$ method, are given below (excerpt):

| Code | $n$ | AQL 0.65 | AQL 1.0 | AQL 1.5 | AQL 2.5 | AQL 4.0 | AQL 6.5 |
|---|---|---|---|---|---|---|---|
| B | 3 | — | — | — | — | 0.950 | 0.566 |
| C | 4 | — | — | — | 1.452 | 0.917 | 0.550 |
| D | 5 | — | — | 1.666 | 1.242 | 0.874 | 0.536 |
| E | 7 | — | 1.879 | 1.490 | 1.133 | 0.824 | 0.523 |
| F | 10 | 2.058 | 1.715 | 1.400 | 1.066 | 0.790 | 0.516 |
| G | 15 | 1.909 | 1.618 | 1.342 | 1.030 | 0.770 | 0.513 |
| H | 20 | 1.833 | 1.565 | 1.307 | 1.011 | 0.759 | 0.512 |
| J | 25 | 1.786 | 1.530 | 1.283 | 0.998 | 0.752 | 0.511 |
| K | 35 | 1.736 | 1.494 | 1.259 | 0.984 | 0.745 | 0.510 |
| L | 50 | 1.696 | 1.464 | 1.239 | 0.973 | 0.739 | 0.509 |

*The symbol "—" indicates that the plan is not available for this AQL.*

#### 3.2.4 Two-sided specifications

For two-sided specifications (lower limit $LSI$ and upper limit $LSS$), ISO 3951-1 offers two approaches:

**Combined method.** $Q_U$ and $Q_L$ are calculated separately and a specific table is used to verify that the estimated proportion of nonconforming items (upper and lower sides combined) does not exceed the AQL.

**Separate method.** The acceptance criterion is applied independently for each limit. This method is more conservative.

---

## 4. SPC control charts (ISO 7870, ASTM E2587)

Statistical process control (SPC) is a set of methods for monitoring a production process in real time using control charts. The objective is to distinguish variations due to common causes (inherent to the process, random) from those due to special causes (assignable, identifiable, and correctable).

### Fundamental principles (Shewhart)

Walter A. Shewhart introduced the concept of the control chart in the 1920s at Bell Laboratories. The principle is based on the following theorem: a process under statistical control exhibits only random variations, predictable by the laws of statistics. Any observation falling outside the control limits, or any non-random pattern in the data, signals a special cause that must be identified and eliminated.

A control chart comprises three horizontal lines:
- **UCL** (upper control limit): $CL + 3\sigma$.
- **CL** (center line): mean value of the monitored parameter.
- **LCL** (lower control limit): $CL - 3\sigma$.

The $\pm 3\sigma$ limits correspond to a false alarm probability of approximately 0.27% per point (i.e., approximately 1 point out of 370 outside the limits by chance alone, if the process is under control and the distribution is normal).

<!-- IMG:normal_distribution_3sigma.png -->

**Caution:** control limits are NOT specification limits. Control limits are calculated from the process data and reflect its natural variability. Specification limits are defined by the customer or the designer.

### ISO 7870-1 — general guide

ISO 7870-1 provides a general framework for the selection and use of control charts. It covers definitions, types of charts, application conditions, and guidelines for interpretation.

### ISO 7870-2 — control charts for variables and for attributes

ISO 7870-2 details the formulas, constants, and procedures for the main types of control charts.

---

### 4.1 Charts for variables

Charts for variables use data measured on a continuous scale (dimensions, masses, concentrations, etc.).

#### 4.1.1 $\bar{x}$ / R chart (mean and range)

This is the most widely used control chart for small subgroup sizes ($2 \leq n \leq 10$). It consists of two graphs:
- The $\bar{x}$ chart monitors the process location (mean).
- The $R$ chart monitors the process dispersion (range).

**Data collection.** $k$ subgroups of size $n$ are drawn. For each subgroup $j$:
- Mean: $\bar{x}_j = \frac{1}{n} \sum_{i=1}^{n} x_{ij}$
- Range: $R_j = x_{max,j} - x_{min,j}$

**Central parameter calculations:**
- Grand mean: $\bar{\bar{x}} = \frac{1}{k} \sum_{j=1}^{k} \bar{x}_j$
- Average range: $\bar{R} = \frac{1}{k} \sum_{j=1}^{k} R_j$

**Control limits for the $\bar{x}$ chart:**

$$UCL_{\bar{x}} = \bar{\bar{x}} + A_2 \bar{R}$$

$$CL_{\bar{x}} = \bar{\bar{x}}$$

$$LCL_{\bar{x}} = \bar{\bar{x}} - A_2 \bar{R}$$

**Control limits for the $R$ chart:**

$$UCL_R = D_4 \bar{R}$$

$$CL_R = \bar{R}$$

$$LCL_R = D_3 \bar{R}$$

**Within-subgroup standard deviation estimate:**

$$\hat{\sigma} = \frac{\bar{R}}{d_2}$$

**Constants table for the $\bar{x}$ / R chart ($n$ = 2 to 10):**

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

*Note: $D_3 = 0$ for $n \leq 6$ means that $LCL_R = 0$ (no lower limit on the R chart).*

**Numerical example.** Suppose $k = 25$ subgroups of size $n = 5$, with $\bar{\bar{x}} = 50{,}00$ mm and $\bar{R} = 0{,}40$ mm.

- $UCL_{\bar{x}} = 50{,}00 + 0{,}577 \times 0{,}40 = 50{,}231$ mm
- $LCL_{\bar{x}} = 50{,}00 - 0{,}577 \times 0{,}40 = 49{,}769$ mm
- $UCL_R = 2{,}114 \times 0{,}40 = 0{,}846$ mm
- $LCL_R = 0 \times 0{,}40 = 0$ mm
- $\hat{\sigma} = 0{,}40 / 2{,}326 = 0{,}172$ mm

<!-- IMG:control_chart_xbar.png -->

#### 4.1.2 $\bar{x}$ / S chart (mean and standard deviation)

The $\bar{x}$ / S chart is preferred when the subgroup size is large ($n \geq 10$), because the range $R$ becomes a less efficient estimator of dispersion for large subgroups. The standard deviation $s$ is then a more reliable estimator.

**Parameter calculations:**
- Standard deviation of subgroup $j$: $s_j = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_{ij} - \bar{x}_j)^2}$
- Average standard deviation: $\bar{S} = \frac{1}{k}\sum_{j=1}^{k} s_j$

**Control limits for the $\bar{x}$ chart:**

$$UCL_{\bar{x}} = \bar{\bar{x}} + A_3 \bar{S}$$

$$CL_{\bar{x}} = \bar{\bar{x}}$$

$$LCL_{\bar{x}} = \bar{\bar{x}} - A_3 \bar{S}$$

**Control limits for the $S$ chart:**

$$UCL_S = B_4 \bar{S}$$

$$CL_S = \bar{S}$$

$$LCL_S = B_3 \bar{S}$$

**Within-subgroup standard deviation estimate:**

$$\hat{\sigma} = \frac{\bar{S}}{c_4}$$

**Constants table for the $\bar{x}$ / S chart ($n$ = 2 to 25):**

| $n$ | $A_3$ | $B_3$ | $B_4$ | $c_4$ |
|---|---|---|---|---|
| 2 | 2.659 | 0 | 3.267 | 0.7979 |
| 3 | 1.954 | 0 | 2.568 | 0.8862 |
| 4 | 1.628 | 0 | 2.266 | 0.9213 |
| 5 | 1.427 | 0 | 2.089 | 0.9400 |
| 6 | 1.287 | 0.030 | 1.970 | 0.9515 |
| 7 | 1.182 | 0.118 | 1.882 | 0.9594 |
| 8 | 1.099 | 0.185 | 1.815 | 0.9650 |
| 9 | 1.032 | 0.239 | 1.761 | 0.9693 |
| 10 | 0.975 | 0.284 | 1.716 | 0.9727 |
| 11 | 0.927 | 0.321 | 1.679 | 0.9754 |
| 12 | 0.886 | 0.354 | 1.646 | 0.9776 |
| 13 | 0.850 | 0.382 | 1.618 | 0.9794 |
| 14 | 0.817 | 0.406 | 1.594 | 0.9810 |
| 15 | 0.789 | 0.428 | 1.572 | 0.9823 |
| 16 | 0.763 | 0.448 | 1.552 | 0.9835 |
| 17 | 0.739 | 0.466 | 1.534 | 0.9845 |
| 18 | 0.718 | 0.482 | 1.518 | 0.9854 |
| 19 | 0.698 | 0.497 | 1.503 | 0.9862 |
| 20 | 0.680 | 0.510 | 1.490 | 0.9869 |
| 21 | 0.663 | 0.523 | 1.477 | 0.9876 |
| 22 | 0.647 | 0.534 | 1.466 | 0.9882 |
| 23 | 0.633 | 0.545 | 1.455 | 0.9887 |
| 24 | 0.619 | 0.555 | 1.445 | 0.9892 |
| 25 | 0.606 | 0.565 | 1.435 | 0.9896 |

#### 4.1.3 I-MR chart (individual and moving range)

The I-MR (Individual - Moving Range) chart is used when data are collected one at a time ($n = 1$), for example when:
- Production is very slow (one part per hour or per day).
- Measurements are costly or destructive.
- Each measurement represents a lot or a batch.
- The data are homogeneous (no natural subgroups).

**Parameter calculations:**
- Mean: $\bar{X} = \frac{1}{k}\sum_{j=1}^{k} x_j$
- Moving range: $MR_j = |x_j - x_{j-1}|$ for $j = 2, 3, \ldots, k$
- Average moving range: $\bar{MR} = \frac{1}{k-1}\sum_{j=2}^{k} MR_j$

**Control limits for the I (individual) chart:**

$$UCL_X = \bar{X} + 2{,}66 \, \bar{MR}$$

$$CL_X = \bar{X}$$

$$LCL_X = \bar{X} - 2{,}66 \, \bar{MR}$$

The coefficient $2{,}66 = 3 / d_2 = 3 / 1{,}128$ comes from the relationship between the moving range (calculated on consecutive pairs, $n = 2$) and the standard deviation.

**Control limits for the MR chart:**

$$UCL_{MR} = D_4 \, \bar{MR} = 3{,}267 \, \bar{MR}$$

$$CL_{MR} = \bar{MR}$$

$$LCL_{MR} = D_3 \, \bar{MR} = 0$$

The constants used are those for $n = 2$ because the moving range is calculated on pairs of consecutive values: $d_2 = 1{,}128$, $D_3 = 0$, $D_4 = 3{,}267$.

**Standard deviation estimate:**

$$\hat{\sigma} = \frac{\bar{MR}}{d_2} = \frac{\bar{MR}}{1{,}128}$$

**Important:** the I-MR chart is sensitive to departures from normality. If the data do not follow an approximately normal distribution, the control limits may be misleading. It is recommended to verify normality (section 7) before using this chart.

**Numerical example.** The pH of a surface treatment bath is measured daily. Over 20 days, we obtain $\bar{X} = 4{,}50$ and $\bar{MR} = 0{,}15$.

- $UCL_X = 4{,}50 + 2{,}66 \times 0{,}15 = 4{,}899$
- $LCL_X = 4{,}50 - 2{,}66 \times 0{,}15 = 4{,}101$
- $UCL_{MR} = 3{,}267 \times 0{,}15 = 0{,}490$
- $\hat{\sigma} = 0{,}15 / 1{,}128 = 0{,}133$

#### 4.1.4 Study phase and monitoring phase

The implementation of a control chart takes place in two distinct phases.

**Phase 1 — study (retrospective).** Historical data are collected (at least 25 subgroups according to ISO 7870-2, clause 7.2). Provisional control limits are calculated and it is verified that no point is out of control. If out-of-control points are identified:
1. Search for the special cause.
2. If the cause is found and eliminated, remove the subgroup and recalculate the limits.
3. Repeat until the process is under control.

The final Phase 1 limits become the reference limits for Phase 2.

**Phase 2 — monitoring (prospective).** The limits calculated in Phase 1 are used to monitor production in real time. Each new point is plotted and evaluated. The Western Electric / Nelson rules (section 4.3) are applied. The limits are recalculated only if the process has been intentionally modified (new setting, new material, improvement).

#### 4.1.5 Choosing between charts for variables

| Criterion | $\bar{x}$ / R | $\bar{x}$ / S | I-MR |
|---|---|---|---|
| Subgroup size | $2 \leq n \leq 9$ | $n \geq 10$ | $n = 1$ |
| Estimation of $\sigma$ | $\bar{R}/d_2$ | $\bar{S}/c_4$ | $\bar{MR}/d_2$ ($n=2$) |
| Statistical efficiency | Good for small $n$. | Better for large $n$. | Less efficient (no subgroups). |
| Sensitivity to outliers | Moderate. | More robust. | High (single point per subgroup). |
| Normality assumption | Robust (central limit theorem). | Robust (central limit theorem). | Sensitive (no averaging). |
| Complexity | Simple. | Moderate. | Simple. |

#### 4.1.6 Estimation of $\sigma$ — comparison of methods

The within-subgroup standard deviation estimate $\hat{\sigma}$ can be obtained in three ways:

| Method | Formula | Associated chart | Bias |
|---|---|---|---|
| Average range | $\hat{\sigma} = \bar{R} / d_2$ | $\bar{x}$ / R | Unbiased (corrected by $d_2$). |
| Average standard deviation | $\hat{\sigma} = \bar{S} / c_4$ | $\bar{x}$ / S | Unbiased (corrected by $c_4$). |
| Moving range | $\hat{\sigma} = \bar{MR} / d_2$ ($n=2$) | I-MR | Unbiased (corrected by $d_2$). |
| Pooled standard deviation | $\hat{\sigma} = S_p = \sqrt{\frac{\sum(n_j-1)s_j^2}{\sum(n_j-1)}}$ | Alternative | Unbiased, most efficient estimator. |

---

### 4.2 Charts for attributes

Charts for attributes use discrete data (number or proportion of nonconforming items, number of defects, etc.).

#### 4.2.1 $p$ chart (fraction nonconforming)

The $p$ chart monitors the fraction of nonconforming parts in samples that may be of variable size. It is based on the binomial distribution.

**Central parameter:**

$$\bar{p} = \frac{\sum_{j=1}^{k} d_j}{\sum_{j=1}^{k} n_j}$$

where $d_j$ is the number of nonconforming items in subgroup $j$ of size $n_j$.

**Control limits:**

$$UCL_p = \bar{p} + 3\sqrt{\frac{\bar{p}(1 - \bar{p})}{n}}$$

$$CL_p = \bar{p}$$

$$LCL_p = \bar{p} - 3\sqrt{\frac{\bar{p}(1 - \bar{p})}{n}}$$

If $LCL_p < 0$, set $LCL_p = 0$. When sample sizes vary, the control limits are recalculated for each subgroup.

**Application condition:** $n\bar{p} \geq 5$ and $n(1 - \bar{p}) \geq 5$ for the normal approximation to be valid.

#### 4.2.2 $np$ chart (number of nonconforming items)

The $np$ chart monitors the number of nonconforming parts in samples of **constant size** $n$. It is a variant of the $p$ chart that is easier to interpret.

**Control limits:**

$$UCL_{np} = n\bar{p} + 3\sqrt{n\bar{p}(1 - \bar{p})}$$

$$CL_{np} = n\bar{p}$$

$$LCL_{np} = n\bar{p} - 3\sqrt{n\bar{p}(1 - \bar{p})}$$

If $LCL_{np} < 0$, set $LCL_{np} = 0$.

#### 4.2.3 $c$ chart (number of nonconformities)

The $c$ chart monitors the total number of nonconformities (defects) in an inspection unit of constant size. It is based on the Poisson distribution.

**Central parameter:**

$$\bar{c} = \frac{\sum_{j=1}^{k} c_j}{k}$$

**Control limits:**

$$UCL_c = \bar{c} + 3\sqrt{\bar{c}}$$

$$CL_c = \bar{c}$$

$$LCL_c = \bar{c} - 3\sqrt{\bar{c}}$$

If $LCL_c < 0$, set $LCL_c = 0$.

**Example.** The number of defective solder joints on electronic circuit boards is counted. If $\bar{c} = 4{,}0$:
- $UCL_c = 4{,}0 + 3\sqrt{4{,}0} = 4{,}0 + 6{,}0 = 10{,}0$
- $LCL_c = 4{,}0 - 6{,}0 = -2{,}0 \rightarrow 0$

#### 4.2.4 $u$ chart (nonconformities per unit rate)

The $u$ chart monitors the number of nonconformities per inspection unit. It is used when the size of inspection units varies.

**Central parameter:**

$$\bar{u} = \frac{\sum_{j=1}^{k} c_j}{\sum_{j=1}^{k} n_j}$$

**Control limits:**

$$UCL_u = \bar{u} + 3\sqrt{\frac{\bar{u}}{n}}$$

$$CL_u = \bar{u}$$

$$LCL_u = \bar{u} - 3\sqrt{\frac{\bar{u}}{n}}$$

If $LCL_u < 0$, set $LCL_u = 0$. When the size $n$ varies, the limits are recalculated for each subgroup.

**Summary table for attribute charts:**

| Chart | Monitored data | Sample size | Distribution | UCL formula |
|---|---|---|---|---|
| $p$ | Fraction nonconforming | Variable or constant | Binomial | $\bar{p} + 3\sqrt{\bar{p}(1-\bar{p})/n}$ |
| $np$ | Number of nonconforming items | Constant | Binomial | $n\bar{p} + 3\sqrt{n\bar{p}(1-\bar{p})}$ |
| $c$ | Number of nonconformities | Constant | Poisson | $\bar{c} + 3\sqrt{\bar{c}}$ |
| $u$ | Nonconformities per unit rate | Variable or constant | Poisson | $\bar{u} + 3\sqrt{\bar{u}/n}$ |

---

### 4.3 Western Electric / Nelson rules

The $\pm 3\sigma$ control limits constitute the basic Shewhart rule. However, the Shewhart chart alone is not very sensitive to small mean shifts. The supplementary Western Electric (WECO, 1956) and Nelson (1984) rules increase sensitivity by detecting non-random patterns in the data, even if no point exceeds the control limits.

To apply these rules, the zone between the control limits is divided into three bands on each side of the center line:
- **Zone A**: between $2\sigma$ and $3\sigma$ from the center line.
- **Zone B**: between $1\sigma$ and $2\sigma$ from the center line.
- **Zone C**: between the center line and $1\sigma$.

#### Rule 1 — one point beyond 3$\sigma$

**Description:** a single point falls beyond the upper or lower control limit (outside Zone A).

**Signal:** obvious special cause, major isolated event.

**False alarm probability:** 0.27% per point.

#### Rule 2 — 9 consecutive points on the same side of the center line

**Description:** nine consecutive points all fall above or all below the center line.

**Signal:** sustained shift of the process mean.

**False alarm probability:** $(0{,}5)^9 = 0{,}195\%$ per sequence of 9.

#### Rule 3 — 6 consecutive points in monotone increase or decrease

**Description:** six consecutive points show a strictly increasing or strictly decreasing trend.

**Signal:** progressive process drift (tool wear, temperature drift, etc.).

#### Rule 4 — 14 consecutive points alternating up and down

**Description:** fourteen consecutive points alternate going up and down in a regular pattern.

**Signal:** overcontrol of the process, or two alternating sources of variation (for example, two machines alternating production).

#### Rule 5 — 2 out of 3 points beyond 2$\sigma$ (same side)

**Description:** two out of three consecutive points fall in Zone A (between $2\sigma$ and $3\sigma$) on the same side of the center line.

**Signal:** temporary increase in variability or momentary mean shift.

#### Rule 6 — 4 out of 5 points beyond 1$\sigma$ (same side)

**Description:** four out of five consecutive points fall beyond $1\sigma$ (in Zones A or B) on the same side of the center line.

**Signal:** moderate mean shift.

#### Rule 7 — 15 consecutive points in Zone C (stratification)

**Description:** fifteen consecutive points all fall in Zone C (between the center line and $1\sigma$), on either side of the center line.

**Signal:** stratification — the data come from mixed sources whose means are close, or the control limits are too wide.

#### Rule 8 — 8 consecutive points beyond 1$\sigma$ (mixture)

**Description:** eight consecutive points all fall beyond $1\sigma$ from the center line (in Zones A or B), on either side.

**Signal:** mixture — the data come from two different distributions (two machines, two operators, two raw material lots).

**Summary table of Western Electric / Nelson rules:**

| Rule | Description | Typical signal |
|---|---|---|
| 1 | 1 point beyond $3\sigma$ | Isolated special cause. |
| 2 | 9 points on the same side of CL | Mean shift. |
| 3 | 6 points in monotone trend | Progressive drift. |
| 4 | 14 points alternating up/down | Overcontrol or alternating sources. |
| 5 | 2 out of 3 beyond $2\sigma$ (same side) | Shift or temporary instability. |
| 6 | 4 out of 5 beyond $1\sigma$ (same side) | Moderate mean shift. |
| 7 | 15 points in Zone C | Stratification (limits too wide). |
| 8 | 8 points beyond $1\sigma$ (both sides) | Mixture of distributions. |

**Practical recommendation.** In production, it is common to apply only rules 1 through 4 (or even only rule 1) to limit false alarms. Applying all rules simultaneously increases the false alarm rate to approximately 2 to 4% per point, compared to 0.27% for rule 1 alone. The choice of rules depends on the cost of a false alarm relative to the cost of an undetected defect.

**Sensitivity to mean shifts.** The Shewhart chart with rule 1 alone detects a $1{,}5\sigma$ shift on average after 6 to 7 subgroups (ARL $\approx 6{,}3$). Adding supplementary rules reduces the ARL to approximately 2 to 3 subgroups for the same shift. For even faster detection of small shifts, CUSUM (cumulative sum) or EWMA (exponentially weighted moving average) charts can be used, described in ISO 7870-4 and ISO 7870-6 respectively.

---

### 4.4 Complete SPC constants table

The following table consolidates the reference SPC constants for subgroup sizes $n$ ranging from 2 to 25. These constants are used to construct $\bar{x}$/R, $\bar{x}$/S, and I-MR charts.

**Constant definitions:**
- $A_2$: factor for $\bar{x}$ chart limits based on $\bar{R}$.
- $A_3$: factor for $\bar{x}$ chart limits based on $\bar{S}$.
- $B_3$: factor for the lower limit of the $S$ chart.
- $B_4$: factor for the upper limit of the $S$ chart.
- $D_3$: factor for the lower limit of the $R$ chart.
- $D_4$: factor for the upper limit of the $R$ chart.
- $d_2$: conversion factor from range to standard deviation ($\hat{\sigma} = \bar{R}/d_2$).
- $c_4$: bias correction factor for the standard deviation ($\hat{\sigma} = \bar{S}/c_4$).

| $n$ | $A_2$ | $A_3$ | $B_3$ | $B_4$ | $D_3$ | $D_4$ | $d_2$ | $c_4$ |
|---|---|---|---|---|---|---|---|---|
| 2 | 1.880 | 2.659 | 0 | 3.267 | 0 | 3.267 | 1.128 | 0.7979 |
| 3 | 1.023 | 1.954 | 0 | 2.568 | 0 | 2.574 | 1.693 | 0.8862 |
| 4 | 0.729 | 1.628 | 0 | 2.266 | 0 | 2.282 | 2.059 | 0.9213 |
| 5 | 0.577 | 1.427 | 0 | 2.089 | 0 | 2.114 | 2.326 | 0.9400 |
| 6 | 0.483 | 1.287 | 0.030 | 1.970 | 0 | 2.004 | 2.534 | 0.9515 |
| 7 | 0.419 | 1.182 | 0.118 | 1.882 | 0.076 | 1.924 | 2.704 | 0.9594 |
| 8 | 0.373 | 1.099 | 0.185 | 1.815 | 0.136 | 1.864 | 2.847 | 0.9650 |
| 9 | 0.337 | 1.032 | 0.239 | 1.761 | 0.184 | 1.816 | 2.970 | 0.9693 |
| 10 | 0.308 | 0.975 | 0.284 | 1.716 | 0.223 | 1.777 | 3.078 | 0.9727 |
| 11 | 0.285 | 0.927 | 0.321 | 1.679 | 0.256 | 1.744 | 3.173 | 0.9754 |
| 12 | 0.266 | 0.886 | 0.354 | 1.646 | 0.283 | 1.717 | 3.258 | 0.9776 |
| 13 | 0.249 | 0.850 | 0.382 | 1.618 | 0.307 | 1.693 | 3.336 | 0.9794 |
| 14 | 0.235 | 0.817 | 0.406 | 1.594 | 0.328 | 1.672 | 3.407 | 0.9810 |
| 15 | 0.223 | 0.789 | 0.428 | 1.572 | 0.347 | 1.653 | 3.472 | 0.9823 |
| 16 | 0.212 | 0.763 | 0.448 | 1.552 | 0.363 | 1.637 | 3.532 | 0.9835 |
| 17 | 0.203 | 0.739 | 0.466 | 1.534 | 0.378 | 1.622 | 3.588 | 0.9845 |
| 18 | 0.194 | 0.718 | 0.482 | 1.518 | 0.391 | 1.608 | 3.640 | 0.9854 |
| 19 | 0.187 | 0.698 | 0.497 | 1.503 | 0.403 | 1.597 | 3.689 | 0.9862 |
| 20 | 0.180 | 0.680 | 0.510 | 1.490 | 0.415 | 1.585 | 3.735 | 0.9869 |
| 21 | 0.173 | 0.663 | 0.523 | 1.477 | 0.425 | 1.575 | 3.778 | 0.9876 |
| 22 | 0.167 | 0.647 | 0.534 | 1.466 | 0.434 | 1.566 | 3.819 | 0.9882 |
| 23 | 0.162 | 0.633 | 0.545 | 1.455 | 0.443 | 1.557 | 3.858 | 0.9887 |
| 24 | 0.157 | 0.619 | 0.555 | 1.445 | 0.451 | 1.548 | 3.895 | 0.9892 |
| 25 | 0.153 | 0.606 | 0.565 | 1.435 | 0.459 | 1.541 | 3.931 | 0.9896 |

**Fundamental relationships between constants:**

- $A_2 = 3 / (d_2 \sqrt{n})$: relates $\bar{x}$ limits to the average range.
- $A_3 = 3 / (c_4 \sqrt{n})$: relates $\bar{x}$ limits to the average standard deviation.
- $D_3 = 1 - 3 d_3 / d_2$ and $D_4 = 1 + 3 d_3 / d_2$: R chart limits ($d_3$ is the standard deviation of the relative range).
- $B_3 = 1 - 3\sqrt{1 - c_4^2}/c_4$ and $B_4 = 1 + 3\sqrt{1 - c_4^2}/c_4$: S chart limits.

---

## 5. Process capability (ISO 22514)

Process capability measures the ability of a process to produce results that conform to specifications. It compares the natural process spread to the specified tolerance interval.

### 5.1 ISO 22514-1 — general concepts

ISO 22514-1 defines the basic terms and concepts related to capability. It distinguishes:
- **Machine capability**: short-term performance under controlled conditions (same operator, same material, same setting).
- **Process capability**: long-term performance including all sources of variation (operator changes, material changes, setting changes, etc.).

### 5.2 ISO 22514-2 — machine and process capability

#### 5.2.1 Short-term capability indices ($C_p$, $C_{pk}$)

These indices use the within-subgroup standard deviation $\sigma$ estimated from control charts (short-term variation, within-subgroup).

**Potential capability index $C_p$:**

$$C_p = \frac{LSS - LSI}{6\sigma}$$

$C_p$ compares the tolerance width to the process spread. It does not account for process centering.

**Actual capability index $C_{pk}$:**

$$C_{pk} = \min\left(\frac{LSS - \bar{x}}{3\sigma}, \frac{\bar{x} - LSI}{3\sigma}\right)$$

$C_{pk}$ accounts for centering. If the process is perfectly centered, $C_{pk} = C_p$. Otherwise, $C_{pk} < C_p$.

<!-- IMG:capability_cp_cpk.png -->

#### 5.2.2 Long-term performance indices ($P_p$, $P_{pk}$)

These indices use the total standard deviation $s$ calculated from all individual data (total variation, overall).

**Potential performance index $P_p$:**

$$P_p = \frac{LSS - LSI}{6s}$$

**Actual performance index $P_{pk}$:**

$$P_{pk} = \min\left(\frac{LSS - \bar{x}}{3s}, \frac{\bar{x} - LSI}{3s}\right)$$

#### 5.2.3 Difference between $\sigma$ (within-subgroup) and $s$ (total)

| Parameter | Symbol | Estimation | Source of variation |
|---|---|---|---|
| Within-subgroup standard deviation | $\sigma$ | $\hat{\sigma} = \bar{R}/d_2$ or $\bar{S}/c_4$ | Short-term variation only (within subgroups). |
| Total standard deviation | $s$ | $s = \sqrt{\frac{1}{N-1}\sum(x_i - \bar{x})^2}$ | Total variation including between-subgroup variations. |

In general, $s \geq \sigma$, and therefore $P_p \leq C_p$ and $P_{pk} \leq C_{pk}$. A significant gap between capability and performance indices indicates the presence of between-subgroup variation sources (mean shifts, operator effects, etc.).

#### 5.2.4 Interpretation of capability indices

| $C_{pk}$ (or $P_{pk}$) | Interpretation | PPM out of tolerance (one tail) | Recommended action |
|---|---|---|---|
| $< 0{,}67$ | Highly incapable | $> 22750$ | Immediate action required. |
| $0{,}67$ to $1{,}00$ | Incapable | $2700$ to $22750$ | Urgent improvement. |
| $1{,}00$ to $1{,}33$ | Marginal | $63$ to $2700$ | Improvement desired. |
| $1{,}33$ to $1{,}67$ | Capable | $0{,}6$ to $63$ | Acceptable for most applications. |
| $1{,}67$ to $2{,}00$ | Highly capable | $< 0{,}6$ | Excellent. |
| $> 2{,}00$ | World class | $< 0{,}001$ | Exceptional (Six Sigma target). |

#### 5.2.5 PPM table as a function of $C_{pk}$

The following table gives the number of parts per million (PPM) out of tolerance for a centered and normally distributed process as a function of $C_{pk}$:

| $C_{pk}$ | Total PPM (both sides) | Sigma level |
|---|---|---|
| 0.33 | 317310 | 1$\sigma$ |
| 0.50 | 133614 | 1.5$\sigma$ |
| 0.67 | 45500 | 2$\sigma$ |
| 0.83 | 12419 | 2.5$\sigma$ |
| 1.00 | 2700 | 3$\sigma$ |
| 1.17 | 467 | 3.5$\sigma$ |
| 1.33 | 63 | 4$\sigma$ |
| 1.50 | 6.8 | 4.5$\sigma$ |
| 1.67 | 0.57 | 5$\sigma$ |
| 2.00 | 0.002 | 6$\sigma$ |

*Note: these values assume a perfectly centered and normally distributed process. The 1.5$\sigma$ shift often mentioned in the Six Sigma approach is NOT taken into account here.*

#### 5.2.6 Numerical example of capability calculation

A machining process produces shafts whose diameter must be between $LSI = 9{,}95$ mm and $LSS = 10{,}05$ mm ($T = 0{,}10$ mm). Over 30 subgroups of size $n = 5$, we obtain:
- $\bar{\bar{x}} = 10{,}005$ mm
- $\hat{\sigma} = \bar{R}/d_2 = 0{,}012$ mm (within-subgroup standard deviation)
- $s = 0{,}015$ mm (total standard deviation)

**Short-term indices:**
- $C_p = \frac{0{,}10}{6 \times 0{,}012} = 1{,}39$
- $C_{pk} = \min\left(\frac{10{,}05 - 10{,}005}{3 \times 0{,}012}, \frac{10{,}005 - 9{,}95}{3 \times 0{,}012}\right) = \min(1{,}25 ; 1{,}53) = 1{,}25$

**Long-term indices:**
- $P_p = \frac{0{,}10}{6 \times 0{,}015} = 1{,}11$
- $P_{pk} = \min\left(\frac{10{,}05 - 10{,}005}{3 \times 0{,}015}, \frac{10{,}005 - 9{,}95}{3 \times 0{,}015}\right) = \min(1{,}00 ; 1{,}22) = 1{,}00$

**Interpretation:** the short-term capability ($C_{pk} = 1{,}25$) is close to the acceptable threshold ($1{,}33$) but is not reached. The process off-centering ($\bar{x} = 10{,}005$ vs target $= 10{,}00$) reduces $C_{pk}$ relative to $C_p$. The long-term performance ($P_{pk} = 1{,}00$) is marginal. The gap between $C_{pk}$ and $P_{pk}$ reveals between-subgroup variation sources.

**Recommended actions:**
1. Recenter the process on the target value (reduce the 0.005 mm bias).
2. Identify and reduce between-subgroup variation sources.
3. Aim for $C_{pk} \geq 1{,}33$ and $P_{pk} \geq 1{,}33$.

#### 5.2.7 Prerequisites for capability calculation

Before calculating capability indices, the following must be verified:
1. The process is **under statistical control** (no special cause detected on the control chart).
2. The data follow an **approximately normal** distribution (normality test, section 7).
3. The **measurement system** is adequate (acceptable GRR, section 6).
4. The data are sufficient in number (at least 25 subgroups, ISO 22514-2, clause 6).

---

## 6. Measurement system capability (ISO 22514-7)

ISO 22514-7 defines methods for evaluating measurement system capability. An inadequate measurement system can mask the true process variations or generate false alarms on control charts.

### 6.1 $C_g$ and $C_{gk}$ indices

The $C_g$ and $C_{gk}$ indices evaluate the measurement system capability by comparing its repeatability to the product tolerance.

**$C_g$ index (gage capability):**

$$C_g = \frac{0{,}2 \times T}{6 s_g}$$

where:
- $T = LSS - LSI$ is the tolerance interval.
- $s_g$ is the repeatability standard deviation (obtained by measuring the same reference part $n$ times with the same operator, the same instrument, under the same conditions).

The factor $0{,}2$ means that only 20% of the total tolerance is allocated to the measurement system. A $C_g \geq 1{,}33$ is required.

**$C_{gk}$ index (gage capability with bias):**

$$C_{gk} = \frac{0{,}1 \times T - |x_m - \bar{x}|}{3 s_g}$$

where:
- $x_m$ is the reference value (certified value of the reference part).
- $\bar{x}$ is the mean of the repeated measurements.
- $|x_m - \bar{x}|$ is the measurement system bias.

A $C_{gk} \geq 1{,}33$ is required. If $C_g$ is acceptable but $C_{gk}$ is not, the system has a significant bias that must be corrected.

### 6.2 GRR study (Gage Repeatability and Reproducibility)

The GRR study decomposes the total measurement system variability into two components:

**Repeatability (EV — Equipment Variation):** variation observed when the same operator measures the same part multiple times with the same instrument.

$$EV = \bar{R}_{operators} / d_2$$

**Reproducibility (AV — Appraiser Variation):** variation observed between different operators measuring the same parts.

$$AV = \sqrt{\left(\frac{\bar{R}_{parts \, by \, operator}}{d_2}\right)^2 - \frac{EV^2}{n \times r}}$$

where $n$ is the number of parts and $r$ is the number of repetitions.

If the term under the square root is negative, $AV = 0$.

**Combined GRR:**

$$GRR = \sqrt{EV^2 + AV^2}$$

**Part Variation (PV):**

$$PV = \frac{R_{parts}}{d_2}$$

**Total Variation (TV):**

$$TV = \sqrt{GRR^2 + PV^2}$$

**GRR percentage:**

$$\%GRR = \frac{GRR}{TV} \times 100$$

#### 6.2.1 Interpretation of %GRR

| %GRR | Interpretation | Action |
|---|---|---|
| $< 10\%$ | Acceptable measurement system. | No action necessary. |
| $10\%$ to $30\%$ | Marginal system. | Acceptable depending on application and cost. |
| $> 30\%$ | Unacceptable system. | Improvement required before use. |

<!-- IMG:grr_variance_components.png -->

#### 6.2.2 Number of distinct categories (ndc)

The number of distinct categories is an additional indicator of measurement system discrimination:

$$ndc = 1{,}41 \times \frac{PV}{GRR}$$

The result is rounded down to the nearest integer. An $ndc \geq 5$ is required for an acceptable measurement system. This means the system can distinguish at least 5 distinct groups among the measured parts.

### 6.3 Typical procedure for a GRR study

1. Select 10 parts covering the production range.
2. Identify 2 to 3 operators.
3. Each operator measures each part 2 to 3 times (random order, blind).
4. Calculate EV, AV, GRR, PV, TV, %GRR, and ndc.
5. Conclude on the acceptability of the measurement system.

---

## 7. Normality tests (ISO 5479)

Many statistical methods (control charts, capability, tolerance intervals) assume that the data follow a normal distribution. ISO 5479 provides methods to verify this assumption.

### 7.1 Why normality matters

The consequences of undetected non-normality can be serious:
- The **control limits** of $\bar{x}$ charts are relatively robust (thanks to the central limit theorem), but the R, S, and I-MR charts are sensitive to non-normality.
- The **capability indices** $C_p$ and $C_{pk}$ assume normality. On non-normal data, the estimated PPM can be very far from reality.
- The **parametric tolerance intervals** of ISO 16269-6 assume normality.

### 7.2 Shapiro-Wilk test

The Shapiro-Wilk test is considered the most powerful normality test for small samples ($n < 50$, although it can be extended up to $n = 5000$).

**Hypotheses:**
- $H_0$: the data come from a normal distribution.
- $H_1$: the data do not come from a normal distribution.

**Test statistic $W$:**

$$W = \frac{\left(\sum_{i=1}^{m} a_i (x_{(n+1-i)} - x_{(i)})\right)^2}{\sum_{i=1}^{n}(x_i - \bar{x})^2}$$

where $x_{(i)}$ are the order statistics (sorted data), $a_i$ are tabulated coefficients that depend on $n$, and $m = n/2$ (rounded down to the nearest integer).

**Interpretation:** $W$ ranges between 0 and 1. The closer $W$ is to 1, the more the normality assumption is supported. $H_0$ is rejected if $W < W_{critical}$ (or if the $p$-value $< \alpha$, typically $\alpha = 0{,}05$).

**Limitations:** the Shapiro-Wilk test is very powerful but may reject normality for minor deviations on large samples. It is recommended to combine the test result with a graphical analysis (Q-Q plot).

### 7.3 Anderson-Darling test

The Anderson-Darling test is particularly sensitive to deviations in the distribution tails, which is relevant for capability and PPM calculations.

**Test statistic $A^2$:**

$$A^2 = -n - \frac{1}{n}\sum_{i=1}^{n}(2i - 1)\left[\ln(F(x_{(i)})) + \ln(1 - F(x_{(n+1-i)}))\right]$$

where $F$ is the cumulative distribution function of the standard normal distribution and $x_{(i)}$ are the sorted standardized data.

**Corrected statistic:**

$$A^{*2} = A^2 \left(1 + \frac{0{,}75}{n} + \frac{2{,}25}{n^2}\right)$$

**Interpretation:** $H_0$ is rejected if $A^{*2}$ exceeds the critical value. For a significance level $\alpha = 0{,}05$, the critical value is approximately $0{,}752$.

| Level $\alpha$ | Critical value $A^{*2}$ |
|---|---|
| 0.15 | 0.576 |
| 0.10 | 0.656 |
| 0.05 | 0.752 |
| 0.025 | 0.873 |
| 0.01 | 1.035 |

### 7.4 Kolmogorov-Smirnov test

The Kolmogorov-Smirnov (KS) test compares the empirical cumulative distribution function $F_n(x)$ to the theoretical cumulative distribution function $F_0(x)$ of the normal distribution.

**Test statistic $D$:**

$$D = \max_{i} \left| F_n(x_{(i)}) - F_0(x_{(i)}) \right|$$

where $F_n(x_{(i)}) = i/n$ is the empirical cumulative frequency.

**Critical values (Lilliefors test for normality with estimated parameters):**

| $n$ | $\alpha = 0{,}20$ | $\alpha = 0{,}15$ | $\alpha = 0{,}10$ | $\alpha = 0{,}05$ | $\alpha = 0{,}01$ |
|---|---|---|---|---|---|
| 5 | 0.289 | 0.303 | 0.319 | 0.337 | 0.405 |
| 10 | 0.214 | 0.224 | 0.239 | 0.258 | 0.294 |
| 15 | 0.178 | 0.187 | 0.201 | 0.220 | 0.257 |
| 20 | 0.155 | 0.164 | 0.178 | 0.195 | 0.231 |
| 25 | 0.140 | 0.148 | 0.162 | 0.177 | 0.211 |
| 30 | 0.128 | 0.136 | 0.149 | 0.163 | 0.196 |
| 50 | 0.100 | 0.106 | 0.117 | 0.130 | 0.157 |
| 100 | 0.071 | 0.076 | 0.084 | 0.093 | 0.114 |

*Note: when the parameters $\mu$ and $\sigma$ are estimated from the data, Lilliefors tables must be used (not the classical KS tables).*

### 7.5 Q-Q plot (quantile-quantile)

The Q-Q plot is a graphical tool that compares the observed quantiles to the theoretical quantiles of the normal distribution. If the data are normal, the points align approximately on a straight line.

**Construction:**
1. Sort the data: $x_{(1)} \leq x_{(2)} \leq \ldots \leq x_{(n)}$.
2. Calculate cumulative frequencies: $p_i = (i - 0{,}375) / (n + 0{,}25)$ (Blom's formula).
3. Calculate theoretical quantiles: $z_i = \Phi^{-1}(p_i)$.
4. Plot $x_{(i)}$ on the y-axis against $z_i$ on the x-axis.

**Pattern interpretation:**
- Linear alignment: normality confirmed.
- S-shaped curvature: skewness.
- Deviating extremes: heavy tails (kurtosis) or outliers.
- Stepped points: discrete or rounded data.

<!-- IMG:qqplot_comparison.png -->

### 7.6 Comparative table of normality tests

| Test | Sample size | Primary sensitivity | Overall power | Recommended use |
|---|---|---|---|---|
| Shapiro-Wilk | $3 \leq n \leq 5000$ | Center and tails. | Very high. | Reference test for $n < 50$. |
| Anderson-Darling | $n \geq 8$ | Distribution tails. | High. | Complement for PPM calculations. |
| Kolmogorov-Smirnov (Lilliefors) | $n \geq 5$ | Center of distribution. | Moderate. | When other tests are not available. |
| Q-Q plot | Any $n$ | Overall visual diagnostic. | — | Always as a complement to a formal test. |

**Practical recommendation.** Use the Shapiro-Wilk test as the primary test, complemented by the Q-Q plot for visual interpretation. For applications where distribution tails are critical (PPM calculation, capability), add the Anderson-Darling test.

---

## 8. Comparison of populations — tests and ANOVA (ISO 5725, ASTM E691)

In industrial quality, it is common to compare populations: do two machines produce parts with the same average dimension? Do three operators achieve the same measurement dispersion? Has a supplier change affected process performance? This section covers the main parametric comparison tests used to answer these questions.

The general approach is always the same: formulate a null hypothesis $H_0$ (no difference), choose a significance level $\alpha$ (typically 0.05), compute a test statistic from the data, and compare it to a critical value or compute a p-value. If the test statistic exceeds the critical threshold, $H_0$ is rejected and the difference is declared statistically significant.

### 8.1 Comparing two means — Student's t-test

Student's t-test is the fundamental parametric test for comparing means. It assumes that the underlying populations are approximately normally distributed. For large samples ($n > 30$), the test is robust to moderate departures from normality thanks to the central limit theorem.

#### 8.1.1 One-sample t-test

The one-sample t-test compares the mean of a sample to a known reference value $\mu_0$ (for example, a nominal specification).

**Hypotheses:**
- $H_0$: $\mu = \mu_0$ (the population mean equals the reference value).
- $H_1$: $\mu \neq \mu_0$ (two-sided test).

**Test statistic:**

$$t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}$$

where $\bar{x}$ is the sample mean, $s$ is the sample standard deviation, and $n$ is the sample size. Under $H_0$, $t$ follows a Student distribution with $\nu = n - 1$ degrees of freedom.

**Decision rule:** reject $H_0$ if $|t| > t_{\alpha/2, n-1}$.

**Numerical example.** A process is supposed to produce rods with a nominal diameter of 10.00 mm. A sample of $n = 15$ rods gives $\bar{x} = 10.03$ mm and $s = 0.05$ mm.

$$t = \frac{10.03 - 10.00}{0.05 / \sqrt{15}} = \frac{0.03}{0.0129} = 2.32$$

With $\nu = 14$ degrees of freedom, $t_{0.025, 14} = 2.145$. Since $|t| = 2.32 > 2.145$, $H_0$ is rejected at the 5% level. The mean diameter is significantly different from 10.00 mm.

#### 8.1.2 Two-sample t-test (independent samples)

The two-sample t-test compares the means of two independent groups (for example, two machines, two suppliers, or two settings).

**Hypotheses:**
- $H_0$: $\mu_1 = \mu_2$.
- $H_1$: $\mu_1 \neq \mu_2$.

**Case 1 — equal variances (pooled t-test):**

When the two population variances can be assumed equal ($\sigma_1^2 = \sigma_2^2$), the pooled standard deviation is used:

$$s_p = \sqrt{\frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}}$$

The test statistic is:

$$t = \frac{\bar{x}_1 - \bar{x}_2}{s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}$$

with $\nu = n_1 + n_2 - 2$ degrees of freedom.

**Case 2 — unequal variances (Welch's t-test):**

When the variances are not assumed equal, Welch's approximation is used:

$$t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}$$

The degrees of freedom are approximated by the Welch-Satterthwaite formula:

$$\nu = \frac{\left(\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}\right)^2}{\frac{(s_1^2/n_1)^2}{n_1 - 1} + \frac{(s_2^2/n_2)^2}{n_2 - 1}}$$

In practice, always verify the equality of variances first (section 8.2 or 8.6) before choosing between the pooled and Welch versions.

**Numerical example.** Two machines produce the same part. Measurements of the thickness give:
- Machine A: $n_1 = 12$, $\bar{x}_1 = 5.02$ mm, $s_1 = 0.08$ mm.
- Machine B: $n_2 = 10$, $\bar{x}_2 = 4.96$ mm, $s_2 = 0.07$ mm.

Assuming equal variances:

$$s_p = \sqrt{\frac{11 \times 0.08^2 + 9 \times 0.07^2}{20}} = \sqrt{\frac{0.0704 + 0.0441}{20}} = \sqrt{0.005725} = 0.0757$$

$$t = \frac{5.02 - 4.96}{0.0757 \sqrt{\frac{1}{12} + \frac{1}{10}}} = \frac{0.06}{0.0757 \times 0.4264} = \frac{0.06}{0.0323} = 1.86$$

With $\nu = 20$ degrees of freedom, $t_{0.025, 20} = 2.086$. Since $|t| = 1.86 < 2.086$, $H_0$ is not rejected. There is no significant difference between the two machines at the 5% level.

#### 8.1.3 Paired t-test

The paired t-test is used when observations come in natural pairs (same part measured before and after a treatment, same operator on two instruments, etc.). The test operates on the differences $d_i = x_{1i} - x_{2i}$.

**Hypotheses:**
- $H_0$: $\mu_d = 0$ (no systematic difference between pairs).
- $H_1$: $\mu_d \neq 0$.

**Test statistic:**

$$t = \frac{\bar{d}}{s_d / \sqrt{n}}$$

where $\bar{d} = \frac{1}{n}\sum_{i=1}^{n} d_i$ is the mean of the differences, $s_d$ is the standard deviation of the differences, and $n$ is the number of pairs. Under $H_0$, $t$ follows a Student distribution with $\nu = n - 1$ degrees of freedom.

**When to use:** the paired t-test is more powerful than the two-sample t-test when the pairing effectively reduces variability (for example, comparing two treatments on the same batch of parts eliminates part-to-part variability).

### 8.2 Comparing two variances — Fisher's F-test

Fisher's F-test compares the variances of two independent normally distributed populations. It is often used as a preliminary step before choosing between the pooled t-test and Welch's t-test.

**Hypotheses:**
- $H_0$: $\sigma_1^2 = \sigma_2^2$.
- $H_1$: $\sigma_1^2 \neq \sigma_2^2$.

**Test statistic:**

$$F = \frac{s_1^2}{s_2^2}$$

where $s_1^2 \geq s_2^2$ by convention (so that $F \geq 1$). Under $H_0$, $F$ follows a Fisher-Snedecor distribution with $(\nu_1, \nu_2) = (n_1 - 1, n_2 - 1)$ degrees of freedom.

**Decision rule (two-sided):** reject $H_0$ if $F > F_{\alpha/2, \nu_1, \nu_2}$.

**Critical values (excerpt, $\alpha = 0.05$, two-sided):**

| $\nu_1 \backslash \nu_2$ | 5 | 10 | 15 | 20 | 30 |
|---|---|---|---|---|---|
| 5 | 7.15 | 4.24 | 3.58 | 3.29 | 3.03 |
| 10 | 4.24 | 2.98 | 2.54 | 2.35 | 2.16 |
| 15 | 3.58 | 2.54 | 2.18 | 2.01 | 1.86 |
| 20 | 3.29 | 2.35 | 2.01 | 1.84 | 1.70 |
| 30 | 3.03 | 2.16 | 1.86 | 1.70 | 1.57 |

**Caution:** the F-test for equality of variances is very sensitive to departures from normality. If normality is uncertain, prefer the Levene test (section 8.6).

### 8.3 One-way ANOVA

One-way analysis of variance (ANOVA) extends the two-sample t-test to the comparison of $k$ groups ($k \geq 2$). It tests whether the group means are all equal.

**Hypotheses:**
- $H_0$: $\mu_1 = \mu_2 = \ldots = \mu_k$ (all group means are equal).
- $H_1$: at least two means differ.

**Conditions:**
- Independence of observations.
- Normality within each group (or large samples).
- Homogeneity of variances (homoscedasticity): $\sigma_1^2 = \sigma_2^2 = \ldots = \sigma_k^2$.

#### 8.3.1 Sum of squares decomposition

The total variability is decomposed into two components:

$$SS_T = SS_B + SS_W$$

where:

- **Total sum of squares:**

$$SS_T = \sum_{i=1}^{k} \sum_{j=1}^{n_i} (x_{ij} - \bar{x})^2$$

- **Between-groups sum of squares:**

$$SS_B = \sum_{i=1}^{k} n_i (\bar{x}_i - \bar{x})^2$$

- **Within-groups sum of squares:**

$$SS_W = \sum_{i=1}^{k} \sum_{j=1}^{n_i} (x_{ij} - \bar{x}_i)^2$$

Here $\bar{x}$ is the grand mean of all observations and $\bar{x}_i$ is the mean of group $i$.

#### 8.3.2 ANOVA table

| Source | Sum of squares | df | Mean square | F |
|---|---|---|---|---|
| Between groups | $SS_B$ | $k - 1$ | $MS_B = \frac{SS_B}{k - 1}$ | $F = \frac{MS_B}{MS_W}$ |
| Within groups | $SS_W$ | $N - k$ | $MS_W = \frac{SS_W}{N - k}$ | |
| **Total** | $SS_T$ | $N - 1$ | | |

where $N = \sum_{i=1}^{k} n_i$ is the total number of observations.

**Decision rule:** reject $H_0$ if $F > F_{\alpha, k-1, N-k}$.

The F statistic measures the ratio of between-group variability to within-group variability. A large F value indicates that the group means differ more than would be expected from random variation alone.

#### 8.3.3 Numerical example

Three operators measure the same dimension on 5 parts each. The results (in mm) are:

| Operator A | Operator B | Operator C |
|---|---|---|
| 10.02 | 10.05 | 10.08 |
| 10.01 | 10.04 | 10.07 |
| 10.03 | 10.06 | 10.09 |
| 10.02 | 10.05 | 10.06 |
| 10.02 | 10.05 | 10.10 |

Group means: $\bar{x}_A = 10.020$, $\bar{x}_B = 10.050$, $\bar{x}_C = 10.080$. Grand mean: $\bar{x} = 10.050$.

- $SS_B = 5 \times [(10.020 - 10.050)^2 + (10.050 - 10.050)^2 + (10.080 - 10.050)^2] = 5 \times [0.0009 + 0 + 0.0009] = 0.009$
- $SS_W = (0.0006 + 0.0002 + 0.0010) = 0.0018$ (sum of within-group deviations squared)
- $MS_B = 0.009 / 2 = 0.0045$
- $MS_W = 0.0018 / 12 = 0.00015$
- $F = 0.0045 / 0.00015 = 30.0$

With $(\nu_1, \nu_2) = (2, 12)$ degrees of freedom, $F_{0.05, 2, 12} = 3.89$. Since $F = 30.0 \gg 3.89$, $H_0$ is rejected. The three operators produce significantly different mean measurements.

<!-- IMG:anova_boxplot.png -->

### 8.4 Two-way ANOVA

Two-way ANOVA extends the analysis to two factors simultaneously and allows detection of their interaction. For example, one may wish to study the effect of both the machine (factor A with $a$ levels) and the material batch (factor B with $b$ levels) on a quality characteristic.

**Model with interaction (balanced design, $n$ replicates per cell):**

$$x_{ijk} = \mu + \alpha_i + \beta_j + (\alpha\beta)_{ij} + \epsilon_{ijk}$$

where $\alpha_i$ is the effect of level $i$ of factor A, $\beta_j$ is the effect of level $j$ of factor B, $(\alpha\beta)_{ij}$ is the interaction effect, and $\epsilon_{ijk}$ is the random error.

#### 8.4.1 Sum of squares decomposition

$$SS_T = SS_A + SS_B + SS_{AB} + SS_E$$

- $SS_A = bn \sum_{i=1}^{a} (\bar{x}_{i..} - \bar{x}_{...})^2$ — effect of factor A.
- $SS_B = an \sum_{j=1}^{b} (\bar{x}_{.j.} - \bar{x}_{...})^2$ — effect of factor B.
- $SS_{AB} = n \sum_{i=1}^{a} \sum_{j=1}^{b} (\bar{x}_{ij.} - \bar{x}_{i..} - \bar{x}_{.j.} + \bar{x}_{...})^2$ — interaction.
- $SS_E = \sum_{i=1}^{a} \sum_{j=1}^{b} \sum_{k=1}^{n} (x_{ijk} - \bar{x}_{ij.})^2$ — residual error.

#### 8.4.2 ANOVA table (two-way with interaction)

| Source | SS | df | MS | F |
|---|---|---|---|---|
| Factor A | $SS_A$ | $a - 1$ | $MS_A = \frac{SS_A}{a - 1}$ | $F_A = \frac{MS_A}{MS_E}$ |
| Factor B | $SS_B$ | $b - 1$ | $MS_B = \frac{SS_B}{b - 1}$ | $F_B = \frac{MS_B}{MS_E}$ |
| Interaction A $\times$ B | $SS_{AB}$ | $(a-1)(b-1)$ | $MS_{AB} = \frac{SS_{AB}}{(a-1)(b-1)}$ | $F_{AB} = \frac{MS_{AB}}{MS_E}$ |
| Error | $SS_E$ | $ab(n-1)$ | $MS_E = \frac{SS_E}{ab(n-1)}$ | |
| **Total** | $SS_T$ | $abn - 1$ | | |

Each F statistic is compared to the corresponding critical value $F_{\alpha, \nu_1, \nu_2}$. The interaction term is tested first: if the interaction is significant, the main effects must be interpreted with caution (they depend on the level of the other factor).

### 8.5 Post-hoc tests — multiple comparisons

When ANOVA rejects $H_0$, it only tells us that at least two group means differ, but not which ones. Post-hoc tests identify the specific pairs of groups that differ significantly.

#### 8.5.1 Tukey HSD (honestly significant difference)

Tukey's test compares all possible pairs of group means while controlling the family-wise error rate. The critical difference is:

$$HSD = q_{\alpha, k, N-k} \sqrt{\frac{MS_W}{n}}$$

where $q_{\alpha, k, N-k}$ is the critical value of the studentized range distribution. Two means $\bar{x}_i$ and $\bar{x}_j$ are declared significantly different if $|\bar{x}_i - \bar{x}_j| > HSD$.

#### 8.5.2 Bonferroni correction

The Bonferroni correction is the simplest approach to multiple comparisons. For $m = k(k-1)/2$ pairwise comparisons, each individual test is performed at the significance level $\alpha / m$. It is conservative (less powerful than Tukey) but applies to any type of comparison, not only pairwise.

#### 8.5.3 Summary of post-hoc methods

| Method | Principle | Best suited for | Conservatism |
|---|---|---|---|
| Tukey HSD | Studentized range distribution. | All pairwise comparisons, balanced designs. | Moderate. |
| Bonferroni | Adjusted $\alpha$ per comparison. | Any set of planned comparisons. | Conservative. |
| Scheffé | Based on the F distribution. | All possible contrasts (including complex). | Very conservative. |
| Dunnett | Compares each group to a single control. | Comparisons against a reference. | Less conservative than Bonferroni for this purpose. |

### 8.6 Tests for homogeneity of variances

Homogeneity of variances (homoscedasticity) is a prerequisite for the pooled t-test and for ANOVA. Several tests are available.

#### 8.6.1 Bartlett test

Bartlett's test is the most powerful test for comparing $k$ variances when the data are normally distributed. The test statistic is:

$$\chi^2 = \frac{(N - k) \ln(s_p^2) - \sum_{i=1}^{k}(n_i - 1)\ln(s_i^2)}{1 + \frac{1}{3(k-1)}\left(\sum_{i=1}^{k}\frac{1}{n_i - 1} - \frac{1}{N - k}\right)}$$

where $s_p^2 = \frac{\sum(n_i - 1)s_i^2}{N - k}$ is the pooled variance. Under $H_0$, the statistic approximately follows a $\chi^2$ distribution with $k - 1$ degrees of freedom.

**Caution:** the Bartlett test is very sensitive to departures from normality. Non-normal data can lead to false rejections of $H_0$ even when variances are actually equal.

#### 8.6.2 Levene test

The Levene test is a robust alternative to the Bartlett test. It is less sensitive to departures from normality.

**Principle:** replace each observation $x_{ij}$ by its absolute deviation from the group median (or mean):

$$z_{ij} = |x_{ij} - \tilde{x}_i|$$

where $\tilde{x}_i$ is the median of group $i$ (Brown-Forsythe variant, recommended). Then perform a one-way ANOVA on the $z_{ij}$ values. A significant F statistic indicates unequal variances.

**Recommendation:** use the Levene test (Brown-Forsythe variant with medians) as the default test for homogeneity of variances, especially when normality is not guaranteed.

### 8.7 Non-parametric alternative — Kruskal-Wallis test

When the normality assumption is violated and cannot be remedied by transformation, the Kruskal-Wallis test provides a non-parametric alternative to one-way ANOVA. It compares the distributions (not just the means) of $k$ independent groups.

**Procedure:**
1. Pool all $N$ observations and rank them from 1 to $N$.
2. Compute the sum of ranks $R_i$ for each group $i$.
3. Compute the test statistic:

$$H = \frac{12}{N(N+1)} \sum_{i=1}^{k} \frac{R_i^2}{n_i} - 3(N+1)$$

Under $H_0$ (all groups come from the same distribution), $H$ approximately follows a $\chi^2$ distribution with $k - 1$ degrees of freedom for sufficiently large sample sizes ($n_i \geq 5$).

**Decision rule:** reject $H_0$ if $H > \chi^2_{\alpha, k-1}$.

**Note:** the Kruskal-Wallis test is less powerful than ANOVA when the normality assumption holds. It should be used only when normality cannot be reasonably assumed.

### 8.8 Industrial applications — ISO 5725 and ASTM E691

#### 8.8.1 ISO 5725 — accuracy (trueness and precision)

ISO 5725 is a multi-part standard that deals with the accuracy of measurement methods. It uses ANOVA to decompose the total variability of measurement results into repeatability and reproducibility components.

**Key definitions:**
- **Repeatability ($r$):** the variation obtained when the same operator, using the same equipment, measures the same sample multiple times under the same conditions. The repeatability limit $r = 2.8 \times s_r$ gives the maximum expected difference between two results obtained under repeatability conditions (at the 95% confidence level).
- **Reproducibility ($R$):** the variation obtained when different operators, different equipment, or different laboratories measure the same sample. The reproducibility limit $R = 2.8 \times s_R$ gives the maximum expected difference between two results obtained under reproducibility conditions.

**Relationship:**

$$s_R^2 = s_r^2 + s_L^2$$

where $s_r^2$ is the repeatability variance, $s_L^2$ is the between-laboratory variance, and $s_R^2$ is the reproducibility variance.

**ISO 5725-2** provides the statistical framework for organizing interlaboratory experiments and computing $s_r$ and $s_R$ using one-way ANOVA (laboratories as groups).

#### 8.8.2 ASTM E691 — interlaboratory studies

ASTM E691 describes the practice for conducting interlaboratory studies to determine the precision of a test method. It uses Mandel's consistency statistics to identify laboratories that produce atypical results.

**Mandel h statistic (between-laboratory consistency):**

$$h_i = \frac{\bar{x}_i - \bar{x}}{s_{\bar{x}}}$$

where $\bar{x}_i$ is the mean of laboratory $i$, $\bar{x}$ is the grand mean, and $s_{\bar{x}}$ is the standard deviation of laboratory means. A large $|h_i|$ indicates that laboratory $i$ produces results that are biased relative to the others.

**Mandel k statistic (within-laboratory consistency):**

$$k_i = \frac{s_i}{s_r}$$

where $s_i$ is the standard deviation of laboratory $i$ and $s_r$ is the pooled repeatability standard deviation. A large $k_i$ indicates that laboratory $i$ has unusually high variability.

Critical values for $h$ and $k$ are tabulated in ASTM E691 for various numbers of laboratories and replicates. Laboratories exceeding these critical values should be investigated.

### 8.9 Summary table of comparison tests

| Objective | Test | Conditions | Non-parametric alternative |
|---|---|---|---|
| Compare one mean to a reference value. | One-sample t-test. | Normality (or $n > 30$). | Wilcoxon signed-rank test. |
| Compare two means (independent). | Two-sample t-test (pooled or Welch). | Normality, independence. | Mann-Whitney U test. |
| Compare two means (paired). | Paired t-test. | Normality of differences. | Wilcoxon signed-rank test. |
| Compare two variances. | Fisher's F-test. | Normality (strict). | Levene test (robust). |
| Compare $k$ means. | One-way ANOVA. | Normality, homoscedasticity. | Kruskal-Wallis test. |
| Compare $k$ means (two factors). | Two-way ANOVA. | Normality, homoscedasticity. | Friedman test (for blocked designs). |
| Identify differing pairs after ANOVA. | Tukey, Bonferroni, Scheffé, Dunnett. | Same as ANOVA. | Dunn's test (after Kruskal-Wallis). |
| Compare $k$ variances. | Bartlett test. | Normality (strict). | Levene test (robust). |
| Repeatability and reproducibility. | ANOVA (ISO 5725). | Normality, balanced design. | — |
| Interlaboratory consistency. | Mandel h and k (ASTM E691). | Balanced interlaboratory design. | — |

---

## 9. Outlier detection (ISO 16269-4)

Outliers are observations that deviate significantly from the rest of the data. They may arise from measurement errors, transcription errors, special causes, or sample contamination. ISO 16269-4 provides statistical tests to detect them.

### 9.1 Grubbs test

The Grubbs test is the most widely used test for detecting a single outlier in a sample assumed to be normally distributed.

**Hypotheses:**
- $H_0$: there is no outlier.
- $H_1$: the most extreme value is an outlier.

**Test statistic:**

$$G = \frac{\max_i |x_i - \bar{x}|}{s}$$

where $\bar{x}$ is the mean and $s$ is the standard deviation of the sample.

**Variants:**
- One-sided upper test: $G = (x_{(n)} - \bar{x}) / s$
- One-sided lower test: $G = (\bar{x} - x_{(1)}) / s$
- Two-sided test: $G = \max(x_{(n)} - \bar{x}, \bar{x} - x_{(1)}) / s$

**Critical values of the Grubbs test (two-sided, $\alpha = 0{,}05$):**

| $n$ | $G_{critical}$ |
|---|---|
| 3 | 1.155 |
| 4 | 1.481 |
| 5 | 1.715 |
| 6 | 1.887 |
| 7 | 2.020 |
| 8 | 2.126 |
| 9 | 2.215 |
| 10 | 2.290 |
| 12 | 2.412 |
| 15 | 2.549 |
| 20 | 2.709 |
| 25 | 2.822 |
| 30 | 2.908 |
| 40 | 3.036 |
| 50 | 3.128 |
| 60 | 3.199 |
| 80 | 3.305 |
| 100 | 3.383 |

$H_0$ is rejected if $G > G_{critical}$. If an outlier is detected and removed, the test can be repeated on the reduced dataset.

### 9.2 Dixon test

The Dixon test is a non-parametric alternative to the Grubbs test, particularly suited for small samples ($3 \leq n \leq 25$). It uses ratios based on order statistics (sorted data).

**Test statistics according to sample size:**

| Size $n$ | Statistic | Formula (test of the largest value) |
|---|---|---|
| 3 to 7 | $r_{10}$ | $(x_{(n)} - x_{(n-1)}) / (x_{(n)} - x_{(1)})$ |
| 8 to 10 | $r_{11}$ | $(x_{(n)} - x_{(n-1)}) / (x_{(n)} - x_{(2)})$ |
| 11 to 13 | $r_{21}$ | $(x_{(n)} - x_{(n-2)}) / (x_{(n)} - x_{(2)})$ |
| 14 to 25 | $r_{22}$ | $(x_{(n)} - x_{(n-2)}) / (x_{(n)} - x_{(3)})$ |

To test the smallest value, the indices are reversed.

**Critical values of the Dixon test ($\alpha = 0{,}05$, one-sided test):**

| $n$ | $r_{10}$ | $r_{11}$ | $r_{21}$ | $r_{22}$ |
|---|---|---|---|---|
| 3 | 0.941 | — | — | — |
| 4 | 0.765 | — | — | — |
| 5 | 0.642 | — | — | — |
| 6 | 0.560 | — | — | — |
| 7 | 0.507 | — | — | — |
| 8 | — | 0.554 | — | — |
| 9 | — | 0.512 | — | — |
| 10 | — | 0.477 | — | — |
| 11 | — | — | 0.576 | — |
| 12 | — | — | 0.546 | — |
| 13 | — | — | 0.521 | — |
| 14 | — | — | — | 0.546 |
| 15 | — | — | — | 0.525 |
| 20 | — | — | — | 0.450 |
| 25 | — | — | — | 0.406 |

*The symbol "—" indicates that the corresponding statistic is not used for this sample size.*

### 9.3 Comparison of Grubbs and Dixon tests

| Criterion | Grubbs | Dixon |
|---|---|---|
| Normality assumption | Yes (required). | Less sensitive to non-normality. |
| Sample size | $n \geq 3$, ideal for $n \geq 7$. | $3 \leq n \leq 25$. |
| Power | Higher for medium and large samples. | Higher for very small samples. |
| Multiple outliers | Sensitive to masking (one outlier can mask another). | Less sensitive to masking. |
| Calculation | Requires $\bar{x}$ and $s$. | Based only on order statistics. |

**Practical recommendation:** for $n < 10$, prefer Dixon. For $n \geq 10$, prefer Grubbs. In all cases, a graphical analysis (box plot, Q-Q plot) should accompany the formal test.

---

## 10. Statistical tolerance intervals (ISO 16269-6)

A statistical tolerance interval is an interval estimated from a sample that contains at least a proportion $p$ of the population with a confidence level $\gamma$. It should not be confused with the confidence interval (which brackets a parameter) or the industrial tolerance interval (specifications imposed by the customer).

### 10.1 Definitions

**Two-sided tolerance interval:** an interval $[\bar{x} - k \cdot s, \, \bar{x} + k \cdot s]$ that contains at least the proportion $p$ of the population with a confidence level $\gamma$.

**One-sided upper tolerance interval:** $(-\infty, \, \bar{x} + k \cdot s]$ contains at least $p$ of the population.

**One-sided lower tolerance interval:** $[\bar{x} - k \cdot s, \, +\infty)$ contains at least $p$ of the population.

The factor $k$ depends on the sample size $n$, the proportion $p$, and the confidence level $\gamma$.

### 10.2 $k$ factors for two-sided intervals (normal distribution)

The following table gives the $k$ factors for two-sided tolerance intervals under the normality assumption, for common values of $p$ and $\gamma$:

**$p = 0{,}90$ (90% of the population):**

| $n$ | $\gamma = 0{,}90$ | $\gamma = 0{,}95$ | $\gamma = 0{,}99$ |
|---|---|---|---|
| 5 | 3.407 | 4.275 | 6.603 |
| 10 | 2.535 | 2.839 | 3.532 |
| 15 | 2.329 | 2.566 | 3.036 |
| 20 | 2.219 | 2.408 | 2.786 |
| 25 | 2.150 | 2.310 | 2.631 |
| 30 | 2.103 | 2.245 | 2.529 |
| 50 | 1.996 | 2.104 | 2.310 |
| 100 | 1.916 | 1.999 | 2.146 |

**$p = 0{,}95$ (95% of the population):**

| $n$ | $\gamma = 0{,}90$ | $\gamma = 0{,}95$ | $\gamma = 0{,}99$ |
|---|---|---|---|
| 5 | 4.152 | 5.079 | 7.855 |
| 10 | 2.911 | 3.259 | 4.053 |
| 15 | 2.637 | 2.907 | 3.443 |
| 20 | 2.498 | 2.713 | 3.139 |
| 25 | 2.412 | 2.594 | 2.952 |
| 30 | 2.354 | 2.515 | 2.833 |
| 50 | 2.224 | 2.345 | 2.576 |
| 100 | 2.127 | 2.218 | 2.383 |

**$p = 0{,}99$ (99% of the population):**

| $n$ | $\gamma = 0{,}90$ | $\gamma = 0{,}95$ | $\gamma = 0{,}99$ |
|---|---|---|---|
| 5 | 5.741 | 6.634 | 10.260 |
| 10 | 3.739 | 4.187 | 5.209 |
| 15 | 3.329 | 3.669 | 4.343 |
| 20 | 3.126 | 3.395 | 3.927 |
| 25 | 3.002 | 3.231 | 3.677 |
| 30 | 2.919 | 3.118 | 3.513 |
| 50 | 2.735 | 2.882 | 3.165 |
| 100 | 2.601 | 2.715 | 2.917 |

### 10.3 $k$ factors for one-sided intervals (normal distribution)

**$p = 0{,}95$, $\gamma = 0{,}95$:**

| $n$ | $k$ (one-sided) |
|---|---|
| 5 | 3.400 |
| 10 | 2.568 |
| 15 | 2.329 |
| 20 | 2.208 |
| 25 | 2.132 |
| 30 | 2.080 |
| 50 | 1.965 |
| 100 | 1.874 |

### 10.4 Non-parametric (distribution-free) tolerance intervals

When the data distribution is not normal (or cannot be verified), non-parametric tolerance intervals based on order statistics are used.

The interval $[x_{(r)}, x_{(n-r+1)}]$ contains at least the proportion $p$ of the population with a confidence level $\gamma$ if:

$$\sum_{j=0}^{2r-2} \binom{n}{j} p^j (1-p)^{n-j} \leq 1 - \gamma$$

**Minimum sample size for a non-parametric interval:**

For a two-sided interval with $r = 1$ (bounds = minimum and maximum of the sample):

| $p$ | $\gamma = 0{,}90$ | $\gamma = 0{,}95$ | $\gamma = 0{,}99$ |
|---|---|---|---|
| 0.90 | 38 | 46 | 64 |
| 0.95 | 77 | 93 | 130 |
| 0.99 | 388 | 473 | 662 |

These large sample sizes illustrate the cost of having no distributional assumption: much more data are needed to achieve the same coverage.

### 10.5 Distinction between types of statistical intervals

It is essential not to confuse the different types of intervals.

| Interval type | What it brackets | Typical formula | Width |
|---|---|---|---|
| **Confidence interval** | The population parameter $\mu$. | $\bar{x} \pm t_{\alpha/2, n-1} \cdot s / \sqrt{n}$ | Decreases with $n$. |
| **Prediction interval** | The next individual observation. | $\bar{x} \pm t_{\alpha/2, n-1} \cdot s \sqrt{1 + 1/n}$ | Decreases slowly with $n$. |
| **Tolerance interval** | At least $p$% of the population. | $\bar{x} \pm k \cdot s$ | Decreases slowly with $n$. |

The confidence interval is always the narrowest because it targets a single parameter. The tolerance interval is the widest because it must cover an entire proportion of the population with a given confidence level.

### 10.6 Practical application: verifying lot conformity

To verify that a lot satisfies a two-sided specification $[LSI, LSS]$ with at least $p = 99\%$ of the population conforming at a confidence level $\gamma = 95\%$, proceed as follows:
1. Draw a sample of size $n$ (for example, $n = 30$).
2. Verify normality (section 7).
3. Calculate $\bar{x}$ and $s$.
4. Read the $k$ factor from the table ($k = 3{,}118$ for $n = 30$, $p = 0{,}99$, $\gamma = 0{,}95$).
5. Verify that $\bar{x} - k \cdot s \geq LSI$ and $\bar{x} + k \cdot s \leq LSS$.
6. If both conditions are met, one concludes with 95% confidence that 99% of the population is conforming.

---

## 11. Measurement uncertainty (GUM, NIST)

The GUM (Guide to the expression of Uncertainty in Measurement, JCGM 100:2008) is the international reference document for evaluating and expressing measurement uncertainty. The NIST Technical Note TN 1297 is a practical summary for laboratories.

### 11.1 Fundamental principles

Every measurement is subject to uncertainty. A measurement result is complete only when accompanied by its uncertainty. Measurement uncertainty quantifies the dispersion of values that could reasonably be attributed to the measurand.

The measurement model is:

$$Y = f(X_1, X_2, \ldots, X_N)$$

where $Y$ is the measurand, $X_i$ are the input quantities, and $f$ is the measurement function.

### 11.2 Type A evaluation

Type A evaluation uses statistical analysis of a series of $n$ repeated observations.

**Type A standard uncertainty:**

$$u_A = \frac{s}{\sqrt{n}}$$

where $s$ is the experimental standard deviation:

$$s = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2}$$

Type A evaluation is associated with $\nu = n - 1$ degrees of freedom.

### 11.3 Type B evaluation

Type B evaluation uses information other than statistical: calibration certificates, manufacturer specifications, literature data, expert judgment.

**Rectangular (uniform) distribution:**

When it is only known that the value lies within an interval $[-a, +a]$ with equal probability:

$$u_B = \frac{a}{\sqrt{3}}$$

Associated degrees of freedom: $\nu \rightarrow \infty$ (in practice, $\nu = 50$ or more is used).

**Triangular distribution:**

When central values are more probable than extremes:

$$u_B = \frac{a}{\sqrt{6}}$$

**Normal distribution:**

When the information is given as a confidence interval with a coverage factor $k$:

$$u_B = \frac{a}{k}$$

For example, if a calibration certificate states $U = 0{,}1$ mg with $k = 2$, then $u_B = 0{,}1 / 2 = 0{,}05$ mg.

**Summary table of Type B distributions:**

| Distribution | Parameter | Standard uncertainty $u_B$ | Typical use |
|---|---|---|---|
| Rectangular | Half-width $a$ | $a / \sqrt{3}$ | Instrument resolution, component tolerance. |
| Triangular | Half-width $a$ | $a / \sqrt{6}$ | More precise information than rectangular. |
| Normal | Expanded uncertainty $U$, factor $k$ | $U / k$ | Calibration certificate. |
| U-shaped (arcsine) | Half-amplitude $a$ | $a / \sqrt{2}$ | Sinusoidal oscillation (cyclic temperature). |

### 11.4 Combined uncertainty

The combined uncertainty $u_c$ is obtained by the law of propagation of uncertainties (linear approximation):

$$u_c^2 = \sum_{i=1}^{N} c_i^2 \, u_i^2$$

where $c_i$ is the sensitivity coefficient:

$$c_i = \frac{\partial f}{\partial x_i}$$

This formula assumes that the input quantities are independent (uncorrelated). If correlations exist, cross-terms must be added:

$$u_c^2 = \sum_{i=1}^{N} c_i^2 \, u_i^2 + 2 \sum_{i=1}^{N-1}\sum_{j=i+1}^{N} c_i \, c_j \, u(x_i, x_j)$$

where $u(x_i, x_j)$ is the estimated covariance.

### 11.5 Expanded uncertainty

The expanded uncertainty $U$ provides an interval within which the measurand lies with a given confidence level:

$$U = k \cdot u_c$$

| Factor $k$ | Confidence level (normal distribution) |
|---|---|
| 1 | 68.3% |
| 2 | 95.5% |
| 2.576 | 99% |
| 3 | 99.7% |

The factor $k = 2$ is the most commonly used and corresponds to a confidence level of approximately 95%.

**Expression of the result:**

$$Y = y \pm U \quad (k = 2, \text{ confidence level } \approx 95\%)$$

### 11.6 Uncertainty budget — example

An uncertainty budget is a table summarizing all uncertainty components. Here is an example for measuring a length with a caliper.

| Source | Type | Distribution | Value | Divisor | $u_i$ | $c_i$ | $c_i \cdot u_i$ | $(c_i \cdot u_i)^2$ |
|---|---|---|---|---|---|---|---|---|
| Repeatability | A | Normal | $s = 0{,}012$ mm | $\sqrt{n} = \sqrt{5}$ | 0.0054 | 1 | 0.0054 | 0.0000291 |
| Resolution | B | Rectangular | $a = 0{,}005$ mm | $\sqrt{3}$ | 0.0029 | 1 | 0.0029 | 0.0000084 |
| Calibration | B | Normal | $U = 0{,}010$ mm | $k = 2$ | 0.0050 | 1 | 0.0050 | 0.0000250 |
| Temperature | B | Rectangular | $a = 0{,}003$ mm | $\sqrt{3}$ | 0.0017 | 1 | 0.0017 | 0.0000029 |

**Combined uncertainty:** $u_c = \sqrt{0{,}0000291 + 0{,}0000084 + 0{,}0000250 + 0{,}0000029} = \sqrt{0{,}0000654} = 0{,}0081$ mm.

**Expanded uncertainty:** $U = 2 \times 0{,}0081 = 0{,}016$ mm (rounded).

**Result:** $L = 25{,}032 \pm 0{,}016$ mm ($k = 2$, confidence level $\approx 95\%$).

<!-- IMG:uncertainty_budget.png -->

### 11.7 Degrees of freedom and the Welch-Satterthwaite formula

When the combined uncertainty combines components with different degrees of freedom $\nu_i$, the effective number of degrees of freedom $\nu_{eff}$ is estimated by the Welch-Satterthwaite formula:

$$\nu_{eff} = \frac{u_c^4}{\sum_{i=1}^{N} \frac{(c_i \, u_i)^4}{\nu_i}}$$

The result is rounded down to the nearest integer. If $\nu_{eff}$ is small (typically $< 30$), the coverage factor $k$ must be adjusted using the Student's t-distribution:

| $\nu_{eff}$ | $k$ for 95% | $k$ for 99% |
|---|---|---|
| 1 | 12.71 | 63.66 |
| 2 | 4.30 | 9.92 |
| 3 | 3.18 | 5.84 |
| 5 | 2.57 | 4.03 |
| 10 | 2.23 | 3.17 |
| 20 | 2.09 | 2.85 |
| 30 | 2.04 | 2.75 |
| 50 | 2.01 | 2.68 |
| $\infty$ | 1.96 | 2.58 |

### 11.8 Conformity rules and uncertainty (ISO 14253-1)

When a measurement result is compared to a specification, measurement uncertainty must be taken into account. ISO 14253-1 defines the following rules:

**Conformity rule:** a part is declared conforming if the measurement result, reduced by the expanded uncertainty, remains within the specification limits.

$$LSI + U \leq y \leq LSS - U$$

**Nonconformity rule:** a part is declared nonconforming if the measurement result, increased by the expanded uncertainty, falls outside the specification limits.

$$y < LSI - U \quad \text{or} \quad y > LSS + U$$

**Uncertainty zone:** when the result falls between the conformity zone and the nonconformity zone, no decision can be made with certainty. This zone has a width of $2U$ on each side of the specification limit.

### 11.9 Best practices for expressing uncertainty

1. Identify all sources of uncertainty (do not overlook any).
2. Quantify each source by a standard uncertainty (Type A or Type B).
3. Verify units and sensitivity coefficients.
4. Do not forget correlations between input quantities.
5. Round the expanded uncertainty to one or two significant figures.
6. Round the result to the same number of decimal places as the uncertainty.
7. Always state the coverage factor $k$ and the associated confidence level.

---

## 12. SPC guide (ISO 11462) — implementation steps

ISO 11462-1 provides guidelines for implementing statistical process control (SPC) in an industrial environment. The standard emphasizes that SPC is a management and continuous improvement tool, and not merely a statistical calculation.

### 12.1 Step 1 — management commitment

Management must understand and support the SPC initiative. This includes:
- Allocating resources (personnel, training, software, instruments).
- Defining measurable objectives.
- Integrating SPC into the quality system (ISO 9001).

### 12.2 Step 2 — process identification

Identify the critical processes that have a significant impact on product quality. Use tools such as:
- FMEA (Failure Mode and Effects Analysis) to prioritize risks.
- Process flow diagram to understand key steps.
- Pareto analysis to identify the main sources of nonconformity.

### 12.3 Step 3 — measurement system analysis

Before collecting SPC data, verify that the measurement system is adequate (section 6):
- GRR study: %GRR $< 10\%$ (acceptable) or $< 30\%$ (marginal).
- Number of distinct categories $ndc \geq 5$.
- Linearity and stability of the measurement device.

### 12.4 Step 4 — data collection

Define a data collection plan including:
- The characteristic to be monitored.
- The subgroup size $n$ and sampling frequency.
- The sampling method (random within a homogeneous subgroup).
- The minimum number of subgroups for the study phase (at least 25, according to ISO 7870-2).

### 12.5 Step 5 — control chart selection

The choice of control chart depends on the type of data and production conditions.

| Data type | Subgroup size | Recommended chart |
|---|---|---|
| Continuous variables | $n = 1$ | I-MR |
| Continuous variables | $2 \leq n \leq 9$ | $\bar{x}$ / R |
| Continuous variables | $n \geq 10$ | $\bar{x}$ / S |
| Attributes (conforming / nonconforming) | Constant | $np$ |
| Attributes (conforming / nonconforming) | Variable | $p$ |
| Attributes (number of defects) | Constant | $c$ |
| Attributes (defect rate) | Variable | $u$ |

### 12.6 Step 6 — control limit calculation

Calculate the control limits from the study phase data, using the formulas in section 4. Verify that:
- No point falls outside the limits during the study phase.
- No non-random pattern is detected (Western Electric rules, section 4.3).
- If out-of-control points are identified and the special cause is found and eliminated, recalculate the limits after excluding those points.

### 12.7 Step 7 — process monitoring

Implement the control chart in production:
- Plot new data in real time.
- Apply detection rules (section 4.3).
- Train operators on chart interpretation.
- Document events (lot changes, adjustments, etc.).

### 12.8 Step 8 — out-of-control action plan (OCAP)

The OCAP (Out-of-Control Action Plan) defines the actions to be taken when an out-of-control signal is detected. It must include:
- Identification of the special cause (the 5Ms: material, machine, method, manpower, environment).
- Immediate corrective action (stop, adjust, sort).
- Permanent corrective action (process modification, preventive maintenance).
- Verification of the effectiveness of the corrective action.
- Possible update of the control limits.

### 12.9 Step 9 — continuous improvement

SPC is not limited to monitoring: it is a continuous improvement tool (PDCA). The long-term objectives are:
- Reduce process variability (increase $C_{pk}$).
- Center the process on the target.
- Reduce the cost of poor quality.
- Periodically revise the control limits to reflect improvements.

**SPC improvement cycle:**

1. **Plan**: identify the process, choose the chart, define objectives.
2. **Do**: collect data, calculate limits, implement the chart.
3. **Check**: analyze results, detect special causes, calculate capability.
4. **Act**: eliminate special causes, reduce variability, standardize improvements.

---

## 13. Summary and interconnections — cross-reference table

The following table shows how the different standards and methods interconnect. Each row represents a standard, and each column indicates whether that standard is related to a given domain.

| Standard | Sampling | SPC | Capability | Normality | Outliers | Uncertainty | Tolerance intervals |
|---|---|---|---|---|---|---|---|
| **ISO 2859** (attributes) | Yes (primary). | Uses results to adjust inspection. | — | — | — | — | — |
| **ISO 3951** (variables) | Yes (primary). | — | Requires verification of process capability. | Normality assumption required. | Sensitive to outliers. | — | — |
| **ISO 7870** (SPC) | — | Yes (primary). | Provides $\sigma$ estimate for $C_p$, $C_{pk}$. | I-MR chart assumes normality. | WECO rules detect certain outliers. | — | — |
| **ISO 22514-2** (process capability) | — | Requires a process under control (SPC). | Yes (primary). | Normality assumption required for indices. | Outliers distort indices. | Measurement system contributes to variability. | Indices are related to tolerance intervals. |
| **ISO 22514-7** (measurement capability) | — | Prerequisite for reliable SPC. | Prerequisite for reliable capability. | — | — | Related to measurement uncertainty. | — |
| **ISO 5479** (normality) | — | Prerequisite for I-MR. | Prerequisite for $C_p$, $C_{pk}$. | Yes (primary). | Should be performed before outlier test. | — | Prerequisite for parametric intervals. |
| **ISO 5725 / ASTM E691** (ANOVA, comparison) | — | ANOVA decomposes SPC variability sources. | Repeatability/reproducibility affect capability. | Normality assumed for t-test and ANOVA. | Mandel statistics detect atypical laboratories. | $s_r$ and $s_R$ contribute to uncertainty budget. | — |
| **ISO 16269-4** (outliers) | Outliers in the sample distort the decision. | Outliers generate false alarms. | Outliers distort $C_{pk}$. | Grubbs assumes normality. | Yes (primary). | — | Outliers widen intervals. |
| **ISO 16269-6** (tolerance intervals) | — | — | Related to the concept of capability. | Parametric intervals assume normality. | Outliers affect the bounds. | — | Yes (primary). |
| **ISO 11462** (SPC guide) | — | Yes (implementation guide). | Integrates capability into the SPC approach. | Mentions normality verification. | — | Mentions measurement system validation. | — |
| **GUM / NIST** | — | — | Measurement uncertainty affects apparent capability. | Type A assumes normality for $u_A$. | Outliers affect Type A estimation. | Yes (primary). | — |

### Key interconnections

**Recommended logical sequence for a capability study:**

1. **Validate the measurement system** (ISO 22514-7): GRR study, verify %GRR $< 10\%$.
2. **Collect data** (ISO 7870-2): at least 25 subgroups.
3. **Test normality** (ISO 5479): Shapiro-Wilk + Q-Q plot.
4. **Detect outliers** (ISO 16269-4): Grubbs or Dixon.
5. **Construct control charts** (ISO 7870-2): verify that the process is under control.
6. **Calculate capability** (ISO 22514-2): $C_p$, $C_{pk}$, $P_p$, $P_{pk}$.
7. **Estimate uncertainty** (GUM) if necessary for the measurement result.
8. **Calculate tolerance intervals** (ISO 16269-6) if necessary for specifications.

---

## 14. Documents indexed in the RAG

The following documents are available in the RAG statistical collection and can be queried for more detailed information.

### 14.1 Sampling standards

| Reference | Title | Main content |
|---|---|---|
| **ISO 2859-1** | Sampling procedures for inspection by attributes — Part 1: sampling schemes indexed by acceptance quality limit (AQL) for lot-by-lot inspection. | Sampling tables, letter codes, switching rules, OC curves. |
| **ISO 2859-2** | Sampling procedures for inspection by attributes — Part 2: sampling plans indexed by limiting quality (LQ) for isolated lot inspection. | Plans for isolated lots, tables indexed by LQ. |
| **ISO 3951-1** | Sampling procedures for inspection by variables — Part 1: specification for single sampling plans indexed by acceptance quality limit (AQL). | Methods $s$ and $\sigma$, acceptability constant $k$, one-sided and two-sided specifications. |

### 14.2 SPC and control chart standards

| Reference | Title | Main content |
|---|---|---|
| **ISO 7870-1** | Control charts — Part 1: general guidelines. | Overview of chart types, principles, terminology. |
| **ISO 7870-2** | Control charts — Part 2: Shewhart control charts. | $\bar{x}$/R, $\bar{x}$/S, I-MR, $p$, $np$, $c$, $u$ charts, constants tables. |
| **ASTM E2587** | Standard Practice for Use of Control Charts in Statistical Process Control. | Practical guide for control chart implementation, numerical examples. |
| **ISO 11462-1** | Guidelines for implementation of statistical process control (SPC) — Part 1: elements of SPC. | Implementation steps, organization, training, continuous improvement. |

### 14.3 Capability standards

| Reference | Title | Main content |
|---|---|---|
| **ISO 22514-1** | Statistical methods in process management — Capability and performance — Part 1: general principles and concepts. | Definitions, terminology, capability and performance concepts. |
| **ISO 22514-2** | Statistical methods in process management — Capability and performance — Part 2: capability and performance of time-dependent quantitative quality characteristics. | $C_p$, $C_{pk}$, $P_p$, $P_{pk}$ indices, calculation methods. |
| **ISO 22514-7** | Statistical methods in process management — Capability and performance — Part 7: capability of measurement processes. | $C_g$, $C_{gk}$ indices, GRR study, %GRR, ndc. |

### 14.4 Statistical tests and intervals standards

| Reference | Title | Main content |
|---|---|---|
| **ISO 5479** | Statistical tests — Tests of normality. | Shapiro-Wilk, Anderson-Darling, Kolmogorov-Smirnov tests, Q-Q plots. |
| **ISO 16269-4** | Statistical interpretation of data — Part 4: detection and treatment of outliers. | Grubbs and Dixon tests, critical value tables. |
| **ISO 16269-6** | Statistical interpretation of data — Part 6: determination of statistical tolerance intervals. | Parametric and non-parametric intervals, $k$ factor tables. |

### 14.5 International guides for uncertainty

| Reference | Title | Main content |
|---|---|---|
| **GUM (JCGM 100:2008)** | Evaluation of measurement data — Guide to the expression of uncertainty in measurement. | Type A and B, propagation of uncertainties, combined and expanded uncertainty, Welch-Satterthwaite. |
| **NIST TN 1297** | Guidelines for Evaluating and Expressing the Uncertainty of NIST Measurement Results. | Practical summary of the GUM adapted for laboratories, examples, recommendations. |

---

*This document serves as a course and reference support. For contractual or regulatory applications, it is essential to refer directly to the official standard texts in their current version.*
