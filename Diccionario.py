persona={"nombre":"Nancy", "edad":22, "ciudad":"México"}
print(persona["nombre"])
print(persona["edad"])
print(persona["ciudad"])

print(persona.keys())
print(persona.values())
print(persona.items())

persona.update({"profesion":"ingeniera"})
print(persona)