#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 19:40:36 2021

@author: home
"""
                    #lets make this colourful!!
N = '\033[0m'     #NOCOLOUR
R = '\033[0;31m'  
B = '\033[0;34m'   #remaining all have their
G = '\033[0;32m'   #usual meanings
Y = '\033[1;33m'   
W = '\033[1;37m'  
O = '\033[0;33m'
P = '\033[0;35m'
LG = '\033[1;32m'
LB = '\033[1;34m'

import pickle as pkl
import os

filename = 'addressBook.pkl'
choice = 'y'
print(Y,'\n\t\tADDRESS BOOK',N)

try:
    file = open(filename,'rb')
    contacts_in_one_list = pkl.load(file)
    file.close()
except FileNotFoundError:
    file = open(filename,'wb')
    file.close()
except EOFError:
    contacts_in_one_list = []
    
def add_contact():
    contact = {}
    contact['Name'] = input('\033[0;35mName: ')
    contact['Number'] = input('Number: ')
    contact['Email'] = input('Email: \033[0m')
    contacts_in_one_list.append(contact)
    file = open(filename, 'wb')
    pkl.dump(contacts_in_one_list,file)
    file.close()
    print(LB,'Contact Saved!',N)
    
def display_contact():
    if not contacts_in_one_list:
        print(B,'No Contacts!',N)
    else:
        print(LG,"\nYour Contacts\n",N)
        for i in contacts_in_one_list:
            for key,values in i.items():
                print(W,key,':',values,N)
            print(N)

def delete_contact():
    if not contacts_in_one_list:
        print(B,'No Contacts!',N)
    else:
        searchis = input('{}Name to be deleted: {}'.format(P,N))
        for i in contacts_in_one_list:
            if i['Name'] == searchis:
                del contacts_in_one_list[contacts_in_one_list.index(i)]
                file = open(filename,'wb')
                pkl.dump(contacts_in_one_list,file)
                file.close()
                print(LB,'Contact Deleted!',N)
                break
        else:
            print(B,'Contact Not Found!',N)
         
            
def modify_contact():        
    if not contacts_in_one_list:
        print(B,'No Contacts!',N)
    else:
        searchis = input('{}Name to be modified: {}'.format(P,N))
        for i in contacts_in_one_list:
            if i['Name'] == searchis:
                nameis = input('{}Name: '.format(P))
                numberis = input('Number: ')
                emailis = input('Email: {}'.format(N))
                if len(nameis)!=0:
                    i['Name'] = nameis
                if len(numberis)!=0:
                    i['Number'] = numberis
                if len(emailis)!=0:
                    i['Email'] = emailis
                file = open(filename,'wb')
                pkl.dump(contacts_in_one_list,file)
                print(LB,'Changes Saved!',N)                
                file.close()
                break
        else:
            print(B,'No Contacts found!',N)
            
def search_contact():
    if not contacts_in_one_list:
        print(B,'No Contacts!',N)
    else:
        searchis = input('{}Name to be searched: {}'.format(P,N))
        for i in contacts_in_one_list:
            if i['Name'] == searchis:
                for key,value in i.items():
                    print(W,key,':',value,N)
                
                file = open(filename,'wb')
                pkl.dump(contacts_in_one_list,file)
                file.close()
                break
        else:
            print(B,'Contact Not Found!',N)

while choice!='x':
    print('\n{}1. Add Contact'.format(G))
    print('2. Display Contact')
    print('3. Delete Contact')
    print('4. Modify Contact')
    print('5. Search Contact')
    print('6. E[x]it{}'.format(N))
    choice = input("\t{}Your Choice: {}".format(P,N))
    if choice == '1':
        add_contact()
    elif choice == '2':
        display_contact()
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        modify_contact()
    elif choice == '5':
        search_contact()
    elif choice == 'x':
        print(Y,'EXITTED!',N)
    else:
        print(B,'Invalid Option!',N)
        
  