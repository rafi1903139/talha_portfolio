from django.shortcuts import render
from planner.models import AreaOfExpertise, ExtraCurricular, Education, LanguageSkill, OrganizationalAffiliation, Participation, Portfolio, Reference, SoftwareSkill, Training, Experience, TrainingSection, TrainingSubSection

# Create your views here.


def home(request):
    return render(request, "home.html")


def experience(request):
    experiences = Experience.objects.all()
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
        if section_filter:
            for subsection in subsections:
                if subsection.title == section_filter:
                    trainings = trainings.filter(subsection=subsection)
           


    institutes = [training.institutes_instructor for training in trainings]
    institutes = set(institutes)

    years = [training.completion_year for training in trainings]
    years = set(years)

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
