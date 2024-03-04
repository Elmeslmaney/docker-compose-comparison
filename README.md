# docker-compose-comparison
This Python script is designed to compare two Docker Compose YAML files (`online-compose.yml` and `staging-compose.yml`) and write the comparison results to an Excel file (`docker_compose_comparison.xlsx`). The comparison includes:

1. Finding common services between the two files.
2. Identifying services unique to each file.
3. Comparing versions of services between the files.

Here's a breakdown of the script:

- The `ComposeComparator` class is responsible for extracting services from the provided YAML files, comparing services, and comparing versions.
- The `write_to_excel` function is responsible for writing the comparison results to an Excel file.

Here's what the script does:

1. It initializes a `ComposeComparator` object with the paths to the two YAML files.
2. It specifies the output Excel file path.
3. It calls the `write_to_excel` function with the output file path and the `ComposeComparator` object to write the comparison results to the Excel file.
4. It prints a message indicating where the comparison results have been written.

The comparison results in the Excel file include:
- Common services between the two files.
- Services unique to each file.
- Version mismatches between the two files, if any.

The script utilizes the `yaml` library to parse YAML files and the `openpyxl` library to manipulate Excel files.
