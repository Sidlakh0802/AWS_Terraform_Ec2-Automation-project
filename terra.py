import subprocess

def terraform_run(command):
    subprocess.run(command, shell=True,check=True)
directory = "/Users/sid0802/PycharmProjects/pthon_workishop_with_shubham/practice/terra-automate/Wanderlust-Mega-Project/terraform"
#command = f"terraform -chdir={directory} init"
command = f"terraform -chdir={directory} apply -auto-approve"
terraform_run(command)