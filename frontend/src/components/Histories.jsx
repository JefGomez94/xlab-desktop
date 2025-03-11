import { Button, Dropdown, Card, Checkbox, Label, TextInput } from "flowbite-react";
import { useState } from "react";
import MultiSelectDropdown from "./MultiSelectDropdown";

export function Histories() {
    const [patientId, setpatientId] = useState("")
    const [patientTypeid, setpatientTypeid] = useState("")
    const [patientSex, setpatientSex] = useState("")
    const [patientBirth, setpatientBirth] = useState("")
    const [patientAp1, setpatientAp1] = useState("")
    const [patientAp2, setpatientAp2] = useState("")
    const [patientName, setpatientName] = useState("")
    const [patientDir, setpatientDir] = useState("")
    const [patientTel, setpatientTel] = useState("")
    const [patientMail, setpatientMail] = useState("")
    const [patientNote, setpatientNote] = useState("")
    const options = ["CC", "CE", "RC", "NUI", "TI", "PAS", "NIT"];

    const handleCheckboxChange = (type) => {
        setSelectedItems((prev) =>
            prev.includes(type) ? prev.filter((item) => item !== type) : [...prev, type]
        );
    };
    return (
        <div>

            <div className="flex items-center space-x-2 border-gray-300">
                <Label htmlFor="patientId" value="Ident/Historia" className="text-gray-700" />
                <TextInput
                    id="patientId"
                    type="text"
                    value={patientId}
                    onChange={(e) => setpatientId(e.target.value)}
                    required
                //className="w-32 h-8"               
                />
            </div>

            <div className="flex items-center space-x-2">
                <Label htmlFor="patientId" value="Tipo doc" className="text-gray-700" />

                {/* DROPDOWN MODIFICADO */}
                <MultiSelectDropdown options={options} label="" multiple={false} onSelect={setpatientTypeid} />

            </div>

            <div className="flex items-center space-x-2 w-64 h-16">
                <Label htmlFor="patientSex" value="Sexo" className="text-gray-700" />
                <TextInput
                    id="patientSex"
                    type="text"
                    value={patientSex}
                    onChange={(e) => setpatientSex(e.target.value)}
                    required
                    className="w-32 h-8" />
            </div>

            <div className="flex items-center space-x-2 w-64 h-16">
                <Label htmlFor="patientBirth" value="Fecha Nacimiento" className="text-gray-700" />
                <TextInput
                    id="patientBirth"
                    type="text"
                    value={patientBirth}
                    onChange={(e) => setpatientBirth(e.target.value)}
                    required
                    className="w-32 h-8" />
            </div>

            <div className="flex items-center space-x-2 w-64 h-16">
                <Label htmlFor="patientAp1" value="Apellido 1" className="text-gray-700" />
                <TextInput
                    id="patientAp1"
                    type="text"
                    value={patientAp1}
                    onChange={(e) => setpatientAp1(e.target.value)}
                    required
                    className="w-32 h-8" />
            </div>

            <div className="flex items-center space-x-2 w-64 h-16">
                <Label htmlFor="patientAp1" value="Apellido 2" className="text-gray-700" />
                <TextInput
                    id="patientAp2"
                    type="text"
                    value={patientAp2}
                    onChange={(e) => setpatientAp2(e.target.value)}
                    required
                    className="w-32 h-8" />
            </div>

            <div className="flex items-center space-x-2 w-64 h-16">
                <Label htmlFor="patientName" value="Nombres" className="text-gray-700" />
                <TextInput
                    id="patientName"
                    type="text"
                    value={patientName}
                    onChange={(e) => setpatientName(e.target.value)}
                    required
                    className="w-32 h-8" />
            </div>

            <div className="flex items-center space-x-2 w-64 h-16">
                <Label htmlFor="patientDir" value="Direccion" className="text-gray-700" />
                <TextInput
                    id="patientDir"
                    type="text"
                    value={patientDir}
                    onChange={(e) => setpatientDir(e.target.value)}
                    required
                    className="w-32 h-8" />
            </div>

            <div className="flex items-center space-x-2 w-64 h-16">
                <Label htmlFor="patientTel" value="Teléfonos" className="text-gray-700" />
                <TextInput
                    id="patientTel"
                    type="text"
                    value={patientTel}
                    onChange={(e) => setpatientTel(e.target.value)}
                    required
                    className="w-32 h-8" />
            </div>

            <div className="flex items-center space-x-2 w-64 h-16">
                <Label htmlFor="patientMail" value="e-mail" className="text-gray-700" />
                <TextInput
                    id="patientMail"
                    type="text"
                    value={patientMail}
                    onChange={(e) => setpatientMail(e.target.value)}
                    required
                    className="w-32 h-8" />
            </div>

            <div className="flex items-center space-x-2 w-64 h-16">
                <Label htmlFor="patientNote" value="Notas Paciente" className="text-gray-700" />
                <TextInput
                    id="patientNote"
                    type="text"
                    value={patientNote}
                    onChange={(e) => setpatientNote(e.target.value)}
                    required
                    className="w-32 h-8"
                />
            </div>
        </div>
    )
}