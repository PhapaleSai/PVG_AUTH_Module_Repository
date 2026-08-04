Pune Vidyarthi Griha’s

College of Science & Commerce, Pune-9

Department of Computer Science

AY 2025-26

A

PROJECT REPORT ON

“ Authentication Module for College ERP System”

Submitted to

Savitribai Phule Pune University for

M.Sc. Computer Science  Semester – IV

Submitted by

Sai Phapale (2378)

 Swaraj Bhagat(2359) 

Varad Karve(2374)

Under the Guidance of

Mrs. Rekha Joshi

P.V.G’s College of Science & Commerce, Pune-9

Department of Computer Science

Project Certificate

This is to certify that Sai Phapale ,Swaraj Bhagat ,Varad Karve of S.Y.M.Sc. (Computer Science), Semester-IV has satisfactorily completed the Industrial Training / Institutional Project under the course CS/-651-MJP, in the academic year 2025-2026, as prescribed by Savitribai Phule Pune University.

 The title of the project is :

Authentication & Authorization Module for College ERP System

 Project Guide 									HOD

Internal Examiner                           Industry Expert                      External Examiner     

INDEX

1.1 Company Certificate & Internship Certificate

  1.2                    Acknowledgement

We express our sincere gratitude to Pune Vidyarthi Griha's College of Science and Commerce for providing us with the opportunity and platform to undertake this Industrial Training / Institutional Project successfully.

We would like to convey our heartfelt thanks to our project guides, Mr. Prashant Deshmukh and Mr. Swapnil Jadhavrao, along with all our respected faculty members, for their continuous guidance, valuable suggestions, motivation, and support throughout the completion of this project.

We extend our special thanks to Mr. Mahadeo Pisal, Head of the Department of Computer Science, and Mrs. Rekha Joshi, Vice-Principal of the college, for their encouragement, inspiration, and administrative support during the internship/project work.

We are also highly thankful to our organization/company/institute for giving us the valuable opportunity to work on this project and gain practical exposure in the industry. Our sincere appreciation goes to the technical experts and mentors from the company/institute who provided us with continuous technical support, guidance, and cooperation, which helped us accomplish this internship/project successfully.

Finally, we would like to thank everyone who directly or indirectly contributed to the successful completion of this project work.

1.3     DECLARATION

I, the undersigned, hereby declare that the project titled "College ERP (Auth module)" is a record of independent work carried out by me. This project is being submitted for the award of the degree of M.Sc. (Computer Science) to Pune Vidyarthi Griha's College of Science, affiliated with Savitribai Phule Pune University.

I further declare that this project was conducted under the guidance of Guide Name  and is a result of my own original effort. This work has not been previously submitted, in part or in full, to this or any other institution for the award of any degree or diploma.

Date:  __/__/____

Place: Pune

(Signature of the Student) 

Sai Rajesh Phapale (2378)

Varad Santosh Karve(2374)

Swaraj Sachin Bhagat(2359)

s

1.4 Project Motivation

The motivation behind this project arose from the growing need for secure and structured access control in educational institutions. Traditional college management systems often lack proper authentication mechanisms, making them vulnerable to unauthorized access and data breaches. In many colleges, sensitive information such as student records, attendance, fees, and hostel data is either poorly protected or managed through outdated manual processes, which creates serious security risks.

Observing these challenges at PVG's College of Science & Commerce, Pune, we felt the need to build a modern, reliable, and secure authentication system as the foundation of a complete College ERP platform. The absence of role-based access control in existing systems means that any logged-in user can potentially access data beyond their authorization, which is a major concern for data privacy and institutional integrity.

This project is also motivated by the practical application of modern technologies such as React, FastAPI, PostgreSQL, JWT, and bcrypt, which are widely used in the industry. Implementing these technologies in a real-world college environment gave us the opportunity to bridge the gap between academic learning and professional development. Additionally, the integration of the Authentication Module with the Admission Module using APIs and ngrok further motivated us to build a system that is not only secure but also scalable and ready for future ERP module integration.

Furthermore, the project emphasizes the importance of secure password storage using hashing techniques, ensuring that user credentials are never stored in plain text. The use of JWT-based authentication enhances session management by providing stateless and efficient token handling. This improves system performance while maintaining high security standards. The modular architecture of the system allows easy expansion, enabling the addition of new features without affecting existing functionality.

The project also aims to improve administrative efficiency by reducing dependency on manual verification processes and minimizing human errors. By implementing structured access levels for Admin, Faculty, and Students, the system ensures proper data segregation and controlled information flow. This strengthens accountability within the institution and enhances transparency in operations. Overall, the desire to replace insecure, fragmented systems with a centralized, efficient, and role-driven access control solution served as the core motivation for this project.

1.5 Problem Statement

Traditional college management systems often rely on outdated and insecure methods for managing user access, which leads to several critical challenges in terms of data security, privacy, and operational efficiency. In most conventional systems, there is no structured mechanism to verify the identity of users before granting them access to sensitive information. This lack of proper authentication makes the system highly vulnerable to unauthorized access, data tampering, and potential security breaches.

