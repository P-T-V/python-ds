# import lesson25_5_0_Module_Garden
# from lesson25_5_0_Module_Garden import * # No tak ne rekomenduetsa delat, t.k. luchshe importirovat tolko to,
#                                          # chto nujno
from lesson25_5_0_Module_Garden import PotatoGarden


# my_garden = lesson25_5_0_Module_Garden.PotatoGarden(5)
my_garden = PotatoGarden(5)
my_garden.are_all_ripe()
for _ in range(3):
    my_garden.grow_all()
    my_garden.are_all_ripe()
