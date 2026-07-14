from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API
import nlpcloud

class NLPapp:
    def __init__(self):
        self.dbo=Database()
        self.root=Tk()
        self.root.title("NLPapp")
        self.root.geometry('350x600')
        self.root.configure(bg='#34495E')
        self.login_gui()
        self.apio=API()


        self.root.mainloop()
    def login_gui(self):
        self.clear()
        heading=Label(self.root,text="NLP",bg='#34495E',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        label1=Label(self.root,text='Enter Your registered Email',bg='#6D5DFC')
        label1.pack(pady=(10,10))

        self.input_email=Entry(self.root,width=50)
        self.input_email.pack(pady=(5,10),ipady=4)

        label2=Label(self.root,text='Enter Your Password',bg='#6D5DFC')
        label2.pack(pady=(10,10))
        self.password_input=Entry(self.root,width=50,show='*')
        self.password_input.pack(pady=(5,10),ipady=4)

        login_btn=Button(self.root,text='Login',width=30,height=2,bg='red',command=self.perform_login)
        login_btn.pack(pady=(10,10))

        label3=Label(self.root,text='Not a member?',bg='#6D5DFC')
        label3.pack(pady=(20,10))

        redirect_btn=Button(self.root,text='Register Now!',width=10,height=1,bg='red',command=self.register_gui)
        redirect_btn.pack(pady=(10,10))



    def register_gui(self):
        self.clear()
        heading=Label(self.root,text="NLP",bg='#34495E',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        label1=Label(self.root,text='Enter Name',bg='#6D5DFC')
        label1.pack(pady=(10,10))

        self.input_name=Entry(self.root,width=50)
        self.input_name.pack(pady=(5,10),ipady=4)

        label2=Label(self.root,text='your email',bg='#6D5DFC')
        label2.pack(pady=(10,10))

        self.input_email=Entry(self.root,width=50)
        self.input_email.pack(pady=(5,10),ipady=4)
        
        label3=Label(self.root,text='Enter password',bg='#6D5DFC')
        label3.pack(pady=(10,10))

        self.password_input=Entry(self.root,width=50)
        self.password_input.pack(pady=(5,10),ipady=4)


        register_btn=Button(self.root,text='Register',width=30,height=2,bg='red',command=self.perform_registration)
        register_btn.pack(pady=(10,10))

        label3=Label(self.root,text='Already a Member?',bg='#6D5DFC')
        label3.pack(pady=(20,10))

        redirect_btn=Button(self.root,text='Login now',width=10,height=1,bg='red',command=self.login_gui)
        redirect_btn.pack(pady=(10,10))



    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
        

    def perform_registration(self):

        name=self.input_name.get()
        email=self.input_email.get()
        password=self.password_input.get()
        response=self.dbo.add_data(name,email,password)
        
        if response:
            messagebox.showinfo('sucess','Registration sucessfully. You can login now!')
        else:
            messagebox.showerror('Error','Email already exists')
    

    def perform_login(self):
        email=self.input_email.get()
        password=self.password_input.get()

        response=self.dbo.search(email,password)

        if response:
            messagebox.showinfo('sucess',"login sucessfully!")
            self.home_gui()
        else:
            messagebox.showerror("error",'you entered wrong id/password')



    def home_gui(self):
        self.clear()

        heading=Label(self.root,text="NLP",bg='#34495E',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))


        Sentiment_btn=Button(self.root,text='Sentiment Analysis',width=30,height=2,bg='red',command=self.Sentiment)
        Sentiment_btn.pack(pady=(10,10))



        ner_btn=Button(self.root,text=' Named entity recongition',width=30,height=2,bg='red',command=self.ner)
        ner_btn.pack(pady=(10,10))

        emotion_btn=Button(self.root,text='Emotion Predictions',width=30,height=2,bg='red',)
        emotion_btn.pack(pady=(10,10))


        logout_btn=Button(self.root,text='logout ',width=10,height=1,bg='red',command=self.login_gui)
        logout_btn.pack(pady=(10,10))


    def Sentiment(self):
        self.clear()
        heading1=Label(self.root,text="NLP",bg='#34495E',fg='white')
        heading1.pack(pady=(30,30))
        heading1.configure(font=('verdana',24,'bold'))

        heading2=Label(self.root,text="Sentiment Analysis",bg='#34495E',fg='white',width=30)
        heading2.pack(pady=(13,20))
        heading2.configure(font=('verdana',20,))

        label1=Label(self.root,text='Enter Your Text Below',bg='#6D5DFC')
        label1.pack(pady=(20,10))

        self.Sentiment_input=Entry(self.root,width=50)
        self.Sentiment_input.pack(pady=(5,10),ipady=4)

        Sentiment_btn=Button(self.root,text='Analyze Sentiment',width=15,height=3,bg='red',command=self.do_sentiment_analysis)
        Sentiment_btn.pack(pady=(10,10))


        self.Sentiment_result=Label(self.root,text='',bg='#34495E',fg='white')
        self.Sentiment_result.pack(pady=(20,10))
        self.Sentiment_result.configure(font=('verdana',16))

        goback_btn=Button(self.root,text='GO back ->',width=10,height=1,bg='red',command=self.home_gui)
        goback_btn.pack(pady=(10,10))

    def do_sentiment_analysis(self):
        text=self.Sentiment_input.get()
        result=self.apio.sentiment_analysis(text)
        print(result)
        txt = ''

        for item in result['scored_labels']:
            txt += f"{item['label']} -> {item['score']}\n"
        self.Sentiment_result['text']=txt
    def ner(self):
        self.clear()
        heading1=Label(self.root,text="NLP",bg='#34495E',fg='white')
        heading1.pack(pady=(30,30))
        heading1.configure(font=('verdana',24,'bold'))

        heading2=Label(self.root,text="Named Entity Recongitiom",bg='#34495E',fg='white',width=30)
        heading2.pack(pady=(13,20))
        heading2.configure(font=('verdana',20,))

        label1=Label(self.root,text='Enter Your Text Below',bg='#6D5DFC')
        label1.pack(pady=(20,10))


        self.ner_input=Entry(self.root,width=50)
        self.ner_input.pack(pady=(5,10),ipady=4)

        label2=Label(self.root,text=' Insert search entity',bg='#6D5DFC')
        label2.pack(pady=(20,10))

        self.search_entity_input=Entry(self.root,width=50)
        self.search_entity_input.pack(pady=(5,10),ipady=4)



        self.ner_result=Label(self.root,text='',bg='#34495E',fg='white')
        self.ner_result.pack(pady=(20,10))
        self.ner_result.configure(font=('verdana',16))

        Sentiment_btn=Button(self.root,text='Process',width=15,height=3,bg='red',command=self.do_ner)
        Sentiment_btn.pack(pady=(10,10))

        goback_btn=Button(self.root,text='GO back ->',width=10,height=1,bg='red',command=self.home_gui)
        goback_btn.pack(pady=(10,10))

    def do_ner(self):
        text=self.ner_input.get()
        entity=self.search_entity_input.get()
        result=self.apio.NER(text,entity)
        print(result)
        txt = ''

        for entity in result['entities']:
            txt += f"{entity['text']} -> {entity['type']} ({entity['start']}-{entity['end']})\n"

        self.ner_result['text'] = txt

        

nlp=NLPapp()