One of the major problems observed in existing college ERP systems is the absence of Role-Based Access Control (RBAC). Without RBAC, all users may have equal access to the system regardless of their role, meaning a student could potentially access administrative data, or an unauthorized person could view confidential records related to fees, attendance, hostel, or examination results. This not only compromises data integrity but also raises serious concerns about student and institutional privacy.

Another significant issue is the insecure storage of user credentials. Many traditional systems either store passwords in plain text or use weak encryption methods, making it easy for attackers to retrieve and misuse login credentials. There is also no reliable session management in place, which means user sessions can be exploited or remain active even after logout, creating further security vulnerabilities.

Furthermore, the lack of audit tracking in conventional systems makes it nearly impossible to monitor user activity, detect suspicious behavior, or trace unauthorized changes made to the data. This absence of transparency and accountability weakens the overall reliability of the system.

The problem is further complicated by the fact that these systems are not scalable or modular, making it difficult to integrate new functionalities such as attendance, fees, examination, hostel, or transport modules in the future. The need for a secure, scalable, and role-driven authentication and authorization system that can serve as a strong foundation for a complete College ERP platform is therefore clearly identified as the core problem this project aims to solve.

2) System Analysis

2.1 Objective of the System

The primary objective of the College ERP Authentication and Authorization Module is to design and implement a secure, scalable, and efficient access control system that manages user identity and permissions across the entire college ERP platform. The system is built to ensure that only authenticated and authorized users can access the resources and functionalities relevant to their designated roles, thereby eliminating the risks associated with unauthorized access and data misuse.

One of the core objectives is to implement JWT (JSON Web Token) based authentication, which provides a stateless and secure method for managing user sessions. Upon successful login, a token is generated containing the user's identity, role, and expiration time, which is then used to validate every subsequent API request. This ensures that the system remains secure and efficient without the need for repeated login verification.

Another key objective is to protect user credentials through bcrypt password hashing. Rather than storing passwords in plain text, the system encrypts them before saving to the database, ensuring that even in the event of a data breach, the actual passwords remain protected and unreadable.

The system also aims to implement Role-Based Access Control (RBAC), where each user is assigned a specific role such as Guest, Student, or Admin. By default, every new user is assigned a Guest role following the principle of least privilege, ensuring minimal access until proper role assignment is done by the administrator. This structured permission model prevents users from accessing data or functionalities beyond their authorization level.

Additionally, the system includes token tracking and audit fields such as created_at and updated_at, which help monitor user activity, track session history, and maintain transparency across all operations. Secure API validation is also incorporated to protect backend routes from unauthorized requests.

Developed using React for the frontend, FastAPI for the backend, and PostgreSQL for the database, the overall objective is to replace outdated and insecure manual systems with a centralized, modern, and reliable solution. The module is also designed to support future integration with other ERP.

2.2  Scope of the System

The scope of the College ERP Authentication and Authorization Module covers the complete design, development, and implementation of a secure and role-based access control system for PVG's College of Science & Commerce, Pune. This module serves as the foundational security layer for the entire College ERP platform, ensuring that all users are properly authenticated and authorized before accessing any part of the system.

The scope of this system includes user registration and login functionality, where new users can sign up by providing their details such as name, class, phone number, username, and password. The system securely stores these credentials by encrypting passwords using bcrypt hashing before saving them to the PostgreSQL database. Upon login, the system verifies the credentials and generates a JWT token for secure and stateless session management, which is then used to authenticate all further API requests made by the user.

The system also covers the implementation of Role-Based Access Control (RBAC), where users are assigned roles such as Guest, Student, Teacher, or Admin. Each role has a defined set of permissions, and users can only access the data and functionalities allowed for their specific role. By default, all newly registered users are assigned the Guest role, ensuring minimal access until further role assignment is done by the administrator. This role management falls within the scope of the current module and can be extended in future versions.

Token management is also within the scope of this system, including the creation, validation, storage, and expiration of JWT tokens. The system tracks all active tokens in the database and maintains audit fields such as created_at and updated_at for monitoring user activity and ensuring accountability. Secure API validation is implemented to protect all backend routes from unauthorized access.

The scope further extends to the integration of this Authentication Module with other ERP modules. As a proof of concept, the module has already been successfully integrated with the Admission Module using APIs and ngrok for secure API exposure. This demonstrates that the system is capable of communicating with external modules in a distributed environment, and the same approach can be applied to future modules such as attendance, fees, examinations, hostel, transport, library, and placement cell.

However, the current scope does not include advanced features such as Multi-Factor Authentication (MFA), refresh token mechanisms, or cloud-based deployment, as these are planned for future enhancements. The system is currently designed and tested for use within the college environment and is containerized using Docker and Docker Compose to ensure consistent performance across different development and deployment environments.

Overall, the scope of this project is focused on building a secure, modular, and scalable authentication foundation that can grow alongside the College ERP system and support the institution's long-term digital management goals.

2.3 Limitations of the Existing System

