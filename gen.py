from icecream import ic
baseurl='https://www.foaas.com/'
finalstr='''import os
from flask import Flask,redirect

app = Flask(__name__)

'''

with open('foaas.txt','r') as fp:
    for url in fp.readlines():
        url=url.strip()
        innerurl=url[len(baseurl):]
        innerpaths=innerurl.split('/')
        fpaths=innerurl.split('/')
        funcname=[]
        variables=[]
        for i,pathpart in enumerate(innerpaths):
            if ':' in pathpart:
                if pathpart[1:]=='from':
                    pathpart=':'+'ffrom' #avoid reserved name
                innerpaths[i] = '<'+pathpart[1:]+'>'
                variables.append(pathpart[1:])
                fpaths[i] = '{'+pathpart[1:]+'}'
            funcname.append(''.join([e for e in pathpart if e.isalpha()]))
        innerpaths='/'+'/'.join(innerpaths)
        variables=','.join(variables)
        funcname='_'.join(funcname)
        fpaths='/'.join(fpaths)
        funcstr= \
                f"@app.route('{innerpaths}') \ndef {funcname}({variables}): \n\treturn redirect('{baseurl}{fpaths}', code=302)\n\n"
        if funcname!='version':
            finalstr+=funcstr

finalstr+='''
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''

with open('foaas.py','w') as fp:
    fp.write(finalstr)
