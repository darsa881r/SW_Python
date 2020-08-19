import numpy as np
import pandas as pd 

def proc_single(dataset):
    dataset.columns=['fluids', 'upper_rho', 'upper_nu', 'lower_rho','lower_nu', 'gamma', 'tubetype', 'dia', 'Q', 'S', 'depth', 'day','temp']
    dataset.drop(['tubetype','depth','day','temp'], axis=1, inplace=True)
    dataset['Q'] = (0.00006309 * dataset['Q'])
    dataset['S'] = (0.0254 * dataset['S'])
    dataset['lower_nu'] = (dataset['lower_nu']*(1e-6))
    dataset['upper_nu'] = (dataset['upper_nu']*(1e-6))
    dataset['fluids'] = dataset.fluids.astype("category").cat.codes
    dataset['g_reduced'] = 9.81 * (1 - (dataset['upper_rho'] / dataset['lower_rho']))
    dataset['lc']= (dataset['gamma'] / (dataset['g_reduced'] * dataset['lower_rho'])) ** (1/2)
    dataset['lc_d'] = dataset['lc'] / dataset['dia']
    dataset['S_d'] = dataset['S'] / dataset['dia']
    dataset['S_lc'] = dataset['S'] / dataset['lc']
    dataset['nu_ratio'] = dataset['upper_rho'] / dataset['lower_rho']
    dataset['rho_ratio'] = dataset['upper_nu'] / dataset['lower_nu']
    dataset['V_tube'] = dataset['Q'] / ((np.pi/4) * (dataset['dia'] ** 2))
    dataset['Re_lc'] = (dataset['Q'] * dataset['lc']) / (dataset['lower_nu'] * (dataset['dia'] ** 2))
    dataset['Fr_lc'] = ((dataset['Q'] ** 2) / (dataset['g_reduced'] * dataset['lc'] * (dataset['dia'] ** 4))) ** (1/2)
    dataset['Fr_dia'] = ((dataset['Q'] ** 2) / (dataset['g_reduced'] * dataset['dia'] * (dataset['dia'] ** 4))) ** (1/2)
    dataset['We_lc'] = (dataset['lower_rho'] * dataset['lc'] * (dataset['Q'] ** 2) / (dataset['gamma'] * (dataset['dia'] ** 4)))
    dataset['We_lc_1_5'] = dataset['We_lc'] ** (1/5)
    return dataset


def proc_utube(dataset):
    dataset.columns=['fluids', 'upper_rho', 'upper_nu', 'lower_rho','lower_nu', 'gamma', 'tubetype', 'dia', 'Q', 'S', 'depth']
    dataset.drop(['tubetype','depth'], axis=1, inplace=True)
    dataset['Q'] = (0.00006309 * dataset['Q'])
    dataset['S'] = (0.0254 * dataset['S'])
    dataset['lower_nu'] = (dataset['lower_nu']*(1e-6))
    dataset['upper_nu'] = (dataset['upper_nu']*(1e-6))
    dataset['fluids'] = dataset.fluids.astype("category").cat.codes
    dataset['g_reduced'] = 9.81 * (1 - (dataset['upper_rho'] / dataset['lower_rho']))
    dataset['lc']= (dataset['gamma'] / (dataset['g_reduced'] * dataset['lower_rho'])) ** (1/2)
    dataset['lc_d'] = dataset['lc'] / dataset['dia']
    dataset['S_d'] = dataset['S'] / dataset['dia']
    dataset['S_lc'] = dataset['S'] / dataset['lc']
    dataset['nu_ratio'] = dataset['upper_rho'] / dataset['lower_rho']
    dataset['rho_ratio'] = dataset['upper_nu'] / dataset['lower_nu']
    dataset['V_tube'] = dataset['Q'] / ((np.pi/4) * (dataset['dia'] ** 2))
    dataset['Re_lc'] = (dataset['Q'] * dataset['lc']) / (dataset['lower_nu'] * (dataset['dia'] ** 2))
    dataset['Fr_lc'] = ((dataset['Q'] ** 2) / (dataset['g_reduced'] * dataset['lc'] * (dataset['dia'] ** 4))) ** (1/2)
    dataset['Fr_dia'] = ((dataset['Q'] ** 2) / (dataset['g_reduced'] * dataset['dia'] * (dataset['dia'] ** 4))) ** (1/2)
    dataset['We_lc'] = (dataset['lower_rho'] * dataset['lc'] * (dataset['Q'] ** 2) / (dataset['gamma'] * (dataset['dia'] ** 4)))
    dataset['We_lc_1_5'] = dataset['We_lc'] ** (1/5)
    return dataset


def proc_cohen(dataset):
    dataset['dia'] = pd.DataFrame(np.tile(0.0016,(len(dataset),1)),columns=['dia'])
    dataset['fluids'] = dataset['UpperFluid'] + dataset['LowerFluid']
    dataset['fluids'] = dataset.fluids.astype("category").cat.codes
    dataset.drop(['Kusat_1_cm','UpperFluid','LowerFluid'], axis=1, inplace=True)
    dataset.columns = ['gamma', 'upper_rho', 'lower_rho', 'upper_nu','lower_nu', 'Q', 'S', 'dia','fluids']
    dataset['gamma'] = dataset['gamma'] * 0.001
    dataset['lower_rho'] = dataset['lower_rho'] * 1000
    dataset['upper_rho'] = dataset['upper_rho'] * 1000
    dataset['Q'] = dataset['Q'] * (1e-06)
    dataset['S'] = dataset['S'] / 100
    dataset['lower_nu']=(dataset['lower_nu'] * 0.1) / dataset['lower_rho']
    dataset['upper_nu']=(dataset['upper_nu'] * 0.1) / dataset['upper_rho']
    dataset['g_reduced'] = 9.81 * (1 - (dataset['upper_rho'] / dataset['lower_rho']))
    dataset['lc']= (dataset['gamma'] / (dataset['g_reduced'] * dataset['lower_rho'])) ** (1/2)
    dataset['lc_d'] = dataset['lc'] / dataset['dia']
    dataset['S_d'] = dataset['S'] / dataset['dia']
    dataset['S_lc'] = dataset['S'] / dataset['lc']
    dataset['nu_ratio'] = dataset['upper_rho'] / dataset['lower_rho']
    dataset['rho_ratio'] = dataset['upper_nu'] / dataset['lower_nu']
    dataset['V_tube'] = dataset['Q'] / ((np.pi/4) * (dataset['dia'] ** 2))
    dataset['Re_d'] = dataset['Q'] / (dataset['lower_nu'] * dataset['dia'])
    dataset['Fr_lc'] = ((dataset['Q'] ** 2) / (dataset['g_reduced'] * dataset['lc'] * (dataset['dia'] ** 4))) ** (1/2)
    dataset['Fr_dia'] = ((dataset['Q'] ** 2) / (dataset['g_reduced'] * dataset['dia'] * (dataset['dia'] ** 4))) ** (1/2)
    dataset['We_lc'] = (dataset['lower_rho'] * dataset['lc'] * (dataset['Q'] ** 2) / (dataset['gamma'] * (dataset['dia'] ** 4)))
    dataset['We_lc_1_5'] = dataset['We_lc'] ** (1/5)
    return dataset



if __name__ == "__main__":
    
    file_name = 'C:\\Users\\sabbi\\Dropbox\\Darryl James\\Mendeley_library\\JetEntrainment\\Selective\\Qualifying_docs\\SW_Python\\input\\cohen.csv' 
    data_cohen = pd.read_csv(file_name)
    data_cohen = proc_cohen(data_cohen)
    print(data_cohen.head())
    print("Done")


