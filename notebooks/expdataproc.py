import numpy as np
import pandas as pd 

def proc_single(dataset):

    dataset.columns=['fluids', 'upper_rho', 'upper_nu', 'lower_rho','lower_nu', 'gamma', 'tubetype', 'D', 'Q', 'S', 'depth', 'day','temp']
    
    dataset.drop(['tubetype','depth','day','temp'], axis=1, inplace=True)
    
    dataset['Q'] = (0.00006309 * dataset['Q'])
    dataset['S'] = (0.0254 * dataset['S'])

    dataset['lower_nu'] = (dataset['lower_nu']*(1e-6))
    dataset['upper_nu'] = (dataset['upper_nu']*(1e-6))

    dataset['fluids'] = dataset.fluids.astype("category").cat.codes

    dataset['g_reduced'] = 9.81 * (1 - (dataset['upper_rho'] / dataset['lower_rho']))

    dataset['lc']= (dataset['gamma'] / (dataset['g_reduced'] * dataset['lower_rho'])) ** (1/2)
    dataset['lc_D'] = dataset['lc'] / dataset['D']
    dataset['S_D'] = dataset['S'] / dataset['D']
    dataset['S_lc'] = dataset['S'] / dataset['lc']
    
    dataset['nu_ratio'] = dataset['upper_rho'] / dataset['lower_rho']
    dataset['rho_ratio'] = dataset['upper_nu'] / dataset['lower_nu']
    
    dataset['V_tube'] = dataset['Q'] / ((np.pi/4) * (dataset['D'] ** 2))
    dataset['Re_D'] = dataset['Q'] / (dataset['lower_nu'] * dataset['D'])
    dataset['Re_lc'] = (dataset['Q'] * dataset['lc']) / (dataset['lower_nu'] * (dataset['D'] ** 2))
    

    dataset['Fr_lc'] = ((dataset['Q'] ** 2) / (dataset['g_reduced'] * dataset['lc'] * (dataset['D'] ** 4))) ** (1/2)
    dataset['Fr_D'] = ((dataset['Q'] ** 2) / (dataset['g_reduced'] * dataset['D'] * (dataset['D'] ** 4))) ** (1/2)

    dataset['We_lc'] = (dataset['lower_rho'] * dataset['lc'] * (dataset['Q'] ** 2) / (dataset['gamma'] * (dataset['D'] ** 4)))
    dataset['We_D'] = (dataset['lower_rho'] * dataset['D'] * (dataset['Q'] ** 2) / (dataset['gamma'] * (dataset['D'] ** 4)))

    dataset['Ca_lc'] = (dataset['lower_rho'] * dataset['lower_nu'] * dataset['Q']) / (dataset['gamma'] * (dataset['lc']**2))
    dataset['Ca_D'] = (dataset['lower_rho'] * dataset['lower_nu'] * dataset['Q']) / (dataset['gamma'] * (dataset['D']**2))

    dataset['Oh_lc'] = dataset['We_lc']**(1/2) / dataset['Re_lc']
    dataset['Oh_D'] = dataset['We_D']**(1/2) / dataset['Re_D']


    return dataset


def proc_utube(dataset):

    dataset.columns=['fluids', 'upper_rho', 'upper_nu', 'lower_rho','lower_nu', 'gamma', 'tubetype', 'D', 'Q', 'S', 'depth']
    dataset.drop(['tubetype','depth'], axis=1, inplace=True)

    dataset['Q'] = (0.00006309 * dataset['Q'])
    dataset['S'] = (0.0254 * dataset['S'])

    dataset['lower_nu'] = (dataset['lower_nu']*(1e-6))
    dataset['upper_nu'] = (dataset['upper_nu']*(1e-6))

    dataset['fluids'] = dataset.fluids.astype("category").cat.codes

    dataset['g_reduced'] = 9.81 * (1 - (dataset['upper_rho'] / dataset['lower_rho']))

    dataset['lc']= (dataset['gamma'] / (dataset['g_reduced'] * dataset['lower_rho'])) ** (1/2)
    dataset['lc_D'] = dataset['lc'] / dataset['D']
    dataset['S_D'] = dataset['S'] / dataset['D']
    dataset['S_lc'] = dataset['S'] / dataset['lc']
    
    dataset['nu_ratio'] = dataset['upper_rho'] / dataset['lower_rho']
    dataset['rho_ratio'] = dataset['upper_nu'] / dataset['lower_nu']
    
    dataset['V_tube'] = dataset['Q'] / ((np.pi/4) * (dataset['D'] ** 2))
    dataset['Re_D'] = dataset['Q'] / (dataset['lower_nu'] * dataset['D'])
    dataset['Re_lc'] = (dataset['Q'] * dataset['lc']) / (dataset['lower_nu'] * (dataset['D'] ** 2))
    

    dataset['Fr_lc'] = ((dataset['Q'] ** 2) / (dataset['g_reduced'] * dataset['lc'] * (dataset['D'] ** 4))) ** (1/2)
    dataset['Fr_D'] = ((dataset['Q'] ** 2) / (dataset['g_reduced'] * dataset['D'] * (dataset['D'] ** 4))) ** (1/2)

    dataset['We_lc'] = (dataset['lower_rho'] * dataset['lc'] * (dataset['Q'] ** 2) / (dataset['gamma'] * (dataset['D'] ** 4)))
    dataset['We_D'] = (dataset['lower_rho'] * dataset['D'] * (dataset['Q'] ** 2) / (dataset['gamma'] * (dataset['D'] ** 4)))

    dataset['Ca_lc'] = (dataset['lower_rho'] * dataset['lower_nu'] * dataset['Q']) / (dataset['gamma'] * (dataset['lc']**2))
    dataset['Ca_D'] = (dataset['lower_rho'] * dataset['lower_nu'] * dataset['Q']) / (dataset['gamma'] * (dataset['D']**2))

    dataset['Oh_lc'] = dataset['We_lc']**(1/2) / dataset['Re_lc']
    dataset['Oh_D'] = dataset['We_D']**(1/2) / dataset['Re_D']

    
    return dataset


