import os.path
import pandas as pd

with open('input.txt', 'r') as f:
    content = f.readlines()

df = pd.DataFrame(columns=['variable_name', 'data_type'])

data = []
for line in content:
    port_type = line.strip().split(' ')
    port_name = line.strip().split(' ')[1].strip().split(',')
    data.append({'port_name':port_name[:len(content)],'port_type':port_type[0]})

new_df = pd.DataFrame()
for i in range(len(content)):
    new_df = pd.concat([pd.DataFrame.from_dict(data[i]),new_df])

patterns = {
            ######### Read Handlers ##########
            'IOS_read_handle_sint32':'sint32',
            'IOS_read_handle_uint32':'uint32',
            'IOS_read_handle_float32':'float32',
            'IOS_read_handle_float64':'float64',
            'IOS_read_handle_bool':'bool',
            'IOS_read_handle_binary':'binary',
            'IOS_read_handle_uint8':'uint8',
            'IOS_read_handle_uint16':'uint16',
            'IOS_read_handle_uint64':'uint64',
            'IOS_read_handle_sint8':'sint8',
            'IOS_read_handle_sint16':'sint16',
            'IOS_read_handle_sint64':'sint64',
            'IOS_read_handle_val_float64':'float64',
            'IOS_read_handle_val_uint32':'uint32',
            'IOS_read_handle_val_string':'string',
            'IOS_read_handle_val_float32':'float32',
            'IOS_read_handle_val_uint8': 'uint8',
            'IOS_read_handle_val_uint16':'uint16',
            'IOS_read_handle_val_uint64':'uint64',
            'IOS_read_handle_val_sint8':'sint8',
            'IOS_read_handle_val_sint16':'sint16',
            'IOS_read_handle_val_sint64':'sint64',
            'IOS_read_handle_val_bool': 'bool',
            ############ Write Handlers ###############
            'IOS_write_handle_sint32':'sint32',
            'IOS_write_handle_uint32':'uint32',
            'IOS_write_handle_float32':'float32',
            'IOS_write_handle_float64':'float64',
            'IOS_write_handle_bool':'bool',
            'IOS_write_handle_binary':'binary',
            'IOS_write_handle_val_float64':'float64',
            'IOS_write_handle_val_uint32':'uint32',
            'IOS_write_handle_val_sint32':'sint32',
            'IOS_write_handle_val_string':'string',
            'IOS_write_handle_val_uint16':'uint16',
            'IOS_write_handle_val_uint64':'uint64',
            'IOS_write_handle_val_sint8':'sint8',
            'IOS_write_handle_val_sint16':'sint16',
            'IOS_write_handle_val_sint64':'sint64',
            'IOS_write_handle_val_float32': 'float32',
            'IOS_write_handle_val_uint8': 'uint8',
            'IOS_write_handle_val_bool': 'bool',
            }
symbol = ';'

df1 = new_df.replace({'port_type': patterns})
df1['port_name'] = df1['port_name'].str.replace(symbol, '')
df1 = df1.sort_values('port_type')

def custom_dtype_size(x):
    if x == 'bool':
        return 1
    elif x == 'float32':
        return 4
    elif x == 'float64':
        return 8
    elif x == 'uint8':
        return 1
    elif x == 'uint16':
        return 2
    elif x == 'uint32':
        return 4
    elif x == 'uint64':
        return 8
    elif x == 'sint8':
        return 1
    elif x == 'sint16':
        return 2
    elif x == 'sint32':
        return 4
    elif x == 'sint64':
        return 8
    elif x == 'binary':
        return 1
    elif x == 'string':
        return None
    else:
        return None
    
df1['dtype_size'] = df1['port_type'].apply(custom_dtype_size).astype(int)

df1['rate'] = 10
df1['zero1'] = 0
df1['false1'] = 'FALSE'
df1['false2'] = 'FALSE'
df1['false3'] = 'FALSE'
df1['zero2'] = 0
df1['zero3'] = 0
df1['zero4'] = 0
df1['NA'] = 'NA'
df1.insert(0, 'Six', 6)
df1.insert(1, 'Test1', 'Test_01')
df1.insert(2, 'Test2', 'Test_01')
df1.insert(3, 'partition1', 'partition')
df1.insert(4, 'partition2', 'partition')

append_string = lambda x: x + '.1'
df1['port_name'] = df1['port_name'].apply(append_string)

file_path = 'Custom_Input_SMC.csv'

if os.path.isfile(file_path):
    df1.to_csv(file_path, mode='a', header=False, index=False)
else:
    df1.to_csv(file_path, header=False, index=False)