
# My Personal API

This is a personal API built with Python, FastAPI, and SQLAlchemy. It provides public endpoints for stories, opinions, and videos, as well as admin endpoints for managing the content.

## Features

- **Public API:** Exposes endpoints for retrieving stories, opinions, and videos.
- **Admin API:** Provides secure endpoints for creating, updating, and deleting content.
- **File Uploads:** Supports file uploads for cover images, videos, and other media.
- **Database:** Uses SQLite for local development and can be configured for other databases.
- **Authentication:** Secures admin endpoints with JWT-based authentication.

## Getting Started

### Prerequisites

- Python 3.8+
- Pip

### Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment:**

   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

To run the application, use the following command:

```bash
fastapi dev main.py
```

The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

The API is divided into two main sections: public and admin.

### Public API

The public API is available under the `/api/v1/public/` prefix. It provides read-only access to the following resources:

- `/stories`: Get all stories.
- `/stories/{slug}`: Get a single story by its slug.
- `/opinions`: Get all opinions.
- `/opinions/{slug}`: Get a single opinion by its slug.
- `/videos`: Get all videos.
- `/videos/{slug}`: Get a single video by its slug.

### Admin API

The admin API is available under the `/api/v1/admin/` prefix. It requires authentication and provides endpoints for managing the content.

- `/auth/token`: Get an authentication token.
- `/admins`: Manage admin users.
- `/stories`: Manage stories.
- `/opinions`: Manage opinions.
- `/videos`: Manage videos.

## File Uploads

To upload files to the admin endpoints, you need to use a client that supports `multipart/form-data` requests. You can use tools like `curl` or a GUI-based API client like Postman or Insomnia.

When creating or updating a resource that includes a file (e.g., a video with a cover image and video file), you need to send the file as a separate part of the multipart request.

For example, to create a new video with a cover image and a video file, you would send a `POST` request to `/api/v1/admin/videos/` with the following fields:

- `title`: The title of the video.
- `slug`: The slug of the video.
- `description`: The description of the video.
- `cover_image`: The cover image file.
- `video`: The video file.

The API will save the files to the `static` directory and store the file paths in the database.
