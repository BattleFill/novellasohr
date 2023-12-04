# -*- coding: cp1251 -*-
import os
import json
import csv
def convert_response(response): 
    if response == "��" or response == "lf":
        return 1
    elif response == "��" or response == "Lf":
        return 1
    elif response == "yes" or response == "���":
        return 1
    elif response == "yes" or response == "���":
        return 1
    elif response == "���" or response == "ytn":
        return 2
    elif response == "���" or response == "Ytn" or response == "���" or response == "yTN":
        return 2
    elif response == "���" or response == "YTN":
        return 2
    elif response == "No" or response == "��" or response == "nO" or response == "��":
        return 2
    elif response == "no" or response == "��":
        return 2
    elif response == "NO" or response == "��":
        return 2
def wait_for_enter():
    input("������� Enter ��� �����������...")
def checkint():
    while True:
        try:
            input_data = int(input())
            return input_data
            break
        except ValueError:
            print("�� ����� �� �����. ���������� �����: ")
          
def save_data(person):
    with open('save_file.json', 'w') as file:
        json.dump(person, file)

def load_data():
    if os.path.exists('save_file.json'):
        with open('save_file.json', 'r') as file:
            return json.load(file)
    else:
        return None

def delete_save():
    if os.path.exists('save_file.json'):
        os.remove('save_file.json')
        print("���������� ������� �������.")
    else:
        print("���������� �� �������.")

