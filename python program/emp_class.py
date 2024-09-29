class emp:
    def __init__(self, eid, esal,edept ):
        self.eid =  eid
        self.esal =  esal
        self.edept =  edept
    
    def checkdetails (self):
        print("*************EMP DETAILS**********")
        print("employee id :",self.eid)
        print("employee salary :",self.esal)
        print("employee department :",self.edept)
        
emps = []
for i in range(2):
    id = int(input("please enter id :"))
    sal = int(input("please enter sal:"))
    dept = (input("please enter dept:"))
        
    e = emp( id, sal, dept)
    emps.append(e)
    
for e in emps:
    e.checkdetails()
    
    