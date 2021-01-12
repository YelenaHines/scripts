from random_num_generate import generate_random_reading as grr


LVL_C_NEG = ['0I3', '0I4', '0J3', '0J4', '0K3', '0K4', '0L3', '0L4']
LVL_C_POS = ['0M3', '0M4', '0N3', '0N4', '0O3', '0O4', '0P3', '0P4']
MVL_C_NEG = ['I23', 'I24', 'J23', 'J24', 'K23', 'K24', 'L23', 'L24']
MVL_C_POS = ['M23', 'M24', 'N23', 'N24', 'O23', 'O24', 'P23', 'P24']
HVL_C_NEG = ['A21', 'A22',  'B21', 'B22',  'C21', 'C22',  'D21', 'D22',  'E21', 'E22', 'F21', 'F22', 'G21', 'G22',  'H21', 'H22', 'I21', 'I22', 'J21', 'J22', 'K21', 'K22', 'L21', 'L22', 'M21', 'M22', 'N21', 'N22', 'O21', 'O22', 'P21', 'P22']
HVL_C_POS = ['A23', 'A24', 'B23', 'B24', 'C23', 'C24', 'D23', 'D24', 'E23', 'E24', 'F23', 'F24', 'G23', 'G24', 'H23', 'H24'] + MVL_C_NEG + MVL_C_POS
CHANNELS = ['1A', '1B', '2B']

def choose_ctrl_neg(volume, channel):
    return_neg_dict = {}
    
    if volume == "LVL":
        for well in LVL_C_NEG: 
            return_neg_dict[channel+well] = (str(grr(channel, 'NEG')))
    elif volume == 'MVL':
        for well in MVL_C_NEG:
            return_neg_dict[channel+well] = (str(grr(channel, 'NEG')))
    elif volume == 'HVL':
        for well in HVL_C_NEG:
            return_neg_dict[channel+well] = (str(grr(channel, 'NEG')))
    
    return return_neg_dict

def choose_ctrl_pos(volume, channel):
    return_pos_dict = {}
    
    if volume == 'LVL':
        for well in LVL_C_POS:
            return_pos_dict[channel+well] = (str(grr(channel, 'POS')))
    elif volume == 'MVL':
        for well in MVL_C_POS:
            return_pos_dict[channel+well] = (str(grr(channel, 'POS')))
    elif volume == 'HVL':
        for well in HVL_C_POS:
            return_pos_dict[channel+well] = (str(grr(channel, 'POS')))
    
    return return_pos_dict

def get_unexp_ctrl_well(volume, fail_for="NEG", endo="N"):
    ''' return list of strings of which wells to change so that the well will score as a fail '''
    
    return_list = []
    
    if volume == "LVL" and fail_for == "NEG":
        for chan in CHANNELS:
            for i in range(4):
                return_list.append((chan + LVL_C_NEG[i]))

    elif volume == 'LVL' and fail_for == 'POS':
        for chan in CHANNELS:
            for i in range(4):
                return_list.append((chan + LVL_C_POS[i]))
    
    elif volume == 'MVL' and fail_for == 'NEG':
        for chan in CHANNELS:
            for i in range(4):
                return_list.append((chan + MVL_C_NEG[i]))
    
    elif volume == 'MVL' and fail_for == 'POS':
        for chan in CHANNELS:
                for i in range(4):
                    return_list.append((chan + MVL_C_POS[i]))
    
    elif volume == 'HVL' and fail_for == 'NEG':
        for chan in CHANNELS:
            if endo == "N":
                for i in range(8):
                    return_list.append((chan + HVL_C_NEG[i]))
            elif endo == "Y":
                for i in range(16):
                    return_list.append((chan + HVL_C_NEG[i]))
                
    elif volume == 'HVL' and fail_for == 'POS':
        for chan in CHANNELS:
            for i in range(8):
                return_list.append((chan + HVL_C_POS[i]))
    
    return return_list

# def get_endo_wells(volume):
#     ''' get negative controls wells that should be positive for endogenous assays '''
    
#     return_list = []
    
#     if volume == "LVL":
#         for chan in CHANNELS:
#             for i in range(4):
#                 return_list.append((chan + LVL_C_NEG[i]))
    
#     elif volume == "MVL":
#         for chan in CHANNELS:
#             for i in range(4):
#                 return_list.append((chan + MVL_C_NEG[i]))
    
#     elif volume == "HVL":
#         for chan in CHANNELS:
#             for i in range(16):
#                 return_list.append((chan + HVL_C_NEG[i]))
    
#     return return_list
