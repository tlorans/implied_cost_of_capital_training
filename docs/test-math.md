# Math Examples

Test page to verify LaTeX math rendering.

## Inline Math

The Gordon Growth Model formula $r = \frac{D_1}{P_0} + g$ shows the relationship between dividend, price, and growth.

We can also write inline equations like $E = mc^2$ or $a^2 + b^2 = c^2$.

## Display Math (Block)

The present value formula:

$$PV = \frac{CF_1}{(1+r)^1} + \frac{CF_2}{(1+r)^2} + \cdots + \frac{CF_n}{(1+r)^n}$$

Or more compactly:

$$PV = \sum_{t=1}^{n} \frac{CF_t}{(1+r)^t}$$

## Complex Equations

The Black-Scholes formula for a European call option:

$$C = S_0 N(d_1) - K e^{-rT} N(d_2)$$

Where:

$$d_1 = \frac{\ln(S_0/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}}$$

$$d_2 = d_1 - \sigma\sqrt{T}$$

## Greek Letters

Common financial Greek letters: $\alpha$ (alpha), $\beta$ (beta), $\gamma$ (gamma), $\delta$ (delta), $\sigma$ (sigma), $\mu$ (mu), $\rho$ (rho)

## Matrices

Portfolio weights:

$$w = \begin{bmatrix} w_1 \\ w_2 \\ w_3 \end{bmatrix}$$

Covariance matrix:

$$\Sigma = \begin{bmatrix} 
\sigma_1^2 & \sigma_{12} & \sigma_{13} \\
\sigma_{21} & \sigma_2^2 & \sigma_{23} \\
\sigma_{31} & \sigma_{32} & \sigma_3^2
\end{bmatrix}$$

## Multiple Lines

Derivation example:

$$
\begin{align}
r &= \frac{D_1}{P_0} + g \\
  &= \frac{\$2}{\$50} + 0.05 \\
  &= 0.04 + 0.05 \\
  &= 0.09
\end{align}
$$

## Test Your Math

If you can see all the equations above properly formatted, math rendering is working correctly! 🎉
