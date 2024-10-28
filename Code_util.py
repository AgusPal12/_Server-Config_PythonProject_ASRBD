import os
dir_path = "."
json_files = [f for f in os.listdir(dir_path) if f.endswith('.json')]
print(json_files)

dir_path2 = ".\Points_de_Restauration\SauvegardeLundi_28-10-2024_18-21"
json_files2 = [f for f in os.listdir(dir_path2) if f.endswith('.json')]

while True:
    if json_files == json_files2:
        print("ils sont egal")
        break
        #effacet tout et copier coller.
    else:
        print("sont differents")
        #efface les égales et copier touts.
        break

        