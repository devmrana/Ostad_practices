-- Create Doctors Table
CREATE TABLE Doctors (
    DoctorID INT PRIMARY KEY,
    Name VARCHAR(100),
    Specialization VARCHAR(50),
    Phone VARCHAR(15)
);

-- Create Patients Table
CREATE TABLE Patients (
    PatientID INT PRIMARY KEY,
    Name VARCHAR(100),
    Age INT,
    Gender VARCHAR(10),
    Phone VARCHAR(15)
);

-- Create Departments Table
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    Name VARCHAR(100),
    Location VARCHAR(100)
);

-- Create Appointments Table
CREATE TABLE Appointments (
    AppointmentID INT PRIMARY KEY,
    Date DATE,
    Time TIME,
    Status VARCHAR(50),
    DoctorID INT,
    PatientID INT,
    DepartmentID INT,
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID),
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

-- Insert Dummy Data into Doctors --
INSERT INTO Doctors (DoctorID, Name, Specialization, Phone) VALUES
(1, 'Dr. John Smith', 'Cardiology', '555-1234'),
(2, 'Dr. Emily Davis', 'Orthopedics', '555-5678'),
(3, 'Dr. Robert Johnson', 'Neurology', '555-9876'),
(4, 'Dr. Lisa Brown', 'Pediatrics', '555-6543'),
(5, 'Dr. Michael Green', 'Dermatology', '555-3456');

-- Insert Dummy Data into Patients --
INSERT INTO Patients (PatientID, Name, Age, Gender, Phone) VALUES
(1, 'Alice Walker', 30, 'Female', '555-1111'),
(2, 'James Miller', 45, 'Male', '555-2222'),
(3, 'Sophia Wilson', 60, 'Female', '555-3333'),
(4, 'David Moore', 35, 'Male', '555-4444'),
(5, 'Olivia Taylor', 25, 'Female', '555-5555');

-- Insert Dummy Data into Departments --
INSERT INTO Departments (DepartmentID, Name, Location) VALUES
(1, 'Cardiology', 'Building A, Floor 2'),
(2, 'Orthopedics', 'Building B, Floor 1'),
(3, 'Neurology', 'Building A, Floor 3'),
(4, 'Pediatrics', 'Building C, Floor 1'),
(5, 'Dermatology', 'Building D, Floor 4');

-- Insert Dummy Data into Appointments --
INSERT INTO Appointments (AppointmentID, Date, Time, Status, DoctorID, PatientID, DepartmentID) VALUES
(1, '2024-12-20', '09:00:00', 'Scheduled', 1, 1, 1),
(2, '2024-12-20', '10:00:00', 'Scheduled', 2, 2, 2),
(3, '2024-12-21', '11:00:00', 'Scheduled', 3, 3, 3),
(4, '2024-12-21', '14:00:00', 'Scheduled', 4, 4, 4),
(5, '2024-12-22', '15:00:00', 'Scheduled', 5, 5, 5);
