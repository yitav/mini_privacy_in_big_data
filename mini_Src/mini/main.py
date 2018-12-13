
import re
from mini.taxonomies import attributes_array_by_order_database
from mini.taxonomies import attributes_array_int_then_string
from mini.taxonomies import list_num
from mini.helper_funcs import remove_nodes_under_k,map_iterator_int,map_iterator_str, generalize_S
from mini.k_anon import k_anon


from mini.algorithm_6_7 import algorithm_7,algorithm_6
from mini.algorithm_6_7 import algorithm_6_test
from mini.algorithm_4 import algorithm_4
from mini.algorithm_2 import algorithm_2
from mini.test_taxonomies import *
import copy

from mini.hierarchical_clustering import single_linkage_clustering
from mini.hierarchical_clustering import num


def convert_from_newmap_to_oldmap(map_num):
    if map_num["children"] == []:
        num = map_num["data"][0]
        return {"data":[num,num] , "children":[],"index":[]}
    else:
        minVal = min(map_num["data"])
        maxVal = max(map_num["data"])
        return {"data":[minVal , maxVal] , 
                "children":list(map(convert_from_newmap_to_oldmap , map_num["children"])) }


def make_int_lists(list_num):
    with open("./big_database.txt") as f: 
        i = 1
        for line in f:
            line_arr = re.split(", |\\n",line)
            #line_arr = line.split(", ")
            if "?" in line_arr:
                i = i + 1
                continue 
            for j in range(0,len(attributes_array_by_order_database)):
                current_row = attributes_array_by_order_database[j]
                index_of_int = attributes_array_int_then_string.index(current_row)
                if index_of_int in range(0,len(list_num)):
                    #print(line_arr[j])
                    list_num[index_of_int].append(num(line_arr[j]))   
            i = i + 1
    f.close()
    return list_num

def make_new_int_maps(list_num , attributes_array_by_order_database, attributes_array_int_then_string ):
    for i  in range(0 , len(list_num)):
        hierarchical_clustering_i = single_linkage_clustering(list_num[i])
        new_map_i = convert_from_newmap_to_oldmap(hierarchical_clustering_i)
        curr_map = attributes_array_int_then_string[i]
        index_in_order = attributes_array_by_order_database.index(curr_map)
        attributes_array_by_order_database[index_in_order] = new_map_i
        attributes_array_int_then_string[i] = new_map_i

#print(attributes_array_int_then_string)

#print(lists_num)

#make_new_int_maps(lists_num , attributes_array_int_then_string , attributes_array_by_order_database )

print("Enter k")
k = num(input())
#print(algorithm_6_test(3,[DB_test]))
#print(attributes_array_by_order_database[4])#age map
'''
def algorithm_6(database_path,k,attributes_array_by_order_database,attributes_array_int_then_string):
    step 1
    with open(database_path) as f: 
        i = 1
        relevant_indexes = set()
        for line in f:
            line_arr = re.split(", |\\n",line)
            if "?" in line_arr:
                i = i + 1
                continue 
            for j in range(0,len(attributes_array_by_order_database)):
                current_row = attributes_array_by_order_database[j]
                if attributes_array_int_then_string.index(current_row) in range(0,1):
                    map_iterator_int(line_arr[j],i,current_row)
                else:
                    map_iterator_str(line_arr[j],i,current_row)
            relevant_indexes.add(i)        
            i = i + 1
    f.close()
            
    step 2
    list(map(lambda n:remove_nodes_under_k(n,k),attributes_array_by_order_database))
     steps 5-9
    attributes_map = {"data": "root", "children": attributes_array_by_order_database}
    processed = []
    F_cf = []
    F_cf = algorithm_7(attributes_map, k, processed,F_cf)
    return (F_cf, relevant_indexes)
  '''  

def algorithm_5(database_path, k, attributes_array_by_order_database):
    (F_cf, relevant_indexes, lines_in_database) = algorithm_6(database_path,k,attributes_array_by_order_database,attributes_array_int_then_string)
    cover = algorithm_4(relevant_indexes, F_cf,k, database_path,attributes_array_by_order_database)
    cluster = algorithm_2(k,cover)
    k_anon(database_path, cluster, relevant_indexes,attributes_array_by_order_database, lines_in_database)
    
   
    
  
'''
list_num = [list_age]
lists_num = make_int_lists(list_num)    
make_new_int_maps(lists_num , DB_test1, DB_test2 )
(F_cf, relevant_indexes) = algorithm_6("./database",k,DB_test1,DB_test2)
print(F_cf)
print(algorithm_4(relevant_indexes, F_cf, k, "./database",DB_test1))
'''


lists_num = make_int_lists(list_num)
make_new_int_maps(lists_num , attributes_array_by_order_database, attributes_array_int_then_string )

'''
(F_cf, relevant_indexes, i) = algorithm_6("./big_database.txt",k,attributes_array_by_order_database,attributes_array_int_then_string)
print("F_cf: ", F_cf)
cover = algorithm_4(relevant_indexes, F_cf, k, "./big_database.txt",attributes_array_by_order_database)
print("cover: ", cover)
cluster = algorithm_2(k,cover)
print("cluster: ", cluster)
'''
algorithm_5("./big_database.txt", k, attributes_array_by_order_database)




