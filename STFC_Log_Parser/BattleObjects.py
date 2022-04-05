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
                crits[player] = crits[player] + playerCrits[player]

        return crits


class Round(object):
    dmg_instance = []
    
    def __init__(self, dmginstance):
        self.dmg_instance = dmginstance

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


    def mit_percent():
        return (mitigated/totalDamage) * 100
    
    def shield_damage_percent():
        return (shield/(shieldHP + hullHP)) * 100