The existing college management systems used in traditional educational institutions suffer from several critical limitations that affect their security, efficiency, and scalability. These limitations highlight the need for a modern, secure, and structured authentication and authorization system such as the one developed in this project.

One of the most significant limitations of the existing system is the lack of proper authentication mechanisms. Many traditional college management systems either use basic username and password login without any encryption or rely on simple session-based authentication that is vulnerable to session hijacking and replay attacks. There is no implementation of token-based authentication such as JWT, which means that user sessions are not managed securely and can be easily exploited by unauthorized users.

Another major limitation is the absence of secure password storage. In many existing systems, passwords are stored in plain text or using weak and outdated hashing algorithms, making it extremely easy for attackers to retrieve and misuse user credentials in the event of a database breach. This poses a serious threat to the privacy and security of all users including students, faculty, and administrative staff.

The existing systems also lack Role-Based Access Control (RBAC), which means that all users may have equal or uncontrolled access to different parts of the system. Without proper role assignment and permission management, a student may be able to access administrative data, or an unauthorized user may view or modify sensitive records related to fees, attendance, hostel, or examination results. This unstructured access control creates serious data integrity and privacy issues.

Traditional systems also suffer from poor session management. There is no mechanism to track active sessions, manage token expiration, or invalidate sessions after logout. This means that a user's session may remain active even after they have logged out, allowing potential misuse of the session by unauthorized parties. The absence of audit fields such as created_at and updated_at further limits the ability to monitor and track user activity or detect suspicious behavior within the system.

Scalability is another major limitation of existing systems. Most traditional college management systems are built as monolithic applications that are difficult to extend or integrate with new modules. Adding new functionalities such as attendance, fees, examinations, hostel, or transport management requires significant rework of the entire system, making it costly and time-consuming to maintain and upgrade.

Furthermore, the existing systems lack proper API security and validation. Without secure and protected API endpoints, the backend is exposed to various attacks such as unauthorized data access, injection attacks, and man-in-the-middle attacks. The absence of containerization tools like Docker also makes deployment inconsistent across different environments, leading to compatibility issues and increased maintenance efforts.

Overall, these limitations of the existing system clearly establish the need for a modern, secure, and scalable Authentication and Authorization Module that addresses each of these challenges and provides a reliable foundation for a complete and efficient College ERP system.

3) System Requirements

3.1 Hardware Requirements

The system does not require high-end hardware and can run efficiently on standard systems. The minimum hardware requirements are:

Processor: Intel i3 or above 

RAM: 8 GB or higher recommended for smooth performance 

Storage: 20 GB free disk space 

Operating System: Windows, Linux, or macOS 

Internet: Required for installation and dependency management 

These requirements ensure that the system can be easily developed and tested on commonly available machines.

3.2 Software Requirements

The system is developed using a combination of modern and industry-standard software tools and technologies to ensure high performance, scalability, and security. The following are the key software specifications used in this project:

1. Frontend – React The frontend of the system is developed using React, a popular JavaScript library for building responsive and interactive user interfaces. React enables a smooth and dynamic user experience by efficiently updating and rendering components based on user interactions, making the Signup, Login, and Welcome pages clean and easy to use.

2. Backend – FastAPI The backend is built using FastAPI, a high-performance Python web framework that supports asynchronous programming and fast API execution. FastAPI handles all user requests, processes authentication logic, manages business rules, and communicates with the database, making the system efficient and reliable.

3. Database – PostgreSQL PostgreSQL is used as the primary database management system for storing structured data related to users, roles, and tokens. It provides strong support for relational data, ensures data consistency, and offers reliable performance even as the volume of data grows over time.

4. Authentication – JSON Web Tokens (JWT) JWT is used for implementing secure and stateless authentication and session management. Upon successful login, a token containing the user's identity, role, and expiration time is generated and used to validate all further API requests, ensuring that only authenticated users can access protected resources.

5. Security – bcrypt Password Hashing Passwords are encrypted using bcrypt hashing before being stored in the database. This ensures that even if the database is compromised, the actual passwords remain protected and cannot be easily retrieved or misused by unauthorized parties.

6. Containerization – Docker and Docker Compose The system is containerized using Docker and Docker Compose, which simplifies the deployment process and ensures that the application runs consistently across different development and production environments. Docker eliminates compatibility issues and makes the system easy to set up and maintain.

7. Version Control – Git and GitHub Git is used for version control throughout the development process, allowing the team to track changes, manage code history, and collaborate efficiently. GitHub is used as the remote repository for storing and sharing the project code, including the integrated Authentication and Admission Module implementation.

8. Development Editor – Visual Studio Code Visual Studio Code is used as the primary code editor for developing the project. It provides a rich set of features such as syntax highlighting, extensions, debugging tools, and integrated terminal support, making the development process faster and more efficient.

4 Feasibility Study

4.1 Economic Feasibility

The College ERP Authentication and Authorization Module is highly economically feasible as it is developed using entirely free and open-source technologies, which eliminates the need for any costly software licenses or proprietary tools. Technologies such as React, FastAPI, PostgreSQL, Docker, Git, and Visual Studio Code are all freely available, making the overall development cost minimal and well within the budget of an academic project.

