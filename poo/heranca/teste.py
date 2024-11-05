from gato import Gato
from cachorro import Cachorro
from ave import Ave

gato = Gato('Tom', 5, 'Siames')
cachorro = Cachorro('Rex', 3, 'Pastor Alemão')
ave = Ave('Piu', 1, 'Calopsita')

print(gato.emitir_som())
print(cachorro.emitir_som())
print(ave.emitir_som())