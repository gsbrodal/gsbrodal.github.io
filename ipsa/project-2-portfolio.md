# Project II - Portfolio optimization


[<img src="portfolio.png" width="40%" class="right">](portfolio.png)

We consider the problem of choosing a _long term_ stock portfolio, given a set of stocks and their price over some period under _risk aversion parameter_ &gamma;&nbsp;&gt;&nbsp;0.

Assume there are _m_ stocks to be considered.
The _portfolio_ will be represented by a column vector _w_ &isin; &#8477;<sup>_m_</sup>,
such that &sum;<sub>_i_=1.._m_</sub> _w_<sub>_i_</sub> = 1.
If _w_<sub>_i_</sub>&nbsp;&gt;&nbsp;0,
you use a fraction _w_<sub>_i_</sub> of your total money to buy
the _i_'th stock, while _w_<sub>_i_</sub>&nbsp;&lt;&nbsp;0
represent [shorting](https://en.wikipedia.org/wiki/Short_(finance)) that stock.
In both cases we assume the stock is bought/shorted for the entire period.

Let _p_<sub>_j_,_i_</sub> represent the price of the _i_'th stock at time step _j_.
If there are _n_&nbsp;+&nbsp;1 time steps, then _p_&nbsp;&isin;&nbsp;&#8477;<sup>(_n_+1)&times;_m_</sup> is a matrix.

We let _r_ &isin; &#8477;<sup>_n_&times;_m_</sup> be  the matrix, where _r_<sub>_j_,_i_</sub> represents the fractional reward of stock _i_ at time step _j_, i.e., _r_<sub>_j_,_i_</sub> = (_p_<sub>_j_+1,_i_</sub>&nbsp;&minus;&nbsp;_p_<sub>_j_,_i_</sub>)&nbsp;/&nbsp;_p_<sub>_j_,_i_</sub> for 1&nbsp;&le;&nbsp;_j_&nbsp;&le;&nbsp;_n_.

By _r_<sub>_j_</sub> we denote the _j_'th row of _r_, viewed as a _column vector_ (_r_<sub>_j_,1</sub>, ..., _r_<sub>_j_,_m_</sub>).

We make the (unrealistic) assumption that we can model _r_ by a _random variable_, distributed as a multivariate Gaussian, with _estimated_ means

> &mu; &#8771; 1/_n_ &middot; &sum;<sub>_j_=1.._n_</sub> _r_<sub>_j_</sub>

and _estimated covariance matrix_

> &Sigma;&nbsp;&#8771;&nbsp;1&nbsp;/&nbsp;_n_&nbsp;&middot;&nbsp;&sum;<sub>_j_=1.._n_</sub> [(_r_<sub>_j_</sub> &minus; &mu;)(_r_<sub>_j_</sub> &minus; &mu;)<sup>_T_</sup>]

Note that &mu;<sub>_i_</sub> and &Sigma;<sub>_i_,_i_</sub> are the estimated mean and variance for stock _i_.

The distribution of _returns_ using some _w_ is then

> _R_<sub>_w_</sub> = _N_(&mu;<sub>_w_</sub>, &sigma;<sub>_w_</sub><sup>2</sup>)

> &mu;<sub>_w_</sub> = _w_<sup>_T_</sup>&mu;

> &sigma;<sub>_w_</sub><sup>2</sup> = _w_<sup>T</sup>&Sigma;_w_

Now, we want to maximize for a balance between high return &mu;<sub>_w_</sub> and low risk &sigma;<sub>_w_</sub><sup>2</sup>.
This leads to the following optimization problem, where we want to find the value _w*_ of _w_ maximizing the following expresion:

> maximize&nbsp;&nbsp;&nbsp;&nbsp; _w_<sup>_T_</sup>&mu; &minus; &gamma;_w_<sup>_T_</sup>&Sigma;_w_

> subject to&nbsp;&nbsp;&nbsp;&nbsp; &sum;<sub>_i_=1.._m_</sub> _w_<sub>_i_</sub> = 1 ,

where &gamma; controls the balance between risk and return. A high value of &gamma; indicate we are willing to take low risk and vise versa.

In this project you should find _w_* for different values of &gamma; and using real stock values of your choice. 
The project consists of the following three questions.

1. We need a module for collecting stock values, for this we will use the Python modyle `yfinance` that connects to Yahoo! Finance's API. See [https://pypi.org/project/yfinance/](https://pypi.org/project/yfinance/) for a description of how to install and use the module. Using this you should write a function `get_prices([stocks, ... ], start, end, interval)`, that returns a tuple, `(stocks, prices)`. Where `prices[i, j]` represent the **opening** price of stock _j_ at time step _i_ and `stocks[j]` is the name of the _j_'th stock. Save the fetched data to a file, such that when requesting the same data again, the data is be loaded from the file instead of using the API (e.g., save a pandas dataframe as a csv file).

2. Plot the loaded price data. Each stock should be labeled with its name (for example `MSFT` or `GOOGL`). You should use at least 5 stocks. The legend should be ordered by the last price fetched for each stock. Plot both the raw stock prices and stocks normalized to all start with price 1.0.

3.  Calculate _r_, &mu; and &Sigma; using the formulas above and the prices _p_ calculated in the first question. Plot the probability density function (_pdf_) of the return of each stock.
<br>
_Hint_. The method `norm.pdf` from the module `scipy.stats` might become convenient.

4.  Solve the optimization problem defined above for different values of &gamma;, e.g., `gammas = numpy.linspace(1.0, 2.8, 10)`, and plot the _pdf_ of each solution to a single plot with appropriate legends.  Finally, create a scatter plot of how _w_* changes as &gamma; changes. For each value of &gamma; plot the fraction of
each stock in the portfolio.