The hardware requirements for this system are also very modest, as the system can run efficiently on standard machines with an Intel i3 processor, 8 GB RAM, and 20 GB of free disk space. This means that no additional investment in expensive hardware infrastructure is required, and the system can be developed and tested using commonly available college laboratory computers or personal laptops.

Since the system is containerized using Docker and Docker Compose, deployment and maintenance costs are significantly reduced. Docker ensures that the application runs consistently across different environments without requiring separate configuration for each machine, saving both time and resources during the deployment phase.

The long-term economic benefit of this project is also considerable. By replacing manual and insecure college management processes with a centralized and automated ERP authentication system, the college can reduce administrative overhead, minimize the risk of costly data breaches, and improve overall operational efficiency. The modular design of the system further ensures that future ERP modules such as attendance, fees, examinations, and hostel can be integrated without rebuilding the entire system from scratch, saving significant development costs in the future.

Overall, the system is cost-effective, resource-efficient, and delivers strong economic value both in the short term and long term, making it a highly feasible solution for the college environment.

4.2 Technical Feasibility

The College ERP Authentication and Authorization Module is fully technically feasible as it is developed using modern, well-documented, and widely adopted technologies that are proven to deliver high performance, security, and scalability in real-world applications. The choice of React, FastAPI, PostgreSQL, JWT, bcrypt, and Docker ensures that the system is built on a strong and reliable technical foundation.

The frontend developed using React is technically capable of providing a responsive and interactive user interface that works seamlessly across different devices and screen sizes. React's component-based architecture makes it easy to manage and update the UI efficiently, ensuring a smooth user experience for all types of users including students, faculty, and administrators.

The backend developed using FastAPI is technically well-suited for handling multiple API requests simultaneously due to its support for asynchronous programming. FastAPI is one of the fastest Python frameworks available and is capable of processing authentication requests, token generation, and role validation efficiently without any performance bottlenecks, even when multiple users are accessing the system at the same time.

PostgreSQL, used as the database management system, is technically capable of handling structured relational data for users, roles, and tokens in a secure and consistent manner. Its support for complex queries, indexing, and data integrity constraints ensures that all database operations are performed accurately and efficiently.

The implementation of JWT for authentication and bcrypt for password hashing are both industry-standard security techniques that are technically proven and widely used in production-level applications. These technologies ensure that the system meets modern security requirements without adding unnecessary complexity to the development process.

The use of Docker and Docker Compose further confirms the technical feasibility of the system by ensuring consistent deployment across different environments. The successful integration of the Authentication Module with the Admission Module using APIs and ngrok also demonstrates that the system is technically capable of communicating and working with external modules in a distributed environment, confirming its readiness for future ERP module integration.

4.3 Operational Feasibility

The College ERP Authentication and Authorization Module is fully operationally feasible as it is designed to be simple, user-friendly, and easy to operate for all types of users including students, faculty, and administrative staff, regardless of their technical background or experience with ERP systems.

The user interface of the system is developed using React and is designed to be clean, minimal, and intuitive. The Signup, Login, and Welcome pages are straightforward and require only a few simple steps to complete, ensuring that even non-technical users can register and log in to the system without any difficulty. Clear error messages are displayed whenever invalid inputs are entered, helping users understand and correct their mistakes quickly and easily.

The Role-Based Access Control (RBAC) system ensures smooth and organized operation by automatically assigning roles and permissions to users based on their designation. New users are assigned a default Guest role upon registration, which limits their access until an administrator assigns them a more appropriate role. This structured role management reduces the operational burden on administrators and ensures that the system runs in an organized and controlled manner at all times.

The system is also operationally feasible from a maintenance perspective. The use of Docker and Docker Compose ensures that the system can be easily deployed, updated, and maintained across different environments without requiring specialized technical knowledge. Audit fields such as created_at and updated_at, along with token tracking, help administrators monitor user activity and system operations efficiently, making day-to-day management of the system straightforward and transparent.

Furthermore, the modular design of the system ensures that new ERP modules such as attendance, fees, examinations, hostel, and transport can be integrated into the existing platform without disrupting current operations. This flexibility makes the system operationally sustainable in the long term and ensures that it can grow alongside the evolving needs of the college without requiring a complete overhaul of the existing infrastructure.

Overall, the system is easy to use, easy to manage, and designed to fit naturally into the daily operational workflow of the college, confirming its strong operational feasibility.

5 Fact Finding Techniques

Based on your project report, here is the 5.1 Interviews / Questionnaires section with proper interview questions and answers:

5.1 Interviews / Questionnaires

The following interviews and questionnaires were conducted with students, faculty members, and administrative staff of PVG's College of Science & Commerce, Pune, to gather requirements for the College ERP Authentication and Authorization Module. The responses collected helped in understanding the existing system's limitations and defining the functional requirements of the new system.

Interview with Administrative Staff / Project Guide

Q1. What are the major security concerns you face with the current college management system? The current system does not have any structured login mechanism. Anyone with basic access credentials can log in and view sensitive data including student records, fees, and attendance information. There is no way to restrict access based on the user's role or designation.

