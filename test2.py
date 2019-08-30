# import pandas as pd
# import numpy as np
import sys
from itertools import combinations, groupby
from collections import Counter
# from IPython.display import display
# from apyori import apriori
# Generator that yields item pairs, one at a time
def get_item_pairs1(order_item):
	import csv
	with open(order_item) as _in:
		f_in=csv.reader(_in)
		item_list=[]
		for line in f_in:
					item_list.append(line)
		# item_list=[]
		# i=0
		# for line in f_in.read().splitlines():
			# if not i:
				# header = line.split(',')
				# i=1
			# if  line.strip():
				# line =line.split(',')
				# item_list.append(line)
	# For each item list, generate item pairs, one at a time
	return item_list



# def item_pair(file):
	# orders = pd.read_csv('outfile1.csv')
	# orders.dropna(axis=0, how='all', inplace = True)
	
# # Returns frequency counts for items and item pairs
# def freq(iterable):
    # if type(iterable) == pd.core.series.Series:
        # return iterable.value_counts().rename("freq")
    # else: 
        # return pd.Series(Counter(iterable)).rename("freq")
		
# # Returns number of unique orders
# def order_count(order_item):
    # return len(set(order_item.index))


# # Returns generator that yields item pairs, one at a time
# def get_item_pairs(order_item):
    # order_item = order_item.reset_index().as_matrix()
    # for order_id, order_object in groupby(order_item, lambda x: x[0]):
        # item_list = [item[1] for item in order_object]
              
        # for item_pair in combinations(item_list, 2):
            # yield item_pair
            

# # Returns frequency and support associated with item
# def merge_item_stats(item_pairs, item_stats):
    # return (item_pairs
                # .merge(item_stats.rename(columns={'freq': 'freqA', 'support': 'supportA'}), left_on='item_A', right_index=True)
                # .merge(item_stats.rename(columns={'freq': 'freqB', 'support': 'supportB'}), left_on='item_B', right_index=True))


# # Returns name associated with item
# def merge_item_name(rules, item_name):
    # columns = ['itemA','itemB','freqAB','supportAB','freqA','supportA','freqB','supportB', 
               # 'confidenceAtoB','confidenceBtoA','lift']
    # rules = (rules
                # .merge(item_name.rename(columns={'item_name': 'itemA'}), left_on='item_A', right_on='item_id')
                # .merge(item_name.rename(columns={'item_name': 'itemB'}), left_on='item_B', right_on='item_id'))
    # return rules[columns]  

# def association_rules(order_item, min_support):

    # print("Starting order_item: {:22d}".format(len(order_item)))


    # # Calculate item frequency and support
    # item_stats             = freq(order_item).to_frame("freq")
    # item_stats['support']  = item_stats['freq'] / order_count(order_item) * 100


    # # Filter from order_item items below min support 
    # qualifying_items       = item_stats[item_stats['support'] >= min_support].index
    # order_item             = order_item[order_item.isin(qualifying_items)]

    # print("Items with support >= {}: {:15d}".format(min_support, len(qualifying_items)))
    # print("Remaining order_item: {:21d}".format(len(order_item)))


    # # Filter from order_item orders with less than 2 items
    # order_size             = freq(order_item.index)
    # qualifying_orders      = order_size[order_size >= 2].index
    # order_item             = order_item[order_item.index.isin(qualifying_orders)]

    # print("Remaining orders with 2+ items: {:11d}".format(len(qualifying_orders)))
    # print("Remaining order_item: {:21d}".format(len(order_item)))


    # # Recalculate item frequency and support
    # item_stats             = freq(order_item).to_frame("freq")
    # item_stats['support']  = item_stats['freq'] / order_count(order_item) * 100


    # # Get item pairs generator
    # item_pair_gen          = get_item_pairs(order_item)


    # # Calculate item pair frequency and support
    # item_pairs              = freq(item_pair_gen).to_frame("freqAB")
    # item_pairs['supportAB'] = item_pairs['freqAB'] / len(qualifying_orders) * 100

    # print("Item pairs: {:31d}".format(len(item_pairs)))


    # # Filter from item_pairs those below min support
    # item_pairs              = item_pairs[item_pairs['supportAB'] >= min_support]

    # print("Item pairs with support >= {}: {:10d}\n".format(min_support, len(item_pairs)))


    # # Create table of association rules and compute relevant metrics
    # item_pairs = item_pairs.reset_index().rename(columns={'level_0': 'item_A', 'level_1': 'item_B'})
    # item_pairs = merge_item_stats(item_pairs, item_stats)
    
    # item_pairs['confidenceAtoB'] = item_pairs['supportAB'] / item_pairs['supportA']
    # item_pairs['confidenceBtoA'] = item_pairs['supportAB'] / item_pairs['supportB']
    # item_pairs['lift']           = item_pairs['supportAB'] / (item_pairs['supportA'] * item_pairs['supportB'])
    
    
    # # Return association rules sorted by lift in descending order
    # return item_pairs.sort_values('lift', ascending=False)
