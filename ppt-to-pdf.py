import os, subprocess
direcotry = os.getcwd()

filesInDirectory =os.listdir(direcotry)

for idx,val in enumerate(filesInDirectory):
    if val.endswith('.ppt'):
        print('Converting: ' + val)
        subprocess.call( ['soffice',
                 '--headless',
                 '--convert-to',
                 'pdf',
                   direcotry +'\\' + val] )