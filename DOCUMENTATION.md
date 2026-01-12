# FastAPI Content API Documentation

This document provides detailed information about the API, including authentication, available endpoints, and usage examples.

## Authentication

All `POST` and `DELETE` endpoints under the `/api/v1/admin/` path are protected and require a valid JSON Web Token (JWT) to be included in the request headers.

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

#### 2. Get a Story by ID

- **Endpoint**: `GET /api/v1/public/stories/{story_id}`
- **Description**: Retrieves a single story by its ID.
- **Response**: The story object.

### Opinions

#### 1. Get All Opinions

- **Endpoint**: `GET /api/v1/public/opinions/`
- **Description**: Retrieves a list of all published opinions.
- **Query Parameters**:
    - `skip` (optional, default: 0): The number of opinions to skip.
    - `limit` (optional, default: 100): The maximum number of opinions to return.
- **Response**: A list of opinion objects.

#### 2. Get an Opinion by ID

- **Endpoint**: `GET /api/v1/public/opinions/{opinion_id}`
- **Description**: Retrieves a single opinion by its ID.
- **Response**: The opinion object.

### Videos

#### 1. Get All Videos

- **Endpoint**: `GET /api/v1/public/videos/`
- **Description**: Retrieves a list of all published videos.
- **Query Parameters**:
    - `skip` (optional, default: 0): The number of videos to skip.
    - `limit` (optional, default: 100): The maximum number of videos to return.
- **Response**: A list of video objects.

#### 2. Get a Video by ID

- **Endpoint**: `GET /api/v1/public/videos/{video_id}`
- **Description**: Retrieves a single video by its ID.
- **Response**: The video object.

---

## Admin Endpoints

These endpoints require admin authentication.

### Authentication

#### 1. Login

- **Endpoint**: `POST /api/v1/admin/auth/login`
- **Description**: Authenticates an admin user and returns a JWT token.
- **Request Body**:
  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }
  ```
- **Response**:
  ```json
  {
    "access_token": "your_jwt_token",
    "token_type": "bearer"
  }
  ```

### Stories

#### 1. Create a Story

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
- **Response**: The newly created story object, including its `id`.

#### 2. Delete a Story

- **Endpoint**: `DELETE /api/v1/admin/stories/{story_id}`
- **Description**: Deletes a story by its ID.
- **Response**: The deleted story object.

### Opinions

#### 1. Create an Opinion

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
- **Response**: The newly created opinion object, including its `id`.

#### 2. Delete an Opinion

- **Endpoint**: `DELETE /api/v1/admin/opinions/{opinion_id}`
- **Description**: Deletes an opinion by its ID.
- **Response**: The deleted opinion object.

### Videos

#### 1. Create a Video

- **Endpoint**: `POST /api/v1/admin/videos/`
- **Description**: Creates a new video entry.
- **Request Body**:
  ```json
  {
    "title": "New Video Title",
    "url": "http://example.com/video.mp4"
  }
  ```
- **Response**: The newly created video object, including its `id`.

#### 2. Delete a Video

- **Endpoint**: `DELETE /api/v1/admin/videos/{video_id}`
- **Description**: Deletes a video by its ID.
- **Response**: The deleted video object.