def proc_cohen(dataset):
    # getting a column of fixed diameter
    dataset['D'] = pd.DataFrame(np.tile(0.0016,(len(dataset),1)),columns=['D'])
    # fixing the categorical fluid types
    dataset['fluids'] = dataset['UpperFluid'] + dataset['LowerFluid']
    dataset['fluids'] = dataset.fluids.astype("category").cat.codes
    # Dropping curvature
    dataset.drop(['Kusat_1_cm','UpperFluid','LowerFluid'], axis=1, inplace=True)

    dataset.columns = ['gamma', 'upper_rho', 'lower_rho', 'upper_nu','lower_nu', 'Q', 'S', 'D','fluids']

    dataset['gamma'] = dataset['gamma'] * 0.001

    dataset['lower_rho'] = dataset['lower_rho'] * 1000
    dataset['upper_rho'] = dataset['upper_rho'] * 1000

    dataset['Q'] = dataset['Q'] * (1e-06)
    dataset['S'] = dataset['S'] / 100

    dataset['lower_nu']=(dataset['lower_nu'] * 0.1) / dataset['lower_rho']
    dataset['upper_nu']=(dataset['upper_nu'] * 0.1) / dataset['upper_rho']

    dataset['g_reduced'] = 9.81 * (1 - (dataset['upper_rho'] / dataset['lower_rho']))

    dataset['lc']= (dataset['gamma'] / (dataset['g_reduced'] * dataset['lower_rho'])) ** (1/2)

    dataset['lc_D'] = dataset['lc'] / dataset['D']
    dataset['S_D'] = dataset['S'] / dataset['D']
    dataset['S_lc'] = dataset['S'] / dataset['lc']

    dataset['nu_ratio'] = dataset['upper_rho'] / dataset['lower_rho']
    dataset['rho_ratio'] = dataset['upper_nu'] / dataset['lower_nu']

    dataset['V_tube'] = dataset['Q'] / ((np.pi/4) * (dataset['D'] ** 2))
    dataset['Re_D'] = dataset['Q'] / (dataset['upper_nu'] * dataset['D'])
    dataset['Re_lc'] = (dataset['Q']*dataset['lc']) / (dataset['upper_nu'] * (dataset['D']**2))

    dataset['Fr_lc'] = ((dataset['Q'] ** 2) / (dataset['g_reduced'] * dataset['lc'] * (dataset['D'] ** 4))) ** (1/2)
    dataset['Fr_D'] = ((dataset['Q'] ** 2) / (dataset['g_reduced'] * dataset['D'] * (dataset['D'] ** 4))) ** (1/2)
    #dataset['Fr_D_2_5'] = dataset['Fr_D'] ** (2/5)
        

    dataset['We_lc'] = (dataset['upper_rho'] * dataset['lc'] * (dataset['Q'] ** 2) / (dataset['gamma'] * (dataset['D'] ** 4)))
    dataset['We_D'] = (dataset['upper_rho'] * dataset['D'] * (dataset['Q'] ** 2) / (dataset['gamma'] * (dataset['D'] ** 4)))

    dataset['Ca_lc'] = (dataset['upper_rho'] * dataset['upper_nu'] * dataset['Q']) / (dataset['gamma'] * (dataset['lc']**2))
    dataset['Ca_D'] = (dataset['upper_rho'] * dataset['upper_nu'] * dataset['Q']) / (dataset['gamma'] * (dataset['D']**2))

    dataset['Oh_lc'] = dataset['We_lc']**(1/2) / dataset['Re_lc']
    dataset['Oh_D'] = dataset['We_D']**(1/2) / dataset['Re_D']


    return dataset


