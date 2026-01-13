
# FastAPI Content API Documentation

This document provides detailed information about the API, including authentication, available endpoints, and usage examples.

## Authentication

All `POST`, `PUT`, and `DELETE` endpoints under the `/api/v1/admin/` path are protected and require a valid JSON Web Token (JWT) to be included in the request headers.

- **Header Name**: `Authorization`
- **Header Value**: `Bearer <YOUR_JWT_TOKEN>`

A token can be obtained by authenticating against the `/api/v1/admin/auth/login` endpoint.

## CORS (Cross-Origin Resource Sharing)

The API has CORS enabled to allow requests from any origin. This is configured in the main application file (`main.py`) and can be customized as needed.

---

## Public Endpoints

These endpoints are publicly accessible and do not require authentication.

### Stories

#### 1. Get All Stories

- **Endpoint**: `GET /api/v1/public/stories/`
- **Description**: Retrieves a list of all published stories.
- **Query Parameters**:
    - `skip` (optional, default: 0): The number of stories to skip.
    - `limit` (optional, default: 100): The maximum number of stories to return.
- **Response**: A list of story objects.

#### 2. Get a Story by Slug

- **Endpoint**: `GET /api/v1/public/stories/{slug}`
- **Description**: Retrieves a single published story by its slug.
- **Response**: The story object.

### Opinions

#### 1. Get All Opinions

- **Endpoint**: `GET /api/v1/public/opinions/`
- **Description**: Retrieves a list of all published opinions.
- **Query Parameters**:
    - `skip` (optional, default: 0): The number of opinions to skip.
    - `limit` (optional, default: 100): The maximum number of opinions to return.
- **Response**: A list of opinion objects.

#### 2. Get an Opinion by Slug

- **Endpoint**: `GET /api/v1/public/opinions/{slug}`
- **Description**: Retrieves a single published opinion by its slug.
- **Response**: The opinion object.

### Videos

#### 1. Get All Videos

- **Endpoint**: `GET /api/v1/public/videos/`
- **Description**: Retrieves a list of all published videos.
- **Query Parameters**:
    - `skip` (optional, default: 0): The number of videos to skip.
    - `limit` (optional, default: 100): The maximum number of videos to return.
- **Response**: A list of video objects.

#### 2. Get a Video by Slug

- **Endpoint**: `GET /api/v1/public/videos/{slug}`
- **Description**: Retrieves a single published video by its slug.
- **Response**: The video object.

---

## Admin Endpoints

These endpoints require admin authentication.

### Authentication

#### 1. Login

- **Endpoint**: `POST /api/v1/admin/auth/login`
- **Description**: Authenticates an admin user and returns a JWT token.
- **Request Body** (as `application/x-www-form-urlencoded`):
  - `username`: The admin's email address.
  - `password`: The admin's password.
- **Response**:
  ```json
  {
    "access_token": "your_jwt_token",
    "token_type": "bearer"
  }
  ```

### Admins

#### 1. Create an Admin

- **Endpoint**: `POST /api/v1/admin/admins/`
- **Description**: Creates a new admin user.
- **Request Body**:
  ```json
  {
    "name": "Admin Name",
    "email": "admin@example.com",
    "password": "your_secret_password"
  }
  ```
- **Response**: The newly created admin object.

### Stories

#### 1. Get All Stories
- **Endpoint**: `GET /api/v1/admin/stories/`
- **Description**: Retrieves all stories (published and unpublished).
- **Response**: A list of all story objects.

#### 2. Get a Story by Slug
- **Endpoint**: `GET /api/v1/admin/stories/{slug}`
- **Description**: Retrieves a single story by its slug.
- **Response**: The story object.

#### 3. Create a Story
- **Endpoint**: `POST /api/v1/admin/stories/`
- **Description**: Creates a new story.
- **Request Body** (`multipart/form-data`):
    - `title`: The title of the story.
    - `slug`: The slug for the story URL.
    - `content`: The main content of the story.
    - `author`: The author's name.
    - `cover_image`: The cover image file to upload.
    - `main_photo`: The main photo file to upload.
    - `is_published`: `true` or `false`.
    - `is_featured`: `true` or `false`.
- **Response**: The newly created story object.

