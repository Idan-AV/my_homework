class USDConverter:
    def __init__(self, usd, nis, yen):
        self.usd = usd
        self.nis = nis
        self.yen = yen

    def convers_usd_to_nis(self):
        usd_to_nis = self.usd * 3.5
        return usd_to_nis

    def convers_usd_to_yen(self):
        usd_to_yen = self.usd * 136.72
        return usd_to_yen

    def convers_usd_to_euro(self):
        usd_to_euro = self.usd * 0.94
        return usd_to_euro

    def japanese_yen_to_usd(self):
        yen_to_usd = self.yen * 0.0073
        return yen_to_usd


if __name__ == "__main__":
    convert = USDConverter(100, 100, 100)
    my_nis = convert.convers_usd_to_nis()
    print(f"convert usd to nis {my_nis}₪")
    my_euro = convert.convers_usd_to_euro()
    print(f"convert usd to euro {my_euro}")
    my_yen = convert.convers_usd_to_yen()
    print(f"convert usd to yen {my_yen}")
    my_usd_from_yen = convert.japanese_yen_to_usd()
    print(f" convert yen to usd {my_usd_from_yen}")
