class Helpers:

    @staticmethod
    def search(items_list,item_id,item_key): 
        for item in items_list:
            if item[item_key] == int(item_id):
                return item  

    @staticmethod
    def gen_id(items_list,item_key):
        if len(items_list) == 0:
            item_id  = 1
            return item_id
        else:
            ##setting id if list is not empty
            last_dict = items_list[len(items_list)-1]
            id = int(last_dict[item_key])
            item_id = int(id + 1)
            return item_id

    @staticmethod
    def gen_price(weight):
	    if weight > 1000:
		    return 'Weight exceeded'
	    if weight < 0 :
		    return 'weight should not be zero'
	    if weight <= 20:
		    return 5000
	    if weight <=50:
		    return 10000
	    if weight <=100:
		    return 15000
	    if weight > 100:
		    return 20000

    staticmethod
    def validate_strings(args):
        for i in args:
            if not isinstance(i,str) or i.isspace():
                return 'Data provided not a string and should not be a space'

    staticmethod
    def validate_integer(args):
        for i in args:
            if not isinstance(i,int) or i < 0:
                return 'Data provided not an integer and should not be a positive number'
    @staticmethod    
    def modify_status(mylist,key,new_entry,parcelId):
	    for i in mylist:
		    if i[key] == 1:
			    i['status'] = new_entry
	    return mylist
