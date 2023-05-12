# Cascade CMS Sync, todo items, requests, and pending bug fixes.

- Check permissions of directories, do not upload files if a parent directory is not world readable
- Provide for a DONT_IGNORE variable in config.py that will add the file even if it would have been otherwise ignored, example: .htaccess files should be transfered.
