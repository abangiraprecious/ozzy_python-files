# Django Basics — Beginner Study Guide

> Rebuilt from class notes for self-study. A few things in the original notes were typos or slightly wrong (mostly the HTTP status codes and one point about apps). Wherever I corrected something, you'll see a **📝 Note from the notes** callout so you know what changed and why.

---

## 1. Python and How We Get Extra Tools

There are two common ways to work with Python:

1. **Plain Python** — the standard installation.
2. **Anaconda distribution** — Python bundled with many extra packages already included (popular for data science).

Python on its own can't do everything. When you need a tool (a "package") that doesn't come built in, you install it using **pip**, Python's package installer.

```
pip install <package-name>
```

Think of pip as an app store for Python code.

### Web frameworks you can install

A *web framework* is a package that gives you a ready-made structure for building websites. Common Python ones:

- **Django** — highly structured and very reliable (this is what we're learning)
- **Flask** — lighter and more flexible
- **Pyramid**
- **Web2py**

None of these come with Python by default; you install them with pip.

---

## 2. What Makes Django Special

Django is **highly structured** — it follows a fixed set of guidelines and conventions about where things go and how they connect. That structure feels strict at first, but it means once you learn the pattern, every Django project looks familiar.

Installing Django is a **one-time installation** on your machine. After that, you can create as many projects as you want.

```
pip install django
```

---

## 3. Creating Your First Django Project (Step by Step)

### Step 1 — Install Django

```
pip install django
```

### Step 2 — Choose a folder for your projects

Pick (or create) a folder on your computer where your projects will live, then open a command line **inside that folder**:

- Open the folder in your file explorer.
- Click into the address/path bar.
- Type `cmd` and press Enter — this opens the command prompt already pointed at that folder.

From here on, you type commands into this window.

> **Helpful command:** `dir` lists everything inside the current folder (on Mac/Linux the equivalent is `ls`). Use it any time you're not sure what's around you.

### Step 3 — Create the project

A *project* is the master folder where all your instructions live.

```
python -m django startproject <name_of_project>
```

- You create one project at a time.
- Django ships with its own built-in web server, so you don't need to install one separately.

Now move **into** the project folder:

```
cd <name_of_project>
```

Then start the development server:

```
python manage.py runserver
```

A computer that runs both a server and a web browser is called a **local host** — it's serving pages to itself.

Open your browser and visit either of these to see your site:

```
127.0.0.1:8000
localhost:8000
```

To stop the server, go back to the command window and press **Ctrl + C**.

### Step 4 — Create an application inside the project

An **application (app)** is a self-contained unit of functionality. Examples of functionalities: login, registration, reporting, and so on.

```
python manage.py startapp <name_of_app>
```

> **📝 Note from the notes:** The original notes said both "can create one or more applications" and "each project takes one application" — those contradict each other. The correct version is: **a single project can contain many apps.** That's actually the whole point of the app system — you split a big project into smaller, focused apps (one for login, one for reports, etc.). Your HTML files for an app live inside that app's folder.

### Step 5 — Install (register) the app

Creating an app isn't enough; you have to tell the project it exists by registering it in the settings file (more on that file next). Until you do, Django ignores it.

---

## 4. Understanding the Project Structure

When you create a project, Django auto-generates a folder **with the same name as your project**. This is called the **configuration folder**, and it comes with several files already inside it. Here's what they're for:

| File | What it does |
|------|--------------|
| `settings.py` | The main control panel for your project (explained below). |
| `urls.py` | The "address book" — maps web addresses to the code that handles them. |
| `wsgi.py` and `asgi.py` | Used for API (Application Programming Interface) work and deployment — how your app talks to the outside world. |
| `manage.py` | The command tool you keep using (`runserver`, `startapp`, `migrate`, etc.). Lives just outside the config folder. |

### Key things inside `settings.py`

- **`BASE_DIR`** — points to the exact location of your project folder on disk, so Django can find files reliably.
- **`SECRET_KEY`** — every Django project is created with a unique secret key used for security. Keep it private.
- **`DEBUG = True`** — when `True`, Django shows detailed error pages that help you find and fix problems. When you set it to `False`, errors are hidden and no debugging clues appear. Keep it `True` while learning; switch it to `False` only when the site goes live to the public.
- **`ALLOWED_HOSTS`** — lets you restrict which server(s) are allowed to run your application.
- **`INSTALLED_APPS`** — the list of apps in use. This includes apps that **come bundled with Django**, so you don't have to download them. Registering your own app (Step 5) means adding it here.
- **`MIDDLEWARE`** — a chain of components that lets Django keep track of and process each request/response as it passes through your application.

---

## 5. Setting Up the Database

Django stores data in tables made of **rows and columns** (like a spreadsheet).

Here's the important idea: **all the current functionalities need one or more database tables to store their information.** For example, a login functionality needs a registration functionality behind it, and registration needs somewhere to store users.

Before you can use the apps that come bundled with Django, you have to create the database tables they rely on. The command that does this is:

```
python manage.py migrate
```

**`migrate`** activates (creates) the database tables for your installed apps. Run it early, and run it again whenever your data structures change.

---

## 6. Templates — Serving HTML Pages

In Django, **HTML files are called templates.**

By default, Django expects to find them in a folder named `templates`. Create that folder and put your `.html` files inside it so Django knows where to look.

---

## 7. How a Web Server and Web Browser Talk to Each Other

This is the mental model behind everything above.

### Ports

A web server has several entry points called **ports**. Ports are what the operating system uses to route incoming page requests. Django's development server uses port **8000** by default — that's why the address is `localhost:8000`.

### Status codes (the server's replies)

When your browser asks for a page, the server answers with a numeric **status code** describing what happened:

| Code | Meaning | When it happens |
|------|---------|-----------------|
| **200** | OK | The page exists and access is granted. Everything worked. |
| **404** | Not Found | The requested page doesn't exist. |
| **403** | Forbidden | You asked for a restricted page you're not allowed to see. |
| **408** | Request Timeout | The server was too busy / the request took too long. |
| **500** | Internal Server Error | Something is broken on the server side (e.g. a syntax error in the code). |

> **📝 Note from the notes:** The original notes used **300** for both "restricted page" and "request timeout," and said 500 means "the page was requested many times." Those are mixed up. The corrected versions are in the table above: **403** for a forbidden/restricted page, **408** for a timeout, and **500** for an internal server/code error (nothing to do with how many times it was requested). The `3xx` codes are actually about *redirects*, not restrictions.

---

## 8. HTTP Methods — GET, POST, DELETE

> **📝 Note from the notes:** The notes call this the "HTTPS protocol." The methods below are **HTTP** methods. HTTPS is just the *secure* (encrypted) version of HTTP — same methods, extra security. Good to know the difference, but the methods work the same way.

When a browser talks to a server, it uses a **method** to say what it wants to do:

- **GET** — "Give me a page." The browser sends a GET request; the server replies with the page and a status code (like 200) or an error. This is the default way pages are fetched.
- **POST** — "Here's some data, please store it." When you fill in a form and submit it, the browser sends the form data to the server (and on to the database). That submission is a POST request. A successful POST is confirmed with a 200.
- **DELETE** — "Remove this thing." The browser asks the server to delete something.

A rough order of events: a GET usually happens first (you load the page with the form), *then* a POST happens (you submit the form).

---

## 9. URLs and Views — How a Request Finds Its Code

This ties the whole request cycle together.

- A request always **starts with a `/`**. Typing `/something` means "I want the page at `something`."
- That request is sent to **`urls.py`**, the address book of your project.
- In `urls.py` you **define a path**: you match a URL to the code that should handle it.
- The code that handles a request is called a **view**. A **view is a function that returns a web page in response to a request.**

The rule to remember:

> **Every page needs its own view and its own URL.**

So the flow is:

```
Browser types  /something
        ↓
urls.py  matches "/something" to a view
        ↓
view function  runs and returns a page
        ↓
Browser  displays the page (with status code 200 if all went well)
```

---

## Quick Command Cheat Sheet

```bash
pip install django                          # install Django (one time)
python -m django startproject myproject     # create a project
cd myproject                                # move into it
python manage.py startapp myapp             # create an app
python manage.py migrate                    # set up database tables
python manage.py runserver                  # start the dev server
# visit localhost:8000 in the browser
# Ctrl + C to stop the server
```

---

## The Big Picture (in one paragraph)

You install Django once with pip. You create a **project** (the master folder), and inside it one or more **apps** (units of functionality like login or reports). The **configuration folder** holds `settings.py`, where you register your apps, control `DEBUG`, and manage security. You prepare storage by running **`migrate`**, which builds the **database tables**. Your HTML **templates** live in a `templates` folder. When a browser requests `/something`, **`urls.py`** matches that address to a **view** (a function), which returns the page — and the server reports how it went with a **status code** like 200 (OK) or 404 (Not Found). That request-to-response loop is the heartbeat of every Django site.