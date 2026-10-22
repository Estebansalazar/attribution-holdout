# Holdout por tarea: hacer atribuible el impacto de agentes

## Problema
La atribución ingenua (todos los que convierten después del contacto) infla el lift. Ignora que parte de la cohorte habría convertido de todos modos.

## Propuesta de producto
Holdout por tarea (reactivación, no-shows, churn). Un porcentaje aleatorio de la cohorte no recibe el agente. Se mide la diferencia real.

### Casos borde
- **Inbound**: no usar holdout. El usuario pidió ayuda.
- **Reactivación / no-show / churn**: sí. El usuario no pidió contacto.
- Tamaño de muestra mínimo para detectar el efecto esperado.
- Reglas de detención (opt-out, compliance).

## Cómo medirlo en las primeras 2 semanas
1. Definir la tarea y el outcome binario.
2. Randomizar holdout (10-20%).
3. Reportar lift incremental + intervalo, no solo tasa de conversión del grupo tratado.

## Ejecutar la simulación
```bash
python attribution_sim.py
