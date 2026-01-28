# -----------------------------
# Step 1: Given constants
# -----------------------------
Q = 150              # Heat power
T_ambient = 25       # Ambient temperature in °C

# Material
k_al = 167           #(Aluminum)
k_tim = 4            #(Thermal grease)
k_air = 0.0262       #(Air)

# Air
air_velocity = 1
kinematic_viscosity = 1.57e-5
prandtl_number = 0.71

# -----------------------------
# Step 2: Geometry
# -----------------------------
die_area = 0.002363
tim_thickness = 0.0001

base_thickness = 0.0025
sink_width = 0.116
num_fins = 60
fin_thickness = 0.0008
fin_height = 0.0245

# -----------------------------
# Step 3: Thermal Resistances
# -----------------------------

# Junction-to-case resistance (given)
R_jc = 0.1   # °C/W

# TIM resistance
R_tim = tim_thickness / (k_tim * die_area)

# Heat sink conduction resistance
R_cond = base_thickness / (k_al * die_area)

# -----------------------------
# Step 4: Convection calculations
# -----------------------------
fin_spacing = (sink_width - (num_fins * fin_thickness)) / (num_fins - 1)

Re = (air_velocity * fin_spacing) / kinematic_viscosity

if Re < 2300:
    Nu = 1.86 * ((Re * prandtl_number * (2 * fin_spacing / fin_height)) ** (1/3))
else:
    Nu = 0.023 * (Re ** 0.8) * (prandtl_number ** 0.3)

h = (Nu * k_air) / (2 * fin_spacing)
#correction
h_correction = 0.6
h = h * h_correction

# Approximate surface area
# Effective area factor (accounts for non-ideal airflow)
area_efficiency = 0.55

total_area = area_efficiency * num_fins * 2 * fin_height * sink_width

R_conv = 1 / (h * total_area)

R_hs = R_cond + R_conv

# -----------------------------
# Step 5: Final results
# -----------------------------
R_total = R_jc + R_tim + R_hs
T_junction = T_ambient + (Q * R_total)

# Output
print("Total Thermal Resistance (°C/W):", round(R_total, 4))
print("Junction Temperature (°C):", round(T_junction, 2))
