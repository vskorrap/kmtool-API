from django.core.validators import validate_comma_separated_integer_list
from django.db import models
from datetime import date


class AllocationTypes(models.Model):
    allocationType = models.CharField(max_length=25, unique=True)


class Teams(models.Model):
    teamName = models.CharField(max_length=10, unique=True)
    region = models.BooleanField(default=True)


class Countries(models.Model):
    country = models.CharField(max_length=100, unique=True)
    abbrev = models.CharField(max_length=4, unique=True)
    hexRegion = models.ForeignKey(Teams, on_delete=models.DO_NOTHING)


class Disciplines(models.Model):
    discipline = models.CharField(max_length=100, unique=True)


class Roles(models.Model):
    role = models.CharField(max_length=255, unique=True)


class StatusTypes(models.Model):
    statusType = models.CharField(max_length=100, unique=True)
    activeType = models.BooleanField(default=True)


class Locations(models.Model):
    location = models.CharField(max_length=100, unique=True)
    abbrev = models.CharField(max_length=4, unique=True)
    country = models.ForeignKey(Countries, on_delete=models.DO_NOTHING)


class Resources(models.Model):
    firstName = models.CharField(max_length=100)
    surName = models.CharField(max_length=100)
    country = models.ForeignKey(Countries, on_delete=models.DO_NOTHING)
    discipline = models.ForeignKey(Disciplines, on_delete=models.DO_NOTHING)
    statusType = models.ForeignKey(StatusTypes, on_delete=models.DO_NOTHING)
    allocationType = models.ForeignKey(AllocationTypes, on_delete=models.DO_NOTHING)
    minUtilization = models.FloatField()
    maxUtilization = models.FloatField()
    inactiveDate = models.DateField(blank=True, null=True)
    activeDate = models.DateField(blank=True, null=True)
    role = models.ForeignKey(Roles, on_delete=models.DO_NOTHING)
    team = models.ForeignKey(Teams, on_delete=models.DO_NOTHING)
    # location = models.ForeignKey(Locations, on_delete=models.DO_NOTHING)

    class Meta:
        managed = True
        unique_together = ('firstName', 'surName')


class ProjectStatusCategoryTypes(models.Model):
    statusCategory = models.CharField(max_length=100, unique=True)
    statusCategoryId = models.SmallIntegerField()
    show = models.BooleanField(default=False)


class ProjectStatusTypes(models.Model):
    projectStatus = models.CharField(max_length=100, unique=True)
    activeType = models.BooleanField(default=True)
    category = models.SmallIntegerField()
    sort = models.SmallIntegerField()
    show = models.BooleanField(default=False)


class Customers(models.Model):
    customer = models.CharField(max_length=100,unique=True)
    abbrev = models.CharField(max_length=20, unique=True)
    SFDCID = models.CharField(max_length=100,blank=True,null=True)
    status = models.ForeignKey(StatusTypes,on_delete=models.DO_NOTHING)


class ProjectChargeTypes(models.Model):
    charge=models.CharField(max_length=25)


class Projects(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.DO_NOTHING,null=True,blank=True)  # Field name made lowercase.
    projectName = models.CharField(max_length=100)
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)
    product=models.ForeignKey(Disciplines, on_delete=models.DO_NOTHING,null=True,blank=True)
    status = models.IntegerField(blank=True, null=True)
    defAllocation = models.FloatField(default=1)
    chargeable = models.ForeignKey(ProjectChargeTypes, on_delete=models.DO_NOTHING,null=True,blank=True)
    sfdcOppName = models.CharField(max_length=255, blank=True, null=True)
    country = models.ForeignKey(Countries, on_delete=models.DO_NOTHING,null=True,blank=True)
    projectStatus = models.ForeignKey(ProjectStatusTypes, on_delete=models.DO_NOTHING)
    adminUse = models.BooleanField(default=False)
    sfdcId = models.CharField(max_length=100, blank=True, null=True)
    weeksDuration = models.IntegerField(blank=True, null=True)
    probability = models.FloatField(default=100,blank=True,null=True)
    docType = models.CharField(max_length=10, blank=True, null=True)
    adminLock = models.BooleanField(default=False)
    createdDate=models.DateField()
    budgetHours = models.FloatField(null=True,blank=True)
    projectManager=models.ForeignKey(Resources,null=True,blank=True,on_delete=models.DO_NOTHING)
    # Region = models.ForeignKey(Teams, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ('projectName', 'customer', 'projectStatus')


