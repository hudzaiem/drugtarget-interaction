import pandas as pd
import numpy as np
from rdkit.Chem import MACCSkeys,Draw, PandasTools

def to_maccs(smiles):
    '''
    This function is used to conver smiles to maccs

    Args:
        smiles (string) : smiles that want to convert to maccs
    return:
        array: array of maccs
    '''
    smiles = [smiles]
    df = pd.DataFrame(smiles, columns=['smiles'])
    PandasTools.AddMoleculeColumnToFrame(df,'smiles','structure')
    MACCS = MACCSkeys.GenMACCSKeys(df.structure[0])
    return np.array(MACCS)

def make_dataframe(MACCS):
    '''
    This function us used to make data test from extracted smiles combined to aac protein
    
    Args:
        MACCS (string) : MACCS feature that done from to_maccs function
        df (dataframe): from aac extraction protein dataframe
    return:
        dataframe : df_predict that ready to predict
    '''
    df_aac = pd.read_csv('static/dataset/protein_aac.csv')
    df_predict = df_aac.copy()
    df_predict.drop(columns='uniprot_id', inplace= True)
    df_predict['id'] = 'id'
    df_temp = pd.DataFrame([np.array(MACCS)])
    df_temp['id'] = 'id'
    df_predict = df_predict.merge(df_temp, on='id')
    df_predict.drop(columns='id', inplace=True)
    return df_predict

