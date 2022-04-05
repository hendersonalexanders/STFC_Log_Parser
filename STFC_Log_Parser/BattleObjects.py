class Battle(object):
    rounds = []
    ships = {}
    players ={}

    def __init__(self):
        pass

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


class Round(object):
    dmg_instance = []
    
    def __init__(self):
        pass

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

    def total_hull_damage_per_player(self):
        dmg = {}

        for instance in self.dmg_instance:
            if instance.playerName not in dmg:
                dmg[instance.playerName] = 0

            dmg[instance.playerName] = dmg[instance.playerName] + instance.hullHP
            if instance.targetDestroyed:
                break

        return dmg


class DamageInstance(object):
    mitigated = 0
    shieldHP = 0
    hullHP = 0
    totalDamage = 0
    playerName = "jaqen h'ghar"
    targetDestroyed = False

    def __init__(self, mit, shp, hhp, tdmg, tdes, playname):
        self.mitigated = mit
        self.shieldHP = shp
        self.hullHP = hhp
        self.totalDamage = tdmg
        if tdes.lower() == "yes":
            self.targetDestroyed = True
        self.playerName = playname


    def mit_percent():
        return (mitigated/totalDamage) * 100
    
    def shield_damage_percent():
        return (shield/(shieldHP + hullHP)) * 100







