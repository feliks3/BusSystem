
class Stop:
    def __init__(self, code) -> None:
        self.code = code

    def get_code(self):
        return self.code


class Route:
    def __init__(self, route_name, stops) -> None:
        self.route_name = route_name
        self.stops = stops

    def details(self):
        details = ""
        details += ("route name:" + self.route_name + " ")
        details += "route stops:"
        for id in self.stops:
            details += (self.stops[id].code + " ")

        return details

class Line:
    def __init__(self, id, routes) -> None:
        self.id = str(id)
        self.routes = routes

    def details(self):
        details = ""
        details += "Line id:" + str(self.id) + "\n"
        for id in self.routes:
            details += self.routes[id].details() + "\n"
        return details


class TimeSchedule:
    def __init__(self, first_arrival_time) -> None:
        self.first_arrival_time = first_arrival_time

    def details(self):
        return self.first_arrival_time

class Bus:
    def __init__(self, id, line=None, time_schedule=None) -> None:
        self.id = str(id)
        self.line = line
        self.time_schedule = time_schedule

    def assign_bus(self, line, time_schedule):
        self.line = line
        self.time_schedule = time_schedule

    def details(self):
        details = ""
        details += "bus id:" + str(self.id) + "\n"
        details += "line:" + self.line.details()
        details += "time schedule:" + str(self.time_schedule.details())
        return details

class Bussystem:
    def __init__(self, buses=None, lines=None, routes=None, stops=None) -> None:
        self.buses = {} if buses == None else buses
        self.lines = {} if lines == None else lines
        self.routes = {} if routes == None else routes
        self.stops = {} if stops == None else stops

    def add_buses(self, buses):
        for bus_id in buses:
            if buses[bus_id].id not in self.buses:
                self.buses[buses[bus_id].id] = buses[bus_id]

    def remove_buses(self, buses):
        for bus_id in buses:
            if int(buses[bus_id].id) in self.buses:
                del self.buses[int(buses[bus_id].id)]

    def define_stop(self, code):
        stop = Stop(code)
        return stop

    def add_stops(self, stop_codes):
        stops = {}
        for code in stop_codes:
            if code not in self.stops:
                stop = self.define_stop(code)
                stops[code] = stop
                self.stops[code] = stop
            else:
                stops[code] = self.stops[code]
                print("stop " + str(code) + " already exist")
        return stops

    def get_stops(self, stop_codes):
        stops = {}
        for stop_code in stop_codes:
            if stop_code in self.stops:
                stops[stop_code] = self.stops[stop_code]
        return stops

    def define_route(self, route_name, stops):
        route = Route(route_name, stops)
        return route

    def add_route(self, route_name, stops):
        route = self.define_route(route_name, stops)
        if route.route_name not in self.routes:
            self.routes[route.route_name] = route
        else:
            print("route " + route.route_name + " already exist")
        return self.routes[route.route_name]

    def define_line(self, line_id, routes):
        line = Line(line_id, routes)
        return line

    def add_line(self, line_id, routes):
        line = self.define_line(line_id, routes)
        if line.id not in self.lines:
            self.lines[line.id] = line
        else:
            print("line " + line.id + " already exist")
        return self.lines[line.id]

    def define_bus(self, bus_id):
        return Bus(bus_id)

    def define_add_bus(self, bus_id):
        if bus_id not in self.buses:
            bus = self.define_bus(bus_id)
            self.buses[bus_id] = bus
        else:
            print("bus " + bus_id + " already exist")
        return self.buses[bus_id]

    def assign_bus(self, bus, line, time):
        bus.assign_bus(line, time)

    def details(self):
        details = ""
        details += "Bus:"
        for id in self.buses:
            details += self.buses[id].id + " "
        details += "\n"

        details += "Line:"
        for id in self.lines:
            details += str(self.lines[id].id) + " "
        details += "\n"

        details += "Route:"
        for id in self.routes:
            details += self.routes[id].route_name + " "
        details += "\n"

        details += "Stop:"
        for id in self.stops:
            details += str(self.stops[id].code) + " "
        details += "\n"
        details += "\n"

        details += "Bus details:\n"
        for id in self.buses:
            details += "bus " + self.buses[id].id + ": Line" + self.buses[id].line.id + \
                " " + self.buses[id].time_schedule.first_arrival_time + "\n"
        details += "\n"

        details += "Line details:\n"
        for id in self.lines:
            details += "Line" + str(self.lines[id].id) + ": "
            for route_id in self.lines[id].routes:
                details += "" + \
                    self.lines[id].routes[route_id].route_name + " "
            details += "\n"
        details += "\n"

        details += "Route details:\n"
        for id in self.routes:
            details += self.routes[id].route_name + ": "
            for stop_id in self.routes[id].stops:
                details += "stop" + \
                    str(self.routes[id].stops[stop_id].code) + " "
            details += "\n"
        return details


