#hola future amigo mk2.1
import logger

#todo: put in replacement logers for flow tracking

"""logging"""
def log(msg,lvl=0):
    """wraper for the logger library"""
    if log==True:
        print(logger.log(msg,lvl,__name__))
    else:
        logger.log(msg,lvl)

"""error class"""
class InvalidCoords(BaseException):
    pass

"""classes"""
class game(): 
    def __init__(self,name): 
        self.name=name
        places=[] 
        players=[] 
        self.places=places 
        self.players=players 
    def addplace(self,place): 
        if place.exists(): 
            self.places.append(place) 
        return place.exists 
        
    def addplayer(self,player): 
        if player.exists(): 
            self.players.append(player) 

        return player.exists 
        
    def coords_exist(self,x,y): 
        cond=None 
        for place in self.places: 
            if (x,y) == (place.x,place.y): 
                cond=True 
        if cond==True: 
            return True 
        elif cond==None: 
            return False 


        else: 
            pass 
         
    def gattr(self,ix,iy,attr):
        for place in self.places:
            #log((place),(place.x),(place.y))
            if (ix,iy)==(place.x,place.y):
                try:
                    if attr=="descrip":
                        log(place.descrip)
                        return place.descrip
                except:
                    pass
                 
class place(): 
    def __init__(self,name,x,y,descrip=None): 
        self.name=name 
        self.y=y 
        self.x=x 
        self.y=y 
        self.descrip=descrip 
    def exists(self): 
        return True 
        
class obj():
    def __init__ (self,name,x,y,mgeng,descrip=None,ident=[]):
        print(mgeng.coords_exist(x,y))
        if mgeng.coords_exist(x,y)==True:
            self.name=name
            self.x=x 
            self.y=y
            self.mgeng=mgeng
            self.descrip=descrip
            self.ident=ident
        else:
            raise InvalidCoords
    
class player(): 
    def __init__(self,name,x,y,management_engine): 
        self.name=name 
        self.x=x 
        self.y=y 
        self.mgeng=management_engine 
    def exists(self): 
        return True 
    def goto(self,x,y): 
        if self.mgeng.coords_exist(x,y): 
            self.x=x 
            self.y=y
        else:
            log('no such coord: '+str((x,y))+' in mg. eng. : '+str(self.mgeng))
    def look(self):
        return self.mgeng.gattr(self.x,self.y,"descrip")
            
'''            
print("dbj init")
mapp=game("mapp") 
fred=player('fred',0,0,mapp) 
dock=place('dock',0,0,"its a dock")
street=place('street',1,0,"its a street")
house=place("house",2,0,"its a old decrepit house")
boat=place(-1,0,"a rickety old motor boat")   
mapp.addplace(dock)    
mapp.addplace(street) 
mapp.addplace(house)    
mapp.addplace(boat)
mapp.addplayer(fred)
rock=obj("rock",0,0,mapp)
print(fred.x,fred.y,fred.look())
fred.goto(1,0)
print(fred.x,fred.y,fred.look())
fred.goto(2,0)
print(fred.x,fred.y,fred.look())
fred.goto(-1,0)
print(fred.x,fred.y,fred.look())
'''
