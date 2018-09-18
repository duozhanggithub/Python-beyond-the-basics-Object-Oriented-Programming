#data science method in OOP way

class MovingAverage():

    def __init__(self,
                 symbol,
                 bars,
                 short_window,
                 long_window):

        self.symbol = symbols
        self.bars = bars
        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(self):
        signals = pd.DataFrame(index=self.bars.index)
        signals['signal'] = 0.0
        signals['short_mavg'] = self.bars['Close'].rolling(window=self.short_window, min_periods=1, center=False).mean()
        signals['long_mavg'] = self.bars['Close'].rolling(window=self.long_window, min_periods=1, center=False).mean()
        signals['signal'][self.short_window:] = np.where(signals['short_mavg'][self.short_window:] > signals['long_mavg'][self.short_window:], 1.0, 0.0)
        signals['positions'] = signals['signal'].diff()


class MyLinearRegression():
    def __init__(self, _fit_intercept=True):
        self.coef_ = None
        self.intercept_ = None
        self._fit_intercept = fit_intercept

    def fit(self, X, y):
        if len(X.shape) == 1:
            X = X.reshape(-1, 1)

        if self._fit_intercept:
            X = np.c_[np.ones(X.shape[0]), X]

        xTx = np.dot(X.T, X)
        inverse_xTx = np.linalg.inv(xTx)
        xTy = np.dot(X.T, y)
        coef = np.dot(inverse_xTx, xTy)

        if self._fit_intercept:
            self.intercept_ = coef[0]
            self.coef_ = coef[1:]
        else:
            self.intercept_ = 0
            self.coef_ = coef

    def predict(self, X):

        if len(X.shape) == 1:
            X = X.reshape(-1, 1)
        return self.intercept_ + np.dot(X, self.coef_)

#call functions in class
class Test():
    def __init__(self, a, b):
        self.a=a
        self.b=b

    def plus(self, para):
        return para + 2

    def mutiple(self):
        return self.a * self.plus(self.b)

test = Test(2,3)
print(test.mutiple())
