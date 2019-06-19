
class Solution:
    def canVisitAllRooms(self, rooms):
        ownKeys = set([0])
        notEnterRooms = {x for x in range(len(rooms))}

        while len(ownKeys)>0:
            key = ownKeys.pop()
            if key in notEnterRooms:
                notEnterRooms.remove(key)
                ownKeys.update(rooms[key])

        if len(notEnterRooms)>0:
            return False
        else:
            return True


s = Solution()
print(s.canVisitAllRooms([[1],[2],[3],[]]))

