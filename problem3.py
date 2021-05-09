from copy import deepcopy

class problem3:

    def __init__(self, ori_hub_dest):
        self._ori_hub_dest=ori_hub_dest

    def solving_Problem3(self):
        print(self.__rankify())
        print(self.__scoring())

    def __rankify(self):
        result=deepcopy(self._ori_hub_dest)
        for idx in range(len(self._ori_hub_dest)):
            for i in range(len(self._ori_hub_dest[idx])):
                count=0
                for j in range(len(self._ori_hub_dest[idx])):
                    if (self._ori_hub_dest[idx][j]>self._ori_hub_dest[idx][i]):
                        count+=1
                result[idx][i]=count+1
        return result

    def __scoring(self):
        result=self.__rankify()
        for idx in range(len(result)):
            for jdx in range(len(result[idx])):
                result[idx][jdx]=result[idx][jdx]/5
        return result
