#Python script

"""
Write and execute a script which requests the user to input its monthly electricity consumption price per kWh.
Then, it must compute the total price to pay according to the following per-consumption price per kWh.

from 0 kWh t0 100 kWh: 0.16 EUR/kWh
from 100 kWh t0 300 kWh: 0.14 EUR/kWh
from 300 kWh t0 500 kWh: 0.12 EUR/kWh
500 kWh or mor 0.10 EUR/kWh.

Note that at the price-turning points the cheapest rate are always applied. For example, in the case of 100 kWh, the considered rate should be
0.14 EUR/kWh. Note also that all kWh are paid at the same price, that is determined according to the total consumption.

Example: If the total consumption is 114 kWh, the solution would be 'You have to pay 15.96 euros'.
"""