import uvicorn
import os


def main():
    uvicorn.run("app.app:app", host='0.0.0.0', port=4567, reload=True, log_level='info', workers=os.cpu_count())


if __name__ == "__main__":
    main()
