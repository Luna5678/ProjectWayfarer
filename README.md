<h1>Project Wayfarer</h1>
<p>Wayfarer is a web application where people can share tips about their travel locations around the world. It builds a community for people seeking to travel or craving to learn about the art and architectures around the world. Users can create posts to share their travel tips and highlights. Users also have their own profile page, which shows their information and their history of posts in descending order.</p>

<h2>Live Link: http://wayfarer-art-app.herokuapp.com/</h2>

<h2>Team</h2>
<p>Lonna Lu</p>
<p>Jon Ver Cabral Dela Cruz</p>
<p>Gerald Tiamzon</p>
<p>Sergio Laguardia</p>

<p>We created this website in sprints. Each sprint is broken down by major functionalities. We individually programmed and pair-programmed to tackle complex issues together. We communicated on design and dissected each sprint into technical milestones to track our progress as a team.</p>

<h2>Technologies Used</h2>
<p>Django, Python, Heroku, PostgreSQL, Heroku, Bootstrap, CSS for custom styles, Github for change control.</p>

<h2>User Stories</h2>
<h3>Sprint 1: Basic Auth and Profiles</h3>
A user should be able to:
<ol>
    <li>Navigate to "/" and see a basic splash page with:
        <ul>
            <li>The name of the website.</li>
            <li>Links to "Log In" and "Sign Up".</li>
        </ul>
    </li>
    <li>Sign up for an account.</li>
    <li>Log in to their account if they already have one.</li>
    <li>Be redirected to their public profile page after logging in.</li>
    <li>On their public profile page, see their name, the current city they have set in their profile, and their join date.</li>
    <li>See the site-wide header on every page with:
        <ul>
            <li>A link to "Log Out" if they're logged in.</li>
            <li>Links to "Log In" and "Sign Up" if they're logged out.</li>
        </ul>
    </li>
    <li>Update their profile by making changes to their name and/or current city.</li>
    <li>See the titles of all the posts they've contributed (start with pre-seeded data).</li>
    <li>Click on the title of one of their posts and be redirected to a "show" page for that post.</li>
    <li>View post "show" pages with title, author, and content.</li>
</ol>

<h3>Sprint 2: Full CRUD</h3>
A user should be able to:
<ol>
    <li>View the "San Francisco" page (at "/cities/1") including:
        <ul>
            <li>The site-wide header.</li>
            <li>The name of the city.</li>
            <li>An iconic photo of the city.</li>
        </ul>
    </li>
    <li>View a list of posts on the San Francisco page:
        <ul>
            <li>Sorted by newest first.</li>
            <li>With the post titles linked to the individual post "show" pages.</li>
        </ul>
    </li>
    <li>Use an "Add New Post" button on the San Francisco city page to pull up the new post form.</li>
    <li>Create a new post for San Francisco.</li>
    <li>Click "Edit" on ANY individual post, and be redirected to the edit form.</li>
    <li>Click "delete" on ANY individual post, then:
        <ul>
            <li>See a pop-up that says: "Are you sure you want to delete #{title}?"</li>
            <li>If the user confirms, delete the post.</li>
        </ul>
    </li>
</ol>

<h3>Sprint 3: Validations and Authorization</h3>
A user should be able to:
<ol>
    <li>View city pages for "London" and "Gibraltar".</li>
    <li>Verify that a new post they create is successfully published on the correct city page.</li>
    <li>A user CANNOT save invalid data to the database, according to the following rules:
        <ul>
            <li>A post's title must be between 1 and 200 characters.</li>
            <li>A post's content must not be empty.</li>
        </ul>
    </li>
    <li>A user is authorized to perform certain actions on the site, according to the following rules:
        <ul>
            <li>A user MUST be logged in to create/update/destroy resources.</li>
            <li>A user may only edit/delete their own posts.</li>
            <li>A user may only edit their own profile</li>
        </ul>
    </li>
</ol>

<h3>To-Do's for Future Iterations</h3>
<ol>
    <li>A user CANNOT sign up with an email (or username) that is already in use.</li>
    <li>Allow a user to view another user's profile</li>
</ol>

<h2>Wireframe</h2>
<p>This wireframe was provided to us from the "client" and we arranged daily meetings to ask questions about the wireframe and functionality. Through those daily meetings, we gathered more information, which allowed us to build the website based off our notes.</p>
<img src="https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F96d7485d-f97e-4dfd-a26e-e7341d5f8818%2Fwireframes.png?table=block&id=ff181223-40d4-4e3f-a4dd-743dec886ec5&spaceId=2d8bbfbe-92b6-4c51-aa43-e64c639c7655&width=2830&userId=&cache=v2" alt="Wayfarer Wireframe Diagram" />