class ProductSkills(models.Model):
    productSkill = models.CharField(max_length=100, unique=True)
    discipline = models.ForeignKey(Disciplines, on_delete=models.DO_NOTHING)


class ResourceProductSkills(models.Model):
    resource = models.ForeignKey(Resources, on_delete=models.DO_NOTHING)
    productSkill = models.ForeignKey(ProductSkills, on_delete=models.DO_NOTHING)
    lastUsed = models.DateField(blank=True, null=True)
    noOfYears = models.IntegerField()
    startDate = models.DateField(blank=True, null=True)

    class Meta:
        unique_together = ('resource', 'productSkill')


class TechnicalGroup(models.Model):
    technicalGroup = models.CharField(max_length=100, unique=True)


class TechnicalSkills(models.Model):
    technicalSkill = models.CharField(max_length=100, unique=True)
    technicalGroup = models.ForeignKey(TechnicalGroup, on_delete=models.DO_NOTHING)


class ResourceTechnicalSkills(models.Model):
    resource = models.ForeignKey(Resources, on_delete=models.DO_NOTHING,)
    technicalSkill = models.ForeignKey(TechnicalSkills, on_delete=models.DO_NOTHING)
    lastUsed = models.DateField(blank=True, null=True)
    noOfYears = models.IntegerField()
    startDate = models.DateField(blank=True, null=True)

    class Meta:
        unique_together = ('resource', 'technicalSkill')


class ResourceExperience(models.Model):
    resource = models.ForeignKey(Resources, on_delete=models.DO_NOTHING,unique=True)
    yearOfJoiningInIndustry = models.IntegerField()
    yearOfJoiningInHexagon = models.IntegerField()
    willingToTravel = models.BooleanField(default=True)
    experienceSummary = models.TextField()


class TrainingType(models.Model):
    trainingType = models.CharField(unique=True, max_length=50)


class ResourceTrainings(models.Model):
    resource = models.ForeignKey(Resources, on_delete=models.DO_NOTHING)
    trainingName = models.CharField(max_length=255)
    trainingType = models.CharField(max_length=255)
    startDate = models.DateField(null=True, blank=True)
    endDate = models.DateField(null=True, blank=True)
    comments = models.TextField(blank=True, null=True)


class ResourceProjects(models.Model):
    resource = models.ForeignKey(Resources, on_delete=models.DO_NOTHING)
    projectName = models.CharField(max_length=255)
    summary = models.CharField(max_length=255, blank=True, null=True)
    client = models.CharField(max_length=255)
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)
    productSkills = models.CharField(max_length=4000, blank=True, null=True)
    technicalSkills = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        unique_together = ('resource', 'projectName')


class ProjectDemand(models.Model):
    project = models.ForeignKey(Projects,on_delete=models.DO_NOTHING)
    discipline = models.ForeignKey(Disciplines,on_delete=models.DO_NOTHING,blank=True, null=True)
    productSkills = models.CharField(validators=[validate_comma_separated_integer_list],max_length=3500, blank=True, null=True)
    technicalSkills = models.CharField(validators=[validate_comma_separated_integer_list],max_length=3500, blank=True, null=True)
    ftes = models.FloatField()
    startDate=models.DateField()
    endDate=models.DateField()
    team=models.ForeignKey(Teams,on_delete=models.DO_NOTHING)
    Version = models.IntegerField(default=1)


class SupportType(models.Model):
    support=models.CharField(max_length=20)

    def __str__(self):
        return self.support


class ResourcePlanning(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.DO_NOTHING)
    resource = models.ForeignKey(Resources, on_delete=models.DO_NOTHING)
    role = models.ForeignKey(Roles, on_delete=models.DO_NOTHING)
    discipline = models.ForeignKey(Disciplines, on_delete=models.DO_NOTHING)
    chargeTo=models.ForeignKey(ProjectChargeTypes,on_delete=models.DO_NOTHING)
    support = models.ForeignKey(SupportType, on_delete=models.DO_NOTHING)
    crossCharging = models.BooleanField()
    onSite = models.BooleanField(default=True)
    startDate=models.DateField()
    endDate=models.DateField()
    percentage=models.FloatField()