def save_to_csv(person):
    fieldnames = ['name', 'age', 'weapon', 'bronya', 'Klass']
    if not os.path.exists('game_data.csv'):
        with open('game_data.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            

person = {"name": "???", "age": "???", "weapon": "???", "bronya": "???", "Klass": "???", "???": 0}

print("1.����� ����")
print("2.��������� ����������")
print("3.������� ����������")
while True:
    print("������� ����� ������:")
    nachalo = checkint()
    if nachalo == 1:
        break
    if nachalo == 2:
        person = load_data()
        break
    if nachalo == 3:
        delete_save()
        break
    else:
        print("�������, �� ���� ������� �� �������� � ������")
            
if person["???"] == 0:
    print('Terraria part 1\n')
    print('����������')
    print('�� ��������� � ����������� ���, ������� �� �� ������� ��� �� ������.����� ���� �� ���� ������� ���������.')
    print('������������, ��� �� ������... ��� ��� �������������. �� ���� � ��������� ������� ���������.')
    print('����� �� ��������, ��� ������ ��� ���� ������ ���, ����� � ����������� �����.')
    print('�� ������ ������ ���� ������ � �����, ������ � �������� �������� �����, ������� �� ��������. ��� �� �������� ����. �������, �� ��� ��� � �����.')
    print('�� ��� �� ����� ����� �� ���, �� �������,��� �� ����� ����� ����, ����� ������ ��� �� ���������� ������!!!')
    print('��� �������� ���� � ����, � ����� ������, ��� ����� �������� ���.')
    wait_for_enter()
    print('����� �� ������ ����-���� �������� �� ������ ������� � ���������.')
    print('� � ���� ������ �� ���������� �������� ������ � �� ����� ���������� ��� ���, ��� �� �� �����.')
    print('�� ����� ������, �� ��������� ������ ���� ���.')
    name = str(input("������� ���: "))
    person["name"] = name
    person["???"] = 1
    save_data(person)
if person["???"] == 1:
    print('�� � ������� �����, �� ������� ������� ���� ���� ������.')
    print('������ �� ' + name)
    print('�� � �� ������ ��� ��� ����������')
    print('�� ���������� � ���������. ��� �� ��� ����?')
    wait_for_enter()
    print('� ��� ���� ����� ��������� � �� ������������ �� ����� �������:')
    print('1.����')
    print('2.������')
    print('3.���')
    while True:
        print("������� ����� ������:")
        klasvibor = checkint()
        if klasvibor == 1:
            klas = str("����")
            break
        if klasvibor == 2:
            klas = str("������")
            break
        if klasvibor == 3:
            klas = str("���")
            break
        else:
            print("�������, �� ���� ������� �� �������� � ������")
    person["Klass"] = klas
    person["???"] = 2
    save_data(person)
    print("������ �� " + klas + ".")
    print("������ ���� ��������. �� ������, ��� ��� ���� ���������.")
    wait_for_enter()

if person["???"] == 2:
    print("\n����� ???")
    print("��� ��������� ���� ���, �� ��� ���� � �������.")
    print("�� �� ���� ��� ������ ��������� � �� ������ ������� ������� ���� �������� � ������������ ���")
    print("�� ������ �� ������. ���� �� ��������� ��������� ����� � �������� ������, �� ���� �� �� ��������� ���� �����.")
    print("�� ��������� ����� ���������� ����� ������ ������ ������:\n �� ������� �������, ���� � �����-�� �������� � ���������� ����������... �� ������� � ������ ")
    print("������ ��� ��� ���������� ������ � ������ ����������, �������� � � �� �� ����� ��������� ��������, � ����� ���� ������ ������")
    wait_for_enter()
    print("��� ���� �� �� ����� ������� � �����")
    print("������ �������� �� ����������� � �������� ����� �����, �� � ����� ����������� �� ���-�� ������")
    print("��� ���� ������ �� ������� �����... � �� ��� ��� � �������... �������")
    print("���� ��� ��������� ������� ��� ����� ����������� � ����� ������, �� ������ ��� ��� ����� �� ���-�� ����� ����� ��������� � �������� ��� ���������.")
    print("�� ��������� ��� ���� ������. �� �� ������ ��� ���� ��� ��� �������� � ����� ����� ������")
    print("�� � �� ���� ����... �����...�� �� ���� ���� ������")
    wait_for_enter()
    print("����� ����� �� ���������� ������ ����������")
    print("��� �� " + person["Klass"] + " " + person["name"] + " �� ��� ������ ����� ������� ����� � ���� �����-�� ������ �������")
    print("�� ������ ������ �� ���� �� ������� �����, ��������� ��� ���� �������� ����������")
    print("� ���� �������, � �������... �������? � ������� ����� ���� �������. ��� ����� �� ���� ������ �� ������.")
    wait_for_enter()
    print("����� ��� �� �������������� � �����. �� ������������ �� � ���?")
    broni = ["���������� �����","����� �� �������� ������","���������� �����"]
    while True:
        print("������� ����� �������:")
        cer = str(input())
        otveta = convert_response(cer)
        if otveta == 1:
            print("��� ��� ����������� ��� ������� ����� �� �������. �������, �� �� ��������� ���������� �������.")
            print("�� � � ������ �������")
            person["bronya"] = broni[0]
            break
        if otveta == 2:
            print("�� ������� ������� ����� ����")
            print("������� ������ ��� �� �� ������?")
            print("1.������")
            print("2.������")
            print("3.������� ������")
            print("4.������")
            while True:
                print("������� ����� ������:")
                vibor1 = checkint()
                if vibor1 == 1:
                    person["bronya"] = broni[2]
                    break
                if vibor1 == 2:
                    person["bronya"] = broni[0]
                    break
                if vibor1 == 3:
                    person["bronya"] = broni[1]
                    break
                if vibor1 == 4:
                    person["bronya"] = broni.pop()
                    print("�� � ����� �������" + person["bronya"])
                    break
                else:
                    print("�������, �� ���� ������� �� �������� � ������")
                break
            break
    print("����� ���������� ��������� ������� �� ������� ���� ����� �� �������")
    wait_for_enter()
    person["???"] = 3
    save_data(person)
    
if person["???"] == 3:
    print("����� ����� �� ������ � ����� � ���� � �� ���� �� �������� ������� ����� ���������� ������")
    wait_for_enter()
    if person["Klass"] == "����":
        print("��� ��� ��� ����������, �� ������� ��� �����")
        person["weapon"] = "�����"
    if person["Klass"] == "���":
        print("��� ��� ��� ������. �������� ���������, �� � ������ ������ �����")
        person["weapon"] = "������"
    if person["Klass"] == "������":
        print("��� ��� ��� ���������� ���. �������� ������� � �����")
        person["weapon"] = "���������� ���"
    person["???"] = 4
    save_data(person)
    wait_for_enter()
    
if person["???"] == 4:
    print("�� �������� ��������� ��� ����, �� ������� �������� �� ������. ���� ���� ����� ������ ������.")
    print("� ������������ �� � ���. �� �������, ��� �� ������, �� ���������� ���� ��� ��� � �� ������� �����, ��� �� ����.")
    print("������ ��������")
    wait_for_enter()
    print("�� ������ ����� �������� �������� �����, ������� �� �����, � �������� ���� � �������� �������")
    print("��� ��� ��������, �� �������. �� ������������� ������ �� ���� ����� � ������ ������� ���������� ��������� ���� �������")
    print("��� ��-�� ����� ������ ������ ���������� � �� ����������� ����")
    print("�� ����������� ����������� ��������� ��� ������� ������ � � ����� ��� ������ � ������������.")
    wait_for_enter()
    if person["bronya"] == "���������� �����":
        print("��� ���� ������ ������. �� ���� ����� �� ������.")
    else:
        print("��� ���� ������ ������. �� ���� �� ������ � ���� ����� ���������.")
    print("�� ������ ����� ������� ���-�� ������� �� �����.")
    print("�� ������� � ����� ����� � ������ �������������.")
    print("� ����� �� ������ ������������ � ����� �������� � ��� ������� ������� ������")
    wait_for_enter()
    print("�����")
    save_to_csv(person)

