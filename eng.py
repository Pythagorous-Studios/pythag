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
    def addplace(self,plc): 
        if isinstance(plc,place): 
            self.places.append(plc) 
        return isinstance(plc,place) 
        
    def addplayer(self,plyr): 
        if isinstance(plyr,player): 
            self.players.append(plyr)

        return isinstance(plyr,player) 
        
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

        

    
class player(): 
    def __init__(self,name,x,y,management_engine): 
        self.name=name 
        self.x=x 
        self.y=y 
        self.mgeng=management_engine 

    def goto(self,x,y): 
        if self.mgeng.coords_exist(x,y): 
            self.x=x 
            self.y=y
        else:
            log('no such coord: '+str((x,y))+' in mg. eng. : '+str(self.mgeng))
    def look(self):
        return self.mgeng.gattr(self.x,self.y,"descrip")
            

