import random
import string

alpha = string.ascii_uppercase
ALPHABET = alpha[0:16]

channel_pos_key = {"1A":[25000, 29000], "1B":[154000, 157000], "2B":[25000, 28000]}
channel_neg_key = {"1A":[14000, 17000], "1B":[25000, 29000], "2B":[7500, 9000]}
LVL_SAMPLE_WELLS = ['0A1', '0B1', '0C1', '0D1', '0E1', '0F1', '0G1', '0H1', '0I1', '0J1', '0K1', '0L1', '0M1', '0N1', '0O1', '0P1', '0A2', '0B2', '0C2', '0D2', '0E2', '0F2', '0G2', '0H2']

def generate_random_reading(channel, result):
    ''' generate random number according to paramters set by channel and result where
        channel is either "1A", "1B" or "2B"
        result is either "POS" or "NEG" 
    '''

    rand_num = 0
    
    if result == "POS":
        for key, value in channel_pos_key.items():
            if channel == key:
                rand_num = random.randint(value[0], value[1])
    
    if result == "NEG":
        for key, value in channel_neg_key.items():
            if channel == key:
                rand_num = random.randint(value[0], value[1])
    
    return rand_num 



def generate_random_wells(volume, fail_nums=12):
    
    rand_wells = []
    
    if volume == "LVL":
        for i in range(fail_nums):
            rand_wells.append(LVL_SAMPLE_WELLS[i])
    
    return rand_wells


# list_ret = []

# channels = ['1A', '1B', '2B']
# count = 1
# while count < 10:
#     for letter in ALPHABET:
#         for chan in channels:
#             well_str_1 = '{}0{}{}'.format(chan, letter, count)
#             list_ret.append(well_str_1)
#             count += 1
# while count < 21:
#     for letter in ALPHABET:
#         for chan in channels:
#             well_str = '{}{}{}'.format(chan, letter, count)
#             list_ret.append(well_str)
#             count += 1

# print(list_ret)
        
            
            
            
        