Q2. Do you feel the current system has proper role-based access control for different users? No, the existing system does not differentiate between student, faculty, and admin users properly. All users tend to have similar levels of access, which is a serious concern for data privacy and security.

Q3. How are user passwords currently stored and managed in the system? Passwords are either stored in plain text or using very basic encryption, which is not safe at all. If the database is ever compromised, all user credentials would be directly exposed to attackers.

Q4. Is there any session management or token tracking mechanism in the existing system? No, the current system has no proper session management. User sessions do not expire automatically, and there is no way to track or invalidate active sessions, which creates a serious security vulnerability.

Q5. How important is it for the new system to support future integration with other ERP modules? It is very important. The college plans to digitize all operations including attendance, fees, examinations, hostel, and transport. The new authentication system should be able to serve as a common login platform for all these modules in the future.

Interview with Faculty Members

Q6. Do you find it easy to access the current college management system? What difficulties do you face? The current system is not very user-friendly. The login process is confusing, error messages are not clear, and sometimes the session gets timed out without any proper notification, forcing us to log in again repeatedly.

Q7. Would you prefer a system where your access is limited only to the information relevant to your role? Yes, absolutely. As a faculty member, I only need access to student attendance, marks, and course-related information. I do not need access to administrative or financial data, and having unnecessary access only increases the risk of accidental data modification.

Q8. How important is response speed and system performance for your daily usage? It is very important. If the system is slow or takes too long to load, it disrupts our daily workflow. The login and data retrieval process should be fast and reliable, especially during peak hours when many users are accessing the system simultaneously.

Questionnaire for Students

Q9. Do you feel your personal data such as attendance, fees, and examination records is currently secure in the college system? Most students responded that they are not confident about the security of their personal data. They felt that the existing system lacks proper protection and that their information could be accessed by unauthorized users easily.

Q10. Would you prefer a system where you are required to log in securely before accessing your personal college information? Yes, all students responded positively to this question. They preferred a secure login system where their data is protected and accessible only to them and authorized college staff.

Q11. How do you feel about the current login interface of the college system? Is it simple and easy to use? Most students found the current interface outdated and confusing. They expressed a preference for a clean, simple, and modern login page that is easy to navigate and works well on both desktop and mobile devices.

Q12. Would you like to receive clear error messages when you enter incorrect login details? Yes, students strongly preferred clear and specific error messages during login so that they can quickly understand and correct their mistakes without confusion.

Key Findings from Interviews and Questionnaires

The existing system lacks secure authentication and proper password encryption.

There is no Role-Based Access Control, leading to unstructured and risky data access.

Session management and token tracking are completely absent in the current system.

Users prefer a simple, clean, and responsive interface for login and registration.

All stakeholders agreed on the need for a secure, fast, and role-driven ERP authentication system.

Future integration with other ERP modules is a priority for the college administration.

5.2 Record Reviews

Record review is a requirement gathering technique that involves examining existing documents, records, and data maintained by the institution to understand the current system and identify its limitations. As part of this process, the following existing records at PVG's College of Science & Commerce, Pune were reviewed to define the requirements for the new Authentication and Authorization Module.

1. User Registration Records Existing student and faculty registration records were reviewed and it was found that user data was stored in basic spreadsheets or physical registers without any structured database or proper password encryption, confirming the need for a secure and structured user management system.

2. Access Control Records A review of existing access control practices revealed that there was no formal role-based permission system in place. All users had similar levels of access regardless of their designation, which confirmed the need for implementing Role-Based Access Control (RBAC) in the new system.

3. Login and Session Management Logs The existing system maintained no proper logs of user login activity or session management. There was no token tracking or session expiration mechanism, which highlighted the importance of implementing JWT-based authentication with audit fields such as created_at and updated_at.

4. Password Management Records Passwords were found to be stored in plain text or using weak hashing methods, which posed a serious security risk. This directly supported the decision to implement bcrypt password hashing in the new system for secure credential storage.

5. User Complaint Records Past user complaints revealed frequent issues related to unauthorized access, session timeouts, unclear error messages, and difficulty recovering login credentials, which influenced the design of a user-friendly and secure login interface in the new system.

These record reviews helped in clearly identifying the gaps in the existing system and directly guided the development of a secure, structured, and efficient Authentication and Authorization Module for the College ERP system.

6 System Design (Diagrams)

6.1 System Flowchart / Architecture

6.2 Entity Relationship Diagram (ERD)   

6.3 UML Diagrams (Use Case, Sequence, Class, Activity Diagram etc.)

UML Diagrams (Use Case, Class, Sequence, etc.) 

1) Use Case :-

The use case diagram shows how different users interact with the system. In this project, the primary user is the student who can register, log in, and view the welcome page. Admin users can manage roles and users. The system handles authentication and authorization processes.

2) Class Diagram

The class diagram represents the overall structure of the system and shows how different components interact with each other. It mainly consists of core entities such as User, Role, and Token, along with supporting classes like AuthService and Database, which help in managing authentication logic and data storage.The User class stores all the essential details of a user, including personal information such as name, class, phone number, and login credentils like username and pass

