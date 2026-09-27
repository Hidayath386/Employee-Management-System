let employees = [];

// Add Employee
document
  .getElementById("employeeForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    let employeeId = document.getElementById("employeeId").value;

    let employeeName = document.getElementById("employeeName").value;

    let salary = Number(document.getElementById("salary").value);

    let bonus = Number(document.getElementById("bonus").value);

    let employee = {
      employeeId: employeeId,
      name: employeeName,
      salary: salary,
      bonus: bonus,
    };

    employees.push(employee);

    alert("Employee added successfully!");

    document.getElementById("employeeForm").reset();

    displayEmployees();
  });

// Display Employees
function displayEmployees() {
  let table = document.getElementById("employeeTable");

  table.innerHTML = "";

  employees.forEach(function (employee) {
    let totalSalary = employee.salary + employee.bonus;

    let row = `
            <tr>

                <td>${employee.employeeId}</td>

                <td>${employee.name}</td>

                <td>₹${employee.salary}</td>

                <td>₹${employee.bonus}</td>

                <td>₹${totalSalary}</td>

                <td>
                    <button
                        onclick="deleteEmployee('${employee.employeeId}')">
                        Delete
                    </button>
                </td>

            </tr>
        `;

    table.innerHTML += row;
  });
}

// Search Employee
function searchEmployee() {
  let searchId = document.getElementById("searchId").value;

  let employee = employees.find(function (employee) {
    return employee.employeeId === searchId;
  });

  let result = document.getElementById("searchResult");

  if (employee) {
    let totalSalary = employee.salary + employee.bonus;

    result.innerHTML = `
            <h3>Employee Found</h3>

            <p>
                <strong>ID:</strong>
                ${employee.employeeId}
            </p>

            <p>
                <strong>Name:</strong>
                ${employee.name}
            </p>

            <p>
                <strong>Salary:</strong>
                ₹${employee.salary}
            </p>

            <p>
                <strong>Bonus:</strong>
                ₹${employee.bonus}
            </p>

            <p>
                <strong>Total Salary:</strong>
                ₹${totalSalary}
            </p>
        `;
  } else {
    result.innerHTML = "<p>Employee not found.</p>";
  }
}

// Delete Employee
function deleteEmployee(employeeId) {
  employees = employees.filter(function (employee) {
    return employee.employeeId !== employeeId;
  });

  alert("Employee deleted successfully!");

  displayEmployees();
}
