import numpy as np 
import pandas as pd 
import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
import tkinter.filedialog 


nd_filename=''
ed_filename=''
G=nx.Graph()
node=[]
edge=[]

def nd_file_open():
    global nd_filename
    nd_filename=nd_file=tk.filedialog.askopenfilename()
    nd_file_etr.insert(tk.INSERT,nd_filename)

def ed_file_open():
    global ed_filename
    ed_filename=tk.filedialog.askopenfilename()
    ed_file_etr.insert(tk.INSERT,ed_filename)

def path_draw():
    nodes=np.array(np.arange(int(nd_etr.get())))
    G.clear()
    G.add_path(nodes)
    nx.draw(G,with_labels=True)
    plt.show()

def star_draw():
    nodes=np.array(np.arange(int(nd_etr.get())))
    G.clear()
    G.add_star(nodes)
    nx.draw(G,with_labels=True)
    plt.show()

def circle_draw():
    nodes=np.array(np.arange(int(nd_etr.get())))
    G.clear()
    G.add_cycle(nodes)
    nx.draw(G,with_labels=True)
    plt.show()
    
def measure():
    global node,edge
    G.clear()
    node_csv=pd.read_csv(nd_filename)
    edge_csv=pd.read_csv(ed_filename)
    node=node_csv.sample(n=100).to_numpy().ravel()
    edge=edge_csv.sample(n=100).to_numpy()
    G.add_nodes_from(node)
    G.add_edges_from(edge)
    total=0
    for C in nx.connected_component_subgraphs(G):
        total+=nx.average_shortest_path_length(C)
    avg_path=total/len(G)
    avg_degree=nx.average_degree_connectivity(G)
    avg_clustering=nx.average_clustering(G)
    measure_res.insert(tk.INSERT,'平均路径:%s \n平均度数:%s \n 平均聚集: %s'%(avg_path,avg_degree,avg_clustering))

def draw():
    global node,edge
    G.clear()
    G.add_nodes_from(node)
    G.add_edges_from(edge)
    nx.draw(G,with_labels=True)
    plt.show()

win=tk.Tk()
win.title('网络测度系统')

stc_lb=tk.Label(win,text='典型网络结构')
nd_lb=tk.Label(win,text='节点数')
nd_etr=tk.Entry(win,width=10)
frm1=tk.Frame(win)
star_bt=tk.Button(frm1,text='星型',command=star_draw)
path_bt=tk.Button(frm1,text='线性',command=path_draw)
circle_bt=tk.Button(frm1,text='环形',command=circle_draw)
measure_lb=tk.Label(win,text='网络测度')
nd_file_lb=tk.Label(win,text='节点文件')
nd_file_etr=tk.Text(win,height=1,width=40)
nd_open=tk.Button(win,text='打开',command=nd_file_open)
ed_file_lb=tk.Label(win,text='边文件')
ed_file_etr=tk.Text(win,height=1,width=40)
ed_open=tk.Button(win,text='打开',command=ed_file_open)
measure_bt=tk.Button(win,text='测度',command=measure)
draw_bt=tk.Button(win,text='绘图',command=draw)
measure_res=tk.Text(win,height=20,width=40)

stc_lb.grid(row=0,column=0)
nd_lb.grid(row=1,column=0)
nd_etr.grid(row=1,column=1,sticky=tk.W)
frm1.grid(row=2,columnspan=3,sticky=tk.E+tk.W)
path_bt.grid(row=0,column=0)
star_bt.grid(row=0,column=1)
circle_bt.grid(row=0,column=2)
measure_lb.grid(row=3,column=0)
nd_file_lb.grid(row=4,column=0)
nd_file_etr.grid(row=4,column=1,sticky=tk.E+tk.W)
nd_open.grid(row=4,column=2)
ed_file_lb.grid(row=5,column=0)
ed_file_etr.grid(row=5,column=1,sticky=tk.E+tk.W)
ed_open.grid(row=5,column=2)
measure_bt.grid(row=6)
draw_bt.grid(row=7,sticky=tk.N)
measure_res.grid(row=6,column=1,columnspan=1,rowspan=2)


win.mainloop()

