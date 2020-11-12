import pathlib //получи
import shutill

path = str(pathlib.Path().absolute())
try:
    shutil.rmtree(path)
except OSError:
    print ("no")
else:
    print ("norm")

try:
    os.mkdir(path)
except OSError:
    print ("no")
else:
    print ("Successfully created the directiry %s , zagr foto" % path)
km = ['4km','9km']
amount = 6

for formatt in km:


    kmpath = path + '//' + formatt

    try:
        os.mkdir(kmpath)
    except OSError:
        print ("no")
    else:
        print (("Successfully created the directory %s " + formatt) %(path + '//'+ formatt))

    for n in range(amount):
        fotoname = str(n) + '.png'
        name = 'https://oceancolor.gsfc.nasa.gov/showimages/MODISA/IMAGES/SST/L3/2020/09' + str(n).zfill(2)+'/AQUA_MODIS.202009'+str(n).zfill(2)+'.L3m.DAY.SST.sst.'+formatt+'.NRT.nc.png'
        r = requests.get(name)
        
        open (kmpath + '//' + fotoname, 'wb').write(r.content)
    
#Hello! Help me with my code!