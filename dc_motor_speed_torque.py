# Python Program to Calculate Speed and Torque of a DC Motor

print("========================================")
print("      DC MOTOR SPEED & TORQUE")
print("========================================")

# Input values
V = float(input("Enter supply voltage (V): "))
Ia = float(input("Enter armature current (A): "))
Ra = float(input("Enter armature resistance (ohm): "))
Eb = float(input("Enter back EMF (V): "))
P = float(input("Enter mechanical output power (W): "))
N = float(input("Enter motor speed (RPM): "))

# Calculate speed
# Back EMF equation: Eb = V - Ia*Ra
calculated_Eb = V - (Ia * Ra)

# Speed is proportional to back EMF for constant flux
speed_ratio = calculated_Eb / Eb
calculated_speed = N * speed_ratio

# Calculate torque
# T = P / omega
omega = (2 * 3.14159 * N) / 60
torque = P / omega

# Display results
print("\n------------- RESULTS ----------------")
print(f"Calculated Back EMF : {calculated_Eb:.2f} V")
print(f"Motor Speed         : {calculated_speed:.2f} RPM")
print(f"Motor Torque        : {torque:.2f} N-m")
print("--------------------------------------")
