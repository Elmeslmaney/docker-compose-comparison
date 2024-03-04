import yaml
from openpyxl import Workbook

class ComposeComparator:
    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2
        self.services1 = self._extract_services(file1)
        self.services2 = self._extract_services(file2)
        self.common_services = set(self.services1.keys()) & set(self.services2.keys())
        self.unique_services_file1 = set(self.services1.keys()) - set(self.services2.keys())
        self.unique_services_file2 = set(self.services2.keys()) - set(self.services1.keys())
        print('here')
    def _extract_services(self, file_path):
        with open(file_path, 'r') as file:
            compose_data = yaml.safe_load(file)
            if 'services' in compose_data:
                return compose_data['services']
            else:
                return {}

    def compare_services(self):
        return self.common_services, self.unique_services_file1, self.unique_services_file2

    def compare_versions(self):
        version_comparison = []
        for service, version in self.services1.items():
            if service in self.services2:
                version_file2 = self.services2[service].get('image')
                if version_file2:
                    version_file2 = version_file2.split(":")[-1]
                    version = version.get('image').split(":")[-1]
                    if version != version_file2:
                        version_comparison.append((service, version, version_file2))
                else:
                    version_comparison.append((service, version, "No version specified in file2"))
        return version_comparison

def write_to_excel(file_path, comparator):
    wb = Workbook()
    ws = wb.active
    ws.append(["Comparison Type", "Service Name", "online-compose", "staging-compose"])

    common_services, unique_services_file1, unique_services_file2 = comparator.compare_services()
    for service in common_services:
        ws.append(["Common", service, comparator.services1[service]['image'], comparator.services2[service]['image']])

    for service in unique_services_file1:
        ws.append(["Unique to File 1", service, comparator.services1[service]['image'], ""])

    for service in unique_services_file2:
        ws.append(["Unique to File 2", service, "", comparator.services2[service]['image']])

    version_comparison = comparator.compare_versions()
    for service, version1, version2 in version_comparison:
        # Convert the dictionary to a string representation
        service_config_str = str(comparator.services1[service])
        ws.append(["Version Mismatch", service, version1, version2, service_config_str])

    wb.save(file_path)

if __name__ == "__main__":
    file1 = "online-compose.yml"
    file2 = "staging-compose.yml"
    comparator = ComposeComparator(file1, file2)
    output_excel_file = "docker_compose_comparison.xlsx"
    write_to_excel(output_excel_file, comparator)
    print(f"Comparison results have been written to '{output_excel_file}'")
