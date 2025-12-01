let contactos = [];

document.getElementById("btnGuardar").addEventListener("click", function () {
    const nombre = document.getElementById("nombre").value;
    const telefono = document.getElementById("telefono").value;
    const correo = document.getElementById("correo").value;
    const editIndex = document.getElementById("editIndex").value;

    if (editIndex === "") {
        // Crear
        contactos.push({ nombre, telefono, correo });
    } else {
        // Actualizar
        contactos[editIndex] = { nombre, telefono, correo };
        document.getElementById("editIndex").value = "";
    }

    mostrarContactos();
    limpiarFormulario();
});

function mostrarContactos() {
    const tbody = document.getElementById("contactosBody");
    tbody.innerHTML = "";

    contactos.forEach((c, index) => {
        const fila = `
            <tr>
                <td>${c.nombre}</td>
                <td>${c.telefono}</td>
                <td>${c.correo}</td>
                <td>
                    <button onclick="editarContacto(${index})">Editar</button>
                    <button onclick="eliminarContacto(${index})">Eliminar</button>
                </td>
            </tr>
        `;
        tbody.innerHTML += fila;
    });
}

function editarContacto(i) {
    const c = contactos[i];
    document.getElementById("nombre").value = c.nombre;
    document.getElementById("telefono").value = c.telefono;
    document.getElementById("correo").value = c.correo;
    document.getElementById("editIndex").value = i;
}

function eliminarContacto(i) {
    contactos.splice(i, 1);
    mostrarContactos();
}

function limpiarFormulario() {
    document.getElementById("nombre").value = "";
    document.getElementById("telefono").value = "";
    document.getElementById("correo").value = "";
}
