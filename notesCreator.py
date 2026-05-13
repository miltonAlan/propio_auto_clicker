import argparse

def create_sql_file(filename="propio.sql", total_lines=50000):
    if total_lines < 2:
        raise ValueError("El archivo debe tener al menos 2 líneas para /* y */")

    with open(filename, "w", encoding="utf-8") as f:
        # Primera línea
        f.write("/*\n")

        # Líneas vacías
        for _ in range(total_lines - 2):
            f.write("\n")

        # Última línea
        f.write("*/\n")

    print(f"Archivo '{filename}' creado con {total_lines} líneas.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Genera un archivo SQL completamente comentado con líneas vacías")
    parser.add_argument("--file", default="propio.sql", help="Nombre del archivo")
    parser.add_argument("--lines", type=int, default=50000, help="Número total de líneas")

    args = parser.parse_args()

    create_sql_file(
        filename=args.file,
        total_lines=args.lines
    )