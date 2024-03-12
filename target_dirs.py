import pathlib

def arborescence_to_dict(root):
  """Takes a pathlib.Path object and returns a dictionary representing the arborescence.
  Each node has key 'stop' which is associated with the Path to that node in particular."""
  subdirectories = [x for x in root.iterdir() if x.is_dir()]
  if len(subdirectories) == 0:
    return root
  result = {p.parts[-1]:arborescence_to_dict(p) for p in subdirectories}
  result['stop'] = root
  return result



def get_directories(data_dir):
    pokedir = arborescence_to_dict(data_dir)
    return [

        pokedir['pokemon']['versions']['generation-vii']['ultra-sun-ultra-moon']['stop'],               #this block is all rgba
        pokedir['pokemon']['versions']['generation-vii']['ultra-sun-ultra-moon']['shiny']['stop'],
        pokedir['pokemon']['versions']['generation-vii']['ultra-sun-ultra-moon']['shiny']['female'],
        pokedir['pokemon']['versions']['generation-vii']['ultra-sun-ultra-moon']['female'],

        pokedir['pokemon']['versions']['generation-vi']['x-y']['stop'],                                   #nearly all rgb, a few rgba
        pokedir['pokemon']['versions']['generation-vi']['x-y']['shiny']['stop'],
        pokedir['pokemon']['versions']['generation-vi']['x-y']['shiny']['female'],
        pokedir['pokemon']['versions']['generation-vi']['x-y']['female'],

        pokedir['pokemon']['versions']['generation-vi']['omegaruby-alphasapphire']['stop'],                 #more rgba than rgb, but split
        pokedir['pokemon']['versions']['generation-vi']['omegaruby-alphasapphire']['shiny']['stop'],
        pokedir['pokemon']['versions']['generation-vi']['omegaruby-alphasapphire']['shiny']['female'],
        pokedir['pokemon']['versions']['generation-vi']['omegaruby-alphasapphire']['female'],

        pokedir['pokemon']['versions']['generation-v']['black-white']['stop'],                 #this one throws errors sometimes
        pokedir['pokemon']['versions']['generation-v']['black-white']['shiny']['stop'],           #mostly rgb
        pokedir['pokemon']['versions']['generation-v']['black-white']['shiny']['female'],
        pokedir['pokemon']['versions']['generation-v']['black-white']['female'],

        pokedir['pokemon']['versions']['generation-iv']['heartgold-soulsilver']['stop'],          #all rgba
        pokedir['pokemon']['versions']['generation-iv']['heartgold-soulsilver']['shiny']['stop'],
        pokedir['pokemon']['versions']['generation-iv']['heartgold-soulsilver']['shiny']['female'],
        pokedir['pokemon']['versions']['generation-iv']['heartgold-soulsilver']['female'],

        pokedir['pokemon']['versions']['generation-iv']['diamond-pearl']['stop'],               #all rgba
        pokedir['pokemon']['versions']['generation-iv']['diamond-pearl']['shiny']['stop'],
        pokedir['pokemon']['versions']['generation-iv']['diamond-pearl']['shiny']['female'],
        pokedir['pokemon']['versions']['generation-iv']['diamond-pearl']['female'],

        pokedir['pokemon']['versions']['generation-iv']['platinum']['stop'],                  #all rgb
        pokedir['pokemon']['versions']['generation-iv']['platinum']['shiny']['stop'],
        pokedir['pokemon']['versions']['generation-iv']['platinum']['shiny']['female'],
        pokedir['pokemon']['versions']['generation-iv']['platinum']['female'],

    ]



