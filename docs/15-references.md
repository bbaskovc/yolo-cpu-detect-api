# References

This project uses external interfaces as compatibility targets. The implementation must be validated against the current official documentation at the time of development and release.

## OpenAI API conventions

- OpenAI API authentication overview: `https://developers.openai.com/api/reference/overview#authentication`
- OpenAI images and vision guide: `https://developers.openai.com/api/docs/guides/images-vision`
- OpenAI Responses API reference: `https://developers.openai.com/api/reference/responses`

## Notes

The official OpenAI documentation demonstrates bearer authentication and Base64 data URL image input for both Chat Completions `image_url` and Responses `input_image`. This project intentionally implements only the smallest useful compatible subset and imposes stricter rules: one image, Base64 data URL only, no remote URLs, no file IDs, no storage, no background execution, and no streaming.

When this repository reaches implementation, treat documentation versions as a verification input rather than immutable truth. Update the compatibility matrix if upstream client contracts materially change.
