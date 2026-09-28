import yfinance as yf
import pandas as pd
import numpy as np
from methods import get_pct_change
class Portfolio:
    def __init__(self,ptf):
        self.ptf = ptf
        # dictionary in format [Asset:Weight]
    def get_ptf(self):
        return self.ptf

    def get_assets(self):
        return self.ptf.keys()

    def get_pct_changes(self):
        assets = self.ptf.keys()
        return get_pct_change(assets)

    def get_mean_return(self):
        ptf = self.ptf
        assets = ptf.keys()
        total_weight = sum(list(ptf.values()))
        mean_return = 0
        for asset in assets:
            weight = ptf[asset]/total_weight
            mean_return += get_pct_change(assets).mean() * weight
        return mean_return

    def get_risk(self):
        ptf = self.ptf
        assets = ptf.keys()
        total_weight = sum(list(ptf.values()))
        vol_vect = []

        for asset in assets:
            weight = ptf[asset]/total_weight
            st_dev = get_pct_change(asset).std()
            vol_vect.append(weight*st_dev)

        vol_vect = np.array(vol_vect)

        asset_changes = get_pct_change(assets)
        cor_mat = asset_changes.corr(method='pearson').to_numpy()

        st_dev = ( np.dot(vol_vect,np.dot(cor_mat,np.transpose(vol_vect))) ) ** 0.5
        return st_dev









