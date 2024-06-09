# Exercise 4: Cost and Time Estimation

This document provides an estimation of cost and time to implement the described software project.

## 1. Estimating Function Points (FP):

| FUNCTION                         | ACTION                         | CATEGORY           | POINTS |
|----------------------------------|--------------------------------|--------------------|--------|
| SELECT BOX to select a Sensor    | SELECT                         | External Input     | 4      |
| ADD Button to add Sensor         | ADD                            | External Input     | 4      |
| Several sensors can be added     | AGGREGATE                      | Internal Logical File | 7      |
| If Sensor exists in list, ADD operation is ignored | VALIDATE         | Internal Logical File | 7      |
| Sensor in list can be marked     | MARK                           | External Inquiry   | 3      |
| REMOVE button pushed (removes marked Sensor) | REMOVE            | External Input     | 3      |
| START button pushed App collects Sensor data. (changes label to STOP) | COLLECT     | EI / EO | 9      |
| ADD or REMOVE Sensors not possible when collecting data | LOCK   | Internal Logical File | 7      |
| After pushing STOP data is sent to backend service | TRANSFER      | External Output    | 4      |

**Total FP: 48**

## 2. Calculate Lines of Code (LOC) and Kilo Delivered Lines (KDL)
- Using Java: LOC per FP = 53
  - LOC = 48 * 53 = 2544
- KDL = 2544 / 1000 = 2.54

## 3. Effort Estimation with COCOMO (COnstructive COst MOdel)
- Effort: `a * KDL^b = 2.8 * 2.54^1.20 = 8.56 Person-Months`
- Effort Adjustment Factor: `8.56 * 1.40 * 1.08 * 0.86 = 11.37 Person-Months` (~ 337 workdays)

## 4. Duration Based on Workforce
- Assuming 3 developers:
  - Duration = 337 workdays / 3 = 112.33 workdays (~ 16.04 weeks, 3.69 months)

## 5. Calculate Cost
- Based on Swiss developer average salary: [Source](https://ch.talent.com/en/salary?job=software+developer)
  - Average salary: 430.8 CHF/day (8 hours)
  - Cost = 112.33 workdays * 430.8 CHF/day = 48,392 CHF

## 6. Conclusion
- **Estimated implementation duration (3 Developers):** 16.04 weeks or 3.69 months.
- **Projected total cost:** 48,392 CHF.

For more details on salary data, visit [Swiss Developer Salary](https://ch.talent.com/en/salary?job=software+developer).
