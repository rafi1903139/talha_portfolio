from django.shortcuts import render
from planner.models import AreaOfExpertise, ExtraCurricular, Education, LanguageSkill, OrganizationalAffiliation, Participation, Portfolio, Reference, SoftwareSkill, Training, Experience, TrainingSection, TrainingSubSection
import re 
# Create your views here.

def getOrgInfo(input_string):
    # Define regular expression patterns
    business_type_pattern = re.compile(r'\*Business Type: (.+)')
    organization_type_pattern = re.compile(r'\*Organization Type: (.+)')
    address_pattern = re.compile(r'\*Address: (.+)')

    # Find matches in the input string
    business_type_match = business_type_pattern.search(input_string)
    organization_type_match = organization_type_pattern.search(input_string)
    address_match = address_pattern.search(input_string)

    # Extract information
    business_type = business_type_match.group(1) if business_type_match else None
    organization_type = organization_type_match.group(1) if organization_type_match else None
    address = address_match.group(1) if address_match else None

    # Print the extracted information
    data = {"business_type" : business_type,
            "organization_type" :organization_type,
            "address" : address,
            }

    return data 

def getProjectInfo(input_string):
        # Define regular expression patterns
        project_name_pattern = re.compile(r'Project Name: (.+)')
        summary_pattern = re.compile(r'Summary: (.+)')
        work_station_pattern = re.compile(r'Work Station: (.+)')
        project_location_pattern = re.compile(r'Project Location: (.+)')
        supervisor_name_pattern = re.compile(r'Supervisor Name: (.+)')
        designation_pattern = re.compile(r'Designation: (.+)')
        email_pattern = re.compile(r'Email: (.+)')
        mobile_pattern = re.compile(r'Mobile: (.+)')

        # Find matches in the input string
        project_name_match = project_name_pattern.search(input_string)
        summary_match = summary_pattern.search(input_string)
        work_station_match = work_station_pattern.search(input_string)
        project_location_match = project_location_pattern.search(input_string)
        supervisor_name_match = supervisor_name_pattern.search(input_string)
        designation_match = designation_pattern.search(input_string)
        email_match = email_pattern.search(input_string)
        mobile_match = mobile_pattern.search(input_string)

        # Extract information
        project_name = project_name_match.group(1) if project_name_match else None
        summary = summary_match.group(1) if summary_match else None
        work_station = work_station_match.group(1) if work_station_match else None
        project_location = project_location_match.group(1) if project_location_match else None
        supervisor_name = supervisor_name_match.group(1) if supervisor_name_match else None
        designation = designation_match.group(1) if designation_match else None
        email = email_match.group(1) if email_match else None
        mobile = mobile_match.group(1) if mobile_match else None

        
        data = {
            "project_name": project_name,
            "summary": summary,
            "work_station": work_station,
            "supervisor_name": supervisor_name,
            "project_location": project_location,
            "designation": designation,
            "email": email, 
            "mobile": mobile,
        }

        return data 
        


def home(request):
    return render(request, "home.html")


def experience(request):
    experiences = Experience.objects.all()
    
    for experience in experiences:
        experience.achievement = experience.achievement.split("*")[1:]
        experience.responsibilities = experience.responsibilities.split("*")[1:]
        experience.skills = experience.skills.split("*")[1:]
        experience.training = experience.training.split("*")[1:]
        experience.knowledge = experience.knowledge.split("*")[1:]
        experience.project_info = getProjectInfo(experience.project_info)
        experience.organization_info = getOrgInfo(experience.organization_info)
        
    return render(request, "experience.html", {'experiences': experiences})


def education(request):
    educations = Education.objects.all()
    return render(request, "education.html", {'educations': educations})


def extra_curricular(request):
    extra_curricular = ExtraCurricular.objects.all()
    return render(request, "extra_curricular.html", {'extra_curricular': extra_curricular})


def org_affiliation(request):
    affiliations = OrganizationalAffiliation.objects.all()
    return render(request, "org_affiliation.html", {'affiliations': affiliations})


def participation(request):
    participations = Participation.objects.all()
    return render(request, "participation.html", {'participations': participations})


def portfolio(request):
    portfolios = Portfolio.objects.all()
    return render(request, "portfolio.html", {'portfolios':portfolios})


def reference(request):
    reference_list = Reference.objects.all()
    return render(request, "reference.html", {'reference_list': reference_list})


def skills(request):
    areas_of_expertise = AreaOfExpertise.objects.all()
    software_skills = SoftwareSkill.objects.all()
    language_skills = LanguageSkill.objects.all()
    return render(request, "skills.html", {'areas_of_expertise': areas_of_expertise, 'software_skills': software_skills, 'language_skills': language_skills})


def training(request):

    training_sections = TrainingSection.objects.all() 
    sections_with_subsection = []


    trainings = Training.objects.all()


    for section in training_sections:
        subsections = TrainingSubSection.objects.filter(training_section=section)
        sections_with_subsection.append({'section': section, 'subsections': subsections})

        section_filter = request.GET.get(f'{section.title}')
        print(section_filter)
        if section_filter:
            for subsection in subsections:
                if subsection.title == section_filter:
                    trainings = trainings.filter(subsection=subsection)
           


    institutes = [training.institutes_instructor for training in trainings]
    institutes = set(institutes)

    years = [training.completion_year for training in trainings]
    years = sorted(set(years))
    

    mediums = [training.medium for training in trainings if training.medium is not None ]
    mediums = set(mediums)

    year_filter = request.GET.get('year')
    institute_filter = request.GET.get('institute')
    medium_filter = request.GET.get('medium')
    

    if institute_filter:
        trainings = trainings.filter(institutes_instructor=institute_filter)
    if year_filter:
        trainings = trainings.filter(completion_year=year_filter)  

    if medium_filter:
        trainings = trainings.filter(medium=medium_filter)


    return render(request, "training.html", {
        'trainings': trainings, 
        'institutes': institutes, 
        'years': years, 
        'sections_with_subsections': sections_with_subsection,
        'mediums': mediums  
        })
