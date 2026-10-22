
import numpy as np
import pandas as pd

np.random.seed(42)

def simulate(n=1520, base_rate=0.03, lift=0.07, holdout_pct=0.15):
    """Simula atribución ingenua vs holdout para una cohorte de reactivación.
    
    n: tamaño total de la cohorte
    base_rate: tasa de conversión natural (sin agente)
    lift: incremento absoluto esperado por el agente
    holdout_pct: porcentaje que no recibe el agente
    """
    holdout_n = int(n * holdout_pct)
    treated_n = n - holdout_n
    
    holdout_conv = np.random.binomial(1, base_rate, holdout_n)
    treated_conv = np.random.binomial(1, base_rate + lift, treated_n)
    
    naive_rate = treated_conv.mean()
    holdout_rate = holdout_conv.mean()
    true_incremental = naive_rate - holdout_rate
    inflation = naive_rate / true_incremental if true_incremental > 0 else np.inf
    
    return {
        "n": n,
        "treated_n": treated_n,
        "holdout_n": holdout_n,
        "naive_rate": round(naive_rate, 4),
        "holdout_rate": round(holdout_rate, 4),
        "incremental_lift": round(true_incremental, 4),
        "inflation_factor": round(inflation, 2)
    }

if __name__ == "__main__":
    result = simulate()
    print(pd.DataFrame([result]).to_string(index=False))
    print("\nNota: con n≈1520 y holdout 15%, el factor de inflación muestra cuánto se sobreestima el lift si no se usa holdout.")
    print("Tamaño de muestra aproximado para detectar 5pp de lift (80% power, alpha=0.05): ~1500-2000 por brazo.")
