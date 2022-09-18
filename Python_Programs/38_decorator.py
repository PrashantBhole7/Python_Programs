def dec1(func):
    def execnow():
        print("Executing Now")
        func()
        print("Executed")
    return execnow

@dec1
def who_is_prashant():
    print("Prashant is a good boy")

# Below lines are nothing but decorator
# who_is_prashant = dec1(who_is_prashant)
who_is_prashant()