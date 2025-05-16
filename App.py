<!DOCTYPE html>
<html>
<head>
  <title>Student Manager</title>
  <style>
    body { font-family: Arial; margin: 20px; }
    input, button { padding: 8px; margin: 5px; }
    .student-list { margin-top: 20px; }
    .student-item { margin: 5px 0; }
    .delete-button {
      margin-left: 10px;
      color: red;
      border: none;
      background: none;
      cursor: pointer;
      font-weight: bold;
    }
  </style>
</head>
<body>
  <h2>Student Manager</h2>
  <input id="name" placeholder="Enter student name">
  <input id="marks" placeholder="Enter marks" type="number">
  <button onclick="addStudent()">Add Student</button>

  <div class="student-list" id="studentList"></div>

  <script>
    const studentList = [];

    function addStudent() {
      const name = document.getElementById("name").value.trim();
      const marks = document.getElementById("marks").value.trim();
      if (name && marks) {
        studentList.push({ name, marks });
        displayStudents();
        document.getElementById("name").value = "";
        document.getElementById("marks").value = "";
      }
    }

    function deleteStudent(index) {
      studentList.splice(index, 1);
      displayStudents();
    }

    function displayStudents() {
      const list = document.getElementById("studentList");
      list.innerHTML = "";
      studentList.forEach((s, i) => {
        const studentItem = document.createElement("div");
        studentItem.className = "student-item";
        studentItem.innerHTML = `
          ${i + 1}. ${s.name} - ${s.marks}
          <button class="delete-button" onclick="deleteStudent(${i})">Delete</button>
        `;
        list.appendChild(studentItem);
      });
    }
  </script>
</body>
</html>