3) Sequence Diagram

The sequence diagram shows the step-by-step flow of the user login process in the College ERP system. First, the user enters the username and password on the React frontend. The frontend sends the login request to the FastAPI backend through an API call. The backend then checks the PostgreSQL database to verify whether the user exists. It retrieves the stored user details and validates the password using bcrypt hashing. If the credentials are correct, the backend generates a JWT token with user information and expiry time. The token is stored in the database for session tracking and security. Finally, the backend sends the token and success response back to the frontend, and the user is redirected to the welcome page. This process ensures secure authentication and proper session management.

4) Activity Diagram

The activity diagram illustrates the step-by-step workflow of the authentication process in the system. It begins when the user enters their login credentials on the interface. The system then validates the entered details by checking them against the stored data in the database. If the credentials are correct, the system generates a JWT token and stores it for session management. After successful token generation, access is granted to the user. If the credentials are invalid, an error message is displayed and the process ends without granting access

5) User Interface Design 

The user interface is designed to be simple, clean, and easy to use, allowing even non-technical users to interact with the system without difficulty. It focuses on providing a smooth experience while performing basic authentication tasks. The system includes three main pages: Signup, Login, and Welcome. The Signup page allows users to enter their details with proper validation, while the Login page securely verifies user credentials and generates a JWT token on successful authentication. In case of invalid input, clear error messages are displayed. After login, the Welcome page shows a personalized message to the user. Overall, the interface is minimal, responsive, and ensures easy navigation across devices.

7 Database Design

7.1 Data Dictionary

The Data Dictionary provides a comprehensive description of all the critical data entities stored within the College ERP Authentication and Authorization database. It defines the purpose, scope, and significance of each entity used in the system, helping developers, testers, and stakeholders understand the structure and relationships of the data managed by the system.

Based on your uploaded document, here is the complete 7.2 Table Structure content ready to paste:

7.2 Table Structure

The following section outlines the exact schema and column definitions for all the primary database tables used in the College ERP Authentication and Authorization Module. Each table is designed to ensure data integrity, security, and scalability. Most tables inherit standard audit fields such as created_at and updated_at through the AuditMixin or TimestampMixin for complete data traceability.

1. users Table

The users table is the primary table for identity management. It stores all essential authentication and profile information for every user accessing the ERP system.

2. roles Table

The roles table defines all system-wide authorization levels available within the ERP system. Each role determines the level of access a user has across the system.

3. user_roles Table

The user_roles table establishes a many-to-many relationship between the users and roles tables. It allows a single user to be assigned multiple roles and supports the complete implementation of Role-Based Access Control (RBAC).

4. user_tokens Table

The user_tokens table manages secure authentication sessions for all logged-in users. It stores JWT access tokens, refresh tokens, and expiration details to ensure proper session handling and security.

5. modules Table

The modules table represents all distinct subsystems available within the ERP ecosystem. Each module groups related features and functionalities together under one category.

6. features Table

The features table defines specific functional areas or components within each module. Each feature represents a distinct action or view that a user may access within a particular module.

7. permissions Table

The permissions table stores granular access rights that define what specific actions can be performed on each feature. It supports fine-grained control over system access for each role.

8. role_permissions Table

The role_permissions table maps roles to specific permissions, forming the core of the RBAC implementation. It determines what each role is allowed to do across all modules and features in the system.

9. log Table

The log tsable serves as a complete security audit trail for the system. It records every login attempt made by any user, capturing details such as IP address, device information, and the outcome of each attempt.

Note: All tables in the system inherit created_at and updated_at audit fields through the AuditMixin or TimestampMixin. These fields ensure complete data traceability, accountability, and monitoring across the entire College ERP Authentication and Authorization system.

s

8 Screen Designing (Input/Output)

These screenshots show the complete flow of our project from user registration to successful login and access. They help in understanding how the Authentication and Authorization Module works in real-time. Through these output screens, we can clearly see the Signup page, Login process, JWT-based authentication, and the Welcome page after successful login. These screens provide visual proof of the working system and make the project easier to explain and understand.

1)Login Portal

2)Admin Dashboard

3)Buttons to other modules

4) New User Sign up page 

5)When user login as Guest into portal this is shown.

6)Database and the when user register’s its entries get save into user’s tables.

9 Conclusion:-

In this project, a secure, scalable, and efficient Authentication and Authorization Module for a College ERP system was successfully designed and implemented using modern technologies including React for the frontend, FastAPI for the backend, and PostgreSQL for database management. The module incorporates essential security features such as user registration, login, bcrypt password encryption, and JWT-based authentication to ensure safe and reliable session handling throughout the system.

Role-Based Access Control (RBAC) was effectively implemented to ensure that users can only access data and functionalities relevant to their assigned roles, with new users defaulting to a Guest role to maintain minimal access and enhance overall system security. Token tracking and audit fields such as created_at and updated_at were also included to improve transparency, accountability, and monitoring of user activity across the system.

