strange_quark = ['1/2', '-1/3']
charm_quark = ['1/2', '2/3']
electron_lepton = ['1/2', '-1']
neutrino_lepton = ['1/2', '0']
photon_boson = ['1', '0']

spin = input()
charge = input()

if spin == strange_quark[0] and charge == strange_quark[1]:
    print("Strange Quark")
elif spin == charm_quark[0] and charge == charm_quark[1]:
    print("Charm Quark")
elif spin == electron_lepton[0] and charge == electron_lepton[1]:
    print("Electron Lepton")
elif spin == neutrino_lepton[0] and charge == neutrino_lepton[1]:
    print("Neutrino Lepton")
else:
    print("Photon Boson")
