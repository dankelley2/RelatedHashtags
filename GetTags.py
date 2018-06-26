from tkinter import *
import requests, codecs

def output_similar_tags(base_tag, f_name=None):
    if base_tag == str.rstrip(' ').lstrip(' ') == '':
        return 'tag_list = []'
    r = requests.get('https://d212rkvo8t62el.cloudfront.net/tag/' +
                     str(base_tag).replace('#','').rstrip(' ').lstrip(' '), verify=False)
    json = r.json()
    if len(json['results']) == 0:
        return 'tag_list = []'
    str_to_write = 'tag_list = [\r\n'
    for jsonTag in json['results']:
        str_to_write += ("  '#" + jsonTag['tag'] + "',\n")
    if f_name != None:
        with codecs.open(str.replace(f_name,'.txt','') + '.txt', 'w', 'utf-8') as f:
                f.write(str_to_write[0:-2] + ']')
    return str_to_write[0:-2] + ']'

def refresh_tags(event=None):
    txt_output.delete(1.0,END)
    txt_output.insert(END,output_similar_tags(txt_entry.get()))

root = Tk()

root.title('Get Related Hashtags')
root.resizable(False, False)

txt_entry = Entry(root, text="Enter a hashtag", width=25)
txt_entry.grid(row=0, column=1, sticky="nsew")
txt_entry.bind('<Return>',refresh_tags)

btn_refresh = Button(root, text="Refresh", width=10, command=refresh_tags)
btn_refresh.grid(row=0, column=2, sticky="nsew")

txt_output = Text(root, width=30)
txt_output.grid(row=1, column=1, rowspan=20, columnspan=2, sticky="nsew")

root.update()
root.mainloop()
