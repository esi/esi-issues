# Warp-in Points

A warp-in point is where your ship will land in space when warping to an object.

Many external factors may disrupt a warp, e.g. warp disruption fields, insufficient electrical capacity, warp jitter, etc.; these formulas do not account for these phenomenas, they assume perfect conditions.

## Ordinary Objects

An ordinary object is any object that does not fall withing any of the other categories described below.

Let the 3D vectors ``$ p_d $`` and ``$ p_s $`` represent the object's position and the warp's origin, respectively; and ``$ \vec{v} $`` the directional vector from ``$ p_s $`` to ``$ p_d $``. Let ``$ r $`` be the object's radius.

The object's warp-in point is the vector ``$ p_s + \vec{v} - r\hat{v} $``.

## Large Objects

A large object is any celestial body whose radius exceeds 90 kilometres (180 kilometres in diameter), except planets.

Let ``$ x $``, ``$ y $``, and ``$ z $`` represent the object's coordinates. Let ``$ r $`` be the object's radius.

The object's warp-in point is the vector ``$ \left(x + (r + 5000000)\cos{r} \\,
  y + 1.3r - 7500 \\,
  z - (r + 5000000)\sin{r} \\  \right). $``

## Planets

The warp-in point of a planet is determined by the planet's ID, its location, and radius.

Let ``$ x $``, ``$ y $``, and ``$ z $`` represent the planet's coordinates. Let ``$ r $`` be the planet's radius.

The planet's warp-in point is the vector ``$ \left(x + d \sin{\theta}, y + \frac{1}{2} r \sin{j}, z - d \cos{\theta}\right) $``
where:

```math
d = r(s + 1) + 1000000
```
```math
 \theta = \sin^{-1}\left(\frac{x}{|x|} \cdot \frac{z}{\sqrt{x^2 + z^2}}\right) + j
```
```math
 s|_{0.5 \leq s \leq 10.5} = 20\left(\frac{1}{40}\left(10\log_{10}\left(\frac{r}{10^6}\right) - 39\right)\right)^{20} + \frac{1}{2}
```

Now, ``$ j $`` is a special snowflake. Its value is the Python equivalent of<br/>
`(random.Random(planetID).random() - 1.0) / 3.0`.

### Example Implementation

```python
import math
import random

def warpin(id, x, y, z, r):
    j = (random.Random(id).random() - 1.0) / 3.0
    t = math.asin(x/abs(x) * (z/math.sqrt(x**2 + z**2))) + j
    s = 20.0 * (1.0/40.0 * (10 * math.log10(r/10**6) - 39))**20.0 + 1.0/2.0
    s = max(0.5, min(s, 10.5))
    d = r*(s + 1) + 1000000

    return (x + d * math.sin(t), y + 1.0/2.0 * r * math.sin(j), z - d * math.cos(t))
```

# Skillpoints

## Skillpoints needed per level

The skillpoints needed for a level depend on the skill rank.

```math
 y_{skillpoints} = 2^{2.5(x_{skilllevel}-1)} \cdot 250 \cdot r_{skillrank}
 ```

### Skillpoints for common ranks

<table>
<thead>
<tr><th>Rank</th><th>Level 1</th><th>Level 2</th><th>Level 3</th><th>Level 4</th><th>Level 5</th></tr>
</thead>
<tbody>
<tr><th>1</th> <td>250</td>  <td>1.414</td> <td>8.000</td>  <td>45.254</td> <td>256.000</td></tr>
<tr><th>2</th> <td>500</td>  <td>2.828</td> <td>16.000</td> <td>90.509</td> <td>512.000</td></tr>
<tr><th>3</th> <td>750</td>  <td>4.242</td> <td>24.000</td> <td>135.764</td><td>768.000</td></tr>
<tr><th>4</th> <td>1.000</td><td>5.656</td> <td>32.000</td> <td>181.019</td><td>1.024.000</td></tr>
<tr><th>5</th> <td>1.250</td><td>7.071</td> <td>40.000</td> <td>226.274</td><td>1.280.000</td></tr>
<tr><th>6</th> <td>1.500</td><td>8.485</td> <td>48.000</td> <td>271.529</td><td>1.536.000</td></tr>
<tr><th>7</th> <td>1.750</td><td>9.899</td> <td>56.000</td> <td>316.783</td><td>1.792.000</td></tr>
<tr><th>8</th> <td>2.000</td><td>11.313</td><td>64.000</td> <td>362.038</td><td>2.048.000</td></tr>
<tr><th>9</th> <td>2.250</td><td>12.727</td><td>72.000</td> <td>407.293</td><td>2.304.000</td></tr>
<tr><th>10</th><td>2.500</td><td>14.142</td><td>80.000</td> <td>452.548</td><td>2.560.000</td></tr>
<tr><th>11</th><td>2.750</td><td>15.556</td><td>88.000</td> <td>497.803</td><td>2.816.000</td></tr>
<tr><th>12</th><td>3.000</td><td>16.970</td><td>96.000</td> <td>543.058</td><td>3.072.000</td></tr>
<tr><th>13</th><td>3.250</td><td>18.384</td><td>104.000</td><td>588.312</td><td>3.328.000</td></tr>
<tr><th>14</th><td>3.500</td><td>19.798</td><td>112.000</td><td>633.567</td><td>3.584.000</td></tr>
<tr><th>15</th><td>3.750</td><td>21.213</td><td>120.000</td><td>678.822</td><td>3.840.000</td></tr>
<tr><th>16</th><td>4.000</td><td>22.627</td><td>128.000</td><td>724.077</td><td>4.096.000</td></tr>
</tbody>
</table>

## Skillpoints per minute

The skillpoints generated each minute depend on the primary ``$ (a_{primary}) $`` and secondary attribute ``$ (a_{secondary}) $`` of the skill.

```math
y_{skillpointsPerMinute} = a_{primary} + {a_{secondary} \over 2}
```

# Combat

## Target lock time

The target lock time (`$ t_{targetlock} $`) in seconds depends on the ship's scan resolution (`$ s $`) and the target's signature radius (`$ r $`)

```math
t_{targetlock} = {40000 \over s \cdot asinh(r)^2}
```

## Alignment time

The ship alignment time (`$ t_{align} $`) depends on the ship's inertia modifier (`$ i $`) and the ships mass (`$ m $`)

```math
t_{align} = { ln(2) \cdot i \cdot m \over 500000 }
```
