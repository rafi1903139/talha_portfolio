from django.db import models

# Create your models here.


class Experience(models.Model):
    company_logo = models.ImageField(upload_to="company_logos/", blank=True, null=True)
    job_position = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    starting_date = models.DateField()
    duration = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    achievement = models.TextField()
    responsibilities = models.TextField()
    organization_info = models.TextField()
    project_info = models.TextField(blank=True, null=True)
    skills = models.TextField()
    training = models.TextField()
    knowledge = models.TextField()

    def __str__(self):
        return self.organization


class Participation(models.Model):
    title = models.CharField(max_length=200)
    event_type = models.CharField(max_length=100)
    purpose = models.TextField()
    organized_by = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.title


class OrganizationalAffiliation(models.Model):
    name = models.CharField(max_length=200)
    org_type = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    identification = models.CharField(max_length=50)
    period = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Education(models.Model):
    degree = models.CharField(max_length=200)
    concentration = models.CharField(max_length=100)
    institute = models.CharField(max_length=200)
    result = models.CharField(max_length=50)
    passing_year = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.degree} - {self.institute} ({self.passing_year})"


class TrainingSection(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class TrainingSubSection(models.Model):
    title = models.CharField(max_length=255)
    training_section = models.ForeignKey(TrainingSection, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Training(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    institutes_instructor = models.CharField(max_length=100)
    location_platform = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    completion_year = models.IntegerField()
    subsection = models.ForeignKey(
        TrainingSubSection, on_delete=models.CASCADE, null=True, blank=True
    )
    medium = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    work_type = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    published_on = models.DateField()
    published_by = models.CharField(max_length=100)
    external_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class ExtraCurricular(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, null=True, blank=True)
    organization = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    year = models.CharField(max_length=100)

    def __str__(self):
        return self.title


# define areas of experties
class AreaOfExpertise(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class ExpertiseItem(models.Model):
    area_of_expertise = models.ForeignKey(
        AreaOfExpertise, on_delete=models.CASCADE, related_name="expertise_items"
    )
    item_name = models.CharField(max_length=100)

    def __str__(self):
        return self.item_name


class SoftwareSkill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SoftwareName(models.Model):
    software_skill = models.ForeignKey(
        SoftwareSkill, on_delete=models.CASCADE, related_name="software_names"
    )
    name = models.CharField(max_length=200)
    working_knowledge = models.TextField(null=True)

    def __str__(self):
        return self.name


class LanguageSkill(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Reference(models.Model):
    reference_img = models.ImageField(upload_to="ref_img/", blank=True, null=True)
    refrence_type = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    organization_name = models.CharField(max_length=200)
    designation = models.CharField(max_length=100)
    address = models.TextField()
    contact_no = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name
