

def doc_tap_tin(thumuc= str, tentaptin= str):
    try:
        with open(os.path.join(thumuc, tentaptin),'rb') as f:
            nv=pickle.load(f)
            return nv
    except Exception as e:
        return None