total = int(input("enter no. of question : "))
html=[]

for i in range(total):
    option_list=[]
    qtype = str(input("enter question type : "))
    if qtype=="text":
        q = str(input("enter your question : "))
        text='''
                <p>{}</p>
                <textarea  aria-rowindex="5" aria-autocomplete="inline" placeholder="Enter the Review"> </textarea>
        '''.format(q)
        html.append(text)
    
    elif qtype=="radio":
        q_no = int(input('enter no. of options : '))
        q = str(input("enter question : "))
        q_id = str(input("enter qid: "))
        option_list=[]
        for i in range(q_no):
            option = input("enter option"+str(i+1)+": ")
            radio = '''
                    <label class="btn btn-secondary{}">
                        <input type="radio"  name="{}" id="{}" autocomplete="off"> {}
                    </label>
            '''.format(str(i),q_id,q_id+str(i+1),option)
            option_list.append(radio)

        radio_final = '''
                        <p>{}</p>
              <div class="btn-group" data-bs-toggle="buttons">
              {}
              </div>
        '''.format(q,"\n".join(option_list))
        html.append(radio_final)

    elif qtype=="check":
        q_no = int(input('enter no. of options : '))
        q = str(input("enter question : "))
        option_list=[]
        for i in range(q_no):
            option = input("enter option "+str(i+1)+" :")
            basic_check = '''
                    <label class="list-group-item">
                      <input class="form-check-input-me-{}" type="checkbox" value="">
                      {}
                    </label>
                    &nbsp        
            '''.format(str(i),option)
            option_list.append(basic_check)
        check_final='''
                        <p>{}</p>
            <div class="list-group">
            {}
            </div>    
        '''.format(q,"\n".join(option_list))
        html.append(check_final)

#print("\n".join(html))

with open(r'basic_text.html',"r") as file:
    x = file.readlines()

x[50]= "\n".join(html)

with open(r'basic_text.html',"w") as file2:
    x = file2.writelines(x)

import os
os.startfile("basic_text.html")
#os.move("basic_text.html","./templates")