class Heating:
    def __init__(self, name, current_temp, min_temp, max_temp):
        self.name = name
        self._current_temp = current_temp
        self.min_temp = min_temp
        self.max_temp = max_temp

    def __str__(self):
        return (f'{self.name} is currently {self.current_temp} degrees and the minimum temperature {self.min_temp} and the maximum temperature {self.max_temp}')
    
    def __repr__(self):
        return f"Heating('{self.name}', {self.current_temp}, {self.min_temp}, {self.max_temp})"

    def change_temperature(self, temp_change):
        new_temp = self.current_temp + temp_change
        self.current_temp = new_temp

    @property
    def current_temp(self):
        return self._current_temp
    # This is a getter, it will return the current temperature.
    # It is a private value, it is not accessible from outside the class.
    
    
    @current_temp.setter
    def current_temp(self, new_temp):
        if new_temp < self.min_temp:
            self._current_temp = self.min_temp
        elif new_temp > self.max_temp:
            self._current_temp = self.max_temp
        else:
            self._current_temp = new_temp
    # This is a setter, it will set the current temperature.
    # if the new temperature is lower than the minimum temperature, 
    # it will set the current temperature to the minimum temperature.

    # if the new temperature is higher than the maximum temperature, 
    # it will set the current temperature to the maximum temperature.

    # if the new temperature is between the minimum and maximum temperature, 
    # it will set the current temperature to the new temperature.

living_room = Heating('Living room', 20, 15, 25)
print(living_room)