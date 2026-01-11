# FastAPI Content API Documentation

This document provides detailed information about the API, including authentication, available endpoints, and usage examples.

## Authentication

All `POST` and `DELETE` endpoints under the `/api/v1/admin/` path are protected and require a valid JSON Web Token (JWT) to be included in the request headers.

- **Header Name**: `Authorization`
- **Header Value**: `Bearer <YOUR_JWT_TOKEN>`

A token can be obtained by authenticating against the `/api/v1/auth/login` endpoint.

---

## Endpoints

### Authentication

#### 1. Login

- **Endpoint**: `POST /api/v1/auth/login`
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

---

### Stories

The following endpoints are for managing stories. Admin authentication is required.

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
  ```json
  {
    "id": 1,
    "title": "New Story Title",
    "slug": "new-story-title",
    "cover_image": "http://example.com/image.jpg",
    "content": "This is the full content of the story.",
    "author": "Author Name",
    "is_published": false,
    "is_featured": false
  }
  ```

#### 2. Delete a Story

- **Endpoint**: `DELETE /api/v1/admin/stories/{story_id}`
- **Description**: Deletes a story by its ID.
- **Response**: The deleted story object.

---

### Opinions

The following endpoints are for managing opinions. Admin authentication is required.

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

---

### Videos

The following endpoints are for managing videos. Admin authentication is required.

#### 1. Create a Video

- **Endpoint**: `POST /api/v1/admin/videos/`
- **Description**: Creates a new video entry.
- **Request Body**:
  ```json
  {
    "title": "New Video Title",
    "slug": "new-video-title",
    "cover_image": "http://example.com/image.jpg",
    "content": "This is the video embed code or description.",
    "author": "Author Name",
    "is_published": false,
    "is_featured": false
  }
  ```
- **Response**: The newly created video object, including its `id`.

#### 2. Delete a Video

- **Endpoint**: `DELETE /api/v1/admin/videos/{video_id}`
- **Description**: Deletes a video by its ID.
- **Response**: The deleted video object.
