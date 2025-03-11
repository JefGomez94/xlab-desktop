import { useState } from "react";
import { Dropdown, Checkbox, Label, Radio } from "flowbite-react";
import { HiChevronDown } from "react-icons/hi";

const MultiSelectDropdown = ({ options, label = "Seleccionar", multiple = true, onSelect }) => {
    const [selectedItems, setSelectedItems] = useState(multiple ? [] : "");

    const handleSelectionChange = (type) => {
        let newSelection;
        if (multiple) {
            newSelection = selectedItems.includes(type)
                ? selectedItems.filter((item) => item !== type)
                : [...selectedItems, type];
        } else {
            newSelection = type;
        }

        setSelectedItems(newSelection);
        onSelect(newSelection); // ⬅️ Actualiza el estado en el padre
    };

    return (
        <Dropdown
            dismissOnClick={false}
            renderTrigger={() => (
                <button className="flex px-4 py-2 bg-gray-50 border border-gray-300 text-gray-700 rounded-md text-left">
                    <span>
                        {multiple
                            ? selectedItems.length > 0
                                ? selectedItems.join(", ")
                                : label
                            : selectedItems || label}
                    </span>
                    <HiChevronDown className="w-5 h-5 text-gray-600" />
                </button>
            )}
        >
            <div className="p-2 w-48 bg-white border border-gray-300 rounded-md shadow-lg">
                {options.map((type) => (
                    <div key={type} className="flex items-center gap-2 mb-1">
                        {multiple ? (
                            <Checkbox
                                id={type}
                                checked={selectedItems.includes(type)}
                                onChange={() => handleSelectionChange(type)}
                            />
                        ) : (
                            <Radio
                                id={type}
                                name="dropdown-selection"
                                checked={selectedItems === type}
                                onChange={() => handleSelectionChange(type)}
                            />
                        )}
                        <Label htmlFor={type} className="text-gray-900">{type}</Label>
                    </div>
                ))}
            </div>
        </Dropdown>
    );
};

export default MultiSelectDropdown;