# start a RockBand here
class RockBand:
    genre = "rock"
    key_instruments = ["electric guitar", "drums"]
    n_members = 4

    def get_member_count(self):
        return self.n_members, self.key_instruments, self.n_members


my_rock_band = RockBand()
print(my_rock_band.genre)
print(my_rock_band.n_members)
print(my_rock_band.key_instruments)
