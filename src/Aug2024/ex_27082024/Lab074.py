my_shopping_list =["bread","milk","butter"]

print (my_shopping_list[0])
print(len(my_shopping_list))

def bring_more_item(my_list):
    more_item=("Enter new item \n")
    my_list.append(more_item)
    print(my_list)
    my_list.remove(more_item)
    print(my_list)
    return 


    bring_more_item()