def generate_radom_output():	
	import random
	import csv
	li= [False,True]
	with open('test3.csv', 'w') as writeFile:
		writer = csv.writer(writeFile)
		rows=[['a','b','c_dependon_a_b_or_e','d','e','f_dependon_c_d','g_dependon_d_e']]
		for i in range(0,500000):
			a=(random.choice(li))
			b=(random.choice(li))
			
			d=(random.choice(li))
			e=(random.choice(li))
			c_dependon_a_b_or_e= (a and b) or e
			f_dependon_c_d = c_dependon_a_b_or_e and d
			g_dependon_d_e= d and e
			rows.append([a,b,c_dependon_a_b_or_e,d,e,f_dependon_c_d,g_dependon_d_e])
		writer.writerows(rows)	
def convert():		
	import csv
	with open("test3.csv") as _in, open("associa/outfile1.csv",'w') as f_out:
		f_in=csv.reader(_in)
		head=next(f_in)
		for line in f_in:
			ou=[]
			for i,ind in enumerate(line):
				if ind =='False':
					ou.append(head[i])

			f_out.write(','.join(ou)+'\n')	
def main():
	import datetime
	start=datetime.datetime.now()
	all_item=get_item_pairs1('associa/outfile1.csv')
	from collections import Counter
	counts= Counter()
	counts.update(j for i in all_item  for j in i )
	uni = set.union(*map(set,all_item))
	print(uni)
	print(len(all_item))
	comb =combinations(uni,2)
	import csv
	with open('combined_file.csv', 'w') as outcsv:
		writer = csv.writer(outcsv)
		writer.writerow(['itemA','itemB','freqAB','supportAB','freqA','supportA','freqB','supportB', 
               'confidenceAtoB','confidenceBtoA','conclusion','lift','min_set'])
		for i in comb:
			min_set=[]
			for j in all_item:
				j = sorted(j)
				if i[0] in j and i[1] in j:
					counts.update([i[0]+'And'+i[1] ])
					if not min_set:
						min_set.append(j)
					if j not in min_set and len(j)< len(min_set[0]):
						min_set.clear()
						min_set.append(j)
					if j not in min_set and len(j)==len(min_set[0]):
						min_set.append(j)
					
			# counts.update(i[0] for j in all_item if i[0] in j)
			# counts.update(i[1] for j in all_item if i[1] in j)
			# counts.update(i[0]+'And'+i[1] for j in all_item if i[0] in j and i[1] in j)
			supportAB = counts[i[0]+'And'+i[1]] / len(all_item)
			supportB = counts[i[1]] / len(all_item)
			supportA = counts[i[0]] / len(all_item)
			confidenceAtoB = supportAB/supportA
			confidenceBtoA = supportAB/supportB
			conclusion ='Need info'
			if (confidenceAtoB > confidenceBtoA and len(min_set[0])>2 and len(min_set) >1) or \
				confidenceAtoB < confidenceBtoA  and len(min_set[0])>2 and len(min_set) >1 :
				min_se= map(set,min_set)
				intersect= set.intersection(*min_se)
				conclusion = i[0] +' depends on '+ i[1]  + ' AND ' + ' OR '.join([(' AND '.join(list(i- intersect)) ) for i in min_se])
			elif confidenceAtoB > confidenceBtoA:
				conclusion= i[1] +' depends on '+ i[0] 
			elif confidenceAtoB < confidenceBtoA: 
				conclusion=i[0] +' depends on '+ i[1] 
			writer.writerow([i[0],i[1],counts[i[0]+'And'+i[1]],supportAB,counts[i[0]],supportA,counts[i[1]],supportB,confidenceAtoB,
					confidenceBtoA,conclusion,(supportAB/(supportA*supportB)),min_set])
	print(datetime.datetime.now()-start)	
main()
# generate_radom_output()
# convert()