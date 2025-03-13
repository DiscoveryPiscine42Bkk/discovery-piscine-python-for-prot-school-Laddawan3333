import sys
if len(sys.argv) > 1:
    for parame in sys.argv[1:]:
       if not param.endswith('ism'):
            print(parame + 'ism')
else:
    print("none")