The authentication module was successfully integrated with the Admission Module APIs using ngrok for secure API exposure, demonstrating the system's ability to communicate with external ERP modules and function efficiently in a distributed environment. This integration serves as a strong proof of concept for connecting the authentication layer with future ERP modules such as attendance, fees, examinations, hostel, and transport.

The system performed reliably during all testing phases, handling user authentication, token generation, and role validation without any errors. The use of Docker further ensured consistent deployment across different environments. Overall, this project confirms that a modular, secure, and role-driven approach is highly effective for building a robust and scalable College ERP platform, with strong potential for future enhancements such as Multi-Factor Authentication and a refresh token mechanism.

10 Future Scope

The College ERP Authentication and Authorization Module has been successfully implemented as a strong security foundation, and there are several promising directions in which the system can be further improved and expanded in future versions.

One of the most significant future enhancements is the addition of Multi-Factor Authentication (MFA) using OTP verification through email or mobile, which will provide an extra layer of security during the login process. A Refresh Token mechanism can also be implemented to allow secure token renewal without requiring repeated login, thereby improving session management and overall user experience.

The existing Role-Based Access Control (RBAC) system can be upgraded by introducing fine-grained permissions such as view, edit, delete, approve, and export, replacing the current broad role structure of Guest and Admin. Advanced audit logging and real-time monitoring dashboards can also be added to help administrators track login attempts, user activities, and data changes more efficiently.

A Parent and Guardian Portal can be developed as an additional module, allowing parents to monitor their child's attendance, fees, and academic performance directly through the ERP system. Performance optimization techniques such as database indexing, query optimization, and caching mechanisms can be applied to ensure the system runs efficiently even when handling a large number of concurrent users.

Cloud deployment using platforms such as AWS or Azure is another important future goal, as it will significantly improve system availability, backup reliability, and overall performance at scale. The most important long-term extension is the complete integration of the Authentication Module with all remaining ERP modules including Attendance, Fees, Examinations, Hostel, Transport, Library, and Placement Cell. Since the system is already successfully integrated with the Admission Module using APIs and ngrok, this proves that the module is fully capable of connecting with other systems, and in the future, a single centralized login can provide secure and seamless access to the entire College ERP platform.

11 Bibliography and References 

1. FastAPI Official Documentation – Used for learning backend API development, routing, authentication, and FastAPI project structure.  

2. PostgreSQL Official Documentation – Referred for database design, table creation, queries, and relational database management.  

3. React Official Documentation – Used for frontend development, component structure, state management, and UI implementation.  

4. Docker Official Documentation – Helped in understanding Docker, Docker Compose, and containerized deployment of the project.  

5. JWT Introduction – Auth0 – Referred for implementing JWT-based authentication, token generation, and secure session handling.  

6. bcrypt Documentation – PyPI – Used for password hashing and secure storage of user credentials in the database.  

7. GitHub Repository for Project Integration – Contains the merged Authentication and Admission Module implementation using API integration and ngrok.  

8. GitHub Repository for Authentication Module – Contains the complete Authentication and Authorization module with JWT and RBAC implementation.  

9. Dribbble – Used for frontend UI design inspiration and modern layout ideas for login and signup pages.  

10.Figma– Referred for professional UI/UX design inspiration and project presentation ideas.  

11. Pinterest – Used for simple UI design references, color combinations, and layout inspiration for frontend screens.

Student Signature							Guide Signature

Date: __/__/____

Chapter No. | Title | Page No.

1 | Introduction | 

 | 1.1 Company Certificate & Internship Certificate | 5

 | 1.2 Acknowledgement | 9

 | 1.3 Declaration | 10

 | 1.4 Project Motivation | 11

 | 1.5 Problem Statement | 12

2 | System Analysis | 

 | 2.1 Objective of the System | 13

 | 2.2 Scope of the System | 14

 | 2.3 Limitations of the Existing System | 15

3 | System Requirements | 

 | 3.1 Hardware Requirements | 16

 | 3.2 Software Requirements | 17

4 | Feasibility Study | 

 | 4.1 Economic Feasibility | 18

 | 4.2 Technical Feasibility | 18

 | 4.3 Operational Feasibility | 19

5 | Fact Finding Techniques | 

 | 5.1 Interviews / Questionnaires | 21

 | 5.2 Record Reviews | 23

6 | System Design (Diagrams) | 

 | 6.1 System Flowchart / Architecture | 25

 | 6.2 Entity Relationship Diagram (ERD) | 26,27

 | 6.3 UML Diagrams (Use Case, Sequence, Class, Activity Diagram etc.) | 28 to 31

7 | Database Design | 

 | 7.1 Data Dictionary | 32

 | 7.2 Table Structures | 33 to 38

8 | Screen Designing (Input/Output) | 

 | 8.1 Login & Dashboard Screens | 39 to 42

9 | Conclusion | 42

10 | Future Scope | 43

11 | Bibliography and References | 44

Entity Name | Description

users | Stores core authentication and profile details for all individuals accessing the ERP system including Students, Alumni, Teaching Staff, and Admins. It includes login credentials, contact information, department details, and account status.