#### 4. Update a Story
- **Endpoint**: `PUT /api/v1/admin/stories/{slug}`
- **Description**: Updates a story by its slug.
- **Request Body** (`multipart/form-data`):
    - `title`: (Optional) The updated title.
    - `slug`: (Optional) The updated slug.
    - `content`: (Optional) The updated content.
    - `author`: (Optional) The updated author.
    - `cover_image`: (Optional) A new cover image file.
    - `main_photo`: (Optional) A new main photo file.
    - `is_published`: (Optional) `true` or `false`.
    - `is_featured`: (Optional) `true` or `false`.
- **Response**: The updated story object.

#### 5. Delete a Story
- **Endpoint**: `DELETE /api/v1/admin/stories/{slug}`
- **Description**: Deletes a story by its slug.
- **Response**: The deleted story object.

### Opinions

#### 1. Get All Opinions
- **Endpoint**: `GET /api/v1/admin/opinions/`
- **Description**: Retrieves all opinions (published and unpublished).
- **Response**: A list of all opinion objects.

#### 2. Get an Opinion by Slug
- **Endpoint**: `GET /api/v1/admin/opinions/{slug}`
- **Description**: Retrieves a single opinion by its slug.
- **Response**: The opinion object.

#### 3. Create an Opinion
- **Endpoint**: `POST /api/v1/admin/opinions/`
- **Description**: Creates a new opinion piece.
- **Request Body** (`multipart/form-data`):
    - `title`: The title of the opinion.
    - `slug`: The slug for the opinion URL.
    - `content`: The main content of the opinion.
    - `author`: The author's name.
    - `cover_image`: The cover image file to upload.
    - `main_photo`: The main photo file to upload.
    - `is_published`: `true` or `false`.
    - `is_featured`: `true` or `false`.
- **Response**: The newly created opinion object.

#### 4. Update an Opinion
- **Endpoint**: `PUT /api/v1/admin/opinions/{slug}`
- **Description**: Updates an opinion by its slug.
- **Request Body** (`multipart/form-data`):
    - `title`: (Optional) The updated title.
    - `slug`: (Optional) The updated slug.
    - `content`: (Optional) The updated content.
    - `author`: (Optional) The updated author.
    - `cover_image`: (Optional) A new cover image file.
    - `main_photo`: (Optional) A new main photo file.
    - `is_published`: (Optional) `true` or `false`.
    - `is_featured`: (Optional) `true` or `false`.
- **Response**: The updated opinion object.

#### 5. Delete an Opinion
- **Endpoint**: `DELETE /api/v1/admin/opinions/{slug}`
- **Description**: Deletes an opinion by its slug.
- **Response**: The deleted opinion object.

### Videos

#### 1. Get All Videos
- **Endpoint**: `GET /api/v1/admin/videos/`
- **Description**: Retrieves all videos.
- **Response**: A list of all video objects.

#### 2. Get a Video by Slug
- **Endpoint**: `GET /api/v1/admin/videos/{slug}`
- **Description**: Retrieves a single video by its slug.
- **Response**: The video object.

#### 3. Create a Video
- **Endpoint**: `POST /api/v1/admin/videos/`
- **Description**: Creates a new video entry.
- **Request Body** (`multipart/form-data`):
    - `title`: The title of the video.
    - `slug`: The slug for the video URL.
    - `author`: The author's name.
    - `cover_image`: The cover image file to upload.
    - `video`: The video file to upload.
    - `is_published`: `true` or `false`.
    - `is_featured`: `true` or `false`.
- **Response**: The newly created video object.

#### 4. Update a Video
- **Endpoint**: `PUT /api/v1/admin/videos/{slug}`
- **Description**: Updates a video by its slug.
- **Request Body** (`multipart/form-data`):
    - `title`: (Optional) The updated title.
    - `slug`: (Optional) The updated slug.
    - `author`: (Optional) The updated author.
    - `cover_image`: (Optional) A new cover image file.
    - `video`: (Optional) A new video file.
    - `is_published`: (Optional) `true` or `false`.
    - `is_featured`: (Optional) `true` or `false`.
- **Response**: The updated video object.

#### 5. Delete a Video
- **Endpoint**: `DELETE /api/v1/admin/videos/{slug}`
- **Description**: Deletes a video by its slug.
- **Response**: The deleted video object.
