from pymatgen.core import Structure

import warnings

import matgl
from matgl.ext.ase import Relaxer


warnings.simplefilter("ignore") # To suppress warnings for clearer output


# Import the POSCAR file
crystal_structure = Structure.from_file("POSCAR")

# Load the M3GNet model
pot = matgl.load_model("M3GNet-MP-2021.2.8-PES")

# Create the ionic relaxation method
relaxer = Relaxer(potential=pot)

relax_results = relaxer.relax(crystal_structure, verbose=True) # other labels: fmax, ...

# Show the results
final_structure = relax_results['final_structure']
final_energy_per_atom = float(relax_results['trajectory'].energies[-1] / len(crystal_structure))

print("The relaxed structure is: ", final_structure)
print(f"Final energy is {final_energy_per_atom:.3f} eV/atom")

# Save the structure in CONTCAR type file
final_structure.to(filename='CONTCAR', fmt='poscar')