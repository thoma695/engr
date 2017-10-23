from math import pow, pi

#given
energy_out = 120
gravity = 9.81
water_density = 1000

# #inputs
# pump_efficiency
# turbine_efficiency
# pipe_diameter
# pipe_length
# pipe_friction_factor
# reservoir_depth
# bottom_reservoir_elevation
# flow_rate_pump
# flow_rate_turbine
# bend_coefficient_1
# bend_coefficient_2
#
# #outputs
# reservoir_surface_area
# energy_in
# system_efficiency
# fill_time
# empty_time

#other variables



#functions needed
def energyTurbine(energy_out,turbine_efficiency):
    return energy_out * (1 / turbine_efficiency - 1)

def pipeFrictionDown(water_mass, pipe_friction_factor, pipe_length, velocity_down, pipe_diameter):
    return water_mass * (pipe_friction_factor * pipe_length * pow(velocity_down, 2) / (2 * pipe_diameter))

def energyLossHitting(water_mass, velocity_down):
    return water_mass * pow(velocity_down, 2) / 2