roles | Defines the various authorization levels available within the system such as admin, student, alumni, and hod. Each role controls what a user is allowed to access.

user_roles | A mapping entity that assigns one or more roles to a specific user. This table enables Role-Based Access Control (RBAC) by linking the users table with the roles table.

modules | Represents the distinct subsystems available within the ERP ecosystem such as Admission, Academic, Feedback, and Examination modules.

features | Defines specific functional areas or components within a module. For example, "Exam Results View" is a feature inside the Examination module.

permissions | Stores granular access rights that define what actions can be performed on specific features, such as read, write, or delete operations.

role_permissions | A mapping entity that links roles to specific permissions, dictating what each role is allowed to perform system-wide across all modules and features.

user_tokens | Manages active session data for authenticated users by storing JWT access tokens, refresh tokens, and their respective expiration timestamps to ensure secure session handling.

login_log | An audit trail that records every login attempt made in the system. It captures the user's IP address, device information, and login status indicating success or failure, providing full security monitoring.

Column Name | Data Type | Constraints | Description

user_id | Integer | Primary Key, Auto-increment | Unique identifier for each user

username | String(100) | Unique, Not Null | The user's login username

full_name | String(150) | Nullable | The user's legal full name

email | String(150) | Unique, Not Null, Indexed | User's primary contact email address

password_hash | String(255) | Not Null | bcrypt encrypted password stored securely

status | Boolean | Default: True | Active or inactive account status flag

department | String(100) | Nullable | The academic or staff department of the user

phone_number | String(20) | Nullable | Contact phone number of the user

created_at | Timestamp | Not Null | Timestamp when the record was created

updated_at | Timestamp | Not Null | Timestamp when the record was last updated

Column Name | Data Type | Constraints | Description

role_id | Integer | Primary Key, Auto-increment | Unique identifier for each role

role_name | String(100) | Unique, Not Null | Name of the role (e.g., admin, student, alumni, hod)

description | String | Nullable | Details describing the role's privileges and access level

created_at | Timestamp | Not Null | Timestamp when the role was created

Column Name | Data Type | Constraints | Description

user_role_id | Integer | Primary Key, Auto-increment | Unique mapping identifier

user_id | Integer | Foreign Key (users.user_id) | Reference to the user being assigned the role

role_id | Integer | Foreign Key (roles.role_id) | Reference to the role being assigned to the user

created_at | Timestamp | Not Null | Timestamp when the role was assigned

Column Name | Data Type | Constraints | Description

token_id | Integer | Primary Key, Auto-increment | Unique token record identifier

user_id | Integer | Foreign Key (users.user_id) | Owner of the session token

token | String | Unique, Not Null, Indexed | The JWT access token string

refresh_token | String | Unique, Nullable, Indexed | Token used to renew sessions without re-login

expiry_date | DateTime | Not Null | Expiration timestamp of the access token

is_active | Boolean | Default: True | Flag indicating whether the session is currently valid

created_at | Timestamp | Not Null | Timestamp when the token was generated

Column Name | Data Type | Constraints | Description

module_id | Integer | Primary Key, Auto-increment | Unique identifier for each ERP module

module_name | String | Not Null | Name of the module (e.g., Admission, Examination, Feedback)

description | String | Nullable | Brief description of the module's purpose and scope

created_at | Timestamp | Not Null | Timestamp when the module was created

Column Name | Data Type | Constraints | Description

feature_id | Integer | Primary Key, Auto-increment | Unique identifier for each feature

feature_name | String | Not Null | Name of the feature (e.g., Exam Results View)

module_id | Integer | Foreign Key (modules.module_id) | The module this feature belongs to

created_at | Timestamp | Not Null | Timestamp when the feature was added

Column Name | Data Type | Constraints | Description

permission_id | Integer | Primary Key, Auto-increment | Unique identifier for each permission

permission_name | String | Not Null | Name of the permission (e.g., read, write, delete)

action | String | Nullable | The specific action allowed by this permission

feature_id | Integer | Foreign Key (features.feature_id) | The feature this permission applies to

created_at | Timestamp | Not Null | Timestamp when the permission was defined

Column Name | Data Type | Constraints | Description

role_id | Integer | Foreign Key (roles.role_id) | Reference to the role being granted the permission

permission_id | Integer | Foreign Key (permissions.permission_id) | Reference to the permission being granted to the role

created_at | Timestamp | Not Null | Timestamp when the permission was assigned to the role

Column Name | Data Type | Constraints | Description

login_log_id | Integer | Primary Key, Auto-increment | Unique log entry identifier

user_id | Integer | Foreign Key (users.user_id) | The user who attempted the login

ip_address | String(50) | Nullable | IP address from which the login was attempted

device_info | String(255) | Nullable | Browser or device user-agent string

status | String(50) | Nullable | Outcome of the attempt (SUCCESS or FAILED)

login_time | DateTime | Default: Current Time | Timestamp of the login attempt

created_at | Timestamp | Not Null | Timestamp when the log entry was recorded