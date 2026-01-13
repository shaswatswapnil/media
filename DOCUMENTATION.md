# FastAPI Content API Documentation

This document provides detailed information about the API, including authentication, available endpoints, and usage examples.

## Authentication

All `POST`, `PUT`, and `DELETE` endpoints under the `/api/v1/admin/` path are protected and require a valid JSON Web Token (JWT) to be included in the request headers.

- **Header Name**: `Authorization`
- **Header Value**: `Bearer <YOUR_JWT_TOKEN>`

A token can be obtained by authenticating against the `/api/v1/admin/auth/login` endpoint.

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
- **Request Body**:
  ```json
  {
    "title": "New Story Title",
    "slug": "new-story-title",
    "cover_image": "http://example.com/image.jpg",
    "content": "This is the full content of the story.",
    "author": "Author Name",
    "is_published": false,
    "is_featured": false
  }
  ```
- **Response**: The newly created story object.

#### 4. Update a Story
- **Endpoint**: `PUT /api/v1/admin/stories/{slug}`
- **Description**: Updates a story by its slug.
- **Request Body**:
  ```json
  {
    "title": "Updated Story Title",
    "slug": "updated-story-title",
    "cover_image": "http://example.com/updated_image.jpg",
    "content": "This is the updated content of the story.",
    "author": "Author Name",
    "is_published": true,
    "is_featured": true
  }
  ```
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
- **Request Body**:
  ```json
  {
    "title": "New Opinion Title",
    "slug": "new-opinion-title",
    "cover_image": "http://example.com/image.jpg",
    "content": "This is the full content of the opinion.",
    "author": "Author Name",
    "is_published": false,
    "is_featured": false
  }
  ```
- **Response**: The newly created opinion object.

#### 4. Update an Opinion
- **Endpoint**: `PUT /api/v1/admin/opinions/{slug}`
- **Description**: Updates an opinion by its slug.
- **Request Body**:
  ```json
  {
    "title": "Updated Opinion Title",
    "slug": "updated-opinion-title",
    "cover_image": "http://example.com/updated_image.jpg",
    "content": "This is the updated content of the opinion.",
    "author": "Author Name",
    "is_published": true,
    "is_featured": true
  }
  ```
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
- **Request Body**:
  ```json
  {
    "title": "New Video Title",
    "slug": "new-video-title",
    "cover_image": "http://example.com/video_cover.jpg",
    "content": "This is the description or content for the video.",
    "author": "Video Creator Name",
    "is_published": false,
    "is_featured": false
  }
  ```
- **Response**: The newly created video object.

#### 4. Update a Video
- **Endpoint**: `PUT /api/v1/admin/videos/{slug}`
- **Description**: Updates a video by its slug.
- **Request Body**:
  ```json
  {
    "title": "Updated Video Title",
    "slug": "updated-video-title",
    "cover_image": "http://example.com/new_video_cover.jpg",
    "content": "This is the updated description for the video.",
    "author": "Video Creator Name",
    "is_published": true,
    "is_featured": true
  }
  ```
- **Response**: The updated video object.

#### 5. Delete a Video
- **Endpoint**: `DELETE /api/v1/admin/videos/{slug}`
- **Description**: Deletes a video by its slug.
- **Response**: The deleted video object.
