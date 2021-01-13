#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 12:33:20 2021

@author: yoyo
"""




def fail_few_sample(channel, num_fails, fail_cols=1):
    
    ''' return list of wells to change '''
    
    wells_list = []
    alpha_map = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    
    if num_fails > 8:
        return "max is 8"
    
    
    # num = 1
    # for well in range(num_fails):
    #     well_str = channel + "0" + alpha_map[well] + str(num)
    #     wells_list.append(well_str)
    #     if num_fails == num:
    #         return wells_list
    
    
    column = 1
    iters = 1
    for well in alpha_map[:num_fails]:
        for col in range(1, fail_cols + 1):
            well_str_1 = ''
            if col < 10:
                well_str_1 = f'{channel}0{alpha_map[iters - 1]}{col}'
            elif col >= 10:
                well_str_1 = f'{channel}{alpha_map[iters - 1]}{col}'
            wells_list.append(well_str_1)
            column += 1
        if num_fails == iters:
            return wells_list
        iters += 1
