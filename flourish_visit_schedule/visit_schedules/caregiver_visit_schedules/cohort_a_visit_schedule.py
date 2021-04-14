from edc_visit_schedule import VisitSchedule, site_visit_schedules

from ..schedules import a_enrollment1_schedule_1, a_birth1_schedule_1, a_quarterly1_schedule_1
from ..schedules import a_dyad1_schedule_1
from ..schedules import a_enrollment2_schedule_1, a_birth2_schedule_1, a_quarterly2_schedule_1
from ..schedules import a_dyad2_schedule_1
from ..schedules import a_enrollment3_schedule_1, a_birth3_schedule_1, a_quarterly3_schedule_1
from ..schedules import a_dyad3_schedule_1

# Cohort A Visit Schedules
cohort_a1_visit_schedule_v1 = VisitSchedule(
    name='a1_visit_schedule1',
    verbose_name='Cohort A Visit Schedule 1',
    offstudy_model='flourish_prn.caregiveroffstudy',
    death_report_model='flourish_prn.deathreport',
    locator_model='',
    previous_visit_schedule=None)

cohort_a1_visit_schedule_v1.add_schedule(a_enrollment1_schedule_1)
cohort_a1_visit_schedule_v1.add_schedule(a_birth1_schedule_1)
cohort_a1_visit_schedule_v1.add_schedule(a_quarterly1_schedule_1)
cohort_a1_visit_schedule_v1.add_schedule(a_dyad1_schedule_1)

cohort_a2_visit_schedule_v1 = VisitSchedule(
    name='a2_visit_schedule1',
    verbose_name='Cohort A2 Visit2 Schedule 1',
    offstudy_model='flourish_prn.caregiveroffstudy',
    death_report_model='flourish_prn.deathreport',
    locator_model='',
    previous_visit_schedule=None)

cohort_a2_visit_schedule_v1.add_schedule(a_enrollment2_schedule_1)
cohort_a2_visit_schedule_v1.add_schedule(a_birth2_schedule_1)
cohort_a2_visit_schedule_v1.add_schedule(a_quarterly2_schedule_1)
cohort_a2_visit_schedule_v1.add_schedule(a_dyad2_schedule_1)

cohort_a3_visit_schedule_v1 = VisitSchedule(
    name='a3_visit_schedule1',
    verbose_name='Cohort A3 Visit Schedule 1',
    offstudy_model='flourish_prn.caregiveroffstudy',
    death_report_model='flourish_prn.deathreport',
    locator_model='',
    previous_visit_schedule=None)

cohort_a3_visit_schedule_v1.add_schedule(a_enrollment3_schedule_1)
cohort_a3_visit_schedule_v1.add_schedule(a_birth3_schedule_1)
cohort_a3_visit_schedule_v1.add_schedule(a_quarterly3_schedule_1)
cohort_a3_visit_schedule_v1.add_schedule(a_dyad3_schedule_1)

# Registering Visit Schedules
site_visit_schedules.register(cohort_a1_visit_schedule_v1)
site_visit_schedules.register(cohort_a2_visit_schedule_v1)
site_visit_schedules.register(cohort_a3_visit_schedule_v1)