def main():
    bussystem = Bussystem()
    stop_codes1 = [1, 2, 3, 4, 5]
    stops1_1 = bussystem.add_stops(stop_codes1)
    route1_1 = bussystem.add_route("route1_1", stops1_1)
    stops1_2 = bussystem.get_stops([5, 4, 3, 2, 1])
    route1_2 = bussystem.add_route("route1_2", stops1_2)
    routes1 = {route1_1.route_name: route1_1, route1_2.route_name: route1_2}
    line1 = bussystem.add_line(1, routes1)
    timeSchedule1 = TimeSchedule("10:00")
    bus1 = bussystem.define_add_bus(1)
    bussystem.assign_bus(bus1, line1, timeSchedule1)

    stop_codes2 = [6,7,8,9,10]
    stops2_1 = bussystem.add_stops(stop_codes2)
    route2_1 = bussystem.add_route("route2_1", stops2_1)
    stops2_2 = bussystem.get_stops([10,9,8,7,6])
    route2_2 = bussystem.add_route("route2_2", stops2_2)
    routes2 = {route2_1.route_name: route2_1, route2_2.route_name: route2_2}
    line2 = bussystem.add_line(2, routes2)
    timeSchedule2 = TimeSchedule("13:00")
    bus2 = bussystem.define_add_bus(2)
    bussystem.assign_bus(bus2, line2, timeSchedule2)

    stop_codes3 = [11, 12, 13, 14, 15]
    stops3_1 = bussystem.add_stops(stop_codes3)
    route3_1 = bussystem.add_route("route3_1", stops3_1)
    stops3_2 = bussystem.get_stops([15,14,13,12])
    route3_2 = bussystem.add_route("route3_2", stops3_2)
    routes3 = {route3_1.route_name: route3_1, route3_2.route_name: route3_2}
    line3 = bussystem.add_line(3, routes3)
    timeSchedule3 = TimeSchedule("15:00")
    bus3 = bussystem.define_add_bus(3)
    bussystem.assign_bus(bus3, line3, timeSchedule3)
    
    stop_codes4 = [21, 22, 23, 24, 25]
    stops4_1 = bussystem.add_stops(stop_codes4)
    route4_1 = bussystem.add_route("route4_1", stops4_1)
    stops4_2 = bussystem.get_stops([25,14,22,12])
    route4_2 = bussystem.add_route("route4_2", stops4_2)
    routes4 = {route4_1.route_name: route4_1, route4_2.route_name: route4_2}
    line4 = bussystem.add_line(4, routes4)
    timeSchedule4 = TimeSchedule("11:00")
    bus4 = bussystem.define_add_bus(4)
    bussystem.assign_bus(bus4, line4, timeSchedule4)
    
    
    print("*******************")
    print("add 4 buses\n")
    print(bussystem.details())
    buses_to_removed = {bus2.id:bus2,bus3.id:bus3,bus4.id:bus4}

    print("*******************")
    print("remove bus 2 3 and 4\n")
    bussystem.remove_buses(buses_to_removed)
    print(bussystem.details())

    print("*******************")
    print("add bus 2 and 4 again\n")
    buses_to_add = {bus2.id:bus2,bus4.id:bus4}
    bussystem.add_buses(buses_to_add)
    print(bussystem.details())

    print("*******************")
    print("assign bus 2 with line 3 and time schedule 3\n")
    bussystem.assign_bus(bus2, line3, timeSchedule3)
    print(bussystem.details())

    print("*******************")
    print("add stops, stop 2 and stop 4 are alreay in it\n")
    stop_codes5 = [31, 2, 33, 4, 35]
    stops5_1 = bussystem.add_stops(stop_codes5)
    route5_1 = bussystem.add_route("route5_1", stops5_1)
    stops5_2 = bussystem.get_stops([35, 4, 33, 2, 31])
    route5_2 = bussystem.add_route("route5_2", stops5_2)
    stops5_3 = bussystem.get_stops([31, 2, 33, 4])
    route5_3 = bussystem.add_route("route5_3", stops5_3)
    routes5 = {route5_1.route_name: route5_1, route5_2.route_name: route5_2, route5_3.route_name: route5_3}
    line5 = bussystem.add_line(5, routes5)
    timeSchedule5 = TimeSchedule("12:00")
    bus5 = bussystem.define_add_bus(5)
    bussystem.assign_bus(bus5, line5, timeSchedule5)

    print(bussystem.details())

if __name__ == "__main__":
    main()
