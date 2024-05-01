def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:

    with (
        open(data_file_name, "r") as data_file,
        open(report_file_name, "w") as report_file
    ):

        data = data_file.read().splitlines()
        supply = 0
        buy = 0

        for un in data:
            unit = un.split(",")
            if unit[0] == "supply":
                supply += int(unit[1])
            if unit[0] == "buy":
                buy += int(unit[1])

        result = supply - buy

        report_file.write(f"supply, {supply}\nbuy, {buy}\nresult, {result}\n")
