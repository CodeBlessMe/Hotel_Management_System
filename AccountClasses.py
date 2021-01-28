class wallet:

    #constructor
    def __init__(self):
        self.data = []
        self.count = 0

    #add a new category to the wallet
    def addcategory(self,text):
        datacategory = [text,]
        self.data.append(datacategory)
        self.count += 1
   
    #delete a category from the wallet
    def deletecategory(self,category):
        n = self.findcategory(category)
        if (n >= 0):
            del self.data[n]
        else:
            print('There isn\'t this category.')
    
    #find above category from the wallet
    def findcategory(self, category):
        count = 0
        for i in self.data:
            if (i[0] == category):
                return count
            count += 1
        return -1

    #get sum of payments of the wallet
    def total_payment(self):
        sum_total=0
        for i in self.data:
            for j in i[1:]:
               sum_total+=j[0]
        return sum_total

    #this function may need to be modified
    def check_category_activity(self,category,expense):
        for i in self.data:
            if i[0]==category.info:
                for j in i[1:]:
                    if j[1]==expense.activity:
                        return j[0]

    #add a new expense to a category
    def addexpense(self,category,dataexpense):
        self.data[category].append(dataexpense)
    
    def findexpense(self,payment,note):
        count_1 = 0
        count_2 = 1
        for i in self.data:
            for j in i[1:]:
                if (j[0] == payment) and (j[1] == note):
                    return [count_1,count_2]
                count_2 += 1
            count_1 += 1
        return -1

    #delete an expense
    def deleteexpense(self,payment,note):
        position = self.findexpense(payment,note)
        if (position == -1):
            print('There isn\'t this expense!')
        else:
            del self.data[position[0]][position[1]]
            print('It is deleted.')


#build an expense
class expense:

    def __init__(self, payment, text):
        self.dataexpense = [payment,text]