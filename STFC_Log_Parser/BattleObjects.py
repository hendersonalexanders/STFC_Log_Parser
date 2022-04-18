#This file is going to get crowded pretty quickly. Probably need to split them into something easier to process (1 obj per file?)

class Battle(object):
    rounds = []
    ships = {}
    players = []

    def __init__(self, playerList = []):
        self.players = playerList

    def populate_player_list(self):
        
        for round in self.rounds:
            for damage_instance in round.dmg_instance:
                if damage_instance.playerName not in self.players:
                    self.players.append(damage_instance.playerName);
    

    def total_hull_damage(self):
        dmg = 0

        for round in self.rounds:
            dmg = dmg + round.total_hull_damage()

        return dmg

    #per player functions
    def total_hull_damage_per_player(self):
        dmg = {}

        for round in self.rounds:
            playerDmg = round.total_hull_damage_per_player()
            for player in playerDmg:
                if player not in dmg:
                    dmg[player] = 0
                dmg[player] = dmg[player] + playerDmg[player]

        return dmg

    def total_shield_damage_per_player(self):
        dmg = {}

        for round in self.rounds:
            playerDmg = round.total_shield_damage_per_player()
            for player in playerDmg:
                if player not in dmg:
                    dmg[player] = 0
                dmg[player] = dmg[player] + playerDmg[player]

        return dmg

    def total_mitigated_damage_per_player(self):
        dmg = {}

        hull = self.total_hull_damage_per_player()
        shield = self.total_shield_damage_per_player()

        for player in hull:
            if player not in dmg:
                    dmg[player] = 0
            dmg[player] = dmg[player] + hull[player]

        for player in shield:
            if player not in dmg:
                    dmg[player] = 0
            dmg[player] = dmg[player] + shield[player]

        return dmg

    def total_crits_per_player(self):
        crits = {}

        for round in self.rounds:
            playerCrits = round.total_crits_per_player()
            for player in playerCrits:
                if player not in crits:
                    crits[player] = 0
                crits[player] += playerCrits[player]

        return crits
 
    def avg_mit_percent_per_player(self):
        mit_pct = {}
        player_avg_count = {}
        for round in self.rounds:
            playerMits = round.mitigation_percentage_per_player();
            for player in playerMits:
                if player not in mit_pct:
                    mit_pct[player] = 0
                    player_avg_count[player] = 0
                mit_pct[player] += playerMits[player]
                player_avg_count[player] += 1

        for player in mit_pct:
            mit_pct[player] = mit_pct[player] / player_avg_count[player]

        return mit_pct

            


class Round(object):
    dmg_instance = []
    round_nbr = 0
    
    def __init__(self, dmginstance, round_nbr):
        self.dmg_instance = dmginstance
        self.round_nbr = round_nbr

#All ships/player functions
    def avg_mit_pct():
        avg = 0

        for instance in dmg_instance:
            avg = avg + instance.mit_percent()

        return avg/len(dmg_instance)

    def avg_shd_pct():
        avg = 0

        for instance in dmg_instance:
            avg = avg + instance.shield_damage_percent()

        return avg/len(dmg_instance)

    def total_damage():
        dmg = 0
        for instance in dmg_instance:
            dmg = dmg + instance.totalDamage;

        return dmg

    def total_hull_damage(self):
        dmg = 0

        for instance in self.dmg_instance:
            dmg = dmg + instance.hullHP
            if instance.targetDestroyed:
                break

        return dmg

    def total_shield_damage():
        dmg = 0

        for instance in dmg_instance:
            dmg = dmg + instance.sheildHP

        return dmg

## Per Player functions
    def total_hull_damage_per_player(self):
        dmg = {}

        for instance in self.dmg_instance:
            if instance.playerName not in dmg:
                dmg[instance.playerName] = 0

            dmg[instance.playerName] = dmg[instance.playerName] + instance.hullHP
            if instance.targetDestroyed:
                break

        return dmg

    def total_shield_damage_per_player(self):
        dmg = {}

        for instance in self.dmg_instance:
            if instance.playerName not in dmg:
                dmg[instance.playerName] = 0

            dmg[instance.playerName] = dmg[instance.playerName] + instance.shieldHP
            if instance.targetDestroyed:
                break

        return dmg

    def total_crits_per_player(self):
        crits = {}

        for instance in self.dmg_instance:
            if instance.playerName not in crits:
                crits[instance.playerName] = 0
            if instance.isCrit == True:
                crits[instance.playerName] = crits[instance.playerName] + 1
            if instance.targetDestroyed:
                break

        return crits

    def mitigation_percentage_per_player(self):
        avg_mit_pct = {}
        player_instance_count = {}
        for instance in self.dmg_instance:
            if instance.playerName not in avg_mit_pct:
                avg_mit_pct[instance.playerName] = 0
                player_instance_count[instance.playerName] = 0
            
            avg_mit_pct[instance.playerName] += instance.mit_percent()
            player_instance_count[instance.playerName] += 1

            if instance.targetDestroyed:
                break
        for player in avg_mit_pct:
            avg_mit_pct[player] = avg_mit_pct[player] / player_instance_count[player]

        return avg_mit_pct


class DamageInstance(object):
    mitigated = 0
    shieldHP = 0
    hullHP = 0
    totalDamage = 0
    playerName = "jaqen h'ghar"
    targetDestroyed = False
    isCrit = False

    def __init__(self, mit, shp, hhp, tdmg, tdes, playname, crit):
        self.mitigated = mit
        self.shieldHP = shp
        self.hullHP = hhp
        self.totalDamage = tdmg
        if tdes.lower() == "yes":
            self.targetDestroyed = True
        self.playerName = playname
        if crit.lower() == "yes":
            self.isCrit = True


    def mit_percent(self):
        if self.totalDamage is 0:
            return 0
        return (self.mitigated/self.totalDamage) * 100
    
    def shield_damage_percent(self):
        return (self.shield/(self.shieldHP +self. hullHP)) * 100







