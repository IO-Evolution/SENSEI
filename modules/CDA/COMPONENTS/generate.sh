#!/bin/bash

# Lista di nomi di classe
class_names=("Component" "BL_Boolean" "II_InstanceIdentifier" "ED_EncapsulatedData" "ST_String" "CD_ConceptDescriptor" "CE_CodedWithEquivalents" "CV_CodedValue" "CS_CodedSimpleValue" "TEL_TelecomincationAddress" "AD_PostalAddress" "PN_PersonName" "ON_OrganisationName" "INT_IntegerNumber" "PQ_PhysicalQuantities" "TS_PointInTime" "IVL_TS_IntervalOfTime" "IVL_PQ_IntervalOfPhysicalQuantities" "RTO_QTY_QTY_RatioOfQuantities" "ClinicalDocument" "InfrastructureRootTypeId" "RecordTarget" "PatientRole" "Patient" "DocumentRoot" "Guardian" "Person" "Organization" "OrganizationPartOf" "BirthPlace" "Place" "LanguageCommunication" "Author" "AssignedAuthor" "AuthoringDevice" "MaintainedEntity" "DataEnterer" "AssignedEntity" "Informant12" "RelatedEntity" "Custodian" "AssignedCustodian" "CustodianOrganization" "InformationRecipient" "IntendedRecipient" "LegalAuthenticator" "Authenticator" "Participant1" "AssociatedEntity" "InFulfillmentOf" "Order" "DocumentationOf" "ServiceEvent" "Performer1" "RelatedDocument" "ParentDocument" "Authorization" "Consent" "Component1" "EncompassingEncounter" "ResponsibleParty" "EncounterParticipant" "Location" "HealthCareFacility" "Component2" "NonXMLBody" "StructuredBody" "Component3" "Section" "Subject" "RelatedSubject" "SubjectPerson" "Entry" "Act" "Specimen" "SpecimenRole" "PlayingEntity" "Performer2" "Participant2" "ParticipantRole" "Device" "Entity" "EntryRelationship" "Encounter" "Reference" "ExternalAct" "ExternalObservation" "ExternalProcedure" "ExternalDocument" "Precondition" "Criterion" "Observation" "ReferenceRange" "ObservationRange" "ObservationMedia" "Organizer" "Component4" "Procedure" "RegionOfInterest" "RegionOfInterestValue" "SubstanceAdministration" "Consumable" "ManufacturedProduct" "LabeledDrug" "Material" "Supply" "Product" "Component5")

# Contenuto del template per le classi
template_content='from STRUCTURE_UTILS.exceptions import InvalidGivenValue
import STRUCTURE_UTILS.elements as Element
import STRUCTURE_UTILS.Component as Component

class %s(Component):
    def __init__(self, name: str, data: dict):
        pass

    @classmethod
    def as_dict(cls):
        return {}'

# Loop per creare i file per ciascuna classe
for class_name in "${class_names[@]}"; do
    # Costruzione del nome del file
    file_name="${class_name}.py"

    # Creazione del file con il contenuto del template
    printf "$template_content" "$class_name" > "$file_name"

    echo "Creato il file $file_name"
done

echo "Generazione completata!"