def get_blacklist(data_dir):
   blacklist =  [
      '/pokemon/versions/generation-v/black-white/10186.png',       #this image is corrupted

      '/pokemon/versions/generation-vii/ultra-sun-ultra-moon/118.png',
      '/pokemon/versions/generation-vii/ultra-sun-ultra-moon/699.png',
      '/pokemon/versions/generation-vii/ultra-sun-ultra-moon/376.png',
      '/pokemon/versions/generation-vii/ultra-sun-ultra-moon/260-mega.png',
      '/pokemon/versions/generation-vii/ultra-sun-ultra-moon/487-origin.png',

      '/pokemon/versions/generation-vii/ultra-sun-ultra-moon/shiny/376.png',
      '/pokemon/versions/generation-vii/ultra-sun-ultra-moon/shiny/713.png',
      '/pokemon/versions/generation-vii/ultra-sun-ultra-moon/shiny/452.png',

      '/pokemon/versions/generation-vii/ultra-sun-ultra-moon/female/118.png',

      '/pokemon/versions/generation-vi/omegaruby-alphasapphire/669.png',

      '/pokemon/versions/generation-vi/omegaruby-alphasapphire/shiny/382-primal.png',
      '/pokemon/versions/generation-vi/omegaruby-alphasapphire/shiny/376.png',






      '/pokemon/versions/generation-v/black-white/0.png',
      '/pokemon/versions/generation-v/black-white/282-mega.png',
      '/pokemon/versions/generation-v/black-white/650.png',
      '/pokemon/versions/generation-v/black-white/651.png',
      '/pokemon/versions/generation-v/black-white/659.png',
      '/pokemon/versions/generation-v/black-white/662.png',
      '/pokemon/versions/generation-v/black-white/664.png',
      '/pokemon/versions/generation-v/black-white/665.png',
      '/pokemon/versions/generation-v/black-white/668.png',
      '/pokemon/versions/generation-v/black-white/669.png',
      '/pokemon/versions/generation-v/black-white/672.png',
      '/pokemon/versions/generation-v/black-white/673.png',
      
      '/pokemon/versions/generation-v/black-white/687.png',
      '/pokemon/versions/generation-v/black-white/688.png',
      '/pokemon/versions/generation-v/black-white/693.png',
      '/pokemon/versions/generation-v/black-white/698.png',
      '/pokemon/versions/generation-v/black-white/699.png',
      '/pokemon/versions/generation-v/black-white/703.png',
      '/pokemon/versions/generation-v/black-white/705.png',
     
      '/pokemon/versions/generation-v/black-white/712.png',
      '/pokemon/versions/generation-v/black-white/792.png',
      '/pokemon/versions/generation-v/black-white/795.png',
      '/pokemon/versions/generation-v/black-white/797.png',
      '/pokemon/versions/generation-v/black-white/804.png',
      '/pokemon/versions/generation-v/black-white/804s.png',
      '/pokemon/versions/generation-v/black-white/806.png',
      '/pokemon/versions/generation-v/black-white/808.png',
      '/pokemon/versions/generation-v/black-white/811.png',
      '/pokemon/versions/generation-v/black-white/812.png',
      '/pokemon/versions/generation-v/black-white/815.png',
      '/pokemon/versions/generation-v/black-white/818.png',
      '/pokemon/versions/generation-v/black-white/818-gmax.png',
      '/pokemon/versions/generation-v/black-white/819.png',
      '/pokemon/versions/generation-v/black-white/820.png',
      '/pokemon/versions/generation-v/black-white/822.png',
      '/pokemon/versions/generation-v/black-white/824.png',
      '/pokemon/versions/generation-v/black-white/825.png',
      '/pokemon/versions/generation-v/black-white/827.png',
      '/pokemon/versions/generation-v/black-white/828.png',
      '/pokemon/versions/generation-v/black-white/830.png',
      
      '/pokemon/versions/generation-v/black-white/815.png',
      '/pokemon/versions/generation-v/black-white/819.png',
      '/pokemon/versions/generation-v/black-white/824.png',
      '/pokemon/versions/generation-v/black-white/825.png',
      '/pokemon/versions/generation-v/black-white/826.png',
      '/pokemon/versions/generation-v/black-white/826-gmax.png',
      
  

      '/pokemon/versions/generation-v/black-white/841.png',
      '/pokemon/versions/generation-v/black-white/843.png',
      '/pokemon/versions/generation-v/black-white/844.png',
      '/pokemon/versions/generation-v/black-white/844-gmax.png',
      '/pokemon/versions/generation-v/black-white/846.png',
      '/pokemon/versions/generation-v/black-white/849.png',
      '/pokemon/versions/generation-v/black-white/849-gmax.png',
   
      '/pokemon/versions/generation-v/black-white/851-gmax.png',
      '/pokemon/versions/generation-v/black-white/854.png',
    
      '/pokemon/versions/generation-v/black-white/858.png',
   
      '/pokemon/versions/generation-v/black-white/861.png',
      '/pokemon/versions/generation-v/black-white/862.png',
      '/pokemon/versions/generation-v/black-white/863.png',
      '/pokemon/versions/generation-v/black-white/864.png',
      '/pokemon/versions/generation-v/black-white/866.png',
      '/pokemon/versions/generation-v/black-white/867.png',
      '/pokemon/versions/generation-v/black-white/876.png',
      '/pokemon/versions/generation-v/black-white/878.png',
      '/pokemon/versions/generation-v/black-white/882.png',
      '/pokemon/versions/generation-v/black-white/884-gmax.png',
      '/pokemon/versions/generation-v/black-white/889.png',
      '/pokemon/versions/generation-v/black-white/890.png',
      '/pokemon/versions/generation-v/black-white/891.png',
      '/pokemon/versions/generation-v/black-white/893.png',
      '/pokemon/versions/generation-v/black-white/874.png',
      '/pokemon/versions/generation-v/black-white/875.png',
      '/pokemon/versions/generation-v/black-white/876.png',
      '/pokemon/versions/generation-v/black-white/879.png',
      '/pokemon/versions/generation-v/black-white/879-gmax.png',
      '/pokemon/versions/generation-v/black-white/882.png',
      '/pokemon/versions/generation-v/black-white/888.png',
      '/pokemon/versions/generation-v/black-white/889.png',
      '/pokemon/versions/generation-v/black-white/891.png',
      '/pokemon/versions/generation-v/black-white/895.png',
      '/pokemon/versions/generation-v/black-white/897.png',
      '/pokemon/versions/generation-v/black-white/898.png',
      '/pokemon/versions/generation-v/black-white/10034.png',
      '/pokemon/versions/generation-v/black-white/10036.png',
      '/pokemon/versions/generation-v/black-white/10037.png',
      '/pokemon/versions/generation-v/black-white/10038.png',
      '/pokemon/versions/generation-v/black-white/10042.png',
      '/pokemon/versions/generation-v/black-white/10048.png',
      '/pokemon/versions/generation-v/black-white/10049.png',
      '/pokemon/versions/generation-v/black-white/10050.png',
      '/pokemon/versions/generation-v/black-white/10055.png',
      '/pokemon/versions/generation-v/black-white/10056.png',
      '/pokemon/versions/generation-v/black-white/10059.png',
      '/pokemon/versions/generation-v/black-white/10070.png',
      '/pokemon/versions/generation-v/black-white/10074.png',
      '/pokemon/versions/generation-v/black-white/10076.png',
      '/pokemon/versions/generation-v/black-white/10087.png',
      '/pokemon/versions/generation-v/black-white/10089.png',
      '/pokemon/versions/generation-v/black-white/10094.png',
      '/pokemon/versions/generation-v/black-white/10099.png',
      '/pokemon/versions/generation-v/black-white/10148.png',
      '/pokemon/versions/generation-v/black-white/10164.png',
      '/pokemon/versions/generation-v/black-white/10175.png',
      '/pokemon/versions/generation-v/black-white/10184.png',
      '/pokemon/versions/generation-v/black-white/10185.png',
      '/pokemon/versions/generation-v/black-white/10189.png',
      '/pokemon/versions/generation-v/black-white/10194.png',
      '/pokemon/versions/generation-v/black-white/10196.png',
      '/pokemon/versions/generation-v/black-white/10199.png',
      '/pokemon/versions/generation-v/black-white/10201.png',
      '/pokemon/versions/generation-v/black-white/10204.png',
      '/pokemon/versions/generation-v/black-white/10205.png',
      '/pokemon/versions/generation-v/black-white/10206.png',
      '/pokemon/versions/generation-v/black-white/10211.png',
      '/pokemon/versions/generation-v/black-white/10213.png',
      '/pokemon/versions/generation-v/black-white/10216.png',
      '/pokemon/versions/generation-v/black-white/10217.png',
      '/pokemon/versions/generation-v/black-white/10218.png',
      '/pokemon/versions/generation-v/black-white/10219.png',
      '/pokemon/versions/generation-v/black-white/10220.png',
      '/pokemon/versions/generation-v/black-white/10224.png',
      '/pokemon/versions/generation-v/black-white/10225.png',
      '/pokemon/versions/generation-v/black-white/10226.png',
      '/pokemon/versions/generation-v/black-white/10228.png',







      '/pokemon/versions/generation-v/black-white/shiny/0.png',
      '/pokemon/versions/generation-v/black-white/shiny/659.png',
      '/pokemon/versions/generation-v/black-white/shiny/662.png',
      '/pokemon/versions/generation-v/black-white/shiny/664.png',
      '/pokemon/versions/generation-v/black-white/shiny/665.png',
      '/pokemon/versions/generation-v/black-white/shiny/669.png',
      '/pokemon/versions/generation-v/black-white/shiny/672.png',
      '/pokemon/versions/generation-v/black-white/shiny/681.png',
      '/pokemon/versions/generation-v/black-white/shiny/703.png',
      '/pokemon/versions/generation-v/black-white/shiny/708.png',
      '/pokemon/versions/generation-v/black-white/shiny/811.png',
      '/pokemon/versions/generation-v/black-white/shiny/812.png',
      '/pokemon/versions/generation-v/black-white/shiny/820.png',
      '/pokemon/versions/generation-v/black-white/shiny/822.png',
      '/pokemon/versions/generation-v/black-white/shiny/824.png',
      '/pokemon/versions/generation-v/black-white/shiny/828.png',
      '/pokemon/versions/generation-v/black-white/shiny/830.png',
      '/pokemon/versions/generation-v/black-white/shiny/832.png',
      '/pokemon/versions/generation-v/black-white/shiny/843.png',
      '/pokemon/versions/generation-v/black-white/shiny/846.png',
      '/pokemon/versions/generation-v/black-white/shiny/849.png',
      '/pokemon/versions/generation-v/black-white/shiny/851.png',
      '/pokemon/versions/generation-v/black-white/shiny/854.png',
      '/pokemon/versions/generation-v/black-white/shiny/855.png',
      '/pokemon/versions/generation-v/black-white/shiny/858.png',
      '/pokemon/versions/generation-v/black-white/shiny/860.png',
      '/pokemon/versions/generation-v/black-white/shiny/861.png',
      '/pokemon/versions/generation-v/black-white/shiny/862.png',
      '/pokemon/versions/generation-v/black-white/shiny/863.png',
      '/pokemon/versions/generation-v/black-white/shiny/864.png',
      '/pokemon/versions/generation-v/black-white/shiny/867.png',
      '/pokemon/versions/generation-v/black-white/shiny/875.png',
      '/pokemon/versions/generation-v/black-white/shiny/876.png',
      '/pokemon/versions/generation-v/black-white/shiny/879.png',
      '/pokemon/versions/generation-v/black-white/shiny/888.png',
      '/pokemon/versions/generation-v/black-white/shiny/889.png',
      '/pokemon/versions/generation-v/black-white/shiny/891.png',
      '/pokemon/versions/generation-v/black-white/shiny/892.png',
      '/pokemon/versions/generation-v/black-white/shiny/893.png',
      '/pokemon/versions/generation-v/black-white/shiny/898.png',
      '/pokemon/versions/generation-v/black-white/shiny/869_5.png',
      '/pokemon/versions/generation-v/black-white/shiny/869_9.png',
      '/pokemon/versions/generation-v/black-white/shiny/869_11.png',
      '/pokemon/versions/generation-v/black-white/shiny/869_13.png',
      '/pokemon/versions/generation-v/black-white/shiny/869_15.png',
      '/pokemon/versions/generation-v/black-white/shiny/869_17.png',
      '/pokemon/versions/generation-v/black-white/shiny/869_19.png',
      '/pokemon/versions/generation-v/black-white/shiny/869_23.png',
      '/pokemon/versions/generation-v/black-white/shiny/869_27.png',
      '/pokemon/versions/generation-v/black-white/shiny/869_29.png',
      '/pokemon/versions/generation-v/black-white/shiny/869_31.png',
      '/pokemon/versions/generation-v/black-white/shiny/869_33.png',
      '/pokemon/versions/generation-v/black-white/shiny/869_37.png',
      '/pokemon/versions/generation-v/black-white/shiny/869_43.png',
      '/pokemon/versions/generation-v/black-white/shiny/869_45.png',
      '/pokemon/versions/generation-v/black-white/shiny/869_47.png',
      '/pokemon/versions/generation-v/black-white/shiny/869_51.png',
      '/pokemon/versions/generation-v/black-white/shiny/869_55.png',
      '/pokemon/versions/generation-v/black-white/shiny/869_57.png',
      '/pokemon/versions/generation-v/black-white/shiny/869_59.png',
      '/pokemon/versions/generation-v/black-white/shiny/892_2.png',
      '/pokemon/versions/generation-v/black-white/shiny/10034.png',
      '/pokemon/versions/generation-v/black-white/shiny/10036.png',
      '/pokemon/versions/generation-v/black-white/shiny/10065.png',
      '/pokemon/versions/generation-v/black-white/shiny/10066.png',
      '/pokemon/versions/generation-v/black-white/shiny/10074.png',
      '/pokemon/versions/generation-v/black-white/shiny/10116.png',
      '/pokemon/versions/generation-v/black-white/shiny/10164.png',
      '/pokemon/versions/generation-v/black-white/shiny/10175.png',
      '/pokemon/versions/generation-v/black-white/shiny/10185.png',
      '/pokemon/versions/generation-v/black-white/shiny/10195.png',
      '/pokemon/versions/generation-v/black-white/shiny/10197.png',
      '/pokemon/versions/generation-v/black-white/shiny/10200.png',
      '/pokemon/versions/generation-v/black-white/shiny/10201.png',
      '/pokemon/versions/generation-v/black-white/shiny/10205.png',
      '/pokemon/versions/generation-v/black-white/shiny/10210.png',
      '/pokemon/versions/generation-v/black-white/shiny/10211.png',
      '/pokemon/versions/generation-v/black-white/shiny/10218.png',
      '/pokemon/versions/generation-v/black-white/shiny/10219.png',
      '/pokemon/versions/generation-v/black-white/shiny/10220.png',
      '/pokemon/versions/generation-v/black-white/shiny/10228.png',

      '/pokemon/versions/generation-v/black-white/shiny/female/876.png',

      '/pokemon/versions/generation-v/black-white/female/876.png',



      '/pokemon/versions/generation-iv/diamond-pearl/339.png',
      '/pokemon/versions/generation-iv/diamond-pearl/30.png',
      '/pokemon/versions/generation-iv/diamond-pearl/415.png',
      '/pokemon/versions/generation-iv/diamond-pearl/416.png',
      '/pokemon/versions/generation-iv/diamond-pearl/431.png',

      '/pokemon/versions/generation-iv/diamond-pearl/shiny/339.png',
      '/pokemon/versions/generation-iv/diamond-pearl/shiny/30.png',
      '/pokemon/versions/generation-iv/diamond-pearl/shiny/415.png',
      '/pokemon/versions/generation-iv/diamond-pearl/shiny/416.png',
      '/pokemon/versions/generation-iv/diamond-pearl/shiny/431.png',

      '/pokemon/versions/generation-iv/diamond-pearl/shiny/female/415.png',

      '/pokemon/versions/generation-iv/diamond-pearl/female/415.png',
   ]
   return [pathlib.PosixPath(data_dir + s) for s in blacklist]