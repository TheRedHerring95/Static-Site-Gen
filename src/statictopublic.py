import os
import shutil

def static_to_public(public:str = None, static:str = None):
    if static == None:
        static = "static"
    if public == None:
        public = "public"
    if os.path.exists(f"./{public}") != False:
        if len(os.listdir(f"./{public}")) != 0:
            shutil.rmtree(f"./{public}")
            os.mkdir(f"./{public}")
    else: os.mkdir(f"./{public}")
    items = os.listdir(f"./{static}")
    for item in items:
        if os.path.isfile(f"./{static}/{item}") == True:
            shutil.copy(f"./{static}/{item}", f"./{public}")
        else:
            next_public = f"{public}/{item}"
            next_static = f"{static}/{item}"
            static_to_public(next_public, next_static)
        