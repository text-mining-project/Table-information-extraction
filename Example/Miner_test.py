from bs4 import BeautifulSoup
import re
import xlwt


class Table_miner:
    def __init__(self, label, dest):
        super(Table_miner, self).__init__()
        self.label = label
        self.dest = dest

    def extract(self):
        a,b = self.extraction(self.label)
        b = self.coordinate_transform(b)
        o, to_be_write, len_l = self.reconf(a)
        location = self.insert_list(b,len_l)

        f = xlwt.Workbook()
        sheet1 = f.add_sheet('A',cell_overwrite_ok=True)
        for n,i in enumerate(location):
            sheet1.write(i[1],i[0],to_be_write[n])
        f.save(self.dest)

    def position_extra(self,s):
        left=re.findall(r'\bleft:(\d{2,4})px',s)
        top = re.findall(r'\btop:(\d{2,4})px', s)
        s_ext=[left[0],top[0]]
        return s_ext

    def extraction(self, filename):
        try:
            soup = BeautifulSoup(open(filename,"r",encoding='UTF-8'))
        except Exception as e:
            soup = BeautifulSoup(open(filename,"r"))
        num_div = len(soup.find_all('div'))
        style = []
        for i in range(num_div):
            style.append(soup.find_all('div')[i]['style'])
        num_span = []
        for i in range(num_div):
            num_span.append(len(soup.find_all('div')[i].find_all('span')))
        text = []
        for i in range(num_div):
            t = []
            for j in range(num_span[i]):
                t.append(soup.find_all('div')[i].find_all('span')[j].text)
            text.append(t)
        position = []
        for i in style:
            position.append(self.position_extra(i))
        return text,position


    def number_integrate(self, b):
        c=sorted(b)
        new_list=[]
        new_list.append(c[0])
        index1=0
        for i in range(len(c)):
            if index1>0:
                if abs(c[index1]-new_list[index1-1]) <10:
                    new_list.append(new_list[index1-1])
                else:
                    if abs(c[index1] - c[index1-1])>10:
                        new_list.append(c[index1])
                    else:
                        new_list.append(c[index1-1])
            index1=index1+1
        return new_list

    def coordinate_transform(self, ori_list):
        list_horizontal=[int(i[0]) for i in ori_list]
        list_vertical=[int(i[1]) for i in ori_list]
        list_hori=sorted(list_horizontal)
        list_ver=sorted(list_vertical)
        list_hori2=self.number_integrate(list_hori)
        list_ver2=self.number_integrate(list_ver)
        list_x=sorted(set(list_hori), key = list_hori.index)
        list_y=sorted(set(list_ver), key = list_ver.index)
        list_x_cor=[]
        list_y_cor=[]
        for i in list_horizontal:
            index=0
            list_x_cor.append(list_x.index(i))
            index=index+1
        for k in list_vertical:
            indey=0
            list_y_cor.append(list_y.index(k))
            indey=indey+1
        final_list=[]
        for j in range(len(list_x_cor)):
            final_list.append([list_x_cor[j],list_y_cor[j]])
        return final_list

    def merge(self,li):
        return ' '.join(li)

    def insert_list(self, loc_L,len_L):
        F_loc_L=[]
        for i,j in enumerate(len_L):
            if j==1:
                F_loc_L.append(loc_L[i])
            elif j>1:
                F_loc_L.append(loc_L[i])
                for t in range(1,j):
                    F_loc_L.append([loc_L[i][0],loc_L[i][1]+t])
        return F_loc_L

    def reconf(self, li):
        li_new = []
        for j,i in enumerate(li):
            li_new.append(self.merge(i))
        t = []
        for i in li_new:
            t.append(i.split('\n'))
        o = [];nu=''
        for i,j in enumerate(t):
            if nu in j:
                j.remove(nu)
                o.append(j)
            else:
                o.append(j)
        new_o = []
        for q in o:
            if len(q)<=1:
                new_o.append(q[0])
            else:
                for w in range(0,len(q)):
                    new_o.append(q[w])
        len_l = [len(kl) for kl in o]
        return o,new_o,len_l

