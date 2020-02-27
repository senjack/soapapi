# def generateID():
#     initial_string = "RFCT/SOAP/ADM/001"
#     appended_string = ""
#     final_string = ""
#     return final_string


# adminitrator_id = "RFCT/SOAP/ADM/A001"
# staff_id = "RFCT/SOAP/STF/A001"
# applicant_id = "RFCT/SOAP/APT/{20}/A0001"

from models import Administrator

def admin_id_creator():
    print(Administrator.objects.all())
    
