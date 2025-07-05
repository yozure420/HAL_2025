class Robot:
    def __init__(self,personal_num,name,model_type):
        self.__personal_num = personal_num
        self.__name = name
        self.__model_type = model_type
    def get_personal_num(self):
        return self.__personal_num
    def get_name(self):
        return self.__name
    def get_model_type(self):
        return self.__model_type
    def set_personal_num(self, value):
        self.__personal_num = value
    def set_name(self, value):
        self.__name = value
    def set_model_type(self, value):
        self.__model_type = value