import pandas as pd


def cargar_datos(ruta):
    return pd.read_csv(ruta)


def limpiar_texto(df):
    df["paciente"] = df["paciente"].str.title()
    df["especialidad"] = df["especialidad"].str.upper()
    return df


def procesar_fechas(df):
    df["fecha_cita"] = pd.to_datetime(df["fecha_cita"], errors="coerce")
    return df.dropna(subset=["fecha_cita"])


def aplicar_reglas_negocio(df):
    return df[
        (df["estado"] == "CONFIRMADA") &
        (df["costo"] > 0)
    ]


def manejar_nulos(df):
    df["telefono"] = df["telefono"].fillna("NO REGISTRA")
    return df


def guardar_datos(df, ruta):
    df.to_csv(ruta, index=False)


def run_etl():
    df = cargar_datos("data/citas_clinica.csv")
    df = limpiar_texto(df)
    df = procesar_fechas(df)
    df = aplicar_reglas_negocio(df)
    df = manejar_nulos(df)
    guardar_datos(df, "data/output.csv")


if __name__ == "__main__":
    run_etl()
