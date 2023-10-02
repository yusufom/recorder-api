# Recorder API

The **Recorder API** is a Django application that allows you to create, save, and retrieve video files received from any screen recording chrome extension. This application creates recordings, merge recording chunks, transcribe the merged video, and get the compiled video for a specific video ID.

## Endpoints

### Create Video (POST)

- Create a new video record.
- Method: POST
- Endpoint: `https://recorder-api.onrender.com/api/create/`
- Response: JSON containing the created video ID.

Example Request:
```bash
curl -X POST https://recorder-api.onrender.com/api/create/
```

Example Response:
```json
{
    "id": 14
}
```

### Append Video Chunk (POST)

- Append a video chunk to an existing video.
- Method: PUT
- Endpoint: `https://recorder-api.onrender.com/api/save-data/<video_id>/`
- Request Body: Video chunk data in binary format.
- Response: JSON with a success message.

For the first chunk:
```json
{
    "message": "Recording(s) saved successfully!"
}
```

For subsequent chunks:
```json
{
    "message": "Recording(s) saved successfully!"
}
```

### Merge Video Chunk (POST)

- Append a video chunk to an existing video.
- Method: POST
- Endpoint: `https://recorder-api.onrender.com/api/merge-data/<video_id>/`
- Response: JSON with a success message.

For the first chunk:
```json
{
    "message": "Video files is currently being merged."
}
```

### Get Video (GET)

- Retrieve the compiled video for a specific video ID.
- Method: GET
- Endpoint: `https://recorder-api.onrender.com/api/<video_id>/`
- Response: JSON with a data message..

Example Request:
```bash
curl https://recorder-api.onrender.com/api/53/
```

Example Response
```json
{
   "status": "success",
    "message": "Video fetched successfully!",
    "data": {
        "id": 53,
        "name": "2bbb3478-12b9-428a-9b63-b5d13f7a0a43",
        "title": null,
        "transcript": null,
        "video": "/media/videos/video_53.webm",
        "is_completed": false,
        "is_transcript_completed": false,
        "created_at": "2023-10-01T19:50:15.024237Z"
    }
}
```

## Usage

1. Create a new video record using the "Create Video" endpoint. Note the returned `video_id`.

2. Append video chunks to the video using the "Append Video Chunk" endpoint. Ensure you include the `video_id` in the URL.

4. Merge the video chunks together with the Merge video endpoint which will operates in the background, Ensure you include the `video_id` of the video to be merged in the url.

3. Once all video chunks are appended, you can retrieve the compiled video using the "Get Video" endpoint with the `video_id`.

## Deployment

The API has been deployed and can be accessed at the following base URL:
- Base URL: `https://recorder-api.onrender.com`

## Known Limitations and Assumptions

- This API does not implement authentication or authorization.
- Video files are not appended sequentially, they are appending once the merge data endpoint is triggered (Once user stops recording)
- It takes time to append video chunks