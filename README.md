# black-scholes-option-pricer
Black-Scholes European Option Pricing model implemented in Python and Excel
# Black-Scholes Option Pricer

This project implements the **Black-Scholes formula** to calculate the value of a **European put option** using:

- Analytical Black-Scholes formula for call price
- Put-call parity to derive put price
- Implemented in **Python** and **Excel**
- Tabulates how put option value changes with different interest rates

---

## 📘 Formulae

Let:

- \( S \): current stock price
- \( K \): strike price
- \( T \): time to maturity (in years)
- \( r \): annual interest rate
- \( \sigma \): volatility
- \( N(x) \): cumulative standard normal distribution

**Black-Scholes Call Option Price:**

\[
C = S N(d_1) - K e^{-rT} N(d_2)
\]

\[
d_1 = \frac{\ln(S/K) + (r + \frac{1}{2} \sigma^2)T}{\sigma \sqrt{T}}, \quad
d_2 = d_1 - \sigma \sqrt{T}
\]

**Put-Call Parity:**

\[
P = C - S + K e^{-rT}
\]

---

## 📈 Output (Python)

The Python script tabulates values of **Put option price (P)** for interest rates ranging from 9x% to 14x%.

---

## 🧮 Technologies Used

- Python
- `math`, `scipy.stats`
- Excel
- GitHub

---

## 🧠 Insight

You will see that as the interest rate increases, the value of the put option generally **decreases**, due to the time value of money.

---

## 🗂 Folder Structure

black-scholes-option-pricer/
├── black_scholes.py
├── excel-version.xlsx
└── README.md


---

## 📌 Author

[Mogamat Wazir Daniels](https://github.com/WazirDan)
