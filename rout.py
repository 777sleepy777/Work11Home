class Bus:
    def __init__(self, route: str) -> None:
        self.__route = None
        self.route = route
    
    @property
    def route(self) -> str:
        return f"#{self.__route}"

    @route.setter
    def route(self, route: str) -> None:
        if len(route) > 3:
            raise ValueError("Route must be 3 characters")
        self.__route = route
    
    def __str__(self) -> str:
        return f"Bus on route {self.route}"


try:
    bus = Bus("385q")
except ValueError as e:
    print(e)

print(bus)

bus.set_route("657")

print(bus.get_route())