def proc_lubin(dataset):

    dataset['D'] = dataset['a']
    dataset['upper_rho'] = dataset['rhoU']
    dataset['lower_rho'] = dataset['rhoL']
    dataset['upper_nu'] = dataset['viscU'] / dataset['upper_rho']
    dataset['lower_nu'] = dataset['viscL'] / dataset['lower_rho']
    dataset['gamma'] = dataset['Gamma']
    
    dataset['g_reduced'] = 9.81 * (1 - (dataset['upper_rho'] / dataset['lower_rho']))

    dataset['lc']= (dataset['gamma'] / (dataset['g_reduced'] * dataset['lower_rho'])) ** (1/2)
    dataset['lc_D'] = dataset['lc'] / dataset['D']

    dataset['S_D'] = (1 / dataset['a_Hc']) * 0.5
    dataset['S'] = dataset['S_D'] * dataset['D']
    dataset['S_lc'] = dataset['S'] / dataset['lc']

    dataset['Q'] = (dataset['g_reduced'] * ((dataset['D'] / 2)**5) * dataset['Lu']) ** (1/2)
    dataset['fluids'] = dataset.FluidType.astype("category").cat.codes

    dataset.drop(['a','Lu', 'a_Hc', 'rhoU', 'rhoL', 'viscU', 'viscL', 'Gamma', 'FluidType'], axis=1, inplace=True)

    
    dataset['nu_ratio'] = dataset['upper_rho'] / dataset['lower_rho']
    dataset['rho_ratio'] = dataset['upper_nu'] / dataset['lower_nu']
    
    dataset['V_tube'] = dataset['Q'] / ((np.pi/4) * (dataset['D'] ** 2))
    dataset['Re_D'] = dataset['Q'] / (dataset['lower_nu'] * dataset['D'])
    dataset['Re_lc'] = (dataset['Q'] * dataset['lc']) / (dataset['lower_nu'] * (dataset['D'] ** 2))
    

    dataset['Fr_lc'] = ((dataset['Q'] ** 2) / (dataset['g_reduced'] * dataset['lc'] * (dataset['D'] ** 4))) ** (1/2)
    dataset['Fr_D'] = ((dataset['Q'] ** 2) / (dataset['g_reduced'] * dataset['D'] * (dataset['D'] ** 4))) ** (1/2)

    dataset['We_lc'] = (dataset['lower_rho'] * dataset['lc'] * (dataset['Q'] ** 2) / (dataset['gamma'] * (dataset['D'] ** 4)))
    dataset['We_D'] = (dataset['lower_rho'] * dataset['D'] * (dataset['Q'] ** 2) / (dataset['gamma'] * (dataset['D'] ** 4)))

    dataset['Ca_lc'] = (dataset['lower_rho'] * dataset['lower_nu'] * dataset['Q']) / (dataset['gamma'] * (dataset['lc']**2))
    dataset['Ca_D'] = (dataset['lower_rho'] * dataset['lower_nu'] * dataset['Q']) / (dataset['gamma'] * (dataset['D']**2))

    dataset['Oh_lc'] = dataset['We_lc']**(1/2) / dataset['Re_lc']
    dataset['Oh_D'] = dataset['We_D']**(1/2) / dataset['Re_D']
    
    
    return dataset




if __name__ == "__main__":
    
    file_name = 'C:\\Users\\sabbi\\Dropbox\\Darryl_James\\Mendeley_library\\JetEntrainment\\Selective\\Qualifying_docs\\SW_Python\\input\\cohen.csv' 
    data_cohen = pd.read_csv(file_name)
    data_cohen = proc_cohen(data_cohen)
    print(data_cohen.head())
    print(data_cohen.shape)
    print("Done")

    file_name = 'C:\\Users\\sabbi\\Dropbox\\Darryl_James\\Mendeley_library\\JetEntrainment\\Selective\\Qualifying_docs\\SW_Python\\input\\single.csv' 
    data_single = pd.read_csv(file_name)
    data_single = proc_single(data_single)
    print(data_single.head())
    print(data_single.shape)
    print("Done")

    file_name = 'C:\\Users\\sabbi\\Dropbox\\Darryl_James\\Mendeley_library\\JetEntrainment\\Selective\\Qualifying_docs\\SW_Python\\input\\utube.csv' 
    data_utube = pd.read_csv(file_name)
    data_utube = proc_utube(data_utube)
    print(data_utube.head())
    print(data_utube.shape)
    print("Done")

    file_name = 'C:\\Users\\sabbi\\Dropbox\\Darryl_James\\Mendeley_library\\JetEntrainment\\Selective\\Qualifying_docs\\SW_Python\\input\\Lubin_Data.csv' 
    data_lubin = pd.read_csv(file_name)
    data_lubin = proc_lubin(data_lubin)
    print(data_lubin.head())
    print(data_lubin.shape)
    print("Done")

