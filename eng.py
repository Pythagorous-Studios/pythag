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
    class bat_mng():
        def __init__(self,combs=[],team=False):
            turnorder=[]
            if team==True:
                for team in combs:
                    for comb in team:
                        turnorder.append(comb)
            elif team==False:
                for comb in combs:
                    turnorder.append(comb)
            else:
                log('huh?',3)
            #human readable,ie not pointers, for the inevitable debug
            humanturnorder=[]
            for comb in turnorder:
                humanturnorder.append(comb.name)
            turn=iter(turnorder)
            next(turn)
            self.combs=combs
            self.team=team
            self.turnorder=turnorder
            self.humanturnorder=humanturnorder
            self.turn=turn
        def action(self,src,mv,tgt):
            if src==turn:
                if move in src.moves and isinstance(mv,move):
                    if tgt in combs:
                        mvdat=src.move.effect()
                        #fyi form is eff,stat,amt
                        if mvdat[0]=='attack':
                            if mvdat[1]=='hp':
                                #what else?, fyi all atks should be positive
                                tgt.hpmod(mvdat[1]*-1)
                        if mvdat[0]=='buff':
                            if mvdat[1]=='hp':
                                tgt.hpmod(mvdat[1])
                            
            else:
                log('nice try enchillada man! Wait until its your turn! If this is an actuall error msg;I don\'t know what you did, my condolances.')
        def chtur():
            try:
                next(turn)
            except StopIteration:
                turn=iter(turnorder)
class place(): 
    def __init__(self,name,x,y,descrip=None): 
        self.name=name 
        self.y=y 
        self.x=x 
        self.y=y 
        self.descrip=descrip 

        

    
class player(): 
    def __init__(self,name,x,y,management_engine,hp=100): 
        moves=[]
        self.name=name 
        self.x=x 
        self.y=y 
        self.mgeng=management_engine 
        self.hp=hp
        self.moves=moves
    def goto(self,x,y): 
        if self.mgeng.coords_exist(x,y): 
            self.x=x 
            self.y=y
        else:
            log('no such coord: '+str((x,y))+' in mg. eng. : '+str(self.mgeng))
    def look(self):
        return self.mgeng.gattr(self.x,self.y,"descrip")
    def hpmod(self,amt):
        self.hp+=amt
        return hp
    def learn(self,mv):
        if mv.isinstance(mv,move):
            if mv not in self.moves:
                #maybe more conditions?
                self.moves.append(mv)
    def forget(self,mv):
        if mv in self.moves:
            self.moves.remove(mv)
    def humoves(self):
        return [mv for mv in self.moves mv.name]
    def action(self,mv):
        """do move"""

class move():
    """A comon parent of different types of moves"""
    def __init__(self,name,descrip=None):
        self.name=name
        self.descrip=descrip
    def move():
        #the format is effect ie:attack,buff etc ;stat ie:hp,speed etc ;amount ie 69,420,21
        return (None)

class attack(move):
    def __init__(self,name,dmg=10,stat='hp',descrip=None):
        #the stat isnt super nesccescary but hey options, and consistent effect return format
        super().__init__(name=name,descrip=descrip)
        self.dmg=dmg
        eff='attack'
        self.eff=eff
    def effect(self):
        return (self.eff,self.stat,self.dmg)

class buff(move):
    def __init__(self,name,stat='hp',amt=10,descrip=None):
        self.stat=stat
        self.amt=amt
        super().__init__(name=name,descrip=descrip)
        eff='buff'
    def effect(self):
        return (self.eff,self.stat,self.amt)
