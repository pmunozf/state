#!/usr/bin/env python
#
# Pablo Munoz (c) 2019
# pablo.bmf@gmail.com
#
# Facilities for state management
import state

if __name__ == '__main__':

    #nombre
    nombre = 'hola'
    s = state.State(nombre=nombre)
    print(s.__dict__)
    print(s.nombre)
    s.nombre = 'john'
    print(s.nombre)
