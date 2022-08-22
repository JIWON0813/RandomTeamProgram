import random

class Service:
    def __init__(self, room_number_dic, room_result_dic, priority_number):
        self.name_dic = {}
        self.room_number_dic = room_number_dic
        self.room_result_dic = room_result_dic
        self.priority_number = priority_number

    def get_name_dic(self, text):
        listByLine = text.split('\n')
        for line in listByLine:
            splitData = line.split(' ')
            if len(splitData) - 1 != self.priority_number:
                return None

            name = splitData[0]
            self.name_dic[name] = [splitData[i] for i in range(1, len(splitData), 1)]

        return self.name_dic

    def get_room_dic(self, text):
        listByLine = text.split('\n')
        for line in listByLine:
            splitData = line.split(' ')
            if len(splitData) != 2:
                return None

            self.room_number_dic[splitData[0]] = int(splitData[1])

        return self.room_number_dic

    def get_result(self, name_dic, room_number_dic):
        room_team_dic = {}
        room_result = {}
        for i in range(self.priority_number):
            for key in name_dic:
                room_name = name_dic[key][i]
                if room_name not in room_team_dic:
                    room_result[room_name] = []
                    room_team_dic[room_name] = []

                room_team_dic[room_name].append(key)

            room_result = self.get_random_team(room_team_dic, room_result, room_number_dic, name_dic)

        if len(name_dic) > 0:
            left_key, left_value = self.get_left_people(name_dic)
            room_result[left_key] = left_value

        result_text = self.change_result_to_text(room_result)
        return result_text

    def get_random_team(self, room_team_dic, room_result, room_number_dic, name_dic):
        for room_name in room_team_dic:
            for index in range(len(room_result[room_name]), len(room_team_dic[room_name]), 1):
                if index == room_number_dic[room_name]:
                    break;

                room = room_team_dic[room_name]
                if len(room) == 0:
                    break;

                max_num = len(room) - 1
                if max_num < 0:
                    randomNumber = 0
                else:
                    randomNumber = random.randint(0, max_num)

                name = room.pop(randomNumber)
                room_result[room_name].append(name)
                name_dic.pop(name)

        return room_result

    def change_result_to_text(self, room_result):
        text = ""
        for key in room_result:
            room_list = room_result[key]
            text += "{0} : {1}\n".format(key, ", ".join(room_list))

        return text

    def get_left_people(self, name_dic):
        return '남은사람', list(name_dic.keys())

    def set_priority_number(self, priority_number):
        self.priority_number = priority_number
